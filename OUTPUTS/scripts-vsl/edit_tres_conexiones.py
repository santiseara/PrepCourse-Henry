"""Edición del VSL de Las Tres Conexiones (Argentina, Juliana Alves).
Uso: python3 edit_tres_conexiones.py <heygen.mp4> <carpeta_trabajo> <salida.mp4>
La carpeta de trabajo tiene brolls/ (recortes de TikTok + Higgsfield), gfx/, sfx/ y fonts/.
Edición copiada del VSL de LATAM: avatar a cámara, subtítulos de a una palabra (Bangers, blanco con borde negro,
a la altura del pecho). Encima: B-rolls cortos y variados, placas de pasos/precio/garantía, música y pocos efectos. 1.3x.
"""
import sys, os, json, subprocess, unicodedata

FF = os.path.expanduser('~/bin/ffmpeg')
SPEED = 1.3
GAP_MAX, GAP_KEEP = 0.45, 0.20

src, wd, out = sys.argv[1:4]
work = os.path.join(wd, 'edit'); os.makedirs(work, exist_ok=True)
BR, GFX, SFX, FONTS = (os.path.join(wd, x) for x in ('brolls', 'gfx', 'sfx', 'fonts'))

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
    segs, _ = m.transcribe(wav, language='es', word_timestamps=True, beam_size=5)
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
keep.append((cur_s, min(dur0, words0[-1]['e'] + 0.6)))
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
         '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-crf', '16', '-preset', 'fast', '-r', '30',
         '-c:a', 'aac', '-b:a', '192k', trimmed])
words = [{'w': w['w'], 's': mapt(w['s']), 'e': mapt(w['e'])} for w in words0]
# Whisper parte números ("15" ".990") y se equivoca en algunas palabras: se unen los números
# y, si hay guion.txt en la carpeta de trabajo, se corrige el texto de los subtítulos con el guion.
merged = []
for w in words:
    if merged and w['w'][:1] in '.,' and w['w'][1:2].isdigit():
        merged[-1] = {**merged[-1], 'w': merged[-1]['w'] + w['w'], 'e': w['e']}
    else:
        merged.append(w)
words = merged
gpath = os.path.join(wd, '..', 'guion.txt')
if os.path.exists(gpath):
    import difflib
    gt = open(gpath, encoding='utf-8').read().split()
    a, b = [norm(w['w']) for w in words], [norm(x) for x in gt]
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op == 'replace' and i2 - i1 == j2 - j1:
            for i, j in zip(range(i1, i2), range(j1, j2)):
                if not any(c.isdigit() for c in words[i]['w']):
                    words[i]['w'] = gt[j]
total = mapt(dur0)
N = [norm(w['w']) for w in words]

def _hits(phrase, after):
    for alt in phrase.split('|'):
        toks = [t for t in (norm(x) for x in alt.split()) if t]
        h = [(i, len(toks)) for i in range(len(N) - len(toks) + 1) if N[i:i + len(toks)] == toks and words[i]['s'] >= after]
        if h: return h
    return []
def find(phrase, after=0.0):
    h = _hits(phrase, after)
    if not h: print('NO ENCONTRADO:', phrase); return None
    return words[h[0][0]]['s']

# ---------- B-rolls: recortes cortos, nunca el clip entero ----------
# (archivo, frase, duración en tiempo pre-1.3x, desde qué segundo del clip)
PLAN = [
    ('tt_ignora_gira', 'te ignora porque vos', 2.6, 0.0),
    ('tt_grito_brazo', 'sin gritar ni una', 2.4, 0.0),
    ('tt_ignora_boca', 'le pedís algo una vez|le pedís alguna vez', 2.6, 0.0),
    ('hf_se_va', 'segunda vez', 2.4, 1.0),
    ('tt_grito_cuna', 'ya estás gritando', 2.4, 0.2),
    ('tt_rincon_mira', 'como si la del problema', 2.6, 0.0),
    ('hf_brazos', 'no procesan órdenes', 2.6, 0.5),
    ('tt_brazos_lejos', 'le hablaba a la pared', 2.4, 0.0),
    ('tt_control_tele', 'que apagara la tele', 2.2, 0.0),
    ('hf_cuna', 'levantando la voz', 2.6, 0.5),
    ('tt_llanto_cuna', 'peor mamá del mundo', 2.4, 0.0),
    ('ai_altura', 'ponerte a su altura', 2.8, 0.3),
    ('tt_rincon_gira', 'desde otra habitación', 2.4, 0.0),
    ('ai_ojos', 'te mire a los ojos|a los ojos', 2.8, 0.3),
    ('tt_berrinche_piso', 'tu hijo se escapa', 2.4, 0.0),
    ('hf_berrinche', 'hablan solos', 2.4, 1.0),
    ('ai_juguetes', 'responder al primer pedido', 2.8, 0.5),
    ('ai_altura', 'bajá a su altura', 2.4, 2.4),
    ('ai_dormir', 'la hora de dormir', 2.6, 0.3),
    ('tt_publico', 'berrinches en público', 2.4, 0.0),
    ('ai_celular', 'listos para usar hoy', 2.8, 0.5),
    ('ai_juguetes', 'esta misma noche', 2.6, 2.3),
]
brolls = []
for name, phrase, d, ss in PLAN:
    f = os.path.join(BR, name + '.mp4'); t = find(phrase)
    if t is None or not os.path.exists(f):
        if t is not None: print('falta B-roll:', name)
        continue
    brolls.append((f, max(0, t - 0.1), min(d, duration(f) - ss), ss))

# ---------- Placas ----------
pngs, gray, sfx = [], [], []
def png(name, a, d):
    if a is not None: pngs.append((os.path.join(GFX, name), a, a + d))
t1, t2, t3 = find('primero la conexión física'), find('segundo la conexión de confirmación'), find('tercero la conexión de cierre')
png('paso1.png', t1, 2.6); png('paso2.png', t2, 2.6); png('paso3.png', t3, 2.6)
for t in (t1, t2, t3):
    if t is not None: sfx.append(('pop.wav', t, 0.8))
t_an = find('doscientos mil pesos|200000 pesos|200 000 pesos|200 mil pesos')
png('anclaje.png', t_an, 2.4)
t_p = find('quince mil novecientos noventa|15990|15 990|15 mil')
png('precio.png', t_p, 4.2)
if t_p is not None: gray.append((t_p, t_p + 4.2)); sfx.append(('chaching.wav', t_p, 1.0))
t_g = find('treinta días de garantía|30 días de garantía|treinta días|30 días')
png('garantia.png', t_g, 3.6)
if t_g is not None: sfx.append(('sello.wav', t_g, 0.9))
t_tc = find('por eso armé')
if t_tc is not None: sfx.append(('whoosh.wav', max(0, t_tc - 0.2), 0.7))
sfx.append(('ding.wav', 0.05, 0.6))

# zoom alternado por oración (suave, como "corte de cámara")
starts = [0.0] + [words[i + 1]['s'] for i in range(len(words) - 1) if words[i]['w'][-1:] in '.?!']
zoom = [(starts[i], starts[i + 1] if i + 1 < len(starts) else total) for i in range(1, len(starts), 2)]

# ---------- Subtítulos: una palabra por vez, como el original ----------
def ts(t):
    return f'{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}'
nocap = [(a, b) for f, a, b in pngs if os.path.basename(f) in ('precio.png', 'anclaje.png', 'garantia.png')]
ev = []
for i, w in enumerate(words):
    txt = w['w'].upper().strip(' .,;:…"¿?¡!')
    if not txt: continue
    a = w['s']; b = words[i + 1]['s'] if i + 1 < len(words) else w['e'] + 0.3
    b = min(b, w['e'] + 0.35)
    if b - a < 0.06: b = a + 0.06
    if any(a < y and b > x for x, y in nocap): continue
    ev.append(f'Dialogue: 0,{ts(a)},{ts(b)},Cap,,0,0,0,,{txt}')
ass = os.path.join(work, 'subs.ass')
open(ass, 'w', encoding='utf-8').write("""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Bangers,112,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,0,0,0,0,100,100,2,0,1,7,3,2,40,40,640,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""" + '\n'.join(ev) + '\n')

# ---------- Pasada 2: video ----------
def en(iv): return '+'.join(f'between(t,{a:.3f},{b:.3f})' for a, b in iv) or '0'
inputs = ['-i', trimmed]
for f, _, d, ss in brolls: inputs += ['-ss', f'{ss:.2f}', '-t', f'{d:.2f}', '-i', f]
for f, _, _ in pngs: inputs += ['-loop', '1', '-i', f]
fc = ["[0:v]split=3[base][zs][gs]",
      "[zs]scale=1190:-2,crop=1080:1920[zoom]",
      "[gs]hue=s=0,eq=contrast=1.08[gray]",
      f"[base][zoom]overlay=0:0:enable='{en(zoom)}'[v0]",
      f"[v0][gray]overlay=0:0:enable='{en(gray)}'[v1]"]
last, k = 'v1', 1
for i, (f, t, d, _) in enumerate(brolls):
    fc.append(f"[{1 + i}:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setpts=PTS-STARTPTS+{t:.3f}/TB[b{i}]")
    fc.append(f"[{last}][b{i}]overlay=0:0:eof_action=pass:enable='between(t,{t:.3f},{t + d:.3f})'[v{k + 1}]")
    last = f'v{k + 1}'; k += 1
off = 1 + len(brolls)
for j, (f, a, b) in enumerate(pngs):
    fc.append(f"[{off + j}:v]format=rgba,scale=1080:1920[p{j}]")
    fc.append(f"[{last}][p{j}]overlay=0:0:shortest=1:enable='between(t,{a:.3f},{b:.3f})'[v{k + 1}]")
    last = f'v{k + 1}'; k += 1
assp = ass.replace(':', r'\:')
fc.append(f"[{last}]ass='{assp}':fontsdir='{FONTS}',setpts=PTS/{SPEED}[vout]")
fc.append(f"[0:a]atempo={SPEED}[aout]")
open(os.path.join(work, 'fc.txt'), 'w').write(';\n'.join(fc))
vid = os.path.join(work, 'video_voz.mkv')
run([FF, '-v', 'error', '-y'] + inputs + ['-filter_complex_script', os.path.join(work, 'fc.txt'),
     '-map', '[vout]', '-map', '[aout]', '-t', f'{total / SPEED:.2f}', '-r', '30',
     '-c:v', 'libx264', '-crf', '20', '-preset', 'medium', '-pix_fmt', 'yuv420p',
     '-c:a', 'pcm_s16le', vid])

# ---------- Audio: voz -15 LUFS, música -30 con ducking, efectos en la palabra exacta ----------
fin = total / SPEED
music = os.path.join(work, 'music.wav')
run(['python3', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'music.py'), f'{fin + 1:.1f}', music])
ain = ['-i', vid, '-i', music]
for f, _, _ in sfx: ain += ['-i', os.path.join(SFX, f)]
af = ["[0:a]loudnorm=I=-15:TP=-1.5:LRA=11,asplit=2[voz][sc]",
      "[1:a]loudnorm=I=-30:TP=-6,volume=1.0[mus]",
      "[mus][sc]sidechaincompress=threshold=0.03:ratio=4:attack=20:release=400[duck]"]
mix = ['[voz]', '[duck]']
for i, (f, t, g) in enumerate(sfx):
    ms = int(t / SPEED * 1000)
    af.append(f"[{2 + i}:a]volume={g * 0.55:.2f},adelay={ms}|{ms}[s{i}]"); mix.append(f'[s{i}]')
af.append(''.join(mix) + f"amix=inputs={len(mix)}:normalize=0:duration=first,alimiter=limit=0.95[aout]")
open(os.path.join(work, 'af.txt'), 'w').write(';\n'.join(af))
run([FF, '-v', 'error', '-y'] + ain + ['-filter_complex_script', os.path.join(work, 'af.txt'),
     '-map', '0:v', '-map', '[aout]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', f'{fin:.2f}',
     '-movflags', '+faststart', out])
print('listo:', out, f'duración {fin:.1f}s', 'brolls', len(brolls), 'placas', len(pngs), 'efectos', len(sfx), 'palabras', len(ev))
