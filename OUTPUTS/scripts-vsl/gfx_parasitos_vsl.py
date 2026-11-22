"""Placas del VSL de Desparasitacion Articular (AR, 2026-11-22).

Paleta tomada del quiz que esta en vivo (verde #16a34a, rojo #dc2626) para que el VSL
y la landing a la que lleva sean la misma marca. Tipografia: Rubik, la misma de los
subtitulos de los ads de la oferta.

Uso: python3 gfx_parasitos_vsl.py <dir_fuentes> <dir_salida>
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONTS, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
W, H = 1080, 1920

VERDE   = (22, 163, 74, 255)
VERDE_O = (13, 110, 50, 255)
ROJO    = (220, 38, 38, 255)
BLANCO  = (255, 255, 255, 255)
TINTA   = (3, 7, 18, 255)
GRIS    = (107, 114, 128, 255)
AMAR    = (250, 204, 21, 255)

def f(size):
    return ImageFont.truetype(os.path.join(FONTS, 'Rubik.ttf'), size)

def sombra(d, xy, t, fn, fill, anchor='mm', sw=8):
    d.text(xy, t, font=fn, fill=fill, anchor=anchor, stroke_width=sw, stroke_fill=(0, 0, 0, 255))

def lienzo():
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    return im, ImageDraw.Draw(im)

def tarjeta(d, box, r=40, fill=(255, 255, 255, 248), im=None):
    if im is not None:
        sh = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(sh).rounded_rectangle((box[0], box[1] + 18, box[2], box[3] + 18), r, fill=(0, 0, 0, 150))
        im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(22)))
    d.rounded_rectangle(box, r, fill=fill)

def estrella(d, cx, cy, r, fill=(245, 179, 1, 255)):
    import math
    pts = []
    for k in range(10):
        ang = -math.pi / 2 + k * math.pi / 5
        rr = r if k % 2 == 0 else r * 0.42
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    d.polygon(pts, fill=fill)

def estrellas(d, x, y, n=5, r=22, sep=54):
    for k in range(n):
        estrella(d, x + r + k * sep, y, r)

def tilde(d, x, y, s=1.0, fill=None, w=6):
    fill = fill or VERDE
    d.line([(x, y + 4 * s), (x + 7 * s, y + 12 * s), (x + 20 * s, y - 6 * s)],
           fill=fill, width=int(w * s), joint='curve')

def check_circulo(d, cx, cy, r=17):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=VERDE)
    tilde(d, cx - 9, cy - 1, s=0.85, fill=BLANCO, w=6)

def envolver(d, txt, fn, ancho):
    out, cur = [], ''
    for w in txt.split():
        p = (cur + ' ' + w).strip()
        if d.textlength(p, font=fn) <= ancho:
            cur = p
        else:
            out.append(cur); cur = w
    if cur: out.append(cur)
    return out

# ---------------------------------------------------------------- 1 · titulo
im, d = lienzo()
sombra(d, (540, 300), 'PROTOCOLO', f(96), BLANCO, sw=9)
sombra(d, (540, 410), 'DESPARASITACIÓN', f(88), BLANCO, sw=9)
sombra(d, (540, 510), 'ARTICULAR', f(88), BLANCO, sw=9)
d.rounded_rectangle((330, 580, 750, 710), 28, fill=VERDE)
d.text((540, 645), '9 DÍAS', font=f(86), fill=BLANCO, anchor='mm')
im.save(os.path.join(OUT, 'titulo.png'))

# ---------------------------------------------------------------- 2 · etapas
etapas = [
    ('DÍAS 1 · 2 · 3', 'SOLTAR',      'el parásito se despega'),
    ('DÍAS 4 · 5 · 6', 'LIMPIAR',     'el cuerpo lo elimina'),
    ('DÍAS 7 · 8 · 9', 'RECONSTRUIR', 'vuelve el colágeno'),
]
for i, (dias, nom, baja) in enumerate(etapas, 1):
    im, d = lienzo()
    tarjeta(d, (90, 620, 990, 1070), 44, (255, 255, 255, 250), im)
    d.rounded_rectangle((90, 620, 990, 740), 44, fill=VERDE)
    d.rectangle((90, 700, 990, 740), fill=VERDE)
    d.text((540, 680), dias, font=f(60), fill=BLANCO, anchor='mm')
    d.text((540, 850), nom, font=f(110), fill=VERDE_O, anchor='mm')
    d.text((540, 975), baja, font=f(46), fill=GRIS, anchor='mm')
    im.save(os.path.join(OUT, f'etapa{i}.png'))

# ---------------------------------------------------------------- 3 · resenas
resenas = [
    ('Hugo Benítez', 'Córdoba',
     'Tenía artrosis en la rodilla y me había roto el ligamento. Nunca pensé que una simple '
     'desparasitación me podía ayudar, después de haber gastado una fortuna en suplementos y pomadas.'),
    ('Teresa Ferreyra', 'Mendoza',
     'Me decían Teresa la Dolorida, porque tenía fibromialgia, pico de loro y unos dolores terribles '
     'en los hombros, las manos y las piernas. Después de completar el Protocolo quedé totalmente libre.'),
    ('Antonio Rivas', 'San Miguel de Tucumán',
     'Ya me habían puesto infiltraciones y tenía fecha de cirugía para la espalda. Los dolores '
     'simplemente se me fueron de una semana para la otra.'),
]
for i, (nom, ciu, txt) in enumerate(resenas, 1):
    im, d = lienzo()
    fn_t = f(40)
    lineas = envolver(d, txt, fn_t, 740)
    alto = 300 + len(lineas) * 56
    y0 = 1500 - alto
    tarjeta(d, (80, y0, 1000, y0 + alto), 44, (255, 255, 255, 250), im)
    ini = ''.join(p[0] for p in nom.split()[:2])
    d.ellipse((130, y0 + 50, 250, y0 + 170), fill=(220, 237, 226, 255))
    d.text((190, y0 + 110), ini, font=f(50), fill=VERDE_O, anchor='mm')
    d.text((285, y0 + 68), nom, font=f(50), fill=TINTA)
    tilde(d, 287, y0 + 146, s=1.0)
    d.text((320, y0 + 128), ciu, font=f(36), fill=VERDE)
    estrellas(d, 130, y0 + 205)
    for k, ln in enumerate(lineas):
        d.text((130, y0 + 265 + k * 56), ln, font=fn_t, fill=(40, 48, 62, 255))
    im.save(os.path.join(OUT, f'resena{i}.png'))

# ---------------------------------------------------------------- 4 · value stack
items = [
    ('Preparación para la desparasitación', '$17.990'),
    ('Desparasitación completa',            '$26.990'),
    ('Acompañamiento individual',           '$45.990'),
    ('Guía alimentaria contra los parásitos', '$12.990'),
    ('Consultas con el equipo',             '$13.990'),
    ('Mantenimiento anual del protocolo',   '$22.990'),
    ('Receta de la desparasitación en 9 días', '$45.990'),
]
im, d = lienzo()
tarjeta(d, (60, 380, 1020, 1540), 44, (255, 255, 255, 250), im)
d.rounded_rectangle((60, 380, 1020, 500), 44, fill=VERDE)
d.rectangle((60, 460, 1020, 500), fill=VERDE)
d.text((540, 442), 'TODO LO QUE RECIBÍS', font=f(52), fill=BLANCO, anchor='mm')
y = 550
fn_i, fn_p = f(34), f(38)
for nom, pre in items:
    lns = envolver(d, nom, fn_i, 560)
    for j, ln in enumerate(lns):
        if j == 0:
            check_circulo(d, 137, y + 17)
        d.text((172, y), ln, font=fn_i, fill=(40, 48, 62, 255))
        y += 44
    d.text((985, y - 44), pre, font=fn_p, fill=GRIS, anchor='rm')
    y += 48
d.line([(120, y + 10), (960, y + 10)], fill=(220, 224, 230, 255), width=4)
d.text((120, y + 55), 'VALOR TOTAL', font=f(44), fill=TINTA)
tot = '$186.930'
d.text((960, y + 55), tot, font=f(56), fill=ROJO, anchor='rt')
bb = d.textbbox((960, y + 55), tot, font=f(56), anchor='rt')
d.line([(bb[0] - 8, (bb[1] + bb[3]) / 2), (bb[2] + 8, (bb[1] + bb[3]) / 2)], fill=ROJO, width=8)
im.save(os.path.join(OUT, 'stack.png'))

# ---------------------------------------------------------------- 5 · precio
im, d = lienzo()
tach = '$186.930'
fn = f(90)
sombra(d, (540, 560), tach, fn, BLANCO, sw=9)
bb = d.textbbox((540, 560), tach, font=fn, anchor='mm')
d.line([(bb[0] - 14, 560), (bb[2] + 14, 560)], fill=ROJO, width=14)
sombra(d, (540, 780), '$17.990', f(220), VERDE, sw=11)
d.rounded_rectangle((250, 930, 830, 1040), 26, fill=(255, 255, 255, 240))
d.text((540, 985), 'o 3 cuotas de $5.997', font=f(48), fill=TINTA, anchor='mm')
im.save(os.path.join(OUT, 'precio.png'))

# ---------------------------------------------------------------- 6 · boton + garantia
im, d = lienzo()
sh = Image.new('RGBA', (W, H), (0, 0, 0, 0))
ImageDraw.Draw(sh).rounded_rectangle((110, 1210, 970, 1375), 36, fill=(0, 0, 0, 170))
im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(20)))
d.rounded_rectangle((110, 1190, 970, 1355), 36, fill=VERDE)
d.text((540, 1272), 'QUIERO MI PROTOCOLO', font=f(58), fill=BLANCO, anchor='mm')
d.rounded_rectangle((250, 1395, 830, 1490), 24, fill=(255, 255, 255, 240))
tilde(d, 300, 1444, s=1.1)
d.text((345, 1442), '180 DÍAS DE GARANTÍA', font=f(42), fill=VERDE_O, anchor='lm')
im.save(os.path.join(OUT, 'boton.png'))

# ---------------------------------------------------------------- 7 · cierre
im = Image.new('RGBA', (W, H), (8, 10, 14, 255))
d = ImageDraw.Draw(im)
d.rounded_rectangle((70, 430, 1010, 620), 30, fill=VERDE)
d.text((540, 492), 'ESTA ES TU', font=f(66), fill=BLANCO, anchor='mm')
d.text((540, 566), 'ÚLTIMA OPORTUNIDAD', font=f(66), fill=BLANCO, anchor='mm')
d.text((540, 730), 'Tenés 180 días de garantía', font=f(48), fill=(214, 219, 227, 255), anchor='mm')
d.text((540, 800), 'Estás a un clic de dejar de sufrir', font=f(48), fill=(214, 219, 227, 255), anchor='mm')
d.rounded_rectangle((110, 940, 970, 1105), 36, fill=VERDE)
d.text((540, 1022), 'QUIERO MI PROTOCOLO', font=f(58), fill=BLANCO, anchor='mm')
d.text((540, 1185), 'Tocá el botón de abajo', font=f(44), fill=AMAR, anchor='mm')
ax = 540
d.rectangle((ax - 20, 1260, ax + 20, 1370), fill=AMAR)
d.polygon([(ax - 70, 1360), (ax + 70, 1360), (ax, 1455)], fill=AMAR)
im.convert('RGB').save(os.path.join(OUT, 'cierre.png'))

print('placas:', sorted(os.listdir(OUT)))
