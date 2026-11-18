#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gráficos de los dos formatos nuevos de Fausto Almeida (medidos el 18/11/2026):

  · "¿ESTO O ESTO?" (su creativo de 0:51, 11 anuncios estrenados el 18/11)
      pantalla partida comida arriba / comida abajo, cartel blanco con el nombre,
      cruz roja o tilde verde, marco verde en la que gana y el avatar recortado adelante.

  · "EL SHOT" (su creativo de 0:24, 10 anuncios desde el 16/11)
      placa negra de tres líneas fija arriba (blanca / amarilla / blanca),
      subtítulo en mayúsculas con la palabra clave en amarillo y botón amarillo al final.

Todas las medidas salen de los cuadros de sus videos, escaladas de 360x640 a 1080x1920.
"""
import os, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gfx_fausto as G

W, H, FPS = 1080, 1920, 30
SCR = G.SCR
FF = os.path.expanduser('~/bin/ffmpeg')

# --- geometría de "¿ESTO O ESTO?" (de su cuadro a los 9,0 s) -----------------
PA_Y, PA_H = 280, 644            # panel de arriba
PB_X, PB_Y = 16, 974             # panel de abajo
PB_W, PB_H = 1048, 666
BORDE = 8                        # marco verde de la que gana
CHIP_H, CHIP_TS = 66, 34
MARCA_D = 72

VERDE = '0x22C55E'
ROJO = '0xDC2626'
AMAR = '0xFFD400'


def _f():
    return G.fuente()


def esc(t):
    return G.esc(t)


# ---------------------------------------------------------------------------
def marcas_png():
    """Dibuja una vez la cruz roja y el tilde verde (PNG con alfa)."""
    from PIL import Image, ImageDraw
    d = f'{SCR}/eslo'
    os.makedirs(d, exist_ok=True)
    sal = {}
    for nom, col, tipo in (('cruz', (220, 38, 38), 'x'), ('tilde', (34, 197, 94), 'v')):
        p = f'{d}/{nom}.png'
        sal[nom] = p
        if os.path.exists(p):
            continue
        S = MARCA_D * 4                       # se dibuja grande y se achica: bordes limpios
        im = Image.new('RGBA', (S, S), (0, 0, 0, 0))
        dr = ImageDraw.Draw(im)
        dr.ellipse([0, 0, S - 1, S - 1], fill=col + (255,))
        gr = int(S * 0.10)
        if tipo == 'x':
            a, b = int(S * 0.30), int(S * 0.70)
            dr.line([a, a, b, b], fill=(255, 255, 255, 255), width=gr)
            dr.line([a, b, b, a], fill=(255, 255, 255, 255), width=gr)
        else:
            dr.line([int(S*0.26), int(S*0.52), int(S*0.44), int(S*0.70)],
                    fill=(255, 255, 255, 255), width=gr)
            dr.line([int(S*0.44), int(S*0.70), int(S*0.76), int(S*0.32)],
                    fill=(255, 255, 255, 255), width=gr)
        im.resize((MARCA_D, MARCA_D), Image.LANCZOS).save(p)
    return sal


def boton_amarillo_png(texto='MIRÁ EL PASO A PASO'):
    """Pastilla amarilla con chevrones a los costados (el cierre de su 0:24)."""
    from PIL import Image, ImageDraw, ImageFont
    d = f'{SCR}/eslo'
    os.makedirs(d, exist_ok=True)
    p = f'{d}/boton_{abs(hash(texto)) % 99999}.png'
    if os.path.exists(p):
        return p
    fnt = ImageFont.truetype(G.fuente(), 56)
    im = Image.new('RGBA', (W, 220), (0, 0, 0, 0))
    dr = ImageDraw.Draw(im)
    tw = dr.textlength(texto, font=fnt)
    bw, bh = int(tw + 110), 104
    bx, by = (W - bw) // 2, 58
    dr.rounded_rectangle([bx, by, bx + bw, by + bh], radius=bh // 2, fill=(255, 212, 0, 255))
    dr.text((bx + (bw - tw) / 2, by + 20), texto, font=fnt, fill=(17, 17, 17, 255))
    # chevrones amarillos a los dos lados, tres por lado
    for lado in (0, 1):
        cx = 72 if lado == 0 else W - 72
        for k in range(3):
            cy = 52 + k * 58
            dr.line([cx - 34, cy, cx, cy + 30], fill=(255, 212, 0, 255), width=13)
            dr.line([cx, cy + 30, cx + 34, cy], fill=(255, 212, 0, 255), width=13)
    im.save(p)
    return p


# ---------------------------------------------------------------------------
def titulo_eso(l1, l2, ini, fin):
    """El título de apertura: '¿ESTO O ESTO?' y abajo la aclaración."""
    f = _f()
    return ','.join([
        f"drawtext=fontfile='{f}':text='{esc(l1)}':fontcolor=white:fontsize=84:"
        f"borderw=8:bordercolor=black:x=(w-text_w)/2:y=370:{G.entre(ini, fin)}",
        f"drawtext=fontfile='{f}':text='{esc(l2)}':fontcolor=white:fontsize=46:"
        f"borderw=6:bordercolor=black:x=(w-text_w)/2:y=482:{G.entre(ini, fin)}",
    ])


def chip(texto, x, y, ini, fin):
    """Cartel blanco con el nombre de la comida, en negro y mayúsculas."""
    f = _f()
    return (f"drawtext=fontfile='{f}':text='{esc(texto.upper())}':fontcolor=0x111111:"
            f"fontsize={CHIP_TS}:box=1:boxcolor=white@0.96:boxborderw=16:"
            f"x={x}:y={y}:{G.entre(ini, fin)}")


def letra_o(ini, fin):
    f = _f()
    return (f"drawtext=fontfile='{f}':text='o':fontcolor=white:fontsize=40:borderw=5:"
            f"bordercolor=black:x=(w-text_w)/2:y={PA_Y + PA_H + 6}:{G.entre(ini, fin)}")


def placa_tres(l1, l2, l3, alto=270):
    """La placa negra fija de arriba del 0:24: blanca / amarilla / blanca."""
    f = _f()
    p = [f"drawbox=x=0:y=0:w={W}:h={alto}:color=black@0.88:t=fill"]
    for i, (txt, col, ts) in enumerate(((l1, 'white', 46), (l2, '0xFFD400', 50), (l3, 'white', 46))):
        p.append(f"drawtext=fontfile='{f}':text='{esc(txt.upper())}':fontcolor={col}:"
                 f"fontsize={ts}:x=(w-text_w)/2:y={26 + i * 74}")
    return ','.join(p)


# ---------------------------------------------------------------------------
def subtitulos_amarillo(palabras, out, por_vez=3, clave=None, y=1020, ts=78, mayus=False):
    """Subtítulo blanco con borde negro y la palabra clave en AMARILLO (su estilo nuevo)."""
    clave = {G.sinac(k).lower() for k in (clave or [])}
    fn = 'Anton' if os.path.exists(G.ANTON) else 'Arial'
    mv = max(10, H - y)
    est = (f'Style: D,{fn},{ts},&H00FFFFFF,&H00000000,&H00000000,&H90000000,-1,0,0,0,'
           f'100,100,0,0,1,5,3,2,60,60,{mv},1')
    cab = ('[Script Info]\nScriptType: v4.00+\n'
           f'PlayResX: {W}\nPlayResY: {H}\nWrapStyle: 2\n\n'
           '[V4+ Styles]\nFormat: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,'
           'OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,'
           'Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding\n'
           + est + '\n\n[Events]\nFormat: Layer,Start,End,Style,Name,MarginL,MarginR,'
           'MarginV,Effect,Text\n')
    ev = []
    grupos = [palabras[i:i + por_vez] for i in range(0, len(palabras), por_vez)]
    for gi, gr in enumerate(grupos):
        ini, fin = gr[0][0], gr[-1][1] + 0.08
        # que no se pisen dos carteles: el de atrás corta donde arranca el siguiente
        if gi + 1 < len(grupos):
            fin = min(fin, grupos[gi + 1][0][0] - 0.01)
        if fin <= ini:
            fin = ini + 0.12
        trozos = []
        for _, _, w in gr:
            lw = G.sinac(w).lower().strip('.,¿?¡!:;')
            t = w.upper() if mayus else w
            trozos.append(r'{\c&H00D4FF&}' + t + r'{\c&HFFFFFF&}' if lw in clave else t)
        ev.append(f'Dialogue: 0,{G.ass_t(ini)},{G.ass_t(fin)},D,,0,0,0,,' + ' '.join(trozos))
    open(out, 'w').write(cab + '\n'.join(ev) + '\n')
    return out


if __name__ == '__main__':
    print('modulo de graficos de los formatos nuevos — no se corre solo')
    marcas_png(); print(boton_amarillo_png())
