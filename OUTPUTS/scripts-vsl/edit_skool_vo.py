"""Ads de VOZ EN OFF de Skool AI (2026-10-29). Misma estetica que edit_skool.py (hook en caja blanca,
subtitulo de una palabra, placa final, cama de Herrero a -8 dB), pero sin avatar: la linea de tiempo
son clips de TikTok encadenados. NO entra ni una foto fija (regla del 29/10): lo que antes era una
hoja dibujada del producto ahora es una PLACA DE TEXTO con el numero de pagina ENCIMA del clip.
A diferencia del de avatar, aca SI se recortan los silencios y la voz va a speed 1.30 (regla del 26/10).
Uso: python3 edit_skool_vo.py plan.json salida.mp4
plan.json:
 "vo": "vo/V5.wav", "script": "V5.txt", "speed": 1.30, "silence": [0.26, 0.12], "lang": "en",
 "hook": "...", "hook_dur": 3.5,
 "pages": {"excel": {"src": "tt/cand/excel_033.mp4", "ss": 4.0, "zoom": 1.2, "ybias": 1.0}, ...},
 "shots": [[null, 0, "desk"], ["files", 0, "excel", {"badge": 18, "head": "Ask about your own files"}], ...]
   # palabra de arranque, ocurrencia, clip y (opcional) la placa de pagina que va encima de ese plano
 "end": {"sub": "...", "cta": "..."}, "music": "...", "music_db": -8, "capy": 1430
"""
import os, re, sys, json, subprocess, difflib, math
from faster_whisper import WhisperModel
from PIL import Image, ImageDraw, ImageFont

FF = os.path.expanduser('~/bin/ffmpeg')
P = json.load(open(sys.argv[1])); OUT = sys.argv[2]
base = os.path.dirname(os.path.abspath(sys.argv[1]))
def F(p): return p if os.path.isabs(p) else os.path.join(base, p)
tmp = os.path.join(base, os.path.basename(OUT) + '_tmp'); os.makedirs(tmp, exist_ok=True)

W, H, FPS = 1080, 1920, 30
NAVY = (14, 20, 32)
ORANGE = (247, 147, 30)
FONT_BLACK = os.path.expanduser('~/Desktop/bachas-concreto/work-mark/fonts/Arial Black.ttf')
FONT_B = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
EMOJI = '/System/Library/Fonts/Apple Color Emoji.ttc'

def run(c): subprocess.run(c, check=True)
def norm(w): return re.sub(r'[^\w]', '', w.lower())
def dur(p):
    r = subprocess.run([FF, '-i', p], capture_output=True, text=True).stderr
    h, m, s = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r).groups()
    return int(h) * 3600 + int(m) * 60 + float(s)

# 1) voz: se cortan los silencios y se acelera (regla de voz en off, 24 y 26/10)
sp = P.get('speed', 1.30)
th, keep = P.get('silence', [0.26, 0.12])
run([FF, '-v', 'error', '-y', '-i', F(P['vo']), '-af',
     f'silenceremove=stop_periods=-1:stop_duration={keep}:stop_threshold=-38dB:detection=peak,'
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
print(f'{len(vw)} palabras sobre {L:.1f}s')
def wt(word, occ=0):
    ts_ = [w for w in vw if norm(w[2]) == norm(word)]
    if occ >= len(ts_): print(f'aviso: "{word}" n.º {occ} no aparece'); return None
    return ts_[occ]

# 3) los planos: cada uno arranca en su palabra y dura hasta el siguiente
marks = []
for sh in P['shots']:
    word, occ, key = sh[0], sh[1], sh[2]
    badge = sh[3] if len(sh) > 3 else None
    if word is None: marks.append([0.0, key, badge]); continue
    w = wt(word, occ)
    if not w: continue
    marks.append([max(0.0, w[0] - 0.12), key, badge])
marks.sort(key=lambda m: m[0])
shots = []
for i, (t0, key, badge) in enumerate(marks):
    t1 = marks[i + 1][0] if i + 1 < len(marks) else L
    if t1 - t0 < 0.5:
        print(f'aviso: el plano {key} dura {t1-t0:.2f}s, se saltea'); continue
    shots.append((t0, t1, key, badge))
print('planos:', ' '.join(f'{k}:{t1-t0:.1f}s' for t0, t1, k, _ in shots))

parts = []
for n, (t0, t1, key, _b) in enumerate(shots):
    d_ = t1 - t0; pc = f'{tmp}/s{n:02d}.mp4'
    c = P['pages'][key]
    if isinstance(c, str): c = {'src': c}
    src = F(c['src'])
    if src.lower().endswith(('.png', '.jpg', '.jpeg')):
        # regla 29/10: en voz en off no entra ni una foto fija, todo es B-roll de TikTok
        raise SystemExit(f'ERROR: "{key}" es una foto ({os.path.basename(src)}). Los planos son clips, no fotos.')
    ss = c.get('ss', 0.0)
    avail = max(0.3, dur(src) - ss)
    slow = max(1.0, d_ / avail)                           # si el tramo es corto, se estira apenas
    z0 = c.get('zoom', 1.0); yb = c.get('ybias', 0.5)
    vf = (f"setpts={slow:.4f}*(PTS-STARTPTS),fps={FPS},"
          f"scale=w='ceil(max({W}/iw,{H}/ih)*iw*{z0}/2)*2':h=-2:flags=lanczos,"
          f"crop={W}:{H}:(iw-{W})/2:(ih-{H})*{yb},setsar=1,format=yuv420p")
    run([FF, '-v', 'error', '-y', '-ss', str(ss), '-t', f'{min(avail, d_ / slow) + 0.1:.3f}', '-i', src,
         '-an', '-vf', vf, '-t', f'{d_:.3f}',
         '-c:v', 'libx264', '-crf', '18', '-preset', 'fast', pc])
    parts.append(pc)
open(f'{tmp}/all.txt', 'w').write(''.join(f"file '{p}'\n" for p in parts))
run([FF, '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', f'{tmp}/all.txt', '-c', 'copy', f'{tmp}/cat.mp4'])

# 4) hook arriba y placa final (iguales a los del ad con avatar)
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

def png_badge(num, head, path):
    """La placa de pagina del ganador, pero ENCIMA del clip: caja blanca con el titulo y
    una pastilla naranja 'PAGE NN' pisando la esquina. Reemplaza a la hoja dibujada (29/10)."""
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im); f = font(54, FONT_B)
    words, lines, cur = head.upper().split(), [], ''
    for w_ in words:
        t_ = (cur + ' ' + w_).strip()
        if d.textlength(t_, font=f) > 760 and cur: lines.append(cur); cur = w_
        else: cur = t_
    lines.append(cur)
    lw = [d.textlength(l, font=f) for l in lines]
    top = 46 if num else 20                      # con badge, la primera linea arranca mas abajo
    bw, bh = max(max(lw) + 72, 620), len(lines) * 70 + top + 24
    x0, y0 = (W - bw) / 2, 258
    d.rounded_rectangle((x0 + 7, y0 + 10, x0 + bw + 7, y0 + bh + 10), 18, fill=(0, 0, 0, 110))
    d.rounded_rectangle((x0, y0, x0 + bw, y0 + bh), 18, fill=(255, 255, 255, 248))
    for i, l in enumerate(lines):
        d.text(((W - lw[i]) / 2, y0 + top + i * 70), l, font=f, fill=NAVY)
    if not num: im.save(path); return            # placa sin numero: solo la frase
    fb = font(44); t = f'PAGE {num}'
    pw = d.textlength(t, font=fb) + 62
    px, py = x0 + bw - pw + 16, y0 - 42      # la pastilla pisa el borde, nunca el texto
    d.rounded_rectangle((px + 5, py + 8, px + pw + 5, py + 88), 40, fill=(0, 0, 0, 120))
    d.rounded_rectangle((px, py, px + pw, py + 80), 40, fill=ORANGE + (255,))
    d.text((px + 31, py + 17), t, font=fb, fill=NAVY)
    im.save(path)

def png_end(o, path):
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im)
    d.rectangle((0, 0, W, H), fill=NAVY + (242,))
    cx, cy = W // 2, 640
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
for n, (t0, t1, key, b) in enumerate(shots):          # las placas de pagina, encima del clip que les toca
    if not b: continue
    pth = f'{tmp}/o_bg{n}.png'; png_badge(b.get('badge'), b['head'], pth)
    ovs.append((pth, t0 + 0.10, max(t0 + 0.9, t1 - 0.10)))

END = P.get('end'); end_t = L
if END:
    end_t = max(0.0, L - P.get('end_dur', 2.4))
    png_end(END, f'{tmp}/o_end.png'); ovs.append((f'{tmp}/o_end.png', end_t, L))

# 5) subtitulos de una palabra
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

# 6) armado
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
run([FF, '-v', 'error', '-y', '-i', f'{tmp}/cat.mp4', '-i', f'{tmp}/ov.mov', '-filter_complex',
     f"[0:v][1:v]overlay=0:0:format=auto[ov];[ov]ass={tmp}/subs.ass[v]", '-map', '[v]',
     '-c:v', 'libx264', '-crf', '18', '-pix_fmt', 'yuv420p', '-t', f'{L:.2f}', f'{tmp}/video.mp4'])

# 7) cama musical a -8 dB del RMS de la voz
if P.get('music'):
    import numpy as np, soundfile as sf
    m_, sr_ = sf.read(F(P['music'])); v_, _ = sf.read(f'{tmp}/vo.wav')
    if m_.ndim == 1: m_ = np.stack([m_, m_], 1)
    need = int((L + 0.5) * sr_); xf = int(1.0 * sr_)
    while len(m_) < need:
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
print(f'OK {OUT} {L:.1f}s, {len(shots)} planos')
