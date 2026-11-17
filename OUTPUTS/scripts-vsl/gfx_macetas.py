# -*- coding: utf-8 -*-
"""Chips fijos arriba a la izquierda, calcados de Aula Digital 360 (macetas de cemento, AR).

Sus tres juegos, medidos sobre sus propios ads (360x640 -> escalados a 1080x1920):
  A · un chip azul:  "fabrica y emprende con macetas de cemento"
  B · azul "1 maceta de cemento = $60.000" + rojo "aprendé a fabricarlas y a venderlas desde 0."
      + rojo "Descargá nuestra guía 👇"
  C · rojo "APRENDÉ A FABRICAR MACETAS DE CEMENTO DESDE CERO" + azul "1 maceta de cemento: $60.000"
      + azul "inversión = $4.500"

Uso: python3 gfx_macetas.py <carpeta_salida>   -> chips_A.png, chips_B.png, chips_C.png
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
FD = os.path.expanduser('~/Desktop/macetas-cemento/anuncios/work/fonts')
MX = FD + '/Montserrat-ExtraBold.ttf'
EMOJI = '/System/Library/Fonts/Apple Color Emoji.ttc'
AZUL = (29, 118, 240)
ROJO = (214, 26, 32)
X0, Y0 = 26, 64
GAP = 9
PADX, PADY = 14, 9
RAD = 7

JUEGOS = {
    'A': [(AZUL, 36, ['fabrica y emprende con', 'macetas de cemento'])],
    'B': [(AZUL, 32, ['1 maceta de cemento = $60.000']),
          (ROJO, 32, ['aprendé a fabricarlas', 'y a venderlas desde 0.']),
          (ROJO, 32, ['Descargá nuestra guía 👇'])],
    'C': [(ROJO, 31, ['APRENDÉ A FABRICAR MACETAS', 'DE CEMENTO DESDE CERO']),
          (AZUL, 31, ['1 maceta de cemento: $60.000']),
          (AZUL, 31, ['inversión = $4.500'])],
}


def emoji_img(ch, size):
    for s in (160, 128, 96, 64):
        try:
            f = ImageFont.truetype(EMOJI, s)
            im = Image.new('RGBA', (s * 2, s * 2), (0, 0, 0, 0))
            ImageDraw.Draw(im).text((s // 2, s // 2), ch, font=f, embedded_color=True)
            bb = im.getbbox()
            if bb:
                return im.crop(bb).resize((size, size), Image.LANCZOS)
        except Exception:
            continue
    return None


def chip_png(juego, path):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    y = Y0
    for color, fsz, lineas in JUEGOS[juego]:
        f = ImageFont.truetype(MX, fsz)
        lh = fsz + 9
        anchos = []
        for ln in lineas:
            cuerpo = ''.join(c for c in ln if ord(c) < 0x2190)
            extra = fsz + 6 if cuerpo != ln else 0
            anchos.append(d.textlength(cuerpo, font=f) + extra)
        bw = max(anchos) + PADX * 2
        bh = lh * len(lineas) + PADY * 2 - 4
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
    im.save(path)
    return path


if __name__ == '__main__':
    dst = sys.argv[1] if len(sys.argv) > 1 else '.'
    os.makedirs(dst, exist_ok=True)
    for j in JUEGOS:
        print(chip_png(j, os.path.join(dst, f'chips_{j}.png')))
