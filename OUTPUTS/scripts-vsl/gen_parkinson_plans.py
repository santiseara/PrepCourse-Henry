# -*- coding: utf-8 -*-
"""Planes de los 6 ads de voz en off de Vence al Parkinson (Argentina, 2026-11-01).
Visual 100% clips de TikTok del nicho (nada de stock ni fotos fijas). Placas blancas con
la palabra clave en dorado, como el ganador del nicho.
Uso: python3 gen_parkinson_plans.py   -> escribe V1.json .. V6.json en ~/Desktop/vence-al-parkinson/anuncios/work/
"""
import os, json

WK = os.path.expanduser('~/Desktop/vence-al-parkinson/anuncios/work')
MUS = os.path.join(WK, 'music/bed_herrero.wav')

# clip -> (inicio util, fin util, extras)  ventanas revisadas en la hoja de contactos
# fam = familia visual: varios clips del mismo creador cuentan como una sola fuente
VENT = {}   # se completa abajo, en CLIPS

SEG = 3.0          # largo de cada recorte del pool
TOPE = 10          # tope de recortes por clip (regla del 30/10)

def construir(clips):
    pool, out = [], {}
    for k, (a, b, ex) in clips.items():
        out[k] = dict(src=f'tiktoks/{k}.mp4', **ex)
        t, n = a, 0
        while t < b - 1.6 and n < TOPE:
            pool.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG; n += 1
    return pool, out

FIN = dict(type='end', head=['VENCE AL', 'PARKINSON'],
           sub='5 TOMOS + 4 BONOS · +1.395 PÁGINAS',
           sub2='ACCESO INMEDIATO · GARANTÍA DE 7 DÍAS',
           cta='Tocá Más información 👇')

def card(text, word, gold=None, dur=2.6, y=900):
    return dict(type='card', text=text, word=word, gold=gold, dur=dur, y=y)

# ---- pool revisado clip por clip en la hoja de contactos (hojas/*.jpg) ----
CLIPS = {
    # fam: creador / fuente visual. Varios clips de la misma fam cuentan como una sola fuente.
    'fisio_395078': (3.5, 13.0, dict(fam='vedius')),        # hombre mayor sentado (el cartel en portugues esta en los primeros 3 s)
    'fisio_673413': (0.0,  9.0, dict(fam='neuroevo')),      # terapeuta trabajando manos y brazos en el living
    'parki_467423': (0.0, 28.0, dict(fam='shaky')),         # temblor comiendo con tenedor
    'parki_345246': (34.0, 78.0, dict(fam='temblando')),    # mujer con Parkinson, de pie en su living
    'fisio_870811': (1.5, 22.0, dict(fam='kriss', zoom=1.30, ybias=0.0)),   # manos: recorte de abajo por la marca de TikTok
    'fisio_990533': (0.0, 40.0, dict(fam='solidarte', zoom=1.30, ybias=1.0)),   # prueba de brazo y mano (recorte de arriba por el logo)
    'cuida_482567': (0.0, 40.0, dict(fam='grandmas')),      # cuidadora pasando a la senora de la silla a la cama
    'cuida_485125': (0.0, 19.0, dict(fam='orfiliah')),      # cuidadora: andador, afeitada, presion, manos (limpio entero)
    'adult_374405': (4.0, 78.0, dict(fam='profero')),       # senora de 103 entrenando (el cartel solo esta en los primeros 3 s)
    'fisio_801173': (0.0, 29.0, dict(fam='vic')),           # fisio con senora: banda, hombro y movilizacion en la cama (limpio entero)
    # --- Vedius (brasilero): demos de ejercicio con fondo blanco. El cartel en portugues va arriba,
    #     asi que van con zoom 1.80 y ybias 1.0 (recorte de arriba) y la ventana corta antes de la placa final.
    'ved_373013': (2.0, 12.0, dict(fam='vedius', zoom=1.80, ybias=1.0)),   # senora mayor, equilibrio entre conos
    'ved_234375': (1.0, 11.0, dict(fam='vedius', zoom=1.80, ybias=1.0)),   # hombre mayor, escalera y pelota
    'ved_233749': (2.0, 12.0, dict(fam='vedius2', zoom=1.80, ybias=1.0)),  # pelota, equilibrio en una pierna
    'ved_022662': (2.0, 11.0, dict(fam='vedius3', zoom=1.80, ybias=1.0)),   # abdominales con pelota en el piso
    'ved_135239': (2.0, 11.0, dict(fam='vedius4', zoom=1.80, ybias=1.0)),   # manos en la zona lumbar
    'gcg_086738': (0.0, 44.0, dict(fam='grandmas2')),                      # cuidadora dandole de tomar a la abuela en la cama
}

VIDEOS = [
    dict(n=1, slug='los-cordones', voz='1 mujer calida', seed=11,
         hook='NO ES EL TEMBLOR. ES EL TERRENO.', hook_until='fecha',
         first=['cuida_485125', 6.0],
         anchors=[['marcha', 0, 'fisio_395078', 3.5], ['bloqueos', 0, 'parki_345246', 34.0],
                  ['páginas', 0, 'fisio_870811', 1.5]],
         overlays=[('TODO LO QUE TODAVÍA HACÉS SOLO', 'terreno', 'SOLO'),
                   ('MARCHA · EQUILIBRIO · RESPIRACIÓN · BLOQUEOS', 'ritmo', None),
                   ('+1.395 PÁGINAS ILUSTRADAS POR NIVEL Y OBJETIVO', 'páginas', '+1.395')],
         fin='Tocá'),
    dict(n=2, slug='la-lista-en-silencio', voz='3 mujer grande', seed=22,
         hook='Y NINGUNA DE ESAS COSAS ES EL TEMBLOR', hook_until='temblor',
         first=['parki_467423', 0.0],
         anchors=[['pies', 0, 'ved_234375', 1.0], ['silla', 0, 'adult_374405', 4.0],
                  ['tomos', 0, 'fisio_395078', 3.5]],
         overlays=[('NO APARECEN EN NINGÚN ESTUDIO', 'Ninguna', None),
                   ('5 TOMOS · PASO A PASO · CON EL DIBUJO AL LADO', 'tomos', '5 TOMOS'),
                   ('QUÉ HACER EL LUNES A LA MAÑANA', 'lunes', 'LUNES')],
         fin='Está'),
    dict(n=3, slug='en-cuotas', voz='1 mujer calida', seed=33,
         hook='NADIE PIERDE LA INDEPENDENCIA DE GOLPE', hook_until='cuotas',
         first=['adult_374405', 4.0],
         anchors=[['baño', 0, 'cuida_482567', 0.0], ['giros', 0, 'ved_373013', 2.0],
                  ['sentado', 0, 'fisio_395078', 3.5]],
         overlays=[('CADA SEMANA SIN TRABAJARLO TE SACA UN POCO MÁS', 'semana', None),
                   ('MARCHA · GIROS · EQUILIBRIO · LEVANTARTE', 'ilustradas', None),
                   ('LA MITAD SE HACEN SENTADO', 'mitad', 'SENTADO')],
         fin='Probalo'),
    dict(n=4, slug='deja-pa-yo-lo-limpio', voz='3 mujer grande', seed=44,
         hook='«DEJÁ, PA, YO LO LIMPIO»', hook_until='limpio',
         first=['cuida_482567', 0.0],
         anchors=[['anota', 0, 'parki_345246', 34.0], ['levantarte', 0, 'cuida_485125', 0.0],
                  ['acompaña', 0, 'cuida_485125', 6.0]],
         overlays=[('EL CUERPO LO ANOTA Y LO ENTREGA', 'anota', 'ANOTA'),
                   ('QUÉ DECIR, QUÉ CALLAR, CUÁNDO ESPERAR', 'decir', None),
                   ('5 TOMOS + 4 GUÍAS ILUSTRADAS', 'cinco', '5 TOMOS')],
         fin='Tocá'),
    dict(n=5, slug='clavada-en-la-puerta', voz='1 mujer calida', seed=55,
         hook='ME QUEDABA CLAVADA EN LA PUERTA DEL BAÑO', hook_until='llamar',
         first=['parki_345246', 34.0],
         anchors=[['protocolo', 0, 'fisio_673413', 0.0], ['freezing', 0, 'parki_345246', 34.0],
                  ['salgo', 0, 'adult_374405', 58.0]],
         overlays=[('UN PROTOCOLO PARA DESTRABAR EL PASO', 'protocolo', 'DESTRABAR'),
                   ('FREEZING · MARCHA · EQUILIBRIO · RESPIRACIÓN', 'freezing', None),
                   ('HOY SALGO SOLA', 'salgo', 'SOLA')],
         fin='El'),
    dict(n=6, slug='lo-ayudas-o-lo-frenas', voz='3 mujer grande', seed=66,
         hook='¿LO AYUDÁS O LO ESTÁS FRENANDO?', hook_until='frenando',
         first=['cuida_485125', 6.0],
         anchors=[['pasillo', 0, 'parki_345246', 34.0], ['bloqueo', 0, 'fisio_673413', 0.0],
                  ['juntos', 0, 'cuida_482567', 0.0]],
         overlays=[('ESO NO TE LO ENSEÑÓ NADIE', 'enseñó', 'NADIE'),
                   ('QUÉ HACER Y QUÉ NO DURANTE UN BLOQUEO', 'bloqueo', 'QUÉ NO'),
                   ('4 TOMOS MÁS PARA HACER JUNTOS EN CASA', 'juntos', 'JUNTOS')],
         fin='Empezá'),
]

pool, clips = construir(CLIPS)
for v in VIDEOS:
    ovs = [card(t, w, g) for (t, w, g) in v['overlays']]
    e = dict(FIN); e['word'] = v['fin']; ovs.append(e)
    P = dict(vo=f"vo/V{v['n']}.wav", script=f"../guiones/V{v['n']}.txt", lang='es',
             speed=1.30, silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], flash=0, words=2,
             seed=v['seed'], usage='usage.json',
             hook=v['hook'], hook_until=v['hook_until'], hook_y=250,
             first=v['first'], anchors=v['anchors'], clips=clips, pool=pool, overlays=ovs,
             music=MUS, music_db=-8, capy=1420)
    json.dump(P, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print(f"V{v['n']}  {v['slug']}  voz {v['voz']}  pool {len(pool)} recortes de {len(clips)} clips")
