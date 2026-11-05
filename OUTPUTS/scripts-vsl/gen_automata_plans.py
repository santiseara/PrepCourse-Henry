# -*- coding: utf-8 -*-
"""Planes de los 6 ads de voz en off de Your First Wooden Automaton (mercado ingles, 2026-11-05).

v2 (5/11, pedido de Santiago: "pegate a la edicion de ellos"): se copia el montaje de Orzzen.
  - SIN caja de hook arriba y SIN placa final oscura. El video arranca en el b-roll y cierra con
    la tapa del ebook mas un boton ambar, igual que ellos.
  - Subtitulos de 3 palabras (antes 2) y un COLOR DISTINTO POR VIDEO: ellos rotan amarillo, verde,
    rosa, celeste y naranja entre creativos.
  - INSERTS DE PRODUCTO anclados a la palabra que los nombra: la tapa, una hoja de planos, la
    biblioteca de mecanismos, las 6 fases y la pantalla de la app simuladora. Es lo que mas los
    diferencia de nosotros: muestran el producto todo el tiempo. Se dibujan por codigo con
    gfx_automata.py, asi que no hace falta que el producto exista todavia.

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

# inserts del producto (gfx_automata.py). Entran por anchor, en la palabra que los nombra.
GFX = {'CV': 'cover.png', 'PL': 'plans.png', 'MC': 'mechanisms.png', 'PH': 'phases.png', 'AP': 'app.png'}


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
    for k, fn in GFX.items():
        clips[k] = dict(src=f'gfx/{fn}', fam=k, still=True)
        pool.append([k, 0, 3.4])
    return pool, clips


BTN = dict(type='button', text='I WANT TO START', y=1560)

VIDEOS = [
    dict(n=1, hi='&H0018C5F5&', first=['E', 0],                      # amarillo
         anchors=[('jargon', 0, 'PH', 0), ('illustrations', 0, 'PL', 0)],
         overlays=[dict(type='chip', text='1,400+ FIRST AUTOMATONS BUILT', icon='✓', word='hundred', dur=2.4),
                   dict(type='chip', text='PHOTOS · PLANS · STEP BY STEP', icon='✓', word='photos', dur=2.4),
                   dict(BTN=1, word='Tap')]),
    dict(n=2, hi='&H00F5C835&', first=['F', 0],                      # celeste
         anchors=[('plans', 0, 'PL', 0), ('course', 0, 'PH', 0), ('app', 0, 'AP', 0)],
         overlays=[dict(type='chip', text='PLANS · TEMPLATES · MEASUREMENTS', icon='✓', word='measurements', dur=2.4),
                   dict(type='chip', text='USE THE TOOLS YOU ALREADY HAVE', icon='✓', word='workshop', dur=2.4),
                   dict(BTN=1, word='Tap')]),
    dict(n=3, hi='&H0039E639&', first=['N', 0],                      # verde
         anchors=[('plans', 0, 'PL', 0), ('videos', 0, 'AP', 0)],
         overlays=[dict(type='chip', text='REAL WOOD · REAL MECHANISM', icon='✓', word='fake', dur=2.4),
                   dict(type='chip', text='NO SCREEN · NO BATTERY', icon='✓', word='algorithm', dur=2.4),
                   dict(BTN=1, word='Tap')]),
    dict(n=4, hi='&H003CA9F0&', first=['K', 0],                      # ambar
         anchors=[('order', 0, 'PL', 0), ('videos', 0, 'AP', 0)],
         overlays=[dict(type='chip', text='WHAT TO CUT · WHAT TO GLUE · IN WHAT ORDER', icon='✓', word='glue', dur=2.4),
                   dict(type='chip', text='ONE PIECE THAT STARTS AND ENDS', icon='✓', word='tool', dur=2.4),
                   dict(BTN=1, word='Tap')]),
    dict(n=5, hi='&H00A34FFF&', first=['J', 1.5],                    # rosa
         anchors=[('connect', 0, 'MC', 0), ('templates', 0, 'PL', 0)],
         overlays=[dict(type='chip', text='ONE MOVEMENT AT A TIME', icon='✓', word='movement', dur=2.4),
                   dict(type='chip', text='PLANS · TEMPLATES · VISUAL GUIDES', icon='✓', word='explanations', dur=2.4),
                   dict(BTN=1, word='Meet')]),
    dict(n=6, hi='&H002F7AFF&', first=['U', 0],                      # naranja
         anchors=[('mechanisms', 0, 'MC', 0), ('plans', 0, 'PL', 0)],
         overlays=[dict(type='chip', text='A PIECE PEOPLE STOP TO WATCH', icon='✓', word='curious', dur=2.4),
                   dict(type='chip', text='MECHANISMS · PLANS · ONE SKILL', icon='✓', word='skill', dur=2.4),
                   dict(BTN=1, word='Check')]),
]

for v in VIDEOS:
    pool, clips = pool_y_clips()
    ovs = [dict(BTN, word=o['word'], occ=o.get('occ', 0)) if o.get('BTN') else o for o in v['overlays']]
    first = v['first']
    if not any(x[0] == first[0] and x[1] == first[1] for x in pool):
        raise SystemExit(f"V{v['n']}: el primer plano {first} no esta en el pool. Hay: "
                         + ', '.join(f'{x[0]}@{x[1]}' for x in pool if x[0] == first[0]))
    plan = dict(
        vo=f"vo/V{v['n']}.wav", script=f"V{v['n']}.txt", lang='en',
        speed=1.30, silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], words=3,
        music='music/bed.wav', music_db=-8,
        hi=v['hi'], capy=1380,
        first=first, last='CV', seed=v['n'] * 97,
        clips=clips, pool=pool, anchors=v.get('anchors', []), overlays=ovs)
    json.dump(plan, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print(f"V{v['n']}.json  ({len(pool)} recortes de {len(clips)} clips)")
