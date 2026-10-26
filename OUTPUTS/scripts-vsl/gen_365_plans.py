import json, os, re, subprocess, string
# Planes de los 6 ads de 365 Actividades Imprimibles - v2 (2026-10-26, con visuales de TikTok).
# Editor: OUTPUTS/scripts-vsl/edit_365.py
FF = os.path.expanduser('~/bin/ffmpeg')
BASE = os.path.dirname(os.path.abspath(__file__))
LETTERS = string.ascii_uppercase + string.ascii_lowercase
# @dccraftlab: maquinas de carton con motor (poleas, engranajes, escaleras mecanicas, cintas). Sin subtitulos, 9:16.
TT = ['7668984113969351967',  # escalera mecanica de carton (pedido por Santiago)
      '7661443609115282696',  # STEM con vasos de papel y carton (pedido por Santiago)
      '7681964611632893215', '7679087114570468639',
      '7678749716326272287', '7677099754882452767',
      '7676783690214657310', '7676380727834987806', '7676368296760904990', '7676158888353254686',
      '7675289155198258462', '7674112666641845534', '7673433674670525726',
      '7673047124384222495', '7672468170719890718', '7671599296604638495', '7671595502999260447',
      '7670880358031723806', '7669892758588378399', '7669526363111476511', '7668778943977114911',
      '7668767195861683487', '7668177366715354398', '7667849932635753758', '7667670861876333854',
      '7667094781050457374', '7666182328456154398']
STOCK = ['mk42166', 'mk34145', 'mk10471', 'mk36046', 'mk43325']   # caras de chicos, lo unico que no hay en los TikToks
STILLS = ['land17', 'land04', 'land09', 'land11', 'land13', 'land15', 'land16', 'land39',
          'land03', 'land21', 'land30', 'land33', 'land35', 'land37', 'land38', 'land06']
def dur(p):
    r = subprocess.run([FF, '-i', os.path.join(BASE, p)], capture_output=True, text=True).stderr
    h, m, s = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r).groups(); return int(h) * 3600 + int(m) * 60 + float(s)
C, SEGS, K = {}, {}, {}
DESDE = {'7661443609115282696': 9.0}      # los primeros 9 s son la creadora hablando a camara
ZOOM = {'7668984113969351967': (1.20, 0.95)}   # recorta el cartelito "Electric power gate" de arriba
for i, v in enumerate(TT):
    k = LETTERS[i]; K[v] = k; p = f'tiktoks/{v}.mp4'; C[k] = {'src': p}
    if v in ZOOM: C[k]['zoom'], C[k]['ybias'] = ZOOM[v]
    d = dur(p); t = DESDE.get(v, 0.8); SEGS[k] = []
    while t + 2.4 <= d - 0.4: SEGS[k].append([k, round(t, 1), round(t + 2.4, 1)]); t += 2.4
    if not SEGS[k]: SEGS[k] = [[k, 0.1, max(1.2, d - 0.2)]]
for j, v in enumerate(STOCK):
    k = LETTERS[len(TT) + j]; K[v] = k; p = f'broll/{v}.mp4'; C[k] = {'src': p}
    d = dur(p); t = 1.0; SEGS[k] = []
    while t + 2.4 <= d - 0.4: SEGS[k].append([k, round(t, 1), round(t + 2.4, 1)]); t += 2.4
    if not SEGS[k]: SEGS[k] = [[k, 0.2, min(2.4, d - 0.2)]]
for s in STILLS:
    C['P_' + s] = {'src': f'stills/{s}.png', 'still': True,
                   'fit': s in ('land04', 'land09', 'land11', 'land13', 'land15', 'land16', 'land39', 'land17')}
    SEGS['P_' + s] = [['P_' + s, 0, 2.4]]
T = [K[v] for v in TT]; S = [K[v] for v in STOCK]
MUS = {1: 'A', 2: 'B', 3: 'C', 4: 'B', 5: 'A', 6: 'C'}
def plan(n, usa, hook, hook_until, anchors, overlays, seed):
    pool = [s for k in list(usa) + [a[2] for a in anchors] for s in SEGS[k]]
    P = {'vo': f'vo/V{n}.wav', 'script': f'vo/V{n}.txt', 'speed': 1.30, 'silence': [0.26, 0.12], 'lang': 'es',
         'music': f'music/bed_{MUS[n]}.wav', 'music_db': -9, 'flash': 4, 'progress': True, 'fit_w': 0.92, 'fit_y': 420,
         'clips': C, 'pool': pool, 'usage': 'usage.json', 'seed': seed, 'hook': hook, 'hook_until': hook_until,
         'anchors': anchors, 'overlays': overlays, 'whoosh': 'flash', 'cut': [1.7, 2.1, 2.6], 'sfx': [],
         'capy': 1330, 'words': 2}
    json.dump(P, open(os.path.join(BASE, f'V{n}.json'), 'w'), indent=1, ensure_ascii=False)
CH = lambda text, word, occ=0, dur=2.0: {'type': 'chip', 'text': text, 'word': word, 'occ': occ, 'dur': dur, 'icon': '✓'}
END = lambda word, occ=0: {'type': 'end', 'word': word, 'occ': occ}
L = lambda s: 'P_' + s
G_ = K['7668984113969351967']  # porton electrico de carton (pedido de Santiago)
M = K['7661443609115282696']   # STEM con vasos de papel (pedido de Santiago)
ESC = K['7677099754882452767'] # escalera mecanica
PARK = K['7667094781050457374']# torre de estacionamiento con autitos

# V1 - el inventor escondido
plan(1, T[2:10] + [S[0], S[4]], 'Desarmó el juguete para ver qué tenía adentro', 'funciona.',
     [['juguete', 0, S[4], 1.0], ['Robots', 0, L('land37'), 0], ['poleas,', 0, ESC, 0.8], ['vehículos', 0, PARK, 0.8], ['mueven.', 0, G_, 2.0],
      ['Imprimes', 0, L('land17'), 0], ['experimentos', 0, M, 9.0], ['imprimir', 0, L('land06'), 0]],
     [CH('+390 PROYECTOS IMPRIMIBLES', 'noventa'), CH('DE 4 A 12 AÑOS', 'doce'), END('Toca')], 101)

# V2 - dos horas sin el celular
plan(2, T[10:18] + [S[1], S[2]], 'Dos horas sin pedir el celular', 'tarde.',
     [['auto', 0, L('land03'), 0], ['grúa.', 0, L('land33'), 0], ['brazo', 0, ESC, 0.8], ['grúa', 0, G_, 2.0],
      ['proyectos', 0, L('land17'), 0], ['casa,', 0, M, 11.4]],
     [CH('SIN PELEAS NI NEGOCIACIÓN', 'negociación,'), CH('+390 PROYECTOS · 6 BONOS', 'proyectos'), END('Entra')], 202)

# V3 - "yo no se nada de robotica"
plan(3, T[18:26] + [S[3], S[0]], 'Yo tampoco sé nada de robótica', 'tampoco.',
     [['dibujado', 0, L('land39'), 0], ['pilas.', 0, G_, 2.0], ['mueve,', 0, ESC, 3.2], ['tapitas,', 0, M, 11.4], ['pantalla.', 0, S[1], 1.0],
      ['cuarenta', 0, L('land09'), 0], ['experimentos', 0, L('land15'), 0], ['concentración.', 0, L('land13'), 0]],
     [CH('PASO A PASO, CON DIBUJOS', 'dibujado'), CH('CARTÓN, BOTELLAS Y TAPITAS', 'Cartón,'), END('Toca')], 303)

# V4 - la tarde de lluvia
plan(4, T[26:] + T[2:6] + [S[2]], 'Llueve y no hay plan', 'lado.',
     [['pantalla,', 0, S[2], 1.0], ['abro', 0, L('land17'), 0], ['experimento', 0, M, 14.0], ['armar.', 0, G_, 2.0],
      ['robot', 0, L('land38'), 0], ['papel.', 0, L('land21'), 0], ['proyectos,', 0, L('land04'), 0]],
     [CH('UNA CAJA Y DOS BOTELLAS', 'botellas,'), CH('DE 4 A 12 AÑOS', 'doce'), END('Está')], 404)

# V5 - el juguete que dura dos dias
plan(5, T[6:14] + [S[0], S[3]], 'El juguete dura dos días', 'cama.',
     [['cama.', 0, S[0], 1.0], ['imprimir,', 0, L('land17'), 0], ['gomita.', 0, L('land03'), 0],
      ['cocina.', 0, L('land15'), 0], ['robótico', 0, ESC, 5.6], ['brazo', 0, G_, 2.0], ['arma,', 0, M, 16.2], ['Robótica,', 0, L('land39'), 0]],
     [CH('SE VUELVE A IMPRIMIR SIEMPRE', 'gasta.'), CH('SIN KITS CAROS', 'caros'), END('Toca')], 505)

# V6 - "mira, lo hice yo solo"
plan(6, T[14:22] + [S[4], S[1]], 'Mira, lo hice yo solo', 'funciona.',
     [['ruedas.', 0, L('land03'), 0], ['solo.', 0, S[4], 1.0], ['robótica', 0, L('land39'), 0],
      ['experimentos', 0, M, 21.2], ['arma.', 0, G_, 2.0], ['plantillas', 0, L('land17'), 0], ['proyectos,', 0, L('land30'), 0]],
     [CH('PACIENCIA, FOCO Y ORGULLO', 'entrena.'), CH('+390 PROYECTOS · 6 BONOS', 'proyectos,'), END('Toca')], 606)
print('planes V1..V6 listos (TikTok)')
