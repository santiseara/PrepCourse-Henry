# -*- coding: utf-8 -*-
"""Recomprime los mp4 para que entren por el conector de Drive.
18/11/2026: el tope de 10 MB del conector es del PAYLOAD, y el payload va en base64,
que infla 4/3. O sea el archivo no puede pasar de ~7,3 MB. Objetivo 6,8 MB.
x264 en dos pasadas, preset veryslow, audio AAC 128k. Uso: python3 comprimir_drive.py <carpeta_in> <carpeta_out>"""
import os, re, subprocess, sys
FF = os.path.expanduser('~/bin/ffmpeg')
SRC, DST = sys.argv[1], sys.argv[2]
os.makedirs(DST, exist_ok=True)
OBJ_MB = 5.2   # 20/11/2026: a 6,8 (archivo de 7,15 MB) el conector devuelve EPROTO; a 5,5 entra

def dur(f):
    r = subprocess.run([FF, '-i', f], capture_output=True, text=True).stderr
    m = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r)
    h, mi, s = m.groups()
    return int(h)*3600 + int(mi)*60 + float(s)

for f in sorted(os.listdir(SRC)):
    if not f.endswith('.mp4'):
        continue
    ent, sal = os.path.join(SRC, f), os.path.join(DST, f)
    if os.path.exists(sal) and os.path.getsize(sal) < 7.2e6:
        print('ya esta', f); continue
    D = dur(ent)
    br = int((OBJ_MB * 8192) / D - 130)
    log = os.path.join(DST, '_2pass')
    base = [FF, '-v', 'error', '-y', '-i', ent, '-c:v', 'libx264', '-preset', 'veryslow',
            '-b:v', f'{br}k', '-pix_fmt', 'yuv420p', '-passlogfile', log]
    subprocess.run(base + ['-pass', '1', '-an', '-f', 'mp4', '/dev/null'], check=True)
    subprocess.run(base + ['-pass', '2', '-c:a', 'aac', '-b:a', '128k', '-ar', '48000',
                           '-ac', '2', '-movflags', '+faststart', sal], check=True)
    mb = os.path.getsize(sal) / 1e6
    print(f'{f}  {D:.1f}s  {br} kbps  ->  {mb:.2f} MB', flush=True)
for x in os.listdir(DST):
    if x.startswith('_2pass'):
        os.remove(os.path.join(DST, x))
print('LISTO')
