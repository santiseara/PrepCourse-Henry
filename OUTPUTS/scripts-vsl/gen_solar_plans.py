# -*- coding: utf-8 -*-
"""Planes de los 6 ads de voz en off de Solar Installer Pro (mercado ingles, 2026-10-29).
Uso: python3 gen_solar_plans.py   -> escribe V1.json .. V6.json en ~/Desktop/solar-installer-pro/anuncios/work/"""
import os, json

WK = os.path.expanduser('~/Desktop/solar-installer-pro/anuncios/work')

# clip -> (inicio util, fin util, extras). Ventanas revisadas en las hojas de contactos.
# Descartados: los que traen cartel quemado (124677 "automatic solar cleaning system",
# 777478 "solar installations 5kva", 524485), marca de agua movil (413702 "Volta Solar"),
# cara del creador hablando a camara (588750, 469447), 16:9 (484193) y los que no son solar (191169, 963462).
# 904430 se corta en 100 s: despues hay un primer plano de cara y un tramo negro.
# 477294 se corta en 16 s: al final entra un cartel de "contact us today for a free quote".
VENT = {
    'A': (0, 13,  {}),   # 363653 cuadrilla cargando y montando paneles
    'B': (0, 100, {}),   # 904430 POV de manos y herramientas sobre el techo
    'C': (0, 16,  {}),   # 556846 techo, hombre sobre el panel y aerea con pileta
    'D': (0, 10,  {}),   # 853354 cuadrilla de azul con casco montando
    'E': (0, 19,  {}),   # 107627 taladro, escalera y panel: un dia de instalador
    'F': (0, 7,   {}),   # 889030 montaje en piso, estructura
    'G': (0, 16,  {}),   # 303342 inversor y tablero electrico en la pared
    'H': (0, 15,  {}),   # 468270 aerea de techos de teja con paneles
    'I': (0, 17,  {}),   # 736834 cuadrilla sobre techo de chapa
    'J': (0, 20,  {}),   # 819566 trabajo en techo + aerea
    'K': (0, 11,  {}),   # 389550 instalador cargando un panel por el techo
    'L': (0, 18,  {}),   # 200923 instalador, camioneta, app en el celular, aerea
    'M': (0, 31,  {}),   # 927146 cuadrilla instalando sobre tejas
    'N': (0, 16,  {}),   # 528046 botas, taladro y canalizacion (ASMR)
    'P': (0, 48,  {}),   # 571169 ganchos sobre teja, rieles, paneles, grua
    'Q': (0, 10,  {}),   # 437446 paneles terminados sobre el techo
    'R': (0, 4.5, {}),   # 301486 elevador de paneles
    'S': (0, 16,  {}),   # 477294 drone sobre casas con paneles
    'T': (0, 17,  {}),   # 822314 array sobre techo comercial
    'V': (0, 10,  {}),   # 960853 paneles y pantalla del inversor
    'W': (0, 17,  {}),   # 978247 drone subiendo paneles al techo
}
SRC = {'A': '363653', 'B': '904430', 'C': '556846', 'D': '853354', 'E': '107627', 'F': '889030',
       'G': '303342', 'H': '468270', 'I': '736834', 'J': '819566', 'K': '389550', 'L': '200923',
       'M': '927146', 'N': '528046', 'P': '571169', 'Q': '437446', 'R': '301486', 'S': '477294',
       'T': '822314', 'V': '960853', 'W': '978247'}
SEG = 6.5

def pool_y_clips():
    pool, clips = [], {}
    for k, (a, b, ex) in VENT.items():
        clips[k] = dict(src=f'tiktoks/{SRC[k]}.mp4', **ex)
        t = a
        while t < b - 2.0:
            pool.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
    return pool, clips

FIN = dict(type='end', head=['SOLAR INSTALLER PRO'],
           sub='6 MODULES · 5 BONUSES · 20-DAY PLAN',
           sub2='INSTANT ACCESS · 7-DAY GUARANTEE',
           cta='Tap Learn more 👇')

VIDEOS = [
    dict(n=1, slug='no-es-dificil-es-el-orden',
         hook='SOLAR ISN’T HARD. FINDING OUT HOW IS', hook_until='people',
         first=['A', 0], seed=11,
         anchors=[['panels', 0, 'K', 0], ['inverter', 0, 'V', 4],
                  ['Mounting', 0, 'N', 0], ['quote', 0, 'L', 8]],
         overlays=[dict(type='chip', text='SIX MODULES, IN SEQUENCE', icon='✓', word='modules', dur=2.4),
                   dict(type='chip', text='EVERY TEMPLATE ALREADY WRITTEN', icon='✓', word='template', dur=2.4),
                   dict(FIN=1, word='Open')]),
    dict(n=2, slug='los-instaladores-son-el-cuello-de-botella',
         hook='THE PANELS AREN’T THE SHORTAGE', hook_until='installers',
         first=['S', 0], seed=22,
         anchors=[['Roofs', 0, 'H', 0], ['hands', 0, 'B', 10],
                  ['install', 0, 'M', 4], ['contracts', 0, 'P', 14]],
         overlays=[dict(type='chip', text='NO DEGREE · NO YEARS', icon='✓', word='degree', dur=2.4),
                   dict(type='chip', text='SUPPLIER PLAYBOOK + 2 CONTRACTS', icon='✓', word='contracts', dur=2.4),
                   dict(FIN=1, word='Tap')]),
    dict(n=3, slug='te-dejan-apuntes-esto-una-cotizacion',
         hook='THEY LEAVE YOU NOTES. THIS LEAVES YOU A QUOTE', hook_until='client',
         first=['M', 0], seed=33,
         anchors=[['sizing', 0, 'B', 30], ['mounting', 0, 'N', 6],
                  ['playbook', 0, 'P', 20], ['signature', 0, 'L', 10]],
         overlays=[dict(type='chip', text='WRITTEN FOR ENGINEERS, NOT FOR YOU', icon='✓', word='engineers', dur=2.4),
                   dict(type='chip', text='QUOTE · CONTRACTS · SCRIPTS', icon='✓', word='signature', dur=2.4),
                   dict(FIN=1, word='Go')]),
    dict(n=4, slug='dimensionar-es-todo-el-oficio',
         hook='LEARN ONE THING: HOW TO SIZE A SYSTEM', hook_until='correctly',
         first=['Q', 0], seed=44,
         anchors=[['panels', 0, 'K', 0], ['battery', 0, 'G', 0],
                  ['inverter', 0, 'V', 4], ['roof', 1, 'B', 40]],
         overlays=[dict(type='chip', text='ON GRID AND OFF GRID', icon='✓', word='grid', dur=2.4),
                   dict(type='chip', text='WORKED EXAMPLES BESIDE EVERY STEP', icon='✓', word='examples', dur=2.4),
                   dict(FIN=1, word='Tap')]),
    dict(n=5, slug='la-otra-mitad-arranca-cuando-dice-si',
         hook='INSTALLING IT IS HALF THE JOB', hook_until='yes',
         first=['N', 0], seed=55,
         anchors=[['panels', 0, 'A', 0], ['roof', 0, 'B', 55],
                  ['distributors', 0, 'P', 28], ['contract', 0, 'L', 12]],
         overlays=[dict(type='chip', text='REAL DISTRIBUTORS IN YOUR COUNTRY', icon='✓', word='distributors', dur=2.4),
                   dict(type='chip', text='FIVE DOCUMENTS, ALREADY WRITTEN', icon='✓', word='written', dur=2.4),
                   dict(FIN=1, word='Open')]),
    dict(n=6, slug='del-dia-uno-al-dia-veinte',
         hook='DAY ONE TO DAY TWENTY, WRITTEN OUT', hook_until='track',
         first=['W', 0], seed=66,
         anchors=[['Register', 0, 'L', 6], ['wholesale', 0, 'P', 22],
                  ['install', 0, 'I', 0], ['grid', 0, 'T', 0]],
         overlays=[dict(type='chip', text='A CALENDAR, NOT A SYLLABUS', icon='✓', word='order', dur=2.4),
                   dict(type='chip', text='ON YOUR PHONE · YOURS FOR LIFE', icon='✓', word='life', dur=2.4),
                   dict(FIN=1, word='Start')]),
]

pool, clips = pool_y_clips()
for v in VIDEOS:
    ovs = []
    for o in v['overlays']:
        if o.get('FIN'):
            e = dict(FIN); e['word'] = o['word']; ovs.append(e)
        else:
            ovs.append(o)
    P = dict(vo=f"vo/SIP-V{v['n']}.wav", script=f"vo/SIP-V{v['n']}.txt", lang='en',
             speed=1.30, silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], flash=4, words=2,
             music='music/bed_A.wav', music_db=-11,
             seed=v['seed'], usage='usage.json', hook=v['hook'], hook_until=v['hook_until'],
             first=v['first'], anchors=v['anchors'], clips=clips, pool=pool, overlays=ovs)
    json.dump(P, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print(f"V{v['n']}  {v['slug']}  {len(pool)} segmentos")
