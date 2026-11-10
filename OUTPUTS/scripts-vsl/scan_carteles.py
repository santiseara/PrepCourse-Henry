# -*- coding: utf-8 -*-
"""Busca texto quemado en las ventanas de un pool de clips, con OCR de Vision.

Por que existe: la hoja de contactos no muestra el cartel BLANCO sobre fondo CLARO. En la tanda 1
de The Party Box Vault (2026-11-10) pasaron el filtro visual cinco clips con leyenda del creador
("TOY STORY PARTY FAVOR BOXES", "KAWAII THEME party favor boxes", "kiddie party favor inspo",
"Hobby Lobby cardstock") y una marca de agua que duraba los 70 segundos ("Kgoodessentials").
Con OCR cuadro por cuadro aparecieron todos en una pasada.

Requiere compilar una vez:  swiftc -O ocr_vision.swift -o ocrbin
Uso: python3 scan_carteles.py <vent_X.py> <carpeta_clips> [paso_en_segundos]

Imprime, por clip, en que segundo aparece texto y cual. OJO: el texto del PRODUCTO tambien sale
(nombres, envoltorios de golosinas, marcas de herramientas). Lo que se descarta es la leyenda del
creador y el usuario/marca de agua, no la etiqueta de un Kinder.
"""
import os, subprocess, sys, collections

DIR = os.path.dirname(os.path.abspath(__file__))
FF = os.path.expanduser('~/bin/ffmpeg')
OCR = DIR + '/ocrbin'
vent_path, CL = sys.argv[1], sys.argv[2]
PASO = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0
if not os.path.exists(OCR):
    raise SystemExit('falta ocrbin: swiftc -O %s/ocr_vision.swift -o %s' % (DIR, OCR))

tmp = '/tmp/_scan_carteles'; os.makedirs(tmp, exist_ok=True)
VENT = {}
exec(open(vent_path).read())

jobs = []
for k, (fn, a, b, ex) in VENT.items():
    t = a
    while t < b:
        p = f'{tmp}/{fn}_{t:.1f}.jpg'
        if not os.path.exists(p):
            subprocess.run([FF, '-y', '-ss', str(round(t, 2)), '-i', f'{CL}/{fn}.mp4',
                            '-vf', 'scale=720:-1', '-frames:v', '1', p, '-loglevel', 'error'])
        if os.path.exists(p):
            jobs.append((k, fn, t, p))
        t += PASO

r = subprocess.run([OCR], input='\n'.join(j[3] for j in jobs) + '\n',
                   capture_output=True, text=True)
res = {}
for ln in r.stdout.splitlines():
    if '\t' in ln:
        p, txt = ln.split('\t', 1)
        res[p] = txt.strip()

by = collections.defaultdict(list)
for k, fn, t, p in jobs:
    txt = res.get(p, '')
    if txt and txt != 'ERR':
        by[(k, fn)].append((t, txt))

for (k, fn), items in sorted(by.items()):
    total = sum(1 for j in jobs if j[0] == k)
    print(f"=== {k} {fn[-5:]}  ({len(items)} cuadros con texto de {total})")
    seen = set()
    for t, txt in items:
        if txt[:40] in seen:
            continue
        seen.add(txt[:40])
        print(f"   {t:>6.1f}s  {txt[:130]}")
print('\nSIN NADA DE TEXTO:', ' '.join(k for k in VENT if (k, VENT[k][0]) not in by))
