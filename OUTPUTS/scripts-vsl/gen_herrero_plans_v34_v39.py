# -*- coding: utf-8 -*-
# Planes de las 6 renovaciones V34-V39 (2026-10-27). Editor: OUTPUTS/scripts-vsl/edit_herrero_v3.py
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
MUS = {34: 'A', 35: 'B', 36: 'C', 37: 'B', 38: 'A', 39: 'C'}

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

# V34 - la linea de la landing: no te falta mano, te faltan numeros / hoja de porton FM-068
plan(34, 'No te falta mano. Te faltan números.', 'números.',
     [['adentro.', 0, 'D1', 0.2], ['milímetros.', 0, 'P_hoja-1-dibujo', 0], ['hierros.', 0, 'Z', 1.5],
      ['numerado,', 0, 'P_hoja-4-soldadura', 0], ['124', 0, 'P_ficha-fm-068', 0],
      ['carpetas:', 0, 'P_celular-carpetas', 0], ['cortar.', 0, 'T', 4.5], ['Tocá', 0, 'P_todo-incluido', 0]],
     [TAG('Las 4 hojas de cada plano', 'adentro.', dur=2.2),
      CH('Cada medida en milímetros', 'milímetros.'),
      TAG('Hoja de portón de campo 3,66 m', 'portón', dur=1.8),
      MO('$124.000', '$475.000 a $620.000', '124', label='HIERRO · SE COBRA'),
      CH('10 carpetas · +1.200 planos', 'carpetas:'), END('Tocá', **CIERRE)], 3434)

# V35 - demo de pantalla: las cuatro hojas / parrilla argentina BQ-090
plan(35, 'Un plano abierto en el celular', 'sucias.',
     [['celular,', 0, 'D2', 0.2], ['Primera', 0, 'D1', 0.2], ['pulgadas.', 0, 'P_hoja-vistas', 0],
      ['Tercera:', 0, 'P_hoja-3-cortes', 0], ['naranja.', 0, 'P_hoja-4-soldadura', 0],
      ['argentina', 0, 'P_ficha-bq-090', 0], ['trailers.', 0, 'U', 1.5], ['Tocá', 0, 'P_todo-incluido', 0]],
     [TAG('Hoja 2 · Frente, lateral y planta', 'pulgadas.', dur=2.2),
      CH('Barras de 6 m, sin desperdicio', 'Tercera:'),
      TAG('Parrilla argentina 1,83 m', 'argentina', dur=1.8),
      MO('$406.000', '$1.030.000 a $1.340.000', '406', label='HIERRO · SE COBRA'),
      END('Tocá', **CIERRE)], 3535)

# V36 - el que tira el numero se lleva el trabajo / mesa de comedor FN-022
plan(36, 'El que tira el número se lleva el trabajo', 'pierde.',
     [['calculado:', 0, 'P_hoja-trabajo', 0], ['235', 0, 'P_ficha-fn-022', 0], ['dibujo.', 0, 'P_hoja-1-dibujo', 0],
      ['numerado.', 0, 'P_hoja-4-soldadura', 0], ['carpetas:', 0, 'P_celular-carpetas', 0],
      ['segundos.', 0, 'D2', 3.0], ['Tocá', 0, 'P_todo-incluido', 0]],
     [CH('El precio ya viene calculado', 'calculado:', dur=2.2),
      TAG('Mesa de comedor 2,44 x 1,02', '235', dur=1.8),
      MO('$235.000', '$645.000 a $840.000', '645', label='HIERRO · SE COBRA'),
      CH('60 días de garantía', 'garantía.'), END('Tocá', **CIERRE)], 3636)

# V37 - los cuatro numeros / mesa para motos SH-148
plan(37, 'Cuatro números y el sábado ya estás cortando', 'cobrar.',
     [['piezas', 0, 'P_hoja-3-cortes', 0], ['contadas,', 0, 'P_hoja-2-compras', 0],
      ['dibujo.', 0, 'P_hoja-4-soldadura', 0], ['pie,', 0, 'P_hoja-trabajo', 0],
      ['241', 0, 'P_ficha-sh-148', 0], ['carpetas,', 0, 'P_celular-carpetas', 0],
      ['alcanza.', 0, 'R', 1.5], ['Tocá', 0, 'P_todo-incluido', 0]],
     [TAG('Hoja 3 · La lista de cortes', 'piezas', dur=2.2),
      CH('Barras de 6 m contadas', 'contadas,'),
      TAG('Mesa para motos 2,13 m', '241', dur=1.8),
      MO('$241.000', '$750.000 a $975.000', '750', label='HIERRO · SE COBRA'),
      END('Tocá', **CIERRE)], 3737)

# V38 - un trabajo lo paga diez veces / rack overland TK-024
plan(38, 'El primer trabajo lo paga diez veces', 'siempre.',
     [['rack', 0, 'P_ficha-tk-024', 0], ['carpetas,', 0, 'P_celular-carpetas', 0],
      ['soldadura.', 0, 'P_hoja-4-soldadura', 0], ['taller.', 0, 'D1', 2.8],
      ['derecho.', 0, 'I', 1.5], ['hierro.', 0, 'Z', 4.5], ['Tocá', 0, 'P_todo-incluido', 0]],
     [TAG('Rack para la caja de 2,44 m', 'rack', dur=1.8),
      MO('$122.000', '$520.000 a $675.000', '122', label='HIERRO · SE COBRA'),
      CH('Hojas para imprimir y llevar al taller', 'taller.'),
      CH('60 días de garantía', 'plata.'), END('Tocá', **CIERRE)], 3838)

# V39 - la soldadora ya esta paga / fogonero cuadrado BQ-007
plan(39, 'La soldadora que tenés ya está paga', 'paga.',
     [['143', 0, 'P_ficha-bq-007', 0], ['plano.', 0, 'P_hoja-trabajo', 0], ['prendido,', 0, 'E', 1.5],
      ['escalera,', 0, 'D2', 6.0], ['soldadura.', 0, 'P_hoja-4-soldadura', 0], ['Tocá', 0, 'P_todo-incluido', 0]],
     [TAG('Fogonero cuadrado de 70 cm', 'fogonero', dur=1.8),
      MO('$143.000', '$305.000 a $395.000', '143', label='HIERRO · SE COBRA'),
      CH('Nivel principiante · 3 a 5 horas', 'principiante,'),
      STAMP('VENDIDO', 'semana.'), END('Tocá', **CIERRE)], 3939)

if ERRORES:
    print('\n'.join(ERRORES)); sys.exit(1)
print('planes V34-V39 listos')
