# -*- coding: utf-8 -*-
"""Planes de los 6 ads de Inglés con Mapas Mentales (mercado argentino, 2026-11-22).

Formato copiado de Fluente com Legenda (mapa.fluentecomlegenda.com):
  - 9:16, POV sobre el material, sin cara.
  - Se lee UN mapa en voz alta: el ad es el material, no el avatar.
  - Corte cada ~2,4 s (más lento que un ad de b-roll puro: hay que poder leer la hoja).
  - Voz Sulafat rioplatense en off, speed 1.20.
  - Subtítulos quemados abajo, 3 palabras, la que suena en AMARILLO, sobre la banda oscura
    que las páginas dejan libre (la hoja termina en 1500 de 1920).

El material en pantalla son las páginas en español de `gfx_ingles.py` (el producto que
modelamos es brasileño y su material está en portugués), más el b-roll real de TikTok.

Uso: python3 gen_ingles_plans.py <workdir>
"""
import os, re, sys, json, glob

W = sys.argv[1]
SEG = 2.8          # largo del tramo candidato de b-roll
TOPE = 3           # tramos por clip
BORDE = 0.6

AMARILLO = '&H0000D7FF&'
NEGRO = '&H00000000&'

# El b-roll se elige A OJO sobre la hoja de contactos: en este nicho (apuntes, mapas mentales,
# impresoras) el OCR marca texto en casi todos los cuadros, porque el tema ES papel escrito.
# `seleccion.txt`: una linea por clip, "id [t0 t1]" con la ventana util medida a mano.
import subprocess
def dur(p):
    r = subprocess.run([os.path.expanduser('~/bin/ffmpeg'), '-i', p], capture_output=True, text=True).stderr
    m = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r)
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3)) if m else 0.0

ver = {}
for ln in open(W + '/seleccion.txt'):
    ln = ln.split('#')[0].strip()
    if not ln: continue
    campos = ln.split()
    vid = campos[0]
    p = W + '/clips/%s.mp4' % vid
    if not os.path.exists(p):
        raise SystemExit('falta el clip ' + vid)
    D = dur(p)
    a = float(campos[1]) if len(campos) > 2 else BORDE
    b = float(campos[2]) if len(campos) > 2 else D - BORDE
    ver[vid] = dict(ok=True, dur=D, a=a, b=min(b, D - 0.15))

extras = json.load(open(W + '/extras.json')) if os.path.exists(W + '/extras.json') else {}
autores = {}
for ln in open(W + '/autores.txt'):
    ln = ln.strip()
    if '/' in ln:
        a, i = ln.rsplit('/', 1)
        autores[i] = a or i


def pool_broll():
    pool, clips = [], {}
    k = 0
    for vid, v in sorted(ver.items()):
        a, b = v['a'], v['b']
        if b - a < SEG: continue
        key = 'c%03d' % k; k += 1
        clips[key] = dict(src='clips/%s.mp4' % vid, fam=autores.get(vid, vid), **extras.get(vid, {}))
        tramos, t = [], a
        while t < b - SEG * 0.8:
            tramos.append([key, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
        if len(tramos) > TOPE:
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    return pool, clips


def pool_gfx(veces=3):
    """Las páginas del producto. fam = la página (así no se encadenan dos encuadres de la misma)."""
    pool, clips = [], {}
    for p in sorted(glob.glob(W + '/gfx/*.png')):
        key = os.path.basename(p)[:-4]
        clips[key] = dict(src='gfx/%s.png' % key, still=True, fam=re.sub(r'_[ab]$', '', key))
        for i in range(veces):
            pool.append([key, i * 0.5, 6.0])
    return pool, clips


def occ(script, frase, palabra):
    """Cuántas veces aparece `palabra` antes de `frase` (para anclar la ocurrencia correcta)."""
    txt = script.lower()
    i = txt.find(frase.lower())
    if i < 0:
        raise SystemExit('no está la frase: ' + frase)
    n = lambda w: re.sub(r'[^\wáéíóúñü]', '', w.lower())
    return sum(1 for w in re.findall(r"[\w'áéíóúñü-]+", txt[:i]) if n(w) == n(palabra))


# (frase que ubica la ocurrencia, palabra ancla, página)
ANCLAS = {
 1: [('Son mapas mentales de inglés', 'mapas', 'grilla_mapas'),
     ('el significado, la estructura', 'significado', 'mapa_much_many_a'),
     ('el error más común', 'error', 'mapa_much_many_b'),
     ('el del aeropuerto', 'aeropuerto', 'mapa_aeropuerto'),
     ('hasta un mini diálogo', 'diálogo', 'mapa_aeropuerto_b'),
     ('del nivel A2', 'nivel', 'niveles'),
     ('te llevás cinco bonus', 'bonus', 'bonus_los_cinco'),
     ('las 500 frases más usadas', 'frases', 'bonus_frases_1'),
     ('la frase con la pronunciación escrita', 'pronunciación', 'bonus_frases_1_b'),
     ('la ruta de la fluidez', 'ruta', 'bonus_ruta'),
     ('un plan diario de estudio', 'plan', 'bonus_ruta_b')],
 2: [('las 500 frases más usadas', 'frases', 'bonus_frases_1'),
     ('trabajo y estudio', 'trabajo', 'bonus_frases_2'),
     ('Son más de 300', '300', 'grilla_mapas'),
     ('partes del cuerpo', 'partes', 'mapa_cuerpo'),
     ('el dato rápido', 'dato', 'mapa_cuerpo_b'),
     ('la ruta de la fluidez', 'ruta', 'bonus_ruta'),
     ('más cinco bonus exclusivos', 'bonus', 'bonus_los_cinco')],
 3: [('el much y el many', 'much', 'mapa_much_many'),
     ('con sustantivos contables', 'contables', 'mapa_much_many_a'),
     ('el error más común', 'error', 'mapa_much_many_b'),
     ('más de 300 mapas mentales', '300', 'grilla_mapas'),
     ('del nivel A1 hasta', 'nivel', 'niveles'),
     ('los cinco bonus que vienen', 'bonus', 'bonus_los_cinco')],
 4: [('el was y el were', 'was', 'mapa_was_were'),
     ('Usamos was con I', 'Usamos', 'mapa_was_were_a'),
     ('las respuestas cortas', 'respuestas', 'mapa_was_were_b'),
     ('más de 300 mapas mentales', '300', 'grilla_mapas'),
     ('entre los niveles A1 y C2', 'niveles', 'niveles'),
     ('cinco bonus exclusivos', 'bonus', 'bonus_los_cinco')],
 5: [('para todos los niveles', 'niveles', 'niveles'),
     ('más de 82 ebooks', '82', 'bonus_ebooks'),
     ('las 500 frases más usadas', 'frases', 'bonus_frases_1'),
     ('la ruta de la fluidez', 'ruta', 'bonus_ruta'),
     ('100 phrasal verbs', 'phrasal', 'bonus_phrasal'),
     ('150 expresiones y modismos', 'expresiones', 'bonus_expresiones'),
     ('vienen estos bonus especiales', 'bonus', 'bonus_los_cinco')],
 6: [('El have y el has', 'have', 'mapa_have_has'),
     ('frases afirmativas con ejemplos', 'afirmativas', 'mapa_have_has_a'),
     ('el error más común', 'error', 'mapa_have_has_b'),
     ('más de 300 mapas mentales', '300', 'grilla_mapas'),
     ('del nivel A1 hasta el nivel C2', 'nivel', 'niveles'),
     ('cinco bonus especiales', 'bonus', 'bonus_los_cinco')],
}

# Primer plano de cada video: el hook manda (apuntes desparramados, impresora, etc.).
# Se nombra el id de TikTok; si ese clip no quedo en la seleccion, el editor elige solo.
PRIMEROS = {}
if os.path.exists(W + '/primeros.txt'):
    for ln in open(W + '/primeros.txt'):
        ln = ln.split('#')[0].split()
        if len(ln) >= 2: PRIMEROS[int(ln[0])] = ln[1]

pb, cb = pool_broll()
pg, cg = pool_gfx()
print('b-roll: %d tramos de %d clips · páginas: %d' % (len(pb), len(cb), len(cg)))

for n in (1, 2, 3, 4, 5, 6):
    script = open(W + '/voz/V%d.txt' % n).read()
    clips = dict(cb); clips.update(cg)
    pool = list(pb) + list(pg)
    primero = {}
    vid0 = PRIMEROS.get(n)
    if vid0:
        k0 = next((k for k, c in cb.items() if c['src'].endswith(vid0 + '.mp4')), None)
        seg0 = next((t for t in pb if t[0] == k0), None) if k0 else None
        if seg0: primero = dict(first=[seg0[0], seg0[1]])
    anchors = []
    for frase, pal, gfx in ANCLAS[n]:
        if gfx not in clips:
            raise SystemExit('falta la página ' + gfx)
        anchors.append([pal, occ(script, frase, pal), gfx, 0.0])
    plan = dict(
        vo='voz/V%d.wav' % n, script='voz/V%d.txt' % n, lang='es',
        speed=1.20, silence=[0.30, 0.14], cut=[1.9, 2.5, 3.2],
        nosfx=True, words=3,
        hook='', hook_until='',
        hi=AMARILLO, hibox=NEGRO, hibord=0, capy=1700, pop=False,
        font='Montserrat ExtraBold', fsize=58, spacing=6, outline=4, shadow=3,
        seed=n * 617, usage='usage.json',
        **primero,
        whoosh=[], flash=0, clips=clips, pool=pool, anchors=anchors, overlays=[])
    json.dump(plan, open('%s/V%d.json' % (W, n), 'w'), ensure_ascii=False, indent=1)
    print('V%d listo · %d anclas' % (n, len(anchors)))
