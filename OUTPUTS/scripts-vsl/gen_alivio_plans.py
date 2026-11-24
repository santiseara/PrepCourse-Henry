# -*- coding: utf-8 -*-
"""Planes de los 6 ads de Alivio en Cada Plato (LATAM neutro, 2026-11-23),
clonando la edicion de הקלה בכל צלחת (hakala-bechol-tzalachat.impultienda.ar).

Medido sobre 10 de sus 32 ads activos (bajados y transcriptos el 23/11) y 3 hojas de contactos:
  - 9:16, 58 a 110 s (la mayoria 70-78), voz en off de mujer y cama musical por debajo.
  - 100 % b-roll de comida casera, CERO caras, cortes de ~2 s.
  - CAJA DE HOOK ROJA chica arriba los primeros segundos.
  - SUBTITULOS en mayuscula, blancos con borde negro, 4 palabras, con la palabra que suena
    en color: UN color por creativo (magenta, celeste, lima).
  - UN solo insert del producto (la tapa apoyada en la mesa) anclado a "Alivio".
  - CHIP ROJO de descuento cerca del final, en 3 de los 6 (como ellos).
  - Sin placa de cierre y sin boton: termina en el b-roll.

Uso: python3 gen_alivio_plans.py <workdir>
"""
import os, re, sys, json

WK = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser('~/Desktop/alivio-en-cada-plato/anuncios/work')
sys.path.insert(0, WK)
from vent_alivio import VENT

SEG = 2.3          # largo de cada tramo candidato
TOPE = 8           # maximo de recortes por clip (subido el 23/11: tras recortar ventanas el pool queda chico)

MAGENTA = '&H008C19E6&'    # #E6198C
CELESTE = '&H00E6B419&'    # #19B4E6
LIMA    = '&H001AFF7C&'    # #7CFF1A
NEGRO   = '&H00000000&'

AUTOR = {}
_fa = os.path.join(WK, 'autores.json')
if os.path.exists(_fa):
    AUTOR = json.load(open(_fa))


def pool_y_clips():
    pool, clips = [], {}
    for k, v in VENT.items():
        vid, a, b = v[0], v[1], v[2]
        ex = v[3] if len(v) > 3 else {}
        clips[k] = dict(src=f'clips/{vid}.mp4', fam=AUTOR.get(vid, vid), **ex)
        tramos, t = [], a
        while t < b - 1.2:
            tramos.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
        if len(tramos) > TOPE:
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    # el unico insert: la tapa del libro apoyada en la mesa (foto fija, anclada a "Alivio")
    clips['tapa'] = dict(src='gfx/tapa.png', still=True, fam='tapa')
    pool.append(['tapa', 0.0, 3.0])
    return pool, clips


CHIP = 'DESCUENTO POR TIEMPO LIMITADO'

VIDEOS = [
    dict(n=1, hi=MAGENTA, hook='NO SOY CHISMOSA|PERO EL MARTES LA VI', hasta=('mirar', 0), chip=None),
    dict(n=2, hi=CELESTE, hook='EL MÉDICO MIRÓ|Y ME DIJO UNA SOLA COSA', hasta=('nada', 0), chip=('descuento', 0)),
    dict(n=3, hi=LIMA,    hook='MI JEFA ME PARÓ|EN EL PASILLO', hasta=('cocinaste', 0), chip=None),
    dict(n=4, hi=MAGENTA, hook='COMO SI ME HUBIERAN|DADO UN AUMENTO', hasta=('nadie', 0), chip=('botón', 0)),
    dict(n=5, hi=CELESTE, hook='EN EL GRUPO DE WHATSAPP|YO ERA EL CHISTE', hasta=('vez', 0), chip=None),
    dict(n=6, hi=LIMA,    hook='LOS DOMINGOS EN LA NOCHE|ME AGARRABA UNA ANGUSTIA', hasta=('comer', 0), chip=('descuento', 0)),
]

PRIMEROS = json.load(open(os.path.join(WK, 'primeros.json'))) if os.path.exists(os.path.join(WK, 'primeros.json')) else {}

for v in VIDEOS:
    pool, clips = pool_y_clips()
    first_k = PRIMEROS.get(str(v['n']))
    overlays = []
    if v['chip']:
        overlays.append(dict(type='chip', text=CHIP, icon='', word=v['chip'][0], occ=v['chip'][1]))
    plan = dict(
        vo=f"voces/V{v['n']}.wav", script=f"guiones/V{v['n']}.txt", lang='es',
        speed=1.20, silence=[0.26, 0.12], cut=[1.8, 2.1, 2.5], words=4,
        music='music/bed.wav', music_db=-11,
        hi=v['hi'], hibox=NEGRO, hibord=0, capy=1400, pop=False, italic=False, margin=60,
        font='Montserrat ExtraBold', fsize=66, spacing=2, outline=5, shadow=3,
        hook=v['hook'], hook_size=52, hook_y=210,
        hook_until=v['hasta'][0], hook_until_occ=v['hasta'][1],
        seed=v['n'] * 613, usage='usage.json',
        whoosh=[], flash=0, clips=clips, pool=pool,
        anchors=[['Alivio', 0, 'tapa', 0.0]],
        overlays=overlays)
    if first_k:
        plan['first'] = [first_k, next(s[1] for s in pool if s[0] == first_k)]
    json.dump(plan, open(os.path.join(WK, f"V{v['n']}.json"), 'w'), ensure_ascii=False, indent=1)
    print("V%d listo - %d tramos, %d clips" % (v['n'], len(pool), len(clips)))
