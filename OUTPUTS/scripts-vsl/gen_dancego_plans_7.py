# -*- coding: utf-8 -*-
"""Planes de los 4 testeos de DanceGo del 2026-11-07, sobre el ganador del 6/11.

Ganador: V1 (`6-11 - 1.mp4`) — "Hay un gimnasio adentro de la tele de tu living".
Angulo: el gimnasio ya esta en tu casa (se prende como la tele), nadie te ve aprender,
sin horario y sin mensualidad.

  W1 y W2 = variables cercanas: hook nuevo + el cuerpo validado del ganador.
            Mismo pool de clips que el ganador, con seed distinto.
  W3 y W4 = videos nuevos sobre el mismo angulo, con cuerpo propio.
            Pool reforzado con los clips nuevos de #zumbaencasa (plano firma: living + tele),
            que es justo lo que escaseaba en la tanda 1 (7 de 26).

Los clips nuevos que pasaron la revision cuadro por cuadro van en work/casa2_ok.txt
(un id por linea, con 'desde hasta' opcional). Si el archivo no existe, W3 y W4 corren
con el pool viejo.

Uso: python3 gen_dancego_plans_7.py   -> escribe W1.json .. W4.json en work/
"""
import os, json

WK = os.path.expanduser('~/Desktop/dancego/anuncios/work')
SEG = 4.0
TOPE = 5

# --- pool de la tanda 1 (ya revisado cuadro por cuadro el 6/11) ---
VENT = {
    'A1': ('7610626099621547286', 3, 60, {}),
    'A2': ('7636227519372446979', 3, 59, {}),
    'A3': ('7648125976223681824', 3, 61, {}),
    'A4': ('7649589894406343968', 3, 60, {}),
    'A5': ('7667401144569711904', 1, 13.5, {}),
    'A6': ('7675163312371289377', 3, 60, {}),
    'B1': ('7657358050411449633', 3, 57, {}),
    'B2': ('7664812275684936992', 2, 25, {}),
    'C1': ('7542629009524526359', 4, 60, {}),
    'C2': ('7548186403595619606', 5, 60, {}),
    'C3': ('7666224013420629281', 3, 60, {}),
    'D1': ('7666609414261984545', 2, 19, {}),
    'D2': ('7674769209242570017', 3, 59, {}),
    'E1': ('7508751629449973048', 1, 19, dict(zoom=1.45, ybias=1.0)),
    'E2': ('7692189418844720417', 1, 18, dict(zoom=1.30, ybias=1.0)),
    'F1': ('7673143882560834829', 11, 30, {}),
    'G1': ('7704924884257754382', 3, 86, {}),
    'H1': ('7694331681708215573', 2, 58, dict(zoom=1.45, ybias=1.0)),
    'I1': ('7567089753334582540', 3, 100, dict(zoom=1.45, ybias=1.0)),
    'L1': ('7625664102123293974', 3, 58, {}),
    'M1': ('7704504496507915542', 3, 58, {}),
    'N1': ('7684747281182215445', 3, 38, {}),
    'O1': ('7639051723352460552', 3, 58, {}),
    'P1': ('7600919312077016338', 3, 54, {}),
    'Q1': ('7698245022155607316', 5, 120, {}),
    'R1': ('7704573729669451039', 3, 54, {}),
}

GFX = {'XA': 'app.png', 'XW': 'wpp.png'}


def casa2():
    """Clips nuevos de living (tiktoks2/) que pasaron la revision."""
    p = f'{WK}/casa2_ok.txt'
    if not os.path.exists(p):
        return {}
    out = {}
    i = 0
    for l in open(p):
        l = l.split('#')[0].strip()
        if not l:
            continue
        i += 1
        f = l.split()
        vid = f[0]
        a = float(f[1]) if len(f) > 1 else 1.0
        b = float(f[2]) if len(f) > 2 else 58.0
        ex = {}
        if len(f) > 3 and f[3] != '-':
            ex = dict(zoom=float(f[3]), ybias=1.0)
        out[f'Z{i}'] = (vid, a, b, ex, 'tiktoks2')
    return out


def pool_y_clips(extra=None):
    pool, clips = [], {}
    items = dict(VENT)
    for k, v in (extra or {}).items():
        items[k] = v
    for k, v in items.items():
        vid, a, b, ex = v[0], v[1], v[2], v[3]
        carpeta = v[4] if len(v) > 4 else 'tiktoks'
        clips[k] = dict(src=f'{carpeta}/{vid}.mp4', fam=str(vid), **ex)
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
    # ---------- 1 y 2: variables cercanas al ganador ----------
    dict(n=1, casa=False,
         hi='&H00FFFFFF&', hibox='&H005B3AB2&',          # blanco · caja frambuesa (la del ganador)
         hook='Tu living ya tiene todo lo que hace falta', hook_until='piso.',
         first=['F1', 11],
         anchors=[('aplicación,', 0, 'XA', 0), ('tele', 1, 'G1', 3)],
         last='XA',
         overlays=[
             dict(type='chip', word='ciento', text='+150 clases con profes de verdad', icon='✓', dur=2.6),
             dict(type='chip', word='paso:', text='Paso a paso para principiantes', icon='✓', dur=2.6),
             dict(type='chip', word='vivo.', text='Clases en vivo todas las semanas', icon='✓', dur=2.4),
             dict(type='tag', word='mensualidad:', text='Sin mensualidad · pagás una sola vez', y=230, dur=3.0),
             dict(type='end', word='mirá', head=['DANCEGO', 'BAILÁ EN TU LIVING'],
                  sub='+150 CLASES · DESAFÍO DE 28 DÍAS', cta='Tocá Más información 👇', **FIN),
         ]),
    dict(n=2, casa=False,
         hi='&H00FFFFFF&', hibox='&H00A8456B&',          # blanco · caja violeta
         hook='El gimnasio que no te hace salir de casa', hook_until='casa.',
         first=['H1', 2],
         anchors=[('aplicación', 0, 'XA', 0), ('living,', 0, 'F1', 11)],
         last='XA',
         overlays=[
             dict(type='chip', word='ciento', text='+150 clases con profes de verdad', icon='✓', dur=2.6),
             dict(type='chip', word='paso:', text='Paso a paso para principiantes', icon='✓', dur=2.6),
             dict(type='chip', word='vivo.', text='Clases en vivo todas las semanas', icon='✓', dur=2.4),
             dict(type='tag', word='mensualidad:', text='Sin mensualidad · entrás una vez', y=230, dur=3.0),
             dict(type='end', word='Tocá', head=['DANCEGO', 'SIN SALIR DE TU CASA'],
                  sub='+150 CLASES · SIN HORARIO', cta='Empezá hoy 👇', **FIN),
         ]),
    # ---------- 3 y 4: videos nuevos, mismo angulo ----------
    dict(n=3, casa=True,
         hi='&H00FFFFFF&', hibox='&H004F6B21&',          # blanco · caja verde
         hook='El gimnasio está a tres pasos del sillón', hook_until='sillón.',
         first=['Z1', 1],                                   # arranca en el plano firma: living + tele
         anchors=[('ritmo', 0, 'XA', 0), ('tele', 0, 'Z3', 7)],
         last='XA',
         overlays=[
             dict(type='chip', word='seis', text='Abierto a cualquier hora', icon='✓', dur=2.6),
             dict(type='chip', word='profes', text='Profes que te marcan el paso', icon='✓', dur=2.6),
             dict(type='chip', word='Cumbia,', text='Cumbia · cuarteto · salsa · bachata', icon='', dur=2.8),
             dict(type='tag', word='cuota', text='Sin cuota mensual · pago único', y=230, dur=2.8),
             dict(type='end', word='Tocá', head=['DANCEGO', 'A TRES PASOS DEL SILLÓN'],
                  sub='CLASES DE 10 MINUTOS · SIN EQUIPO', cta='Mirá tu plan 👇', **FIN),
         ]),
    dict(n=4, casa=True,
         hi='&H001A1A1A&', hibox='&H00338FD6&',          # tinta · caja ámbar
         hook='La misma tele, pero parada', hook_until='muevas.',
         first=['Z3', 7],                                   # arranca en el living con la tele grande
         anchors=[('capítulo', 0, 'XA', 0), ('parada.', 0, 'Z2', 1)],
         last='XA',
         overlays=[
             dict(type='chip', word='principiantes,', text='Para principiantes · sin saltos', icon='✓', dur=2.8),
             dict(type='chip', word='vivo', text='Clases en vivo todas las semanas', icon='✓', dur=2.4),
             dict(type='chip', word='cumbia,', text='Cumbia · cuarteto · salsa · bachata', icon='', dur=2.8),
             dict(type='tag', word='mensualidad:', text='Sin mensualidad · queda tuyo', y=230, dur=2.8),
             dict(type='end', word='Tocá', head=['DANCEGO', 'DIEZ MINUTOS, DE PIE'],
                  sub='+150 CLASES · CLASES EN VIVO', cta='Tocá Más información 👇', **FIN),
         ]),
]

EX = casa2()
for v in VIDEOS:
    pool, clips = pool_y_clips(EX if v['casa'] else None)
    plan = dict(
        vo=f"vo/W{v['n']}.wav", script=f"W{v['n']}.txt", lang='es',
        speed=1.30, silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], words=3,
        music='music/bed_activo.wav', music_db=-8,
        hi=v['hi'], hibox=v['hibox'], hibord=20, capy=1420,
        hook=v['hook'], hook_until=v['hook_until'],
        first=v['first'], last=v['last'], seed=700 + v['n'] * 137, usage='usage7.json',
        clips=clips, pool=pool, anchors=v['anchors'], overlays=v['overlays'])
    json.dump(plan, open(f"{WK}/W{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print(f"W{v['n']}.json  ({len(pool)} recortes de {len(clips)} clips)" + ('  [+living nuevo]' if v['casa'] and EX else ''))
