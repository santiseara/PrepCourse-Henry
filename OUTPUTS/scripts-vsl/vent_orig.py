# -*- coding: utf-8 -*-
"""Ventanas usables de los creativos ORIGINALES de Fluente com Legenda.

Se mira el cuadro YA RECORTADO arriba del watermark (crop=576:1024:72:0 sobre 720x1280,
regla del 22/11), que es lo que se va a ver en el ad. Se cae el tramo que tiene CARA
(la presentadora de 2 o 3 de sus creativos) y el que tiene una CAPTURA DE PANTALLA del
area de miembros (se detecta por el titulo en portugues "Ingles Nivel" / "Modulo").
Se devuelven TODOS los tramos limpios de 2,5 s o mas.

Uso: python3 vent_orig.py <workdir> [parte] [de]
"""
import os, re, sys, glob, json, subprocess, collections
W = sys.argv[1]
PARTE = int(sys.argv[2]) if len(sys.argv) > 2 else 0
DE = int(sys.argv[3]) if len(sys.argv) > 3 else 1
S = os.path.dirname(os.path.abspath(__file__))
FF = os.path.expanduser('~/bin/ffmpeg')
SCAN = S + '/scanbin2'
CROP = 'crop=576:1024:72:0'
FPS = 2
MIN = 2.5
MALAS = ('nivel a1', 'nivel a2', 'nivel b1', 'nivel b2', 'nivel c1', 'nivel c2',
         'modulo', 'módulo', 'area de membros', 'área de membros', 'bem-vindo', 'bem vindo',
         'aulas', 'login', 'acesso', 'fluente com legenda', 'curso')
tmp = W + '/_vo%d' % PARTE; os.makedirs(tmp, exist_ok=True)

def dur(p):
    r = subprocess.run([FF, '-i', p], capture_output=True, text=True).stderr
    m = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r)
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3)) if m else 0.0

res = {}
clips = sorted(glob.glob(W + '/orig/*.mp4'))[PARTE::DE]
for i, p in enumerate(clips, 1):
    vid = os.path.basename(p)[:-4]
    D = dur(p)
    for f in glob.glob(tmp + '/*.jpg'): os.remove(f)
    subprocess.run([FF, '-v', 'error', '-y', '-i', p, '-vf', '%s,fps=%d,scale=576:-2' % (CROP, FPS),
                    tmp + '/f_%04d.jpg'], check=False)
    frames = sorted(glob.glob(tmp + '/f_*.jpg'))
    if not frames:
        res[vid] = dict(dur=D, ventanas=[], nota='sin cuadros'); continue
    o = subprocess.run([SCAN], input='\n'.join(frames) + '\n', capture_output=True,
                       text=True, timeout=1200).stdout
    sucio, textos = {}, collections.defaultdict(set)
    for ln in o.strip().split('\n'):
        pr = ln.split('\t')
        if len(pr) < 3 or pr[1] == 'ERR': continue
        k = int(re.search(r'f_(\d+)\.jpg', pr[0]).group(1)) - 1
        mal = pr[1].startswith('FACES=') and int(pr[1][6:]) > 0
        for t in pr[2].split('||'):
            c = t.lstrip('|').split(';')      # un texto que termina en '|' parte mal el separador
            if len(c) < 4: continue
            try:
                alto = float(c[0])
            except ValueError:
                continue
            txt = ';'.join(c[3:]).lower()
            if any(w in txt for w in MALAS): mal = True
            if txt and alto > 0.02:
                textos[k].add(';'.join(c[3:])[:40])
        sucio[k] = mal
    n = len(frames)
    ventanas, ini = [], None
    for k in range(n + 1):
        if k < n and not sucio.get(k, False):
            if ini is None: ini = k
        else:
            if ini is not None:
                a, b = ini / FPS, k / FPS
                if b - a >= MIN:
                    tx = set()
                    for kk in range(ini, k): tx |= textos.get(kk, set())
                    ventanas.append([round(a + 0.2, 2), round(min(b - 0.2, D - 0.2), 2),
                                     sorted(tx)[:14]])
                ini = None
    res[vid] = dict(dur=round(D, 1), ventanas=ventanas,
                    limpio=round(sum(v[1] - v[0] for v in ventanas), 1))
    print(vid, res[vid]['limpio'], 's limpios en', len(ventanas), 'tramos', flush=True)
json.dump(res, open(W + '/vent_orig%d.json' % PARTE, 'w'), indent=1)
