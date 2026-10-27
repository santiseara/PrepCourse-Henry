"""Valida las anclas de plan/heads/stickers contra la MISMA lista de palabras que usa el editor.
Ojo: no alcanza con mirar words0.json (la transcripción cruda) ni el guion. El editor alinea una
contra el otro con difflib y reemplaza las palabras de Whisper por las del guion cuando calzan;
las que no calzan quedan como las dijo Whisper (los números, sobre todo: "7 minutos", "17 .990").
Este script reproduce ese paso y busca ahí.
Uso: python3 validar_anclas.py <carpeta_work> <n> <guion.txt>
"""
import os, json, sys, unicodedata, difflib

WD, n, gpath = sys.argv[1], sys.argv[2], sys.argv[3]
words0 = json.load(open(f'{WD}/edit_bloque{n}_heygen/words0.json'))
GUION = open(gpath, encoding='utf-8').read()

def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    return ''.join(c for c in s if c.isalnum() and unicodedata.category(c) != 'Mn')

gt = GUION.split()
# 1) fuera lo que Whisper inventó en los silencios
ops = difflib.SequenceMatcher(None, [norm(w['w']) for w in words0], [norm(x) for x in gt], autojunk=False).get_opcodes()
bad = {i for op, i1, i2, _, _ in ops if op == 'delete' for i in range(i1, i2)}
words = [w for i, w in enumerate(words0) if i not in bad]
# 2) pegar los guiones sueltos, como hace el editor
w2 = []
for w in words:
    if w2 and w['w'][:1] == '-': w2[-1] = {**w2[-1], 'w': w2[-1]['w'] + w['w'], 'e': w['e']}
    else: w2.append(dict(w))
words = w2
# 3) reemplazar por las palabras del guion donde calzan
a_, b_ = [norm(w['w']) for w in words], [norm(x) for x in gt]
drop = set()
for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a_, b_, autojunk=False).get_opcodes():
    if op in ('equal', 'replace') and i2 - i1 == j2 - j1:
        for i, j in zip(range(i1, i2), range(j1, j2)): words[i]['w'] = gt[j]
    elif op == 'delete':
        drop.update(range(i1, i2))
words = [w for i, w in enumerate(words) if i not in drop]

N = [norm(w['w']) for w in words]
def buscar(fr):
    t = [x for x in (norm(y) for y in fr.split()) if x]
    return [i for i in range(len(N) - len(t) + 1) if N[i:i + len(t)] == t]

mal = 0
print(f'=== BLOQUE {n} · {len(words)} palabras, {words[-1]["e"]:.1f}s ===')
for it in json.load(open(f'{WD}/plan{n}.json')):
    A, B = buscar(it[1]), buscar(it[2])
    if not A or not B:
        print(f'  ✗ {it[0]:16} FALTA ' + (f'inicio «{it[1]}»' if not A else f'fin «{it[2]}»')); mal += 1; continue
    a, b = words[A[0]]['s'], words[B[0]]['s']
    flag = '✗ FIN ANTES DEL INICIO' if b <= a else ('⚠ ancla repetida' if len(A) > 1 or len(B) > 1 else '✓')
    if flag[0] in '✗⚠': mal += 1
    print(f'  {flag:22} {it[0]:16} {a:6.1f}s → {b:6.1f}s')
for nombre, arch in (('HEADLINE', f'heads{n}.json'), ('PLACA', f'stickers{n}.json')):
    for h in json.load(open(f'{WD}/{arch}')):
        A = buscar(h[0])
        if not A: print(f'  ✗ {nombre} falta: «{h[0]}»'); mal += 1
        elif len(A) > 1: print(f'  ⚠ {nombre} repetido ({len(A)}x): «{h[0]}»'); mal += 1
print(f'  --- problemas: {mal}')
sys.exit(1 if mal else 0)
