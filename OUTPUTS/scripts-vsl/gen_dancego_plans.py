# -*- coding: utf-8 -*-
"""Planes de los 3 ads de voz en off de DanceGo (Argentina, 2026-11-06).

Se clona la edición del DanceGo brasileño (31 ads activos, el más viejo del 7 de enero de 2026):
banda de hook de dos líneas arriba desde el cuadro cero, placas de beneficio ancladas a la palabra
que las nombra, el inserto de la app en el celular y la comunidad de WhatsApp, y una placa de
cierre con el CTA y la flecha. Los subtítulos van bajos, con la palabra activa adentro de una caja
de color, un color por creativo.

El visual es 100 % clip de TikTok (#bailoterapia, #zumbaencasa): clase de baile en estudio y
mujeres bailando en el living frente a la tele, que es el plano firma de la oferta.

La primera letra de cada clave es la FAMILIA (el creador): el editor penaliza repetir familia, así
no se come la tanda una sola creadora. Los clips con cartel arriba van con zoom y ybias 1.0, ya
verificado cuadro por cuadro que el cartel queda afuera.

Uso: python3 gen_dancego_plans.py   -> escribe V1.json .. V3.json en work/
"""
import os, json

WK = os.path.expanduser('~/Desktop/dancego/anuncios/work')
SEG = 4.0
TOPE = 5

# clave: (id de tiktok, desde, hasta, extras)   — una letra por creador
VENT = {
    # karlagaviria6 (rumbaterapia en estudio)
    'A1': ('7610626099621547286', 3, 60, {}),
    'A2': ('7636227519372446979', 3, 59, {}),
    'A3': ('7648125976223681824', 3, 61, {}),
    'A4': ('7649589894406343968', 3, 60, {}),
    'A5': ('7667401144569711904', 1, 13.5, {}),
    'A6': ('7675163312371289377', 3, 60, {}),
    # pao_c_music_baila
    'B1': ('7657358050411449633', 3, 57, {}),
    'B2': ('7664812275684936992', 2, 25, {}),
    'B3': ('7693392764708375840', 1, 12, {}),
    # vibrafit7
    'C1': ('7542629009524526359', 4, 60, {}),
    'C2': ('7548186403595619606', 5, 60, {}),
    'C3': ('7666224013420629281', 3, 60, {}),
    # sarayiceth1
    'D1': ('7666609414261984545', 2, 19, {}),
    'D2': ('7674769209242570017', 3, 59, {}),
    # lilielicar (en casa)
    'E1': ('7508751629449973048', 1, 19, dict(zoom=1.45, ybias=1.0)),
    'E2': ('7692189418844720417', 1, 18, dict(zoom=1.30, ybias=1.0)),
    # una casa por creadora
    'F1': ('7673143882560834829', 11, 30, {}),                              # living con la tele
    'G1': ('7704924884257754382', 3, 86, {}),                               # living, clase sola
    'H1': ('7694331681708215573', 2, 58, dict(zoom=1.45, ybias=1.0)),       # living con luces
    'I1': ('7567089753334582540', 3, 100, dict(zoom=1.45, ybias=1.0)),      # cocina
    'J1': ('7612877286320246046', 1, 26, dict(zoom=1.45, ybias=1.0)),       # living con la tele
    # estudio, una clave por creadora
    'K1': ('7646526700699782421', 2, 28, {}),
    'L1': ('7625664102123293974', 3, 58, {}),
    'M1': ('7704504496507915542', 3, 58, {}),
    'N1': ('7684747281182215445', 3, 38, {}),
    'O1': ('7639051723352460552', 3, 58, {}),
    'P1': ('7600919312077016338', 3, 54, {}),
    'Q1': ('7698245022155607316', 5, 120, {}),
    'R1': ('7704573729669451039', 3, 54, {}),
}

GFX = {'XA': 'app.png', 'XW': 'wpp.png'}


def pool_y_clips():
    pool, clips = [], {}
    for k, (vid, a, b, ex) in VENT.items():
        clips[k] = dict(src=f'tiktoks/{vid}.mp4', fam=str(vid), **ex)
        tramos, t = [], a
        while t < b - 1.8:
            tramos.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
        if len(tramos) > TOPE:
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    for k, fn in GFX.items():
        clips[k] = dict(src=f'gfx/{fn}', fam=k, still=True)
        pool.append([k, 0, 3.4])
    return pool, clips


FIN = dict(sub2='ACCESO POR MAIL Y WHATSAPP EN 2 MINUTOS · GARANTÍA DE 7 DÍAS')

VIDEOS = [
    dict(n=1,
         hi='&H00FFFFFF&', hibox='&H005B3AB2&',          # blanco · caja frambuesa
         hook='El gimnasio entra en la tele de tu living', hook_until='aplicación,',
         first=['P1', 3],
         anchors=[('aplicación,', 0, 'XA', 0), ('tele', 1, 'F1', 11)],
         last='XA',
         overlays=[
             dict(type='chip', word='ciento', text='+150 clases con profes de verdad', icon='✓', dur=2.6),
             dict(type='chip', word='paso', occ=1, text='Paso a paso para principiantes', icon='✓', dur=2.6),
             dict(type='chip', word='vivo.', text='Clases en vivo todas las semanas', icon='✓', dur=2.4),
             dict(type='tag', word='mensualidad.', text='Sin mensualidad · pagás una sola vez', y=230, dur=3.0),
             dict(type='end', word='mirá', head=['DANCEGO', 'BAILÁ EN TU LIVING'],
                  sub='+150 CLASES · DESAFÍO DE 28 DÍAS', cta='Tocá Más información 👇', **FIN),
         ]),
    dict(n=2,
         hi='&H00FFFFFF&', hibox='&H004F6B21&',          # blanco · caja verde
         hook='Diez minutos mientras se hace la cena', hook_until='entera.',
         first=['G1', 3],
         anchors=[('Adentro', 0, 'XA', 0), ('cuerpo', 0, 'I1', 3)],
         last='XA',
         overlays=[
             dict(type='chip', word='veintiocho', occ=0, text='Desafío de 28 días personalizado', icon='✓', dur=2.8),
             dict(type='chip', word='peso,', text='Registro de peso y seguimiento', icon='✓', dur=2.4),
             dict(type='chip', word='Cumbia,', text='Cumbia · cuarteto · salsa · bachata', icon='', dur=2.8),
             dict(type='tag', word='cuota', text='Sin cuota ni mensualidad', y=230, dur=2.8),
             dict(type='end', word='Tocá', head=['DANCEGO', 'DIEZ MINUTOS POR DÍA'],
                  sub='DESAFÍO DE 28 DÍAS · SIN EQUIPO', cta='Armá tu desafío 👇', **FIN),
         ]),
    dict(n=3,
         hi='&H001A1A1A&', hibox='&H00338FD6&',          # tinta · caja ámbar
         hook='En tu casa nadie te ve aprender', hook_until='aprendiendo.',
         first=['J1', 1],
         anchors=[('grupo', 0, 'XW', 0), ('casa', 0, 'E1', 1)],
         last='XW',
         overlays=[
             dict(type='chip', word='principiantes,', text='Clases cortas · sin saltos ni impacto', icon='✓', dur=2.8),
             dict(type='chip', word='vivo', text='Clases en vivo todas las semanas', icon='✓', dur=2.4),
             dict(type='chip', word='recetas', text='Comunidad de WhatsApp + recetario', icon='', dur=2.8),
             dict(type='tag', word='siete', text='7 días de garantía', y=230, dur=2.6),
             dict(type='end', word='Tocá', head=['DANCEGO', 'BAILAR ES EL ENTRENAMIENTO'],
                  sub='COMUNIDAD · CLASES EN VIVO', cta='Empezá hoy 👇', **FIN),
         ]),
]

for v in VIDEOS:
    pool, clips = pool_y_clips()
    plan = dict(
        vo=f"vo/V{v['n']}.wav", script=f"V{v['n']}.txt", lang='es',
        speed=1.30, silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], words=3,
        music='music/bed_activo.wav', music_db=-8,
        hi=v['hi'], hibox=v['hibox'], hibord=20, capy=1420,
        hook=v['hook'], hook_until=v['hook_until'],
        first=v['first'], last=v['last'], seed=v['n'] * 131, usage='usage.json',
        clips=clips, pool=pool, anchors=v['anchors'], overlays=v['overlays'])
    json.dump(plan, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print(f"V{v['n']}.json  ({len(pool)} recortes de {len(clips)} clips)")
