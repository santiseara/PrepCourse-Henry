# -*- coding: utf-8 -*-
"""Las 2 fotos (estáticos 4:5) de Macetas de Cemento AR, con la estética exacta de Aula Digital 360.

Aula Digital corre 58 ads y los 58 son video: no hay un estático que copiar. Lo que sí se repite en
todos sus videos son DOS planos (los de @ali.diyideas 7678821416162184478): la maceta de tela blanca
con el moño amarillo y las flores, y las tres macetas terminadas en el living. Esas son "las que se
repiten mucho", y son las que van a foto.

De sus videos se copia el sistema entero: chips arriba a la izquierda y titular abajo en mayúscula,
blanco con borde negro grueso y una parte adentro de una caja roja o verde.

Uso: python3 gfx_fotos_macetas.py <carpeta_cuadros> <carpeta_salida>
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1350
FD = os.path.expanduser('~/Desktop/macetas-cemento/anuncios/work/fonts')
MX = FD + '/Montserrat-ExtraBold.ttf'
AZUL = (29, 118, 240)
ROJO = (214, 26, 32)
VERDE = (34, 197, 64)
X0, Y0, GAP, PADX, PADY, RAD = 26, 46, 9, 14, 9, 7

FOTOS = [
    dict(src='h_19.4.png', out='FOTO-1.jpg', crop_y=0.00,
         chips=[(AZUL, 32, ['1 maceta de cemento = $60.000']),
                (ROJO, 32, ['aprendé a fabricarlas', 'y a venderlas desde 0.']),
                (ROJO, 32, ['Descargá nuestra guía 👇'])],
         titulo=[('LA HICE YO\n', None), ('ARENA Y CEMENTO', VERDE), (' NADA MÁS', None)]),
    dict(src='h_23.0.png', out='FOTO-2.jpg', crop_y=0.06,
         chips=[(ROJO, 31, ['APRENDÉ A FABRICAR MACETAS', 'DE CEMENTO DESDE CERO']),
                (AZUL, 31, ['1 maceta de cemento: $60.000']),
                (AZUL, 31, ['inversión = $4.500'])],
         titulo=[('HOY VENDO\n', None), ('40 POR MES', ROJO), ('\nDESDE MI CASA', None)]),
]


def emoji_img(ch, size):
    for s in (160, 128, 96):
        try:
            f = ImageFont.truetype('/System/Library/Fonts/Supplemental/Apple Color Emoji.ttc', s)
        except Exception:
            try:
                f = ImageFont.truetype('/System/Library/Fonts/Apple Color Emoji.ttc', s)
            except Exception:
                return None
        im = Image.new('RGBA', (s * 2, s * 2), (0, 0, 0, 0))
        ImageDraw.Draw(im).text((s // 2, s // 2), ch, font=f, embedded_color=True)
        bb = im.getbbox()
        if bb:
            return im.crop(bb).resize((size, size), Image.LANCZOS)
    return None


def pegar_chips(im, chips):
    d = ImageDraw.Draw(im)
    y = Y0
    for color, fsz, lineas in chips:
        f = ImageFont.truetype(MX, fsz)
        lh = fsz + 9
        anchos = []
        for ln in lineas:
            cuerpo = ''.join(c for c in ln if ord(c) < 0x2190)
            anchos.append(d.textlength(cuerpo, font=f) + (fsz + 6 if cuerpo != ln else 0))
        bw, bh = max(anchos) + PADX * 2, lh * len(lineas) + PADY * 2 - 4
        d.rounded_rectangle((X0 + 3, y + 3, X0 + bw + 3, y + bh + 3), RAD, fill=(0, 0, 0, 90))
        d.rounded_rectangle((X0, y, X0 + bw, y + bh), RAD, fill=color + (255,))
        ty = y + PADY - 2
        for ln in lineas:
            cuerpo = ''.join(c for c in ln if ord(c) < 0x2190)
            emo = ''.join(c for c in ln if ord(c) >= 0x2190)
            tx = X0 + (bw - (d.textlength(cuerpo, font=f) + (fsz + 6 if emo else 0))) / 2
            d.text((tx, ty), cuerpo, font=f, fill=(255, 255, 255))
            if emo:
                e = emoji_img(emo[0], fsz)
                if e:
                    im.alpha_composite(e, (int(tx + d.textlength(cuerpo, font=f) + 6), int(ty + 1)))
            ty += lh
        y += bh + GAP


def titular(im, partes, fsz=76, y=None):
    """Mayúscula, blanco con borde negro grueso; los tramos marcados van adentro de una caja."""
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype(MX, fsz)
    texto = ''.join(t for t, _ in partes).upper()
    # dos líneas si no entra
    lineas = []
    for trozo in texto.split('\n'):
        cur = ''
        for p in trozo.split():
            t = (cur + ' ' + p).strip()
            if d.textlength(t, font=f) > W - 110 and cur:
                lineas.append(cur); cur = p
            else:
                cur = t
        lineas.append(cur)
    lh = fsz + 16
    y0 = (y if y is not None else H - 70 - lh * len(lineas))
    # mapa caracter -> color de caja
    colores = []
    for t, c in partes:
        colores += [c] * len(t.upper())
    i = 0
    for ln in lineas:
        wln = d.textlength(ln, font=f)
        x = (W - wln) / 2
        # saltear el espacio que separa lineas
        while i < len(texto) and texto[i] in ' \n':
            i += 1
        # cajas primero
        j, xx = i, x
        for ch in ln:
            col = colores[j] if j < len(colores) else None
            cw = d.textlength(ch, font=f)
            if col:
                d.rounded_rectangle((xx - 4, y0 - 8, xx + cw + 4, y0 + fsz + 18), 5, fill=col + (255,))
            xx += cw; j += 1
        # texto con borde
        xx, j = x, i
        for ch in ln:
            for dx in (-5, -3, 0, 3, 5):
                for dy in (-5, -3, 0, 3, 5):
                    if dx or dy:
                        d.text((xx + dx, y0 + dy), ch, font=f, fill=(0, 0, 0))
            d.text((xx, y0), ch, font=f, fill=(255, 255, 255))
            xx += d.textlength(ch, font=f); j += 1
        i = j
        y0 += lh


if __name__ == '__main__':
    src_dir, dst = sys.argv[1], sys.argv[2]
    os.makedirs(dst, exist_ok=True)
    for cfg in FOTOS:
        base = Image.open(os.path.join(src_dir, cfg['src'])).convert('RGBA')
        esc = W / base.width
        base = base.resize((W, int(base.height * esc)), Image.LANCZOS)
        top = int((base.height - H) * (0.5 + cfg['crop_y']))
        im = base.crop((0, max(0, top), W, max(0, top) + H))
        # viñeta suave abajo para que el titular se lea siempre
        sombra = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        ds = ImageDraw.Draw(sombra)
        for k in range(360):
            ds.line([(0, H - k), (W, H - k)], fill=(0, 0, 0, int(118 * (k / 360) ** 1.6)))
        im.alpha_composite(sombra)
        pegar_chips(im, cfg['chips'])
        titular(im, cfg['titulo'])
        im.convert('RGB').save(os.path.join(dst, cfg['out']), quality=94)
        print(os.path.join(dst, cfg['out']))
