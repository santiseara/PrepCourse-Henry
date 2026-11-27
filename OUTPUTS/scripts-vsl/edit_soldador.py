"""Ad de voz en off para el Pack Tesoro del Soldador (LATAM, 2026-11-27): clon exacto del
formato de welders-treasure.online (Daniel Brooks), medido sobre sus 162 creativos de video.

Su edicion, tal cual:
  - 23 a 42 s, 9:16, voz en off de HOMBRE grave (F0 105-136 Hz) y cama musical por debajo.
  - 100 % b-roll del oficio: soldadura, portones, remolques, muebles de hierro, taller.
  - Cortes de 1,3 a 2,2 s.
  - SUBTITULOS abajo (y 0,78 del alto), 2-3 palabras, MAYUSCULA, blancos con borde negro,
    la que suena en AMARILLO #FFE000, SIN caja.
  - FICHAS DE PLANO: grabacion de pantalla del PDF sobre fondo gris oscuro (van al pool como clip).
  - MOCKUP del pack con resplandor, 1 o 2 veces, anclado a donde la voz nombra el producto.
  - Placa de cierre con el CTA.
Lo que cambia contra edit_acm.py: overlay "mockup", capa de avatar en PIP abajo a la derecha
(su formato con cara) y subtitulo amarillo sin caja.
Uso: python3 edit_soldador.py plan.json salida.mp4

--- cabecera original (edit_acm.py) ---
Ad de voz en off para la Guia Puertas de ACM Rentables (LATAM, 2026-11-26): clon del
formato B de orbitadigital2026.com / AcademiaPractica.com, medido sobre sus 20 creativos de
video bajados de la Biblioteca el 26/11 y 5 hojas de contactos.

Su edicion, tal cual:
  - 22 a 39 s, 9:16, voz en off de MUJER (F0 198-219 Hz) y cama musical suave por debajo.
  - 100 % b-roll del oficio: placa de ACM, amoladora cortando, marco, manos armando, la puerta
    instalada. Hay operarios trabajando, pero no hay nadie hablando a camara.
  - SUBTITULOS abajo, 2 palabras, MAYUSCULA, blancos con borde negro, la que suena en CIAN
    #38E8DB (medido sobre sus cuadros). Sin caja.
  - PASTILLA VERDE LIMA #CFF80E con el nombre del producto en negro, al medio del cuadro
    (y 0,47-0,52 del alto, 81 % del ancho), en el tramo donde la voz nombra la guia.
  - Sin titular, sin chips y sin placa de cierre: termina en el b-roll.
La musica NO sale de su audio: sale de las pistas que mando Santiago (regla del 26/11).
Uso: python3 edit_acm.py plan.json salida.mp4

--- cabecera original (edit_laser.py) ---
Ad de voz en off para The Laser Profit Vault (mercado ingles, 2026-11-25): clon del formato B
de Taller Laser Rentable (mikitlaser.auracreativadigital.com), medido sobre 13 videos suyos.

Su edicion, tal cual:
  - 23 a 49 s, 9:16, voz en off de hombre y cama musical por debajo (la cama sale de SU audio).
  - 100 % b-roll del nicho: laser cortando, lamparas encendidas, relojes, manos armando. Cero caras.
  - TITULAR GRANDE arriba los primeros segundos, SIN caja: renglon 1 blanco, renglon 2 AMARILLO.
  - CHIPS NEGROS redondeados ARRIBA con emoji ("Clocks", "7-day plan", "4 bonus collections").
  - SUBTITULOS abajo, mayuscula, blancos con borde negro, la palabra que suena en AMARILLO.
  - PLACA AMARILLA de cierre con el CTA.
Efectos de sonido: salen de ~/SFX/alias (regla del 25/11), nunca sintetizados.
Uso: python3 edit_laser.py plan.json salida.mp4

--- cabecera original ---
Ad de voz en off para Alivio en Cada Plato (LATAM, 2026-11-23): clon de la edicion de
הקלה בכל צלחת (hakala-bechol-tzalachat.impultienda.ar), medida sobre 10 de sus 32 ads activos
y 3 hojas de contactos (bajados el 23/11).

Su edicion, tal cual:
  - 58 a 110 s (la mayoria 70-78), 9:16, voz en off de mujer y cama musical por debajo.
  - 100 % b-roll de comida casera: manos, sarten, bandeja del horno, tortas, tuppers. CERO caras.
  - Cortes de ~2 s, ritmo parejo de punta a punta.
  - CAJA DE HOOK ROJA chica arriba, texto blanco en mayuscula, solo los primeros segundos.
  - SUBTITULOS de 3-5 palabras abajo, mayuscula, blancos con borde negro, con la palabra que
    suena en COLOR (texto de color, sin caja: hibord 0). El color es UNO POR CREATIVO:
    rotan magenta, celeste y verde lima.
  - UN SOLO INSERT del producto (la tapa del libro apoyada en la mesa), anclado a la palabra
    donde la voz lo nombra.
  - CHIP ROJO "50 % DE DESCUENTO - POR TIEMPO LIMITADO" cerca del final.
  - Sin placa de cierre y sin boton: termina en el b-roll.

Lo que cambia contra edit_helados.py: png_hook pasa a caja ROJA con texto blanco y png_chip
pasa de verde hoja a rojo. Las fuentes salen de scripts-vsl/fonts (regla del 22/11).
Uso: python3 edit_alivio.py plan.json salida.mp4
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
ORANGE = (255, 199, 0)         # amarillo #FFC700 (su placa de CTA y su palabra resaltada)
GOLD = (255, 200, 0)           # dorado #FFC800 (la palabra que suena en sus subtitulos)
ROJO = (18, 18, 18)            # negro #121212 (sus chips redondeados de arriba)
GREEN = (122, 158, 118)        # verde salvia #7A9E76 (check de los chips)
FD = os.environ.get('LASER_FONTS', os.path.join(DIR, 'fonts'))
BC = FD + '/BarlowCondensed-ExtraBold.ttf'
MX = FD + '/Montserrat-ExtraBold.ttf'
FONT = '/System/Library/Fonts/Supplemental/DIN Condensed Bold.ttf'
FONT_B = FD + '/Montserrat-ExtraBold.ttf'   # la caja de hook de ellos usa una geométrica bold, no Arial
EMOJI = '/System/Library/Fonts/Apple Color Emoji.ttc'
ICONF = '/System/Library/Fonts/Supplemental/Arial Unicode.ttf'
SOLO_AUDIO = os.environ.get('SOLO_AUDIO') == '1'
def run(c):
    # con SOLO_AUDIO=1 se reusa lo que ya esta en la carpeta _tmp (cortes, cat.mp4, ov.mov,
    # video.mp4) y solo se rehace lo que uno borro a mano: musica, mezcla y el mp4 final.
    # Sirve para cambiarle la cama musical a una tanda sin volver a montar el video.
    if SOLO_AUDIO and c and os.path.exists(c[-1]) and os.path.getsize(c[-1]) > 1000:
        return
    subprocess.run(c, check=True)
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
# familia de cada plano: el autor del clip (clave "fam"), para no poner dos planos seguidos
# del mismo creador. Las claves de este pool son todas c##, por eso no sirve la primera letra.
def fam(k): return (P['clips'].get(k, {}).get('fam') or k) if k else ''
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
        cand = [s for s in P['pool'] if f'{s[0]}@{s[1]}' not in used and fam(s[0]) not in [fam(q) for q in prev[-1:]] and fam(s[0]) != fam(nxt)]
        here = {}
        for p in plan: here[fam(p[0])] = here.get(fam(p[0]), 0) + 1    # misma fuente = mismo autor de TikTok
        def score(s):
            return (usage.get(f'{s[0]}@{s[1]}', 0) * 10 + here.get(fam(s[0]), 0) * 3 + (3 if s[0] in prev else 0)
                    + (6 if s[2] - s[1] < d * 0.75 else 0) + rnd.random())
        seg = min(cand, key=score)
    sid = f'{seg[0]}@{seg[1]}'; used.add(sid)
    plan.append((seg[0], seg[1], seg[2], usage.get(sid, 0) % 2 == 1 and not P['clips'][seg[0]].get('still') and not P['clips'][seg[0]].get('noflip')))   # las fotos nunca se espejan (tienen texto)
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

def png_tag(txt, path, y0=210):
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im); f = font(96, BC)
    words, lines, cur = txt.upper().split(), [], ''
    for w_ in words:
        t_ = (cur + ' ' + w_).strip()
        if d.textlength(t_, font=f) > 880 and cur: lines.append(cur); cur = w_
        else: cur = t_
    lines.append(cur)
    bw = max(d.textlength(l, font=f) for l in lines) + 70; bh = len(lines) * 100 + 40
    x0 = (W - bw) / 2
    d.rectangle((x0 + 8, y0 + 10, x0 + bw + 8, y0 + bh + 10), fill=(0, 0, 0, 110))
    d.rectangle((x0, y0, x0 + bw, y0 + bh), fill=ORANGE + (255,))
    for i, l in enumerate(lines):
        d.text((W / 2, y0 + 22 + i * 100), l, font=f, fill=(18, 14, 8), anchor='mt')
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
        d.text((x, y), b_, font=fb, fill=GREEN)
    im.save(path)

def png_hook(txt, path):
    """Su titular de arranque: SIN caja, mayuscula, renglon 1 blanco y renglon 2 AMARILLO,
    con borde negro grueso para que se lea sobre cualquier b-roll.
    El texto se parte con | ("YOUR LASER SITTING IDLE|EARNS YOU NOTHING")."""
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im)
    lines = [l.strip().upper() for l in txt.split('|') if l.strip()]
    f = font(P.get('hook_size', 96), BC)
    while max(d.textlength(l, font=f) for l in lines) > 960 and f.size > 46:
        f = font(f.size - 3, BC)
    lh = int(f.size * 1.08); y0 = P.get('hook_y', 180)
    for i, l in enumerate(lines):
        col = (255, 255, 255) if i % 2 == 0 else ORANGE
        d.text((W / 2 + 6, y0 + i * lh + 7), l, font=f, fill=(0, 0, 0, 170), anchor='mt')
        d.text((W / 2, y0 + i * lh), l, font=f, fill=col, anchor='mt',
               stroke_width=7, stroke_fill=(0, 0, 0))
    im.save(path)

def png_flecha(o, path):
    """Flecha roja hacia abajo sobre el b-roll, como la que ponen en el CTA."""
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im)
    cx, y = W / 2 + o.get('dx', 0), o.get('y', 1180)
    w, h, th = 56, 130, 34
    R = (214, 26, 48, 255)
    d.rectangle((cx - th / 2, y, cx + th / 2, y + h * 0.58), fill=R)
    d.polygon([(cx - w, y + h * 0.52), (cx + w, y + h * 0.52), (cx, y + h)], fill=R)
    im.save(path)

def png_step(txt, path, y=250, x=None):
    """Ficha de paso azul arriba, como sus "1. PRINT" / "2. CUT & FOLD" / "3. PRAY & GIVE"."""
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im); f = font(58, FONT_B)
    t_ = txt.upper()
    while d.textlength(t_, font=f) > W - 260 and f.size > 34: f = font(f.size - 2, FONT_B)
    bw, bh = d.textlength(t_, font=f) + 70, 92
    x0 = (W - bw) / 2 if x is None else x
    d.rounded_rectangle((x0 + 6, y + 8, x0 + bw + 6, y + bh + 8), 18, fill=(0, 0, 0, 90))
    rrect(d, (x0, y, x0 + bw, y + bh), 18, (30, 58, 110, 240))
    d.text((x0 + 35, y + 16), t_, font=f, fill=(255, 255, 255))
    im.save(path)


def png_box(txt, path, y=250, size=58):
    """La misma cajita blanca del hook, para la placa de cierre (texto azul marino, 1-3 renglones)."""
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im); f = font(size, FONT_B)
    words, lines, cur = txt.upper().split(), [], ''
    for w_ in words:
        t_ = (cur + ' ' + w_).strip()
        if d.textlength(t_, font=f) > 740 and cur: lines.append(cur); cur = w_
        else: cur = t_
    lines.append(cur)
    bw = max(d.textlength(l, font=f) for l in lines) + 80
    bh = len(lines) * (size + 18) + 44
    x0 = (W - bw) / 2
    d.rounded_rectangle((x0 + 7, y + 9, x0 + bw + 7, y + bh + 9), 24, fill=(0, 0, 0, 80))
    rrect(d, (x0, y, x0 + bw, y + bh), 24, (255, 255, 255, 250))
    for i, l in enumerate(lines):
        d.text((W / 2, y + 20 + i * (size + 18)), l, font=f, fill=(30, 58, 110), anchor='mt')
    im.save(path)


def png_chip(txt, icon, path):
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im); f = font(74, BC)
    t_ = txt.upper(); fi = font(52, ICONF)
    emo = emoji_img(icon, 56) if (icon and ord(icon[0]) > 0x2000) else None   # U+2699 (engranaje) cae fuera de 0x1F000 y salia como cuadradito
    iw = (emo.width + 16) if emo else ((d.textlength(icon, font=fi) + 16) if icon else 0)
    while d.textlength(t_, font=f) + iw > W - 150 and f.size > 40: f = font(f.size - 4, BC)
    tw = d.textlength(t_, font=f) + iw; bw, bh = tw + 70, 96
    x0, y0 = (W - bw) / 2, P.get('chip_y', 230)
    d.rounded_rectangle((x0 + 5, y0 + 7, x0 + bw + 5, y0 + bh + 7), 20, fill=(0, 0, 0, 90))
    rrect(d, (x0, y0, x0 + bw, y0 + bh), 20, ROJO + (235,))   # negro #121212, como sus chips de arriba
    if emo: im.alpha_composite(emo, (int(x0 + 35), int(y0 + 20)))
    elif icon: d.text((x0 + 35, y0 + 20), icon, font=fi, fill=ORANGE)
    d.text((x0 + 35 + iw, y0 + 14), t_, font=f, fill=(255, 255, 255))
    im.save(path)

LIMA = (207, 248, 14)          # verde lima #CFF80E: la pastilla del nombre del producto

def png_pastilla(o, path):
    """La pastilla del ganador: 81 % del ancho, 5,3 % del alto, centrada en y 0,497."""
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im)
    bw = int(W * o.get('ancho', 0.81)); bh = int(H * 0.053)
    x0 = (W - bw) / 2; y0 = int(H * o.get('y', 0.47))
    f = font(int(bh * 0.72), MX)
    t_ = o['text']
    while d.textlength(t_, font=f) > bw - 56 and f.size > 24: f = font(f.size - 2, MX)
    d.rounded_rectangle((x0 + 4, y0 + 6, x0 + bw + 4, y0 + bh + 6), bh // 2, fill=(0, 0, 0, 70))
    rrect(d, (x0, y0, x0 + bw, y0 + bh), bh // 2, LIMA + (245,))
    tw = d.textlength(t_, font=f)
    d.text(((W - tw) / 2, y0 + (bh - f.size * 1.22) / 2), t_, font=f, fill=(12, 12, 12))
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

def png_mockup(o, path):
    """El mockup del pack, con resplandor dorado detras, como lo pone el ganador."""
    im = Image.new('RGBA', (W, H))
    mk = Image.open(F(o['src'])).convert('RGBA')
    anc = int(W * o.get('ancho', 0.90))
    mk = mk.resize((anc, int(mk.height * anc / mk.width)), Image.LANCZOS)
    cy = int(H * o.get('y', 0.44))
    gl = Image.new('RGBA', (W, H), (0, 0, 0, 0)); gd = ImageDraw.Draw(gl)
    r = int(anc * 0.62)
    for k in range(26, 0, -1):
        rr = int(r * k / 26)
        gd.ellipse((W / 2 - rr, cy - rr * 0.92, W / 2 + rr, cy + rr * 0.92),
                   fill=(255, 176, 32, int(70 * (1 - k / 26) ** 1.6)))
    gl = gl.filter(ImageFilter.GaussianBlur(26))
    im.alpha_composite(gl)
    sh = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    sh.alpha_composite(mk, ((W - mk.width) // 2 + 8, cy - mk.height // 2 + 14))
    im.alpha_composite(Image.new('RGBA', (W, H), (0, 0, 0, 0)))
    im.alpha_composite(mk, ((W - mk.width) // 2, cy - mk.height // 2))
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
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im)
    g = Image.new('RGBA', (W, H)); gd = ImageDraw.Draw(g)
    for y in range(0, 1100):
        gd.line([(0, y + 300), (W, y + 300)], fill=(0, 0, 0, int(150 * max(0, 1 - abs(y - 420) / 600))))
    im.alpha_composite(g)
    im.alpha_composite(Image.new('RGBA', (W, H), (8, 8, 8, 175)))
    head_ = o.get('head', ['GUÍA DE AUTOCURACIÓN', 'ENERGÉTICA'])
    fs_ = 132
    while fs_ > 60 and max(d.textlength(l, font=font(fs_, BC)) for l in head_) > 980: fs_ -= 4
    ft = font(fs_, BC); y = 400
    for i, l in enumerate(head_):
        d.text((W / 2 + 5, y + i * 150 + 6), l, font=ft, fill=(0, 0, 0, 200), anchor='mt'); d.text((W / 2, y + i * 150), l, font=ft, fill=(255, 255, 255), anchor='mt')
    y += 150 + len(head_) * (fs_ + 18)
    g = o.get('sub', '80 FICHAS · 8 BONOS DE REGALO'); fsz = 70
    while fsz > 38 and d.textlength(g, font=font(fsz, BC)) > 960: fsz -= 2   # la pastilla no se desborda nunca
    fg = font(fsz, BC); gw = d.textlength(g, font=fg) + 70
    rrect(d, ((W - gw) / 2, y, (W + gw) / 2, y + 100), 16, GOLD + (255,)); d.text((W / 2, y + 14), g, font=fg, fill=(20, 20, 10), anchor='mt')
    s2 = o.get('sub2', 'DESCARGA INMEDIATA · GARANTÍA DE 30 DÍAS'); f2 = 40
    while f2 > 24 and d.textlength(s2, font=font(f2, MX)) > 980: f2 -= 1
    fs = font(f2, MX)
    d.text((W / 2, y + 130), s2, font=fs, fill=(230, 230, 230), anchor='mt'); y = y - 20
    body, emo = split_emoji(o.get('cta', 'Toca Más información 👇')); fc = font(66, MX)
    em = emoji_img(emo, 58) if emo else None
    cw = d.textlength(body, font=fc) + (em.width + 14 if em else 0); bw = cw + 90
    x0, y0 = (W - bw) / 2, y + 230
    rrect(d, (x0, y0, x0 + bw, y0 + 104), 52, ORANGE + (255,))
    d.text((x0 + 45, y0 + 24), body, font=fc, fill=(18, 14, 8))
    if em: im.alpha_composite(em, (int(x0 + 45 + d.textlength(body, font=fc) + 14), int(y0 + 22)))
    im.save(path)


def png_cta(o, path):
    """Su placa de cierre: caja AMARILLA redondeada sobre el b-roll (no tapa la pantalla),
    renglon 1 grande en negro y renglon 2 mas chico, con el emoji de la flechita."""
    im = Image.new('RGBA', (W, H)); d = ImageDraw.Draw(im)
    l1 = o.get('l1', 'INSTANT ACCESS').upper()
    l2 = o.get('l2', 'Tap the button')
    f1 = font(o.get('s1', 86), BC)
    while d.textlength(l1, font=f1) > 860 and f1.size > 48: f1 = font(f1.size - 3, BC)
    f2 = font(o.get('s2', 52), MX)
    body, emo = split_emoji(l2)
    em = emoji_img(emo, 48) if emo else None
    w2 = d.textlength(body, font=f2) + (em.width + 12 if em else 0)
    bw = max(d.textlength(l1, font=f1), w2) + 90
    bh = f1.size + f2.size + 70
    x0, y0 = (W - bw) / 2, o.get('y', 1120)
    d.rounded_rectangle((x0 + 9, y0 + 11, x0 + bw + 9, y0 + bh + 11), 26, fill=(0, 0, 0, 110))
    rrect(d, (x0, y0, x0 + bw, y0 + bh), 26, ORANGE + (252,))
    d.text((W / 2, y0 + 16), l1, font=f1, fill=(22, 18, 6), anchor='mt')
    yy = y0 + 16 + f1.size + 12
    d.text(((W - w2) / 2, yy), body, font=f2, fill=(45, 38, 12))
    if em: im.alpha_composite(em, (int((W - w2) / 2 + d.textlength(body, font=f2) + 12), int(yy + 2)))
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
    d.text((x0 + 55, y0 + 22), body, font=fc, fill=(18, 14, 8))
    if em: im.alpha_composite(em, (int(x0 + 55 + d.textlength(body, font=fc) + 14), int(y0 + 20)))
    im.save(path)

ovs = []      # (png, t0, t1, anima)
if P.get('hook'):
    png_hook(P['hook'], f'{tmp}/o_hook.png')
    hu = wt(P['hook_until'], P.get('hook_until_occ', 0)) if P.get('hook_until') else None
    ovs.append((f'{tmp}/o_hook.png', 0, hu[1] + 0.15 if hu else (min(cuts[1] + 0.6, 2.8) if len(cuts) > 2 else 2.6), True))
for k, o in enumerate(P.get('overlays', [])):
    if o.get('from_end') is not None:
        t0 = max(0.0, L - float(o['from_end']))
    else:
        w = wt(o['word'], o.get('occ', 0))
        if not w: continue
        t0 = w[0] - 0.05
    pth = f'{tmp}/o{k}.png'
    if o['type'] == 'step': png_step(o['text'], pth, o.get('y', 250)); hits.append(('pop', t0))
    elif o['type'] == 'box': png_box(o['text'], pth, o.get('y', 250), o.get('size', 58)); hits.append(('pop', t0))
    elif o['type'] == 'chip': png_chip(o['text'], o.get('icon', ''), pth); hits.append(('pop', t0))
    elif o['type'] == 'pastilla': png_pastilla(o, pth); hits.append(('pop', t0))
    elif o['type'] == 'tag': png_tag(o['text'], pth, o.get('y', 210)); hits.append(('pop', t0))
    elif o['type'] == 'money': png_money(o, pth); hits.append(('chaching', t0 + 0.15))
    elif o['type'] == 'price': png_price(o, pth); hits.append(('chaching', t0 + 0.25))
    elif o['type'] == 'plan': png_plan(o, pth); hits.append(('pop', t0))
    elif o['type'] == 'mockup': png_mockup(o, pth); hits.append(('pop', t0))
    elif o['type'] == 'stamp': t0 += o.get('delay', 0.6); png_stamp(o, pth); hits.append(('sello', t0))
    elif o['type'] == 'flecha': png_flecha(o, pth)
    elif o['type'] == 'end': png_end(o, pth); hits.append(('ding', t0))
    elif o['type'] == 'button': png_button(o, pth); hits.append(('ding', t0))
    elif o['type'] == 'cta': png_cta(o, pth); hits.append(('ding', t0))
    if o['type'] in ('end', 'button', 'cta', 'flecha') or (o['type'] == 'box' and o.get('hasta_el_final')): t1 = L
    elif o.get('until'):
        u = wt(o['until'], o.get('until_occ', 0)); t1 = u[1] + 0.2 if u else t0 + o.get('dur', 2.2)
    else: t1 = t0 + o.get('dur', 2.2)
    if o['type'] == 'stamp': t1 = min(t1, min([c for c in cuts if c > t0 + 0.1] or [L]) - 0.02)   # el sello no pasa al plano siguiente
    ovs.append((pth, t0, t1, o['type'] not in ('end', 'button', 'cta')))

for pf in P.get('fixed', []):      # chips de Aula Digital: pegados los L segundos, sin pop
    ovs.append((F(pf), 0.0, L, False))

# 5) subtítulos (3 palabras, DIN condensada, la que suena en naranja); se ocultan bajo la placa final
def ts(t): t = max(0, t); return f'{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}'
CAPY = P.get('capy', 1500)
HI = P.get('hi', '&H0000E0FF&')   # amarillo #FFE000 en BGR         # color del TEXTO de la palabra activa (BGR)
HIBOX = P.get('hibox', '&H00B08BF5&')   # color de la CAJA detras de la palabra activa (BGR)
HIBOX2 = P.get('hibox2')                # Aula Digital alterna DOS colores de caja dentro del mismo ad
HIB = P.get('hibord', 0)               # grosor de la caja (0 = sin caja, solo texto de color)
FNAME = P.get('font', 'Montserrat ExtraBold')
FSZ = P.get('fsize', 66)
ITAL = 1 if P.get('italic', False) else 0
MRG = P.get('margin', 50)
SPC = P.get('spacing', 4)
OUTL = P.get('outline', 6)
SHAD = P.get('shadow', 3)
end_t = min([t0 for (p, t0, t1, a), o in zip(ovs[len(ovs) - len(P.get('overlays', [])):], P.get('overlays', [])) if o['type'] == 'end'] or [L + 1])
ass = [f'''[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: C,{FNAME},{FSZ},&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,{ITAL},0,0,100,100,{SPC},0,1,{OUTL},{SHAD},5,{MRG},{MRG},0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text''']
def clean(w): return w.replace('…', '').strip(' ,;:."“”').upper()
chunks, cur = [], []
for x in vw:
    cur.append(x)
    if len(cur) == P.get('words', 3) or re.search(r'[.?!…]$', x[2]): chunks.append(cur); cur = []
if cur: chunks.append(cur)
for ci, ch in enumerate(chunks):
    if ch[0][0] >= end_t - 0.05: continue
    nxt = chunks[ci + 1][0][0] if ci + 1 < len(chunks) else ch[-1][1] + 0.4
    for wi, (s, e, w) in enumerate(ch):
        e2 = ch[wi + 1][0] if wi + 1 < len(ch) else min(nxt, ch[-1][1] + 0.5)
        e2 = min(e2, end_t)
        pop = '{\\fscx118\\fscy118\\t(0,90,\\fscx100\\fscy100)}' if (wi == 0 and P.get('pop', True)) else ''
        box = (HIBOX2 if (HIBOX2 and ci % 2) else HIBOX)
        marca = (f'{{\\1c{HI}}}' if HIB == 0 else f'{{\\3c{box}\\bord{HIB}\\shad0\\1c{HI}}}')
        txt = pop + ' '.join((marca + clean(x[2]) + '{\\r}') if j == wi else clean(x[2]) for j, x in enumerate(ch))
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
    # DUCKING (25/11): "que se escuche pero que no tape la voz". La cama baja sola mientras
    # hay voz y vuelve al nivel pleno en los huecos, que es donde se tiene que lucir.
    dk = P.get('duck', 0)
    if dk:
        from scipy.ndimage import maximum_filter1d
        vv = v_.mean(1) if v_.ndim > 1 else v_
        e = np.abs(vv)
        w = max(1, int(0.03 * 48000))
        e = np.convolve(e, np.ones(w) / w, 'same')
        idx = np.minimum((np.arange(len(m_)) * (len(e) / max(len(m_), 1))).astype(int), len(e) - 1)
        e = e[idx]
        pos = e[e > 1e-5]
        thr = np.percentile(pos, 55) if len(pos) else 1.0
        hay = np.clip(e / (thr + 1e-9), 0, 1) ** 0.6
        hay = maximum_filter1d(hay, size=max(3, int(0.22 * sr_)))      # cola: no sube entre palabras
        k2 = max(3, int(0.09 * sr_))
        hay = np.convolve(hay, np.ones(k2) / k2, 'same')               # sin escalones
        m_ = m_ * (1.0 - (1.0 - 10 ** (-dk / 20)) * hay)[:, None]
    sf.write(f'{tmp}/music.wav', np.clip(m_, -1, 1), sr_); MVOL = 1.0
else:
    run(['python3', os.path.join(DIR, 'music.py'), f'{L + 1:.2f}', f'{tmp}/music.wav']); MVOL = 0.10
# los efectos salen SIEMPRE de la carpeta de Santiago (regla fija del 25/11), nunca sintetizados
import shutil
ALIAS = os.path.expanduser('~/SFX/alias')
os.makedirs(f'{tmp}/sfx', exist_ok=True)
for _f in os.listdir(ALIAS):
    if _f.endswith('.wav') and not os.path.exists(f'{tmp}/sfx/{_f}'):
        shutil.copy(os.path.join(ALIAS, _f), f'{tmp}/sfx/{_f}')
VOL = {'chaching': 0.30, 'ding': 0.26, 'pop': 0.26, 'whoosh': 0.30, 'sello': 0.40,
       'tick': 0.26, 'swoosh': 0.26, 'texto': 0.30, 'camara': 0.26, 'papel': 0.26,
       'impacto': 0.26, 'sorpresa': 0.26, 'burbuja': 0.22, 'glitch': 0.24, 'flare': 0.26,
       'boom': 0.26, 'subdrop': 0.26, 'scribble': 0.24, 'buzzer': 0.26, 'bwong': 0.26,
       'fuego': 0.26, 'alarma': 0.22, 'llamada': 0.24, 'grillo': 0.20, 'camara_fotos': 0.24}
if isinstance(P.get('whoosh', []), list): hits += [('whoosh', cuts[i] - 0.18) for i in P.get('whoosh', []) if 0 < i < len(cuts) - 1]
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
AV = P.get('avatar')
av_in = ['-i', F(AV['src'])] if AV else []
if AV:
    ax, ay = AV.get('x', 615), AV.get('y', 1230)
    aw, ah = AV.get('w', 465), AV.get('h', 690)
    pre = (f"[2:v]fps={FPS},scale=w='max({aw}/iw,{ah}/ih)*iw':h=-2:eval=init,"
           f"crop={aw}:{ah}:(iw-{aw})*{AV.get('cx',0.5)}:(ih-{ah})*{AV.get('cy',0.18)},setsar=1[av];"
           f"[0:v][1:v]overlay=0:0:format=auto[ovv];[ovv][av]overlay={ax}:{ay}:shortest=0[ov];")
else:
    pre = "[0:v][1:v]overlay=0:0:format=auto[ov];"
run([FF, '-v', 'error', '-y', '-i', f'{tmp}/cat.mp4', '-i', f'{tmp}/ov.mov'] + av_in + ['-filter_complex',
     pre + f"[ov]ass={tmp}/subs.ass:fontsdir={FD}[s0];"
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
