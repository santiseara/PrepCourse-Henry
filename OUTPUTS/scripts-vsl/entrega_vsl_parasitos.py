#!/usr/bin/env python3
"""Entrega del VSL de Desparasitacion Articular (AR, 2026-11-22).

Deja el master y la version web en ~/Desktop/limpia-dolor/vsl/ (regla de carpeta por oferta).
La version web sigue la receta de [[quizzes-reglas-de-armado]]: 720x1280, CRF 25, AAC 96k
y `-movflags +faststart`, que es lo que Panda Video y el hosting necesitan para ir cargando
mientras se reproduce.

  python3 entrega_vsl_parasitos.py <vsl_montado.mp4>
"""
import os, sys, subprocess, shutil

FF   = os.path.expanduser('~/bin/ffmpeg')
SRC  = os.path.abspath(sys.argv[1])
DST  = os.path.expanduser('~/Desktop/limpia-dolor/vsl')
NOM  = 'VSL-desparasitacion-articular-9-dias'
os.makedirs(DST, exist_ok=True)

master = os.path.join(DST, NOM + '.mp4')
web    = os.path.join(DST, NOM + '-web.mp4')
shutil.copy2(SRC, master)

subprocess.run([FF, '-v', 'error', '-y', '-i', master,
                '-vf', 'scale=720:1280:flags=lanczos', '-c:v', 'libx264', '-crf', '25',
                '-preset', 'slow', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '96k',
                '-ar', '48000', '-movflags', '+faststart', web], check=True)

for f in (master, web):
    print(f'{os.path.basename(f):50s} {os.path.getsize(f)/1e6:7.1f} MB')
