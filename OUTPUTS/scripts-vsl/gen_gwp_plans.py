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
 1: dict(hook='A WHOLE YEAR WITHOUT REPEATING ONE ACTIVITY',
         broll=['ronda_sentados', 'ronda_parados', 'circulo_charla', 'circulo_abajo', 'jovenes_ventana', 'manos_mesa'],
         anchors=[['twenty-five', 0, 'L02', 1], ['sheet', 0, 'L01', 1], ['hundred', 0, 'L00', 1]],
         tag_word='Every', chip_word='icebreakers'),
 2: dict(hook='THE PROPOSAL A COMPANY SAYS YES TO',
         broll=['rotafolio_mujer', 'rotafolio_sala', 'reunion_mesa', 'equipo_mesa', 'equipo_cenital', 'firma'],
         anchors=[['proposal', 0, 'L00', 1], ['workplace', 0, 'L03', 1], ['teams', 0, 'L04', 1]],
         tag_word='company', chip_word='module'),
 3: dict(hook='ONE ACTIVITY YOU CAN RUN TOMORROW, FREE',
         broll=['ronda_sentados', 'pizarra_welcome', 'circulo_charla', 'ronda_parados', 'cuaderno', 'manos_plan'],
         anchors=[['Agreement', 0, 'L02', 1], ['sheet', 0, 'L01', 1], ['forty-nine', 1, 'L00', 1]],
         tag_word='Here', chip_word='Playbook'),
 4: dict(hook='NEVER RUN A GROUP? START WITH THE PLAN',
         broll=['mujer_pensando', 'mujer_papel', 'circulo_charla', 'taller_mesa', 'escritorio', 'ronda_parados'],
         anchors=[['plan', 1, 'L04', 1], ['close', 0, 'L01', 1], ['guide', 0, 'L00', 1]],
         tag_word='never', chip_word='Playbook'),
 5: dict(hook='EVERY SHEET ENDS WITH ITS CARE NOTES',
         broll=['mujer_seria', 'mujer_angustia', 'mujer_pensando', 'ronda_sentados', 'aula_docente', 'circulo_abajo'],
         anchors=[['care', 0, 'L01', 1], ['workshops', 0, 'L04', 1], ['guide', 0, 'L00', 1]],
         tag_word='Some', chip_word='hundred'),
 6: dict(hook='THREE GROUP WORKSHOPS A MONTH',
         broll=['rotafolio_mujer', 'aula_chicos', 'aula_adultos', 'oficina_grupo', 'cuaderno', 'ronda_sentados'],
         anchors=[['icebreakers', 0, 'L02', 1], ['template', 0, 'L00', 1], ['school', 0, 'L04', 1]],
         tag_word='year', chip_word='costs'),
}

os.makedirs('plans', exist_ok=True)
for n, c in V.items():
    stills_usados = sorted({a[2] for a in c['anchors']})
    pool = [[k, 0, 4.5] for k in c['broll']] + [[k, 4.5, 9] for k in c['broll'][:4]] \
         + [[k, 0, 3] for k in stills_usados]
    P = {
        'vo': f'../vo/V{n}.wav', 'script': f'../vo/V{n}.txt', 'speed': 1.15, 'lang': 'en',
        'clips': CLIPS, 'pool': pool, 'seed': n, 'usage': '../usage.json',
        'cut': [2.6, 3.4, 4.2],
        'capy': 1180, 'words': 3, 'progress': True,
        'music': f'../music/bed_{"ABC"[(n-1)%3]}.wav', 'music_db': -26,
        'hook': c['hook'],
        'anchors': c['anchors'],
        'first': [c['broll'][0], 0],   # el plano de apertura de cada video
        'whoosh': [1, 3, 5, 7],
        'sfx': [['pop', 'Tap', 0]],
        'overlays': [
            {'type': 'tag',  'text': TAG,  'word': c['tag_word'],  'dur': 3.0},
            {'type': 'chip', 'text': CHIP, 'word': c['chip_word'], 'dur': 2.4},
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
