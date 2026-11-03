# -*- coding: utf-8 -*-
"""Planes de los 6 ads de voz en off de Academia del Trazo (Argentina, 2026-11-03).
Uso: python3 gen_trazo_plans.py   -> escribe V1.json .. V6.json en ~/Desktop/dibujo-creativo/anuncios/work/"""
import os, json

WK = os.path.expanduser('~/Desktop/dibujo-creativo/anuncios/work')

# clip -> (inicio util, fin util, extras). Ventanas revisadas en hojas de contactos a 1 cuadro cada 2 s.
# Descartados por texto quemado o cara hablando a camara: 7605276822896446741 (sticker + manga), 7623671649505676565
# y 7676648338615242005 y 7692198175708417300 y 7052155341810699525 y 7667968137505148180 (subtitulos quemados),
# 7663499145914748167 (oscuro, teclado y glitches), 7672465939467635988 (cuadro estatico), 7673503911168298247
# (logo + PiP), 7673685935128694034 (craneos surrealistas), 7703569253064101142 y 7703926299793820950 (el autor
# hablando a camara), 7694123926099610893 (garabato infantil), 6926381029452205317 (fuente apaisada),
# 6847728580961537285 (sticker + dibujos a color).
VENT = {
    'A': (0, 32,  {}),                              # 7290714 retrato en cuaderno espiral, limpio de punta a punta
    'B': (0, 66,  {}),                              # 7514725 escena circular a lapiz, cenital, sin texto
    'C': (0, 30,  {}),                              # 7524925 retrato femenino, planos muy cerrados del lapiz
    'D': (4, 20,  {}),                              # 7270223 manzana realista (ventana sin los carteles del inicio y del final)
    'E': (24, 48, {}),                              # 7376438 retrato familiar (arranca despues del autor en camara)
    'F': (8, 24,  {}),                              # 7639583 perfil en cuaderno (ventana sin la placa del inicio)
    'G': (4, 12,  {}),                              # 7689652 cuaderno nuevo, AR (ventana entre los dos carteles)
    'H': (0, 38,  {}),                              # 7463613 retrato de un senor (sin el "dale like" del final)
    'I': (0, 52,  {}),                              # 7465892 retrato de una senora, limpio
    'J': (0, 58,  dict(zoom=1.30, ybias=1.0)),      # 7658232 mano paso a paso (recorte por el cartel de arriba)
    'K': (0, 60,  dict(zoom=1.30, ybias=1.0)),      # 7658959 mano con manzana (mismo cartel arriba)
    'L': (0, 68,  {}),                              # 7517317 rostro construido desde el circulo, limpio
    'M': (0, 90,  {}),                              # 7376491 retrato grande en atril, limpio
    'N': (0, 68,  {}),                              # 7329749 sombreado de rostro en primerisimo plano
    'O': (0, 42,  {}),                              # 7550631 retrato realista, planos cerrados
}
SRC = {'A': '7290714287776009478', 'B': '7514725669117414661', 'C': '7524925043365694725',
       'D': '7270223525473144070', 'E': '7376438372610477317', 'F': '7639583406728236308',
       'G': '7689652898581482772', 'H': '7463613509910203678', 'I': '7465892650797829406',
       'J': '7658232090349079822', 'K': '7658959106920811790', 'L': '7517317342662036741',
       'M': '7376491812879404294', 'N': '7329749534349839622', 'O': '7550631925598260487'}
# familias: varios clips del mismo creador cuentan como una sola fuente visual
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

FIN = dict(type='end', head=['ACADEMIA', 'DEL TRAZO'],
           sub='+200 PROYECTOS · PLAN DE 21 DÍAS',
           sub2='ACCESO DE POR VIDA · GARANTÍA DE 30 DÍAS',
           cta='Tocá en Más información 👇')

VIDEOS = [
    dict(n=1, hook='NO TE FALTA PULSO. TE FALTA ORDEN.', hook_until='mismo', first=['L',0],
         overlays=[dict(type='chip', text='FORMA · VOLUMEN · PIEL', icon='✓', word='capas', dur=2.4),
                   dict(type='chip', text='+200 PROYECTOS GUIADOS', icon='✓', word='doscientos', dur=2.4),
                   dict(FIN=1, word='Tocá')]),
    dict(n=2, hook='ESE CUADERNO ESTÁ POR LA MITAD.', hook_until='ganas', first=['A',0],
         overlays=[dict(type='chip', text='PLAN DE 21 DÍAS', icon='✓', word='veintiún', dur=2.4),
                   dict(type='chip', text='BLOQUES DE 20 MINUTOS', icon='✓', word='bloques', dur=2.4),
                   dict(FIN=1, word='Tocá')]),
    dict(n=3, hook='COPIANDO SALE. DE LA NADA, NO.', hook_until='ver.', first=['N',0],
         overlays=[dict(type='chip', text='DIBUJAR ES 90% MIRAR', icon='✓', word='noventa', dur=2.4),
                   dict(type='chip', text='DE MENOR A MAYOR DIFICULTAD', icon='✓', word='dificultad', dur=2.4),
                   dict(FIN=1, word='Tocá')]),
    dict(n=4, hook='ESTE REGALO NO SE COMPRA.', hook_until='mamá', first=['M',0],
         overlays=[dict(type='chip', text='EL PASO A PASO DEL ROSTRO', icon='✓', word='proporciones', dur=2.4),
                   dict(type='chip', text='+200 PROYECTOS GUIADOS', icon='✓', word='doscientos', dur=2.4),
                   dict(FIN=1, word='momento')]),
    dict(n=5, hook='20 MINUTOS SIN MIRAR UNA PANTALLA.', hook_until='dormir.', first=['G',4],
         overlays=[dict(type='chip', text='UN LÁPIZ Y UNA HOJA', icon='✓', word='hoja.', dur=2.4),
                   dict(type='chip', text='+200 PROYECTOS GUIADOS', icon='✓', word='doscientos', dur=2.4),
                   dict(FIN=1, word='Tocá')]),
    dict(n=6, hook='DÍA 1 Y DÍA 21. LA MISMA MANO.', hook_until='orden.', first=['B',0],
         overlays=[dict(type='chip', text='DÍA 1: LÍNEAS Y FORMAS', icon='✓', word='simples.', dur=2.4),
                   dict(type='chip', text='SEMANA 3: EL ROSTRO', icon='✓', word='rostro,', dur=2.4),
                   dict(FIN=1, word='Tocá')]),
]

for v in VIDEOS:
    pool, clips = pool_y_clips()
    ovs = [dict(FIN, word=o['word'], occ=o.get('occ', 0)) if o.get('FIN') else o for o in v['overlays']]
    first = v.get('first') or pool[v['n'] % len(pool)][:2]
    if not any(x[0] == first[0] and x[1] == first[1] for x in pool):
        raise SystemExit(f"V{v['n']}: el primer plano {first} no esta en el pool.")
    plan = dict(
        vo=f"vo/V{v['n']}.wav", script=f"V{v['n']}.txt", lang='es',
        speed=1.30, silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], words=2,
        music='music/bed.wav', music_db=-8,
        hi='&H004BB2F0&', capy=1380,
        hook=v['hook'], hook_until=v['hook_until'],
        first=first, seed=v['n'] * 110,
        clips=clips, pool=pool, anchors=v.get('anchors', []), overlays=ovs)
    json.dump(plan, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print(f"V{v['n']}.json  ({len(pool)} recortes de {len(clips)} clips)")
