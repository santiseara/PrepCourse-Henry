# -*- coding: utf-8 -*-
"""Junta los ventanasN.json de los workers y escribe <workdir>/vent_<nombre>.py con
VENT = {'cNN': ('<id>', ini, fin), ...}, ordenado por largo de ventana limpia.
Uso: python3 vent_a_py.py <workdir> <nombre> [max_clips]"""
import glob, json, os, sys
W, NOM = sys.argv[1], sys.argv[2]
TOPE = int(sys.argv[3]) if len(sys.argv) > 3 else 999
res = {}
for f in sorted(glob.glob(os.path.join(W, 'ventanas*.json'))):
    res.update(json.load(open(f)))
buenos = [(k, v) for k, v in res.items() if v.get('ok')]
buenos.sort(key=lambda kv: -(kv[1]['fin'] - kv[1]['ini']))
buenos = buenos[:TOPE]
out = ['# generado por vent_a_py.py: ventana limpia de cada clip del pool',
       'VENT = {']
for i, (vid, v) in enumerate(buenos):
    out.append("    'c%02d': ('%s', %.2f, %.2f)," % (i, vid, v['ini'], v['fin']))
out.append('}')
open(os.path.join(W, 'vent_%s.py' % NOM), 'w').write('\n'.join(out) + '\n')
print('%d clips con ventana limpia de %d analizados -> vent_%s.py' % (len(buenos), len(res), NOM))
