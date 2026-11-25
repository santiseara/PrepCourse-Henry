# -*- coding: utf-8 -*-
"""Segunda pasada sobre la ventana YA aprobada, a 3 cuadros por segundo.
El filtro a 1 cuadro/s aprueba ventanas con carteles que viven entre muestra y muestra
(el "HOT DOG W/ MUSTARD $140" de una feria duraba 2 s dentro de una ventana "limpia").
Recorta la ventana al tramo limpio mas largo y tira el clip si no queda nada util.
Uso: python3 afinar.py <workdir> <worker> <nworkers>"""
import os, sys, json, glob, subprocess
WK, WI, WN = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
D = '/Users/santiagoseara/PrepCourse-Henry/OUTPUTS/scripts-vsl'
FF = os.path.expanduser('~/bin/ffmpeg')
sys.path.insert(0, WK)
from vent_laser import VENT
FPS = 3; MIN = 2.6
tmp = os.path.join(WK, '_af%d' % WI); os.system('rm -rf ' + tmp); os.makedirs(tmp)
out = {}
ks = [k for j, k in enumerate(sorted(VENT)) if j % WN == WI]
for k in ks:
    vid, a, b = VENT[k][0], VENT[k][1], VENT[k][2]
    ex = VENT[k][3] if len(VENT[k]) > 3 else {}
    for f in glob.glob(tmp + '/*.jpg'): os.remove(f)
    subprocess.run([FF, '-v', 'error', '-y', '-ss', f'{a:.2f}', '-to', f'{b:.2f}',
                    '-i', f'{WK}/clips/{vid}.mp4', '-vf', f'fps={FPS},scale=900:-2', '-q:v', '3',
                    tmp + '/g_%04d.jpg'], check=False)
    fs = sorted(glob.glob(tmp + '/g_*.jpg'))
    if not fs:
        out[k] = None; print(k, 'FUERA no se pudo leer', flush=True); continue
    o = subprocess.run([D + '/scanbin'], input='\n'.join(fs) + '\n', capture_output=True, text=True).stdout
    idx = {os.path.abspath(f): n for n, f in enumerate(fs)}
    sucio = [True] * len(fs); textos = set()
    for ln in o.strip().split('\n'):
        p = ln.split('\t')
        if len(p) < 3 or p[1] == 'ERR': continue
        n = idx.get(os.path.abspath(p[0]))
        if n is None: continue
        ts = [t.strip() for t in p[2].split('||') if len(t.strip()) >= 3]
        caras = int(p[1][6:]) if p[1].startswith('FACES=') else 0
        for t in ts: textos.add(t[:40])
        sucio[n] = bool(ts) or caras > 0
    mejor = (0, 0, 0); j = 0
    while j < len(sucio):
        if sucio[j]: j += 1; continue
        m = j
        while m < len(sucio) and not sucio[m]: m += 1
        if m - j > mejor[0]: mejor = (m - j, j, m)
        j = m
    n, i0, i1 = mejor
    ini = a + i0 / FPS + 0.15
    fin = a + i1 / FPS - 0.15
    if fin - ini < MIN:
        out[k] = None
        print(k, vid, 'FUERA queda %.1f s (%d/%d sucios): %s' % (max(fin-ini,0), sum(sucio), len(sucio), ' | '.join(list(textos)[:2])), flush=True)
    else:
        out[k] = [vid, round(ini, 2), round(fin, 2), ex]
        marca = '' if fin-ini >= (b-a) - 0.4 else ' (recortada de %.1f a %.1f s)' % (b-a, fin-ini)
        print(k, vid, 'OK %.2f-%.2f%s' % (ini, fin, marca), flush=True)
json.dump(out, open(f'{WK}/afin{WI}.json', 'w'))
print('FIN', WI)
