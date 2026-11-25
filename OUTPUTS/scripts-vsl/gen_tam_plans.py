# -*- coding: utf-8 -*-
"""Planes de los 6 ads de voz en off de The Artist Method (mercado ingles, 2026-11-25).
Modelada del ganador argentino Metodo Artista (metododibujar.online): mismo formato de video
(b-roll de manos dibujando a lapiz + voz en off calma + subtitulos de 2 palabras con la activa en
ambar + chips terracota) y sus angulos ganadores. Mismo pool de 15 clips de TikTok que
Academia del Trazo / The Drawing World (ventanas y vetos ya revisados).
Uso: python3 gen_tam_plans.py   -> escribe V1.json .. V6.json en ~/Desktop/the-artist-method/anuncios/work/"""
import os, json, wave

WK = os.path.expanduser('~/Desktop/the-artist-method/anuncios/work')

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
TOPE = 8
PPM = 178.0   # ritmo final objetivo: la banda que valido Santiago el 24/11 (167-188 ppm)


def velocidad(n):
    """Speed por video para que el montaje final caiga en PPM.
    El estilo de voz del 25/11 lee entre 145 y 211 ppm en crudo segun el guion, asi que un
    speed fijo (el 1.20 de la regla) deja unos arrastrados y otros atropellados. Medido:
    a speed 1.00 el final sale a 0.988 del crudo (el editor recorta silencios)."""
    w = wave.open(f'{WK}/vo/V{n}.wav')
    crudo = len(open(f'{WK}/V{n}.txt').read().split()) / (w.getnframes() / w.getframerate()) * 60
    return round(min(1.30, max(0.84, PPM / (crudo * 0.988))), 2)


def pool_y_clips():
    pool, clips = [], {}
    for k, (a, b, ex) in VENT.items():
        clips[k] = dict(src=f'tiktoks/{SRC[k]}.mp4', fam=FAM[k], **ex)
        tramos, t = [], a
        while t < b - 1.8:
            tramos.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
        if len(tramos) > TOPE:
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    return pool, clips


FIN = dict(type='end', head=['THE ARTIST', 'METHOD'],
           sub='220 STEP-BY-STEP PROJECTS · 8 LEVELS',
           sub2='5 BONUSES FREE TODAY · INSTANT ACCESS',
           cta='Tap Learn more 👇')

VIDEOS = [
    # 1 - el ritual de la noche (su angulo nº1: 4 de sus 5 ads de mas impresiones)
    dict(n=1, hook='PUT THE PHONE DOWN. PICK UP A PENCIL.', hook_until='paper', first=['L', 0],
         overlays=[dict(type='chip', text='SHAPES → OUTLINE → SHADOWS', icon='✓', word='shadows', dur=2.4),
                   dict(type='chip', text='200+ PROJECTS IN 8 LEVELS', icon='✓', word='levels', dur=2.4),
                   dict(FIN=1, word='Tap')],
         sfx=[['papel', 'projects', 0]]),
    # 2 - el contraste: media hora de pantalla contra diez minutos de lapiz
    dict(n=2, hook='THE SCREEN SPEEDS YOU UP. THE PENCIL SLOWS YOU DOWN.', hook_until='off', first=['N', 0],
         overlays=[dict(type='chip', text='NO NOTIFICATIONS. JUST THE PAPER.', icon='✓', word='news', dur=2.4),
                   dict(type='chip', text='200+ PROJECTS IN 8 LEVELS', icon='✓', word='levels', dur=2.4),
                   dict(FIN=1, word='Tap')],
         sfx=[['papel', 'projects', 0]]),
    # 3 - el paisaje / diez minutos de paz (su angulo nº2)
    dict(n=3, hook='TEN QUIET MINUTES', hook_until='horizon', first=['B', 0],
         overlays=[dict(type='chip', text='EVERY STROKE ALREADY DRAWN FOR YOU', icon='✓', word='shadows', dur=2.4),
                   dict(type='chip', text='FLOWERS · ANIMALS · LANDSCAPES · FACES', icon='✓', word='faces', dur=2.4),
                   dict(FIN=1, word='Tap')],
         sfx=[['papel', 'projects', 0]]),
    # 4 - el peor consejo: "practica todos los dias" (su unico angulo de metodo/logica)
    dict(n=4, hook='THE WORST ADVICE: “JUST PRACTICE EVERY DAY”', hook_until='mistakes', first=['L', 13.5],
         overlays=[dict(type='chip', text='THE ORDER IS THE METHOD', icon='✓', word='steps', dur=2.4),
                   dict(type='chip', text='200+ PROJECTS IN THAT EXACT ORDER', icon='✓', word='order', occ=1, dur=2.4),
                   dict(FIN=1, word='Tap')],
         sfx=[['papel', 'projects', 0]]),
    # 5 - nunca es tarde (sus angulos nº3 y nº4 fundidos en la linea mas fuerte)
    dict(n=5, hook='NOBODY ASKS IF IT IS TOO LATE TO WALK', hook_until='going', first=['M', 0],
         overlays=[dict(type='chip', text='IT ISN’T TALENT. IT’S THE ORDER.', icon='✓', word='first', dur=2.4),
                   dict(type='chip', text='A PENCIL, PAPER, 15 MINUTES A DAY', icon='✓', word='minutes', dur=2.4),
                   dict(FIN=1, word='Tap')],
         sfx=[['papel', 'projects', 0]]),
    # 6 - angulo nuevo, sacado del mercado ingles (Pigment & Papier, Japanese Doodling Class):
    #     "nunca supiste por donde empezar" + "lo primero en anos de lo que estas orgullosa"
    dict(n=6, hook='YOU NEVER KNEW WHERE TO START', hook_until='order', first=['I', 0],
         overlays=[dict(type='chip', text='THE NEXT LINE IS ALREADY DRAWN', icon='✓', word='next', dur=2.4),
                   dict(type='chip', text='8 LEVELS, FROM LINE ONE TO REALISM', icon='✓', word='realism', dur=2.4),
                   dict(FIN=1, word='Tap')],
         sfx=[['papel', 'projects', 0]]),
]

for v in VIDEOS:
    pool, clips = pool_y_clips()
    ovs = [dict(FIN, word=o['word'], occ=o.get('occ', 0)) if o.get('FIN') else o for o in v['overlays']]
    first = v.get('first') or pool[v['n'] % len(pool)][:2]
    if not any(x[0] == first[0] and abs(x[1] - first[1]) < 0.01 for x in pool):
        raise SystemExit(f"V{v['n']}: el primer plano {first} no esta en el pool.")
    plan = dict(
        vo=f"vo/V{v['n']}.wav", script=f"V{v['n']}.txt", lang='en',
        speed=velocidad(v['n']), silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], words=2,
        music='music/bed.wav', music_db=-11,
        hi='&H004BB2F0&', capy=1380,
        hook=v['hook'], hook_until=v['hook_until'],
        first=first, seed=v['n'] * 110,
        clips=clips, pool=pool, anchors=v.get('anchors', []),
        sfx=v.get('sfx', []), overlays=ovs)
    json.dump(plan, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print(f"V{v['n']}.json  ({len(pool)} recortes de {len(clips)} clips)")
