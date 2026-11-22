# -*- coding: utf-8 -*-
"""Marca las ventanas que tienen el SUBTITULO QUEMADO EN PORTUGUES de ellos.

Sus creativos llevan su propio subtitulo blanco en el tercio de abajo, justo donde va el nuestro.
El recorte del watermark (zoom 1.25) no lo saca. Se mira SOLO la franja de abajo del cuadro ya
recortado y se mide el alto del renglon: el subtitulo de ellos es grande (>9 % de la franja),
lo impreso en la hoja es chico.

Uso: python3 subs_quemados.py <workdir> [parte] [de]
"""
import os, sys, json, glob, subprocess
W = sys.argv[1]
PARTE = int(sys.argv[2]) if len(sys.argv) > 2 else 0
DE = int(sys.argv[3]) if len(sys.argv) > 3 else 1
S = os.path.dirname(os.path.abspath(__file__))
FF = os.path.expanduser('~/bin/ffmpeg')
SCAN = S + '/scanbin2'
# franja de abajo del cuadro recortado (576x1024 arranca en y=0 del original 720x1280)
# franja de abajo (su subtitulo) y de arriba (sus stickers de comentario/pregunta)
FRANJAS = [('abajo', 'crop=576:300:72:700'), ('arriba', 'crop=576:300:72:30')]
ALTO = 0.09
tmp = W + '/_sq%d' % PARTE; os.makedirs(tmp, exist_ok=True)

filas = json.load(open(W + '/indice_ventanas.json'))
res = {}
for i, (vid, a, b) in enumerate(filas):
    if i % DE != PARTE: continue
    p = '%s/orig/%s.mp4' % (W, vid)
    sucia, muestras = False, []
    for k in (0.15, 0.45, 0.78):
        t = a + (b - a) * k
        for nombre, franja in FRANJAS:
            f = '%s/s.jpg' % tmp
            subprocess.run([FF, '-v', 'error', '-y', '-ss', '%.2f' % t, '-i', p, '-vframes', '1',
                            '-vf', franja + ',scale=576:-2', f], check=False)
            if not os.path.exists(f): continue
            o = subprocess.run([SCAN], input=f + '\n', capture_output=True, text=True, timeout=120).stdout
            os.remove(f)
            for ln in o.strip().split('\n'):
                pr = ln.split('\t')
                if len(pr) < 3: continue
                for tx in pr[2].split('||'):
                    c = tx.lstrip('|').split(';')
                    if len(c) < 4: continue
                    try: alto = float(c[0])
                    except ValueError: continue
                    if alto > ALTO:
                        sucia = True; muestras.append(nombre + ':' + ';'.join(c[3:])[:30])
    res[str(i)] = dict(vid=vid, a=a, b=b, sucia=sucia, textos=muestras[:3])
    print(i, vid, 'SUCIA' if sucia else 'ok', ' | '.join(muestras[:2]), flush=True)
json.dump(res, open(W + '/subs_quemados%d.json' % PARTE, 'w'), ensure_ascii=False, indent=1)
