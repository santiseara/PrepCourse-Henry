"""Ad de voz en off de Carteras Maison / el Metodo Riviera (Argentina, 2026-11-10):
copia de edit_epoxi.py con la edicion de Maison Luxe Bags clonada.

Lo que copia del ganador:
  - Subtitulos de 2 palabras EN MAYUSCULA, blancos con borde negro grueso y la palabra activa
    en MAGENTA (sin caja): es exactamente su resalte.
  - Placa de texto arriba en los cortos ("MIRA COMO UNA PLANCHA DE PLASTICO SE VUELVE UNA CARTERA").
  - Los insertos del producto (gfx_carteras.py) anclados a la palabra que los nombra.
  - Placa de cierre con el celular y el boton.

Uso: python3 edit_carteras.py plan.json salida.mp4
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
ORANGE = (212, 53, 111)        # magenta #D4356F: el resalte de Maison Luxe Bags
GOLD = (255, 255, 255)         # blanco: pastilla de la placa final
GREEN = (28, 24, 22)           # tinta #1C1816: arranque del degradado de la placa de cierre
MAG = (142, 31, 73)            # vino #8E1F49: cierre del degradado
FD = os.path.expanduser('~/Desktop/carteras-maison/anuncios/work/fonts')
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
sd, ss_ = P.get('silence', [0.26, 0.12])
run([FF, '-v', 'error', '-y', '-i', F(P['vo']), '-af',
     f'silenceremove=start_periods=1:start_threshold=-55dB:stop_periods=-1:stop_duration={sd}:stop_threshold=-55dB:stop_silence={ss_},'
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
if P.get('last'):   # ultimo plano fijo: asi el cierre (la tapa del ebook) nunca queda tapado por otro
    forced[len(cuts) - 2] = next(s for s in P['pool'] if s[0] == P['last'])
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
            return (usage.get(f'{s[0]}@{s[1]}', 0) * 10 + here.get(s[0][:1], 0) * 3 + (3 if s[0] in prev else 0)
                    + (6 if s[2] - s[1] < d * 0.75 else 0) + rnd.random())
        seg = min(cand, key=score)
    sid = f'{seg[0]}@{seg[1]}'; used.add(sid)
    plan.append((seg[0], seg[1], seg[2], usage.get(sid, 0) % 2 == 1 and not P['clips'][seg[0]].get('still')))   # las fotos nunca se espejan (tienen texto)
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
            vf = (f"color=c=0xF4F2EE:s={W}x{H}:d={d:.3f}[bg];[0:v]scale={int(W * P.get('fit_w', 1.0)) // 2 * 2 - 40 * (P.get('fit_w', 1.0) == 1.0)}:-2[fg];[bg][fg]overlay=(W-w)/2:{P.get('fit_y', 360)},fps={FPS},"
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

def png_tag(txt, path, y0=190):
    """Pastilla redondeada rosa con texto blanco en mayuscula, arriba: el chip de Deco Magic."""
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im)
    t_ = txt.upper(); fs = 64
    while fs > 34 and d.textlength(t_, font=font(fs, MX)) > 820: fs -= 2
    f = font(fs, MX)
    tw = d.textlength(t_, font=f); bw = tw + 74; bh = fs + 42
    x0 = (W - bw) / 2
    d.rounded_rectangle((x0 + 6, y0 + 8, x0 + bw + 6, y0 + bh + 8), bh / 2, fill=(0, 0, 0, 110))
    rrect(d, (x0, y0, x0 + bw, y0 + bh), bh / 2, (28, 22, 18, 236))
    d.text((W / 2, y0 + bh / 2), t_, font=f, fill=(255, 255, 255), anchor='mm')
    im.save(path)

def png_money(o, path):
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im)
    fl = font(40, MX); a_, b_ = o['left'], o.get('right', '')
    sz = 92
    while True:
        fa = font(sz, BC); fb = fa; fr = font(int(sz * 0.8), ICONF); arrow = '  →  ' if b_ else ''
        tw = d.textlength(a_, font=fa) + d.textlength(arrow, font=fr) + d.textlength(b_, font=fb)
        if tw <= W - 140 or sz <= 50: break
        sz -= 4
    bw = max(tw, d.textlength(o.get('label', ''), font=fl)) + 80; bh = 200 if o.get('label') else 140
    x0, y0 = (W - bw) / 2, o.get('y', 1480)
    rrect(d, (x0, y0, x0 + bw, y0 + bh), 22, (18, 18, 18, 238))
    if o.get('label'): d.text((W / 2, y0 + 22), o['label'], font=fl, fill=(200, 200, 200), anchor='mt')
    x = (W - tw) / 2; y = y0 + (82 if o.get('label') else 22)
    d.text((x, y), a_, font=fa, fill=(255, 255, 255)); x += d.textlength(a_, font=fa)
    if b_:
        d.text((x, y + sz * 0.12), arrow, font=fr, fill=(255, 255, 255)); x += d.textlength(arrow, font=fr)
        d.text((x, y), b_, font=fb, fill=ORANGE)
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
    """Pastilla blanca con circulo rojo, como los avisos de defecto del ganador (Bubbles?, Peeling?)."""
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im); f = font(62, MX)
    t_ = txt
    while d.textlength(t_, font=f) > W - 320 and f.size > 36: f = font(f.size - 3, MX)
    tw = d.textlength(t_, font=f); bh = 108; bw = tw + 150
    x0, y0 = (W - bw) / 2, 1500
    d.rounded_rectangle((x0 + 7, y0 + 9, x0 + bw + 7, y0 + bh + 9), bh / 2, fill=(0, 0, 0, 110))
    rrect(d, (x0, y0, x0 + bw, y0 + bh), bh / 2, (255, 255, 255, 250))
    cx, cy, r = x0 + 56, y0 + bh / 2, 26
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(192, 57, 43, 255))
    d.line((cx - 10, cy - 10, cx + 10, cy + 10), fill=(255, 255, 255), width=7)
    d.line((cx - 10, cy + 10, cx + 10, cy - 10), fill=(255, 255, 255), width=7)
    d.text((x0 + 100, y0 + bh / 2), t_, font=f, fill=(28, 22, 18), anchor='lm')
    im.save(path)


def png_price(o, path):
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im)
    bw, bh = 820, 380; x0, y0 = (W - bw) / 2, 260
    rrect(d, (x0, y0, x0 + bw, y0 + bh), 28, (14, 10, 8, 235), outline=GREEN + (255,), width=5)
    def ctr(t_, f, y, col): d.text(((W - d.textlength(t_, font=f)) / 2, y), t_, font=f, fill=col)
    ctr(o.get('label', ''), font(42), y0 + 34, GOLD)
    ctr(o.get('title', ''), font(58), y0 + 92, (255, 255, 255))
    ctr(o['price'], font(170), y0 + 160, (255, 255, 255))
    if o.get('foot'): ctr(o['foot'], font(34), y0 + bh - 52, (190, 190, 190))
    im.save(path)

def png_plan(o, path):
    """Panel claro con los items que se van sumando: el 'THE SYSTEM' del ganador."""
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im)
    rows = o['rows']; bw = 880; bh = 150 + 86 * len(rows); x0, y0 = (W - bw) / 2, o.get('y', 230)
    d.rounded_rectangle((x0 + 9, y0 + 11, x0 + bw + 9, y0 + bh + 11), 26, fill=(0, 0, 0, 110))
    rrect(d, (x0, y0, x0 + bw, y0 + bh), 24, (250, 246, 238, 250))
    lab = o.get('label', 'EL SISTEMA'); f = font(30, MX)
    d.text((x0 + 44, y0 + 30), lab.upper(), font=f, fill=ORANGE)
    ft = font(50)
    d.text((x0 + 44, y0 + 68), o.get('title', 'Lo que nadie te ensena'), font=ft, fill=(28, 22, 18))
    for i, r in enumerate(rows):
        hecho = r.startswith('*')
        txt = r[1:] if hecho else r
        y = y0 + 142 + i * 86
        cx, cy, rr = x0 + 70, y + 26, 24
        if hecho:
            d.ellipse((cx - rr, cy - rr, cx + rr, cy + rr), fill=(28, 22, 18, 255))
            d.line((cx - 11, cy, cx - 2, cy + 10), fill=(255, 255, 255), width=6)
            d.line((cx - 2, cy + 10, cx + 12, cy - 9), fill=(255, 255, 255), width=6)
        else:
            d.ellipse((cx - rr, cy - rr, cx + rr, cy + rr), fill=ORANGE + (255,))
            d.text((cx, cy), str(i + 1), font=font(30, MX), fill=(255, 255, 255), anchor='mm')
        d.text((x0 + 112, y), txt, font=font(44, MX), fill=(28, 22, 18))
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
    """Placa de cierre: degradado marron -> cobre, titular, el manual en el celular y el boton."""
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im)
    for y in range(H):
        k = y / (H - 1)
        d.line([(0, y), (W, y)], fill=tuple(int(GREEN[i] + (MAG[i] - GREEN[i]) * k) for i in range(3)) + (255,))
    head_ = o.get('head', ['TOCA ABAJO'])
    fs_ = 124
    while fs_ > 60 and max(d.textlength(l, font=font(fs_, MX)) for l in head_) > 940: fs_ -= 4
    ft = font(fs_, MX); y = 150
    for i, l in enumerate(head_):
        d.text((W / 2 + 4, y + i * (fs_ + 24) + 5), l, font=ft, fill=(0, 0, 0, 90), anchor='mt')
        d.text((W / 2, y + i * (fs_ + 24)), l, font=ft, fill=(255, 255, 255), anchor='mt')
    y += len(head_) * (fs_ + 24) + 10
    g = o.get('sub', ''); fsz = 50
    while fsz > 30 and d.textlength(g, font=font(fsz, MX)) > 960: fsz -= 2
    d.text((W / 2, y), g, font=font(fsz, MX), fill=(245, 228, 208), anchor='mt')
    tel = o.get('img')
    if tel and os.path.exists(F(tel)):
        t_ = Image.open(F(tel)).convert('RGBA')
        hh = 940; t_ = t_.resize((int(t_.width * hh / t_.height), hh), Image.LANCZOS)
        sh = Image.new('RGBA', (t_.width + 60, t_.height + 60), (0, 0, 0, 0))
        ImageDraw.Draw(sh).rounded_rectangle((30, 40, t_.width + 30, t_.height + 50), 60, fill=(0, 0, 0, 120))
        sh = sh.filter(ImageFilter.GaussianBlur(18))
        im.alpha_composite(sh, ((W - sh.width) // 2, int(y + 96)))
        im.alpha_composite(t_, ((W - t_.width) // 2, int(y + 110)))
    body, emo = split_emoji(o.get('cta', '')); fc = font(58, MX)
    em = emoji_img(emo, 54) if emo else None
    cw = d.textlength(body, font=fc) + (em.width + 14 if em else 0); bw = cw + 100
    x0, y0 = (W - bw) / 2, 1640
    d.rounded_rectangle((x0 + 7, y0 + 9, x0 + bw + 7, y0 + 111), 54, fill=(0, 0, 0, 90))
    rrect(d, (x0, y0, x0 + bw, y0 + 104), 52, (255, 255, 255, 255))
    d.text((x0 + 50, y0 + 22), body, font=fc, fill=(142, 31, 73))
    if em: im.alpha_composite(em, (int(x0 + 50 + d.textlength(body, font=fc) + 14), int(y0 + 20)))
    s2 = o.get('sub2', ''); f2 = 36
    while f2 > 22 and d.textlength(s2, font=font(f2, MX)) > 980: f2 -= 1
    d.text((W / 2, y0 + 128), s2, font=font(f2, MX), fill=(243, 224, 202), anchor='mt')
    im.save(path)


def png_button(o, path):
    """Boton de CTA al estilo Orzzen: pastilla ambar abajo, sobre el b-roll, sin placa oscura."""
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    body, emo = split_emoji(o.get('text', 'I WANT TO START'))
    fc = font(o.get('size', 64), MX)
    em = emoji_img(emo, 56) if emo else None
    cw = d.textlength(body, font=fc) + (em.width + 14 if em else 0); bw = cw + 110
    x0, y0 = (W - bw) / 2, o.get('y', 1560)
    d.rounded_rectangle((x0 + 8, y0 + 10, x0 + bw + 8, y0 + 112), 54, fill=(0, 0, 0, 120))
    rrect(d, (x0, y0, x0 + bw, y0 + 102), 52, ORANGE + (255,))
    d.text((x0 + 55, y0 + 22), body, font=fc, fill=(255, 255, 255))
    if em: im.alpha_composite(em, (int(x0 + 55 + d.textlength(body, font=fc) + 14), int(y0 + 20)))
    im.save(path)

ovs = []      # (png, t0, t1, anima)
if P.get('hook'):
    png_tag(P['hook'], f'{tmp}/o_hook.png')
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
    elif o['type'] == 'button': png_button(o, pth); hits.append(('ding', t0))
    if o['type'] in ('end', 'button'): t1 = L
    elif o.get('until'):
        u = wt(o['until'], o.get('until_occ', 0)); t1 = u[1] + 0.2 if u else t0 + o.get('dur', 2.2)
    else: t1 = t0 + o.get('dur', 2.2)
    if o['type'] == 'stamp': t1 = min(t1, min([c for c in cuts if c > t0 + 0.1] or [L]) - 0.02)   # el sello no pasa al plano siguiente
    ovs.append((pth, t0, t1, o['type'] not in ('end', 'button')))

# 5) subtítulos (3 palabras, DIN condensada, la que suena en naranja); se ocultan bajo la placa final
def ts(t): t = max(0, t); return f'{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}'
CAPY = P.get('capy', 1380)
HI = P.get('hi', '&H003AE2FF&')         # color del TEXTO de la palabra activa (BGR)
HIBOX = P.get('hibox', '&H00B08BF5&')   # color de la CAJA detras de la palabra activa (BGR)
HIB = P.get('hibord', 20)               # grosor de la caja
end_t = min([t0 for (p, t0, t1, a), o in zip(ovs[len(ovs) - len(P.get('overlays', [])):], P.get('overlays', [])) if o['type'] == 'end'] or [L + 1])
ass = [f'''[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: C,Montserrat ExtraBold,96,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,8,5,5,50,50,0,1

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
        txt = pop + ' '.join((f'{{\\3c{HIBOX}\\bord{HIB}\\shad0\\1c{HI}}}' + clean(x[2]) + '{\\r}') if j == wi else clean(x[2]) for j, x in enumerate(ch))
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
run([FF, '-v', 'error', '-y', '-i', f'{tmp}/cat.mp4', '-i', f'{tmp}/ov.mov', '-filter_complex',
     f"[0:v][1:v]overlay=0:0:format=auto[ov];[ov]ass={tmp}/subs.ass:fontsdir={FD}[s0];"
     + (f"color=c=0x{'%02X%02X%02X' % GREEN}:s={W}x14:r={FPS}[pb];[s0][pb]overlay=x='-W+W*t/{L:.3f}':y=0:shortest=1[v]" if P.get('progress') else "[s0]null[v]"),
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
