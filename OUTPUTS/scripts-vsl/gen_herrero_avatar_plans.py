# -*- coding: utf-8 -*-
# Planes de los 3 videos con avatar (A1-A3, 2026-10-28). Editor: OUTPUTS/scripts-vsl/edit_herrero_avatar.py
# La base es el avatar de HeyGen (bloque parado + bloque sentado) y se corta a fichas, hojas del plano,
# el plano en el celular y B-roll solo en las palabras marcadas.
import json, os, re, subprocess, unicodedata, sys
T = '../tiktoks/'
SRC = {'E': '7296931913627880750', 'T': '7509932304077196562', 'Z': '7643576282252381460'}
C = {k: {'src': T + v + '.mp4'} for k, v in SRC.items()}
for k, f in (('D1', 'demo-hojas.mp4'), ('D2', 'demo-scroll.mp4')):
    C[k] = {'src': '../demo/' + f, 'noflip': True}
S = '../stills/'
FIT = ('plan-', 'hoja-', 'ficha-', 'catalogo-')
for f in sorted(os.listdir(S)):
    if f.startswith('.') or f.endswith('.py'): continue
    C['P_' + f.rsplit('.', 1)[0]] = {'src': S + f, 'still': True, 'fit': f.startswith(FIT)}

def norm(w):
    w = unicodedata.normalize('NFD', w.lower())
    return ''.join(c for c in w if unicodedata.category(c) != 'Mn').strip('¿¡"()')
ERR = []
def validar(n, cutaways, overlays, hook_until):
    txt = open(f'../vo/{n}.txt', encoding='utf-8').read().split()
    seq = [norm(w) for w in txt]
    def exacta(w, occ):
        veces = seq.count(norm(w))
        if veces == 0: ERR.append(f'{n}: "{w}" no esta en el texto'); return None
        if occ >= veces: ERR.append(f'{n}: "{w}" aparece {veces} vez/veces, pediste la {occ}'); return None
        return [txt[i] for i, x in enumerate(seq) if x == norm(w)][occ]
    for item in cutaways:
        e = exacta(item[0], item[1])
        if e: item[0] = e
    for o in overlays:
        if not o.get('word'): continue
        e = exacta(o['word'], o.get('occ', 0))
        if e: o['word'] = e
    if hook_until:
        return exacta(hook_until, 0) or hook_until
    return hook_until

def plan(n, bloques, hook, hook_until, cutaways, overlays, music):
    hook_until = validar(n, cutaways, overlays, hook_until)
    P = {'avatar': [f'../heygen/{b}.mp4' for b in bloques], 'script': f'../vo/{n}.txt', 'lang': 'es',
         'music': f'../music/bed_{music}.wav', 'music_db': -13, 'progress': True, 'fit_w': 0.86, 'fit_y': 300,
         'clips': C, 'cutaways': cutaways, 'overlays': overlays, 'hook': hook, 'hook_until': hook_until,
         'gap': 0.5, 'whoosh': [], 'sfx': [], 'capy': 1330, 'words': 3, 'hi': '&H003CA3F2&'}
    json.dump(P, open(f'{n}.json', 'w'), indent=1, ensure_ascii=False)

END = lambda word, occ=0, **kw: dict({'type': 'end', 'word': word, 'occ': occ}, **kw)
TAG = lambda text, word, occ=0, dur=2.0, y=210: {'type': 'tag', 'text': text, 'word': word, 'occ': occ, 'dur': dur, 'y': y}
CH = lambda text, word, occ=0, dur=2.0, icon='✓': {'type': 'chip', 'text': text, 'word': word, 'occ': occ, 'dur': dur, 'icon': icon}
MO = lambda left, right, word, occ=0, dur=2.8, label='': {'type': 'money', 'left': left, 'right': right, 'word': word, 'occ': occ, 'dur': dur, 'label': label}
STAMP = lambda text, word, occ=0, dur=1.6: {'type': 'stamp', 'text': text, 'word': word, 'occ': occ, 'dur': dur}
CIERRE = {'sub': '+1.200 PLANOS · 12 BONUS', 'sub2': 'QUÉ CORTAR · CUÁNTO HIERRO · CUÁNTO COBRAR',
          'cta': 'Tocá Más información', 'foot': '60 DÍAS DE GARANTÍA · UN SOLO PAGO'}

# A1 - "A mi no me faltaba mano" / hoja de porton FM-068
plan('A1', ['A1-b1', 'A1-b2'], 'No me faltaba mano. Me faltaban números.', 'números.',
     [['cartón,', 0, 'Z', 1.5, 2.2], ['adentro.', 0, 'D1', 0.2, 2.6], ['milímetros.', 0, 'P_hoja-1-dibujo', 0, 2.8],
      ['hierros.', 0, 'P_hoja-2-compras', 0, 2.6], ['doce.', 0, 'P_hoja-4-soldadura', 0, 2.6],
      ['124', 0, 'P_ficha-fm-068', 0, 3.0], ['celular', 0, 'D2', 0.2, 2.6],
      ['Tocá', 0, 'P_todo-incluido', 0, 4.0]],
     [TAG('Hoja de portón de campo 3,66 m', 'portón', dur=2.2),
      CH('Cada medida en milímetros', 'milímetros.'),
      CH('Las barras contadas, una sola vuelta', 'hierros.'),
      MO('$124.000', '$475.000 a $620.000', '124', label='HIERRO · SE COBRA'),
      END('Tocá', **CIERRE)], 'A')

# A2 - "Le dije que le avisaba. Nunca le avise." / mesa de comedor FN-022
plan('A2', ['A2-b1', 'A2-b2'], 'El que tira el número se lleva el trabajo', 'avisé.',
     [['otro.', 0, 'T', 1.5, 2.2], ['calculado:', 0, 'P_hoja-trabajo', 0, 2.8], ['235', 0, 'P_ficha-fn-022', 0, 3.0],
      ['dibujo.', 0, 'P_hoja-1-dibujo', 0, 2.6], ['numerado.', 0, 'P_hoja-4-soldadura', 0, 2.6],
      ['segundos.', 0, 'D2', 2.0, 1.6], ['Tocá', 0, 'P_todo-incluido', 0, 4.0]],
     [CH('El precio de venta ya calculado', 'calculado:', dur=2.4),
      TAG('Mesa de comedor 2,44 x 1,02', '235', dur=2.0),
      MO('$235.000', '$645.000 a $840.000', '645', label='HIERRO · SE COBRA'),
      CH('10 carpetas · +1.200 planos', 'segundos.'),
      END('Tocá', **CIERRE)], 'B')

# A3 - "Mi soldadora juntaba polvo" / fogonero BQ-007
plan('A3', ['A3-b1', 'A3-b2'], 'La soldadora ya está paga', 'polvo.',
     [['143', 0, 'P_ficha-bq-007', 0, 3.0], ['plano.', 0, 'P_hoja-trabajo', 0, 2.6],
      ['prendido,', 0, 'E', 1.5, 2.4], ['escaleras.', 0, 'P_celular-carpetas', 0, 2.8],
      ['resuelto,', 0, 'P_hoja-4-soldadura', 0, 2.4], ['Tocá', 0, 'P_todo-incluido', 0, 4.0]],
     [TAG('Fogonero cuadrado de 70 cm', 'fogonero', dur=2.0),
      MO('$143.000', '$305.000 a $395.000', '143', label='HIERRO · SE COBRA'),
      CH('Nivel principiante · 3 a 5 horas', 'principiante,'),
      STAMP('VENDIDO', 'semana.'),
      END('Tocá', **CIERRE)], 'C')

if ERR: print('\n'.join(ERR)); sys.exit(1)
print('planes A1-A3 listos')
