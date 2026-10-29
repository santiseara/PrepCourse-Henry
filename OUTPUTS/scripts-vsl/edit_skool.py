"""Ad UGC con avatar de HeyGen para Skool AI (2026-10-29).
Copia la edicion del ganador (Udemia.IA): hook quemado arriba en caja blanca, subtitulo de UNA palabra
grande abajo al centro, PIP chico abajo a la derecha con otro personaje, y placa final de marca.
La base es el video de la avatar, que habla a camara todo el tiempo. La voz sale del propio video,
asi que no se recortan silencios: video y audio se aceleran juntos para no romper el lipsync.
Sin musica ni efectos: el original es UGC crudo.
Uso: python3 edit_skool.py plan.json salida.mp4
plan.json:
 "avatar": "SK_V1_raw.mp4", "script": "V1.txt", "speed": 1.0, "lang": "en",
 "hook": "THIS IS HOW I LEARNED AI AT 49", "hook_dur": 3.5,
 "pip": {"src": "avatar-4-paul.png", "at": [[5.0, 4.0], [15.0, 3.5]]},   # (segundo de inicio, duracion)
 "end": {"sub": "...", "cta": "Tap Learn More"}, "capy": 1430
"""
import os, re, sys, json, subprocess, difflib
from faster_whisper import WhisperModel
from PIL import Image, ImageDraw, ImageFont

FF = os.path.expanduser('~/bin/ffmpeg')
P = json.load(open(sys.argv[1])); OUT = sys.argv[2]
base = os.path.dirname(os.path.abspath(sys.argv[1]))
def F(p): return p if os.path.isabs(p) else os.path.join(base, p)
tmp = os.path.join(base, os.path.basename(OUT) + '_tmp'); os.makedirs(tmp, exist_ok=True)

W, H, FPS = 1080, 1920, 30
NAVY = (14, 20, 32)            # fondo de la tapa de Skool AI
ORANGE = (247, 147, 30)        # naranja del sol de la tapa
FONT_BLACK = os.path.expanduser('~/Desktop/bachas-concreto/work-mark/fonts/Arial Black.ttf')
FONT_B = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
EMOJI = '/System/Library/Fonts/Apple Color Emoji.ttc'
PIP_W = 300                    # ancho del recuadro de abajo a la derecha
PIP_H = PIP_W * 16 // 9
PIP_X, PIP_Y = W - PIP_W - 26, 1150

def run(c): subprocess.run(c, check=True)
def norm(w): return re.sub(r'[^\w]', '', w.lower())
def dur(p):
    r = subprocess.run([FF, '-i', p], capture_output=True, text=True).stderr
    h, m, s = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r).groups()
    return int(h) * 3600 + int(m) * 60 + float(s)

# 1) avatar y voz: se aceleran juntos (la velocidad fuerte ya se puso en HeyGen)
sp = P.get('speed', 1.0)
AV = F(P['avatar'])
run([FF, '-v', 'error', '-y', '-i', AV, '-an', '-vf',
     f"setpts=PTS/{sp:.4f},fps={FPS},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,format=yuv420p",
     '-c:v', 'libx264', '-crf', '18', '-preset', 'fast', f'{tmp}/av.mp4'])
run([FF, '-v', 'error', '-y', '-i', AV, '-vn', '-af',
     f'atempo={sp:.4f},aresample=48000,afade=t=in:d=0.02', '-ac', '2', f'{tmp}/vo.wav'])
L = dur(f'{tmp}/vo.wav')

# 2) palabras del guion alineadas al audio
model = WhisperModel('small', device='cpu', compute_type='int8')
segs, _ = model.transcribe(f'{tmp}/vo.wav', language=P.get('lang', 'en'), word_timestamps=True)
wd = [(w.start, w.end, w.word.strip()) for s in segs for w in s.words]
sw = open(F(P['script'])).read().split()
a, b = [norm(x[2]) for x in wd], [norm(x) for x in sw]
vw = []
for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
    if op == 'equal':
        vw += [(wd[i1 + k][0], wd[i1 + k][1], sw[j1 + k]) for k in range(i2 - i1)]
    elif j2 > j1:
        s0 = wd[i1][0] if i1 < len(wd) else (vw[-1][1] if vw else 0)
        e0 = wd[i2 - 1][1] if i2 > i1 else s0 + 0.3 * (j2 - j1)
        st = max(0.05, (e0 - s0) / (j2 - j1))
        vw += [(s0 + k * st, s0 + (k + 1) * st, sw[j1 + k]) for k in range(j2 - j1)]
print(f'{len(vw)} palabras alineadas sobre {L:.1f}s')

# 3) cortes del medio: se corta a una PAGINA DEL LIBRO con zoom lento, nunca a otra persona
# (2026-10-29, Santiago: "si está hablando una persona, de la nada otra persona en la edición, no sirve")
AVL = dur(f'{tmp}/av.mp4')
def wt(word, occ=0):
    ts_ = [w for w in vw if norm(w[2]) == norm(word)]
    if occ >= len(ts_): print(f'aviso: "{word}" n.º {occ} no aparece'); return None
    return ts_[occ]
cw = []
for word, occ, key, d_ in P.get('cutaways', []):
    w = wt(word, occ)
    if not w: continue
    t0 = max(0.0, w[0] - 0.10)
    cw.append([t0, min(L, t0 + d_), key])
cw.sort()
cut = []
for c in cw:
    if cut and c[0] < cut[-1][1] + 0.6:
        print(f'aviso: el corte a {c[2]} pisa al anterior, se ignora'); continue
    cut.append(c)
segments, pos = [], 0.0
for t0, t1, key in cut:
    if t0 - pos > 0.5: segments.append(('av', pos, t0, None))
    elif t0 > pos: t0 = pos
    segments.append(('pg', t0, t1, key)); pos = t1
if L - pos > 0.3: segments.append(('av', pos, L, None))
if not segments: segments = [('av', 0.0, L, None)]
print('planos:', ' '.join(f'{s[3] or "AVATAR"}:{s[2]-s[1]:.1f}s' for s in segments))

parts = []
for n, (kind, t0, t1, key) in enumerate(segments):
    d_ = t1 - t0; pc = f'{tmp}/s{n:02d}.mp4'
    if kind == 'av':
        run([FF, '-v', 'error', '-y', '-ss', f'{t0:.3f}', '-t', f'{min(d_, max(0.1, AVL - t0)):.3f}',
             '-i', f'{tmp}/av.mp4', '-an', '-vf', f'fps={FPS},setsar=1,format=yuv420p', '-t', f'{d_:.3f}',
             '-c:v', 'libx264', '-crf', '18', '-preset', 'fast', pc])
    else:
        z = f"(1+0.08*t/{d_:.3f})" if n % 2 == 0 else f"(1.08-0.08*t/{d_:.3f})"
        vf = (f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},"
              f"scale=w='{2*W}*{z}':h=-2:eval=frame:flags=bicubic,crop={2*W}:{2*H}:(iw-{2*W})/2:(ih-{2*H})/2,"
              f"scale={W}:{H}:flags=lanczos,setsar=1,format=yuv420p")
        run([FF, '-v', 'error', '-y', '-loop', '1', '-t', f'{d_:.3f}', '-i', F(P['pages'][key]),
             '-filter_complex', vf, '-t', f'{d_:.3f}', '-r', str(FPS),
             '-c:v', 'libx264', '-crf', '18', '-preset', 'fast', pc])
    parts.append(pc)
open(f'{tmp}/all.txt', 'w').write(''.join(f"file '{p}'\n" for p in parts))
run([FF, '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', f'{tmp}/all.txt', '-c', 'copy', f'{tmp}/cat.mp4'])
vid = f'{tmp}/cat.mp4'

# 4) placas en PNG: el hook de arriba y la placa final
def font(sz, path=FONT_BLACK): return ImageFont.truetype(path, sz)
def emoji_img(ch, h):
    try:
        f = ImageFont.truetype(EMOJI, 160)
        im = Image.new('RGBA', (220, 220)); ImageDraw.Draw(im).text((0, 0), ch, font=f, embedded_color=True)
        im = im.crop(im.getbbox()); return im.resize((int(im.width * h / im.height), h), Image.LANCZOS)
    except Exception: return None
def split_emoji(txt):
    m = re.search(r'\s*([\U0001F300-\U0001FAFF☀-➿]️?)\s*$', txt)
    return (txt[:m.start()], m.group(1)) if m else (txt, None)

def png_hook(txt, path):
    """Caja blanca arriba con el hook en mayuscula, como el ganador."""
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im); f = font(58, FONT_B)
    words, lines, cur = txt.upper().split(), [], ''
    for w_ in words:
        t_ = (cur + ' ' + w_).strip()
        if d.textlength(t_, font=f) > 860 and cur: lines.append(cur); cur = w_
        else: cur = t_
    lines.append(cur)
    lw = [d.textlength(l, font=f) for l in lines]
    bw, bh = max(lw) + 72, len(lines) * 74 + 44
    x0, y0 = (W - bw) / 2, 150
    d.rounded_rectangle((x0, y0, x0 + bw, y0 + bh), 18, fill=(255, 255, 255, 248))
    for i, l in enumerate(lines):
        d.text(((W - lw[i]) / 2, y0 + 22 + i * 74), l, font=f, fill=NAVY)
    im.save(path)

def png_end(o, path):
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im)
    d.rectangle((0, 0, W, H), fill=NAVY + (242,))
    # el sol de nodos de la tapa, simplificado
    cx, cy = W // 2, 640
    import math
    for k in range(10):
        ang = math.radians(k * 36 + 12); r = 215 if k % 2 == 0 else 165
        x, y = cx + r * math.cos(ang), cy + r * math.sin(ang)
        d.line((cx, cy, x, y), fill=ORANGE + (120,), width=4)
        d.ellipse((x - 17, y - 17, x + 17, y + 17), fill=ORANGE + (255,))
    d.ellipse((cx - 62, cy - 62, cx + 62, cy + 62), fill=ORANGE + (255,))
    f1 = font(118); t = 'SKOOL AI'
    d.text(((W - d.textlength(t, font=f1)) / 2, 930), t, font=f1, fill=(255, 255, 255))
    f2 = font(46, FONT_B); t2 = 'MASTER AI IN 7 DAYS'
    d.text(((W - d.textlength(t2, font=f2)) / 2, 1078), t2, font=f2, fill=(255, 255, 255, 220))
    f3 = font(40, FONT_B); s = o.get('sub', '7 days · 15 min a day · instant download')
    d.text(((W - d.textlength(s, font=f3)) / 2, 1190), s, font=f3, fill=ORANGE + (255,))
    body, emo = split_emoji(o.get('cta', 'Tap Learn More 👇')); fc = font(56)
    em = emoji_img(emo, 56) if emo else None
    GAP = 30
    cw = d.textlength(body, font=fc) + (em.width + GAP if em else 0); bw = cw + 96
    x0, y0 = (W - bw) / 2, 1390
    d.rounded_rectangle((x0, y0, x0 + bw, y0 + 106), 53, fill=ORANGE + (255,))
    d.text((x0 + 48, y0 + 22), body, font=fc, fill=NAVY)
    if em: im.alpha_composite(em, (int(x0 + 48 + d.textlength(body, font=fc) + GAP), int(y0 + 24)))
    im.save(path)

ovs = []
if P.get('hook'):
    png_hook(P['hook'], f'{tmp}/o_hook.png'); ovs.append((f'{tmp}/o_hook.png', 0.0, P.get('hook_dur', 3.5)))
END = P.get('end')
end_t = L
if END:
    end_t = max(0.0, L - P.get('end_dur', 2.2))
    png_end(END, f'{tmp}/o_end.png'); ovs.append((f'{tmp}/o_end.png', end_t, L))

# 5) subtitulos: UNA palabra grande, blanca con borde, abajo al centro (como el ganador)
def ts(t): t = max(0, t); return f'{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}'
CAPY = P.get('capy', 1430)
ass = [f'''[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: C,Arial Black,96,&H00FFFFFF,&H00FFFFFF,&H00201409,&H00201409,0,0,0,0,100,100,0,0,1,9,4,5,60,60,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text''']
def clean(w): return w.replace('…', '').strip(' ,;:"“”').lower()
for i, (s, e, w) in enumerate(vw):
    if s >= end_t - 0.05: break
    e2 = min(vw[i + 1][0] if i + 1 < len(vw) else e + 0.3, e + 0.45, end_t)
    if e2 - s < 0.06: continue
    ass.append(f'Dialogue: 0,{ts(s)},{ts(e2)},C,,0,0,0,,{{\\pos({W // 2},{CAPY})}}{clean(w)}')
open(f'{tmp}/subs.ass', 'w').write('\n'.join(ass) + '\n')

# 6) armado final: overlays + subtitulos, audio tal cual (sin musica ni efectos)
blank = Image.new('RGBA', (W, H))
edges = sorted({0.0, L} | {max(0.0, min(L, x)) for _, t0, t1 in ovs for x in (t0, t1)})
cache, lines_ = {}, []
for k in range(len(edges) - 1):
    a_, b_ = edges[k], edges[k + 1]
    if b_ - a_ < 0.01: continue
    act = tuple(i for i, (p_, t0, t1) in enumerate(ovs) if t0 <= a_ + 1e-3 and t1 >= b_ - 1e-3)
    if act not in cache:
        im = blank.copy()
        for i in act: im.alpha_composite(Image.open(ovs[i][0]).convert('RGBA'))
        cache[act] = f'{tmp}/ov_{len(cache)}.png'; im.save(cache[act])
    lines_.append(f"file '{cache[act]}'\nduration {b_ - a_:.3f}\n")
lines_.append(f"file '{cache[act]}'\n")
open(f'{tmp}/ov.txt', 'w').write(''.join(lines_))
run([FF, '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', f'{tmp}/ov.txt', '-vf', f'fps={FPS},format=argb',
     '-t', f'{L:.2f}', '-c:v', 'qtrle', f'{tmp}/ov.mov'])
run([FF, '-v', 'error', '-y', '-i', vid, '-i', f'{tmp}/ov.mov', '-filter_complex',
     f"[0:v][1:v]overlay=0:0:format=auto[ov];[ov]ass={tmp}/subs.ass[v]", '-map', '[v]',
     '-c:v', 'libx264', '-crf', '18', '-pix_fmt', 'yuv420p', '-t', f'{L:.2f}', f'{tmp}/video.mp4'])
# 7) cama musical: la de Herrero, normalizada contra la voz y a music_db (regla del 29/10)
if P.get('music'):
    import numpy as np, soundfile as sf
    m_, sr_ = sf.read(F(P['music'])); v_, _ = sf.read(f'{tmp}/vo.wav')
    if m_.ndim == 1: m_ = np.stack([m_, m_], 1)
    need = int((L + 0.5) * sr_); xf = int(1.0 * sr_)
    while len(m_) < need:      # loop con fundido de 1 s desde el segundo 4
        a2 = m_[int(4 * sr_):]; r_ = np.linspace(0, 1, xf)[:, None]
        m_ = np.concatenate([m_[:-xf], m_[-xf:] * (1 - r_) + a2[:xf] * r_, a2[xf:]])
    m_ = m_[:need]
    rv = np.sqrt(np.mean(v_[v_.any(1) if v_.ndim > 1 else v_ != 0] ** 2)); rm = np.sqrt(np.mean(m_ ** 2))
    m_ = m_ * (rv / rm) * 10 ** (P.get('music_db', -8) / 20)
    sf.write(f'{tmp}/music.wav', np.clip(m_, -1, 1), sr_)
    run([FF, '-v', 'error', '-y', '-i', f'{tmp}/vo.wav', '-i', f'{tmp}/music.wav', '-filter_complex',
         f"[1:a]aresample=48000,afade=t=in:d=0.6,afade=t=out:st={max(0, L - 1.2):.2f}:d=1.2[m];"
         f"[0:a][m]amix=inputs=2:duration=first:normalize=0[a]", '-map', '[a]', '-t', f'{L:.2f}', f'{tmp}/mix.wav'])
    AUD = f'{tmp}/mix.wav'
else:
    AUD = f'{tmp}/vo.wav'
run([FF, '-v', 'error', '-y', '-i', f'{tmp}/video.mp4', '-i', AUD, '-map', '0:v', '-map', '1:a',
     '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', f'{L:.2f}', '-movflags', '+faststart', OUT])
print(f'OK {OUT} {L:.1f}s')
