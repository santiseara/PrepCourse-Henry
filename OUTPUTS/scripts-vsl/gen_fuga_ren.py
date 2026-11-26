# -*- coding: utf-8 -*-
"""Planes de las 3 renovaciones de Fuga Perfecta (variables del Guion 2, el del traidor).
Toma el plan2.json de la tanda del 24/11 como molde: misma edicion, mismo pool, mismo banner.
Lo unico que cambia por video: voz, guion, caja de hook, anclas, semilla y cama musical.
El usage es COMPARTIDO entre los tres (24/11, Santiago: "usás en todos las mismas visuales")."""
import json, os, copy
BASE = json.load(open('plan2.json'))
V = {
 'R1': dict(seed=101, first=['g01', 0.15],
            hook='Hay un sobre que no se abre|delante de nadie.', until='nadie',
            anchors=[['sobre',0,'v5',0.1], ['solas',0,'g03',0.15],
                     ['número',0,'v3z',2.66], ['cronómetro',0,'v1z',0.1]]),
 'R2': dict(seed=202, first=['g09', 0.15],
            hook='Uno de tus amigos|te va a mentir en la cara.', until='vos',
            anchors=[['sobres',0,'v8',0.1], ['solas',0,'g03z',0.15],
                     ['número',0,'v3',2.66], ['reloj',0,'v1z',0.1]]),
 'R3': dict(seed=303, first=['g10', 0.15],
            hook='Seguíamos discutiendo|quién nos frenaba.', until='frenando',
            anchors=[['trampa',0,'v5z',0.1], ['solas',0,'g03',2.75],
                     ['números',0,'v3z',2.66], ['cronómetro',0,'v1z',0.1],
                     ['salimos',0,'g04',0.15]]),
}
for k, c in V.items():
    p = copy.deepcopy(BASE)
    n = k[1]
    p['vo'] = f'voz/r{n}.wav'; p['script'] = f'voz/r{n}.txt'
    p['seed'] = c['seed']; p['first'] = c['first']
    p['hook'] = c['hook']; p['hook_until'] = c['until']
    p['anchors'] = c['anchors']
    p['usage'] = 'usage_ren.json'      # compartido: que no se repitan planos entre las tres
    p['music'] = f'cama_r{n}.wav'
    json.dump(p, open(f'plan_r{n}.json', 'w'), ensure_ascii=False, indent=1)
    print(f'plan_r{n}.json  seed={c["seed"]}  first={c["first"][0]}')
