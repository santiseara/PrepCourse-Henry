"""Placas del VSL de Calistenia Rusa (bonos, precio, anclaje, stack, tilde).
Copia las del VSL original de Calistenia Asiática, en la paleta verde de la oferta.
Uso: python3 gfx_calistenia_rusa.py <carpeta_work>
"""
import sys, os
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
WORK = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser('~/Desktop/calistenia-rusa/vsl/work')
F = os.path.join(WORK, 'fonts')
OUT = os.path.join(WORK, 'gfx'); os.makedirs(OUT, exist_ok=True)

VERDE   = (31, 107, 71, 255)      # #1F6B47, el de la marca
VERDE_C = (45, 170, 106, 255)     # verde claro para el precio nuevo
ROJO    = (179, 38, 30, 255)
BLANCO  = (255, 255, 255, 255)
AMARILLO= (250, 204, 21, 255)

def font(name, size):
    return ImageFont.truetype(os.path.join(F, name), size)

def emoji(ch, size):
    try:
        f = ImageFont.truetype('/System/Library/Fonts/Apple Color Emoji.ttc', 160)
        im = Image.new('RGBA', (220, 220), (0, 0, 0, 0))
        ImageDraw.Draw(im).text((10, 10), ch, font=f, embedded_color=True)
        im = im.crop(im.getbbox())
        return im.resize((size, int(im.height * size / im.width)), Image.LANCZOS)
    except Exception as e:
        print('emoji fail:', e); return None

def sombra(d, xy, t, f, fill, anchor='mm', sw=7, align='center', spacing=12):
    if '\n' in t:
        d.multiline_text(xy, t, font=f, fill=fill, anchor=anchor, align=align,
                         spacing=spacing, stroke_width=sw, stroke_fill=(0, 0, 0, 255))
    else:
        d.text(xy, t, font=f, fill=fill, anchor=anchor, stroke_width=sw, stroke_fill=(0, 0, 0, 255))

def lienzo():
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    return im, ImageDraw.Draw(im)

# ---- 1. tilde verde del "¡Mis felicitaciones!" ----
im, d = lienzo()
cx, cy, r = 540, 560, 190
d.ellipse((cx - r, cy - r, cx + r, cy + r), outline=VERDE_C, width=34)
d.line([(cx - 95, cy + 5), (cx - 20, cy + 85), (cx + 120, cy - 90)], fill=VERDE_C, width=44, joint='curve')
im.save(f'{OUT}/check.png')

# ---- 2. los tres bonos ----
g = emoji('🎁', 230)
bonos = [('BONO 1', 'PROTOCOLO\nANTI-CORTISOL\nNOCTURNO'),
         ('BONO 2', 'MENÚ\nANTIINFLAMATORIO\nMASCULINO'),
         ('BONO 3', 'GUÍA DEL\nRENDIMIENTO\nSEXUAL')]
for i, (t1, t2) in enumerate(bonos, 1):
    im, d = lienzo()
    if g: im.alpha_composite(g, (540 - g.width // 2, 470))
    sombra(d, (540, 810), t1, font('Montserrat-Black.ttf', 112), AMARILLO)
    sombra(d, (540, 1060), t2, font('BarlowCondensed-ExtraBold.ttf', 130), BLANCO, spacing=10)
    im.save(f'{OUT}/bono{i}.png')

# ---- 3. precio: tachado + nuevo + flecha ----
im, d = lienzo()
fo = font('Montserrat-Black.ttf', 110)
sombra(d, (540, 560), '$47.990', fo, BLANCO)
bb = d.textbbox((540, 560), '$47.990', font=fo, anchor='mm')
d.line([(bb[0] - 12, 560), (bb[2] + 12, 560)], fill=ROJO, width=14)
sombra(d, (540, 790), '$17.990', font('Montserrat-Black.ttf', 215), VERDE_C, sw=9)
ax = 540
d.rectangle((ax - 28, 950, ax + 28, 1100), fill=ROJO)
d.polygon([(ax - 90, 1090), (ax + 90, 1090), (ax, 1210)], fill=ROJO)
im.save(f'{OUT}/precio.png')

# ---- 4. anclaje: lo que costaría por fuera ----
im, d = lienzo()
sombra(d, (540, 620), '+$50.000', font('Montserrat-Black.ttf', 190), ROJO, sw=8)
sombra(d, (540, 800), 'POR MES', font('Montserrat-Black.ttf', 105), BLANCO)
im.save(f'{OUT}/anclaje.png')

# ---- 5. stack: todo lo que se lleva ----
im, d = lienzo()
sombra(d, (540, 620),
       'MÉTODO\n+ PLAN ALIMENTARIO\n+ ACOMPAÑAMIENTO\n+ 3 BONOS',
       font('BarlowCondensed-ExtraBold.ttf', 140), VERDE_C, sw=9, spacing=18)
im.save(f'{OUT}/stack.png')

# ---- 6. siete minutos por día ----
im, d = lienzo()
sombra(d, (540, 620), '7 MINUTOS', font('Montserrat-Black.ttf', 160), BLANCO, sw=9)
sombra(d, (540, 790), 'POR DÍA', font('Montserrat-Black.ttf', 130), VERDE_C, sw=8)
im.save(f'{OUT}/siete.png')

# ---- 7. garantía ----
im, d = lienzo()
cx, cy, r = 540, 700, 250
d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(16, 20, 24, 240), outline=VERDE_C, width=12)
sombra(d, (cx, cy - 50), '30', font('Montserrat-Black.ttf', 190), BLANCO, sw=0)
sombra(d, (cx, cy + 90), 'DÍAS', font('Montserrat-Black.ttf', 90), VERDE_C, sw=0)
sombra(d, (540, 1060), 'O TE FUNCIONA\nO TE SALE GRATIS',
       font('BarlowCondensed-ExtraBold.ttf', 120), BLANCO, sw=8, spacing=14)
im.save(f'{OUT}/garantia.png')

print('placas:', sorted(os.listdir(OUT)))
