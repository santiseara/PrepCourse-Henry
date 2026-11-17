# -*- coding: utf-8 -*-
"""Estáticos de Macetas de Cemento (AR) en formato "caja de preguntas de Instagram".

Es el formato que pidió Santiago el 2026-11-17 pasando una captura de la competencia: foto real de
fondo, arriba el sticker de preguntas de IG (cabecera oscura + pregunta sobre fondo blanco) y debajo
una pila de burbujas de chat alineadas a la izquierda, azules y rojas, que contestan la objeción y
cierran con el CTA.

Las fotos de fondo son las dos escenas que más repite Aula Digital en sus 58 ads (medido por hash
sobre los 58 posters): el vivero de @materos_pertuz con la matera negra y el ficus en la maceta
blanca. Ver WIKI/macetas-de-cemento.md.

Uso: python3 gfx_preguntas_macetas.py <carpeta_cuadros> <carpeta_salida>
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1920
FD = os.path.expanduser('~/Desktop/macetas-cemento/anuncios/work/fonts')
MX = FD + '/Montserrat-ExtraBold.ttf'
SIS = '/System/Library/Fonts/Supplemental/Arial.ttf'
SIS_B = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
EMOJI = '/System/Library/Fonts/Apple Color Emoji.ttc'

GRIS = (43, 43, 48)
BLANCO = (255, 255, 255)
TINTA = (38, 38, 43)
AZUL = (47, 134, 238)
ROJO = (232, 65, 63)

FOTOS = [
    dict(src='A_20.6.png', out='PREG-1.jpg', crop_y=0.00,
         cabecera='Dudas sobre macetas de cemento',
         pregunta='¿Se necesita mucha inversión\npara empezar?',
         burbujas=[(AZUL,  'Es solo arena y cemento'),
                   (ROJO,  'Hacer cada maceta me\ncuesta $4.500'),
                   (ROJO,  'Las vendo a $60.000'),
                   (AZUL,  'Descargá mi guía paso\na paso ahora 👇')]),
    dict(src='B_1.2.png', out='PREG-2.jpg', crop_y=-0.10,
         cabecera='Dudas sobre macetas de cemento',
         pregunta='¿Me sirve si nunca hice\nuna en mi vida?',
         burbujas=[(AZUL,  'Yo tampoco sabía nada'),
                   (ROJO,  'Con una mesa y un molde\nya arrancás'),
                   (ROJO,  'Hoy vendo más de\n40 por mes'),
                   (AZUL,  'Descargá mi guía paso\na paso ahora 👇')]),
]


def emoji_img(ch, size):
    for s in (160, 128, 96):
        try:
            f = ImageFont.truetype(EMOJI, s)
        except Exception:
            return None
        im = Image.new('RGBA', (s * 2, s * 2), (0, 0, 0, 0))
        ImageDraw.Draw(im).text((s // 2, s // 2), ch, font=f, embedded_color=True)
        bb = im.getbbox()
        if bb:
            return im.crop(bb).resize((size, size), Image.LANCZOS)
    return None


def sombra(im, caja, rad, blur=18, alpha=95, dy=8):
    """Sombra suave detrás de una caja redondeada, sin tocar el resto del lienzo."""
    capa = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    x0, y0, x1, y1 = caja
    d.rounded_rectangle((x0, y0 + dy, x1, y1 + dy), rad, fill=(0, 0, 0, alpha))
    im.alpha_composite(capa.filter(ImageFilter.GaussianBlur(blur)))


def sticker(im, cabecera, pregunta, y0):
    """El sticker de preguntas de IG: cabecera oscura arriba y la pregunta sobre blanco."""
    d = ImageDraw.Draw(im)
    fc = ImageFont.truetype(SIS, 33)
    fp = ImageFont.truetype(SIS, 45)
    lineas = pregunta.split('\n')
    ancho = max([d.textlength(cabecera, font=fc)] + [d.textlength(l, font=fp) for l in lineas]) + 150
    ancho = min(max(ancho, 600), 820)
    x0 = (W - ancho) / 2
    h_cab = 74
    h_preg = 44 + 56 * len(lineas)
    caja = (x0, y0, x0 + ancho, y0 + h_cab + h_preg)
    sombra(im, caja, 22, blur=20, alpha=85)
    d = ImageDraw.Draw(im)
    # cuerpo blanco entero y después la cabecera oscura encima, así las esquinas quedan bien
    d.rounded_rectangle(caja, 22, fill=BLANCO + (255,))
    cab = Image.new('RGBA', (int(ancho), h_cab + 24), (0, 0, 0, 0))
    ImageDraw.Draw(cab).rounded_rectangle((0, 0, ancho, h_cab + 24), 22, fill=GRIS + (255,))
    im.alpha_composite(cab.crop((0, 0, int(ancho), h_cab)), (int(x0), int(y0)))
    d = ImageDraw.Draw(im)
    d.text((W / 2, y0 + h_cab / 2), cabecera, font=fc, fill=(222, 222, 228), anchor='mm')
    ty = y0 + h_cab + 26
    for l in lineas:
        d.text((W / 2, ty), l, font=fp, fill=TINTA, anchor='ma')
        ty += 56
    return y0 + h_cab + h_preg


def burbuja(im, color, texto, x0, y0, fsz=52):
    """Globo de chat: esquinas redondeadas y una colita abajo a la izquierda."""
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype(MX, fsz)
    lineas = texto.split('\n')
    anchos = []
    for l in lineas:
        cuerpo = ''.join(c for c in l if ord(c) < 0x2190)
        anchos.append(d.textlength(cuerpo, font=f) + (fsz + 10 if cuerpo != l else 0))
    bw = max(anchos) + 56
    if x0 + bw > W - 52:        # ninguna burbuja toca el borde: se achica la tipografía
        return burbuja(im, color, texto, x0, y0, fsz - 3)
    lh = fsz + 16
    bh = lh * len(lineas) + 34
    caja = (x0, y0, x0 + bw, y0 + bh)
    sombra(im, caja, 20, blur=14, alpha=80, dy=6)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle(caja, 20, fill=color + (255,))
    # colita
    d.polygon([(x0 + 26, y0 + bh - 2), (x0 + 72, y0 + bh - 2), (x0 + 30, y0 + bh + 22)], fill=color + (255,))
    ty = y0 + 17
    for l in lineas:
        cuerpo = ''.join(c for c in l if ord(c) < 0x2190)
        emo = ''.join(c for c in l if ord(c) >= 0x2190)
        tx = x0 + 28
        d.text((tx, ty), cuerpo, font=f, fill=BLANCO)
        if emo:
            e = emoji_img(emo[0], fsz)
            if e:
                im.alpha_composite(e, (int(tx + d.textlength(cuerpo, font=f) + 10), int(ty + 2)))
        ty += lh
    return y0 + bh + 26


if __name__ == '__main__':
    src_dir, dst = sys.argv[1], sys.argv[2]
    os.makedirs(dst, exist_ok=True)
    for cfg in FOTOS:
        base = Image.open(os.path.join(src_dir, cfg['src'])).convert('RGBA')
        esc = W / base.width
        base = base.resize((W, int(base.height * esc)), Image.LANCZOS)
        if esc > 1.2:
            base = base.filter(ImageFilter.UnsharpMask(radius=2, percent=70, threshold=3))
        top = int(max(0, (base.height - H) * (0.5 + cfg['crop_y'])))
        im = base.crop((0, top, W, top + H))
        if im.height < H:
            im = im.resize((W, H), Image.LANCZOS)
        # oscurecido parejo: el texto va sobre foto y tiene que leerse en el celular
        velo = Image.new('RGBA', (W, H), (0, 0, 0, 58))
        im.alpha_composite(velo)
        y = sticker(im, cfg['cabecera'], cfg['pregunta'], int(H * 0.12))
        y += 70
        x0 = int(W * 0.11)
        for color, txt in cfg['burbujas']:
            y = burbuja(im, color, txt, x0, y)
        im.convert('RGB').save(os.path.join(dst, cfg['out']), quality=92)
        print(os.path.join(dst, cfg['out']))
