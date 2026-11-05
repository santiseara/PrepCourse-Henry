# -*- coding: utf-8 -*-
"""Inserts de producto de A Tu Medida / Arreglala Vos Misma (clon de Stitched Fits, 2026-11-05).

Replica lo que mete Stitched Fits en sus ads: no un mockup, sino una GRABACIÓN DE PANTALLA
de su propia página de ventas en una laptop, y en el ad de bizop la pantalla del curso con
los títulos de las clases. Se dibuja por código, así que no hace falta que la landing exista.

Diferencia contra el original: ellos muestran £99 → £59. Acá NO va precio en el ad
(regla fija de Santiago), va la pastilla de AHORRÁS 40% y "pago único · acceso de por vida".
Contenido copiado de la landing real que pasó Santiago el 5/11.

Uso: python3 gfx_arreglos.py
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUT = os.path.expanduser('~/Desktop/arreglos-de-ropa/anuncios/work/gfx')
FD = os.path.expanduser('~/Desktop/arreglos-de-ropa/anuncios/work/fonts')
os.makedirs(OUT, exist_ok=True)
W, H = 1080, 1920
MW, MH = 1296, 2304            # lienzo 1.20x: el editor zoomea de 1.0 a 1.14 + golpe de 1.16
BC = FD + '/BarlowCondensed-ExtraBold.ttf'
BCS = FD + '/BarlowCondensed-SemiBold.ttf'
MX = FD + '/Montserrat-ExtraBold.ttf'
SERIF = '/System/Library/Fonts/Supplemental/Didot.ttc'
SERIF_I = '/System/Library/Fonts/Supplemental/Times New Roman.ttf'

# paleta de la página (la de ellos: crema, tinta, borgoña)
CREAM, INK, WINE, GREY = (246, 243, 238), (26, 24, 22), (155, 28, 48), (122, 116, 110)
f = lambda p, s: ImageFont.truetype(p, s)


def marco(im, path):
    bg = im.resize((MW, MH), Image.LANCZOS).filter(ImageFilter.GaussianBlur(26))
    bg = Image.blend(bg, Image.new('RGB', (MW, MH), (16, 15, 14)), 0.35)
    bg.paste(im, ((MW - W) // 2, (MH - H) // 2))
    bg.save(path)


def rr(d, box, r, fill, outline=None, width=2):
    d.rounded_rectangle(box, r, fill=fill, outline=outline, width=width)


def laptop(dibujar_pagina):
    """Lienzo con una laptop en perspectiva leve; `dibujar_pagina(d, x0, y0, w, h)` pinta la pantalla."""
    im = Image.new('RGB', (W, H), (36, 33, 31))
    d = ImageDraw.Draw(im)
    # escritorio de madera oscura con veta
    for y in range(0, H, 6):
        c = 8 + (5 if (y // 6) % 4 == 0 else 0)
        d.line([(0, y), (W, y + 10)], fill=(58 + c, 44 + c, 36 + c), width=5)
    im = im.filter(ImageFilter.GaussianBlur(4))
    d = ImageDraw.Draw(im)
    # cuerpo de la laptop
    bx0, by0, bx1, by1 = 40, 240, W - 40, 1560
    d.rounded_rectangle((bx0 - 10, by0 - 10, bx1 + 10, by1 + 10), 26, fill=(22, 21, 20))
    sx0, sy0, sx1, sy1 = bx0 + 26, by0 + 26, bx1 - 26, by1 - 26
    d.rectangle((sx0, sy0, sx1, sy1), fill=CREAM)
    sub = Image.new('RGB', (sx1 - sx0, sy1 - sy0), CREAM)
    dibujar_pagina(ImageDraw.Draw(sub), sub.width, sub.height)
    im.paste(sub, (sx0, sy0))
    d = ImageDraw.Draw(im)
    # brillo diagonal del vidrio
    gl = Image.new('RGBA', (W, H), (0, 0, 0, 0)); gd = ImageDraw.Draw(gl)
    gd.polygon([(sx0, sy1), (sx0 + 420, sy0), (sx0 + 640, sy0), (sx0 + 170, sy1)], fill=(255, 255, 255, 8))
    im = Image.alpha_composite(im.convert('RGBA'), gl).convert('RGB')
    d = ImageDraw.Draw(im)
    # base y teclado
    d.rounded_rectangle((bx0 - 70, by1 + 10, bx1 + 70, by1 + 70), 16, fill=(30, 28, 27))
    d.rounded_rectangle((bx0 + 40, by1 + 86, bx1 - 40, by1 + 300), 10, fill=(26, 24, 23))
    for r_ in range(4):
        for c_ in range(13):
            x = bx0 + 70 + c_ * 68; y = by1 + 108 + r_ * 48
            d.rounded_rectangle((x, y, x + 52, y + 34), 6, fill=(48, 45, 43))
    return im


def pagina_venta(d, w, h):
    # barra de oferta (como la landing)
    d.rectangle((0, 0, w, 56), fill=WINE)
    d.text((w / 2, 12), 'OFERTA POR TIEMPO LIMITADO', font=f(BCS, 32), fill=(255, 240, 240), anchor='mt')
    # marca
    d.text((w / 2, 84), 'A Tu Medida', font=f(SERIF, 58), fill=INK, anchor='mt')
    d.line([(40, 168), (w - 40, 168)], fill=(216, 210, 200), width=2)
    # columna izquierda: la tapa del curso
    cx0, cy0, cx1, cy1 = 50, 214, 470, 824
    d.rectangle((cx0 + 10, cy0 + 12, cx1 + 10, cy1 + 12), fill=(0, 0, 0))
    d.rectangle((cx0, cy0, cx1, cy1), fill=(40, 33, 30))
    d.rectangle((cx0 + 34, cy0 + 40, cx1 - 34, cy1 - 150), fill=(238, 231, 219))
    d.text(((cx0 + cx1) / 2, cy0 + 88), 'CURSO ONLINE', font=f(BCS, 26), fill=WINE, anchor='mt')
    d.text(((cx0 + cx1) / 2, cy0 + 128), 'A TU', font=f(BC, 70), fill=INK, anchor='mt')
    d.text(((cx0 + cx1) / 2, cy0 + 196), 'MEDIDA', font=f(BC, 70), fill=WINE, anchor='mt')
    d.text(((cx0 + cx1) / 2, cy0 + 276), 'ARREGLALA VOS MISMA', font=f(BCS, 24), fill=(120, 112, 104), anchor='mt')
    # maniquí en la tapa
    mx, my = (cx0 + cx1) / 2, cy0 + 372
    d.polygon([(mx - 78, my + 158), (mx - 54, my - 20), (mx + 54, my - 20), (mx + 78, my + 158)], fill=(176, 150, 128))
    d.ellipse((mx - 26, my - 72, mx + 26, my - 16), fill=(176, 150, 128))
    d.line([(mx, my + 158), (mx, my + 212)], fill=(90, 74, 62), width=10)
    d.line([(mx - 56, my + 212), (mx + 56, my + 212)], fill=(90, 74, 62), width=10)
    for i, yy in enumerate((my + 8, my + 58, my + 108)):
        d.line([(mx - 46 + i * 4, yy), (mx + 46 - i * 4, yy)], fill=(214, 196, 178), width=3)
    px, py = cx1 - 70, cy1 - 112
    d.ellipse((px - 92, py, px + 92, py + 112), fill=(255, 255, 255), outline=(216, 210, 200), width=2)
    d.text((px, py + 22), '+25', font=f(BC, 46), fill=WINE, anchor='mt')
    d.text((px, py + 68), 'VIDEOS', font=f(BCS, 26), fill=INK, anchor='mt')
    # columna derecha
    rx = 520
    d.text((rx, 216), 'ARREGLALA VOS MISMA', font=f(BCS, 28), fill=WINE)
    d.text((rx, 252), 'A Tu', font=f(SERIF, 84), fill=INK)
    d.text((rx, 342), 'Medida', font=f(SERIF, 84), fill=INK)
    for i, l in enumerate(('Dejá de pagarle a una modista y',
                           'aprendé a arreglar tu propia ropa',
                           'en casa, paso a paso.')):
        d.text((rx, 450 + i * 34), l, font=f(BCS, 30), fill=GREY)
    # estrellas dibujadas (la tipografia no tiene el glifo) + alumnas
    import math as _m
    for s in range(5):
        cx_, cy_, r_ = rx + 14 + s * 34, 580, 13
        pts = []
        for k in range(10):
            ang = -_m.pi / 2 + k * _m.pi / 5
            rad = r_ if k % 2 == 0 else r_ * 0.45
            pts.append((cx_ + rad * _m.cos(ang), cy_ + rad * _m.sin(ang)))
        d.polygon(pts, fill=(214, 164, 60))
    d.text((rx + 186, 566), '5.0  ·  +5000 alumnas', font=f(BCS, 28), fill=GREY)
    # pastilla de oferta en lugar del precio
    rr(d, (rx, 614, rx + 400, 690), 10, WINE)
    d.text((rx + 200, 630), 'AHORRÁS 40%  ·  HOY', font=f(BC, 42), fill=(255, 250, 248), anchor='mt')
    d.text((rx, 708), 'Pago único  ·  Acceso de por vida', font=f(BCS, 28), fill=GREY)
    for i, l in enumerate(('9 clases base',
                           '+25 videos de arreglos',
                           'Acceso de por vida',
                           'Miralo desde donde quieras',
                           '30 días de garantía')):
        y = 752 + i * 44
        d.ellipse((rx + 2, y + 8, rx + 22, y + 28), fill=WINE)
        d.line([(rx + 7, y + 18), (rx + 11, y + 23), (rx + 18, y + 13)], fill=(255, 255, 255), width=3)
        d.text((rx + 38, y), l, font=f(BCS, 30), fill=INK)
    rr(d, (rx, 982, rx + 430, 1058), 8, INK)
    d.text((rx + 215, 998), 'QUIERO EMPEZAR', font=f(BC, 42), fill=(255, 255, 255), anchor='mt')


def pagina_clases(d, w, h):
    d.rectangle((0, 0, w, 72), fill=(28, 26, 24))
    d.text((34, 20), 'A Tu Medida', font=f(SERIF, 36), fill=(246, 243, 238))
    d.text((w - 34, 26), 'MIS CLASES', font=f(BCS, 28), fill=(196, 190, 182), anchor='rt')
    d.text((40, 104), '9 clases base', font=f(SERIF, 52), fill=INK)
    d.text((40, 170), 'y +25 videos de marcado y costura sobre prendas reales', font=f(BCS, 28), fill=GREY)
    filas = [('01', 'El equipo que vas a necesitar', '6:12'),
             ('02', 'Medir con precisión', '8:40'),
             ('03', 'Planificar tu arreglo', '7:05'),
             ('04', 'Entender el calce e identificar problemas', '11:22'),
             ('05', 'Evaluar una prenda antes de arreglarla', '6:48'),
             ('06', 'La ciencia del marcado con alfileres', '9:31'),
             ('07', 'Cómo marcarte a vos misma', '10:04'),
             ('08', 'Pasar los alfileres a líneas de costura', '8:57'),
             ('09', 'Las telas más comunes y cómo se comportan', '12:16'),
             ('10', 'Meter la cintura de un jean', '7:42')]
    for i, (n, t_, dur) in enumerate(filas):
        y = 224 + i * 100
        rr(d, (40, y, w - 40, y + 86), 10, (255, 255, 255), (222, 216, 206), 2)
        rr(d, (56, y + 12, 170, y + 74), 8, (232, 226, 216))
        d.polygon([(100, y + 28), (100, y + 58), (128, y + 43)], fill=WINE)
        d.text((196, y + 14), t_, font=f(BCS, 34), fill=INK)
        d.text((196, y + 50), 'Clase ' + n + '  ·  ' + dur, font=f(BCS, 24), fill=GREY)
        d.ellipse((w - 92, y + 30, w - 64, y + 58), outline=(186, 180, 172), width=3)
    y = 224 + len(filas) * 100
    d.text((w / 2, y + 16), '+ 24 videos de arreglos más', font=f(BCS, 32), fill=GREY, anchor='mt')


if __name__ == '__main__':
    marco(laptop(pagina_venta), OUT + '/venta.png')
    marco(laptop(pagina_clases), OUT + '/clases.png')
    print('ok ->', OUT)
