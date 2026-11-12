# -*- coding: utf-8 -*-
"""Planes de las 3 renovaciones de piedras para Brasil (2026-11-11).

No se bajo un solo clip nuevo: el pool sale del material de piedras que ya teniamos.
  - o1..o7: los mismos ads que ya corren en portugues (BR1..BR7), que son 100 % b-roll de piedras.
    Todos tienen subtitulos quemados en ingles, asi que cada clip entra con un ZOOM calculado para
    que la franja del subtitulo quede fuera del encuadre (ybias 0 = recorte desde arriba).
    El tope de cada zoom se midio mirando un cuadro grande de cada clip:
      o1 texto arriba de 0.655 -> 1.60 · o2 pildora 0.72 -> 1.45 · o3 0.61 -> 1.70 · o4 0.645 -> 1.60
      o5 0.72 -> 1.45 · o6 0.615 -> 1.70 · o7 pildora 0.70 -> 1.50
    o8 ("I used to…") queda VETADO: su pildora arranca en 0.48 y haria falta un zoom 2.1.
  - b*: los 6 B-rolls limpios de work/brolls (720x1280, sin una letra). 'crafting' lleva zoom 1.35
    porque la bolsa dice "Pour Stone Plaster" en ingles en la mitad de abajo.

Uso: python3 gen_pedras_ren_plans.py   -> escribe R1.json R2.json R3.json en work/ren11/
"""
import os, json

WK = os.path.expanduser('~/Desktop/scented-stones-ad/anuncios/portugues/work/ren11')
BR = os.path.expanduser('~/Desktop/scented-stones-ad/work/brolls')
SEG = 2.4
TOPE = 6

#  clave -> (archivo, desde, hasta, extras).  Las ventanas salen del OCR de Vision sobre el
#  ENCUADRE FINAL (scan del 11/11, 1 cuadro por segundo): se cayeron los tramos con la tarjeta
#  "Piedra difusora" EN ESPANOL (clips b y g, 8-9 s, 26 s y 32 s), el cartel "STORYTIME!" de los
#  primeros 5 s del cuarto ad, la etiqueta "Pure palette" (d 11 s, e 6 s), la bolsa "Pour Stone
#  Plaster" del broll de IA (m, 0-2 s) y el jarro Pyrex (j, 3 s). 🆕 A 'm' se le corta tambien la
#  cola: a partir de 6 s la feria tiene un BILLETE DE DOLAR apoyado en el cajon, que en un ad
#  brasileno esta mal. El OCR no lo ve (no es texto legible): aparecio en la hoja del render.
VENT = {
    'a':  ('src/o1.mp4', 0.0, 40.0, {'zoom': 1.60, 'ybias': 0.0, 'fam': 'tabla'}),
    'b':  ('src/o2.mp4', 12.0, 24.5, {'zoom': 1.45, 'ybias': 0.0, 'fam': 'proceso'}),
    'b2': ('src/o2.mp4', 35.0, 43.5, {'zoom': 1.45, 'ybias': 0.0, 'fam': 'proceso'}),
    'b3': ('src/o2.mp4', 0.0, 7.0, {'zoom': 1.45, 'ybias': 0.0, 'fam': 'proceso'}),
    'c':  ('src/o3.mp4', 0.0, 42.0, {'zoom': 1.70, 'ybias': 0.0, 'fam': 'mesa'}),
    'd':  ('src/o4.mp4', 12.5, 62.5, {'zoom': 1.60, 'ybias': 0.0, 'fam': 'manos'}),
    'd2': ('src/o4.mp4', 5.5, 9.8, {'zoom': 1.60, 'ybias': 0.0, 'fam': 'manos'}),
    'e':  ('src/o5.mp4', 7.5, 20.3, {'zoom': 1.45, 'ybias': 0.0, 'fam': 'lazo'}),
    'e2': ('src/o5.mp4', 0.0, 4.8, {'zoom': 1.45, 'ybias': 0.0, 'fam': 'lazo'}),
    'f':  ('src/o6.MOV', 0.0, 57.8, {'zoom': 1.70, 'ybias': 0.0, 'fam': 'macrame'}),
    'g':  ('src/o7.mp4', 12.0, 25.0, {'zoom': 1.50, 'ybias': 0.0, 'fam': 'cajon'}),
    'g2': ('src/o7.mp4', 35.0, 44.0, {'zoom': 1.50, 'ybias': 0.0, 'fam': 'cajon'}),
    'g3': ('src/o7.mp4', 0.0, 7.0, {'zoom': 1.50, 'ybias': 0.0, 'fam': 'cajon'}),
    'h':  (BR + '/assembling.mp4', 0.0, 4.2, {'fam': 'ia1'}),
    'h2': (BR + '/assembling.mp4', 6.2, 7.8, {'fam': 'ia1'}),
    'i':  (BR + '/making.mp4', 0.0, 7.8, {'fam': 'ia2'}),
    'j':  (BR + '/stirring.mp4', 4.2, 7.8, {'fam': 'ia3'}),
    'k':  (BR + '/unpacking.mp4', 0.0, 7.8, {'fam': 'ia4'}),
    'l':  (BR + '/wedding.mp4', 0.0, 7.8, {'fam': 'ia5'}),
    'm':  (BR + '/crafting.mp4', 2.2, 5.5, {'zoom': 1.35, 'ybias': 0.0, 'fam': 'ia6'}),
}
TODOS = list(VENT.keys())

AMARILLO = '&H0000E8FF&'   # #FFE800 en BGR: la palabra activa, como en el ad de 58 anos


def pool_y_clips(claves, off=0.0):
    pool, clips = [], {}
    for k in claves:
        fn, a, b, ex = VENT[k]
        d = dict(src=fn); d.update(ex)
        clips[k] = d
        tramos, t = [], a + (off if b - a > off + SEG + 1.6 else 0)
        while t < b - 1.2:
            tramos.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
        if len(tramos) > TOPE:
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    return pool, clips


VIDEOS = [
    dict(n=1, seed=1111, off=0.0),
    dict(n=2, seed=2222, off=1.1),
    dict(n=3, seed=3333, off=2.0),
]

for v in VIDEOS:
    pool, clips = pool_y_clips(TODOS, v['off'])
    plan = dict(
        vo='vo/R%d.wav' % v['n'], script='vo/r%d.txt' % v['n'], lang='pt',
        speed=1.30, cut=[1.9, 2.4, 2.9],
        music='music/bed_piedras.wav', music_db=-21,
        hi=AMARILLO, capy=1380,
        seed=v['seed'], usage='usage.json',
        clips=clips, pool=pool, anchors=[], whoosh=[],
    )
    json.dump(plan, open(os.path.join(WK, 'R%d.json' % v['n']), 'w'), indent=1)
    print('R%d  %d tramos  %d clips' % (v['n'], len(pool), len(clips)))
