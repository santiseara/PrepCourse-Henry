# -*- coding: utf-8 -*-
"""Planes de los 6 ads del Slime Shop Kit (habla inglesa, 2026-11-18), clonando a
Mariana Williams Creations (slimeshopkit.impultienda.ar).

Lo que se copia de ellos, medido sobre sus 17 creativos activos (31/10 al 16/11):
  - 9:16, 21 a 28 s, voz en off de mujer americana y una cama musical por debajo.
  - 100 % b-roll de slime: manos, bowls, glitter, texturas. Ni una cara hablando, ni una foto fija.
  - CAJA DE HOOK blanca redondeada arriba, texto negro bold en mayúscula, 2 renglones, y se va
    cuando termina la primera frase.
  - SUBTÍTULOS de 3 palabras abajo, mayúscula, blancos con borde fino y sombra, y la palabra que
    suena en AMARILLO (texto de color, no caja de color).
  - Sin placa final, sin chips, sin insertos de producto, sin SFX.

Uso: python3 gen_slime_plans.py   -> V1.json .. V6.json en anuncios/work/
"""
import os, re, sys, json

sys.path.insert(0, os.path.expanduser('~/Desktop/slime-shop-kit/anuncios/work'))
from vent_slime import VENT

WK = os.path.expanduser('~/Desktop/slime-shop-kit/anuncios/work')
SEG = 2.6          # largo de cada tramo candidato (sus cortes van de 1,5 a 2,5 s)
TOPE = 6           # máximo de recortes por clip (regla del pool)

AMARILLO = '&H0000D7FF&'   # BGR del amarillo de sus subtítulos (#FFD700)
NEGRO = '&H00000000&'


# familia = autor de TikTok (el comentario de cada linea de vent_slime.py). Las claves de este pool
# son todas c00..c83, asi que la regla de "no repetir fuente" no puede salir de la primera letra:
# sale de esta tabla, y asi dos planos seguidos nunca son del mismo creador.
_vs = open(os.path.join(WK, 'vent_slime.py')).read()
AUTOR = dict(re.findall(r"'(c\d+)':\s*\('\d+'.*?#\s*@?([^\s]+)", _vs))


def pool_y_clips():
    pool, clips = [], {}
    for k, v in VENT.items():
        vid, a, b = v[0], v[1], v[2]
        ex = v[3] if len(v) > 3 else {}
        clips[k] = dict(src=f'clips/{vid}.mp4', fam=AUTOR.get(k, vid), **ex)
        tramos, t = [], a
        while t < b - 1.5:
            tramos.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
        if len(tramos) > TOPE:
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    return pool, clips


# la caja de hook y hasta qué palabra dura, uno por creativo (como rotan ellos)
VIDEOS = [
    dict(n=1, hook='SLIME CAN BE YOUR NEXT LITTLE BUSINESS', until='business'),
    dict(n=2, hook='THE LITTLE BUSINESS ON YOUR KITCHEN TABLE', until='slime'),
    dict(n=3, hook='OTHER MOMS ARE ALREADY SELLING THIS', until='selling'),
    dict(n=4, hook="YOU DON'T NEED A STORE TO START", until='business.'),
    dict(n=5, hook='KIDS LOVE IT. PARENTS PAY FOR IT.', until='own,'),
    dict(n=6, hook='A HOLIDAY PROJECT YOU CAN START THIS WEEK', until='week,'),
]

for v in VIDEOS:
    pool, clips = pool_y_clips()
    plan = dict(
        vo=f"voz/V{v['n']}.wav", script=f"voz/V{v['n']}.txt", lang='en',
        speed=1.20, silence=[0.26, 0.12], cut=[1.5, 2.0, 2.5], words=3,
        music='music/bed.wav', music_db=-10,
        hook=v['hook'], hook_until=v['until'], hook_y=250, hook_size=66,
        hi=AMARILLO, hibox=NEGRO, hibord=0, capy=1500, pop=False,
        font='Montserrat ExtraBold', fsize=60, spacing=7, outline=4, shadow=3,
        seed=v['n'] * 317, usage='usage.json',
        whoosh=[], flash=0, clips=clips, pool=pool, anchors=[], overlays=[])
    json.dump(plan, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print("V%d listo · %d tramos · hook: %s" % (v['n'], len(pool), v['hook']))
