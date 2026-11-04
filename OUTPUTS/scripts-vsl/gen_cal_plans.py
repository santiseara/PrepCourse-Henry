# -*- coding: utf-8 -*-
"""Planes de los 6 ads de voz en off de los Calendarios 2027 (mercado ingles, 2026-11-04).

Pool v2: TODO clip tiene un calendario a la vista. El pool v1 (flores de papel, feria, impresora)
se tiro entero: eran escenas lindas del guion pero en ningun cuadro se veia un calendario, y un ad
de calendarios donde no hay calendario no vende. Buscado por los tags deskcalendar, diycalendar,
papercalendar y handmadecalendar.

Filtros aplicados clip por clip sobre la hoja de contactos de 1.5 s:
  - fuera todo lo que dice 2024/2025/2026 legible (vendemos 2027)
  - fuera el espanol, el aleman, el arabe y el tagalo
  - fuera impresion 3D, e-ink, relojes flip y calendarios de adviento
  - fuera personajes con copyright (Sanrio, Harry Potter, Bearbrick) y famosos
  - fuera fabricas (contradicen el "desde casa") y maquinas de corte (contradicen el "sin Cricut")
Uso: python3 gen_cal_plans.py   -> escribe V1.json .. V6.json en ~/Desktop/calendarios-2027-en/anuncios/work/"""
import os, json

WK = os.path.expanduser('~/Desktop/calendarios-2027-en/anuncios/work')

# letra -> (id de TikTok, inicio util, fin util, extras)
VENT = {
    # --- el producto mismo ---
    'A': ('7679474945889455380', 0, 42, {}),      # calendario-florero 2027 con ramo, en caballete. EL producto
    'B': ('7585091358939942166', 0, 4, {}),       # tulipanes de papel parados sobre la base del calendario
    'C': ('7585091358939942166', 13, 28, {}),     # los mismos tulipanes, armandose a mano
    'D': ('7466996351692295431', 0, 26, {}),      # calendarios de escritorio chicos con flores que se abren
    # --- imprimir y armar en casa ---
    'E': ('7682732880446934292', 0, 60, {}),      # cortar, encuadernar y la Epson imprimiendo el calendario 2027
    'F': ('7322202886929173765', 4.5, 10.5, dict(zoom=1.6, ybias=0.0)),  # la HP escupiendo las hojas (cartel abajo)
    'G': ('7439209547669015826', 7, 15, {}),      # recortar y plegar las hojas impresas
    'H': ('7581429573724704021', 30, 43, {}),     # la Canon imprimiendo las paginas del calendario
    'J': ('7675332899951906056', 3, 7.5, {}),     # cortar las piezas del calendario de papel
    'S': ('7675332899951906056', 11, 21, {}),     # las tiras de los doce meses escritas a mano (pasado el '7cm x 11cm')
    # --- los disenos ---
    'K': ('7582335502536199455', 3, 25.5, {}),    # ilustrar y desplegar las doce tarjetas del ano
    'L': ('7589850087459736863', 3.5, 7, {}),     # paginas mensuales dibujadas a mano (pasado el 'calendar for my bf')
    'M': ('7589850087459736863', 12, 21, {}),     # las mismas, junio a agosto (sin la rana del dibujo de marzo)
    'N': ('7540615426749828384', 3, 20, {}),      # pintar a mano las ilustraciones de cada mes
    # --- la tanda y la venta ---
    'O': ('7688575999272963336', 4.5, 38, {}),    # pilas de hojas 2027 y la fila terminada con tulipanes
    'P': ('7685253422047825172', 7.5, 22.5, dict(zoom=1.3, ybias=1.0)),  # pilas de calendarios 2027 para pedidos
    'R': ('7674237279988174100', 0, 18, dict(zoom=1.28, ybias=1.0)),     # el 2027 por dentro (cartel arriba)
}
SEG = 4.5
TOPE = 5          # maximo de recortes por clip


def pool_y_clips():
    pool, clips = [], {}
    for k, (vid, a, b, ex) in VENT.items():
        clips[k] = dict(src=f'tiktoks3/{vid}.mp4', fam=vid, **ex)
        tramos, t = [], a
        while t < b - 1.8:
            tramos.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
        if len(tramos) > TOPE:
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    return pool, clips


FIN = dict(type='end', head=['2027 CALENDAR', 'PACK'],
           sub='50 PRINTABLE DESIGNS · PRICING APP',
           sub2='INSTANT DOWNLOAD · REPRINT FOREVER',
           cta='Tap Learn more 👇')

VIDEOS = [
    dict(n=1, hook='SOLD OUT ON DAY ONE AT THE CRAFT FAIR', hook_until='business', first=['A', 0],
         overlays=[dict(type='chip', text='PRINT AT HOME · CUT WITH SCISSORS', icon='✓', word='scissors', dur=2.4),
                   dict(type='chip', text='ONE FILE · REPRINT IT FOREVER', icon='✓', word='profit', dur=2.4),
                   dict(FIN=1, word='below')]),
    dict(n=2, hook='THE SCHOOL MUMS TOOK EVERY ONE', hook_until='business', first=['A', 13.5],
         overlays=[dict(type='chip', text='PRINT AT HOME · CUT WITH SCISSORS', icon='✓', word='scissors', dur=2.4),
                   dict(type='chip', text='50 DESIGNS FOR 2027', icon='✓', word='profit', dur=2.4),
                   dict(FIN=1, word='below')]),
    dict(n=3, hook='50 DESIGNS + THE APP THAT PRICES THEM', hook_until='printables', first=['D', 0],
         overlays=[dict(type='chip', text='PRINT · CUT · STACK · SELL', icon='✓', word='table', dur=2.4),
                   dict(type='chip', text='THE APP SAVES EVERY ORDER', icon='✓', word='orders', dur=2.4),
                   dict(FIN=1, word='Tap')]),
    dict(n=4, hook='61, HOPELESS WITH COMPUTERS, STILL SELLING', hook_until='calendars', first=['A', 22.5],
         overlays=[dict(type='chip', text='NO CUTTING MACHINE · NO DESIGN SKILLS', icon='✓', word='Cricut', dur=2.4),
                   dict(type='chip', text='REPRINT FOR THE PRICE OF A SHEET', icon='✓', word='profit', dur=2.4),
                   dict(FIN=1, word='Tap')]),
    dict(n=5, hook='WHAT I SOLD THIS WEEKEND', hook_until='scissors', first=['O', 31.5],
         overlays=[dict(type='chip', text='TOOK 15 · CAME HOME WITH NONE', icon='✓', word='none', dur=2.4),
                   dict(type='chip', text='50 DESIGNS · NO MACHINE NEEDED', icon='✓', word='machine', dur=2.4),
                   dict(FIN=1, word='Tap')]),
    dict(n=6, hook='THESE CALENDARS PAID FOR CHRISTMAS DINNER', hook_until='stretch', first=['A', 31.5],
         overlays=[dict(type='chip', text='NAME STICKERS INCLUDED', icon='✓', word='stickers', dur=2.4),
                   dict(type='chip', text='DIGITAL · NO STOCK, NO SHIPPING', icon='✓', word='profit', dur=2.4),
                   dict(FIN=1, word='below')]),
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
        hi='&H003CA9EF&', capy=1380,
        hook=v['hook'], hook_until=v['hook_until'],
        first=first, seed=v['n'] * 97,
        clips=clips, pool=pool, anchors=v.get('anchors', []), overlays=ovs)
    json.dump(plan, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print(f"V{v['n']}.json  ({len(pool)} recortes de {len(clips)} clips)")
