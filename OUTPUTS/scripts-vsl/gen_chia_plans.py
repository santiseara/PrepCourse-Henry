import json, os, re, subprocess
# Planes de los 6 ads de Protocolo Chia 28D (2026-10-26). Editor: OUTPUTS/scripts-vsl/edit_chia.py
B = '../broll/'
M = {f'c{i:02d}': chr(64 + i) for i in range(1, 14)}
DESDE = {'E': 7.5, 'J': 7.5}      # c05 arranca con el subtitulo quemado y c10 con el envase de una marca de yogur
CLIPS = ['c01-licuado-papaya-manzana', 'c02-tres-frascos-pudding', 'c03-pudding-frutilla', 'c04-licuado-chia-linaza',
         'c05-agua-chia-limon', 'c06-agua-pepino-menta', 'c07-demo-gel-vaso', 'c08-gelatina-jamaica',
         'c09-gelatina-cubos', 'c10-vasito-yogur-chia', 'c11-gel-jugo-rojo-a', 'c12-frasco-de-chia', 'c13-intestino-3d']
def dur(p):
    r = subprocess.run([os.path.expanduser('~/bin/ffmpeg'), '-i', p], capture_output=True, text=True).stderr
    h, m, s = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r).groups(); return int(h) * 3600 + int(m) * 60 + float(s)
C, SEGS = {}, {}
for f in CLIPS:
    k = M[f[:3]]; p = B + f + '.mp4'; C[k] = {'src': p}
    d = dur(p); t = DESDE.get(k, 1.5); SEGS[k] = []
    while t + 3 <= d - 0.8: SEGS[k].append([k, round(t, 1), round(t + 3, 1)]); t += 3
    if not SEGS[k]: SEGS[k] = [[k, 0.2, min(3, d - 0.2)]]
MUS = {1: 'A', 2: 'B', 3: 'C', 4: 'A', 5: 'B', 6: 'C'}
def plan(n, usa, hook, hook_until, anchors, overlays, seed):
    pool = [s for k in usa for s in SEGS[k]]
    P = {'vo': f'vo/V{n}.wav', 'script': f'vo/V{n}.txt', 'speed': 1.20, 'silence': [0.26, 0.12], 'lang': 'es',
         'music': f'music/bed_{MUS[n]}.wav', 'music_db': -9, 'flash': 4, 'progress': True,
         'clips': C, 'pool': pool, 'usage': 'usage.json', 'seed': seed, 'hook': hook, 'hook_until': hook_until,
         'anchors': anchors, 'overlays': overlays, 'whoosh': 'flash', 'cut': [1.9, 2.4, 2.9], 'sfx': [],
         'capy': 1330, 'words': 3}
    json.dump(P, open(f'V{n}.json', 'w'), indent=1, ensure_ascii=False)
CH = lambda text, word, occ=0, dur=2.0: {'type': 'chip', 'text': text, 'word': word, 'occ': occ, 'dur': dur, 'icon': '✓'}
END = lambda word, occ=0: {'type': 'end', 'word': word, 'occ': occ,
                           'head': ['HAZ EL TEST', 'DE 1 MINUTO'], 'sub': 'PLAN DE 28 DÍAS · RECETAS · APP',
                           'sub2': 'CON LO QUE YA HAY EN TU COCINA', 'cta': 'Toca Más información'}

# V1 - el vaso de agua con chia y limon antes de comer
plan(1, ['E', 'G', 'F', 'K', 'A', 'D'], 'El vaso antes de comer', 'comer.',
     [['cucharada', 0, 'E', 7.5], ['gel.', 0, 'G', 4.5], ['exprimo', 0, 'E', 19.5],
      ['picotear.', 0, 'A', 10.5], ['seguidas,', 0, 'K', 1.5], ['recetas', 0, 'D', 10.5]],
     [CH('30 MINUTOS ANTES DE COMER', 'treinta'), CH('TEST DE 1 MINUTO · GRATIS', 'test'), END('Toca', 1)], 101)

# V2 - tres frascos el domingo
plan(2, ['B', 'C', 'J', 'A', 'L'], 'Tres frascos, toda la semana', 'semana.',
     [['domingos', 0, 'B', 1.5], ['frascos.', 0, 'B', 13.5], ['cacao', 0, 'J', 7.5],
      ['café.', 0, 'B', 40.5], ['postre.', 0, 'C', 16.5], ['galletas', 0, 'A', 43.5],
      ['semanas,', 0, 'C', 40.5]],
     [CH('3 FRASCOS · UN DOMINGO', 'frascos.'), CH('TEST DE 1 MINUTO', 'test.'), END('Toca')], 202)

# V3 - el error: la chia seca no sirve
plan(3, ['D', 'G', 'L', 'A', 'B', 'J'], 'Así se desperdicia la chía', 'mitad.',
     [['seca', 0, 'J', 10.5], ['hidratada.', 0, 'D', 1.5], ['cucharadas', 0, 'D', 7.5],
      ['gel', 0, 'G', 7.5], ['semilla.', 0, 'L', 1.5], ['almacén,', 0, 'A', 22.5],
      ['recetas', 0, 'B', 28.5]],
     [CH('2 CUCHARADAS · 30 MINUTOS', 'minutos,'), CH('HIDRATADA, NO SECA', 'Seca,'), END('Está', 2)], 303)

# V4 - el antojo de la noche: gelatina de jamaica
plan(4, ['H', 'I', 'J', 'C', 'K'], 'Lo de las once de la noche', 'tele.',
     [['tele.', 0, 'J', 7.5], ['jamaica', 0, 'H', 7.5], ['adentro.', 0, 'H', 19.5],
      ['cubos,', 0, 'H', 43.5], ['canela.', 0, 'I', 1.5], ['refrigerador.', 0, 'C', 31.5],
      ['semanas.', 0, 'K', 1.5]],
     [CH('SIN AZÚCAR', 'azúcar,'), CH('UNA NOCHE EN EL REFRIGERADOR', 'ingredientes'), END('Toca', 1)], 404)

# V5 - escepticismo: no es una pastilla
plan(5, ['G', 'K', 'L', 'M', 'F', 'E', 'A', 'D', 'J'], 'No es una pastilla', 'nada.',
     [['medicamento,', 0, 'K', 1.5], ['semilla', 0, 'G', 1.5], ['Mírala:', 0, 'G', 4.5],
      ['gel.', 0, 'L', 1.5], ['feed', 0, 'F', 1.5], ['semanas', 0, 'M', 1.5],
      ['recetas', 0, 'E', 22.5]],
     [CH('UNA SEMILLA, NO UNA PASTILLA', 'monedas'), CH('4 SEMANAS · UNA FUNCIÓN CADA UNA', 'función'), END('Toca')], 505)

# V6 - el orden de las cuatro semanas
plan(6, ['A', 'C', 'H', 'J', 'M', 'B', 'D', 'L'], 'El orden de las cuatro semanas', 'orden.',
     [['siembra:', 0, 'A', 4.5], ['estómago', 0, 'M', 1.5], ['tercera', 0, 'H', 25.5],
      ['desayuno,', 0, 'B', 22.5], ['app', 0, 'C', 49.5], ['cocina.', 0, 'J', 10.5],
      ['Responde', 0, 'L', 1.5]],
     [CH('SEMANA 1 · SEMBRAR', 'siembra:'), CH('SEMANA 2 · SANAR', 'tranquilo.'),
      CH('SEMANA 3 · SOLTAR', 'nota,'), CH('SEMANA 4 · SUMAR', 'termina.'), END('Toca', 1)], 606)
print('planes V1..V6 listos')
