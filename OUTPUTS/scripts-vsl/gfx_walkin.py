# -*- coding: utf-8 -*-
"""Inserts de producto del Visual Handbook of Walk-In Coolers & Freezers (2026-11-06).

Carlos Medina (el ganador en español) mete el producto en pantalla en varios de sus ads: la tapa
del manual y una lámina interior. Acá se dibujan por código, con la landing real en la mano
(visual-handbook-of-walk-in-coolers-freezers.impultienda.ar), copiando su jerarquía y su
vocabulario exacto. Lo único que NO se copia es el precio: no va en el ad (regla fija).

Salida (lienzo 1.20x con el sobrante desenfocado, porque el editor zoomea de 1.0 a 1.14 + 1.16):
  cover.png  - la tapa del manual: 8 MODULES · 46 TOPICS · 60 PAGES
  plate.png  - una lámina interior tipo manual: el ciclo de refrigeración con sus 4 etapas
  offer.png  - la tarjeta de oferta del cierre: bullets de la landing + botón, sin precio

Uso: python3 gfx_walkin.py
"""
import os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUT = os.path.expanduser('~/Desktop/walk-in-coolers-freezers/anuncios/work/gfx')
FD = os.path.expanduser('~/Desktop/walk-in-coolers-freezers/anuncios/work/fonts')
os.makedirs(OUT, exist_ok=True)
W, H = 1080, 1920
MW, MH = 1296, 2304

BC = FD + '/BarlowCondensed-ExtraBold.ttf'
BCB = FD + '/BarlowCondensed-Bold.ttf'
BCS = FD + '/BarlowCondensed-SemiBold.ttf'
MX = FD + '/Montserrat-ExtraBold.ttf'

# paleta de la landing: azul frío industrial, hielo, naranja de alerta
NAVY = (14, 32, 56)
BLUE = (28, 92, 168)
ICE = (226, 238, 248)
WHITE = (255, 255, 255)
INK = (22, 26, 32)
GREY = (120, 132, 148)
ORANGE = (240, 122, 30)
GREEN = (36, 160, 96)

f = lambda p, s: ImageFont.truetype(p, s)


def marco(im, path):
    bg = im.resize((MW, MH), Image.LANCZOS).filter(ImageFilter.GaussianBlur(26))
    bg = Image.blend(bg, Image.new('RGB', (MW, MH), (10, 16, 26)), 0.35)
    bg.paste(im, ((MW - W) // 2, (MH - H) // 2))
    bg.save(path)


def rr(d, box, r, fill, outline=None, width=3):
    d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)


def center(d, y, txt, font, fill, w=W):
    tw = d.textbbox((0, 0), txt, font=font)[2]
    d.text(((w - tw) // 2, y), txt, font=font, fill=fill)
    return tw


# ---------------------------------------------------------------- tapa del manual
def cover():
    im = Image.new('RGB', (W, H), ICE)
    d = ImageDraw.Draw(im)
    # fondo: sutil rejilla de plano tecnico
    for x in range(0, W, 54):
        d.line([(x, 0), (x, H)], fill=(212, 226, 240), width=2)
    for y in range(0, H, 54):
        d.line([(0, y), (W, y)], fill=(212, 226, 240), width=2)

    bw, bh = 760, 1040
    bx, by = (W - bw) // 2, 330
    d.rounded_rectangle([bx + 16, by + 20, bx + bw + 18, by + bh + 22], radius=18, fill=(186, 203, 220))
    rr(d, [bx, by, bx + bw, by + bh], 18, NAVY)
    d.rectangle([bx, by, bx + 26, by + bh], fill=(8, 20, 38))   # lomo

    d.rectangle([bx + 70, by + 86, bx + 70 + 150, by + 86 + 8], fill=ORANGE)
    d.text((bx + 70, by + 118), 'VISUAL', font=f(BC, 86), fill=WHITE)
    d.text((bx + 70, by + 200), 'HANDBOOK', font=f(BC, 86), fill=WHITE)
    d.text((bx + 70, by + 300), 'OF WALK-IN COOLERS', font=f(BCB, 52), fill=(150, 196, 240))
    d.text((bx + 70, by + 356), '& FREEZERS', font=f(BCB, 52), fill=(150, 196, 240))

    # dibujito de la camara: puerta + evaporador
    cx, cy, cw, ch = bx + 150, by + 470, 460, 330
    rr(d, [cx, cy, cx + cw, cy + ch], 10, (236, 243, 250), outline=(120, 150, 185), width=4)
    rr(d, [cx + 30, cy + 46, cx + 220, cy + ch - 26], 8, (212, 226, 240), outline=(120, 150, 185), width=4)
    d.rectangle([cx + 196, cy + 150, cx + 212, cy + 196], fill=(90, 110, 135))  # manija
    rr(d, [cx + 270, cy + 40, cx + cw - 30, cy + 130], 8, (198, 214, 232), outline=(120, 150, 185), width=4)
    for i in range(3):
        c0 = cx + 300 + i * 56
        d.ellipse([c0, cy + 58, c0 + 48, cy + 106], outline=(96, 122, 152), width=5)
        d.line([(c0 + 24, cy + 58), (c0 + 24, cy + 106)], fill=(96, 122, 152), width=4)
    d.line([(cx + 290, cy + 150), (cx + 290, cy + ch - 20)], fill=(28, 92, 168), width=7)
    d.line([(cx + 350, cy + 150), (cx + 350, cy + ch - 20)], fill=(196, 60, 50), width=7)

    for i, t in enumerate(['8 MODULES', '46 TOPICS', '60 PAGES']):
        y0 = by + 850 + 0
        x0 = bx + 70 + i * 215
        rr(d, [x0, y0, x0 + 190, y0 + 66], 10, (26, 54, 92), outline=(70, 118, 176), width=3)
        tw = d.textbbox((0, 0), t, font=f(BCB, 40))[2]
        d.text((x0 + (190 - tw) // 2, y0 + 12), t, font=f(BCB, 40), fill=(170, 210, 246))

    center(d, 1470, 'DESIGN  ·  INSTALLATION  ·  DIAGNOSTICS', f(BCB, 46), (70, 92, 120))
    marco(im, OUT + '/cover.png')


# ---------------------------------------------------------------- lamina interior
def plate():
    im = Image.new('RGB', (W, H), (248, 250, 252))
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 150], fill=NAVY)
    d.text((60, 36), 'MODULE 2', font=f(BC, 48), fill=(130, 180, 230))
    d.text((60, 86), 'THE REFRIGERATION CYCLE', font=f(BC, 56), fill=WHITE)
    rr(d, [W - 230, 44, W - 60, 110], 10, ORANGE)
    d.text((W - 208, 56), 'PLATE 07', font=f(BCB, 40), fill=(28, 18, 6))

    # diagrama: 4 etapas en rectangulo
    L, R, T, B = 150, 930, 420, 1180
    comp = [(L, B - 110), (L + 190, B)]
    cond = [(L, T), (L + 190, T + 110)]
    txv = [(R - 190, T), (R, T + 110)]
    evap = [(R - 190, B - 110), (R, B)]
    for box, name, col in [(cond, 'CONDENSER', (196, 60, 50)), (txv, 'METERING\nDEVICE', (70, 100, 140)),
                           (evap, 'EVAPORATOR', (28, 92, 168)), (comp, 'COMPRESSOR', (40, 48, 60))]:
        rr(d, [box[0][0], box[0][1], box[1][0], box[1][1]], 10, WHITE, outline=col, width=6)
        lines = name.split('\n')
        for j, ln in enumerate(lines):
            tw = d.textbbox((0, 0), ln, font=f(BCB, 36))[2]
            d.text((box[0][0] + (190 - tw) // 2, box[0][1] + (110 - len(lines) * 40) // 2 + j * 38),
                   ln, font=f(BCB, 36), fill=col)
    d.line([(L + 190, T + 55), (R - 190, T + 55)], fill=(196, 60, 50), width=8)
    d.line([(R - 95, T + 110), (R - 95, B - 110)], fill=(70, 100, 140), width=8)
    d.line([(R - 190, B - 55), (L + 190, B - 55)], fill=(28, 92, 168), width=8)
    d.line([(L + 95, B - 110), (L + 95, T + 110)], fill=(40, 48, 60), width=8)
    for (x, y, a) in [(530, T + 55, 0), (R - 95, 800, 90), (530, B - 55, 180), (L + 95, 800, 270)]:
        r = 18
        ang = math.radians(a)
        pts = [(x + r * math.cos(ang), y + r * math.sin(ang)),
               (x + r * math.cos(ang + 2.4), y + r * math.sin(ang + 2.4)),
               (x + r * math.cos(ang - 2.4), y + r * math.sin(ang - 2.4))]
        d.polygon(pts, fill=(40, 48, 60))
    center(d, T + 136, 'HIGH PRESSURE VAPOR', f(BCS, 32), (150, 60, 55))
    center(d, B - 160, 'LOW PRESSURE VAPOR', f(BCS, 32), (40, 90, 150))

    y = 1270
    for t in ['Sensible heat and latent heat, with worked examples',
              'Pressure, temperature and refrigerant phase change',
              'Superheat and subcooling: what each reading tells you']:
        d.ellipse([70, y + 10, 94, y + 34], fill=GREEN)
        d.line([(76, y + 22), (82, y + 29), (89, y + 15)], fill=WHITE, width=4)
        d.text((118, y), t, font=f(BCB, 44), fill=INK)
        y += 76
    d.rectangle([0, H - 110, W, H], fill=(236, 241, 247))
    d.text((60, H - 86), 'VISUAL HANDBOOK OF WALK-IN COOLERS & FREEZERS', font=f(BCB, 38), fill=GREY)
    marco(im, OUT + '/plate.png')


# ---------------------------------------------------------------- tarjeta de oferta
def offer():
    im = Image.new('RGB', (W, H), (10, 18, 32))
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 104], fill=ORANGE)
    center(d, 26, 'INSTANT DIGITAL ACCESS', f(BC, 56), (26, 16, 4))

    cw, ch = 940, 1500
    cx, cy = (W - cw) // 2, 190
    rr(d, [cx, cy, cx + cw, cy + ch], 24, (248, 250, 252))

    # mini tapa
    bw, bh = 300, 410
    bx, by = cx + 60, cy + 60
    rr(d, [bx, by, bx + bw, by + bh], 10, NAVY)
    d.rectangle([bx, by, bx + 12, by + bh], fill=(8, 20, 38))
    d.rectangle([bx + 34, by + 46, bx + 34 + 70, by + 50], fill=ORANGE)
    d.text((bx + 34, by + 62), 'VISUAL', font=f(BC, 44), fill=WHITE)
    d.text((bx + 34, by + 104), 'HANDBOOK', font=f(BC, 44), fill=WHITE)
    d.text((bx + 34, by + 152), 'WALK-IN COOLERS', font=f(BCB, 26), fill=(150, 196, 240))
    rr(d, [bx + 34, by + 208, bx + bw - 34, by + bh - 40], 8, (236, 243, 250))
    for i in range(3):
        c0 = bx + 60 + i * 64
        d.ellipse([c0, by + 250, c0 + 52, by + 302], outline=(96, 122, 152), width=5)

    tx = bx + bw + 46
    d.text((tx, by + 40), 'VISUAL HANDBOOK', font=f(BC, 58), fill=INK)
    d.text((tx, by + 100), 'OF WALK-IN COOLERS', font=f(BC, 58), fill=INK)
    d.text((tx, by + 160), '& FREEZERS', font=f(BC, 58), fill=INK)
    d.text((tx, by + 236), '8 MODULES  ·  46 TOPICS', font=f(BCB, 38), fill=BLUE)
    d.text((tx, by + 284), '3 BONUSES  ·  60 PAGES', font=f(BCB, 38), fill=BLUE)
    rr(d, [tx, by + 346, tx + 330, by + 410], 10, (226, 240, 232), outline=GREEN, width=3)
    d.text((tx + 22, by + 360), 'LIFETIME ACCESS', font=f(BCB, 38), fill=(24, 110, 66))

    y = cy + 540
    for t in ['Heat load formulas with worked examples',
              'Panel assembly, vacuum and charging',
              'Diagnosis by pressure and temperature',
              'Commissioning checklist',
              'Preventive maintenance plan',
              'Quick guide to common faults']:
        d.ellipse([cx + 62, y + 8, cx + 90, y + 36], fill=GREEN)
        d.line([(cx + 69, y + 22), (cx + 76, y + 30), (cx + 84, y + 14)], fill=WHITE, width=5)
        d.text((cx + 116, y - 2), t, font=f(BCB, 46), fill=INK)
        y += 86

    by2 = cy + ch - 290
    rr(d, [cx + 60, by2, cx + cw - 60, by2 + 128], 16, ORANGE)
    center(d, by2 + 32, 'I WANT THE HANDBOOK', f(MX, 54), (26, 16, 4))
    center(d, by2 + 170, '30-DAY GUARANTEE  ·  INSTANT ACCESS', f(BCB, 42), GREY)
    marco(im, OUT + '/offer.png')


cover(); plate(); offer()
print('listo:', ', '.join(sorted(os.listdir(OUT))))
