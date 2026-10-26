import json, os, re, subprocess
# Planes de los 6 videos de la tanda V7-V12 (2026-10-23). Editor: OUTPUTS/scripts-vsl/edit_herrero.py
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
    h, m, s = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r).groups(); return int(h) * 3600 + int(m) * 60 + float(s)
# Y lleva el cartel en ingles "And that's how you do that" desde el segundo 97 hasta el final
LIMITE = {'Y': 96}
C, POOL = {}, []
for k, i in SRC.items():
    p = T + i + '.mp4'; C[k] = {'src': p}; d = min(dur(p), LIMITE.get(k, 1e9))
    t = 1.5
    while t + 3 <= d - 0.8: POOL.append([k, round(t, 1), round(t + 3, 1)]); t += 3
S = '../stills/'
for f in sorted(os.listdir(S)):
    if f.startswith('.') or f.endswith('.py'): continue
    key = 'P_' + f.rsplit('.', 1)[0]
    C[key] = {'src': S + f, 'still': True, 'fit': f.startswith('plan-') or f.startswith('hoja-')}
    POOL.append([key, 0, 3])
MUS = {13: 'A', 14: 'B', 15: 'C', 19: 'A', 20: 'B', 21: 'C'}
def plan(n, hook, hook_until, anchors, overlays, seed):
    keys = {a[2] for a in anchors}
    pool = [p for p in POOL if not p[0].startswith('P_') or p[0] in keys]
    P = {'vo': f'../vo/V{n}.wav', 'script': f'../vo/V{n}.txt', 'speed': 1.20, 'silence': [0.26, 0.12], 'lang': 'es',
         'music': f'../music/bed_{MUS[n]}.wav', 'music_db': -8, 'flash': 3, 'progress': True, 'fit_w': 0.86, 'fit_y': 300,
         'clips': C, 'pool': pool, 'usage': 'usage.json', 'seed': seed, 'hook': hook, 'hook_until': hook_until,
         'anchors': anchors, 'overlays': overlays, 'whoosh': 'flash', 'cut': [1.9, 2.4, 2.9], 'sfx': [],
         'capy': 1300, 'words': 2}
    if not hook: P.pop('hook'); P.pop('hook_until')
    json.dump(P, open(f'V{n}.json', 'w'), indent=1, ensure_ascii=False)
STAMP = lambda text, word, occ=0, dur=1.6: {'type': 'stamp', 'text': text, 'word': word, 'occ': occ, 'dur': dur}
END = lambda word, occ=0: {'type': 'end', 'word': word, 'occ': occ}
TAG = lambda text, word, occ=0, dur=1.8, y=210: {'type': 'tag', 'text': text, 'word': word, 'occ': occ, 'dur': dur, 'y': y}
CH = lambda text, word, occ=0, dur=1.8, icon='\u2713': {'type': 'chip', 'text': text, 'word': word, 'occ': occ, 'dur': dur, 'icon': icon}
MO = lambda left, right, word, occ=0, dur=2.4, label='': {'type': 'money', 'left': left, 'right': right, 'word': word, 'occ': occ, 'dur': dur, 'label': label}

# V13 - comparacion de costo: caja de discos / hoja de cortes / rack overland TK-024
plan(13, 'Mas barato que una caja de discos', 'esto.',
     [['esto.', 0, 'T', 4.5], ['mal.', 0, 'U', 1.5], ['1.200', 0, 'P_celular-carpetas', 0],
      ['armada:', 0, 'P_hoja-3-cortes', 0], ['amoladora.', 0, 'T', 7.5], ['justo,', 0, 'Z', 1.5],
      ['overland', 0, 'P_plan-tk-024', 0], ['carpetas:', 0, 'P_celular-carpetas', 0], ['trailers,', 0, 'A', 4.5],
      ['tiza.', 0, 'K', 1.5], ['Toca', 0, 'P_todo-incluido', 0]],
     [CH('+1.200 planos - 10 carpetas', '1.200', dur=2.0), TAG('Hoja 3 - Lista de cortes', 'armada:', dur=2.0),
      TAG('Rack overland para camioneta', 'overland', dur=1.8),
      MO('$456.000', '$855.000 a $1.115.000', '456', label='HIERRO - TE PAGAN', dur=2.8),
      STAMP('VENDIDA', 'rack.', dur=1.8), END('Toca')], 1313)

# V14 - comparacion de costo: tubo de gas / orden de soldadura / parrilla argentina BQ-090
plan(14, 'Mas barato que cargar el tubo', 'esto.',
     [['mezcla', 0, 'D', 1.5], ['mismo.', 0, 'E', 1.5], ['pulso:', 0, 'U', 4.5],
      ['numerado,', 0, 'P_hoja-4-soldadura', 0], ['cordon,', 0, 'U', 7.5], ['panza.', 0, 'V', 1.5],
      ['argentina', 0, 'P_plan-bq-090', 0], ['veinticuatro.', 0, 'Y', 4.5],
      ['carpetas:', 0, 'P_celular-carpetas', 0], ['Toca', 0, 'P_todo-incluido', 0]],
     [TAG('Hoja 4 - Orden de soldadura', 'numerado,', dur=2.2), CH('Sale derecha de una', 'panza.', dur=1.8),
      TAG('Parrilla argentina 1,83 m', 'argentina', dur=1.8),
      MO('$921.000', '$1.550.000 a $2.015.000', '921', label='HIERRO - SE COBRA', dur=2.8),
      CH('10 carpetas - +1.200 planos', 'carpetas:', dur=2.0), END('Toca')], 1414)

# V15 - comparacion de costo: hierro tirado / lista de compras / mesa para motos SH-148
plan(15, 'El hierro que tiras cada mes', 'esto.',
     [['recortes', 0, 'Z', 4.5], ['oxida.', 0, 'B', 1.5], ['ojo.', 0, 'I', 1.5],
      ['hecha.', 0, 'P_hoja-2-compras', 0], ['planchuela,', 0, 'Z', 7.5], ['malla.', 0, 'Q', 1.5],
      ['motos', 0, 'P_plan-sh-148', 0], ['ordenadas', 0, 'P_celular-carpetas', 0], ['Toca', 0, 'P_todo-incluido', 0]],
     [TAG('Hoja 2 - Lista de compras', 'hecha.', dur=2.2), CH('Compras exacto, sin sobrante', 'mano.', dur=1.8),
      TAG('Mesa de trabajo para motos', 'motos', dur=1.8),
      MO('$846.000', '$1.440.000 a $1.870.000', 'motos', label='MATERIAL - SE VENDE', dur=2.8),
      CH('10 carpetas - +1.200 planos', 'ordenadas', dur=2.0), END('Toca')], 1515)

# V19 - que mas sabes hacer (ganador 011 del competidor) / catalogo / isla de cocina FN-107
plan(19, 'Que mas sabes hacer?', 'mostrarle.',
     [['mostrarle.', 0, 'I', 1.5], ['eligio,', 0, 'Q', 4.5], ['mostras:', 0, 'P_celular-carpetas', 0],
      ['camioneta,', 0, 'A', 1.5], ['calculado.', 0, 'P_hoja-1-dibujo', 0], ['isla', 0, 'P_plan-fn-107', 0],
      ['escalera.', 0, 'B', 7.5], ['trabajos.', 1, 'P_celular-carpetas', 0], ['Toca', 0, 'P_todo-incluido', 0]],
     [CH('Ya te compro una vez', 'eligio,', dur=1.8), CH('10 carpetas - +1.200 trabajos', 'mostras:', dur=2.2),
      TAG('Estructura de isla de cocina', 'isla', dur=1.8),
      MO('$708.000', '$1.430.000 a $1.860.000', '708', label='MATERIAL - SE COBRA', dur=2.8),
      STAMP('VENDIDA', 'escalera.', dur=1.8), END('Toca')], 1919)

# V20 - ellos vs nosotros (ganadores 030 y 041) / tres vistas / porta autos TR-129
plan(20, 'Ellos vs. esto', 'herraduras.',
     [['herraduras.', 0, 'I', 4.5], ['colgante.', 0, 'B', 4.5], ['tablillas.', 0, 'N', 1.5],
      ['manivela.', 0, 'Y', 1.5], ['vistas,', 0, 'P_hoja-1-dibujo', 0], ['numerado', 0, 'P_hoja-4-soldadura', 0],
      ['eje:', 0, 'P_plan-tr-129', 0], ['mes.', 0, 'A', 4.5], ['ordenadas', 0, 'P_celular-carpetas', 0],
      ['Toca', 0, 'P_todo-incluido', 0]],
     [TAG('Lo que baja gratis de internet', 'herraduras.', dur=2.0), TAG('Hoja 1 - El dibujo en 3 vistas', 'vistas,', dur=2.0),
      TAG('Porta autos 2,44 x 6,10 doble eje', 'eje:', dur=2.0),
      MO('$7.946.000', '$11.275.000 a $14.660.000', '946', label='HIERRO - SE COBRA', dur=3.0),
      CH('10 carpetas - +1.200 planos', 'ordenadas', dur=2.0), END('Toca')], 2020)

# V21 - cuanto le cobras a tu amigo (ganador 100) / precio sugerido / fogonero BQ-028
plan(21, 'Cuanto le cobras a tu amigo?', 'cobras?',
     [['trabas.', 0, 'I', 1.5], ['regalando.', 0, 'Q', 1.5], ['blando:', 0, 'B', 4.5],
      ['material.', 0, 'P_hoja-2-compras', 0], ['hexagonal', 0, 'P_plan-bq-028', 0],
      ['verguenza:', 0, 'H', 1.5], ['gratis.', 0, 'T', 4.5], ['carpetas.', 0, 'P_celular-carpetas', 0],
      ['Toca', 0, 'P_todo-incluido', 0]],
     [CH('Precio de venta en cada plano', 'material.', dur=2.2), TAG('Fogonero hexagonal 1,22 m', 'hexagonal', dur=1.8),
      MO('$470.000', '$805.000 a $1.045.000', '470', label='HIERRO - SE VENDE', dur=2.8),
      STAMP('VENDIDA', 'listo.', dur=1.8), CH('10 carpetas - +1.200 planos', 'carpetas.', dur=2.0), END('Toca')], 2121)
print('ok', len(POOL))
