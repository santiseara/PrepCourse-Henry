# -*- coding: utf-8 -*-
"""Planes de los 6 ads de voz en off de Your First Wooden Automaton (mercado ingles, 2026-11-05).

Pool: 20 ventanas de 19 clips de TikTok del tag #woodenautomata, todas con el producto a la vista
(automata de madera moviendose con manivela) o con la construccion (tallar, lijar, prensar, armar).

Filtros aplicados clip por clip sobre la hoja de contactos de 1.5 s:
  - fuera lo que tenia subtitulo o cartel quemado (los tramos sucios se recortaron con la ventana)
  - fuera el espanol y el portugues en pantalla
  - fuera las caras hablando a camara (craftsmm) y las marcas de agua centradas (CRAFTSMM)
  - fuera Etsy y los "link in bio" (por eso se cayo entero el clip de los camarones: el cartel vuelve a los 8 s)
Uso: python3 gen_automata_plans.py  -> escribe V1.json .. V6.json en ~/Desktop/wooden-automaton/anuncios/work/"""
import os, json

WK = os.path.expanduser('~/Desktop/wooden-automaton/anuncios/work')

# letra -> (id de TikTok, inicio util, fin util, extras)
VENT = {
    # --- construir: madera, herramientas, manos ---
    'A': ('7267210847594843425', 4.5, 18, {}),    # cortar los bloques, lijar, perforar, pegar la caja
    'B': ('7267210847594843425', 22, 44, {}),     # pintar las figuras, clavar las varillas, la escena entera
    'C': ('7417792762113723680', 0, 28, {}),      # dremel tallando, prensa, las piezas de la manta ray armadas
    'D': ('7703893203149180192', 4.5, 32.5, {}),  # el gato de los fideos y su mecanismo de engranajes por dentro
    # --- el producto moviendose ---
    'E': ('7568095794360798476', 0, 7.4, {}),     # caballo al galope con manivela (proyecto de la landing)
    'F': ('6961204400442379525', 0, 13, {}),      # la garza, mano girando la manivela, fondo blanco
    'G': ('7528437902838156574', 0, 12.4, {}),    # las dos abejas sobre las flores
    'H': ('7258871608184458539', 0, 17.5, {}),    # el cerdo volador y el mecanismo de la caja
    'J': ('7453078616860101910', 1.5, 20.4, {}),  # la mano de madera que toca el violin
    'K': ('7028968870060772613', 0, 15, {}),      # la oruga: "mi primer automata", armado en casa
    'L': ('7592483834613058847', 0, 18, {}),      # el dragon en la caja azul
    'M': ('7556268869179018527', 4.5, 10.5, {}),  # las tres gallinas y las levas (el subtitulo dura hasta 4,0 s)
    'N': ('7699552647803702550', 0, 7, {}),       # la oveja que camina, fondo azul
    'O': ('7696620870889917728', 0, 9.4, {}),     # la figura humana de madera en el jardin
    'P': ('7691412098617822485', 4.0, 12.8, {}),  # el pajaro sobre el campo (texto en espanol hasta 3,5 s; "Gracias por ver" desde 13,0)
    'Q': ('7580249820716141854', 0, 9, {}),       # el acuario de madera con el pez (antes del Etsy)
    'S': ('7596243620512943390', 0, 4.4, {}),     # la casita de madera en la mano
    'T': ('7345700005413408002', 0, 14.8, dict(zoom=1.45, ybias=1.0)),  # la tortuga voladora (firma grabada abajo)
    'U': ('7220458596763569434', 0, 18, {}),      # el barco y el faro sobre las olas azules
}
SEG = 4.0
TOPE = 5          # maximo de recortes por clip


def pool_y_clips():
    pool, clips = [], {}
    for k, (vid, a, b, ex) in VENT.items():
        clips[k] = dict(src=f'tiktoks/{vid}.mp4', fam=vid, **ex)
        tramos, t = [], a
        while t < b - 1.8:
            tramos.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
        if len(tramos) > TOPE:
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    return pool, clips


FIN = dict(type='end', head=['YOUR FIRST WOODEN', 'AUTOMATON'],
           sub='GUIDE · VIDEO COURSE · PLANS',
           sub2='SIMULATOR APP · 30-DAY GUARANTEE',
           cta='Tap Learn more 👇')

VIDEOS = [
    dict(n=1, hook='NO MOTOR. NO ELECTRONICS. NO TRICKS.', hook_until='guide', first=['E', 0],
         overlays=[dict(type='chip', text='1,400+ FIRST AUTOMATONS BUILT', icon='✓', word='hundred', dur=2.4),
                   dict(type='chip', text='PHOTOS · PLANS · STEP BY STEP', icon='✓', word='illustrations', dur=2.4),
                   dict(FIN=1, word='Tap')]),
    dict(n=2, hook="IT'S WOOD. THERE'S NO MOTOR.", hook_until='crank', first=['F', 0],
         overlays=[dict(type='chip', text='PLANS · TEMPLATES · MEASUREMENTS', icon='✓', word='measurements', dur=2.4),
                   dict(type='chip', text='USE THE TOOLS YOU ALREADY HAVE', icon='✓', word='workshop', dur=2.4),
                   dict(FIN=1, word='Tap')]),
    dict(n=3, hook='NO SCREEN. NO BATTERY. NO ALGORITHM.', hook_until='crank', first=['N', 0],
         overlays=[dict(type='chip', text='REAL WOOD · REAL MECHANISM', icon='✓', word='fake', dur=2.4),
                   dict(type='chip', text='PHOTOS · PLANS · VIDEOS', icon='✓', word='videos', dur=2.4),
                   dict(FIN=1, word='Tap')]),
    dict(n=4, hook='WHEN DID YOU LAST FINISH SOMETHING?', hook_until='dishes', first=['K', 0],
         overlays=[dict(type='chip', text='WHAT TO CUT · WHAT TO GLUE · IN WHAT ORDER', icon='✓', word='order', dur=2.4),
                   dict(type='chip', text='ONE PIECE THAT STARTS AND ENDS', icon='✓', word='tool', dur=2.4),
                   dict(FIN=1, word='Tap')]),
    dict(n=5, hook='THAT LOOKS IMPOSSIBLE TO MAKE', hook_until='magic', first=['J', 1.5],
         overlays=[dict(type='chip', text='ONE MOVEMENT AT A TIME', icon='✓', word='movement', dur=2.4),
                   dict(type='chip', text='PLANS · TEMPLATES · VISUAL GUIDES', icon='✓', word='templates', dur=2.4),
                   dict(FIN=1, word='Meet')]),
    dict(n=6, hook='MOST PEOPLE SEE AN ORNAMENT', hook_until='different', first=['U', 0],
         overlays=[dict(type='chip', text='A PIECE PEOPLE STOP TO WATCH', icon='✓', word='curious', dur=2.4),
                   dict(type='chip', text='MECHANISMS · PLANS · ONE SKILL', icon='✓', word='mechanisms', dur=2.4),
                   dict(FIN=1, word='Check')]),
]

for v in VIDEOS:
    pool, clips = pool_y_clips()
    ovs = [dict(FIN, word=o['word'], occ=o.get('occ', 0)) if o.get('FIN') else o for o in v['overlays']]
    first = v['first']
    if not any(x[0] == first[0] and x[1] == first[1] for x in pool):
        raise SystemExit(f"V{v['n']}: el primer plano {first} no esta en el pool. Hay: "
                         + ', '.join(f'{x[0]}@{x[1]}' for x in pool if x[0] == first[0]))
    plan = dict(
        vo=f"vo/V{v['n']}.wav", script=f"V{v['n']}.txt", lang='en',
        speed=1.30, silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], words=2,
        music='music/bed.wav', music_db=-8,
        hi='&H00338FD6&', capy=1380,
        hook=v['hook'], hook_until=v['hook_until'],
        first=first, seed=v['n'] * 97,
        clips=clips, pool=pool, anchors=v.get('anchors', []), overlays=ovs)
    json.dump(plan, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print(f"V{v['n']}.json  ({len(pool)} recortes de {len(clips)} clips)")
