"""Planes de los 2 ads de VOZ EN OFF de Skool AI, version 100% B-roll (30/10/2026).
Regla de Santiago: "no quiero imagenes, quiero que todo sea B-roll". Ningun plano es foto:
las paginas del indice pasaron a ser PLACAS DE TEXTO con el badge naranja encima del clip.
Uso: python3 gen_skool_vo_plans.py <carpeta_scratch_skool>
"""
import json, os, sys
B = sys.argv[1]
MUS = os.path.expanduser('~/Desktop/skool-ai/anuncios/work/music/bed_herrero.wav')

# el pool: cada entrada es un tramo concreto de un clip de TikTok (ss = desde que segundo)
C = 'tt/ok/'
POOL = {
    # --- oficina de contabilidad real, con papeles (bookkeeping_004, 102 s)
    'papeles':    {'src': C + 'bookkeeping_004.mp4', 'ss': 12.0},
    'papel_mano': {'src': C + 'bookkeeping_004.mp4', 'ss': 19.5},
    'firma':      {'src': C + 'bookkeeping_004.mp4', 'ss': 45.5},
    'escritorio': {'src': C + 'bookkeeping_004.mp4', 'ss': 70.0},
    'trabajando': {'src': C + 'bookkeeping_004.mp4', 'ss': 86.5},
    # --- planilla en la laptop, en ingles (bookkeeping_002; recorte abajo por el cartel quemado)
    'planilla':   {'src': C + 'bookkeeping_002.mp4', 'ss': 62.0, 'zoom': 1.45, 'ybias': 0.0},
    'planilla2':  {'src': C + 'bookkeeping_002.mp4', 'ss': 72.0, 'zoom': 1.45, 'ybias': 0.0},
    # --- escritorio con agenda y teclado (adminwork_043, 50 s)
    'agenda':     {'src': C + 'adminwork_043.mp4', 'ss': 5.5},
    'tecla':      {'src': C + 'adminwork_043.mp4', 'ss': 22.5},
    'tecla2':     {'src': C + 'adminwork_043.mp4', 'ss': 30.5},
    # --- el mostrador y el escritorio de oficina (adminwork_044, 63 s)
    'mostrador':  {'src': C + 'adminwork_044.mp4', 'ss': 16.5},
    'oficina':    {'src': C + 'adminwork_044.mp4', 'ss': 23.0},
    # --- otra oficina, persona trabajando (adminwork_042, 64 s)
    'oficina2':   {'src': C + 'adminwork_042.mp4', 'ss': 18.0},
    'manos':      {'src': C + 'adminwork_042.mp4', 'ss': 49.5},
    # --- carpetas colgantes con separadores de colores (filing_066 / filing_061 / filing_067)
    'separadores':{'src': C + 'filing_066.mp4', 'ss': 2.5},
    'archivo':    {'src': C + 'filing_061.mp4', 'ss': 8.0},
    'depo':       {'src': C + 'filing_067.mp4', 'ss': 9.0},
    # --- talonarios de facturas que se hojean (invoice_024 / invoice_030)
    'facturas':   {'src': C + 'invoice_024.mp4', 'ss': 0.5},
    'facturas2':  {'src': C + 'invoice_024.mp4', 'ss': 8.0},
    'talonario':  {'src': C + 'invoice_030.mp4', 'ss': 2.5},
    'talonario2': {'src': C + 'invoice_030.mp4', 'ss': 10.5},
    # --- de la tanda anterior, los que Santiago aprobo
    'pila':       {'src': C + 'accounting_002.mp4', 'ss': 66.0},
    'hoja':       {'src': C + 'accounting_002.mp4', 'ss': 21.0},
    'carpeta':    {'src': C + 'paperwork_024.mp4', 'ss': 0.6},
    'teclado':    {'src': C + 'typing_033.mp4', 'ss': 0.4},
}

V5 = {
    'vo': 'vo/V5.wav', 'script': 'V5.txt', 'speed': 1.30, 'silence': [0.26, 0.12], 'lang': 'en',
    'hook': 'This guide has a path for your job', 'hook_dur': 3.4,
    'pages': POOL,
    'shots': [
        [None,       0, 'facturas'],
        ['files',    0, 'papeles',  {'badge': 18, 'head': 'Ask about your own files'}],
        ['inbox',    0, 'tecla',    {'badge': 24, 'head': 'Your inbox, in your own words'}],
        ['report',   0, 'archivo',  {'badge': 38, 'head': 'Build it once, reuse it forever'}],
        ['Never',    0, 'oficina2', {'badge': 7,  'head': 'Start from absolute zero'}],
        ['Whatever', 0, 'pila'],
    ],
    'end': {'sub': '7 days · 15 min a day · instant download', 'cta': 'Tap Learn More 👇'},
    'end_dur': 2.4, 'music': MUS, 'music_db': -8, 'capy': 1430,
}

V6 = {
    'vo': 'vo/V6.wav', 'script': 'V6.txt', 'speed': 1.30, 'silence': [0.26, 0.12], 'lang': 'en',
    'hook': '15 minutes a day · 7 days', 'hook_dur': 3.4,
    'pages': POOL,
    'shots': [
        [None,      0, 'papel_mano'],
        ['counter', 0, 'mostrador'],
        ['desk',    0, 'oficina2'],
        ['zero',    0, 'agenda',      {'head': 'It starts at zero'}],
        ['split',   0, 'separadores'],
        ['replies', 0, 'trabajando'],
        ['payment', 0, 'talonario'],
    ],
    'end': {'sub': 'One payment · instant download · 7-day guarantee', 'cta': 'Get the guide 👇'},
    'end_dur': 2.4, 'music': MUS, 'music_db': -8, 'capy': 1430,
}

for name, P in (('plan_V5.json', V5), ('plan_V6.json', V6)):
    json.dump(P, open(os.path.join(B, name), 'w'), indent=1, ensure_ascii=False)
    print(name, len(P['shots']), 'planos')
