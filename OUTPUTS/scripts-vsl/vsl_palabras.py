# -*- coding: utf-8 -*-
"""La MISMA lista de palabras que arma edit_vsl_quiz.py para buscar las frases del plan.

Por que existe: el editor no busca contra la transcripcion. Despues de transcribir hace
dos cosas que cambian los tokens, y un anclaje que no las replique no se encuentra nunca:

  1. pega al anterior toda palabra que empieza con guion:  "30" + "-day"  ->  "30-day"
  2. reemplaza cada palabra oida por la del GUION cuando el tramo alinea uno a uno,
     y descarta las que Whisper invento (no estan en el guion)

Asi que los anclajes salen casi siempre del guion, no de lo que se oye. Medido el
11/11/2026: anclar contra la transcripcion dejo 3 b-rolls y 1 placa afuera del render.

Uso:  from vsl_palabras import palabras_del_editor
      W = palabras_del_editor(words0_json, guion_txt)   # [{'w','s','e'}, ...]
"""
import difflib, unicodedata


def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    return ''.join(c for c in s if c.isalnum() and unicodedata.category(c) != 'Mn')


def palabras_del_editor(words0, guion):
    """words0: lista cruda de Whisper. guion: texto del guion. Devuelve la lista final."""
    words = []
    for w in words0:
        w = {'w': w['w'], 's': w['s'], 'e': w['e']}
        if words and w['w'][:1] == '-':
            words[-1] = {**words[-1], 'w': words[-1]['w'] + w['w'], 'e': w['e']}
        else:
            words.append(w)
    gt = guion.split()
    a_, b_ = [norm(w['w']) for w in words], [norm(x) for x in gt]
    drop = set()
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a_, b_, autojunk=False).get_opcodes():
        if op in ('equal', 'replace') and i2 - i1 == j2 - j1:
            for i, j in zip(range(i1, i2), range(j1, j2)):
                words[i]['w'] = gt[j]
        elif op == 'delete':
            drop.update(range(i1, i2))
    return [w for i, w in enumerate(words) if i not in drop]
