# -*- coding: utf-8 -*-
"""Genera los 6 plan.json de Pilates sin Vueltas para edit_gwp.py.
Uso:  cd ~/Desktop/pilates-sin-vueltas/anuncios/work && python3 gen_pilates_plans.py
Montar: for n in 1 2 3 4 5 6; do python3 edit_gwp.py plans/V$n.json ../PSV-V$n.mp4; done

Insumos (todos gratis, sin creditos):
  vo/V1.wav..V6.wav     <- voz en off, Google AI Studio (Sulafat, acento rioplatense por prompt de estilo)
  broll/mk*.mp4         <- stock gratuito de mixkit, estudio de reformers, curado a mano
  ../../landing/*.webp  <- fichas de clase, ejercicios ilustrados y mockups de la propia landing
"""
import json, os

LAND = '../../../landing/'   # relativo a plans/

# stills elegidos de la landing
STILLS = {
 'mock_todo':  'img02',   # abanico de los volumenes + tablet + celular
 'mujer_tab':  'img00',   # instructora mostrando una ficha en la tablet
 'mujer_libro':'img01',   # instructora con el volumen de clases avanzadas
 'clase_ref':  'img03',   # ficha Clase 15 - Reformer
 'clase_pared':'img04',   # ficha Clase 12 - Pilates en pared
 'clase_chair':'img06',   # ficha Clase 51 - Wunda Chair
 'clase_cad':  'img07',   # ficha Clase 80 - Cadillac
 'ej_cisne':   'img09',   # ejercicio El Cisne (con adaptacion y errores)
 'ej_puente':  'img10',   # Puente a una pierna sobre la pelota
 'ej_remo':    'img11',   # Remo sentada con banda
 'ej_aro':     'img12',   # Press de brazos con aro
 'bono_ficha': 'img15',   # Ficha de Evaluacion de la Alumna
 'bono_cal':   'img16',   # Calendario de 30 dias
}
CLIPS = {k: {'src': LAND + v + '.webp', 'still': True, 'fit': True} for k, v in STILLS.items()}
CLIPS['mock_todo']['fit'] = False

# b-roll de estudio (mixkit). mk48544 dura 4.09 s, se usa hasta 3.8
B = ['mk48544','mk48548','mk48554','mk48555','mk48556','mk48557','mk48558',
     'mk48559','mk48560','mk48561','mk48562','mk48564','mk48566','mk48567',
     'mk45761','mk45764']
for f in B:
    CLIPS[f] = {'src': '../broll/' + f + '.mp4'}
TOPE = {'mk48544': 3.8}

TAG  = 'PARA INSTRUCTORAS DE PILATES'
CHIP = '100 CLASES LISTAS PARA DAR'

V = {
 1: dict(hook=u'TE LO DICEN EN LA PUERTA',
         broll=['mk48557','mk48544','mk48556','mk48560','mk48559','mk48564'],
         anchors=[[u'\u00edndice',0,'clase_ref',1],[u'silla',0,'clase_chair',1],[u'ilustrados',0,'mock_todo',1]],
         chip_word=u'Vueltas', end_word=u'fijate'),
 2: dict(hook=u'LA QUE NO VUELVE TE CUESTA EL A\u00d1O',
         broll=['mk48561','mk48562','mk48567','mk48556','mk48544','mk48566'],
         anchors=[[u'numeradas',0,'clase_ref',1],[u'sesenta',0,'clase_pared',1],[u'clases',0,'mock_todo',1]],
         chip_word=u'Vueltas', end_word=u'oferta'),
 3: dict(hook=u'UNA HORA CUIDANDO, CERO DANDO CLASE',
         broll=['mk48559','mk48548','mk48554','mk48564','mk48557','mk48560'],
         anchors=[[u'silla',0,'clase_chair',1],[u'ilustrados',0,'ej_remo',1],[u'manual',0,'mujer_libro',1]],
         chip_word=u'Vueltas', end_word=u'Mir\u00e1'),
 4: dict(hook=u'UN CUERPO PARA EL QUE NO TE PREPARARON',
         broll=['mk48556','mk48566','mk48558','mk48557','mk48544','mk48562'],
         anchors=[[u'pared',0,'clase_pared',1],[u'consignas',0,'ej_cisne',1],[u'ilustrados',0,'mock_todo',1]],
         chip_word=u'Vueltas', end_word=u'Entr\u00e1'),
 5: dict(hook=u'SIN FLEXI\u00d3N PROFUNDA, DICE EL PAPEL',
         broll=['mk48554','mk48555','mk48548','mk48559','mk48564','mk48567'],
         anchors=[[u'rango',0,'ej_puente',1],[u'adaptaciones',0,'ej_cisne',1],[u'siete',0,'mock_todo',1]],
         chip_word=u'Vueltas', end_word=u'Toc\u00e1'),
 6: dict(hook=u'\u00bfYA PUEDO HACER ABDOMINALES?',
         broll=['mk45761','mk45764','mk48562','mk48566','mk48567','mk48560'],
         anchors=[[u'escrita',1,'clase_ref',1],[u'bloque',0,'mujer_tab',1],[u'particular',0,'mock_todo',1]],
         chip_word=u'Vueltas', end_word=u'Fijate'),
}


os.makedirs('plans', exist_ok=True)
for n, c in V.items():
    stills_usados = sorted({a[2] for a in c['anchors']})
    pool = [[k, 0, TOPE.get(k, 4.5)] for k in c['broll']] \
         + [[k, 0, 4.2] for k in stills_usados] + [[k, 0, 3.4] for k in stills_usados] \
         + [[k, 0, 3.0] for k in stills_usados]
    P = {
        'vo': '../vo/V%d.wav' % n, 'script': '../vo/V%d.txt' % n, 'speed': 1.0, 'lang': 'es',
        'clips': CLIPS, 'pool': pool, 'seed': n, 'usage': '../usage.json',
        'cut': [2.6, 3.4, 4.2],
        'capy': 1440, 'words': 4, 'progress': True,
        'music': '../music/bed_%s.wav' % 'ABC'[(n - 1) % 3], 'music_db': -16,
        'hook': c['hook'],
        'anchors': c['anchors'],
        'first': [c['broll'][0], 0],
        'whoosh': [1, 3, 5, 7],
        'sfx': [],
        'overlays': [
            {'type': 'tag',  'text': TAG,  'at': 0.0,  'dur': 3.4},
            {'type': 'chip', 'text': CHIP, 'at': 0.25, 'dur': 3.15, 'icon': u'\U0001F447', 'y': 1020},
            {'type': 'chip', 'text': CHIP, 'word': c['chip_word'], 'dur': 2.4, 'y': 1600},
            {'type': 'end',  'word': c['end_word'],
             'title': ['PILATES', 'SIN VUELTAS'],
             'sub': u'100 CLASES \u00b7 500+ EJERCICIOS',
             'sub2': u'DESCARGA INMEDIATA \u00b7 7 D\u00cdAS DE GARANT\u00cdA',
             'cta': u'Toc\u00e1 M\u00e1s informaci\u00f3n \U0001F447'},
        ],
    }
    json.dump(P, open('plans/V%d.json' % n, 'w'), ensure_ascii=False, indent=1)
    print('plans/V%d.json  %d b-roll + %d stills  |  %s' % (n, len(c['broll']), len(stills_usados), c['hook']))

falta = ['vo/V%d.wav' % n for n in V if not os.path.exists('vo/V%d.wav' % n)]
print(('\nFALTA la voz: ' + ', '.join(falta)) if falta else '\nTodo listo para montar.')
