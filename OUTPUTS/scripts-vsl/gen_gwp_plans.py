# -*- coding: utf-8 -*-
"""Genera los 6 plan.json de The Group Work Playbook para edit_gwp.py.
Uso:  cd ~/Desktop/the-group-work-playbook/anuncios/work && python3 gen_gwp_plans.py
Montar: for n in 1 2 3 4 5 6; do python3 edit_gwp.py plans/V$n.json ../GWP-V$n.mp4; done

Insumos (todos gratis, sin créditos):
  vo/V1.wav..V6.wav  <- voz en off, Google AI Studio (Gemini 3.1 Flash TTS Preview, voz Sulafat)
  broll/*.mp4        <- stock gratuito de mixkit, curado a mano
  ../../landing/*.webp <- stills de la propia landing
"""
import json, os

LAND = '../../../landing/'   # relativo a plans/, que es donde el editor resuelve las rutas
# L00 mockup del producto + bonos · L01 ficha "Three chairs" (con care notes) · L02 índice módulo 1 (las 25)
# L03 ficha "The wheel of my week" · L04 taller 1 de 12, minuto a minuto · L05 worksheet "Body map"
STILLS = {f'L{i:02d}': {'src': f'{LAND}img{i:02d}.webp', 'still': True, 'fit': i > 0} for i in range(6)}

# b-roll curado. ybias 1 = al recortar a 9:16 se queda con la parte de abajo
B = {
 'ronda_sentados': 'mk116', 'ronda_parados': 'mk124', 'circulo_charla': 'mk128',
 'circulo_abajo':  'mk133', 'manos_mesa':    'mk129', 'taller_mesa':   'mk130',
 'jovenes_ventana':'mk106', 'rotafolio_mujer':'mk135','rotafolio_sala':'mk07',
 'reunion_mesa':   'mk08',  'equipo_mesa':   'mk114', 'equipo_cenital':'mk19',
 'oficina_grupo':  'mk123', 'reunion_3':     'mk113', 'aula_chicos':   'mk02',
 'aula_adultos':   'mk10',  'aula_docente':  'mk20',  'aula_ninos':    'mk25',
 'pizarra_welcome':'mk21',  'estudiante':    'mk18',  'mujer_pensando':'mk12',
 'mujer_angustia': 'mk17',  'mujer_seria':   'mk134', 'mujer_papel':   'mk103',
 'cuaderno':       'mk22',  'escritorio':    'mk23',  'firma':         'mk105',
 'manos_plan':     'mk110',
}
CLIPS = dict(STILLS)
for name, f in B.items():
    CLIPS[name] = {'src': f'../broll/{f}.mp4'}

TAG = 'FOR PSYCHOLOGISTS & COUNSELLORS'
CHIP = '+150 READY-TO-RUN ACTIVITIES'

# por video: hook, los b-roll que le tocan, los stills anclados a una palabra del guion
V = {
 1: dict(hook='BUILD YOUR FIRST WORKSHOP IN ONE MORNING',
         broll=['ronda_sentados', 'taller_mesa', 'pizarra_welcome', 'circulo_abajo', 'ronda_parados', 'circulo_charla'],
         anchors=[['index', 0, 'L02', 1], ['step', 0, 'L01', 1], ['proposal', 0, 'L00', 1]],
         tag_word='Building', chip_word='Playbook'),
 2: dict(hook='THE SCHOOL JUST CALLED. WHAT DO YOU BRING?',
         broll=['aula_ninos', 'aula_docente', 'aula_chicos', 'mujer_pensando', 'pizarra_welcome', 'circulo_charla'],
         anchors=[['index', 0, 'L02', 1], ['workshop', 1, 'L04', 1], ['proposal', 0, 'L00', 1]],
         tag_word='school', chip_word='Playbook'),
 3: dict(hook='A WELLBEING CIRCLE, RUN BY YOU',
         broll=['circulo_charla', 'circulo_abajo', 'ronda_parados', 'mujer_seria', 'ronda_sentados', 'taller_mesa'],
         anchors=[['activities', 0, 'L03', 1], ['care', 0, 'L01', 1], ['module', 0, 'L00', 1]],
         tag_word='women', chip_word='Playbook'),
 4: dict(hook='ONE PERSON AN HOUR, OR TEN',
         broll=['ronda_sentados', 'mujer_pensando', 'taller_mesa', 'pizarra_welcome', 'circulo_charla', 'escritorio'],
         anchors=[['activities', 0, 'L02', 1], ['workshops', 0, 'L04', 1], ['structure', 0, 'L00', 1]],
         tag_word='hour', chip_word='Playbook'),
 5: dict(hook="BULLYING DOESN'T STOP WITH A TALK",
         broll=['aula_ninos', 'estudiante', 'aula_chicos', 'aula_adultos', 'pizarra_welcome', 'ronda_parados'],
         anchors=[['module', 0, 'L02', 1], ['care', 0, 'L01', 1], ['workshop', 0, 'L04', 1]],
         tag_word='Bullying', chip_word='Playbook'),
 6: dict(hook='150 ACTIVITIES, A WHOLE YEAR',
         broll=['circulo_abajo', 'ronda_sentados', 'taller_mesa', 'aula_ninos', 'cuaderno', 'circulo_charla'],
         anchors=[['modules', 0, 'L02', 1], ['index', 0, 'L03', 1], ['worksheets', 0, 'L05', 1]],
         tag_word='hundred', chip_word='Playbook'),
}

os.makedirs('plans', exist_ok=True)
for n, c in V.items():
    stills_usados = sorted({a[2] for a in c['anchors']})
    # solo el primer tramo de cada b-roll: mas adelante los clips cambian de escena.
    # el peso lo lleva el producto, como en los ganadores del competidor.
    pool = [[k, 0, 4.5] for k in c['broll']] \
         + [[k, 0, 4.2] for k in stills_usados] + [[k, 0, 3.4] for k in stills_usados] \
         + [[k, 0, 3.0] for k in stills_usados]
    P = {
        'vo': f'../vo/V{n}.wav', 'script': f'../vo/V{n}.txt', 'speed': 1.0, 'lang': 'en',
        'clips': CLIPS, 'pool': pool, 'seed': n, 'usage': '../usage.json',
        'cut': [2.6, 3.4, 4.2],
        'capy': 1440, 'words': 4, 'progress': True,
        'music': f'../music/bed_{"ABC"[(n-1)%3]}.wav', 'music_db': -16,
        'hook': c['hook'],
        'anchors': c['anchors'],
        'first': [c['broll'][0], 0],   # el plano de apertura de cada video
        'whoosh': [1, 3, 5, 7],
        'sfx': [['pop', 'Tap', 0]],
        'overlays': [
            {'type': 'tag',  'text': TAG,  'at': 0.0,  'dur': 3.4},
            {'type': 'chip', 'text': CHIP, 'at': 0.25, 'dur': 3.15, 'icon': '\U0001F447', 'y': 1020},
            {'type': 'chip', 'text': CHIP, 'word': c['chip_word'], 'dur': 2.4, 'y': 1600},
            {'type': 'end',  'word': 'Tap',
             'title': ['THE GROUP WORK', 'PLAYBOOK'],
             'sub': '150+ ACTIVITIES · 12 WORKSHOPS',
             'sub2': 'INSTANT PDF · 30-DAY GUARANTEE',
             'cta': 'Tap Learn More 👇'},
        ],
    }
    json.dump(P, open(f'plans/V{n}.json', 'w'), ensure_ascii=False, indent=1)
    print(f'plans/V{n}.json  {len(c["broll"])} b-roll + {len(stills_usados)} stills  |  {c["hook"]}')

falta = [f'vo/V{n}.wav' for n in V if not os.path.exists(f'vo/V{n}.wav')]
print('\nFALTA la voz: ' + ', '.join(falta) if falta else '\nTodo listo para montar.')
