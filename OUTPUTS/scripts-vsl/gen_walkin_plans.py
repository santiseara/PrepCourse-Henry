# -*- coding: utf-8 -*-
"""Planes de los 6 ads de voz en off del Visual Handbook of Walk-In Coolers & Freezers
(mercado inglés, 2026-11-06).

Se clona la mitad b-roll de Carlos Medina (el ganador en español): clips reales de obra y de
servicio, subtítulo palabra por palabra con la palabra activa adentro de una CAJA DE COLOR,
un color por creativo, sin caja de hook y sin placa final. El video cierra sobre el inserto
de oferta, que es como cierran ellos.

Las ventanas limpias de cada clip están en work/ventanas.json (se arman a mano después de
mirar la hoja de contactos a 1,5 s y un cuadro grande de la mitad inferior de cada clip).

Uso: python3 gen_walkin_plans.py  -> escribe V1.json .. V6.json en work/
"""
import os, json

WK = os.path.expanduser('~/Desktop/walk-in-coolers-freezers/anuncios/work')
VENT = {k: tuple(v) for k, v in json.load(open(f'{WK}/ventanas.json')).items()}
SEG = 4.0
TOPE = 5

GFX = {'CV': 'cover.png', 'PL': 'plate.png', 'OF': 'offer.png'}


def pool_y_clips():
    pool, clips = [], {}
    for k, v in VENT.items():
        vid, a, b = v[0], v[1], v[2]
        ex = v[3] if len(v) > 3 else {}
        clips[k] = dict(src=f'tiktoks/{vid}.mp4', fam=str(vid), **ex)
        tramos, t = [], a
        while t < b - 1.8:
            tramos.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
        if len(tramos) > TOPE:
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    for k, fn in GFX.items():
        clips[k] = dict(src=f'gfx/{fn}', fam=k, still=True)
        pool.append([k, 0, 3.4])
    return pool, clips


# un color de caja por creativo, igual que rota el ganador entre sus ads
VIDEOS = [
    dict(n=1, hi='&H001A1A1A&', hibox='&H003AD2FF&',          # texto tinta · caja amarilla
         anchors=[('Handbook', 0, 'CV', 0), ('plate.', 0, 'PL', 0)]),
    dict(n=2, hi='&H00FFFFFF&', hibox='&H006BC42F&',          # blanco · caja verde
         anchors=[('handbook', 0, 'CV', 0), ('modules,', 0, 'PL', 0)]),
    dict(n=3, hi='&H00FFFFFF&', hibox='&H00F5A82F&',          # blanco · caja celeste
         anchors=[('handbook', 0, 'PL', 0)]),
    dict(n=4, hi='&H00FFFFFF&', hibox='&H001E7AF0&',          # blanco · caja naranja
         anchors=[('handbook,', 0, 'PL', 0)]),
    dict(n=5, hi='&H00FFFFFF&', hibox='&H008C3CE0&',          # blanco · caja magenta
         anchors=[('handbook', 0, 'CV', 0), ('table,', 0, 'PL', 0)]),
    dict(n=6, hi='&H00FFFFFF&', hibox='&H002F3AE0&',          # blanco · caja roja
         anchors=[('handbook', 0, 'CV', 0), ('checklist,', 0, 'PL', 0)]),
]

FIRST = json.load(open(f'{WK}/first.json')) if os.path.exists(f'{WK}/first.json') else {}

for v in VIDEOS:
    pool, clips = pool_y_clips()
    plan = dict(
        vo=f"vo/V{v['n']}.wav", script=f"V{v['n']}.txt", lang='en',
        speed=1.30, silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], words=3,
        music='music/bed_activo.wav', music_db=-8,
        hi=v['hi'], hibox=v['hibox'], hibord=20, capy=1300,
        first=FIRST.get(str(v['n'])), last='OF', seed=v['n'] * 97, usage='usage.json',
        clips=clips, pool=pool, anchors=v['anchors'], overlays=[])
    json.dump(plan, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print(f"V{v['n']}.json  ({len(pool)} recortes de {len(clips)} clips)")
