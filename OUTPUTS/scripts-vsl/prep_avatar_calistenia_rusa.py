"""Saca las barras blancas del avatar parado de HeyGen (la foto era 3:4 y HeyGen rellenó a 9:16).
Recorta el contenido real y lo escala a 1080x1920: el Coach queda entero, solo se pierde jardín
a los costados. Uso: python3 prep_avatar_calistenia_rusa.py <entrada.mp4> <salida.mp4>
"""
import os, subprocess, sys
import numpy as np
from PIL import Image

FF = os.path.expanduser('~/bin/ffmpeg')
ent, sal = sys.argv[1], sys.argv[2]

# 1. medir las barras sobre un cuadro del medio
tmp = '/tmp/_prep_avatar.png'
subprocess.run([FF, '-v', 'error', '-y', '-ss', '3', '-i', ent, '-frames:v', '1', tmp], check=True)
filas = np.asarray(Image.open(tmp).convert('RGB')).astype(float).mean(axis=(1, 2))
H = len(filas)
top = 0
while top < H and filas[top] > 243: top += 1
bot = H - 1
while bot > 0 and filas[bot] > 243: bot -= 1
alto = bot - top + 1
if top == 0 and bot == H - 1:
    print('no hay barras blancas, no toco nada'); sys.exit(0)
print(f'barras: {top} px arriba, {H - 1 - bot} px abajo · contenido {alto} px')

# 2. recortar, escalar a lo alto y centrar
ancho = round(1080 * 1920 / alto / 2) * 2
x = (ancho - 1080) // 2
vf = f'crop=1080:{alto}:0:{top},scale={ancho}:1920,crop=1080:1920:{x}:0'
subprocess.run([FF, '-v', 'error', '-y', '-i', ent, '-vf', vf, '-c:v', 'libx264', '-crf', '17',
                '-preset', 'medium', '-pix_fmt', 'yuv420p', '-c:a', 'copy', sal], check=True)
print('listo:', sal, f'(escalado {ancho/1080:.3f}x, se recortan {x} px por lado)')
