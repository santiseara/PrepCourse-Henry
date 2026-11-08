# -*- coding: utf-8 -*-
"""Planes de los 6 ads de la cartilla de quesos (LATAM, 2026-11-08).

Clonado de Queijo de Casa (BR): b-roll real de queseria artesanal + las paginas del cuadernillo
ORO BLANCO ancladas a la palabra que las nombra, subtitulos derechos en mayuscula de 3 palabras
TODOS BLANCOS (el ganador no resalta la palabra activa en color) y sin placa de cierre: cierra
con el subtitulo sobre el ultimo plano, como ellos.

Pool: clips de TikTok de #comohacerqueso, #quesocasero y #quesoartesanal revisados con hoja de
contactos a 1,5 s. #quesorelleno se midio podrido (resenas de supermercado, caras y subtitulos
quemados) y se descarto entero.

Uso: python3 gen_quesos_plans.py  -> escribe V1.json .. V6.json en work/
"""
import os, json

WK = os.path.expanduser('~/Desktop/quesos/anuncios/work')
SEG = 4.0
TOPE = 5

# clave -> (archivo sin .mp4, desde, hasta, extras).  Ventanas revisadas una por una.
VENT = {}
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vent_quesos.py')).read())

GFX = {'T': 'tapa.png', 'S': 'sumario.png', 'R': 'rellenos.png',
       'U': 'suero.png', 'D': 'rendimiento.png', 'Y': 'yogur.png', 'C': 'carta.png'}


def pool_y_clips(gfx_keys):
    pool, clips = [], {}
    for k, (fn, a, b, ex) in VENT.items():
        d = dict(src=f'clips/{fn}.mp4', fam=fn.split('_')[-1][:12]); d.update(ex)
        clips[k] = d
        tramos, t = [], a
        while t < b - 1.8:
            tramos.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
        if len(tramos) > TOPE:
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    for k in gfx_keys:
        fn = GFX[k]
        clips[k] = dict(src=f'gfx/{fn}', fam=k, still=True)
        pool.append([k, 0, 3.4])
    return pool, clips


BLANCO = '&H00FFFFFF&'    # el ganador NO resalta la palabra activa: todo blanco
NEGRO = '&H00000000&'     # "caja" negra = no se ve caja, solo el borde de siempre

VIDEOS = [
    dict(n=1, gfx='TR', first=['1', 3.0], anchors=[('cartilla', 0, 'T', 0), ('rellenos', 1, 'R', 0)], last='T'),
    dict(n=2, gfx='TUS', first=['b', 6.4], anchors=[('ricota', 0, 'U', 0), ('cartilla', 0, 'T', 0), ('rinde', 0, 'S', 0)], last='U'),
    dict(n=3, gfx='TDC', first=['3', 0.3], anchors=[('segundo', 0, 'D', 0), ('cartilla', 0, 'T', 0), ('yogur', 0, 'C', 0)], last='D'),
    dict(n=4, gfx='TR', first=['2', 0.3], anchors=[('corazon', 0, 'R', 0), ('cartilla', 0, 'T', 0), ('cinco', 1, 'R', 0)], last='R'),
    dict(n=5, gfx='TY', first=['5', 4.0], anchors=[('yogur', 1, 'Y', 0), ('cartilla', 0, 'T', 0)], last='Y'),
    dict(n=6, gfx='TCS', first=['4', 0.3], anchors=[('tacho', 0, 'C', 0), ('cartilla', 0, 'T', 0), ('guia', 0, 'S', 0)], last='C'),
]

for v in VIDEOS:
    pool, clips = pool_y_clips(v['gfx'])
    plan = dict(
        vo=f"vo/V{v['n']}.wav", script=f"V{v['n']}.txt", lang='es',
        speed=1.30, silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], words=3,
        music='music/bed_activo.wav', music_db=-9,
        hi=BLANCO, hibox=NEGRO, hibord=8, capy=1090,
        first=v.get('first'), last=v['last'], seed=v['n'] * 173, usage='usage.json',
        clips=clips, pool=pool, anchors=v['anchors'], overlays=[])
    if plan['first'] is None:
        del plan['first']
    json.dump(plan, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print('V%d listo - %d tramos' % (v['n'], len(pool)))
