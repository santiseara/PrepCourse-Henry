"""Edición del VSL corto de la nutri dentro del quiz (Mounjaro Humilde, 2026-10-14), copiando el original de Brasil.
Uso: python3 edit_vsl_quiz.py <heygen.mp4> <carpeta_trabajo> <salida.mp4> <guion.txt> [idioma=es] [plan.json] [heads.json]
Estilo del original: subtítulos DE A UNA PALABRA en mayúscula (blanco con borde negro, a la altura del pecho);
pantalla dividida con las pantallas del quiz abajo (brolls q_*), imágenes de resultados (i_*) y B-rolls del té a pantalla
completa; palabras clave sueltas en VERDE con "pop". Base: edit_ugc_pip.py.
La carpeta de trabajo tiene brolls/, sfx/ y fonts/. Necesita matte.py y el modelo RVM (ver RVM abajo).

Diferencias con edit_ugc_split.py (pedido de Santiago: variar las ediciones):
- B-roll a PANTALLA COMPLETA con la avatar RECORTADA SIN FONDO, chiquita en la esquina de abajo a la derecha
  (estilo "green screen" de TikTok), alternada con la avatar a pantalla completa y zoom de salto por oración;
- cortes secos, sin whoosh;
- POCOS headlines (solo los puntos importantes) y pocos efectos: "el efecto de sonido cansa".
- subtítulos tipo TikTok: 3 palabras en minúscula, blancos con borde, y la plata resaltada en amarillo.
"""
import sys, os, json, subprocess, unicodedata, difflib, re

FF = os.path.expanduser('~/bin/ffmpeg')
HERE = os.path.dirname(os.path.abspath(__file__))
RVM = os.path.join(sys.argv[2], 'rvm_mobilenetv3_fp32.onnx')   # el modelo va en la carpeta de trabajo
SPEED = float(os.environ.get('SPEED', 1.08))          # VSL largos de OTO: SPEED=1.0 para que queden en 4–5 min
GAP_MAX, GAP_KEEP = float(os.environ.get('GAP_MAX', 0.40)), float(os.environ.get('GAP_KEEP', 0.18))
PIP_W = 430                          # ancho de la avatar recortada (de 1080)
PIP_X, PIP_Y = 1080 - PIP_W + 20, 1920 - PIP_W * 16 // 9 + 60   # esquina de abajo a la derecha, un poco cortada
SPLIT_Y, FADE = 880, 220             # modo 'split': dónde empieza el B-roll (debajo del mentón) y alto del degradé
CAP_Y_SPLIT = 900                    # en el original, la palabra va sobre el corte
SPLIT_CROP_Y = 0                      # desde qué altura del B-roll se toma la mitad de abajo
# "Que no se note tanto la IA" (2026-10-14): a los B-rolls se les da look de celular:
# leve movimiento de mano, menos saturación y contraste, grano y menos nitidez.
ORGANIC = True
GS_DY = 330                          # cuánto se baja la avatar grande en modo 'gs'
CAP_Y_GS = 1560
CAP_Y = 1180                         # a la altura del pecho
CAP_Y_FULL = 1640                    # sobre B-roll o imagen a pantalla completa
HEAD_Y = 1330
# Opciones (VSL 2, 2026-10-14):
#   NOMUSIC=1        -> sin música (las partes se unen y la música se pone una sola vez)
#   CAPCOLOR=&H..&   -> color de los subtítulos en ASS (BGR), ej. amarillo verdoso del testimonio: &H003BFFE5
#   capmap.json      -> [frase, reemplazo]: junta palabras en un solo subtítulo (ej. el precio en cifras)
#   stickers.json    -> [frase, png, segundos, x, y, ancho, efecto]: imagen encima (sello de garantía)
NOMUSIC = os.environ.get('NOMUSIC') == '1'
CAPCOLOR = os.environ.get('CAPCOLOR', '&H00FFFFFF')

src, wd, out, gpath = sys.argv[1:5]
LANG = sys.argv[5] if len(sys.argv) > 5 else 'es'
GUION = open(gpath, encoding='utf-8').read()
work = os.path.join(wd, 'edit_' + os.path.splitext(os.path.basename(src))[0]); os.makedirs(work, exist_ok=True)   # una carpeta por video de HeyGen
BR, SFX, FONTS = (os.path.join(wd, x) for x in ('brolls', 'sfx', 'fonts'))

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
    segs, _ = m.transcribe(wav, language=LANG, word_timestamps=True, beam_size=5, initial_prompt=GUION)
    words = [{'w': w.word.strip(), 's': w.start, 'e': w.end} for s in segs for w in s.words]
    json.dump(words, open(cache, 'w'), ensure_ascii=False)
    return words

def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    return ''.join(c for c in s if c.isalnum() and unicodedata.category(c) != 'Mn')

# ---------- Pasada 1: recorte de silencios ----------
words0 = transcribe(src, os.path.join(work, 'words0.json'))
# Whisper inventa palabras en los silencios ("194.", "Después de un minuto"): se sacan ANTES de recortar silencios
_ops = difflib.SequenceMatcher(None, [norm(w['w']) for w in words0], [norm(x) for x in GUION.split()], autojunk=False).get_opcodes()
_bad = {i for op, i1, i2, j1, j2 in _ops if op == 'delete' for i in range(i1, i2)}
if _bad: print('inventadas por Whisper:', ' '.join(words0[i]['w'] for i in sorted(_bad)))
words0 = [w for i, w in enumerate(words0) if i not in _bad]
dur0 = duration(src)
keep, cur_s = [], 0.0
for a, b in zip(words0, words0[1:]):
    if b['s'] - a['e'] > GAP_MAX:
        keep.append((cur_s, a['e'] + GAP_KEEP / 2)); cur_s = b['s'] - GAP_KEEP / 2
keep.append((cur_s, min(dur0, words0[-1]['e'] + 0.5)))

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
         '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-crf', '15', '-preset', os.environ.get('TRIM_PRESET', 'fast'), '-r', '30',
         '-c:a', 'aac', '-b:a', '192k', trimmed])
mask = os.path.join(work, 'mask.mp4')
if not os.path.exists(mask):
    run(['python3', os.path.join(HERE, 'matte.py'), trimmed, RVM, mask, '540'])

words = []
for w in words0:   # Whisper parte "thirty" "-five": se une al anterior
    w = {'w': w['w'], 's': mapt(w['s']) / SPEED, 'e': mapt(w['e']) / SPEED}
    if words and w['w'][:1] == '-':
        words[-1] = {**words[-1], 'w': words[-1]['w'] + w['w'], 'e': w['e']}
    else:
        words.append(w)
gt = GUION.split()
a_, b_ = [norm(w['w']) for w in words], [norm(x) for x in gt]
drop = set()
for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a_, b_, autojunk=False).get_opcodes():
    if op in ('equal', 'replace') and i2 - i1 == j2 - j1:
        for i, j in zip(range(i1, i2), range(j1, j2)):
            words[i]['w'] = gt[j]
    elif op == 'delete':                 # palabras que Whisper inventó (no están en el guion)
        drop.update(range(i1, i2))
if drop: print('descartadas:', ' '.join(words[i]['w'] for i in sorted(drop)))
words = [w for i, w in enumerate(words) if i not in drop]
total = mapt(dur0) / SPEED
N = [norm(w['w']) for w in words]

def find(phrase, end=False):
    for alt in phrase.split('|'):
        toks = [t for t in (norm(x) for x in alt.split()) if t]
        for i in range(len(N) - len(toks) + 1):
            if N[i:i + len(toks)] == toks:
                return words[i + len(toks) - 1]['e'] if end else words[i]['s']
    print('NO ENCONTRADO:', phrase); return None

# ---------- B-roll a pantalla completa + avatar recortada en la esquina ----------
# (clip, frase donde entra, frase donde termina, segundo del clip). Planos distintos, sin repetir.
# Cada entrada puede llevar un 5.º campo con el modo (formato 3, 2026-10-14):
#   'pip'  = B-roll + avatar chiquita sin fondo en la esquina (por defecto)
#   'full' = solo el B-roll a pantalla completa (corte, sin avatar)
#   'gs'   = avatar recortada EN GRANDE delante del B-roll (green screen)
#   'split'= pantalla dividida: avatar arriba, B-roll abajo con degradé suave (formato 1)
PLAN = json.load(open(os.path.join(wd, sys.argv[6] if len(sys.argv) > 6 else 'plan_pip.json')))
brolls, crop_y = [], {}
for item in PLAN:
    name, p1, p2, ss = item[:4]; mode = item[4] if len(item) > 4 else 'pip'
    cy_ = item[5] if len(item) > 5 else SPLIT_CROP_Y   # 6.º campo opcional: desde qué altura se recorta el B-roll en 'split'
    a, b = find(p1), find(p2, end=True)
    if a is None or b is None: continue
    a = 0.0 if a < 0.6 else a - 0.06
    b = b + 0.12
    if brolls and a - brolls[-1][2] < 0.45:
        brolls[-1] = (*brolls[-1][:2], a, *brolls[-1][3:])
    f = os.path.join(BR, name + '.mp4')
    brolls.append((f, a, a + min(b - a, duration(f) - ss), ss, mode)); crop_y[len(brolls) - 1] = cy_
def merge(iv):
    out_ = []
    for a, b in iv:
        if out_ and a - out_[-1][1] < 0.05: out_[-1] = (out_[-1][0], b)
        else: out_.append((a, b))
    return out_
pip_iv = merge([(a, b) for f, a, b, ss, m in brolls if m == 'pip'])
gs_iv = merge([(a, b) for f, a, b, ss, m in brolls if m == 'gs'])
split_iv = merge([(a, b) for f, a, b, ss, m in brolls if m == 'split'])
full_iv = merge([(a, b) for f, a, b, ss, m in brolls if m == 'full'])

# zoom de salto: en los tramos de avatar a pantalla completa, una oración sí y otra no
starts = [0.0] + [words[i + 1]['s'] for i in range(len(words) - 1) if words[i]['w'][-1:] in '.?!']
zoom = [(starts[i], starts[i + 1] if i + 1 < len(starts) else total) for i in range(1, len(starts), 2)]

# ---------- Headlines: solo los puntos importantes ----------
HEAD = json.load(open(os.path.join(wd, sys.argv[7] if len(sys.argv) > 7 else 'heads_pip.json')))
heads, sfx = [], []
for p, txt, fx, d in HEAD:
    t = find(p)
    if t is None: continue
    heads.append((t, min(t + d, total), txt))
    if fx: sfx.append((fx + '.wav', t, 0.9 if fx == 'chaching' else 0.5))

# ---------- Subtítulos tipo TikTok (3 palabras, la plata en amarillo) ----------
def ts(t): return f'{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}'
# las cantidades de plata se muestran en cifras ("eight hundred and fifty" -> "$850"), en amarillo y en su propio bloque
NUM = {'a': 1, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
       'ten': 10, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90}
def numval(toks):
    total_, cur = 0, 0
    for t in toks:
        t = t.lower().strip('.,?!')
        if t == 'and': continue
        if t == 'hundred': cur = max(cur, 1) * 100
        elif t == 'thousand': total_ += max(cur, 1) * 1000; cur = 0
        elif '-' in t: cur += sum(NUM.get(x, 0) for x in t.split('-'))
        else: cur += NUM[t]
    return total_ + cur
toks = []
i = 0
while i < len(words):
    j = i
    while j < len(words) and (words[j]['w'].lower().strip('.,?!') in NUM or words[j]['w'].lower().strip('.,?!') in ('hundred', 'thousand', 'and')
                              or all(x in NUM for x in words[j]['w'].lower().strip('.,?!').split('-'))):
        if words[j]['w'][-1:] in '.,?!': j += 1; break
        j += 1
    while j > i and words[j - 1]['w'].lower().strip('.,?!') == 'and': j -= 1
    span = [w['w'] for w in words[i:j]]
    nxt = words[j]['w'].lower().strip('.,?!') if j < len(words) else ''
    if any(s.lower().strip('.,?!') in ('hundred', 'thousand') for s in span) and nxt not in ('stones',):
        e = words[j - 1]['e']
        if nxt == 'dollars': e = words[j]['e']; j += 1
        toks.append({'w': f'${numval(span):,}', 's': words[i]['s'], 'e': e, 'money': True}); i = j
    else:
        toks.append(dict(words[i])); i += 1
cm = os.path.join(wd, os.environ.get('CAPMAP', 'capmap.json'))
for phr, txt in (json.load(open(cm)) if os.path.exists(cm) else []):
    pt = [norm(x) for x in phr.split()]
    for k in range(len(toks) - len(pt) + 1):
        if [norm(t['w']) for t in toks[k:k + len(pt)]] == pt:
            toks[k:k + len(pt)] = [{'w': txt, 's': toks[k]['s'], 'e': toks[k + len(pt) - 1]['e'], 'money': True}]
            break
ev, i = [], 0
while i < len(toks):
    grp = [toks[i]]
    while (not grp[0].get('money') and len(grp) < 1 and i + len(grp) < len(toks) and not toks[i + len(grp)].get('money')
           and grp[-1]['w'][-1:] not in '.,?!…:;' and len(' '.join(w['w'] for w in grp)) + len(toks[i + len(grp)]['w']) <= 18):
        grp.append(toks[i + len(grp)])
    a = grp[0]['s']; i += len(grp)
    b = toks[i]['s'] if i < len(toks) else grp[-1]['e'] + 0.3
    b = min(b, grp[-1]['e'] + 0.4)
    parts = [('{\\c&H40D61F&\\fscx125\\fscy125}' + w['w'] + '{\\r}') if w.get('money') else w['w'].rstrip('.,?!…:;').upper() for w in grp]
    cy = (CAP_Y_FULL if any(x - 0.05 <= a < y for x, y in full_iv) else
          CAP_Y_GS if any(x - 0.05 <= a < y for x, y in gs_iv) else
          CAP_Y_SPLIT if any(x - 0.05 <= a < y for x, y in split_iv) else CAP_Y)   # con la avatar grande, el subtítulo va al pecho
    ev.append(f'Dialogue: 0,{ts(a)},{ts(b)},Cap,,0,0,0,,{{\\pos(540,{cy})\\fscx85\\fscy85\\t(0,80,\\fscx100\\fscy100)}}' + ' '.join(parts))
for a, b, txt in heads:
    ev.append(f'Dialogue: 1,{ts(a)},{ts(b)},Head,,0,0,0,,{{\\fscx70\\fscy70\\t(0,110,\\fscx108\\fscy108)\\t(110,190,\\fscx100\\fscy100)}}{txt}')
ass = os.path.join(work, 'subs.ass')
open(ass, 'w', encoding='utf-8').write(f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Arial Black,82,{CAPCOLOR},{CAPCOLOR},&H00000000,&H64000000,0,0,0,0,100,100,1,0,1,7,3,5,60,60,0,1
Style: Head,Arial Black,104,&H0040D61F,&H0040D61F,&H00000000,&H00000000,0,0,0,0,100,100,1,-4,1,8,0,8,50,50,{HEAD_Y},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""" + '\n'.join(ev) + '\n')

# ---------- Pasada 2: video ----------
def en(iv): return '+'.join(f'between(t,{a:.3f},{b:.3f})' for a, b in iv) or '0'
PH = PIP_W * 16 // 9
inputs = ['-i', trimmed, '-i', mask]
for f, a, b, ss, m in brolls: inputs += ['-ss', f'{ss:.2f}', '-t', f'{(b - a) + 0.3:.2f}', '-i', f]
fc = [f"[0:v]setpts=PTS/{SPEED},fps=30,split=4[base][zs][ps][gv]",
      "[zs]scale=1210:-2,crop=1080:1920:65:40[zoom]",
      f"[base][zoom]overlay=0:0:enable='{en(zoom)}'[v0]",
      f"[1:v]setpts=PTS/{SPEED},fps=30,split=2[m1][m2]",
      f"[m1]scale={PIP_W}:{PH},format=gray[pm]",
      "[m2]scale=1080:1920,format=gray[gm]",
      "[gv][gm]alphamerge[gs]",
      f"[ps]scale={PIP_W}:{PH}[pv]",
      "[pv][pm]alphamerge[pip]"]
last = 'v0'
from PIL import Image
import math
BH = 1920 - SPLIT_Y
mk = Image.new('L', (1080, BH), 255)
for y in range(FADE):
    mk.paste(int(255 * (0.5 - 0.5 * math.cos(math.pi * y / FADE))), (0, y, 1080, y + 1))
mpath = os.path.join(work, 'split_mask.png'); mk.save(mpath)
inputs += ['-loop', '1', '-t', f'{total + 1:.2f}', '-i', mpath]   # con -t: si no, la imagen se repite sin fin
MI = 2 + len(brolls)
nsplit = sum(1 for x in brolls if x[4] == 'split')
if nsplit: fc.append(f"[{MI}:v]format=gray,split={nsplit}" + ''.join(f'[sm{k}]' for k in range(nsplit)))
LOOK = ("scale=1124:1998,crop=1080:1920:x='22+14*sin(t*1.6)':y='39+11*sin(t*1.2+1)',"
        "eq=saturation=0.86:contrast=0.95:gamma=1.03,unsharp=5:5:-0.35,noise=alls=7:allf=t," if ORGANIC else '')
k = 0
for i, (f, a, b, ss, m) in enumerate(brolls):
    lk = '' if os.path.basename(f)[:2] in ('q_', 'i_') else LOOK
    fc.append(f"[{2 + i}:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,{lk}setpts=PTS-STARTPTS+{a:.3f}/TB[b{i}]")
    if m == 'split':   # se toma el centro del plano y se funde con la avatar con el degradé
        fc.append(f"[b{i}]crop=1080:{BH}:0:{crop_y[i]},format=rgba[c{i}]")   # se toma desde arriba para que la cabeza de la persona del B-roll no quede bajo el degradé
        fc.append(f"[c{i}][sm{k}]alphamerge[bs{i}]"); k += 1
        fc.append(f"[{last}][bs{i}]overlay=0:{SPLIT_Y}:eof_action=pass:enable='between(t,{a:.3f},{b:.3f})'[v{i + 1}]")
    else:
        fc.append(f"[{last}][b{i}]overlay=0:0:eof_action=pass:enable='between(t,{a:.3f},{b:.3f})'[v{i + 1}]")
    last = f'v{i + 1}'
fc.append(f"[{last}][pip]overlay={PIP_X}:{PIP_Y}:enable='{en(pip_iv)}'[vq]")
fc.append(f"[vq][gs]overlay=0:{GS_DY}:enable='{en(gs_iv)}'[vp]")   # avatar grande, bajada para que se vea el B-roll arriba
sp = os.path.join(wd, os.environ.get('STICKERS', 'stickers.json'))
cur = 'vp'
for n_, (phr, png, d, x, y, w_, fx) in enumerate(json.load(open(sp)) if os.path.exists(sp) else []):
    t = find(phr)
    if t is None: continue
    k = sum(1 for z in inputs if z == '-i')          # índice de la entrada nueva
    inputs += ['-loop', '1', '-t', f'{total + 1:.2f}', '-i', os.path.join(wd, png)]
    fc.append(f"[{k}:v]scale={w_}:-1,format=rgba,fade=t=in:st={t:.2f}:d=0.15:alpha=1,fade=t=out:st={t + d - 0.2:.2f}:d=0.2:alpha=1[st{n_}]")
    fc.append(f"[{cur}][st{n_}]overlay={x}:{y}:enable='between(t,{t:.3f},{t + d:.3f})'[sk{n_}]"); cur = f'sk{n_}'
    if fx: sfx.append((fx + '.wav', t, 0.6))
assp = ass.replace(':', r'\:')
fc.append(f"[{cur}]ass='{assp}':fontsdir='{FONTS}',format=yuv420p[vout]")
fc.append(f"[0:a]atempo={SPEED}[aout]")
open(os.path.join(work, 'fc.txt'), 'w').write(';\n'.join(fc))
vid = os.path.join(work, 'video_voz.mkv')
run([FF, '-v', 'error', '-y'] + inputs + ['-filter_complex_script', os.path.join(work, 'fc.txt'),
     '-map', '[vout]', '-map', '[aout]', '-t', f'{total:.2f}', '-r', '30',
     '-c:v', 'libx264', '-crf', '17', '-preset', 'medium', '-c:a', 'pcm_s16le', vid])

# ---------- Audio: voz -14 LUFS, música muy baja con ducking, pocos efectos ----------
music = os.path.join(work, 'music.wav')
if NOMUSIC:   # silencio en lugar de música
    run([FF, '-v', 'error', '-y', '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo', '-t', f'{total + 1:.1f}', music])
else:
    run(['python3', os.path.join(HERE, 'music.py'), f'{total + 1:.1f}', music])
ain = ['-i', vid, '-i', music]
for f, _, _ in sfx: ain += ['-i', os.path.join(SFX, f)]
af = ["[0:a]loudnorm=I=-14:TP=-1.5:LRA=11,asplit=2[voz][sc]",
      "[1:a]loudnorm=I=-33:TP=-9[mus]",
      "[mus][sc]sidechaincompress=threshold=0.03:ratio=3:attack=20:release=400[duck]"]
mix = ['[voz]', '[duck]']
for i, (f, t, g) in enumerate(sfx):
    ms = int(t * 1000)
    af.append(f"[{2 + i}:a]volume={g * 0.55:.2f},adelay={ms}|{ms}[s{i}]"); mix.append(f'[s{i}]')
af.append(''.join(mix) + f"amix=inputs={len(mix)}:normalize=0:duration=first,alimiter=limit=0.95[aout]")
open(os.path.join(work, 'af.txt'), 'w').write(';\n'.join(af))
run([FF, '-v', 'error', '-y'] + ain + ['-filter_complex_script', os.path.join(work, 'af.txt'),
     '-map', '0:v', '-map', '[aout]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000',
     '-t', f'{total:.2f}', '-movflags', '+faststart', out])
json.dump({'brolls': [(os.path.basename(f), round(a, 2), round(b, 2), ss, m) for f, a, b, ss, m in brolls],
           'heads': [(round(a, 2), round(b, 2), t) for a, b, t in heads], 'sfx': [(f, round(t, 2)) for f, t, g in sfx]},
          open(os.path.join(work, 'plan.json'), 'w'), indent=1)
print('listo:', out, f'duración {total:.1f}s', 'brolls', len(brolls), 'headlines', len(heads), 'efectos', len(sfx))
