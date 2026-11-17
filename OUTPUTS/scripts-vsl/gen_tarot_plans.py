"""Planes de los 6 ads de "Your First Tarot Reading in 2 Days" (mercado ingles, 2026-11-17).

Pool = clips de ambiente generados (manos, cartas, velas, mesa de nogal; ninguno con texto)
     + las tomas de producto de gfx_tarot.py (la pagina de la guia apoyada en la mesa con su carta).

El montaje clona el de Soyjulietacelis: ritmo calmo (cortes de 2 a 3 s), subtitulo blanco sin caja
con la palabra que suena mas grande, cierre fijo sobre la tapa del ebook y el inserto de cada carta
anclado a la palabra que la nombra.

Uso: python3 gen_tarot_plans.py <dir_work>
"""
import json, os, sys

WD = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser('~/Desktop/tarot-2-dias/anuncios/work')

# ---- clips de ambiente (5,04 s cada uno). Inicial unica = fuente distinta para el editor.
AMB = {
    'shu': 'ia/shuffle.mp4',   # manos barajando
    'dra': 'ia/draw.mp4',      # sacando una carta y apoyandola
    'thr': 'ia/three.mp4',     # tres cartas boca abajo, mano eligiendo
    'fan': 'ia/fan.mp4',       # abanico sobre la mesa
    'mes': 'ia/table.mp4',     # mesa con vela, cartas y lavanda, sin nadie
    'hoj': 'ia/pages.mp4',     # manos pasando hojas de un anillado
    'box': 'ia/box.mp4',       # el mazo cerrado en su caja, en el estante
    'jun': 'ia/gather.mp4',    # juntando y cuadrando las cartas
    'lap': 'ia/marker.mp4',    # subrayando con marcador
    'vel': 'ia/candle.mp4',    # macro de la vela, mazo desenfocado
    'cor': 'ia/cut.mp4',       # cortando el mazo en dos pilas
    'amb': 'ia/drift.mp4',     # paneo sobre la mesa con cuaderno, mazo y te
}
# ventanas solapadas: tres por clip, todas de 2,4 s
VENTANAS = [(0.20, 2.60), (1.30, 3.70), (2.40, 4.80)]

# ---- tomas de producto (fotos fijas con zoom). Todas con inicial "p" = una sola fuente.
PROD = {
    'pcov': 'ebook/shot_cover.jpg',
    'ptow': 'ebook/shot_tower.jpg',
    'pdea': 'ebook/shot_death.jpg',
    'pcup': 'ebook/shot_cups04.jpg',
    'pwan': 'ebook/shot_wands08.jpg',
    'ppen': 'ebook/shot_pents02.jpg',
    'pmag': 'ebook/shot_magician.jpg',
    'psta': 'ebook/shot_star.jpg',
    'pmoo': 'ebook/shot_moon.jpg',
}

clips, pool = {}, []
for k, src in AMB.items():
    clips[k] = {'src': src, 'fam': k}
    for a, b in VENTANAS:
        pool.append([k, a, b])
for k, src in PROD.items():
    clips[k] = {'src': src, 'still': True, 'fam': 'prod'}
    pool.append([k, 0.0, 6.0])

BASE = dict(
    lang='en',
    speed=1.20,                  # regla del 15/11
    silence=[0.26, 0.12],
    cut=[2.0, 2.5, 3.0],         # el ganador corta calmo, no a 1,9
    words=4,                     # sus frases son de 4-5 palabras en dos lineas
    music='music/bed.wav',
    music_db=-11,
    fsbase=74,                   # palabras que no suenan
    fshi=104,                    # la palabra que suena, mas grande (su resalte es por tamano)
    capy=1250,
    usage='usage.json',
    whoosh=[],
    overlays=[],
    clips=clips,
    pool=pool,
    last='pcov',                 # cierra siempre sobre la tapa, como ellos
)

VIDEOS = {
    # V1 - The Tower leida en orden (1:08 del ganador)
    'V1': dict(first=['dra', 0.20], seed=101, anchors=[
        ['tower', 0, 'ptow', 0.0],
        ['symbols', 0, 'pmoo', 0.0],
        ['seventy-eight', 0, 'psta', 0.0],
    ]),   # 'last' ya cierra con la tapa: no se le ancla pcov tambien
    # V2 - Death no significa que alguien se muere (0:39)
    'V2': dict(first=['vel', 0.20], seed=202, anchors=[
        ['Death', 0, 'pdea', 0.0],
        ['guide', 0, 'pdea', 0.0],
        ['cards', 0, 'pmag', 0.0],
    ]),
    # V3 - Pick a card: one, two or three (0:57)
    'V3': dict(first=['thr', 0.20], seed=303, anchors=[
        ['Cups', 0, 'pcup', 0.0],
        ['Wands', 0, 'pwan', 0.0],
        ['Pentacles', 0, 'ppen', 0.0],
        ['guide', 0, 'pcov', 0.0],
    ]),
    # V4 - El mazo que sigue en la caja (0:33)
    'V4': dict(first=['box', 0.20], seed=404, anchors=[
        ['guide', 0, 'pmag', 0.0],
        ['symbols', 0, 'psta', 0.0],
    ]),
    # V5 - Lo que me hubiese gustado tener (0:31)
    'V5': dict(first=['amb', 0.20], seed=505, anchors=[
        ['guide', 0, 'pmag', 0.0],
        ['Arcana', 0, 'pmoo', 0.0],
    ]),
}

os.makedirs(WD, exist_ok=True)
for v, extra in VIDEOS.items():
    p = dict(BASE)
    p['vo'] = f'voz/{v}.wav'
    p['script'] = f'txt/{v}.txt'
    p.update(extra)
    with open(os.path.join(WD, f'{v}.json'), 'w') as f:
        json.dump(p, f, ensure_ascii=False, indent=1)
    print(v, 'ok')
print('pool:', len(pool), 'ventanas ·', len(clips), 'fuentes')
