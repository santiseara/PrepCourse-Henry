# -*- coding: utf-8 -*-
"""Planes de los 6 ads de voz en off de BarberPro MegaPack (mercado ingles, 2026-11-01).
Uso: python3 gen_barber_plans.py   -> escribe V1.json .. V6.json y V1.txt .. V6.txt en ~/Desktop/barber-pro/anuncios/work/"""
import os, json

WK = os.path.expanduser('~/Desktop/barber-pro/anuncios/work')

# clip -> (inicio util, fin util, extras). Ventanas revisadas en hojas de contactos a 1 cuadro cada 2 s.
# Descartados por texto quemado: 7391055 y 7532994 y 7550833 (carteles en espanol), 7657013 ("PASO A PASO FADE"),
# 7646883 y 7694093 y 7685863 y 7691755 (subtitulos en espanol), 7677652 y 7609889 (subtitulos en ingles),
# 7645113 y 7656605 (cartel "LEVER OPEN" repetido), 7700332 ("Assume everything will work out"), y los de baja resolucion que no aportan.
VENT = {
    'A': (0, 33,   {}),              # 7524696 tijera y peine, barberia clara, sin texto
    'B': (4, 48,   {}),              # 7606775 manos y tijera, barberia blanca
    'C': (0, 58,   {}),              # 7597515 fade lateral con barba, limpio
    'E': (0, 38,   {}),              # 7700312 peine y maquina, plano cerrado
    'F': (0, 35,   {}),              # 7698172 barbero con peine y maquina
    'G': (0, 14,   {}),              # 7699929 corte terminado, cliente en el sillon
    'H': (7, 13,   {}),              # 7662865 clipper over comb (ventana sin el cartel del inicio)
    'J': (0, 8,    {}),              # 7579245 barberia, plano general
    'K': (0, 8,    {}),              # 7602321 fade, plano corto
}
SRC = {'A': '7524696667791101240', 'B': '7606775155330780438', 'C': '7597515132989639966',
       'E': '7700312134516804894', 'F': '7698172487162416415',
       'G': '7699929635034778887', 'H': '7662865222100602143', 'I': '7656605291265543454',
       'J': '7579245435672595735', 'K': '7602321063153896735'}
# familias: varios clips del mismo creador cuentan como una sola fuente visual
FAM = {'A': 'andres', 'G': 'andres', 'B': 'maagic', 'C': 'faded', 'E': 'faded',
       'F': 'faded', 'K': 'faded', 'H': 'whisperer', 'J': 'gio'}
SEG = 4.5
TOPE = 8          # maximo de recortes por clip

def pool_y_clips():
    pool, clips = [], {}
    for k, (a, b, ex) in VENT.items():
        clips[k] = dict(src=f'tiktoks/{SRC[k]}.mp4', fam=FAM[k], **ex)
        tramos = []
        t = a
        while t < b - 1.8:
            tramos.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
        if len(tramos) > TOPE:                       # repartidos a lo largo del clip, no los primeros
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    return pool, clips

FIN = dict(type='end', head=['BARBERPRO', 'MEGAPACK'],
           sub='100+ VIDEO LESSONS · 5 BONUSES',
           sub2='INSTANT ACCESS · 7-DAY GUARANTEE',
           cta='Tap Learn more 👇')

VIDEOS = [
    dict(n=1, hook='SHOWN ONCE. AT FULL SPEED.', hook_until='eleven', first=['A', 0], seed=110,
         overlays=[dict(type='chip', text='STOP · REWIND · RUN AGAIN', icon='✓', word='rewind', dur=2.4),
                   dict(type='chip', text='100+ VIDEO LESSONS', icon='✓', word='hundred', dur=2.4),
                   dict(FIN=1, word='cut')]),
    dict(n=2, hook='YOU PAID. YOU STILL LEAVE LINES.', hook_until='problem', first=['C', 0], seed=220,
         overlays=[dict(type='chip', text="IT'S NOT YOUR SKILL", icon='✓', word='secret', dur=2.4),
                   dict(type='chip', text='7 FUNDAMENTALS, WRITTEN', icon='✓', word='fundamentals', dur=2.4),
                   dict(FIN=1, word='own')]),
    dict(n=3, hook='ONE EXTRA FADE A WEEK', hook_until='back', first=['B', 4], seed=330,
         overlays=[dict(type='chip', text='LESS THAN A DINNER, ONCE', icon='✓', word='dinner', dur=2.4),
                   dict(type='chip', text='7-DAY GUARANTEE', icon='✓', word='guarantee', dur=2.4),
                   dict(FIN=1, word='weekend')]),
    dict(n=4, hook='CLASS STARTS WHEN YOU HIT PLAY', hook_until='play', first=['F', 0], seed=440,
         overlays=[dict(type='chip', text='NO CAMPUS · NO COMMUTE', icon='✓', word='commute', dur=2.4),
                   dict(type='chip', text='ASK ON WHATSAPP', icon='✓', word='WhatsApp', dur=2.4),
                   dict(FIN=1, word='tonight')]),
    dict(n=5, hook='THEY SIT FOR FREE. NOBODY PAYS.', hook_until='yet', first=['G', 0], seed=550,
         overlays=[dict(type='chip', text='WHAT TO CHARGE PER CUT', icon='✓', word='charge', dur=2.4),
                   dict(type='chip', text='YOUR PRICE LIST, DONE', icon='✓', word='Instagram', dur=2.4),
                   dict(FIN=1, word='Sunday')]),
    dict(n=6, hook='NOBODY SAYS IT. THEY JUST GO.', hook_until='review', first=['C', 18], seed=660,
         overlays=[dict(type='chip', text='IT IS THE ORDER OF THE CUT', icon='✓', word='order', dur=2.4),
                   dict(type='chip', text='10 MISTAKES, LISTED', icon='✓', word='mistakes', dur=2.4),
                   dict(FIN=1, word='front')]),
]

for v in VIDEOS:
    pool, clips = pool_y_clips()
    ovs = []
    for o in v['overlays']:
        ovs.append(dict(FIN, word=o['word'], occ=o.get('occ', 0)) if o.get('FIN') else o)
    if not any(x[0] == v['first'][0] and x[1] == v['first'][1] for x in pool):
        raise SystemExit(f"V{v['n']}: el primer plano {v['first']} no esta en el pool. Tramos de {v['first'][0]}: "
                         + str([x[1] for x in pool if x[0] == v['first'][0]]))
    plan = dict(
        vo=f"vo/V{v['n']}.wav", script=f"V{v['n']}.txt", lang='en',
        speed=1.30, silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], words=2,
        music='music/bed.wav', music_db=-8,
        hi='&H000B9EF5&', capy=1380,
        hook=v['hook'], hook_until=v['hook_until'],
        first=v['first'], seed=v['seed'],
        clips=clips, pool=pool, anchors=v.get('anchors', []), overlays=ovs)
    json.dump(plan, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print(f"V{v['n']}.json  ({len(pool)} recortes de {len(clips)} clips)")
