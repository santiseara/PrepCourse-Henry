# -*- coding: utf-8 -*-
"""Planes de los 3 ads de renovación de A Tu Medida (V7-V9, 2026-11-07).

Qué cambia respecto de la tanda 1 (regla del 27/10: una renovación cambia también la estética):
  - 11 clips de TikTok que nunca se usaron (tags de oficio: ruedos y bridal), revisados con
    hoja de contactos a 1,5 s y los dos bordes de cada ventana a 0,5 s. usage.json se mantiene,
    así el editor prefiere el material nuevo y casi no toca el de la tanda 1.
  - Subtítulos de 4 palabras en vez de 3, y tres colores de caja nuevos (naranja, rojo, turquesa).
  - Mismo sistema: sin caja de hook, sin placa final, cierre sobre el inserto de la página.

Uso: python3 gen_arreglos_plans_v2.py  -> escribe V7.json .. V9.json en work/
"""
import os, json

WK = os.path.expanduser('~/Desktop/arreglos-de-ropa/anuncios/work')
VENT = json.load(open(f'{WK}/ventanas.json'))
SEG = 4.0
TOPE = 5
GFX = {'VE': 'venta.png', 'CL': 'clases.png'}


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
    for k, fn in GFX.items():
        clips[k] = dict(src=f'gfx/{fn}', fam=k, still=True)
        pool.append([k, 0, 3.4])
    return pool, clips


VIDEOS = [
    # texto tinta · caja naranja — abre en la maquina de coser de casa
    dict(n=7, hi='&H001A1A1A&', hibox='&H000E7CFF&', first=['g', 28.0],
         anchors=[('clases', 0, 'CL', 0)]),
    # texto blanco · caja roja — abre en la prenda colgada
    dict(n=8, hi='&H00FFFFFF&', hibox='&H003A3AE8&', first=['b', 0],
         anchors=[('clases', 0, 'CL', 0)]),
    # texto tinta · caja turquesa — abre en la camisa bajo la maquina
    dict(n=9, hi='&H001A1A1A&', hibox='&H00C8C840&', first=['f', 0],
         anchors=[('clases', 0, 'CL', 0)]),
]

for v in VIDEOS:
    pool, clips = pool_y_clips()
    plan = dict(
        vo=f"vo/V{v['n']}.wav", script=f"V{v['n']}.txt", lang='es',
        speed=1.30, silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], words=4,
        music='music/bed_activo.wav', music_db=-8,
        hi=v['hi'], hibox=v['hibox'], hibord=20, capy=1300,
        first=v['first'], last='VE', seed=v['n'] * 131, usage='usage.json',
        clips=clips, pool=pool, anchors=v['anchors'], overlays=[])
    json.dump(plan, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print('V%d listo · %d tramos' % (v['n'], len(pool)))
