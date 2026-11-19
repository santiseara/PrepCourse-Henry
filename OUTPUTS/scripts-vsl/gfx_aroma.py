# -*- coding: utf-8 -*-
"""Tapa del ebook "The Aromatic Plaster Atelier" (mercado ingles, 2026-11-19).

Replica de la tapa de "El Arte de Crear Aromatizadores Decorativos" (Manualidades con Proposito),
leida del cuadro del segundo 34 de su ad 7:
  - fondo crema, mitad superior tipografica y mitad inferior una foto de producto sobre lino;
  - linea chica en serif italica arriba, titulo grande en serif con dos renglones,
    ornamento, cuatro renglones de cuerpo chico centrado y una ramita dibujada;
  - sello redondo abajo a la izquierda.
La foto de producto sale de un cuadro real de un clip del pool (no se genera nada que cobre).

Uso: python3 gfx_aroma.py <foto_producto.jpg> <dir_salida>
  -> tapa.png (1000x1414) y tapa_inserto.png (1080x1920, la tapa sobre fondo, con sombra)
"""
import os, sys, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

FOTO, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)

W, H = 1000, 1414
CREAM  = (247, 242, 234)
INK    = (46, 40, 36)
INK_S  = (122, 108, 98)
LINE   = (205, 188, 170)

def didot(s, it=False): return ImageFont.truetype('/System/Library/Fonts/Supplemental/Didot.ttc', s, index=2 if it else 0)
def cochin(s, it=False): return ImageFont.truetype('/System/Library/Fonts/Supplemental/Cochin.ttc', s, index=0)
def didot_it(s): return ImageFont.truetype('/System/Library/Fonts/Supplemental/Didot.ttc', s, index=2)

def centro(d, y, txt, font, fill, sp=0):
    if sp:
        anchos = [d.textlength(c, font=font) for c in txt]
        total = sum(anchos) + sp * (len(txt) - 1)
        x = (W - total) / 2
        for c, a in zip(txt, anchos):
            d.text((x, y), c, font=font, fill=fill); x += a + sp
        return total
    a = d.textlength(txt, font=font)
    d.text(((W - a) / 2, y), txt, font=font, fill=fill)
    return a

def filete(d, cx, cy, w=150, col=LINE):
    """Filete con rombo al medio: el divisor de su tapa."""
    d.line([(cx - w, cy), (cx - 16, cy)], fill=col, width=2)
    d.line([(cx + 16, cy), (cx + w, cy)], fill=col, width=2)
    d.polygon([(cx, cy - 8), (cx + 8, cy), (cx, cy + 8), (cx - 8, cy)], outline=col, fill=None, width=2)

def grano(img, k=0.05):
    n = Image.effect_noise((img.width, img.height), 42).convert('L').filter(ImageFilter.GaussianBlur(0.7))
    return Image.blend(img, ImageChops.multiply(img, Image.merge('RGB', (n, n, n))), k)

# ---------------------------------------------------------------- tapa
im = Image.new('RGB', (W, H), CREAM)
d = ImageDraw.Draw(im)

# foto de producto: mitad inferior, con degradado suave hacia el crema
foto = Image.open(FOTO).convert('RGB')
fh = int(H * 0.50)
r = max(W / foto.width, fh / foto.height)
foto = foto.resize((int(foto.width * r), int(foto.height * r)), Image.LANCZOS)
foto = foto.crop(((foto.width - W) // 2, (foto.height - fh) // 2, (foto.width - W) // 2 + W, (foto.height - fh) // 2 + fh))
msk = Image.new('L', (W, fh), 255)
md = ImageDraw.Draw(msk)
for i in range(170):
    md.line([(0, i), (W, i)], fill=int(255 * (i / 170) ** 1.4))
im.paste(foto, (0, H - fh), msk)

y = 196
centro(d, y, 'The', didot_it(50), INK_S); y += 62
centro(d, y, 'Art of', didot_it(50), INK_S); y += 92
centro(d, y, 'Aromatic Plaster', didot(92), INK); y += 112
centro(d, y, 'Atelier', didot(92), INK); y += 126
filete(d, W // 2, y + 10, 110); y += 46

cuerpo = ['Learn to make aroma stones, scented tags',
          'and diffuser flowers with a premium finish,',
          'to decorate, to gift or to sell.']
fb = cochin(29)
for ln in cuerpo:
    centro(d, y, ln, fb, INK_S); y += 40
y += 26
filete(d, W // 2, y, 170)

# sello redondo abajo a la izquierda
sx, sy, sr = 136, H - 150, 66
d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(249, 244, 237), outline=(205, 186, 168), width=2)
fs = cochin(17)
for i, ln in enumerate(['THE AROMATIC', 'PLASTER']):
    a = d.textlength(ln, font=fs); d.text((sx - a / 2, sy - 26 + i * 21), ln, font=fs, fill=INK_S)
fsi = cochin(24, True)
a = d.textlength('Atelier', font=fsi); d.text((sx - a / 2, sy + 18), 'Atelier', font=fsi, fill=INK_S)

im = grano(im, 0.045)
im.save(os.path.join(OUT, 'tapa.png'))

# ---------------------------------------------------------------- inserto 1080x1920
# la tapa sobre lienzo transparente, con sombra y una pizca de rotacion: se compone sobre el b-roll
CW, CH = 1080, 1920
tapa = im.resize((int(W * 0.78), int(H * 0.78)), Image.LANCZOS).convert('RGBA')
tapa = tapa.rotate(-2.2, resample=Image.BICUBIC, expand=True)
sombra = Image.new('RGBA', (tapa.width + 90, tapa.height + 90), (0, 0, 0, 0))
ImageDraw.Draw(sombra).rectangle([45, 52, sombra.width - 45, sombra.height - 38], fill=(40, 30, 24, 150))
sombra = sombra.filter(ImageFilter.GaussianBlur(26))
lienzo = Image.new('RGBA', (CW, CH), (0, 0, 0, 0))
px, py = (CW - tapa.width) // 2, (CH - tapa.height) // 2
lienzo.alpha_composite(sombra, (px - 45, py - 45))
lienzo.alpha_composite(tapa, (px, py))
lienzo.save(os.path.join(OUT, 'tapa_inserto.png'))
print('tapa.png y tapa_inserto.png en', OUT)
