# -*- coding: utf-8 -*-
"""Pasa el logo de "SEGREDO DA INSULINA" a "SECRETO DE LA INSULINA".

La palabra INSULINA no se toca: lo unico que cambia es el renglon de arriba,
que ademas viene ARQUEADO. Receta (regla del 19/11 de quizzes-reglas-de-armado):
  1. tapar la banda del renglon viejo interpolando cada columna entre la fila
     limpia de arriba y la de abajo (el fondo del ovalo es un degrade vertical);
  2. retipear letra por letra sobre la misma parabola, con Montserrat Black,
     el color exacto del original (#FE8602) y la rotacion local de la curva.

Entrada:  el PNG original del logo (assets/logo-ozempic-*.png del bundle).
Salida:   logo-es.png, que despues se comprime a ../imagenes/logo.webp.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np, math, sys

ORIGINAL = sys.argv[1] if len(sys.argv) > 1 else 'img-logo-ozempic-CLWt-YVF.png'
FUENTE   = sys.argv[2] if len(sys.argv) > 2 else 'M-BK.ttf'   # Montserrat-Black
SALIDA   = sys.argv[3] if len(sys.argv) > 3 else 'logo-es.png'

TEXTO = "SECRETO DE LA"
COLOR = (254, 134, 2, 255)          # medido sobre la tinta del original
CAP   = 65                          # altura de mayuscula medida en el original
ANCHO = 620.0                       # ancho de la linea nueva, centrada en x=594
CENTRO_X = 594
BANDA = (282, 912, 104, 200)        # x0, x1, y0, y1 del renglon viejo
# parabola ajustada sobre la base de las 9 letras de "SEGREDO DA"
COEF = [1.79084575e-04, -2.04806130e-01, 2.35509107e+02]

baseY = lambda x: float(np.polyval(COEF, x))
slope = lambda x: 2 * COEF[0] * x + COEF[1]

# ── 1. tapar el renglon viejo ──────────────────────────────────────────────
src = Image.open(ORIGINAL).convert('RGBA')
out = np.array(src).astype(float)
X0, X1, Y0, Y1 = BANDA
for x in range(X0, X1):
    ca, cb = out[Y0 - 1, x, :3].copy(), out[Y1 + 1, x, :3].copy()
    for y in range(Y0, Y1 + 1):
        t = (y - (Y0 - 1)) / ((Y1 + 1) - (Y0 - 1))
        out[y, x, :3] = ca * (1 - t) + cb * t
        out[y, x, 3] = 255
base = Image.fromarray(out.clip(0, 255).astype('uint8'))
m = Image.new('L', base.size, 0)
ImageDraw.Draw(m).rectangle([X0 - 2, Y0 - 2, X1 + 2, Y1 + 2], fill=255)
m = m.filter(ImageFilter.GaussianBlur(3))
base = Image.composite(base.filter(ImageFilter.GaussianBlur(1.2)), base, m)

# ── 2. retipear sobre el arco ──────────────────────────────────────────────
f = ImageFont.truetype(FUENTE, 100)
bb = f.getbbox("H")
sz = int(round(100 * CAP / (bb[3] - bb[1])))
f = ImageFont.truetype(FUENTE, sz)
adv = [f.getlength(c) for c in TEXTO]
k = ANCHO / sum(adv)

img = base.copy()
x = CENTRO_X - ANCHO / 2
for ch, w in zip(TEXTO, adv):
    w2 = w * k
    if ch != ' ':
        cx = x + w2 / 2
        bb = f.getbbox(ch)
        pad = 30
        lay = Image.new('RGBA', (int(bb[2] - bb[0]) + 2 * pad, int(bb[3] - bb[1]) + 2 * pad), (0, 0, 0, 0))
        ImageDraw.Draw(lay).text((pad - bb[0], pad - bb[1]), ch, font=f, fill=COLOR)
        lay = lay.resize((max(1, int(lay.width * k)), lay.height), Image.LANCZOS)
        rot = lay.rotate(-math.degrees(math.atan(slope(cx))), resample=Image.BICUBIC, expand=True)
        dy = (rot.height - lay.height) / 2
        img.alpha_composite(rot, (int(round(cx - rot.width / 2)),
                                  int(round(baseY(cx) - (lay.height - pad) - dy))))
    x += w2

img.save(SALIDA)
print(SALIDA, img.size)
