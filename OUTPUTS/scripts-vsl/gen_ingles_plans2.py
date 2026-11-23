# -*- coding: utf-8 -*-
"""Planes de los 6 ads de Inglés con Mapas Mentales — VERSIÓN 2 (2026-11-22, noche).

Corrección de Santiago: *"Horribles las visuales, usá las originales"*. El visual sale 100 % de
los **creativos originales de Fluente com Legenda** bajados de la Biblioteca de Anuncios en
720x1280, recortados arriba del watermark con `zoom=1.25 / ybias=0` (equivale a
`crop=576:1024:72:0`) — el editor lo hace sin recomprimir.

Voces: **3 de mujer (Sulafat: V1, V2, V5) y 3 de hombre (Orus: V3, V4, V6)**, mismos guiones.

Cada tramo del pool es una ventana medida sin cara y sin captura del área de miembros
(`vent_orig.py`). Los anchors atan la hoja que ELLOS muestran a la palabra que la nombra en
nuestro guion, usando el OCR de sus propios cuadros.

Uso: python3 gen_ingles_plans2.py <workdir>
"""
import os, re, sys, json, glob

W = sys.argv[1]
SEG = 2.8          # largo del tramo candidato
TOPE = 5           # tramos por creativo (son 30: alcanza y sobra)

AMARILLO = '&H0000D7FF&'
NEGRO = '&H00000000&'

# voz por video: M = mujer (Sulafat), H = hombre (Orus)
VOZ = {1: 'M', 2: 'M', 3: 'H', 4: 'H', 5: 'M', 6: 'H'}

# vent_final = ventanas sin cara, sin captura del area de miembros y SIN EL SUBTITULO QUEMADO
# de ellos (se detecta por el amarillo de su palabra resaltada, ver amarillo_ingles.py)
vent = {}
for p in sorted(glob.glob(W + '/vent_final*.json')):
    vent.update(json.load(open(p)))

# creativos que se caen enteros: sticker de comentario arriba y pantalla de Drive/navegador
FUERA_CLIP = {'fl_1019815801137438',   # sticker "Replying to lady_araujoo" en 38 s
              'fl_1582187809861026',   # sticker "Qual sua duvida?"
              'fl_2260021771240937',   # sticker "Eu nao sei nada de ingles..." en 64 s
              'fl_1059287213603254'}   # pantalla del Drive con el menu en portugues
# tramos con el CTA de ellos quemado ("Clique em Saiba Mais", "+300 Mapas Mentais do...")
FUERA_TRAMO = [('fl_1077063898568963', 48.7), ('fl_1097359486340358', 32.2),
               ('fl_1108531905113632', 61.7), ('fl_1391104526346280', 40.7),
               ('fl_1623484912489693', 38.7),
               ('fl_1804290747491270', 4.15)]   # barra del navegador en portugues

# ------------------------------------------------------------------ pool
clips, pool, idx = {}, [], {}
k = 0
# segundos donde se ve GRANDE su logo impreso en la hoja (marca_ingles.py)
MARCA = {}
for p_ in sorted(glob.glob(W + '/marca*.json')):
    MARCA.update(json.load(open(p_)))


def partir(vid, w):
    """Corta la ventana sacando los segundos con la marca del ganador."""
    malos = set(MARCA.get(vid, []))
    if not malos:
        return [w]
    a, b, tx = w[0], w[1], (w[2] if len(w) > 2 else [])
    fuera = sorted(x for x in malos if a - 1.2 <= x <= b + 0.2)
    trozos, cur = [], a
    for x in fuera:
        if x - 0.5 - cur >= 2.5:
            trozos.append([round(cur, 2), round(x - 0.5, 2), tx])
        cur = max(cur, x + 1.5)
    if b - cur >= 2.5:
        trozos.append([round(cur, 2), round(b, 2), tx])
    return trozos


for vid, v in sorted(vent.items()):
    if vid in FUERA_CLIP:
        continue
    ventanas = []
    for w in (v.get('ventanas') or []):
        if any(vid == fv and abs(w[0] - ft) < 6 for fv, ft in FUERA_TRAMO):
            continue
        ventanas += partir(vid, w)
    if not ventanas:
        continue
    key = 'o%03d' % k; k += 1
    clips[key] = dict(src='orig/%s.mp4' % vid, fam=vid, zoom=1.25, ybias=0.0)
    idx[vid] = key
    tramos = []
    for w in ventanas:
        a, b = w[0], w[1]
        t = a
        while t < b - SEG * 0.8:
            tramos.append([key, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
    if len(tramos) > TOPE:
        paso = len(tramos) / TOPE
        tramos = [tramos[int(i * paso)] for i in range(TOPE)]
    pool += tramos

# ------------------------------------------------------------------ anchors por OCR
# palabra del guion -> lo que tiene que estar escrito en SU cuadro
TEMAS = {
    'much':        ('much', 'many'),
    'was':         ('was', 'were'),
    'have':        ('have', 'has'),
    'aeropuerto':  ('aeroporto', 'airport', 'embarque', 'voo'),
    'partes':      ('corpo', 'body', 'cabeça', 'cabeca'),
    'frases':      ('frases', 'pronúncia', 'pronuncia'),
    'ruta':        ('rota', 'fluência', 'fluencia'),
    'phrasal':     ('phrasal',),
    'expresiones': ('expressões', 'expressoes', 'gírias', 'girias', 'idioms'),
    'bonus':       ('bônus', 'bonus'),
    'nivel':       ('a1', 'a2', 'b1', 'b2', 'c1', 'c2'),
}


def buscar(tema):
    """Primer tramo del pool cuyo texto OCR contenga alguna de las palabras del tema."""
    pistas = TEMAS[tema]
    for vid, v in sorted(vent.items()):
        if vid not in idx:
            continue
        for w in (v.get('ventanas') or []):
            txt = ' '.join(w[2] if len(w) > 2 else []).lower()
            if any(p in txt for p in pistas):
                key = idx[vid]
                seg = next((s for s in pool if s[0] == key and s[1] >= w[0] - 0.01 and s[1] < w[1]), None)
                if seg:
                    return [seg[0], seg[1]]
    return None


# (frase que ubica la ocurrencia, palabra ancla, tema)
ANCLAS = {
 1: [('el significado, la estructura', 'significado', 'much'),
     ('el del aeropuerto', 'aeropuerto', 'aeropuerto'),
     ('del nivel A2', 'nivel', 'nivel'),
     ('te llevás cinco bonus', 'bonus', 'bonus'),
     ('las 500 frases más usadas', 'frases', 'frases'),
     ('la ruta de la fluidez', 'ruta', 'ruta')],
 2: [('las 500 frases más usadas', 'frases', 'frases'),
     ('partes del cuerpo', 'partes', 'partes'),
     ('la ruta de la fluidez', 'ruta', 'ruta'),
     ('más cinco bonus exclusivos', 'bonus', 'bonus')],
 3: [('el much y el many', 'much', 'much'),
     ('del nivel A1 hasta', 'nivel', 'nivel'),
     ('los cinco bonus que vienen', 'bonus', 'bonus')],
 4: [('el was y el were', 'was', 'was'),
     ('entre los niveles A1 y C2', 'niveles', 'nivel'),
     ('cinco bonus exclusivos', 'bonus', 'bonus')],
 5: [('para todos los niveles', 'niveles', 'nivel'),
     ('las 500 frases más usadas', 'frases', 'frases'),
     ('la ruta de la fluidez', 'ruta', 'ruta'),
     ('100 phrasal verbs', 'phrasal', 'phrasal'),
     ('150 expresiones y modismos', 'expresiones', 'expresiones')],
 6: [('El have y el has', 'have', 'have'),
     ('del nivel A1 hasta el nivel C2', 'nivel', 'nivel'),
     ('cinco bonus especiales', 'bonus', 'bonus')],
}


def occ(script, frase, palabra):
    txt = script.lower()
    i = txt.find(frase.lower())
    if i < 0:
        raise SystemExit('no está la frase: ' + frase)
    n = lambda w: re.sub(r'[^\wáéíóúñü]', '', w.lower())
    return sum(1 for w in re.findall(r"[\w'áéíóúñü-]+", txt[:i]) if n(w) == n(palabra))


print('pool: %d tramos de %d creativos' % (len(pool), len(clips)))
encontrados = {t: buscar(t) for t in TEMAS}
print('temas atados:', ', '.join(t for t, v in encontrados.items() if v) or 'ninguno')
print('temas sin material:', ', '.join(t for t, v in encontrados.items() if not v) or '-')

for n in (1, 2, 3, 4, 5, 6):
    script = open(W + '/voz/V%d.txt' % n).read()
    anchors = []
    usados = set()
    for frase, pal, tema in ANCLAS[n]:
        seg = encontrados.get(tema)
        if not seg or tuple(seg) in usados:
            continue
        usados.add(tuple(seg))
        anchors.append([pal, occ(script, frase, pal), seg[0], seg[1]])
    plan = dict(
        vo='voz/V%d.wav' % n, script='voz/V%d.txt' % n, lang='es',
        speed=1.20, silence=[0.30, 0.14], cut=[1.9, 2.5, 3.2],
        nosfx=True, words=3, noflip=True,   # el material es texto: espejarlo lo deja al reves
        hook='', hook_until='',
        hi=AMARILLO, hibox=NEGRO, hibord=0, capy=1540, pop=False,
        font='Montserrat ExtraBold', fsize=58, spacing=6, outline=4, shadow=3,
        seed=n * 409, usage='usage2.json',
        whoosh=[], flash=0, clips=clips, pool=pool, anchors=anchors, overlays=[])
    json.dump(plan, open('%s/W%d.json' % (W, n), 'w'), ensure_ascii=False, indent=1)
    print('W%d listo · voz %s · %d anclas' % (n, VOZ[n], len(anchors)))
