"""Edición del VSL de Pilates Hormonal.
Uso: python3 edit.py <heygen.mp4> <carpeta_brolls> <salida.mp4>
Pasada 1: recorta silencios. Pasada 2: zoom, B-rolls, placas, B/N, subtítulos y 1.3x.
"""
import sys, os, json, subprocess, unicodedata
from PIL import Image, ImageFilter

FF = os.path.expanduser('~/bin/ffmpeg')
HERE = os.path.dirname(os.path.abspath(__file__))
GFX = os.path.join(HERE, 'gfx')
FONTS = os.path.join(HERE, '..', 'fonts', 'subs')
SPEED = 1.3
GAP_MAX, GAP_KEEP = 0.45, 0.20   # silencios > 0.45 s quedan en 0.20 s

src, broll_dir, out = sys.argv[1:4]
work = os.path.join(HERE, 'work'); os.makedirs(work, exist_ok=True)

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-3000:]); sys.exit(1)

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
dur0 = float(subprocess.run([FF, '-i', src], capture_output=True, text=True).stderr.split('Duration: ')[1].split(',')[0].split(':')[-1]) \
    + 60 * int(subprocess.run([FF, '-i', src], capture_output=True, text=True).stderr.split('Duration: ')[1].split(':')[1])
keep = []
cur_s = 0.0
for a, b in zip(words0, words0[1:]):
    gap = b['s'] - a['e']
    if gap > GAP_MAX:
        cut_s, cut_e = a['e'] + GAP_KEEP / 2, b['s'] - GAP_KEEP / 2
        keep.append((cur_s, cut_s)); cur_s = cut_e
keep.append((cur_s, min(dur0, words0[-1]['e'] + 0.6)))
removed = sum(b - a for a, b in zip([k[1] for k in keep], [k[0] for k in keep[1:]]))
print(f'silencios: {len(keep)-1} cortes, {removed:.1f}s menos')

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
        f"[0:v]select='{expr}',setpts=N/FRAME_RATE/TB[v];[0:a]aselect='{expr}',asetpts=N/SR/TB[a]")
    run([FF, '-v', 'error', '-y', '-i', src, '-filter_complex_script', os.path.join(work, 'sel.txt'),
         '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-crf', '16', '-preset', 'fast', '-r', '30',
         '-c:a', 'aac', '-b:a', '192k', trimmed])
words = [{'w': w['w'], 's': mapt(w['s']), 'e': mapt(w['e'])} for w in words0]
total = mapt(dur0)
N = [norm(w['w']) for w in words]

def _hits(phrase, after):
    for alt in phrase.split('|'):
        toks = [norm(t) for t in alt.split()]
        toks = [t for t in toks if t]
        h = [(i, len(toks)) for i in range(len(N) - len(toks) + 1) if N[i:i + len(toks)] == toks and words[i]['s'] >= after]
        if h: return h
    return []
def find(phrase, after=0.0, last=False):
    hits = _hits(phrase, after)
    if not hits:
        print('NO ENCONTRADO:', phrase); return None
    i, _ = hits[-1] if last else hits[0]
    return words[i]['s']
def end_of(phrase, after=0.0):
    hits = _hits(phrase, after)
    if not hits:
        print('NO ENCONTRADO (fin):', phrase); return None
    i, n = hits[0]
    return words[i + n - 1]['e']

# ---------- Línea de tiempo ----------
B = lambda n: os.path.join(broll_dir, f'b{n:02d}.mp4')
brolls = []   # (archivo, inicio, duración)
def broll(n, phrase, d=3.6, after=0.0, last=False):
    t = find(phrase, after, last)
    if t is not None and os.path.exists(B(n)): brolls.append((B(n), max(0, t - 0.15), d))
broll(1, 'estrógeno')
broll(2, 'cansada todo el tiempo|cansada')
broll(3, 'ropa que les quede|ropa')
broll(4, 'hormona del estrés')
broll(5, 'medio de la panza')
broll(6, 'adormecimiento')
broll(7, 'salir a correr')
broll(8, 'técnica milenaria')
broll(9, 'este asiático|asiático para mantenerse|mantenerse firmes')
broll(10, 'reto de veintiocho días está|reto de 28 días está|está armado')
broll(11, 'suplementos')
broll(12, 'mirarte al espejo|espejo')

# mockup de la app como plano completo (fondo desenfocado)
mk = Image.open(os.path.join(GFX, 'mockup.png')).convert('RGB')
bg = mk.resize((1920, 1920)).crop((420, 0, 1500, 1920)).filter(ImageFilter.GaussianBlur(40))
fg = mk.resize((1080, 1080)); bg.paste(fg, (0, 420)); bg.save(os.path.join(work, 'mockup_full.png'))

pngs = []     # (archivo, inicio, fin)
def png(name, a, b):
    if a is not None and b is not None: pngs.append((name, a, b))
png(os.path.join(GFX, 'check.png'), 0.0, 2.4)
t_app = find('en mi app')
png(os.path.join(work, 'mockup_full.png'), t_app, t_app + 4.0 if t_app else None)
t_mar = find('mirá lo que me escribió')
t_mar_end = end_of('mujer otra vez', t_mar or 0)
png(os.path.join(GFX, 'testimonio.png'), t_mar, (t_mar_end or 0) + 0.3)
t_reg = find('te llevás de regalo')
t_b1, t_b2, t_b3 = find('el primero'), find('el segundo'), find('y el tercero')
t_b3_end = end_of('liviana en minutos')
png(os.path.join(GFX, 'bono1.png'), t_b1, t_b2)
png(os.path.join(GFX, 'bono2.png'), t_b2, t_b3)
png(os.path.join(GFX, 'bono3.png'), t_b3, (t_b3_end or 0) + 0.3)
t_50 = find('cincuenta mil pesos|50000 pesos|50 000 pesos|50 mil pesos')
png(os.path.join(GFX, 'anclaje.png'), t_50, t_50 + 2.6 if t_50 else None)
t_p1 = find('catorce mil novecientos noventa|14990|14 990')
png(os.path.join(GFX, 'precio.png'), t_p1, t_p1 + 4.2 if t_p1 else None)
t_gar = find('lo probás treinta días|lo probás 30 días|probas 30 dias|treinta días|30 días')
png(os.path.join(GFX, 'garantia.png'), t_gar, t_gar + 3.8 if t_gar else None)
t_p2 = find('esto vale mucho más')
png(os.path.join(GFX, 'precio.png'), t_p2, t_p2 + 4.0 if t_p2 else None)

gray = [(t_reg, (t_b3_end or 0) + 0.3), (t_p1, (t_p1 or 0) + 4.2), (t_p2, (t_p2 or 0) + 4.0)]
gray = [g for g in gray if g[0] is not None]
nocap = [(t_mar, (t_mar_end or 0) + 0.3), (t_b1, (t_b3_end or 0) + 0.3)]
nocap = [g for g in nocap if g[0] is not None]

# zoom alternado por oración
sent_starts = [0.0] + [words[i + 1]['s'] for i in range(len(words) - 1) if words[i]['w'][-1:] in '.?!']
zoom = [(sent_starts[i], sent_starts[i + 1] if i + 1 < len(sent_starts) else total)
        for i in range(1, len(sent_starts), 2)]

# ---------- Subtítulos (ASS) ----------
def ts(t):
    h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f'{h}:{m:02d}:{s:05.2f}'
def blocked(a, b):
    return any(a < y and b > x for x, y in nocap)
groups, cur = [], []
for w in words:
    cur.append(w)
    if len(cur) >= 3 or w['w'][-1:] in '.,?!:;' or len(' '.join(x['w'] for x in cur)) > 16:
        groups.append(cur); cur = []
if cur: groups.append(cur)
ev = []
for i, g in enumerate(groups):
    a = g[0]['s']; b = groups[i + 1][0]['s'] if i + 1 < len(groups) else g[-1]['e'] + 0.3
    b = min(b, g[-1]['e'] + 0.5)
    if blocked(a, b): continue
    txt = ' '.join(x['w'] for x in g).upper().strip(' .,;:')
    txt = txt.replace('"', '').replace('...', '…')
    ev.append(f'Dialogue: 0,{ts(a)},{ts(b)},Cap,,0,0,0,,{txt}')
ass = os.path.join(work, 'subs.ass')
open(ass, 'w', encoding='utf-8').write(f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Montserrat ExtraBold,76,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,-1,0,0,0,100,100,1,0,3,16,0,2,60,60,610,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""" + '\n'.join(ev) + '\n')

# ---------- Pasada 2: composición ----------
def en(iv): return '+'.join(f'between(t,{a:.3f},{b:.3f})' for a, b in iv) or '0'
inputs = ['-i', trimmed]
for f, _, d in brolls: inputs += ['-i', f]
for f, _, _ in pngs: inputs += ['-loop', '1', '-i', f]
fc = [f"[0:v]split=3[base][zs][gs]",
      "[zs]scale=1210:-2,crop=1080:1920[zoom]",
      "[gs]hue=s=0,eq=contrast=1.08[gray]",
      f"[base][zoom]overlay=0:0:enable='{en(zoom)}'[v0]",
      f"[v0][gray]overlay=0:0:enable='{en(gray)}'[v1]"]
last = 'v1'; k = 1
for i, (f, t, d) in enumerate(brolls):
    idx = 1 + i
    fc.append(f"[{idx}:v]trim=duration={d},scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setpts=PTS-STARTPTS+{t:.3f}/TB[b{i}]")
    fc.append(f"[{last}][b{i}]overlay=0:0:eof_action=pass:enable='between(t,{t:.3f},{t + d:.3f})'[v{k + 1}]")
    last = f'v{k + 1}'; k += 1
off = 1 + len(brolls)
for j, (f, a, b) in enumerate(pngs):
    idx = off + j
    fc.append(f"[{idx}:v]format=rgba,scale=1080:1920[p{j}]")
    fc.append(f"[{last}][p{j}]overlay=0:0:shortest=1:enable='between(t,{a:.3f},{b:.3f})'[v{k + 1}]")
    last = f'v{k + 1}'; k += 1
assp = ass.replace(':', r'\:')
fc.append(f"[{last}]ass='{assp}':fontsdir='{FONTS}',setpts=PTS/{SPEED}[vout]")
fc.append(f"[0:a]atempo={SPEED}[aout]")
open(os.path.join(work, 'fc.txt'), 'w').write(';\n'.join(fc))
run([FF, '-v', 'error', '-y'] + inputs + ['-filter_complex_script', os.path.join(work, 'fc.txt'),
     '-map', '[vout]', '-map', '[aout]', '-t', f'{total / SPEED:.2f}', '-r', '30',
     '-c:v', 'libx264', '-crf', '20', '-preset', 'medium', '-pix_fmt', 'yuv420p',
     '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', out])
print('listo:', out, f'duración {total / SPEED:.1f}s', 'brolls', len(brolls), 'placas', len(pngs), 'subs', len(ev))
