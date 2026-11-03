# -*- coding: utf-8 -*-
"""Planes de los 6 ads de voz en off de The Drawing World (mercado ingles, 2026-11-03).
Mismo pool de clips de TikTok de manos dibujando que Academia del Trazo (ventanas y vetos ya revisados),
paleta de drawing-world.impultienda.ar y placa final en ingles.
Uso: python3 gen_dw_plans.py   -> escribe V1.json .. V6.json en ~/Desktop/drawing-world/anuncios/work/"""
import os, json

WK = os.path.expanduser('~/Desktop/drawing-world/anuncios/work')

# clip -> (inicio util, fin util, extras). Ventanas heredadas de gen_trazo_plans.py (hojas de contactos a
# 1 cuadro cada 2 s, mas un cuadro grande de la mitad inferior). Los clips descartados por texto quemado,
# cara hablando a camara o capturas de pantalla estan listados ahi y no se vuelven a bajar.
VENT = {
    'A': (0, 32,  {}),                              # retrato en cuaderno espiral, limpio de punta a punta
    'B': (0, 66,  {}),                              # escena circular a lapiz, cenital, sin texto
    'C': (0, 30,  {}),                              # retrato femenino, planos muy cerrados del lapiz
    'D': (4, 20,  {}),                              # manzana realista (volumen y sombra)
    'E': (24, 48, {}),                              # retrato familiar (arranca despues del autor en camara)
    'F': (8, 24,  {}),                              # perfil en cuaderno
    'G': (4, 12,  {}),                              # cuaderno nuevo
    'H': (0, 38,  {}),                              # retrato de un senor
    'I': (0, 52,  {}),                              # retrato de una senora, limpio
    'J': (0, 58,  dict(zoom=1.30, ybias=1.0)),      # mano paso a paso (recorte por el cartel de arriba)
    'K': (0, 60,  dict(zoom=1.30, ybias=1.0)),      # mano con manzana (mismo cartel arriba)
    'L': (0, 68,  {}),                              # rostro construido desde el circulo
    'M': (0, 90,  {}),                              # retrato grande en atril
    'N': (0, 68,  {}),                              # sombreado de rostro en primerisimo plano
    'O': (0, 42,  {}),                              # retrato realista, planos cerrados
}
SRC = {'A': '7290714287776009478', 'B': '7514725669117414661', 'C': '7524925043365694725',
       'D': '7270223525473144070', 'E': '7376438372610477317', 'F': '7639583406728236308',
       'G': '7689652898581482772', 'H': '7463613509910203678', 'I': '7465892650797829406',
       'J': '7658232090349079822', 'K': '7658959106920811790', 'L': '7517317342662036741',
       'M': '7376491812879404294', 'N': '7329749534349839622', 'O': '7550631925598260487'}
FAM = {'A': 'esmit', 'B': 'dibujafacil', 'C': 'artejmc', 'D': 'grafitos', 'E': 'aristaviva',
       'F': 'chriiswo', 'G': 'cintia', 'H': 'gerardo', 'I': 'gerardo', 'J': 'graphite',
       'K': 'graphite', 'L': 'eli7', 'M': 'benito', 'N': 'fiinadys', 'O': 'azure'}
SEG = 4.5
TOPE = 8          # maximo de recortes por clip


def pool_y_clips():
    pool, clips = [], {}
    for k, (a, b, ex) in VENT.items():
        clips[k] = dict(src=f'tiktoks/{SRC[k]}.mp4', fam=FAM[k], **ex)
        tramos, t = [], a
        while t < b - 1.8:
            tramos.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
        if len(tramos) > TOPE:                       # repartidos a lo largo del clip, no los primeros
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    return pool, clips


FIN = dict(type='end', head=['THE DRAWING', 'WORLD'],
           sub='54 VIDEO LESSONS · 4 PDF GUIDES',
           sub2='LIFETIME ACCESS · 10-DAY GUARANTEE',
           cta='Tap Learn more 👇')

VIDEOS = [
    dict(n=1, hook='21 DAYS: THE PHOTO ON YOUR LOCK SCREEN', hook_until='screen', first=['L', 0],
         overlays=[dict(type='chip', text='FROM THE FIRST LINE, IN ORDER', icon='✓', word='path', dur=2.4),
                   dict(type='chip', text='20 MINUTES A DAY · 7 HOURS TOTAL', icon='✓', word='hours', dur=2.4),
                   dict(FIN=1, word='Tap')]),
    dict(n=2, hook='200 TUTORIALS AND STILL NO FACE', hook_until='hand', first=['C', 0],
         overlays=[dict(type='chip', text='BASICS · LINE · SHADOW · FORM', icon='✓', word='order', dur=2.4),
                   dict(type='chip', text='4 WORKING PDFs INCLUDED', icon='✓', word='guides', dur=2.4),
                   dict(FIN=1, word='Tap')]),
    dict(n=3, hook='TALENT IS PRACTICE YOU NEVER SAW', hook_until='volume', first=['H', 0],
         overlays=[dict(type='chip', text='ONE THING PER DAY, IN SEQUENCE', icon='✓', word='sequence', dur=2.4),
                   dict(type='chip', text='200+ GUIDED PROJECTS', icon='✓', word='hundred', dur=2.4),
                   dict(FIN=1, word='Tap')]),
    dict(n=4, hook='NOBODY ASKS IF IT IS TOO LATE TO COOK', hook_until='children', first=['M', 0],
         overlays=[dict(type='chip', text='BUILT FOR COMPLETE BEGINNERS', icon='✓', word='nothing', dur=2.4),
                   dict(type='chip', text='ALL YOU NEED IS PAPER AND A PENCIL', icon='✓', word='pencil', occ=1, dur=2.4),
                   dict(FIN=1, word='Tap')]),
    dict(n=5, hook='YOU STARTED ON DAY 24', hook_until='ball', first=['D', 4],
         overlays=[dict(type='chip', text='DAY 4: SPHERE, CUBE, CYLINDER', icon='✓', word='cylinder', dur=2.4),
                   dict(type='chip', text='DAY 7: IT LIFTS OFF THE PAPER', icon='✓', word='paper', dur=2.4),
                   dict(FIN=1, word='Tap')]),
    dict(n=6, hook='THE FACE YOU KNOW BY HEART', hook_until='died', first=['I', 0],
         overlays=[dict(type='chip', text='HAIR IN SECTIONS, FUR WITH DIRECTION', icon='✓', word='sections', dur=2.4),
                   dict(type='chip', text='54 LESSONS · YOURS FOR LIFE', icon='✓', word='life', dur=2.4),
                   dict(FIN=1, word='Tap')]),
]

for v in VIDEOS:
    pool, clips = pool_y_clips()
    ovs = [dict(FIN, word=o['word'], occ=o.get('occ', 0)) if o.get('FIN') else o for o in v['overlays']]
    first = v.get('first') or pool[v['n'] % len(pool)][:2]
    if not any(x[0] == first[0] and x[1] == first[1] for x in pool):
        raise SystemExit(f"V{v['n']}: el primer plano {first} no esta en el pool.")
    plan = dict(
        vo=f"vo/V{v['n']}.wav", script=f"V{v['n']}.txt", lang='en',
        speed=1.30, silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], words=2,
        music='music/bed.wav', music_db=-8,
        hi='&H000B9EF5&', capy=1380,
        hook=v['hook'], hook_until=v['hook_until'],
        first=first, seed=v['n'] * 110,
        clips=clips, pool=pool, anchors=v.get('anchors', []), overlays=ovs)
    json.dump(plan, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print(f"V{v['n']}.json  ({len(pool)} recortes de {len(clips)} clips)")
