# -*- coding: utf-8 -*-
# Planes de las 3 renovaciones de voz en off V40-V42 (2026-10-28). Editor: OUTPUTS/scripts-vsl/edit_herrero_v3.py
# Edicion nueva: paleta de la landing (rust/amber/ink/blueprint), placa hero de apertura, regla de medidas
# arriba, subtitulos de 3 palabras con la palabra activa en ambar, clips de pantalla del plano en el celular
# y cortes mas largos (2,2-3,2 s) con la voz a 1,30.
import json, os, re, subprocess, unicodedata, sys
T = '../tiktoks/'
SRC = {'A': '7184589200031780138', 'B': '7253123425676365083', 'C': '7291806726557322542', 'D': '7296659006788013355',
       'E': '7296931913627880750', 'G': '7454702962955554094', 'e': '7439717704170327342', 'H': '7465533630979312926',
       'I': '7465739688742276398', 'J': '7468781029281533230', 'K': '7480702060149738758',
       'M': '7494600914062429462', 'N': '7498876898546863366', 'O': '7504214068698320149', 'Q': '7507040325060300037',
       'R': '7507438631334808840', 'T': '7509932304077196562', 'U': '7519325255467420983', 'V': '7565696076930452750',
       'X': '7591665688796810508', 'Y': '7566063571134680350', 'Z': '7643576282252381460',
       'b': '7684049169610427655', 'c': '7691053148219198752', 'd': '7697496096616008961'}
def dur(p):
    r = subprocess.run([os.path.expanduser('~/bin/ffmpeg'), '-i', p], capture_output=True, text=True).stderr
    h, m, s = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r).groups(); return int(h)*3600 + int(m)*60 + float(s)
LIMITE = {'Y': 96, 'c': 254}     # carteles en ingles y placa de marca de otra herreria
# J lleva el cartel en ingles "Trailer Build Part 4: Mobility" hasta el segundo 5
DESDE = {'B': 10.5, 'J': 5.5}
C, POOL = {}, []
for k, i in SRC.items():
    p = T + i + '.mp4'; C[k] = {'src': p}; d = min(dur(p), LIMITE.get(k, 1e9))
    t = DESDE.get(k, 1.5)
    while t + 3 <= d - 0.8: POOL.append([k, round(t, 1), round(t + 3, 1)]); t += 3
# clips nuevos: el plano abierto en el celular (nunca se espejan, tienen texto)
for k, f in (('D1', 'demo-hojas.mp4'), ('D2', 'demo-scroll.mp4')):
    p = '../demo/' + f; C[k] = {'src': p, 'noflip': True}
    t = 0.2
    while t + 2.8 <= dur(p) - 0.3: POOL.append([k, round(t, 1), round(t + 2.8, 1)]); t += 2.8
S = '../stills/'
FIT = ('plan-', 'hoja-', 'ficha-', 'catalogo-')
for f in sorted(os.listdir(S)):
    if f.startswith('.') or f.endswith('.py'): continue
    key = 'P_' + f.rsplit('.', 1)[0]
    C[key] = {'src': S + f, 'still': True, 'fit': f.startswith(FIT)}
    POOL.append([key, 0, 3])
MUS = {40: 'A', 41: 'B', 42: 'C'}

def norm(w):
    w = unicodedata.normalize('NFD', w.lower())
    return ''.join(c for c in w if unicodedata.category(c) != 'Mn').strip('¿¡"()')
ERRORES = []
def validar(n, anchors, overlays, hook_until):
    txt = open(f'../vo/V{n}.txt', encoding='utf-8').read().split()
    seq = [norm(w) for w in txt]
    def exacta(w, occ):
        veces = seq.count(norm(w))
        if veces == 0: ERRORES.append(f'V{n}: "{w}" no esta en el texto'); return None
        if occ >= veces: ERRORES.append(f'V{n}: "{w}" aparece {veces} vez/veces, pediste la {occ}'); return None
        return [txt[i] for i, x in enumerate(seq) if x == norm(w)][occ]
    for item in anchors:
        e = exacta(item[0], item[1])
        if e: item[0] = e
    for o in overlays:
        if not o.get('word'): continue
        e = exacta(o['word'], o.get('occ', 0))
        if e: o['word'] = e
    if hook_until:
        e = exacta(hook_until, 0)
        return e or hook_until
    return hook_until

def plan(n, hook, hook_until, anchors, overlays, seed):
    hook_until = validar(n, anchors, overlays, hook_until)
    keys = {a[2] for a in anchors}
    # las fotos y los clips de pantalla solo entran donde estan ancladas
    pool = [p for p in POOL if not p[0].startswith(('P_', 'D1', 'D2')) or p[0] in keys]
    P = {'vo': f'../vo/V{n}.wav', 'script': f'../vo/V{n}.txt', 'speed': 1.30, 'silence': [0.26, 0.12], 'lang': 'es',
         'music': f'../music/bed_{MUS[n]}.wav', 'music_db': -9, 'flash': 4, 'progress': True, 'fit_w': 0.86, 'fit_y': 300,
         'clips': C, 'pool': pool, 'usage': 'usage.json', 'seed': seed, 'hook': hook, 'hook_until': hook_until,
         'anchors': anchors, 'overlays': overlays, 'whoosh': 'flash', 'cut': [2.2, 2.7, 3.2], 'sfx': [],
         'capy': 1330, 'words': 3, 'hi': '&H003CA3F2&'}
    json.dump(P, open(f'V{n}.json', 'w'), indent=1, ensure_ascii=False)
STAMP = lambda text, word, occ=0, dur=1.6: {'type': 'stamp', 'text': text, 'word': word, 'occ': occ, 'dur': dur}
END = lambda word, occ=0, **kw: dict({'type': 'end', 'word': word, 'occ': occ}, **kw)
TAG = lambda text, word, occ=0, dur=2.0, y=210: {'type': 'tag', 'text': text, 'word': word, 'occ': occ, 'dur': dur, 'y': y}
CH = lambda text, word, occ=0, dur=2.0, icon='✓': {'type': 'chip', 'text': text, 'word': word, 'occ': occ, 'dur': dur, 'icon': icon}
MO = lambda left, right, word, occ=0, dur=2.8, label='': {'type': 'money', 'left': left, 'right': right, 'word': word, 'occ': occ, 'dur': dur, 'label': label}
CIERRE = {'sub': '+1.200 PLANOS · 12 BONUS', 'sub2': 'QUÉ CORTAR · CUÁNTO HIERRO · CUÁNTO COBRAR',
          'cta': 'Tocá Más información', 'foot': '60 DÍAS DE GARANTÍA · UN SOLO PAGO'}


# V40 - nunca mas dibujar en un carton / porton de dos hojas FM-004
plan(40, 'Nunca más dibujar en un cartón', 'hierros.',
     [['hierros.', 0, 'Z', 1.5], ['milímetros.', 0, 'P_hoja-1-dibujo', 0],
      ['justo.', 0, 'P_hoja-2-compras', 0], ['doce.', 0, 'P_hoja-4-soldadura', 0],
      ['188', 0, 'P_ficha-fm-004', 0], ['carpetas:', 0, 'P_celular-carpetas', 0],
      ['alcanza.', 0, 'T', 4.5], ['Tocá', 0, 'P_todo-incluido', 0]],
     [TAG('Portón de dos hojas de 2,60 m', 'portón', dur=1.8),
      CH('Cada medida en milímetros', 'milímetros.'),
      CH('Comprás justo, una sola vuelta', 'justo.'),
      MO('$188.000', '$785.000 a $1.020.000', '188', label='HIERRO · SE COBRA'),
      CH('10 carpetas · +1.200 planos', 'carpetas:'), END('Tocá', **CIERRE)], 4040)

# V41 - el cliente senala una foto / jaula de potencia GY-013
plan(41, 'El cliente señala una foto y vos ya tenés el plano', 'hacer.',
     [['mostrarle:', 0, 'P_catalogo-clientes', 0], ['completo.', 0, 'D1', 0.2],
      ['155', 0, 'P_ficha-gy-013', 0], ['calculado:', 0, 'P_hoja-trabajo', 0],
      ['paso.', 0, 'P_hoja-4-soldadura', 0], ['carpetas,', 0, 'P_celular-carpetas', 0],
      ['cortás.', 0, 'R', 1.5], ['Tocá', 0, 'P_todo-incluido', 0]],
     [TAG('El catálogo para mostrarle al cliente', 'mostrarle:', dur=2.2),
      TAG('Jaula de potencia 1,10 x 1,10', 'jaula', dur=1.8),
      MO('$155.000', '$655.000 a $850.000', '155', label='HIERRO · SE COBRA'),
      CH('El precio ya viene calculado', 'calculado:'),
      CH('60 días de garantía', 'garantía.'), END('Tocá', **CIERRE)], 4141)

# V42 - lo que cobra un dibujante por un plano / invernadero ST-012
plan(42, 'Lo que cobra un dibujante por un solo plano', 'adentro.',
     [['calculado.', 0, 'P_hoja-trabajo', 0], ['372', 0, 'P_ficha-st-012', 0],
      ['vista.', 0, 'P_hoja-1-dibujo', 0], ['milímetros,', 0, 'P_hoja-vistas', 0],
      ['dibujado,', 0, 'P_hoja-3-cortes', 0], ['paso.', 0, 'P_hoja-4-soldadura', 0],
      ['hierro.', 0, 'P_celular-carpetas', 0], ['archivo.', 0, 'D2', 3.0],
      ['Tocá', 0, 'P_todo-incluido', 0]],
     [TAG('Invernadero de 4 x 3 m', 'invernadero', dur=1.8),
      MO('$372.000', '$1.375.000 a $1.790.000', '372', label='HIERRO · SE COBRA'),
      CH('Hoja 2 · Todas las cotas en milímetros', 'milímetros,'),
      CH('Barras de 6 m, sin desperdicio', 'dibujado,'),
      CH('60 días de garantía', 'plata.'), END('Tocá', **CIERRE)], 4242)

if ERRORES:
    print('\n'.join(ERRORES)); sys.exit(1)
print('planes V40-V42 listos')
