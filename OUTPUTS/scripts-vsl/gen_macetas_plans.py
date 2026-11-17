# -*- coding: utf-8 -*-
"""Planes de los 6 ads de Macetas de Cemento (AR, 2026-11-17), clonando a Aula Digital 360.

Lo que se copia de ellos, medido sobre 10 de sus 58 ads:
  - 9:16, 30-55 s, voz en off de mujer y una cama musical por debajo (no tienen un solo silencio).
  - Chips fijos arriba a la izquierda durante todo el video, en tres juegos que rotan por creativo.
  - Subtítulos de 3-4 palabras, mayúscula, blancos con borde negro grueso y la palabra que suena
    adentro de una caja ROJA o VERDE. El color cambia por creativo, igual que ellos.
  - Sin caja de hook, sin placa final, sin insertos del producto: el video es 100 % b-roll.

Uso: python3 gen_macetas_plans.py   -> V1.json .. V6.json en anuncios/work/
"""
import os, sys, json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vent_macetas import VENT

WK = os.path.expanduser('~/Desktop/macetas-cemento/anuncios/work')
SEG = 3.4          # largo de cada tramo candidato
TOPE = 8           # máximo de recortes por clip (regla del pool)

ROJO = '&H002020D6&'      # BGR del rojo de sus cajas (#D62020)
VERDE = '&H0040C522&'     # BGR del verde (#22C540)
BLANCO = '&H00FFFFFF&'


def pool_y_clips():
    pool, clips = [], {}
    for k, v in VENT.items():
        vid, a, b = v[0], v[1], v[2]
        ex = v[3] if len(v) > 3 else {}
        clips[k] = dict(src=f'tiktoks/{vid}.mp4', fam=vid, **ex)
        tramos, t = [], a
        while t < b - 1.8:
            tramos.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
        if len(tramos) > TOPE:
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    return pool, clips


# un juego de chips y un color de caja por creativo, como rota Aula Digital
VIDEOS = [
    dict(n=1, chips='C', hibox=ROJO,  hibox2=VERDE, first=['ali', 0.3]),
    dict(n=2, chips='B', hibox=VERDE, hibox2=ROJO,  first=['alt', 0.3]),
    dict(n=3, chips='A', hibox=ROJO,  hibox2=VERDE, first=['fab', 0.3]),
    dict(n=4, chips='B', hibox=VERDE, hibox2=ROJO,  first=['tel', 0.5]),
    dict(n=5, chips='C', hibox=ROJO,  hibox2=VERDE, first=['bow', 0.3]),
    dict(n=6, chips='A', hibox=VERDE, hibox2=ROJO,  first=['fib', 5.0]),
]

for v in VIDEOS:
    pool, clips = pool_y_clips()
    plan = dict(
        vo=f"vo/V{v['n']}.wav", script=f"vo/V{v['n']}.txt", lang='es',
        speed=1.20, silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], words=3,
        music='music/bed.wav', music_db=-9,
        hi=BLANCO, hibox=v['hibox'], hibox2=v['hibox2'], hibord=20, capy=1180,
        fixed=[f"gfx/chips_{v['chips']}.png"],
        first=v['first'], seed=v['n'] * 317, usage='usage.json',
        whoosh=[], clips=clips, pool=pool, anchors=[], overlays=[])
    json.dump(plan, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print("V%d listo · %d tramos · chips %s" % (v['n'], len(pool), v['chips']))
