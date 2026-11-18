#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Los subtitulos y las graficas de Fernanda Lucas, medidos sobre los 8 creativos
bajados el 18/11/2026 en 720x1280 y reescalados a 1080x1920.

Un estilo por anuncio:
  amarillo   g1  MAYUSCULAS amarillo #FFE100 con contorno negro      (1640...)
  minuscula  g2  una palabra en minuscula, blanca con contorno       (1105... y 4574...)
  azul       g4  MAYUSCULAS blancas, palabra activa en caja azul     (2358...)
  violeta    g5  MAYUSCULAS blancas, palabra activa en caja violeta  (3085...)
  verde      g6  MAYUSCULAS blancas, palabra activa en caja verde    (1348...)
  banda      g7  MAYUSCULAS blancas sobre banda gris translucida     (28990...)
  ranking    g8  banda de arriba ÓPTIMO / BUENO / MALO + titular     (1166...)

Cada funcion devuelve una imagen RGBA de 1080x1920 lista para pegar encima.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
FONTDIR = os.path.expanduser('~/Desktop/cabello-fuerte/work/fonts')
ANTON = f'{FONTDIR}/Anton-Regular.ttf'
MONT = f'{FONTDIR}/Montserrat-Black.ttf'
POPP = f'{FONTDIR}/Poppins-Bold.ttf'

AMARILLO = (255, 225, 0, 255)
BLANCO = (255, 255, 255, 255)
NEGRO = (0, 0, 0, 255)
AZUL = (26, 115, 232, 255)
VIOLETA = (91, 22, 200, 255)
VERDE = (22, 163, 74, 255)
GRIS = (74, 74, 74, 190)
ROJO = (214, 34, 34, 255)

_cache = {}
def fuente(path, size, peso='Black'):
    k = (path, size, peso)
    if k not in _cache:
        f = ImageFont.truetype(path, size)
        try:
            f.set_variation_by_name(peso)   # Montserrat viene como fuente variable
        except Exception:
            pass
        _cache[k] = f
    return _cache[k]


def _ancho(d, txt, f):
    a, b, c, e = d.textbbox((0, 0), txt, font=f)
    return c - a


def _contorno(d, x, y, txt, f, relleno, borde, grosor, anchor='lt'):
    for dx in range(-grosor, grosor + 1):
        for dy in range(-grosor, grosor + 1):
            if dx * dx + dy * dy <= grosor * grosor:
                d.text((x + dx, y + dy), txt, font=f, fill=borde, anchor=anchor)
    d.text((x, y), txt, font=f, fill=relleno, anchor=anchor)


def _lienzo():
    return Image.new('RGBA', (W, H), (0, 0, 0, 0))


# ---------------------------------------------------------------- estilos

def _partir(d, texto, f, ancho_max):
    """Parte el texto en las lineas que entren en `ancho_max` pixeles."""
    palabras = texto.split()
    lineas, cur = [], ''
    for p in palabras:
        prueba = (cur + ' ' + p).strip()
        if _ancho(d, prueba, f) > ancho_max and cur:
            lineas.append(cur); cur = p
        else:
            cur = prueba
    if cur:
        lineas.append(cur)
    return lineas


def amarillo(texto, y=0.755):
    """g1 — MAYUSCULAS amarillas con contorno negro grueso, hasta dos lineas."""
    img = _lienzo(); d = ImageDraw.Draw(img)
    f = fuente(MONT, 66)
    t = texto.upper()
    lineas = _partir(d, t, f, W * 0.88)
    # si no entra en dos lineas, achicar la fuente hasta que entre
    tam = 66
    while len(lineas) > 2 and tam > 42:
        tam -= 4
        f = fuente(MONT, tam)
        lineas = _partir(d, t, f, W * 0.88)
    alto_l = int(tam * 1.18)
    cy = int(H * y)
    y0 = cy - (len(lineas) - 1) * alto_l // 2
    for i, l in enumerate(lineas):
        _contorno(d, W // 2, y0 + i * alto_l, l, f, AMARILLO, NEGRO, 7, anchor='mm')
    return img


def minuscula(texto, y=0.779):
    """g2 y g3 — una sola palabra en minuscula, blanca con contorno negro fino."""
    img = _lienzo(); d = ImageDraw.Draw(img)
    f = fuente(POPP, 62)
    _contorno(d, W // 2, int(H * y), texto.lower(), f, BLANCO, NEGRO, 5, anchor='mm')
    return img


def _caja_palabras(texto, activa, color_caja, y, size, font_path, grosor=4,
                   radio=10, pad=(14, 8)):
    """MAYUSCULAS blancas con la palabra activa adentro de una caja de color.
    Reparte en hasta dos renglones si no entra de una."""
    img = _lienzo(); d = ImageDraw.Draw(img)
    f = fuente(font_path, size)
    palabras = texto.upper().split()
    esp = _ancho(d, ' ', f)
    # repartir en renglones que entren en el 88 % del ancho
    reng, cur = [], []
    for i, p in enumerate(palabras):
        prueba = cur + [p]
        anchoP = sum(_ancho(d, q, f) for q in prueba) + esp * (len(prueba) - 1)
        if anchoP > W * 0.88 and cur:
            reng.append(cur); cur = [p]
        else:
            cur = prueba
    if cur:
        reng.append(cur)
    alto = f.getbbox('Mg')[3] - f.getbbox('Mg')[1]
    alto_l = int(size * 1.22)
    cy0 = int(H * y) - (len(reng) - 1) * alto_l // 2
    k = 0
    for r, linea in enumerate(reng):
        anchos = [_ancho(d, q, f) for q in linea]
        total = sum(anchos) + esp * (len(linea) - 1)
        x = (W - total) // 2
        cy = cy0 + r * alto_l
        for j, p in enumerate(linea):
            if k == activa:
                x0 = x - pad[0]; x1 = x + anchos[j] + pad[0]
                y0 = cy - alto // 2 - pad[1]; y1 = cy + alto // 2 + pad[1]
                d.rounded_rectangle([x0, y0, x1, y1], radius=radio, fill=color_caja)
                d.text((x + anchos[j] // 2, cy), p, font=f, fill=BLANCO, anchor='mm')
            else:
                _contorno(d, x + anchos[j] // 2, cy, p, f, BLANCO, NEGRO, grosor, anchor='mm')
            x += anchos[j] + esp
            k += 1
    return img


def azul(texto, activa=0, y=0.775):
    return _caja_palabras(texto, activa, AZUL, y, 58, MONT, radio=12)


def violeta(texto, activa=0, y=0.778):
    return _caja_palabras(texto, activa, VIOLETA, y, 54, ANTON, radio=4, pad=(10, 6))


def verde(texto, activa=0, y=0.600):
    return _caja_palabras(texto, activa, VERDE, y, 52, ANTON, radio=4, pad=(10, 6))


def banda(texto, y=0.797, ancho_max=0.86):
    """g7 — MAYUSCULAS blancas sobre banda gris translucida, hasta dos lineas."""
    img = _lienzo(); d = ImageDraw.Draw(img)
    f = fuente(MONT, 54)
    palabras = texto.upper().split()
    lineas, cur = [], ''
    for p in palabras:
        prueba = (cur + ' ' + p).strip()
        if _ancho(d, prueba, f) > W * ancho_max and cur:
            lineas.append(cur); cur = p
        else:
            cur = prueba
    if cur: lineas.append(cur)
    lineas = lineas[:2]
    alto_l = 66
    cy = int(H * y)
    altura = alto_l * len(lineas)
    anchos = [_ancho(d, l, f) for l in lineas]
    x0 = (W - max(anchos)) // 2 - 26
    x1 = (W + max(anchos)) // 2 + 26
    d.rectangle([x0, cy - altura // 2 - 16, x1, cy + altura // 2 + 16], fill=GRIS)
    y0 = cy - altura // 2 + alto_l // 2
    for i, l in enumerate(lineas):
        d.text((W // 2, y0 + i * alto_l), l, font=f, fill=BLANCO, anchor='mm')
    return img


def ranking(activo=None, titulo='¿CAÍDA DE PELO?'):
    """g8 — la banda de arriba con OPTIMO / BUENO / MALO.
    activo: 0, 1 o 2 para encender una columna (se dibuja mas grande y en verde lima)."""
    img = _lienzo(); d = ImageDraw.Draw(img)
    ft = fuente(MONT, 54)
    fe = fuente(MONT, 46)
    LIMA = (190, 255, 60, 255)
    _contorno(d, W // 2, 140, titulo, ft, LIMA, NEGRO, 5, anchor='mm')
    cols = [('ÓPTIMO', (56, 142, 90)), ('BUENO', (56, 142, 90)), ('MALO', (200, 60, 70))]
    xs = [W * 0.21, W * 0.51, W * 0.81]
    for i, ((txt, col), x) in enumerate(zip(cols, xs)):
        r = 52
        d.ellipse([x - r, 250 - r, x + r, 250 + r], fill=col + (255,))
        # el tilde y la cruz se dibujan: la fuente no los trae
        if i == 0:
            d.line([(x - 24, 250), (x - 6, 270), (x + 26, 228)], fill=BLANCO, width=10,
                   joint='curve')
        elif i == 2:
            d.line([(x - 22, 228), (x + 22, 272)], fill=BLANCO, width=10)
            d.line([(x + 22, 228), (x - 22, 272)], fill=BLANCO, width=10)
        else:
            # el pulgar arriba sale del emoji del sistema; si falla, un pulgar dibujado
            try:
                # el emoji va en su propia capa: dibujarlo sobre el mismo lienzo
                # rompe los textos que vienen despues
                f_emoji = ImageFont.truetype('/System/Library/Fonts/Apple Color Emoji.ttc', 48)
                cap = Image.new('RGBA', (120, 120), (0, 0, 0, 0))
                ImageDraw.Draw(cap).text((60, 60), '\U0001F44D', font=f_emoji,
                                         anchor='mm', embedded_color=True)
                img.alpha_composite(cap, (int(x) - 60, 250 - 60))
            except Exception:
                d.line([(x - 16, 262), (x - 16, 236), (x - 2, 222)], fill=BLANCO,
                       width=9, joint='curve')
                d.rectangle([x - 20, 238, x + 22, 266], fill=BLANCO)
        color = LIMA if activo == i else BLANCO
        _contorno(d, x, 380, txt, fe, color, NEGRO, 5, anchor='mm')
    return img


def titular_grande(texto, y=0.57, color=(190, 255, 60, 255)):
    """g8 — el nombre del producto que se tacha (Minoxidil, Biotina...) en grande,
    a la altura del pecho de la presentadora, como en el original.

    Medido sobre el original: la palabra ocupa ~82 % del ancho y cae sobre el
    pecho, no arriba: pegada al titulo del sticker se come la fila del ranking."""
    img = _lienzo(); d = ImageDraw.Draw(img)
    f = fuente(MONT, 140)
    while _ancho(d, texto, f) > W * 0.88 and f.size > 56:
        f = fuente(MONT, f.size - 4)
    _contorno(d, W // 2, int(H * y), texto, f, color, NEGRO, 7, anchor='mm')
    return img


def caja_hook(linea_blanca, lineas_rojas):
    """g4 — el cartel de arriba de los primeros 8 segundos: una linea blanca
    sobre banda negra y dos sobre banda roja. Medido sobre el original."""
    img = _lienzo(); d = ImageDraw.Draw(img)
    # banda negra
    d.rectangle([0, 0, W, 205], fill=(8, 8, 8, 255))
    fb = fuente(MONT, 68)
    while _ancho(d, linea_blanca.upper(), fb) > W * 0.95 and fb.size > 40:
        fb = fuente(MONT, fb.size - 3)
    d.text((W // 2, 118), linea_blanca.upper(), font=fb, fill=BLANCO, anchor='mm')
    # banda roja
    d.rectangle([0, 224, W, 389], fill=(205, 16, 20, 255))
    fr = fuente(MONT, 58)
    ls = lineas_rojas[:2]
    ys = [306] if len(ls) == 1 else [280, 350]
    for y, l in zip(ys, ls):
        ff = fr
        while _ancho(d, l.upper(), ff) > W * 0.95 and ff.size > 34:
            ff = fuente(MONT, ff.size - 3)
        d.text((W // 2, y), l.upper(), font=ff, fill=BLANCO, anchor='mm')
    return img


def boton_inscribirme(y=0.86):
    """El boton rojo INSCRIBIRME que aparece sobre el cierre."""
    img = _lienzo(); d = ImageDraw.Draw(img)
    f = fuente(MONT, 52)
    t = 'INSCRIBIRME'
    a = _ancho(d, t, f)
    cy = int(H * y)
    d.rounded_rectangle([(W - a) // 2 - 36, cy - 48, (W + a) // 2 + 36, cy + 48],
                        radius=14, fill=ROJO)
    d.text((W // 2, cy), t, font=f, fill=BLANCO, anchor='mm')
    return img


ESTILOS = {
    'amarillo': amarillo,
    'minuscula': minuscula,
    'azul': azul,
    'violeta': violeta,
    'verde': verde,
    'banda': banda,
}

if __name__ == '__main__':
    out = os.path.expanduser('~/Desktop/cabello-fuerte/work/muestras')
    os.makedirs(out, exist_ok=True)
    fondo = Image.new('RGB', (W, H), (60, 60, 60))
    pruebas = [
        ('amarillo', amarillo('nuevo en tu cabeza')),
        ('minuscula', minuscula('cabelludo')),
        ('azul', azul('no tenia mas el', 0)),
        ('violeta', violeta('cuidaron de los hijos a', 0)),
        ('verde', verde('los sintomas', 1)),
        ('banda', banda('vos mirás esa foto de hace diez años')),
        ('ranking', ranking(2)),
        ('titular', titular_grande('Minoxidil')),
        ('boton', boton_inscribirme()),
    ]
    for n, im in pruebas:
        c = fondo.copy(); c.paste(im, (0, 0), im)
        c.save(f'{out}/{n}.jpg', quality=85)
        print('ok', n)
