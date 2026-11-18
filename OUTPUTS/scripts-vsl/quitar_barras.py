#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Saca las barras blancas que HeyGen le pone a un avatar cuya foto no es 9:16
(§0d de vsl-reglas-de-armado). Mide las filas casi blancas sobre un cuadro del
medio, recorta el contenido real y lo escala a 1080x1920 centrado.

Uso: python3 quitar_barras.py entrada.mp4 [salida.mp4]
Si no hay barras no toca nada y devuelve 1.
"""
import os, subprocess, sys
import numpy as np
from PIL import Image

FF = os.path.expanduser('~/bin/ffmpeg')


def medir(ent, seg=20):
    tmp = '/tmp/_barras.png'
    subprocess.run([FF, '-v', 'error', '-y', '-ss', str(seg), '-i', ent,
                    '-frames:v', '1', tmp], check=True)
    im = np.asarray(Image.open(tmp).convert('RGB')).astype(float)
    filas = im.mean(axis=(1, 2))
    H, W = im.shape[0], im.shape[1]
    top = 0
    while top < H and filas[top] > 243:
        top += 1
    bot = H - 1
    while bot > 0 and filas[bot] > 243:
        bot -= 1
    return W, H, top, bot


if __name__ == '__main__':
    ent = sys.argv[1]
    sal = sys.argv[2] if len(sys.argv) > 2 else ent.replace('.mp4', '_sinbarras.mp4')
    W, H, top, bot = medir(ent)
    alto = bot - top + 1
    if top < 4 and bot > H - 5:
        print(f'{os.path.basename(ent)}: sin barras')
        raise SystemExit(1)
    ancho = round(1080 * 1920 / alto / 2) * 2
    x = (ancho - 1080) // 2
    vf = f'crop={W}:{alto}:0:{top},scale={ancho}:1920,crop=1080:1920:{x}:0'
    subprocess.run([FF, '-v', 'error', '-y', '-i', ent, '-vf', vf,
                    '-c:v', 'libx264', '-crf', '17', '-pix_fmt', 'yuv420p',
                    '-c:a', 'copy', sal], check=True)
    print(f'{os.path.basename(ent)}: {top} px arriba, {H-1-bot} abajo -> {os.path.basename(sal)}')
