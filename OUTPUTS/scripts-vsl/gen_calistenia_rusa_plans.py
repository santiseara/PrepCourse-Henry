"""Planes de edición del VSL de Calistenia Rusa (2026-10-26).
Copian los momentos de B-roll y las placas del VSL original de Calistenia Asiática.
Editor: edit_vsl_quiz.py · Uso: python3 gen_calistenia_rusa_plans.py
Formato del plan:    [broll, frase_inicio, frase_fin, desde_seg, modo, crop_y?]
Formato de heads:    [frase_ancla, texto, efecto, segundos]
Formato de stickers: [frase_ancla, png, segundos, x, y, ancho, efecto]
"""
import json, os

WD = os.path.expanduser('~/Desktop/calistenia-rusa/vsl/work')
G = 'gfx/'

# ───────────────────────── BLOQUE 1 ─────────────────────────
plan1 = [
    # diagnóstico
    ['anat-testosterona', 'Por el resultado de tu test',   'pero muy común en hombres', 0.3, 'split'],
    ['hombre-panza',      'La caída de testosterona',      'sobre todo en la panza.',   0.5, 'split'],
    ['balanza',           'aunque hagas ejercicio',        'como querrías.',            0.5, 'full'],
    ['espejo-antes',      'Si sentís mucho cansancio',     'y la libido baja',          0.5, 'split'],
    # empatía
    ['hombre-cansado',    'Sé que es frustrante',          'al sacarse fotos.',         0.5, 'split'],
    # mecanismo
    ['anat-cortisol',     'Todo entrenamiento largo',      'hormona del estrés.',       0.3, 'full'],
    ['anat-grasa',        'La grasa se empieza a acumular','medio de la panza.',        0.3, 'full'],
    ['anat-fibras',       'Y los músculos profundos',      'se adormecen.',             0.3, 'split'],
    # la trampa
    ['entrenando',        'El gimnasio y el correr',       'no sostiene.',              0.5, 'split'],
    # la solución
    ['dos-hombres',       'Una técnica de la escuela rusa','control del cuerpo.',       0.5, 'split'],
    ['anat-fibras',       'las fibras profundas despiertan','vuelve a quemar grasa',     2.0, 'full'],
    # el producto
    ['flexiones',         'En mi aplicación vas a tener',  'reactivar la testosterona.', 0.5, 'gs'],
    ['app',               'fue creado exactamente',        'sin vueltas.',              0.3, 'split'],
    ['comida',            'un plan alimentario personalizado', 'te gusta comer',        0.5, 'full'],
]

heads1 = [
    ['Mis felicitaciones',            '',                 'ding',   1.0],
    ['la testosterona más baja',      'TESTOSTERONA BAJA','pop',    2.2],
    ['adormecimiento de las fibras',  'FIBRAS PROFUNDAS\nDORMIDAS', 'pop', 2.4],
    ['No es falta de fuerza de voluntad', '',             'pop',    1.0],
    ['activación de las fibras profundas', '',            'whoosh', 1.0],
    ['método simple que llamé',       '',                 'whoosh', 1.0],
    ['Movimientos sin impacto',       '',                 'pop',    1.0],
]

stickers1 = [
    ['Mis felicitaciones',      G + 'check.png', 1.6, 0,  -240, 1080, 'pop'],
    ['Movimientos sin impacto', G + 'siete.png', 2.4, 0,  -120, 1080, 'pop'],
]

# ───────────────────────── BLOQUE 2 ─────────────────────────
plan2 = [
    ['testimonio',   'Ahora mirá lo que me mandó',   'en veintiún días.',          0.3, 'split'],
    ['entrenando',   'Todo hombre de más de cuarenta', 'empezá ahora.',            1.5, 'split'],
    ['comida',       'menú antiinflamatorio masculino', 'sin pasar hambre.',       1.0, 'full'],
    ['app',          'el método, el plan alimentario', 'acceso es para siempre.',  0.3, 'split'],
    ['flexiones',    'se puede resolver con siete minutos', 'Ahora pensalo bien',  1.0, 'split'],
    ['hombre-cansado','Podés cerrar este video',      'frustración de siempre.',   0.5, 'split'],
    ['testimonio',   'O podés empezar hoy',           'gustándote lo que ves.',    1.5, 'split'],
]

heads2 = [
    ['Bono uno',                  '',          'pop',      1.2],
    ['Bono dos',                  '',          'pop',      1.2],
    ['Bono tres',                 '',          'pop',      1.2],
    ['pagarías más de cincuenta mil', '',      'buzzer',   1.2],
    ['normalmente cuesta cuarenta y siete', '','buzzer',   1.2],
    ['por solo diecisiete mil',   '',          'chaching', 1.4],
    ['te llevás todo',            '',          'whoosh',   1.0],
    ['te devuelvo cada peso',     '',          'sello',    1.2],
    ['por diecisiete mil',        '',          'chaching', 1.4],
    ['hacé clic en el botón',     '',          'whoosh',   1.0],
]

stickers2 = [
    ['Bono uno',                      G + 'bono1.png',    2.6, 0, -120, 1080, 'pop'],
    ['Bono dos',                      G + 'bono2.png',    2.6, 0, -120, 1080, 'pop'],
    ['Bono tres',                     G + 'bono3.png',    2.6, 0, -120, 1080, 'pop'],
    ['pagarías más de cincuenta mil', G + 'anclaje.png',  2.4, 0, -160, 1080, 'pop'],
    ['te llevás todo',                G + 'stack.png',    3.0, 0, -120, 1080, 'pop'],
    ['por solo diecisiete mil',       G + 'precio.png',   3.2, 0, -140, 1080, 'pop'],
    ['te devuelvo cada peso',         G + 'garantia.png', 2.8, 0, -120, 1080, 'pop'],
]

for n, (p, h, s) in enumerate([(plan1, heads1, stickers1), (plan2, heads2, stickers2)], 1):
    for nombre, dato in [(f'plan{n}.json', p), (f'heads{n}.json', h), (f'stickers{n}.json', s)]:
        json.dump(dato, open(os.path.join(WD, nombre), 'w'), indent=1, ensure_ascii=False)
    print(f'bloque {n}: {len(p)} b-rolls, {len(h)} headlines, {len(s)} placas')
