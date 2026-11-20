# -*- coding: utf-8 -*-
"""Planes de los 6 ads de Crochet Painting (mercado ingles, 2026-11-20),
clonando la edicion de "Emily Carter" (www.crochetpaint.com).

Lo que se copia de ellos, medido sobre sus 11 creativos de mas impresiones:
  - 9:16, 1:00 a 2:00, voz en off de mujer y cama musical por debajo. Sin SFX.
  - SIN SUBTITULOS.
  - PRECIOS EN VERDE LIMA con borde negro, anclados a la palabra que los dice.
  - PLACA DE CIERRE fucsia de dos renglones ("just tap / Learn More.") con corazon.
  - 100 % b-roll de TikTok del nicho.

Uso: python3 gen_crochet_plans.py <carpeta_work>   -> V1.json .. V6.json
"""
import os, re, sys, json

WK = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser('~/Desktop/crochet-paint/anuncios/work')
sys.path.insert(0, WK)
from vent_crochet import VENT, FAM

SEG = 2.6          # largo de cada tramo candidato
TOPE = 8           # maximo de recortes por clip


def pool_y_clips():
    pool, clips = [], {}
    for k, v in VENT.items():
        vid, a, b = v[0], v[1], v[2]
        ex = v[3] if len(v) > 3 else {}
        clips[k] = dict(src='clips/%s.mp4' % vid, fam=FAM.get(vid, vid), **ex)
        tramos, t = [], a
        while t < b - 1.6:
            tramos.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
        if len(tramos) > TOPE:
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    return pool, clips


def occ(script, frase, palabra):
    """Cuantas veces aparece <palabra> antes de <frase> en el guion."""
    txt = script.lower()
    i = txt.find(frase.lower())
    if i < 0:
        raise SystemExit('no esta la frase: ' + frase)
    pre = re.findall(r"[\w'-]+", txt[:i])
    return sum(1 for w in pre if re.sub(r"[^\w]", '', w) == re.sub(r"[^\w]", '', palabra.lower()))


# (frase del guion que ubica el numero, palabra ancla, texto verde)
VERDES = {
 1: [("fifteen dollars of yarn", "fifteen", "$15"),
     ("a hundred and fifty", "fifty", "$150"),
     ("twenty-five dollars of yarn, three hundred", "twenty-five", "$25"),
     ("twenty-five dollars of yarn, three hundred", "three", "$300")],
 2: [("around ten thousand dollars a month", "ten", "$10,000/mo"),
     ("about twenty-five dollars of yarn", "twenty-five", "$25"),
     ("I sell it for three hundred", "three", "$300")],
 3: [("about twenty-five dollars of yarn", "twenty-five", "$25"),
     ("sells for three hundred", "three", "$300"),
     ("two hundred and seventy-five left", "seventy-five", "$275")],
 4: [("I see three hundred dollars", "three", "$300"),
     ("Twenty-five dollars of yarn to start", "twenty-five", "$25")],
 5: [("Nobody pays three hundred dollars for crochet", "three", "$300"),
     ("they go for six", "six", "$6"),
     ("a hundred and fifty, three hundred, four hundred", "fifty", "$150"),
     ("four hundred, out of twenty-five", "four", "$400"),
     ("out of twenty-five dollars of yarn", "twenty-five", "$25"),
     ("little rugs for ten dollars", "ten", "$10")],
 6: [("nine hundred dollars on yarn", "nine", "$900"),
     ("three thousand nine hundred a month", "three", "$3,900/mo"),
     ("fifteen hundred dollars selling", "fifteen", "$1,500"),
     ("I sold it for three hundred", "three", "$300"),
     ("Twenty-five dollars of yarn", "twenty-five", "$25")],
}

# clip del primer plano y del ultimo, uno distinto por video (se completan a mano)
VIDEOS = json.load(open(os.path.join(WK, 'videos.json')))

for v in VIDEOS:
    n = v['n']
    pool, clips = pool_y_clips()
    script = open(os.path.join(WK, 'guiones', 'V%d.txt' % n)).read()
    overlays = []
    for frase, pal, txt in VERDES[n]:
        overlays.append(dict(type='green', word=pal, occ=occ(script, frase, pal),
                             text=txt, dur=2.0, y=860, size=165))
    # placa de cierre: su "just tap / Learn More." con el corazon
    cta_frase = v.get('cta_frase', 'tap')
    overlays.append(dict(type='cta', word='tap', occ=occ(script, cta_frase, 'tap'),
                         lines=['just tap', 'Learn More.'], y=820, size=100))
    plan = dict(
        vo='voces/V%d.wav' % n, script='guiones/V%d.txt' % n, lang='en',
        speed=1.20, silence=[0.26, 0.12], cut=[1.7, 2.2, 2.7],
        nosubs=True, nosfx=True,
        music='music/bed.wav', music_db=-11,
        first=[v['first'], next(s[1] for s in pool if s[0] == v['first'])],
        last=v['last'],
        seed=n * 977, usage='usage.json',
        whoosh=[], flash=0, clips=clips, pool=pool,
        anchors=[], overlays=overlays)
    json.dump(plan, open(os.path.join(WK, 'V%d.json' % n), 'w'), ensure_ascii=False, indent=1)
    print('V%d listo - %d tramos, %d placas' % (n, len(pool), len(overlays)))
