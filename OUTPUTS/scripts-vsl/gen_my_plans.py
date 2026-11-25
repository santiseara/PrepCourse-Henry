# -*- coding: utf-8 -*-
"""Planes de los 6 ads de Mini Plaster Studio (mercado ingles, 2026-11-25).
Modelada del ganador argentino Mini Yesitos para Pintar / Creaciones con Alma
(miniyesitos.brujulanegocios.com, ~61 ads activos): mismo formato de video (b-roll real de manos
colando yeso, desmoldando y armando kits + voz en off de mujer + subtitulos de 2 palabras con la
palabra que suena en PASTILLA FUCSIA + tarjetas crema con el numero) y sus angulos ganadores.
Uso: python3 gen_my_plans.py   -> escribe V1.json .. V6.json en ~/Desktop/mini-yesitos/anuncios/work/"""
import os, json, wave, importlib.util

WK = os.path.expanduser('~/Desktop/mini-yesitos/anuncios/work')
spec = importlib.util.spec_from_file_location('v', os.path.join(WK, 'vent_yesitos.py'))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
VENT = m.VENT

SEG = 3.6      # el ganador corta rapido: planos de 3-4 s
TOPE = 7
PPM = 178.0    # ritmo final objetivo (banda validada por Santiago: 167-188)


def velocidad(n):
    w = wave.open(f'{WK}/vo/V{n}.wav')
    crudo = len(open(f'{WK}/V{n}.txt').read().split()) / (w.getnframes() / w.getframerate()) * 60
    return round(min(1.30, max(0.84, PPM / (crudo * 0.988))), 2)


def pool_y_clips():
    pool, clips = [], {}
    for k, v in VENT.items():
        vid, a, b = v[0], v[1], v[2]
        ex = v[3] if len(v) > 3 else {}
        clips[k] = dict(src=f'tiktoks/{vid}.mp4', fam=vid, **ex)
        tramos, t = [], a
        while t < b - 1.6:
            tramos.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
        if len(tramos) > TOPE:
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    return pool, clips


FIN = dict(type='end', head=['MINI PLASTER', 'STUDIO'],
           sub='30 COLLECTIONS · 50 KIT IDEAS',
           sub2='5 BONUSES FREE TODAY · 30-DAY GUARANTEE',
           cta='Tap Learn more 👇')

VIDEOS = [
    # 1 - packaging y valor percibido (SU angulo nº1: los 3 ads de mas impresiones lo corren)
    dict(n=1, hook='SAME FIVE FIGURES. ONE BAG SELLS FOR TRIPLE.', hook_until='bags',
         overlays=[dict(type='card', big='$4', small='PLAIN BAG', word='four', dur=2.2),
                   dict(type='card', big='$12', small='COLORS · BAG · TAG', word='twelve', dur=2.4),
                   dict(type='chip', text='30 COLLECTIONS · 50 KIT COMBINATIONS', icon='✓', word='collections', dur=2.4),
                   dict(FIN=1, word='Tap')],
         sfx=[['chaching', 'twelve', 0]]),
    # 2 - packs de 30 y de 50 + la cuenta de los materiales (SU angulo nº2)
    dict(n=2, hook='THEY DO NOT SELL ONE AT A TIME. THEY SELL THIRTY.', hook_until='sell',
         overlays=[dict(type='card', big='4', small='MOLDS TO START', word='Four', dur=2.2),
                   dict(type='card', big='1', unit='BAG', small='DOZENS OF FIGURES', word='dozens', dur=2.4),
                   dict(type='chip', text='PAINTS + BRUSH INCLUDED', icon='✓', word='brush', dur=2.2),
                   dict(FIN=1, word='Tap')],
         sfx=[['chaching', 'margin', 0]]),
    # 3 - el souvenir que no se tira / un cumple por fin de semana (SU angulo nº6 + el ingles)
    dict(n=3, hook='THE PARTY FAVOR THAT DOES NOT END UP IN THE BIN', hook_until='weekend',
         overlays=[dict(type='card', big='30', small='FAVORS PER PARTY', word='thirty', dur=2.4),
                   dict(type='chip', text='HANDMADE · KEEPS THEM OFF THE SCREEN', icon='✓', word='screen', dur=2.4),
                   dict(FIN=1, word='Tap')],
         sfx=[['pop', 'thirty', 0]]),
    # 4 - Navidad (SU angulo nº4, y la mejor ventana del ano en el mercado ingles)
    dict(n=4, hook='29 DAYS TO CHRISTMAS. ONE ORDER IS THIRTY KITS.', hook_until='away',
         overlays=[dict(type='card', big='29', small='DAYS TO CHRISTMAS', word='days', dur=2.4),
                   dict(type='chip', text='TREE · SNOWMAN · STAR · GIFT', icon='✓', word='gift', dur=2.4),
                   dict(FIN=1, word='Tap')],
         # el pool no sabe de Navidad: se fuerzan los dos planos del clip con arbolitos y copos
         anchors=[['tree', 0, 'c33', 6.4], ['snowman', 0, 'c33', 10.0]],
         sfx=[['ding', 'gift', 0]]),
    # 5 - "necesito 25 kits para el sabado, cuanto?" (SU angulo nº7)
    dict(n=5, hook='“I NEED 25 KITS BY SATURDAY. HOW MUCH?”', hook_until='tomorrow',
         overlays=[dict(type='card', big='25', small='KITS BY SATURDAY', word='Saturday', dur=2.4),
                   dict(type='chip', text='PRICE TABLES · QUOTE TEMPLATES', icon='✓', word='templates', dur=2.4),
                   dict(FIN=1, word='Tap')],
         sfx=[['llamada', 'messages', 0]]),
    # 6 - los 3 pasos del acabado (SU unico angulo de mecanismo, y el hueco del mercado ingles)
    dict(n=6, hook='IT IS NOT THE MOLD. IT IS THE FINISH.', hook_until='finish',
         overlays=[dict(type='chip', text='1 · THIN STREAM · TAP · TOOTHPICK', icon='✓', word='toothpick', dur=2.4),
                   dict(type='chip', text='2 · DEMOLD COOL AND FIRM', icon='✓', word='firm', dur=2.4),
                   dict(type='chip', text='3 · FULL CURE · FINE SANDPAPER', icon='✓', word='sandpaper', dur=2.4),
                   # occ=1: el guion dice "tap the mold on the table" antes del CTA, y con occ=0 la
                   # placa final arrancaba a los 20 s y se comia dos chips
                   dict(FIN=1, word='Tap', occ=1)],
         sfx=[['tick', 'toothpick', 0]]),
]

for v in VIDEOS:
    pool, clips = pool_y_clips()
    ovs = [dict(FIN, word=o['word'], occ=o.get('occ', 0)) if o.get('FIN') else o for o in v['overlays']]
    first = pool[(v['n'] * 7) % len(pool)][:2]
    plan = dict(
        vo=f"vo/V{v['n']}.wav", script=f"V{v['n']}.txt", lang='en',
        speed=velocidad(v['n']), silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], words=2,
        music='music/bed.wav', music_db=-9,    # 25/11: su pista de Pixabay. El editor mide la voz entera, no solo el habla:
        # a -9 la musica queda 13 dB por debajo del habla real (Santiago, 25/11: "bajale un poco")
        hi='&H00B857EE&', capy=1390,
        hook=v['hook'], hook_until=v['hook_until'],
        first=first, seed=v['n'] * 110,
        clips=clips, pool=pool, anchors=v.get('anchors', []),
        sfx=v.get('sfx', []), overlays=ovs)
    json.dump(plan, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print(f"V{v['n']}.json  ({len(pool)} recortes de {len(clips)} clips)")
