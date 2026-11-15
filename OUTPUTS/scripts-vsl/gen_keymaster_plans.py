# -*- coding: utf-8 -*-
"""Planes de los 6 ads de KeyMaster Hub (ingles, 2026-11-14).

Clonado de "Centro Maestro del Cerrajero": b-roll de cerrajeria automotriz, la app a pantalla
completa dos o tres veces por video anclada a la palabra que la nombra, subtitulo de UNA palabra
en dorado con borde negro y placa de cierre con el CTA.

Las voces salieron a ritmo natural (26-34 s para 67-86 palabras), asi que van a speed 1.06 y no
a 1.30: con 1.30 quedarian en 20-26 s, por debajo del rango del competidor (27-46 s).

Uso: python3 gen_keymaster_plans.py   -> escribe V1.json .. V6.json en work/
"""
import os, json

WK = os.path.expanduser('~/Desktop/keymaster-hub/anuncios/work')
SEG = 3.4          # largo del tramo que se corta de cada ventana
TOPE = 6           # tramos como maximo por ventana, para que un clip no coma el video

ns = {}
exec(open(os.path.join(WK, 'vent.py')).read(), ns)
VENT, APP = ns['VENT'], ns['APP']


CON_TEXTO = {'x', 'a', 'p', 'O', 'K', 'M'}   # llevan texto del objeto, legible en pantalla


def pool_y_clips():
    """Los clips del pool + las 4 maquetas de la app, que son un plano mas."""
    pool, clips = [], {}
    for k, (vid, a, b, ex) in VENT.items():
        clips[k] = dict(src=f'../tiktoks/{vid}.mp4', **ex)
        if k in CON_TEXTO:            # codigos de espadin, CARDOT, Milwaukee, MaxiIM: no se espejan
            clips[k]['noflip'] = True
        tramos, t = [], a
        while t < b - 1.8:
            tramos.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
        if len(tramos) > TOPE:
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    for k, src in APP.items():
        # van como PNG con still: el editor les pone el zoom y NUNCA las espeja (el texto se leeria al reves)
        clips[k] = dict(src=src, fam=k, still=True)
        pool += [[k, 0.0, 3.6]]
    return pool, clips


ORO    = '&H0038B4F0&'    # dorado (BGR) — el color de su palabra activa
NEGRO  = '&H00000000&'    # sin caja: solo el borde negro de siempre

VIDEOS = [
    # el plano de la app cae justo cuando la voz nombra el dato tecnico
    dict(n=1, anchors=[('transponder', 0, 'A3', 0.0), ('frequency', 0, 'A3', 0.0), ('blank', 0, 'x', 0.0)]),
    dict(n=2, anchors=[('vehicle', 0, 'A2', 0.0), ('transponder', 0, 'A3', 0.0)]),
    dict(n=3, anchors=[('bar', 0, 'A2', 0.0), ('screen', 0, 'A3', 0.0)]),
    dict(n=4, anchors=[('screen', 1, 'A3', 0.0), ('blank', 0, 'x', 0.0)]),
    dict(n=5, anchors=[('vehicles', 0, 'A1', 0.0), ('procedures', 0, 'A4', 0.0)]),
    dict(n=6, anchors=[('batteries', 0, 'A4', 0.0), ('vehicle', 0, 'A3', 0.0)]),
]

# Ellos NO cierran con placa oscura: ponen el CTA sobre el b-roll, en rojo.
# Por eso va 'button' (pastilla sobre el plano) y no 'end' (placa a pantalla completa).
CIERRE = dict(type='button', word='Tap', occ=0, text='TAP LEARN MORE', size=66, y=1530)

for v in VIDEOS:
    pool, clips = pool_y_clips()
    plan = dict(
        vo=f"../vo/V{v['n']}.wav", script=f"V{v['n']}.txt", lang='en',
        speed=1.06, silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], words=1,
        hi=ORO, hibox=NEGRO, hibord=8, capy=1430,
        seed=v['n'] * 211, usage='usage.json',
        clips=clips, pool=pool, anchors=v['anchors'],
        overlays=[CIERRE])
    json.dump(plan, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print('V%d listo · %d tramos en el pool' % (v['n'], len(pool)))
