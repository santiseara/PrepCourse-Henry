# -*- coding: utf-8 -*-
"""Planes de los 6 ads de Helados que Venden (LATAM neutro, 2026-11-19),
clonando la edicion de Camila Torres (heladosquevenden.impultienda.ar).

Medido sobre sus 48 ads activos (12 bajados y transcriptos el 19/11):
  - 9:16, 27 a 40 s, voz en off de mujer y cama musical por debajo.
  - 100 % b-roll de produccion de helado, sin una sola cara.
  - PLACA BLANCA arriba los primeros segundos, dos renglones: el primero NEGRO y el
    segundo ROJO, todo en mayuscula (la tienen 3 de 6: "PARECEN / DE HELADERÍA").
  - SUBTITULOS en mayuscula, Montserrat ExtraBold recta (NO italica), blancos con borde
    negro, 2-3 palabras en un renglon, tercio inferior, con la palabra que suena en
    color (texto de color, sin caja): rotan turquesa, verde lima y amarillo.
  - FLECHA ROJA hacia abajo sobre el b-roll cuando llega el CTA.
  - Sin fichas de paso, sin placa final y sin boton.

Uso: python3 gen_helados_plans.py   -> V1.json .. V6.json en anuncios/work/
"""
import os, re, sys, json

WK = os.path.expanduser('~/Desktop/helados/anuncios/work')
sys.path.insert(0, WK)
from vent_helados import VENT

SEG = 2.6          # largo de cada tramo candidato
TOPE = 6           # maximo de recortes por clip

TURQUESA = '&H00D2E619&'   # #19E6D2
LIMA     = '&H001AFF7C&'   # #7CFF1A
AMARILLO = '&H001AE1FF&'   # #FFE11A
NEGRO    = '&H00000000&'

_vs = open(os.path.join(WK, 'vent_helados.py')).read()
AUTOR = dict(re.findall(r"'(c\d+)':\s*\('(\d+)'", _vs))


def pool_y_clips():
    pool, clips = [], {}
    for k, v in VENT.items():
        vid, a, b = v[0], v[1], v[2]
        ex = v[3] if len(v) > 3 else {}
        clips[k] = dict(src=f'clips/{vid}.mp4', fam=AUTOR.get(k, vid), **ex)
        tramos, t = [], a
        while t < b - 1.4:
            tramos.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
        if len(tramos) > TOPE:
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    return pool, clips


VIDEOS = [
    dict(n=1, hi=TURQUESA, hook='PARECEN|DE HELADERÍA',          hasta=('fiestas', 0),  first='c32'),
    dict(n=2, hi=LIMA,     hook='UNA SOLA BASE|+100 SABORES',    hasta=('olla', 0),     first='c09'),
    dict(n=3, hi=AMARILLO, hook='SIN LECHE CONDENSADA|NI CREMA DE LECHE', hasta=('leche', 1), first='c28'),
    dict(n=4, hi=TURQUESA, hook='DESDE TU CASA|SIN SALIR A TRABAJAR',     hasta=('trabajar', 0), first='c33'),
    dict(n=5, hi=LIMA,     hook='UNA SOLA BASE|+50 SABORES EN UN DÍA',    hasta=('italiana', 0), first='c16'),
    dict(n=6, hi=AMARILLO, hook='UNA OLLA|Y UN CONGELADOR',      hasta=('grande', 0),   first='c25'),
]

for v in VIDEOS:
    pool, clips = pool_y_clips()
    plan = dict(
        vo=f"voces/V{v['n']}.wav", script=f"guiones/V{v['n']}.txt", lang='es',
        speed=1.20, silence=[0.26, 0.12], cut=[1.5, 1.9, 2.4], words=3,
        music='music/bed.wav', music_db=-10,
        hi=v['hi'], hibox=NEGRO, hibord=0, capy=1430, pop=False, italic=False, margin=60,
        font='Montserrat ExtraBold', fsize=70, spacing=2, outline=5, shadow=3,
        hook=v['hook'], hook_size=58, hook_y=250,
        hook_until=v['hasta'][0], hook_until_occ=v['hasta'][1],
        first=[v['first'], next(s[1] for s in pool if s[0] == v['first'])],
        seed=v['n'] * 907, usage='usage.json',
        whoosh=[], flash=0, clips=clips, pool=pool, anchors=[],
        overlays=[dict(type='flecha', word='boton', occ=0, y=1180)])
    json.dump(plan, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print("V%d listo - %d tramos" % (v['n'], len(pool)))
