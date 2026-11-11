"""Rehace los textos del mockup del quiz al castellano, sin IA.
Borra cada texto quemado interpolando el fondo y vuelve a tipear con Playfair/Great Vibes.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np

SRC = 'img/12.webp'
OUT = 'out_12.png'
PLAY = 'fonts/PlayfairDisplay[wght].ttf'
SCRIPT = 'fonts/GreatVibes-Regular.ttf'


def playfair(size, peso='Bold'):
    f = ImageFont.truetype(PLAY, size)
    f.set_variation_by_name(peso)
    return f


def borrar(a, box, suave=7):
    """Rellena box interpolando desde los bordes (horizontal + vertical)."""
    x0, y0, x1, y1 = box
    m = 3
    izq = a[y0:y1, max(0, x0 - m):x0].mean(axis=1)      # (h,3)
    der = a[y0:y1, x1:x1 + m].mean(axis=1)
    arr = a[max(0, y0 - m):y0, x0:x1].mean(axis=0)      # (w,3)
    aba = a[y1:y1 + m, x0:x1].mean(axis=0)
    h, w = y1 - y0, x1 - x0
    tx = np.linspace(0, 1, w)[None, :, None]
    ty = np.linspace(0, 1, h)[:, None, None]
    ph = izq[:, None, :] * (1 - tx) + der[:, None, :] * tx
    pv = arr[None, :, :] * (1 - ty) + aba[None, :, :] * ty
    parche = (ph + pv) / 2
    a[y0:y1, x0:x1] = parche
    return a


def suavizar(im, box, radio=6):
    x0, y0, x1, y1 = box
    pad = 10
    caja = (max(0, x0 - pad), max(0, y0 - pad), min(im.width, x1 + pad), min(im.height, y1 + pad))
    reg = im.crop(caja).filter(ImageFilter.GaussianBlur(radio))
    im.paste(reg, caja)
    return im


def centrar(d, texto, font, box, dy=0, color=(74, 33, 28)):
    x0, y0, x1, y1 = box
    bb = d.textbbox((0, 0), texto, font=font)
    x = x0 + ((x1 - x0) - (bb[2] - bb[0])) / 2 - bb[0]
    y = y0 + ((y1 - y0) - (bb[3] - bb[1])) / 2 - bb[1] + dy
    d.text((x, y), texto, font=font, fill=color)


def ajustar(d, texto, box, maxalto, peso='Bold', inicio=90):
    """Devuelve la fuente más grande que entra en el ancho de box."""
    size = inicio
    while size > 12:
        f = playfair(size, peso)
        bb = d.textbbox((0, 0), texto, font=f)
        if bb[2] - bb[0] <= (box[2] - box[0]) and bb[3] - bb[1] <= maxalto:
            return f
        size -= 2
    return playfair(12, peso)


im = Image.open(SRC).convert('RGB')
a = np.asarray(im).astype(float)

CAJAS = {
    'tapaA':   (178, 160, 468, 284),
    'lomoA':   (68, 240, 114, 545),
    'tapaB':   (602, 178, 938, 318),
    'sello':   (884, 82, 1086, 196),
    'principal': (352, 586, 758, 792),
    'tapaC':   (72, 632, 302, 756),
    'lomoC':   (2, 726, 48, 1096),
    'tapaD':   (836, 680, 1038, 802),
    'tag':     (888, 908, 1008, 962),
}
for b in CAJAS.values():
    a = borrar(a, b)
im = Image.fromarray(np.clip(a, 0, 255).astype('uint8'))
for b in CAJAS.values():
    im = suavizar(im, b, 5)

d = ImageDraw.Draw(im)
TINTA = (74, 33, 28)
TINTA2 = (92, 46, 38)

def dos_lineas(l1, l2, x0, x1, ytop, ybot, maxalto, color=(74, 33, 28), inicio=90):
    """Las dos líneas con el MISMO cuerpo: el que entra para la más larga."""
    larga = l1 if d.textlength(l1, font=playfair(40)) > d.textlength(l2, font=playfair(40)) else l2
    f = ajustar(d, larga, (x0, 0, x1, 0), maxalto, inicio=inicio)
    mitad = (ytop + ybot) / 2
    centrar(d, l1, f, (x0, ytop, x1, mitad), color=color)
    centrar(d, l2, f, (x0, mitad, x1, ybot), color=color)


# --- Tapa A: Packaging para Regalar ---
dos_lineas('Packaging', 'para Regalar', 178, 468, 160, 284, 66, inicio=76)

# --- Tapa B: Duración y Conservación ---
dos_lineas('Duración y', 'Conservación', 612, 878, 180, 314, 66, inicio=76)

# --- Sello: Garantía 30 días ---
dos_lineas('Garantía', '30 días', 914, 1058, 94, 186, 42, color=(86, 50, 18), inicio=42)

# --- Tapa principal: Cápsulas / Encantadas ---
f = ajustar(d, 'Cápsulas', (368, 0, 742, 0), 110, inicio=120)
centrar(d, 'Cápsulas', f, (368, 592, 742, 694), color=(72, 28, 30))
fs = ImageFont.truetype(SCRIPT, 118)
centrar(d, 'Encantadas', fs, (360, 694, 750, 790), color=(120, 44, 52))

# --- Tapa C: Precios Claros ---
dos_lineas('Precios', 'Claros', 80, 288, 638, 750, 54, inicio=56)

# --- Tapa D: Tus Primeros Pedidos ---
dos_lineas('Tus Primeros', 'Pedidos', 842, 1032, 684, 798, 52, inicio=56)

# --- Tarjetita: Gracias ---
fs = ImageFont.truetype(SCRIPT, 46)
centrar(d, 'Gracias', fs, (888, 904, 1008, 956), color=(128, 92, 84))

# --- Lomos: texto chico vertical ---
for clave, texto in (('lomoA', 'Packaging para Regalar'), ('lomoC', 'Precios Claros')):
    x0, y0, x1, y1 = CAJAS[clave]
    alto = y1 - y0
    cap = Image.new('RGBA', (alto, x1 - x0), (0, 0, 0, 0))
    dd = ImageDraw.Draw(cap)
    f = playfair(23, 'Regular')
    bb = dd.textbbox((0, 0), texto, font=f)
    dd.text(((alto - (bb[2] - bb[0])) / 2 - bb[0], ((x1 - x0) - (bb[3] - bb[1])) / 2 - bb[1]),
            texto, font=f, fill=(120, 80, 72, 190))
    cap = cap.rotate(90, expand=True)
    im.paste(cap, (x0, y0), cap)

im.save(OUT)
print('ok', OUT)
