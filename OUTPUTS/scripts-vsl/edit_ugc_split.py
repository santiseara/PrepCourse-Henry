"""Edición de anuncio UGC corto (Scented Stones, inglés) con el estilo de los ads de referencia de Descargas
("Qué pasa cuando", "Mirá ni debería", "Si tu hijo", "Toda mamá necesita").
Uso: python3 edit_ugc_split.py <heygen.mp4> <carpeta_trabajo> <salida.mp4>
La carpeta de trabajo tiene brolls/, sfx/ y fonts/ (Arial Black).

Estilo copiado de las referencias:
- avatar a pantalla completa, alternada con PANTALLA DIVIDIDA: avatar arriba y B-roll abajo,
  unidos con un degradé suave (sin línea de corte);
- subtítulos de 2 palabras, blanco con borde negro, a la altura del pecho;
- headline corto en ROJO con borde negro, en MAYÚSCULAS, arriba de la cabeza, con "pop" al entrar;
- música suave por debajo, "pop" en cada headline, "cha-ching" con la plata, whoosh al entrar el B-roll.
"""
import sys, os, json, subprocess, unicodedata, difflib

FF = os.path.expanduser('~/bin/ffmpeg')
SPEED = 1.1
GAP_MAX, GAP_KEEP = 0.40, 0.18
SPLIT_Y, FADE = 900, 220           # dónde empieza el B-roll y alto del degradé
CAP_Y = 1400                        # centro de los subtítulos (como en las referencias, ~73 %)
HEAD_Y = 200                        # borde superior del headline (frente / arriba de la cabeza)

src, wd, out = sys.argv[1:4]
work = os.path.join(wd, 'edit'); os.makedirs(work, exist_ok=True)
BR, SFX, FONTS = (os.path.join(wd, x) for x in ('brolls', 'sfx', 'fonts'))

GUION = """This box of twelve scented stones cost me about six dollars to make. Tomorrow morning, it turns into a hundred and twenty.
It's for a bridal shower. The bride's mom saw one at my sister's house and messaged me on WhatsApp.
I made them right here, on this table, on Tuesday night. Plaster, a few drops of fragrance oil and a silicone mold. No oven. By morning, they were ready.
Six months ago, I'd never made anything with my hands. Now my orders come from people who smelled one somewhere. No Instagram, no website.
And they come back, because the scent lasts for weeks and then fades.
Everything I know is from Emma Carter's Scented Stones Method. Short PDF, dirt cheap. I made it back with my very first order.
Link's below. Next week, your first box could be sitting on your kitchen table."""

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-3000:]); sys.exit(1)

def duration(path):
    s = subprocess.run([FF, '-i', path], capture_output=True, text=True).stderr.split('Duration: ')[1].split(',')[0]
    h, m, x = s.split(':'); return int(h) * 3600 + int(m) * 60 + float(x)

def transcribe(path, cache):
    if os.path.exists(cache):
        return json.load(open(cache))
    from faster_whisper import WhisperModel
    wav = cache + '.wav'
    run([FF, '-v', 'error', '-y', '-i', path, '-ac', '1', '-ar', '16000', wav])
    m = WhisperModel('small', device='cpu', compute_type='int8')
    segs, _ = m.transcribe(wav, language='en', word_timestamps=True, beam_size=5, initial_prompt=GUION)
    words = [{'w': w.word.strip(), 's': w.start, 'e': w.end} for s in segs for w in s.words]
    json.dump(words, open(cache, 'w'), ensure_ascii=False)
    return words

def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    return ''.join(c for c in s if c.isalnum() and unicodedata.category(c) != 'Mn')

# ---------- Pasada 1: recorte de silencios ----------
words0 = transcribe(src, os.path.join(work, 'words0.json'))
dur0 = duration(src)
keep, cur_s = [], 0.0
for a, b in zip(words0, words0[1:]):
    if b['s'] - a['e'] > GAP_MAX:
        keep.append((cur_s, a['e'] + GAP_KEEP / 2)); cur_s = b['s'] - GAP_KEEP / 2
keep.append((cur_s, min(dur0, words0[-1]['e'] + 0.5)))
print(f'silencios: {len(keep) - 1} cortes')

def mapt(t):
    acc = 0.0
    for (a, b) in keep:
        if t < a: return acc
        if t <= b: return acc + (t - a)
        acc += b - a
    return acc

trimmed = os.path.join(work, 'trimmed.mp4')
if not os.path.exists(trimmed):
    expr = '+'.join(f'between(t,{a:.3f},{b:.3f})' for a, b in keep)
    open(os.path.join(work, 'sel.txt'), 'w').write(
        f"[0:v]select='{expr}',setpts=N/FRAME_RATE/TB,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920[v];"
        f"[0:a]aselect='{expr}',asetpts=N/SR/TB[a]")
    run([FF, '-v', 'error', '-y', '-i', src, '-filter_complex_script', os.path.join(work, 'sel.txt'),
         '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-crf', '15', '-preset', 'fast', '-r', '30',
         '-c:a', 'aac', '-b:a', '192k', trimmed])

# tiempos ya en el video final (recorte + velocidad)
words = [{'w': w['w'], 's': mapt(w['s']) / SPEED, 'e': mapt(w['e']) / SPEED} for w in words0]
# el texto de los subtítulos sale del guion (Whisper se equivoca en nombres y números)
gt = GUION.split()
a_, b_ = [norm(w['w']) for w in words], [norm(x) for x in gt]
for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a_, b_, autojunk=False).get_opcodes():
    if op in ('equal', 'replace') and i2 - i1 == j2 - j1:   # también 'equal', para tomar la puntuación del guion
        for i, j in zip(range(i1, i2), range(j1, j2)):
            words[i]['w'] = gt[j]
total = mapt(dur0) / SPEED
N = [norm(w['w']) for w in words]

def find(phrase, end=False):
    for alt in phrase.split('|'):
        toks = [t for t in (norm(x) for x in alt.split()) if t]
        for i in range(len(N) - len(toks) + 1):
            if N[i:i + len(toks)] == toks:
                return words[i + len(toks) - 1]['e'] if end else words[i]['s']
    print('NO ENCONTRADO:', phrase); return None

# ---------- B-rolls en pantalla dividida: (clip, frase donde entra, frase donde sale, segundo del clip) ----------
# Cada recorte es un plano distinto del clip: no se repite, no se congela, no se estira.
PLAN = [
    ('assembling', 'this box of twelve', 'to make', 0.0),       # arranca con visual
    ('crafting', 'tomorrow morning', 'hundred and twenty', 5.0),  # la plata en mano
    ('wedding', 'its for a bridal', 'bridal shower', 0.0),
    ('stirring', 'plaster a few', 'few drops', 0.5),
    ('making', 'of fragrance oil', 'fragrance oil', 0.0),
    ('making', 'and a silicone', 'silicone mold', 2.0),
    ('crafting', 'by morning', 'were ready', 3.0),
    ('unpacking', 'people who smelled', 'one somewhere', 0.0),
    ('assembling', 'because the scent', 'and then fades', 4.0),
    ('wedding', 'i made it back', 'very first order', 4.0),
]
brolls = []
for name, p1, p2, ss in PLAN:
    a, b = find(p1), find(p2, end=True)
    if a is None or b is None: continue
    a = max(0.0, a - 0.08) if a > 0.3 else 0.0
    b = b + 0.15
    if brolls and a - brolls[-1][2] < 0.5:      # si queda un hueco mínimo, se pega al anterior
        brolls[-1] = (brolls[-1][0], brolls[-1][1], a, brolls[-1][3])
    f = os.path.join(BR, name + '.mp4')
    d = min(b - a, duration(f) - ss)
    brolls.append((f, a, a + d, ss))

# ---------- Headlines (rojo, mayúsculas) + efectos ----------
HEAD = [
    ('six dollars', '$6 TO MAKE', 'pop'),
    ('a hundred and twenty', '$120 TOMORROW', 'chaching'),
    ('bridal shower', 'BRIDAL SHOWER ORDER', 'pop'),
    ('no oven', 'NO OVEN', 'pop'),
    ('six months ago', 'NEVER MADE ANYTHING', 'pop'),
    ('no instagram', 'NO INSTAGRAM. NO WEBSITE.', 'pop'),
    ('they come back', 'THEY COME BACK', 'pop'),
    ('scented stones method', 'SCENTED STONES METHOD', 'pop'),
    ('dirt cheap', 'SHORT PDF, DIRT CHEAP', 'pop'),
    ('very first order', 'PAID BACK ON ORDER #1', 'chaching'),
    ('links below', 'LINK BELOW', 'pop'),
]
heads, sfx = [], []
for k, (p, txt, fx) in enumerate(HEAD):
    t = find(p)
    if t is None: continue
    heads.append([t, txt, fx])
for k, h in enumerate(heads):
    nxt = heads[k + 1][0] if k + 1 < len(heads) else total
    h.append(min(h[0] + 2.4, nxt - 0.05, total))
for t, txt, fx, e in heads:
    sfx.append((fx + '.wav', t, 0.55 if fx == 'pop' else 0.9))
for i, (f, a, b, ss) in enumerate(brolls):   # whoosh solo cuando entra un bloque de B-roll nuevo
    if a > 0.1 and (i == 0 or a - brolls[i - 1][2] > 0.05):
        sfx.append(('whoosh.wav', max(0, a - 0.12), 0.35))

# ---------- Subtítulos de 2 palabras + headlines (ASS) ----------
def ts(t): return f'{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}'
ev = []
i = 0
while i < len(words):
    grp = [words[i]]
    if i + 1 < len(words) and words[i]['w'][-1:] not in '.,?!' and len(words[i]['w'] + words[i + 1]['w']) <= 16:
        grp.append(words[i + 1])
    a = grp[0]['s']; i += len(grp)
    b = words[i]['s'] if i < len(words) else grp[-1]['e'] + 0.3
    b = min(b, grp[-1]['e'] + 0.4)
    txt = ' '.join(w['w'] for w in grp).upper().strip(' .,;:…"')
    txt = txt.rstrip('.,')
    if txt: ev.append(f'Dialogue: 0,{ts(a)},{ts(b)},Cap,,0,0,0,,{txt}')
for t, txt, fx, e in heads:
    ev.append(f'Dialogue: 1,{ts(t)},{ts(e)},Head,,0,0,0,,{{\\fscx70\\fscy70\\t(0,110,\\fscx108\\fscy108)\\t(110,190,\\fscx100\\fscy100)}}{txt}')
ass = os.path.join(work, 'subs.ass')
open(ass, 'w', encoding='utf-8').write(f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Arial Black,64,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,1,0,1,6,0,5,60,60,0,1
Style: Head,Arial Black,78,&H002A1AE8,&H002A1AE8,&H00000000,&H00000000,0,0,0,0,100,100,1,0,1,7,0,8,50,50,{HEAD_Y},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""" + '\n'.join(e.replace(',Cap,,0,0,0,,', f',Cap,,0,0,0,,{{\\pos(540,{CAP_Y})}}') for e in ev) + '\n')

# ---------- Máscara del degradé ----------
from PIL import Image
BH = 1920 - SPLIT_Y
mask = Image.new('L', (1080, BH), 255)
px = mask.load()
for y in range(FADE):
    v = int(255 * (0.5 - 0.5 * __import__('math').cos(3.14159 * y / FADE)))
    for x in range(1080): px[x, y] = v
mpath = os.path.join(work, 'mask.png'); mask.save(mpath)

# ---------- Pasada 2: video ----------
inputs = ['-i', trimmed, '-loop', '1', '-i', mpath]
for f, a, b, ss in brolls: inputs += ['-ss', f'{ss:.2f}', '-t', f'{(b - a) * SPEED + 0.2:.2f}', '-i', f]
fc = [f"[0:v]setpts=PTS/{SPEED},fps=30[base]", "[1:v]format=gray,split=%d%s" % (len(brolls), ''.join(f'[m{i}]' for i in range(len(brolls))))]
last = 'base'
for i, (f, a, b, ss) in enumerate(brolls):
    # el B-roll ocupa la mitad de abajo, encuadrado al centro del plano
    fc.append(f"[{2 + i}:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:{BH}:0:(ih-{BH})/2+60,fps=30,format=rgba[c{i}]")
    fc.append(f"[c{i}][m{i}]alphamerge,setpts=PTS-STARTPTS+{a:.3f}/TB[b{i}]")
    fc.append(f"[{last}][b{i}]overlay=0:{SPLIT_Y}:eof_action=pass:enable='between(t,{a:.3f},{b:.3f})'[v{i}]")
    last = f'v{i}'
assp = ass.replace(':', r'\:')
fc.append(f"[{last}]ass='{assp}':fontsdir='{FONTS}',format=yuv420p[vout]")
fc.append(f"[0:a]atempo={SPEED}[aout]")
open(os.path.join(work, 'fc.txt'), 'w').write(';\n'.join(fc))
vid = os.path.join(work, 'video_voz.mkv')
run([FF, '-v', 'error', '-y'] + inputs + ['-filter_complex_script', os.path.join(work, 'fc.txt'),
     '-map', '[vout]', '-map', '[aout]', '-t', f'{total:.2f}', '-r', '30',
     '-c:v', 'libx264', '-crf', '17', '-preset', 'medium', '-c:a', 'pcm_s16le', vid])

# ---------- Audio: voz -14 LUFS, música suave con ducking, efectos en la palabra exacta ----------
music = os.path.join(work, 'music.wav')
run(['python3', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'music.py'), f'{total + 1:.1f}', music])
ain = ['-i', vid, '-i', music]
for f, _, _ in sfx: ain += ['-i', os.path.join(SFX, f)]
af = ["[0:a]loudnorm=I=-14:TP=-1.5:LRA=11,asplit=2[voz][sc]",
      "[1:a]loudnorm=I=-31:TP=-8[mus]",
      "[mus][sc]sidechaincompress=threshold=0.03:ratio=3:attack=20:release=400[duck]"]
mix = ['[voz]', '[duck]']
for i, (f, t, g) in enumerate(sfx):
    ms = int(t * 1000)
    af.append(f"[{2 + i}:a]volume={g * 0.55:.2f},adelay={ms}|{ms}[s{i}]"); mix.append(f'[s{i}]')
af.append(''.join(mix) + f"amix=inputs={len(mix)}:normalize=0:duration=first,alimiter=limit=0.95[aout]")
open(os.path.join(work, 'af.txt'), 'w').write(';\n'.join(af))
run([FF, '-v', 'error', '-y'] + ain + ['-filter_complex_script', os.path.join(work, 'af.txt'),
     '-map', '0:v', '-map', '[aout]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-t', f'{total:.2f}',
     '-movflags', '+faststart', out])
json.dump({'brolls': [(os.path.basename(f), round(a, 2), round(b, 2), ss) for f, a, b, ss in brolls],
           'heads': [(round(t, 2), txt, round(e, 2)) for t, txt, fx, e in heads],
           'sfx': [(f, round(t, 2)) for f, t, g in sfx]}, open(os.path.join(work, 'plan.json'), 'w'), indent=1)
print('listo:', out, f'duración {total:.1f}s', 'brolls', len(brolls), 'headlines', len(heads), 'efectos', len(sfx))
