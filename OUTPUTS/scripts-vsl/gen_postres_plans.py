# -*- coding: utf-8 -*-
"""Planes de los 6 ads de Postres en Vaso (AR, 2026-11-14).

Clonado de "Recetas para la familia": b-roll 100 % de vasitos armandose, subtitulo de 3 palabras
con la palabra activa en amarillo (sin caja), sin caja de hook y SIN placa final.

Uso: python3 gen_postres_plans.py   -> escribe V1.json .. V6.json en work/
"""
import os, json

WK = os.path.expanduser('~/Desktop/mi-dulce-negocio/anuncios/work')
SEG = 3.6
TOPE = 6

exec(open(os.path.join(WK, 'vent.py')).read())   # VENT = {clave: (id, desde, hasta, extras)}


def pool_y_clips():
    pool, clips = [], {}
    for k, (vid, a, b, ex) in VENT.items():
        clips[k] = dict(src=f'../tiktoks/{vid}.mp4', fam=vid, **ex)
        tramos, t = [], a
        while t < b - 1.8:
            tramos.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
        if len(tramos) > TOPE:
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    return pool, clips


AMAR = '&H0000E8FF&'      # amarillo (BGR), como la palabra activa de ellos
NEGRO = '&H00000000&'     # "caja" negra = no se ve caja, solo el borde de siempre

VIDEOS = [
    # el plano cae justo cuando se dice la palabra
    dict(n=1, anchors=[('veinte', 0, 'r', 0.5), ('heladera', 0, 'z', 0.5)]),
    dict(n=2, anchors=[('diez', 0, 't', 4.0), ('heladera', 0, 'z', 0.5)]),
    dict(n=3, anchors=[('heladera', 0, 'z', 0.5), ('sábado', 0, 'r', 0.5)]),
    dict(n=4, anchors=[('pastelería', 0, 'F', 4.5), ('cumpleaños', 0, 'r', 0.5)]),
    dict(n=5, anchors=[('vasito', 0, 'F', 4.5), ('heladera', 0, 'z', 0.5)]),
    dict(n=6, anchors=[('capas', 0, 't', 4.0), ('foto', 0, 'r', 0.5)]),
]

for v in VIDEOS:
    pool, clips = pool_y_clips()
    plan = dict(
        vo=f"../vo/V{v['n']}.wav", script=f"V{v['n']}.txt", lang='es',
        speed=1.30, silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], words=3,
        music='music/bed_activo.wav', music_db=-9,
        hi=AMAR, hibox=NEGRO, hibord=8, capy=1450,
        seed=v['n'] * 173, usage='usage.json',
        clips=clips, pool=pool, anchors=v['anchors'], overlays=[])
    json.dump(plan, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print('V%d listo · %d tramos' % (v['n'], len(pool)))
