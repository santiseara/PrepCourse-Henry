# -*- coding: utf-8 -*-
"""Planes de los 6 ads de voz en off de Arreglá Tu Ropa (Argentina, 2026-11-05).

Se clona la edición de Stitched Fits, no solo el guion:
  - SIN caja de hook y SIN placa final. El video arranca en el b-roll y cierra sobre el inserto
    de la página de ventas, con el subtítulo encima. Es su cierre exacto.
  - Subtítulos de 3 palabras, en itálica, blancos con borde negro, y la palabra que suena dentro
    de una CAJA DE COLOR. Un color de caja distinto por creativo, igual que ellos.
  - Inserto de producto = grabación de pantalla de la página y de la plataforma (gfx_arreglos.py),
    anclado a la palabra que lo nombra. No es un mockup: ellos filman la pantalla.

Las ventanas limpias de cada clip están en work/ventanas.json (se arman a mano después de mirar
la hoja de contactos a 1,5 s y un cuadro grande de la mitad inferior de cada clip).

Uso: python3 gen_arreglos_plans.py  -> escribe V1.json .. V6.json en work/
"""
import os, json

WK = os.path.expanduser('~/Desktop/arreglos-de-ropa/anuncios/work')
VENT = {k: tuple(v) if len(v) == 3 else (v[0], v[1], v[2], v[3])
        for k, v in json.load(open(f'{WK}/ventanas.json')).items()}
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


# un color de caja por creativo (BGR de ASS), como rota Stitched Fits entre sus ads
VIDEOS = [
    # texto amarillo · caja rosa — abre en la maquina de coser
    dict(n=1, hi='&H003AE2FF&', hibox='&H00B08BF5&', first=['B', 0],
         anchors=[('clases', 0, 'CL', 0)]),
    # texto blanco · caja magenta — abre en la camisa que le queda enorme
    dict(n=2, hi='&H00FFFFFF&', hibox='&H009B45E0&', first=['L', 0],
         anchors=[('videos', 0, 'CL', 0)]),
    # texto blanco · caja celeste — abre en los alfileres sobre el escote
    dict(n=3, hi='&H00FFFFFF&', hibox='&H00F7C34F&', first=['Q', 0],
         anchors=[('clases', 0, 'CL', 0)]),
    # texto tinta · caja amarilla — abre en la maquina industrial
    dict(n=4, hi='&H001A1A1A&', hibox='&H002ED2FF&', first=['J', 3],
         anchors=[('videos', 0, 'CL', 0)]),
    # texto blanco · caja violeta — abre en el ruedo del jean
    dict(n=5, hi='&H00FFFFFF&', hibox='&H00F56B9B&', first=['A', 0],
         anchors=[('Medida', 0, 'CL', 0)]),
    # texto tinta · caja verde — abre en el sweater que le queda grande
    # (sin inserto de clases: en este guion el producto recien se nombra al final, y ahi cierra VE)
    dict(n=6, hi='&H001A1A1A&', hibox='&H007AD65B&', first=['Y', 4.5],
         anchors=[]),
]

for v in VIDEOS:
    pool, clips = pool_y_clips()
    plan = dict(
        vo=f"vo/V{v['n']}.wav", script=f"V{v['n']}.txt", lang='es',
        speed=1.30, silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], words=3,
        music='music/bed_activo.wav', music_db=-8,   # 2026-11-05: Santiago pidio una cama mas activa (118 BPM con bombo, music.py)
        hi=v['hi'], hibox=v['hibox'], hibord=20, capy=1300,
        first=v['first'], last='VE', seed=v['n'] * 97, usage='usage.json',
        clips=clips, pool=pool, anchors=v['anchors'], overlays=[])
    json.dump(plan, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print(f"V{v['n']}.json  ({len(pool)} recortes de {len(clips)} clips)")
