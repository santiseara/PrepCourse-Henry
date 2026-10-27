"""Ad de voz en off con el estilo de los ads de The Weekend Fabricator (Herrero de Finde, 2026-10-22).
Copia de edit_infinity.py con su estética: etiqueta naranja arriba con el título, chips oscuros de plata
(materiales en blanco, precio de venta en verde), subtítulos Montserrat ExtraBold en mayúscula con la
palabra activa en naranja y placa final "FABRICÁ TRABAJOS COMO ESTOS" + chip verde + CTA naranja.
2026-10-22 (Santiago: "está medio aburrida"): su música (separada de la voz, "music"/"music_db"), golpe de zoom en
cada corte, zoom constante, destello blanco + whoosh cada "flash" cortes, placas que entran saltando, sello
{"type":"stamp","text":"VENDIDA"}, subtítulos con la palabra activa en amarillo y barra de progreso naranja arriba.
Overlays: {"type":"tag","text":"5 TRABAJOS QUE SE VENDEN A +$1.500.000","word":..,"until":..}
          {"type":"money","left":"$961.000","right":"$1.590.000 a $2.070.000","label":"MATERIALES → TE PAGAN","word":..,"dur":2.4}
          {"type":"chip","text":"..","word":..}  {"type":"end","word":"Tocá"}
Antes (Infinity):
Base: edit_broll.py (voz recortada y acelerada, pool de recortes sin repetir, anchors, usage.json).
Lo nuevo: cortes cortos (~2,4 s), fotos fijas de la landing con zoom, caja blanca de hook arriba,
etiquetas naranjas, tarjeta de precio, tarjeta de plano con medidas, subtítulos condensados con la
palabra activa en naranja y placa final (INFINITY 3D + Tap Learn More).
Uso: python3 edit_infinity.py plan.json salida.mp4
plan.json (además de lo de edit_broll.py):
 "clips": {"L00": {"src": "landing/img00.webp", "still": true, "fit": false}}   # fit = foto chica sobre fondo desenfocado
 "hook": "What would you charge for this table? 👀",
 "overlays": [
   {"type": "chip", "text": "8 HOURS IN THE SHOP", "word": "eight", "occ": 0, "dur": 2.0, "icon": "✓"},
   {"type": "price", "label": "FACEBOOK MARKETPLACE · OCT 2026", "title": "LED coffee table 39×24", "price": "$495", "word": "Marketplace", "dur": 2.6},
   {"type": "plan", "title": "COFFEE TABLE 39″ × 24″", "rows": [["SIDES", "39 × 6 · ×2"]], "word": "Coffee", "until": "melamine"},
   {"type": "end", "word": "Tap", "sub": "26 plans + 5 bonuses · instant access", "cta": "Tap Learn More 👇"}]
"""
import os, re, sys, json, subprocess, difflib, random
from faster_whisper import WhisperModel
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FF = os.path.expanduser('~/bin/ffmpeg')
DIR = os.path.dirname(os.path.abspath(__file__))
P = json.load(open(sys.argv[1])); OUT = sys.argv[2]
base = os.path.dirname(os.path.abspath(sys.argv[1]))
def F(p): return p if os.path.isabs(p) else os.path.join(base, p)
tmp = os.path.join(base, os.path.basename(OUT) + '_tmp'); os.makedirs(tmp, exist_ok=True)
W, H, FPS = 1080, 1920, 30
ORANGE = (226, 86, 27)     # --rust de la landing
GREEN = (95, 201, 126)     # --ok
AMBER = (242, 163, 60)     # --amber
INK = (247, 243, 238)      # --ink
BGD = (15, 13, 11)         # --bg
PANEL = (28, 25, 22)       # --panel
BP = (12, 22, 32)          # --blueprint
BPL = (46, 90, 122)        # --bp-line
BPI = (207, 230, 245)      # --bp-ink
FD = os.path.expanduser('~/Desktop/herrero-de-finde/anuncios/work/fonts')
BC = FD + '/BarlowCondensed-ExtraBold.ttf'
MX = FD + '/Montserrat-ExtraBold.ttf'
FONT = '/System/Library/Fonts/Supplemental/DIN Condensed Bold.ttf'
FONT_B = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
EMOJI = '/System/Library/Fonts/Apple Color Emoji.ttc'
ICONF = '/System/Library/Fonts/Supplemental/Arial Unicode.ttf'
def run(c): subprocess.run(c, check=True)
def norm(w): return re.sub(r'[^\w]', '', w.lower())

# 1) voz: recorte de silencios + velocidad, palabras alineadas al guion
sp = P.get('speed', 1.15)
run([FF, '-v', 'error', '-y', '-i', F(P['vo']), '-af',
     'silenceremove=start_periods=1:start_threshold=-55dB:stop_periods=-1:stop_duration=0.6:stop_threshold=-55dB:stop_silence=0.35,'
     f'atempo={sp:.4f},aresample=48000,afade=t=in:d=0.02', '-ac', '2', f'{tmp}/vo.wav'])   # solo acorta pausas largas (antes cortaba colas de palabras)
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
def dur(p):
    r = subprocess.run([FF, '-i', p], capture_output=True, text=True).stderr
    h, m, s = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r).groups(); return int(h) * 3600 + int(m) * 60 + float(s)
L = dur(f'{tmp}/vo.wav') + 0.5
def wt(word, occ=0):
    ts_ = [w for w in vw if norm(w[2]) == norm(word)]
    if occ >= len(ts_): print(f'aviso: "{word}" n.º {occ} no aparece'); return None
    return ts_[occ]

# 2) puntos de corte: cerca del ideal, siempre al final de una palabra (mejor si cierra frase)
mn, ideal, mx = P.get('cut', [1.8, 2.4, 3.0])
cuts, t = [0.0], 0.0
while L - t > mx:
    cand = [w for w in vw if t + mn <= w[1] <= t + mx]
    if not cand: t += ideal; cuts.append(t); continue
    best = min(cand, key=lambda w: abs(w[1] - (t + ideal)) - (0.5 if re.search(r'[.?!,]$', w[2]) else 0))
    t = best[1] + 0.04; cuts.append(t)
cuts.append(L)
# los anchors arrancan justo cuando se dice la palabra (antes la ficha podía quedar casi entera antes de la palabra)
for word, occ, key, st in P.get('anchors', []):
    w = wt(word, occ)
    if not w: continue
    tg = w[0] - 0.06; j = min(range(1, len(cuts) - 1), key=lambda i: abs(cuts[i] - tg), default=None)
    if j is None or abs(cuts[j] - tg) < 0.08: continue
    if abs(cuts[j] - tg) < 0.7 and cuts[j - 1] + 0.7 < tg < cuts[j + 1] - 0.7: cuts[j] = tg
    else:
        k = max(i for i in range(len(cuts) - 1) if cuts[i] <= tg)
        if cuts[k] + 0.7 < tg < cuts[k + 1] - 0.7: cuts.insert(k + 1, tg)

# 3) plan de planos (pool sin repetir, anchors, usage.json compartido entre videos)
rnd = random.Random(P.get('seed', 0))
upath = F(P['usage']) if 'usage' in P else None
usage = json.load(open(upath)) if upath and os.path.exists(upath) else {}
used, plan, forced = set(), [], {}
for word, occ, key, st in P.get('anchors', []):
    w = wt(word, occ)
    if not w: continue
    n = max(i for i in range(len(cuts) - 1) if cuts[i] <= w[0] + 0.05)
    if n in forced or forced.get(n - 1, [''])[0] == key or forced.get(n + 1, [''])[0] == key:
        print(f'aviso: anchor "{word}" choca con otro en el plano {n}, se ignora'); continue
    forced[n] = next((s for s in P['pool'] if s[0] == key and s[1] == st), None) or next(s for s in P['pool'] if s[0] == key)
for s in forced.values(): used.add(f'{s[0]}@{s[1]}')
for n in range(len(cuts) - 1):
    d = cuts[n + 1] - cuts[n]
    prev = [p[0] for p in plan[-2:]]
    if n in forced:
        seg = forced[n]
    elif n == 0 and 'first' in P:
        seg = next(s for s in P['pool'] if s[0] == P['first'][0] and s[1] == P['first'][1])
    else:
        nxt = forced[n + 1][0] if n + 1 in forced else None
        cand = [s for s in P['pool'] if f'{s[0]}@{s[1]}' not in used and s[0][:1] not in [q[:1] for q in prev[-1:]] and s[0][:1] != (nxt or ' ')[:1]]
        here = {}
        for p in plan: here[p[0][:1]] = here.get(p[0][:1], 0) + 1     # misma fuente = misma letra inicial
        def score(s):
            return (usage.get(f'{s[0]}@{s[1]}', 0) * 10 + here.get(s[0][:1], 0) * 30 + (12 if s[0] in prev else 0)
                    + (6 if s[2] - s[1] < d * 0.75 else 0) + rnd.random())
        seg = min(cand, key=score)
    sid = f'{seg[0]}@{seg[1]}'; used.add(sid)
    plan.append((seg[0], seg[1], seg[2], usage.get(sid, 0) % 2 == 1 and not P['clips'][seg[0]].get('still') and not P['clips'][seg[0]].get('noflip')))   # fotos y demos de pantalla nunca se espejan (tienen texto)
    usage[sid] = usage.get(sid, 0) + 1
if upath: json.dump(usage, open(upath, 'w'), indent=0)
print('planos:', ' '.join(f'{k}:{s:g}{"↔" if f else ""}' for k, s, e, f in plan))
if os.environ.get('DEBUG'): print('cortes:', ' '.join(f'{c:.2f}' for c in cuts)); sys.exit()

hits = []     # (sonido, t)
parts = []
for n in range(len(cuts) - 1):
    d = cuts[n + 1] - cuts[n]
    key, st, end, flip = plan[n]
    c = P['clips'][key]; src = F(c['src'])
    zin = n % 2 == 0
    punch = f"(1+0.16*max(0,1-t/0.22))" if n > 0 else "1"     # golpe de zoom en cada corte
    fl = P.get('flash', 0); flash = n > 0 and fl and n % fl == 0
    fx = f",fade=t=in:st=0:d=0.18:color=white" if flash else ''
    if flash: hits.append(('whoosh', cuts[n] - 0.2))
    if c.get('still'):
        z = (f"(1+0.14*t/{d:.3f})" if zin else f"(1.14-0.14*t/{d:.3f})") + f"*{punch}"
        if c.get('fit'):      # foto chica: centrada a lo ancho sobre la misma foto desenfocada
            vf = (f"color=c=0x0F0D0B:s={W}x{H}:d={d:.3f}[bg];[0:v]scale={int(W * P.get('fit_w', 1.0)) // 2 * 2 - 40 * (P.get('fit_w', 1.0) == 1.0)}:-2[fg];[bg][fg]overlay=(W-w)/2:{P.get('fit_y', 360)},fps={FPS},"
                  f"scale=w='{2*W}*{z}':h=-2:eval=frame:flags=bicubic,crop={2*W}:{2*H}:(iw-{2*W})/2:(ih-{2*H})/2,scale={W}:{H}:flags=lanczos,{'hflip,' if flip else ''}setsar=1,format=yuv420p{fx}")
        else:
            vf = (f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},"
                  f"scale=w='{2*W}*{z}':h=-2:eval=frame:flags=bicubic,crop={2*W}:{2*H}:(iw-{2*W})/2:(ih-{2*H})/2,scale={W}:{H}:flags=lanczos,{'hflip,' if flip else ''}setsar=1,format=yuv420p{fx}")
        pc = f'{tmp}/s{n:02d}.mp4'
        run([FF, '-v', 'error', '-y', '-loop', '1', '-t', f'{d:.3f}', '-i', src, '-filter_complex', vf,
             '-t', f'{d:.3f}', '-r', str(FPS), '-c:v', 'libx264', '-crf', '18', '-preset', 'fast', pc])
        parts.append(pc); continue
    end = min(end, dur(src))
    avail = end - st
    slow = max(1.0, d / avail) if avail > 0 else 1.0
    z0 = c.get('zoom', 1.0); yb = c.get('ybias', 0.5)
    vf = (f"setpts={slow:.4f}*(PTS-STARTPTS),fps={FPS},"
          f"scale=w='ceil(max({W}/iw,{H}/ih)*iw*{z0}*(1+0.07*t/{d:.3f})*{punch}/2)*2':h=-2:eval=frame:flags=bicubic,"
          f"crop={W}:{H}:(iw-{W})/2:(ih-{H})*{yb},{'hflip,' if flip else ''}setsar=1,format=yuv420p{fx}")
    pc = f'{tmp}/s{n:02d}.mp4'
    run([FF, '-v', 'error', '-y', '-ss', str(st), '-t', f'{min(avail, d / slow) + 0.1:.3f}', '-i', src, '-an',
         '-vf', vf, '-t', f'{d:.3f}', '-c:v', 'libx264', '-crf', '18', '-preset', 'fast', pc])
    parts.append(pc)
lst = f'{tmp}/all.txt'; open(lst, 'w').write(''.join(f"file '{p}'\n" for p in parts))
run([FF, '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', f'{tmp}/cat.mp4'])

# 4) placas en PNG (hook, etiquetas, precio, plano, placa final)
def font(sz, path=FONT): return ImageFont.truetype(path, sz)
def emoji_img(ch, h):
    try:
        f = ImageFont.truetype(EMOJI, 160)
        im = Image.new('RGBA', (200, 200)); ImageDraw.Draw(im).text((0, 0), ch, font=f, embedded_color=True)
        im = im.crop(im.getbbox()); return im.resize((int(im.width * h / im.height), h), Image.LANCZOS)
    except Exception: return None
def split_emoji(txt):
    m = re.search(r'\s*([\U0001F300-\U0001FAFF☀-➿]️?)\s*$', txt)
    return (txt[:m.start()], m.group(1)) if m else (txt, None)
def rrect(d, box, r, fill, outline=None, width=0): d.rounded_rectangle(box, r, fill=fill, outline=outline, width=width)


def png_tag(txt, path, y0=210):
    """Etiqueta estilo plano: panel blueprint con grilla y filete rust (antes: caja naranja llena)."""
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im); f = font(92, BC)
    words, lines, cur = txt.upper().split(), [], ''
    for w_ in words:
        t_ = (cur + ' ' + w_).strip()
        if d.textlength(t_, font=f) > 830 and cur: lines.append(cur); cur = w_
        else: cur = t_
    lines.append(cur)
    bw = max(d.textlength(l, font=f) for l in lines) + 120; bh = len(lines) * 96 + 60
    x0 = (W - bw) / 2
    d.rectangle((x0 + 10, y0 + 12, x0 + bw + 10, y0 + bh + 12), fill=(0, 0, 0, 120))
    d.rectangle((x0, y0, x0 + bw, y0 + bh), fill=BP + (242,))
    for gx in range(int(x0) + 26, int(x0 + bw) - 10, 46): d.line([(gx, y0 + 8), (gx, y0 + bh - 8)], fill=BPL + (60,))
    for gy in range(int(y0) + 26, int(y0 + bh) - 10, 46): d.line([(x0 + 8, gy), (x0 + bw - 8, gy)], fill=BPL + (60,))
    d.rectangle((x0, y0, x0 + bw, y0 + bh), outline=BPL + (255,), width=3)
    d.rectangle((x0, y0, x0 + 16, y0 + bh), fill=ORANGE + (255,))
    for i, l in enumerate(lines):
        d.text((W / 2 + 8, y0 + 26 + i * 96), l, font=f, fill=INK + (255,), anchor='mt')
    im.save(path)


def png_hero(txt, path, y0=250):
    """Placa de apertura con el hero de la landing: eyebrow rust + titular en ink."""
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im)
    eyebrow = 'HERRERO DE FINDE'
    f = font(100, BC); fe = font(40, MX)
    words, lines, cur = txt.upper().split(), [], ''
    for w_ in words:
        t_ = (cur + ' ' + w_).strip()
        if d.textlength(t_, font=f) > 850 and cur: lines.append(cur); cur = w_
        else: cur = t_
    lines.append(cur)
    bw = max([d.textlength(l, font=f) for l in lines] + [d.textlength(eyebrow, font=fe)]) + 110
    bh = len(lines) * 104 + 150
    x0 = (W - bw) / 2
    d.rectangle((x0 + 10, y0 + 12, x0 + bw + 10, y0 + bh + 12), fill=(0, 0, 0, 130))
    d.rectangle((x0, y0, x0 + bw, y0 + bh), fill=BGD + (242,))
    d.rectangle((x0, y0, x0 + bw, y0 + bh), outline=(51, 44, 36, 255), width=3)
    d.text((W / 2, y0 + 34), eyebrow, font=fe, fill=ORANGE + (255,), anchor='mt')
    for i, l in enumerate(lines):
        d.text((W / 2, y0 + 104 + i * 104), l, font=f, fill=INK + (255,), anchor='mt')
    d.rectangle((W / 2 - 90, y0 + bh - 34, W / 2 + 90, y0 + bh - 24), fill=ORANGE + (255,))
    im.save(path)


def png_money(o, path):
    """Cotizacion: panel oscuro con filete rust, hierro en ink y precio de venta en verde."""
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im)
    fl = font(40, MX); a_, b_ = o['left'], o.get('right', '')
    sz = 92
    while True:
        fa = font(sz, BC); fb = fa; fr = font(int(sz * 0.8), ICONF); arrow = '  \u2192  ' if b_ else ''
        tw = d.textlength(a_, font=fa) + d.textlength(arrow, font=fr) + d.textlength(b_, font=fb)
        if tw <= W - 160 or sz <= 50: break
        sz -= 4
    bw = max(tw, d.textlength(o.get('label', ''), font=fl)) + 90; bh = 210 if o.get('label') else 150
    x0, y0 = (W - bw) / 2, o.get('y', 1480)
    d.rectangle((x0 + 8, y0 + 10, x0 + bw + 8, y0 + bh + 10), fill=(0, 0, 0, 120))
    rrect(d, (x0, y0, x0 + bw, y0 + bh), 10, PANEL + (246,))
    d.rectangle((x0, y0, x0 + bw, y0 + 7), fill=ORANGE + (255,))
    if o.get('label'): d.text((W / 2, y0 + 30), o['label'], font=fl, fill=AMBER + (255,), anchor='mt')
    x = (W - tw) / 2; y = y0 + (92 if o.get('label') else 30)
    d.text((x, y), a_, font=fa, fill=INK + (255,)); x += d.textlength(a_, font=fa)
    if b_:
        d.text((x, y + sz * 0.12), arrow, font=fr, fill=AMBER + (255,)); x += d.textlength(arrow, font=fr)
        d.text((x, y), b_, font=fb, fill=GREEN + (255,))
    im.save(path)

def png_hook(txt, path):
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im)
    body, emo = split_emoji(txt); f = font(72, FONT_B)
    words, lines, cur = body.split(), [], ''
    for w_ in words:
        t_ = (cur + ' ' + w_).strip()
        if d.textlength(t_, font=f) > 820 and cur: lines.append(cur); cur = w_
        else: cur = t_
    lines.append(cur)
    em = emoji_img(emo, 68) if emo else None
    lw = [d.textlength(l, font=f) + (em.width + 14 if em and i == len(lines) - 1 else 0) for i, l in enumerate(lines)]
    bw, bh = max(lw) + 90, len(lines) * 88 + 56
    x0, y0 = (W - bw) / 2, 250
    rrect(d, (x0, y0, x0 + bw, y0 + bh), 26, (255, 255, 255, 250))
    for i, l in enumerate(lines):
        y = y0 + 28 + i * 88; x = (W - lw[i]) / 2
        d.text((x, y), l, font=f, fill=(20, 20, 20))
        if em and i == len(lines) - 1: im.alpha_composite(em, (int(x + d.textlength(l, font=f) + 14), int(y + 4)))
    im.save(path)


def png_chip(txt, icon, path):
    """Chip de dato: panel oscuro con borde fino de plano y tilde verde."""
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im); f = font(74, BC)
    t_ = txt.upper(); fi = font(52, ICONF)
    emo = emoji_img(icon, 56) if icon and ord(icon[0]) > 0x1F000 else None
    iw = (emo.width + 16) if emo else ((d.textlength(icon, font=fi) + 16) if icon else 0)
    while d.textlength(t_, font=f) + iw > W - 160 and f.size > 40: f = font(f.size - 4, BC)
    tw = d.textlength(t_, font=f) + iw; bw, bh = tw + 76, 100
    x0, y0 = (W - bw) / 2, 1500
    d.rectangle((x0 + 7, y0 + 9, x0 + bw + 7, y0 + bh + 9), fill=(0, 0, 0, 110))
    rrect(d, (x0, y0, x0 + bw, y0 + bh), 10, PANEL + (246,))
    d.rounded_rectangle((x0, y0, x0 + bw, y0 + bh), 10, outline=BPL + (200,), width=3)
    if emo: im.alpha_composite(emo, (int(x0 + 38), int(y0 + 22)))
    elif icon: d.text((x0 + 38, y0 + 18), icon, font=fi, fill=GREEN + (255,))
    d.text((x0 + 38 + iw, y0 + 14), t_, font=f, fill=INK + (255,))
    im.save(path)

def png_price(o, path):
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im)
    bw, bh = 820, 380; x0, y0 = (W - bw) / 2, 260
    rrect(d, (x0, y0, x0 + bw, y0 + bh), 28, (14, 10, 8, 235), outline=ORANGE + (255,), width=5)
    def ctr(t_, f, y, col): d.text(((W - d.textlength(t_, font=f)) / 2, y), t_, font=f, fill=col)
    ctr(o.get('label', ''), font(42), y0 + 34, ORANGE)
    ctr(o.get('title', ''), font(58), y0 + 92, (255, 255, 255))
    ctr(o['price'], font(170), y0 + 160, (255, 255, 255))
    if o.get('foot'): ctr(o['foot'], font(34), y0 + bh - 52, (190, 190, 190))
    im.save(path)

def png_plan(o, path):
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im)
    rows = o['rows']; bw, bh = 880, 190 + 92 * len(rows); x0, y0 = (W - bw) / 2, 200
    rrect(d, (x0, y0, x0 + bw, y0 + bh), 28, (12, 9, 7, 240), outline=ORANGE + (255,), width=4)
    lab = o.get('label', 'PLAN 01 · MEASUREMENTS IN INCHES'); f = font(36)
    lw = d.textlength(lab, font=f) + 40
    rrect(d, ((W - lw) / 2, y0 + 26, (W + lw) / 2, y0 + 78), 26, ORANGE + (255,))
    d.text(((W - lw) / 2 + 20, y0 + 36), lab, font=f, fill=(25, 15, 5))
    ft = font(80); d.text(((W - d.textlength(o['title'], font=ft)) / 2, y0 + 96), o['title'], font=ft, fill=(255, 255, 255))
    for i, (k, v) in enumerate(rows):
        y = y0 + 196 + i * 92
        rrect(d, (x0 + 40, y, x0 + bw - 40, y + 76), 12, (255, 138, 31, 30), outline=ORANGE + (200,), width=3)
        d.text((x0 + 70, y + 14), k, font=font(54), fill=(255, 255, 255))
        fv = font(54); d.text((x0 + bw - 70 - d.textlength(v, font=fv), y + 14), v, font=fv, fill=ORANGE)
    im.save(path)

def png_stamp(o, path):
    f = font(150, BC); t_ = o['text'].upper()
    tw = int(ImageDraw.Draw(Image.new('RGBA', (1, 1))).textlength(t_, font=f))
    st = Image.new('RGBA', (tw + 120, 250)); d = ImageDraw.Draw(st)
    d.rounded_rectangle((10, 10, tw + 110, 240), 22, outline=GREEN + (255,), width=14, fill=(46, 204, 113, 40))
    d.text(((tw + 120) / 2, 125), t_, font=f, fill=GREEN + (255,), anchor='mm')
    st = st.rotate(14, expand=True, resample=Image.BICUBIC)
    im = Image.new('RGBA', (W, H)); im.alpha_composite(st, ((W - st.width) // 2 + 120, o.get('y', 700)))
    im.save(path)


def png_end(o, path):
    """Cierre con la marca de la landing: logo, chip de garantia y boton rust."""
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im)
    g = Image.new('RGBA', (W, H)); gd = ImageDraw.Draw(g)
    for y in range(0, 1200):
        gd.line([(0, y + 250), (W, y + 250)], fill=(0, 0, 0, int(160 * max(0, 1 - abs(y - 460) / 650))))
    im.alpha_composite(g)
    im.alpha_composite(Image.new('RGBA', (W, H), BGD + (205,)))
    fl = font(130, BC); y = 420
    t1, t2 = 'HERRERO DE ', 'FINDE'
    w1, w2 = d.textlength(t1, font=fl), d.textlength(t2, font=fl)
    x = (W - w1 - w2) / 2
    d.text((x, y), t1, font=fl, fill=INK + (255,)); d.text((x + w1, y), t2, font=fl, fill=ORANGE + (255,))
    y += 180
    fg = font(66, BC); g2 = o.get('sub', '+1.200 PLANOS · 12 BONUS'); gw = d.textlength(g2, font=fg) + 70
    rrect(d, ((W - gw) / 2, y, (W + gw) / 2, y + 96), 10, GREEN + (255,))
    d.text((W / 2, y + 12), g2, font=fg, fill=(8, 26, 14, 255), anchor='mt')
    fs = font(40, MX); s2 = o.get('sub2', 'QUÉ CORTAR · CUÁNTO HIERRO · CUÁNTO COBRAR')
    d.text((W / 2, y + 128), s2, font=fs, fill=BPI + (255,), anchor='mt')
    body, emo = split_emoji(o.get('cta', 'Tocá Más información')); fc = font(66, MX)
    em = emoji_img(emo, 58) if emo else None
    cw = d.textlength(body, font=fc) + (em.width + 14 if em else 0); bw = cw + 90
    x0, y0 = (W - bw) / 2, y + 230
    rrect(d, (x0, y0, x0 + bw, y0 + 108), 54, ORANGE + (255,))
    d.text((x0 + 45, y0 + 26), body, font=fc, fill=(255, 255, 255))
    if em: im.alpha_composite(em, (int(x0 + 45 + d.textlength(body, font=fc) + 14), int(y0 + 24)))
    fgar = font(38, MX)
    d.text((W / 2, y0 + 150), o.get('foot', '60 DÍAS DE GARANTÍA · UN SOLO PAGO'), font=fgar, fill=(190, 185, 178, 255), anchor='mt')
    im.save(path)

ovs = []      # (png, t0, t1, anima)
if P.get('hook'):
    png_hero(P['hook'], f'{tmp}/o_hook.png')
    hu = wt(P['hook_until'], P.get('hook_until_occ', 0)) if P.get('hook_until') else None
    ovs.append((f'{tmp}/o_hook.png', 0, hu[1] + 0.15 if hu else (min(cuts[1] + 0.6, 2.8) if len(cuts) > 2 else 2.6), True))
for k, o in enumerate(P.get('overlays', [])):
    w = wt(o['word'], o.get('occ', 0))
    if not w: continue
    t0 = w[0] - 0.05; pth = f'{tmp}/o{k}.png'
    if o['type'] == 'chip': png_chip(o['text'], o.get('icon', ''), pth); hits.append(('pop', t0))
    elif o['type'] == 'tag': png_tag(o['text'], pth, o.get('y', 210)); hits.append(('pop', t0))
    elif o['type'] == 'money': png_money(o, pth); hits.append(('chaching', t0 + 0.15))
    elif o['type'] == 'price': png_price(o, pth); hits.append(('chaching', t0 + 0.25))
    elif o['type'] == 'plan': png_plan(o, pth); hits.append(('pop', t0))
    elif o['type'] == 'stamp': t0 += o.get('delay', 0.6); png_stamp(o, pth); hits.append(('sello', t0))
    elif o['type'] == 'end': png_end(o, pth); hits.append(('ding', t0))
    if o['type'] == 'end': t1 = L
    elif o.get('until'):
        u = wt(o['until'], o.get('until_occ', 0)); t1 = u[1] + 0.2 if u else t0 + o.get('dur', 2.2)
    else: t1 = t0 + o.get('dur', 2.2)
    if o['type'] == 'stamp': t1 = min(t1, min([c for c in cuts if c > t0 + 0.1] or [L]) - 0.02)   # el sello no pasa al plano siguiente
    ovs.append((pth, t0, t1, o['type'] != 'end'))

# 5) subtítulos (3 palabras, DIN condensada, la que suena en naranja); se ocultan bajo la placa final
def ts(t): t = max(0, t); return f'{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}'
CAPY = P.get('capy', 1380)
HI = P.get('hi', '&H0021D2FF&')
end_t = min([t0 for p, t0, t1, a in ovs if t1 == L] or [L + 1])
ass = [f'''[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: C,Montserrat ExtraBold,102,&H00FFFFFF,&H00FFFFFF,&H00000000,&H90000000,0,0,0,0,100,100,0,0,1,6,5,5,60,60,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text''']
def clean(w): return w.replace('…', '').strip(' ,;:"“”').upper()
chunks, cur = [], []
for x in vw:
    cur.append(x)
    if len(cur) == P.get('words', 2) or re.search(r'[.?!…]$', x[2]): chunks.append(cur); cur = []
if cur: chunks.append(cur)
for ci, ch in enumerate(chunks):
    if ch[0][0] >= end_t - 0.05: continue
    nxt = chunks[ci + 1][0][0] if ci + 1 < len(chunks) else ch[-1][1] + 0.4
    for wi, (s, e, w) in enumerate(ch):
        e2 = ch[wi + 1][0] if wi + 1 < len(ch) else min(nxt, ch[-1][1] + 0.5)
        e2 = min(e2, end_t)
        pop = '{\\fscx118\\fscy118\\t(0,90,\\fscx100\\fscy100)}' if wi == 0 else ''
        txt = pop + ' '.join((f'{{\\c{HI}}}' + clean(x[2]) + '{\\r}') if j == wi else clean(x[2]) for j, x in enumerate(ch))
        ass.append(f'Dialogue: 0,{ts(s)},{ts(e2)},C,,0,0,0,,{{\\pos({W // 2},{CAPY})}}{txt}')
open(f'{tmp}/subs.ass', 'w').write('\n'.join(ass) + '\n')

# 6) música baja + efectos puntuales
if P.get('music'):
    import numpy as np, soundfile as sf
    m_, sr_ = sf.read(F(P['music'])); v_, _ = sf.read(f'{tmp}/vo.wav')
    if m_.ndim == 1: m_ = np.stack([m_, m_], 1)
    need = int((L + 1) * sr_); xf = int(1.0 * sr_)
    while len(m_) < need:      # loop con fundido de 1 s desde el segundo 4
        a2 = m_[int(4 * sr_):]; r_ = np.linspace(0, 1, xf)[:, None]
        m_ = np.concatenate([m_[:-xf], m_[-xf:] * (1 - r_) + a2[:xf] * r_, a2[xf:]])
    m_ = m_[:need]
    rv = np.sqrt(np.mean(v_[v_.any(1) if v_.ndim > 1 else v_ != 0] ** 2)); rm = np.sqrt(np.mean(m_ ** 2))
    m_ = m_ * (rv / rm) * 10 ** (P.get('music_db', -8) / 20)
    sf.write(f'{tmp}/music.wav', np.clip(m_, -1, 1), sr_); MVOL = 1.0
else:
    run(['python3', os.path.join(DIR, 'music.py'), f'{L + 1:.2f}', f'{tmp}/music.wav']); MVOL = 0.10
if not os.path.exists(f'{tmp}/sfx/whoosh.wav'): run(['python3', os.path.join(DIR, 'sfx.py'), f'{tmp}/sfx'])
VOL = {'chaching': 0.30, 'ding': 0.26, 'pop': 0.26, 'whoosh': 0.30, 'sello': 0.40}
if isinstance(P.get('whoosh', [1]), list): hits += [('whoosh', cuts[i] - 0.18) for i in P.get('whoosh', [1]) if 0 < i < len(cuts) - 1]
for snd, word, occ in P.get('sfx', []):
    w = wt(word, occ)
    if w: hits.append((snd, w[0] - 0.05))
# pista única de placas: un PNG por tramo con las placas activas, en un .mov con alfa
POPS = [0.72, 0.9, 1.08, 1.03]
edges = sorted({0.0, L} | {max(0, min(L, x)) for _, t0, t1, a in ovs for x in (t0, t1)}
               | {min(L, t0 + k / FPS) for _, t0, t1, a in ovs if a for k in range(1, len(POPS) + 1)})
def popped(p_, sc):
    im = Image.open(p_).convert('RGBA')
    if sc == 1: return im
    bb = im.getbbox(); piece = im.crop(bb)
    piece = piece.resize((max(1, int(piece.width * sc)), max(1, int(piece.height * sc))), Image.BICUBIC)
    cx, cy = (bb[0] + bb[2]) / 2, (bb[1] + bb[3]) / 2
    out = Image.new('RGBA', (W, H)); out.alpha_composite(piece.crop((0, 0, min(piece.width, W), min(piece.height, H))), (max(0, int(cx - piece.width / 2)), max(0, int(cy - piece.height / 2))))
    return out
blank = Image.new('RGBA', (W, H)); cache, lines_ = {}, []
for k in range(len(edges) - 1):
    a_, b_ = edges[k], edges[k + 1]
    if b_ - a_ < 0.01: continue
    act = tuple((i, POPS[int(round((a_ - ovs[i][1]) * FPS))] if ovs[i][3] and round((a_ - ovs[i][1]) * FPS) < len(POPS) else 1)
                for i, (p_, t0, t1, an) in enumerate(ovs) if t0 <= a_ + 1e-3 and t1 >= b_ - 1e-3)
    if act not in cache:
        im = blank.copy()
        for i, sc in act: im.alpha_composite(popped(ovs[i][0], sc))
        cache[act] = f'{tmp}/ov_{len(cache)}.png'; im.save(cache[act])
    lines_.append(f"file '{cache[act]}'\nduration {b_ - a_:.3f}\n")
lines_.append(f"file '{cache[act]}'\n")
open(f'{tmp}/ov.txt', 'w').write(''.join(lines_))
run([FF, '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', f'{tmp}/ov.txt', '-vf', f'fps={FPS},format=argb',
     '-t', f'{L:.2f}', '-c:v', 'qtrle', f'{tmp}/ov.mov'])
# en dos pasos: con todo junto en un solo filtro, ffmpeg tiraba pedazos de audio (la voz quedaba 1-2 s más corta)
if P.get('progress'):     # regla de medidas arriba (ticks fijos + barra rust que avanza)
    rl = Image.new('RGBA', (W, 30), BGD + (210,)); dr = ImageDraw.Draw(rl)
    for x_ in range(0, W, 24):
        dr.line([(x_, 30), (x_, 30 - (16 if x_ % 120 == 0 else 8))], fill=BPI + (170,), width=2)
    rl.save(f'{tmp}/regla.png')
pb = (f"color=c=0x{'%02X%02X%02X' % ORANGE}:s={W}x30:r={FPS}[pb];[s0][pb]overlay=x='-W+W*t/{L:.3f}':y=0:shortest=1[s1];"
      f"[s1][2:v]overlay=0:0:shortest=1[v]" if P.get('progress') else "[s0]null[v]")
run([FF, '-v', 'error', '-y', '-i', f'{tmp}/cat.mp4', '-i', f'{tmp}/ov.mov']
    + (['-loop', '1', '-i', f'{tmp}/regla.png'] if P.get('progress') else []) + ['-filter_complex',
     f"[0:v][1:v]overlay=0:0:format=auto[ov];[ov]ass={tmp}/subs.ass:fontsdir={FD}[s0];" + pb,
     '-map', '[v]',
     '-c:v', 'libx264', '-crf', '18', '-pix_fmt', 'yuv420p', '-t', f'{L:.2f}', f'{tmp}/video.mp4'])
ains = ['-i', f'{tmp}/vo.wav', '-i', f'{tmp}/music.wav'] + sum([['-i', f'{tmp}/sfx/{s_}.wav'] for s_, _ in hits], [])
afc = [f"[1:a]aresample=48000,volume={MVOL},afade=t=out:st={max(0, L - 1.2):.2f}:d=1.2[m]"]
for k, (s_, t) in enumerate(hits):
    ms = int(max(0, t) * 1000)
    afc.append(f"[{2 + k}:a]aresample=48000,volume={VOL[s_]},adelay={ms}|{ms}[w{k}]")
afc.append(f"[0:a]apad=pad_dur=1[vo];[vo][m]{''.join(f'[w{k}]' for k in range(len(hits)))}amix=inputs={2 + len(hits)}:duration=first:normalize=0[a]")
run([FF, '-v', 'error', '-y'] + ains + ['-filter_complex', ';'.join(afc), '-map', '[a]', '-t', f'{L:.2f}', f'{tmp}/mix.wav'])
run([FF, '-v', 'error', '-y', '-i', f'{tmp}/video.mp4', '-i', f'{tmp}/mix.wav', '-map', '0:v', '-map', '1:a',
     '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', f'{L:.2f}', '-movflags', '+faststart', OUT])
print(f'OK {OUT} {L:.1f}s, {len(cuts) - 1} planos (promedio {L / (len(cuts) - 1):.1f}s)')
