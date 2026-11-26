# -*- coding: utf-8 -*-
"""Recomprime los mp4 para que entren por el conector de Drive, RAPIDO.

26/11/2026: `comprimir_drive.py` usa `-preset veryslow` y tarda MAS DE UNA HORA por video a
1080x1920. Con `-preset medium` y las mismas dos pasadas, los 6 de Puertas de ACM salieron en
60 segundos EN TOTAL y al mismo tamano: a ~1,2 Mbps lo que manda es el objetivo de tamano, no el
preset. Este es el que hay que usar; el otro queda solo como referencia.

Uso: python3 comprimir_drive_rapido.py <carpeta_in> <carpeta_out>"""
import os, re, subprocess, sys
FF = os.path.expanduser('~/bin/ffmpeg')
SRC, DST = sys.argv[1], sys.argv[2]
os.makedirs(DST, exist_ok=True)
OBJ_MB = 5.2   # 20/11/2026: a 6,8 (archivo de 7,15 MB) el conector devuelve EPROTO; a 5,5 entra

def dur(f):
    r = subprocess.run([FF, '-i', f], capture_output=True, text=True).stderr
    h, mi, s = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r).groups()
    return int(h) * 3600 + int(mi) * 60 + float(s)

for f in sorted(os.listdir(SRC)):
    if not f.endswith('.mp4'):
        continue
    ent, sal = os.path.join(SRC, f), os.path.join(DST, f)
    if os.path.exists(sal) and os.path.getsize(sal) < 7.2e6:
        print('ya esta', f); continue
    D = dur(ent)
    br = int((OBJ_MB * 8192) / D - 130)
    log = os.path.join(DST, '_2pass')
    base = [FF, '-v', 'error', '-y', '-i', ent, '-c:v', 'libx264', '-preset', 'medium',
            '-b:v', f'{br}k', '-pix_fmt', 'yuv420p', '-passlogfile', log]
    subprocess.run(base + ['-pass', '1', '-an', '-f', 'mp4', '/dev/null'], check=True)
    subprocess.run(base + ['-pass', '2', '-c:a', 'aac', '-b:a', '128k', '-ar', '48000',
                           '-ac', '2', '-movflags', '+faststart', sal], check=True)
    print(f'{f}  {D:.1f}s  {br} kbps  ->  {os.path.getsize(sal) / 1e6:.2f} MB', flush=True)
for x in os.listdir(DST):
    if x.startswith('_2pass'):
        os.remove(os.path.join(DST, x))
print('LISTO')
