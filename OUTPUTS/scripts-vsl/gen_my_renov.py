# -*- coding: utf-8 -*-
"""Planes de las 4 RENOVACIONES de Mini Plaster Studio (mercado ingles, 2026-11-26).

Despues de la primera tanda, el ganador de la cuenta es el Guion 4 ("29 days to Christmas",
CJTO 3, $10,77 de CPA). Santiago pidio hooks mas virales y organicos: el CUERPO del 4 no se
toca y solo cambia el hook. Mismo formato medido del ganador (b-roll real, subtitulo de 2
palabras con la que suena en pastilla fucsia #EE57B8, tarjetas crema, placa final) y misma voz
de mujer (Sulafat).

Uso: python3 gen_my_renov.py   -> escribe R1.json .. R4.json en ~/Desktop/mini-yesitos/anuncios/work/
"""
import os, json, wave, importlib.util

WK = os.path.expanduser('~/Desktop/mini-yesitos/anuncios/work')
spec = importlib.util.spec_from_file_location('v', os.path.join(WK, 'vent_yesitos.py'))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
VENT = m.VENT

SEG = 3.6      # el ganador corta rapido: planos de 3-4 s
TOPE = 7
PPM = 178.0    # ritmo final objetivo (banda validada por Santiago: 167-188)


def velocidad(n):
    w = wave.open(f'{WK}/vo/R{n}.wav')
    crudo = len(open(f'{WK}/R{n}.txt').read().split()) / (w.getnframes() / w.getframerate()) * 60
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

# el cuerpo es el mismo en los 4: la tarjeta del 29, el chip de las 4 figuras y la placa final
# cuelgan siempre de las mismas palabras. Lo unico propio de cada uno es el hook.
COMUN = [dict(type='chip', text='TREE · SNOWMAN · STAR · GIFT', icon='✓', word='gift', dur=2.4),
         dict(FIN=1, word='Tap')]
ANCL = [['tree', 0, 'c33', 6.4], ['snowman', 0, 'c33', 10.0]]

VIDEOS = [
    # 1 - la cuenta que no cierra en la cabeza: una bolsa de 5 dolares = 40 adornos
    dict(n=1, first='c04', first_t=3.4, hook='A $5 BAG POURS 40 ORNAMENTS', hook_until='them',
         overlays=[dict(type='card', big='40', small='ORNAMENTS PER BAG', word='Forty', occ=1, dur=2.2),
                   dict(type='card', big='29', small='DAYS LEFT TO SELL THEM', word='nine', dur=2.4)] + COMUN,
         sfx=[['chaching', 'Forty', 1], ['ding', 'gift', 0]]),
    # 2 - el mensaje que te va a llegar (la escena antes de la venta)
    dict(n=2, first='c10', first_t=20.6, hook='SOMEBODY IS ABOUT TO ASK YOU', hook_until='gifts',
         overlays=[dict(type='card', big='29', small='DAYS TO CHRISTMAS', word='nine', dur=2.4)] + COMUN,
         sfx=[['llamada', 'phone', 0], ['ding', 'gift', 0]]),
    # 3 - la opinion fuerte (el juguete de plastico que en enero esta en la basura)
    dict(n=3, first='c21', first_t=7.0, hook='IN THE BIN BY JANUARY', hook_until='January',
         overlays=[dict(type='card', big='29', small='DAYS TO CHRISTMAS', word='nine', dur=2.4)] + COMUN,
         sfx=[['pop', 'January', 0], ['ding', 'gift', 0]]),
    # 4 - lo que todos estan mirando mal (todos venden adornos, nadie vende el que el chico pinta)
    dict(n=4, first='c32', first_t=15.6, hook='EVERYONE SELLS ORNAMENTS. NOBODY SELLS THIS.', hook_until='themselves',
         overlays=[dict(type='card', big='29', small='DAYS TO CHRISTMAS', word='nine', dur=2.4)] + COMUN,
         sfx=[['ding', 'gift', 0]]),
]

for v in VIDEOS:
    pool, clips = pool_y_clips()
    ovs = [dict(FIN, word=o['word'], occ=o.get('occ', 0)) if o.get('FIN') else o for o in v['overlays']]
    # 26/11: el plano de apertura elegido a ojo (el automatico le daba a R1 un cuadro negro)
    first = next([s[0], s[1]] for s in pool if s[0] == v['first'] and s[1] == v['first_t'])
    plan = dict(
        vo=f"vo/R{v['n']}.wav", script=f"R{v['n']}.txt", lang='en',
        speed=velocidad(v['n']), silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], words=2,
        music='music/bed.wav', music_db=-9,
        hi='&H00B857EE&', capy=1390,
        hook=v['hook'], hook_until=v['hook_until'],
        first=first, seed=1300 + v['n'] * 37,
        usage='usage_r.json',        # 26/11: compartido entre las 4, para que no se repitan planos
        clips=clips, pool=pool, anchors=ANCL,
        sfx=v.get('sfx', []), overlays=ovs)
    json.dump(plan, open(f"{WK}/R{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print(f"R{v['n']}.json  speed {plan['speed']}  first {first}  ({len(pool)} recortes de {len(clips)} clips)")
