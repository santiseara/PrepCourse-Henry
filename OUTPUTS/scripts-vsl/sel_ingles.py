# -*- coding: utf-8 -*-
"""Junta las ventanas medidas y escribe seleccion.txt (id t0 t1) para el generador de planes."""
import glob, json, sys
W = sys.argv[1]
todo = {}
for p in glob.glob(W + '/ventanas*.json'):
    todo.update(json.load(open(p)))
lineas, fuera = [], []
for vid, v in sorted(todo.items(), key=lambda kv: -(kv[1].get('limpio') or 0)):
    if v.get('a') is None:
        fuera.append('%s  (%.1f s limpios)' % (vid, v.get('limpio', 0))); continue
    lineas.append('%s %.2f %.2f' % (vid, v['a'], v['b']))
open(W + '/seleccion.txt', 'w').write('\n'.join(lineas) + '\n')
print('entran %d, quedan fuera %d' % (len(lineas), len(fuera)))
for f in fuera: print('  -', f)
