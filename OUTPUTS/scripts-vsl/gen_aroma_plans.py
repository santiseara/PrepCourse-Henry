# -*- coding: utf-8 -*-
"""Planes de los 6 ads de The Aromatic Plaster Atelier (mercado ingles, 2026-11-19),
clonando la edicion de Manualidades con Proposito (emprendecontusmanos.com).

Lo que se copia de ellos, medido sobre sus 7 creativos activos (22/10 al 18/11):
  - 9:16, 23 a 59 s, voz en off de mujer calida y una cama musical por debajo.
  - SIN caja de hook, SIN fichas de paso, SIN placa oscura ni boton.
  - SUBTITULOS en mayuscula, Montserrat ExtraBold ITALICA, blancos con borde negro grueso,
    2-3 palabras por renglon y hasta 3 renglones, en el tercio inferior, con la palabra que
    suena en ROSA FUCSIA (texto de color, sin caja: hibord 0).
  - La TAPA DEL EBOOK en mano sobre el b-roll, anclada a la palabra que la nombra.

Uso: python3 gen_aroma_plans.py   -> V1.json .. V6.json en anuncios/work/
"""
import os, re, sys, json

WK = os.path.expanduser('~/Desktop/aromatizadores/anuncios/work')
sys.path.insert(0, WK)
from vent_aroma import VENT

SEG = 2.9          # largo de cada tramo candidato
TOPE = 6           # maximo de recortes por clip

ROSA = '&H00BF3FFF&'     # BGR del fucsia #FF3FBF de sus subtitulos
NEGRO = '&H00000000&'

_vs = open(os.path.join(WK, 'vent_aroma.py')).read()
AUTOR = dict(re.findall(r"'(c\d+)':\s*\('(\d+)'", _vs))


def pool_y_clips():
    pool, clips = [], {}
    for k, v in VENT.items():
        vid, a, b = v[0], v[1], v[2]
        ex = v[3] if len(v) > 3 else {}
        clips[k] = dict(src=f'clips/{vid}.mp4', fam=AUTOR.get(k, vid), **ex)
        tramos, t = [], a
        while t < b - 1.6:
            tramos.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
        if len(tramos) > TOPE:
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    # la tapa del ebook entra como plano fijo, igual que ellos
    clips['tapa'] = dict(src='gfx/tapa_escena.jpg', fam='tapa', still=True)
    pool.append(['tapa', 0.0, 2.6])
    return pool, clips


VIDEOS = [
    dict(n=1, tapa=('Atelier', 0)),
    dict(n=2, tapa=('Atelier', 0)),
    dict(n=3, tapa=('Atelier', 0)),
    dict(n=4, tapa=('method', 0)),
    dict(n=5, tapa=('Atelier', 0)),
    dict(n=6, tapa=('book', 0)),
]

for v in VIDEOS:
    pool, clips = pool_y_clips()
    plan = dict(
        vo=f"voces/V{v['n']}.wav", script=f"guiones/V{v['n']}.txt", lang='en',
        speed=1.20, silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], words=4,
        music='music/bed.wav', music_db=-10,
        hi=ROSA, hibox=NEGRO, hibord=0, capy=1400, pop=False, italic=True, margin=250,
        font='Montserrat ExtraBold', fsize=76, spacing=3, outline=6, shadow=4,
        seed=v['n'] * 613, usage='usage.json',
        whoosh=[], flash=0, clips=clips, pool=pool,
        anchors=[[v['tapa'][0], v['tapa'][1], 'tapa', 0.0]], overlays=[])
    json.dump(plan, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print("V%d listo - %d tramos" % (v['n'], len(pool)))
