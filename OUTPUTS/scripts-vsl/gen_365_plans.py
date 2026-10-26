import json, os, re, subprocess, string
# Planes de los 6 ads de 365 Actividades Imprimibles (2026-10-26). Editor: OUTPUTS/scripts-vsl/edit_365.py
FF = os.path.expanduser('~/bin/ffmpeg')
LETTERS = string.ascii_uppercase + string.ascii_lowercase
LEGO = ['mk34145', 'mk42165', 'mk42166', 'mk42167', 'mk42168', 'mk42169', 'mk42175', 'mk42183', 'mk42196', 'mk42197', 'mk6301']
ARTE = ['mk40306', 'mk40310', 'mk40322', 'mk41602', 'mk41611', 'mk43444', 'mk43446', 'mk30232', 'mk29983', 'mk29984', 'mk16556']   # sin pintura abstracta ni adultos en caballete
CHICOS = ['mk10471', 'mk36046', 'mk43325', 'mk43352', 'mk45166', 'mk4553', 'mk4569', 'mk40417']
CLIPS = LEGO + ARTE + CHICOS
K = {c: LETTERS[i] for i, c in enumerate(CLIPS)}          # la inicial de la clave = la fuente, por eso una letra por clip
def dur(p):
    r = subprocess.run([FF, '-i', p], capture_output=True, text=True).stderr
    h, m, s = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r).groups(); return int(h) * 3600 + int(m) * 60 + float(s)
C, SEGS = {}, {}
for c in CLIPS:
    k = K[c]; p = f'broll/{c}.mp4'; C[k] = {'src': p, 'zoom': 1.0}
    d = dur(os.path.join(os.path.dirname(os.path.abspath(__file__)), p)); t = 1.0; SEGS[k] = []
    while t + 2.6 <= d - 0.5: SEGS[k].append([k, round(t, 1), round(t + 2.6, 1)]); t += 2.6
    if not SEGS[k]: SEGS[k] = [[k, 0.2, min(2.6, d - 0.2)]]
STILLS = ['land17', 'land04', 'land09', 'land11', 'land13', 'land15', 'land16', 'land39',
          'land03', 'land21', 'land30', 'land33', 'land35', 'land37', 'land38', 'land06']
for s in STILLS:
    C['P_' + s] = {'src': f'stills/{s}.png', 'still': True, 'fit': s in ('land04','land09','land11','land13','land15','land16','land39','land17')}
    SEGS['P_' + s] = [['P_' + s, 0, 2.6]]
MUS = {1: 'A', 2: 'B', 3: 'C', 4: 'B', 5: 'A', 6: 'C'}
def plan(n, usa, hook, hook_until, anchors, overlays, seed):
    keys = list(usa) + [a[2] for a in anchors]
    pool = [s for k in keys for s in SEGS[k]]
    P = {'vo': f'vo/V{n}.wav', 'script': f'vo/V{n}.txt', 'speed': 1.22, 'silence': [0.26, 0.12], 'lang': 'es',
         'music': f'music/bed_{MUS[n]}.wav', 'music_db': -9, 'flash': 4, 'progress': True, 'fit_w': 0.92, 'fit_y': 420,
         'clips': C, 'pool': pool, 'usage': 'usage.json', 'seed': seed, 'hook': hook, 'hook_until': hook_until,
         'anchors': anchors, 'overlays': overlays, 'whoosh': 'flash', 'cut': [1.7, 2.1, 2.6], 'sfx': [],
         'capy': 1330, 'words': 2}
    json.dump(P, open(f'V{n}.json', 'w'), indent=1, ensure_ascii=False)
CH = lambda text, word, occ=0, dur=2.0: {'type': 'chip', 'text': text, 'word': word, 'occ': occ, 'dur': dur, 'icon': '✓'}
END = lambda word, occ=0: {'type': 'end', 'word': word, 'occ': occ}
L = lambda s: 'P_' + s
A = [K[c] for c in ARTE]; G = [K[c] for c in LEGO]; N = [K[c] for c in CHICOS]

# V1 - el inventor escondido (familia mas vieja del competidor, 6 ago)
plan(1, G[:4] + A[:5] + N[:4], 'Desarmó el juguete para ver qué tenía adentro', 'funciona.',
     [['juguete', 0, K['mk43352'], 1.0], ['Robots', 0, L('land37'), 0], ['poleas,', 0, L('land03'), 0],
      ['Imprimes', 0, L('land17'), 0], ['experimentos', 0, L('land15'), 0], ['imprimir', 0, L('land06'), 0]],
     [CH('+390 PROYECTOS IMPRIMIBLES', 'noventa'), CH('DE 4 A 12 AÑOS', 'doce'), END('Toca')], 101)

# V2 - dos horas sin el celular (testimonio con numero, 15 oct)
plan(2, G[4:8] + A[5:10] + N[4:], 'Dos horas sin pedir el celular', 'tarde.',
     [['auto', 0, L('land03'), 0], ['grúa.', 0, L('land33'), 0], ['brazo', 0, K['mk43325'], 1.0],
      ['proyectos', 0, L('land17'), 0], ['casa,', 0, L('land30'), 0]],
     [CH('SIN PELEAS NI NEGOCIACIÓN', 'negociación,'), CH('+390 PROYECTOS · 6 BONOS', 'proyectos'), END('Entra')], 202)

# V3 - "yo no se nada de robotica" (el mas nuevo, 22 oct)
plan(3, G[8:] + A[7:] + N[:3], 'Yo tampoco sé nada de robótica', 'tampoco.',
     [['dibujado', 0, L('land39'), 0], ['pilas.', 0, L('land35'), 0], ['pantalla.', 0, K['mk34145'], 1.0],
      ['cuarenta', 0, L('land09'), 0], ['experimentos', 0, L('land15'), 0], ['concentración.', 0, L('land13'), 0]],
     [CH('PASO A PASO, CON DIBUJOS', 'dibujado'), CH('CARTÓN, BOTELLAS Y TAPITAS', 'Cartón,'), END('Toca')], 303)

# V4 - la tarde de lluvia / "me aburro"
plan(4, A[:6] + G[2:6] + N[2:6], 'Llueve y no hay plan', 'lado.',
     [['pantalla,', 0, K['mk4569'], 1.0], ['abro', 0, L('land17'), 0], ['experimento', 0, L('land15'), 0],
      ['robot', 0, L('land38'), 0], ['papel.', 0, L('land21'), 0], ['proyectos,', 0, L('land04'), 0]],
     [CH('UNA CAJA Y DOS BOTELLAS', 'botellas,'), CH('DE 4 A 12 AÑOS', 'doce'), END('Está')], 404)

# V5 - el juguete que dura dos dias
plan(5, N[:4] + G[6:10] + A[5:10], 'El juguete dura dos días', 'cama.',
     [['cama.', 0, K['mk45166'], 1.0], ['imprimir,', 0, L('land17'), 0], ['gomita.', 0, L('land03'), 0],
      ['cocina.', 0, L('land15'), 0], ['robótico', 0, L('land33'), 0], ['Robótica,', 0, L('land39'), 0]],
     [CH('SE VUELVE A IMPRIMIR SIEMPRE', 'gasta.'), CH('SIN KITS CAROS', 'caros'), END('Toca')], 505)

# V6 - "mira, lo hice yo solo" (el orgullo)
plan(6, A[6:11] + G[1:5] + N[3:7], 'Mira, lo hice yo solo', 'funciona.',
     [['ruedas.', 0, L('land03'), 0], ['solo.', 0, K['mk43325'], 1.0], ['robótica', 0, L('land39'), 0],
      ['experimentos', 0, L('land15'), 0], ['plantillas', 0, L('land17'), 0], ['proyectos,', 0, L('land30'), 0]],
     [CH('PACIENCIA, FOCO Y ORGULLO', 'entrena.'), CH('+390 PROYECTOS · 6 BONOS', 'proyectos,'), END('Toca')], 606)
print('planes V1..V6 listos')
