# -*- coding: utf-8 -*-
"""Planes de los 6 ads de Noche de Citas Cristiana (Argentina, 2026-11-10).

V1 a V3: clonados de Date Night Cristao (Ana Cristina, BR) plano por plano:
         4 planos de ambiente con el cartel del hook (0 a 6,4 s), 3 hojas del producto a
         pantalla completa con el segundo cartel (6,4 a 12,4 s) y 3 s de cierre con la caja
         blanca del CTA sobre la pareja. 15,4 s, el mismo largo que los de ellos.
V4 a V6: organicos estilo TikTok: mas juego, una sola hoja, cortes mas cortos y carteles tipo
         sticker, como escribe la gente en TikTok.

Los dos formatos van SIN voz y SIN subtitulos: solo la cama bed_calma y los carteles.

Uso: python3 gen_datenight_plans.py   -> escribe V1.json .. V6.json en work/
"""
import os, json

WK = os.path.expanduser('~/Desktop/date-night/anuncios/work')
os.makedirs(WK, exist_ok=True)

VENT = {}
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vent_datenight.py')).read())


def pl(clave, dur, desde):
    """Un plano del clip <clave> que arranca en <desde> segundos."""
    fn, a, b, ex = VENT[clave]
    assert a <= desde and desde + dur <= b + 0.01, 'ventana fuera de rango en %s' % clave
    d = dict(src='../clips/%s.mp4' % fn, dur=dur)
    d['in'] = round(desde, 2)
    for k in ('zoom', 'ybias'):
        if k in ex: d[k] = ex[k]
    return d


def hoja(nombre, dur):
    return dict(src='gfx/%s.png' % nombre, dur=dur)


def dur_wav(p):
    import wave
    with wave.open(p) as w:
        return w.getnframes() / w.getframerate()


MUS = dict(music='music/bed_calma.wav', music_vol=0.60)

# ------------------------------------------------------------------ los 3 clones
CLON = [
    dict(n=1,
         amb=[('p1', 1.0), ('c1', 1.5), ('a1', 1.0), ('c5', 2.0)],
         hojas=['cartas1', 'cartas2', 'devocional'],
         fin=[('p2', 3.0), ('p3', 2.0)],
         cap1='Después de años casados, esto nos devolvió el tema de conversación ❤️',
         cap2='+100 encuentros listos para hacer de a dos: oración, devocional, quiz bíblico, juegos y cultos 🙏',
         cta='TOCÁ EL LINK DE ABAJO'),
    dict(n=2,
         amb=[('a1', 4.0), ('c6', 1.5), ('p2', 1.0), ('c7', 1.0)],
         hojas=['desafios', 'bingo', 'oraciones'],
         fin=[('p1', 5.0), ('p3', 5.0)],
         cap1='Menos que una pizza, y lo tuvimos en el celular en el mismo momento 🍕',
         cap2='Hicimos el primer encuentro esa misma noche. Acceso al toque y 30 días de garantía 🙏❤️',
         cta='EL LINK ESTÁ ACÁ ABAJO 👇'),
    dict(n=3,
         amb=[('c4', 2.0), ('a1', 6.0), ('c2', 1.5), ('p3', 1.0)],
         hojas=['oraciones', 'devocional', 'verdad'],
         fin=[('p2', 6.0), ('p1', 7.5)],
         cap1='«HOY ORAMOS JUNTOS», Y LLEGABA LA NOCHE Y NINGUNO EMPEZABA',
         cap2='Ahora la oración ya viene escrita y la leemos de a dos 🙏❤️',
         cta='TOCÁ EL LINK DE ABAJO'),
]

# ------------------------------------------------------------------ los 3 organicos
ORG = [
    dict(n=4,
         planos=[('p1', 2.5), ('c5', 4.0), ('c1', 3.0), ('p2', 4.5)],
         hoja='cartas2',
         cola=[('c6', 4.0), ('p3', 7.0), ('p1', 8.0), ('c5', 7.5)],
         caps=[('jueves, 22:40, y los dos con el celular en la mano', 0.3, 4.8),
               ('probamos una carta y terminamos hablando dos horas 🙏', 5.2, 10.6)],
         cta='el link está acá abajo 👇'),
    dict(n=5,
         planos=[('a1', 2.0), ('c7', 3.0), ('p2', 7.5), ('c3', 2.0)],
         hoja='desafios',
         cola=[('p1', 4.0), ('c6', 7.0), ('a1', 5.0), ('p3', 8.0)],
         caps=[('nuestra noche de citas es en casa y no gastamos un peso', 0.3, 5.0),
               ('una carta, una oración, y nos quedamos despiertos hasta las 2 ❤️', 5.4, 10.6)],
         cta='link abajo 👇'),
    dict(n=6,
         planos=[('c1', 6.0), ('p3', 3.5), ('c2', 5.0), ('p1', 6.0)],
         hoja='bingo',
         cola=[('c5', 5.5), ('p2', 8.0), ('c6', 2.5), ('c7', 5.0)],
         caps=[('nos tocó la carta 7 y no la vimos venir', 0.3, 4.8),
               ('+100 encuentros para hacer de a dos, sin salir de casa 🙏', 5.2, 10.6)],
         cta='el link está acá abajo 👇'),
]


def escribir(n, plan):
    p = os.path.join(WK, 'V%d.json' % n)
    json.dump(plan, open(p, 'w'), ensure_ascii=False, indent=1)
    print('V%d listo - %d planos - %.1f s' % (n, len(plan['segments']),
                                              sum(s['dur'] for s in plan['segments'])))


for v in CLON:
    segs = [pl(k, 1.6, t) for k, t in v['amb']]
    segs += [hoja(h, 2.0) for h in v['hojas']]
    segs += [pl(k, 1.5, t) for k, t in v['fin']]
    caps = [dict(t0=0, t1=6.4, text=v['cap1'], y=0.235, fs=64),
            dict(t0=6.4, t1=12.4, text=v['cap2'], y=0.235, fs=60),
            dict(t0=12.4, t1=15.4, text=v['cta'], tipo='caja', y=0.30, fs=58)]
    escribir(v['n'], dict(segments=segs, caps=caps, music_in=round(v['n'] * 1.7, 1), **MUS))

for v in ORG:
    # el largo del video lo manda la locucion ya procesada (speed 1.30 + pausas recortadas)
    vo = 'vo/V%d.wav' % v['n']
    seg_vo = dur_wav(os.path.join(WK, vo))
    T = round(seg_vo + 0.6, 2)
    d_hoja = round(T * 0.20, 3)
    d_pl = round((T - d_hoja) / 8, 3)
    segs = [pl(k, d_pl, t) for k, t in v['planos']]
    segs += [hoja(v['hoja'], d_hoja)]
    segs += [pl(k, d_pl, t) for k, t in v['cola']]
    # con voz queda UN cartel de apertura (el de TikTok) y el del CTA; el del medio lo dice ella
    caps = [dict(t0=v['caps'][0][1], t1=v['caps'][0][2], text=v['caps'][0][0],
                 tipo='sticker', y=0.20, fs=52),
            dict(t0=round(T - 3.6, 2), t1=T, text=v['cta'], tipo='sticker', y=0.205, fs=52)]
    escribir(v['n'], dict(segments=segs, caps=caps, vo=vo, vo_vol=1.0,
                          music='music/bed_activa_dn.wav', music_vol=0.22,
                          music_in=round(v['n'] * 2.0, 1)))
