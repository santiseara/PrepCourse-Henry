# -*- coding: utf-8 -*-
"""Dibuja la tapa de Alivio en Cada Plato y la compone sobre un cuadro REAL del pool,
con sombra y una pizca de rotacion, para que quede como la foto del libro sobre la mesa.

Modela la tapa del ganador israeli (fondo verde oliva claro, marco fino, titulo grande,
"500 recetas", bajada chica y una foto de comida abajo). La foto de la tapa tambien sale
de un cuadro real del pool: nada generado, nada de stock (regla del 17/11).

Uso:
  python3 gfx_alivio.py <cuadro_mesa.jpg> <cuadro_comida.jpg> <salida.png>
"""
import os, sys, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

DIR = os.path.dirname(os.path.abspath(__file__))
FD = os.environ.get('ALIVIO_FONTS', os.path.join(DIR, 'fonts'))
MX = os.path.join(FD, 'Montserrat-ExtraBold.ttf')
BC = os.path.join(FD, 'BarlowCondensed-ExtraBold.ttf')
SERIF = '/System/Library/Fonts/Supplemental/Didot.ttc'

VERDE = (74, 92, 58)        # verde oliva oscuro del texto
CREMA = (238, 237, 224)     # fondo de la tapa
LINEA = (150, 160, 128)

CW, CH = 760, 1060          # tapa en px antes de componer


def f(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.truetype(MX, size)


def ctr(d, y, txt, font, fill, sp=0):
    if sp:
        w = sum(d.textlength(c, font=font) + sp for c in txt) - sp
        x = (CW - w) / 2
        for c in txt:
            d.text((x, y), c, font=font, fill=fill)
            x += d.textlength(c, font=font) + sp
    else:
        d.text((CW / 2, y), txt, font=font, fill=fill, anchor='mt')


def tapa(food_path):
    im = Image.new('RGB', (CW, CH), CREMA)
    d = ImageDraw.Draw(im)
    d.rectangle((26, 26, CW - 27, CH - 27), outline=LINEA, width=3)

    ctr(d, 80, 'RECETARIO DIGITAL', f(BC, 34), LINEA, sp=5)
    ctr(d, 140, 'ALIVIO', f(SERIF, 132), VERDE)
    ctr(d, 290, 'EN CADA PLATO', f(SERIF, 62), VERDE)

    d.line((190, 390, CW - 190, 390), fill=LINEA, width=2)
    ctr(d, 412, '500 RECETAS', f(MX, 54), VERDE)
    ctr(d, 482, 'SIN GLUTEN Y SIN AZÚCAR', f(BC, 36), LINEA, sp=3)

    # foto real del pool, recortada en cuadrado y con esquinas redondeadas
    ph = 400
    fo = Image.open(food_path).convert('RGB')
    lado = min(fo.size)
    fo = fo.crop(((fo.width - lado) // 2, (fo.height - lado) // 2,
                  (fo.width + lado) // 2, (fo.height + lado) // 2)).resize((ph, ph), Image.LANCZOS)
    mask = Image.new('L', (ph, ph), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, ph - 1, ph - 1), 26, fill=255)
    im.paste(fo, ((CW - ph) // 2, 540), mask)

    ctr(d, 975, 'COMER RICO SIN HINCHARTE', f(BC, 30), LINEA, sp=3)
    return im


def shot(bg_path, food_path, out, seed=0):
    rnd = random.Random(seed)
    W, H = 1080, 1920
    bg = Image.open(bg_path).convert('RGB')
    esc = max(W / bg.width, H / bg.height) * 1.04
    bg = bg.resize((int(bg.width * esc), int(bg.height * esc)), Image.LANCZOS)
    bg = bg.crop(((bg.width - W) // 2, (bg.height - H) // 2,
                  (bg.width - W) // 2 + W, (bg.height - H) // 2 + H))
    bg = bg.filter(ImageFilter.GaussianBlur(2.2))
    bg = Image.blend(bg, Image.new('RGB', (W, H), (0, 0, 0)), 0.18)

    tp = tapa(food_path)
    k = 0.95        # el libro ocupa ~55 % del alto: la mesa tiene que verse, como en su insert
    tp = tp.resize((int(CW * k), int(CH * k)), Image.LANCZOS)
    ang = rnd.uniform(-3.2, -1.6)
    msk = Image.new('L', tp.size, 255).rotate(ang, Image.BICUBIC, expand=True, fillcolor=0)
    tp = tp.rotate(ang, Image.BICUBIC, expand=True, fillcolor=(0, 0, 0))

    px, py = (W - tp.width) // 2, (H - tp.height) // 2 + 60
    sh = Image.new('L', (W, H), 0)
    sh.paste(msk, (px + 16, py + 26))
    sh = sh.filter(ImageFilter.GaussianBlur(22))
    bg = Image.composite(Image.new('RGB', (W, H), (0, 0, 0)), bg, sh.point(lambda v: int(v * 0.55)))
    bg.paste(tp, (px, py), msk)
    bg.save(out)
    print(out, bg.size)


if __name__ == '__main__':
    shot(sys.argv[1], sys.argv[2], sys.argv[3], seed=int(sys.argv[4]) if len(sys.argv) > 4 else 0)
