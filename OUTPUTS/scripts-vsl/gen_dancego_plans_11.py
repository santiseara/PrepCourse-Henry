# -*- coding: utf-8 -*-
"""Planes de las 3 renovaciones de DanceGo del 2026-11-10, sobre el mismo ganador del 6/11.

Ganador: V1 (`6-11 - 1.mp4`) - "Hay un gimnasio adentro de la tele de tu living".
Cuerpo validado copiado TEXTUAL en los tres; lo que cambia es el FORMATO del hook
(la tanda del 7/11 fueron cuatro declaraciones sobre el mismo objeto, el living/la tele):

Lectura de la cuenta del 10/11 (captura de Santiago, 6 conjuntos a $10 menos uno a $20):
de la tanda del 9/11 vendieron la LISTA ("Anota", $6,57) y el STORYTIME ("Mi primera", $6,69);
la PREGUNTA DEL CLIENTE ("Lo que mas me preguntan") vendio cero en 512 personas. O sea: lo
concreto y en primera persona rinde, lo meta no. Los tres formatos nuevos van por ahi.

  Y1 - prueba social con la cifra de la landing (150 mil mujeres, y casi ninguna sabia bailar)
  Y2 - reencuadre del costo: no agregues nada al dia, move diez minutos de sillon
  Y3 - el mecanismo emocional: no fue fuerza de voluntad, fue una cancion

Y cambia la ESTETICA, que es la otra mitad de una renovacion (checklist del 27/10):
  - otra paleta de caja de subtitulo: crema sobre FRAMBUESA / tinta sobre CREMA / crema sobre VERDE
    (el 9/11 fue crema-sobre-tinta, blanco-sobre-ciruela y blanco-sobre-petroleo)
  - otro ritmo de corte y otro reparto de palabras por subtitulo (3 / 2 / 4)
  - planos nuevos SIN bajar material: offset de +0,8 s (el 9/11 fue +2,0) sobre las mismas
    ventanas ya revisadas, asi que los tramos caen en otro lado y usage7.json penaliza lo usado.
  - la placa de cierre se ancla a `plan`, que aparece UNA sola vez en los tres guiones
    (regla del 9/11: una palabra repetida le adelanta el cierre al segundo 6).

Uso: python3 gen_dancego_plans_11.py  -> escribe Y1.json .. Y3.json en work/
"""
import os, json, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('g7', f'{HERE}/gen_dancego_plans_7.py')
# no se importa (el modulo escribe archivos al cargarse): se copian las tablas a mano
WK = os.path.expanduser('~/Desktop/dancego/anuncios/work')
SEG = 4.0
TOPE = 9
OFF = 0.8            # desplazamiento respecto de la tanda anterior -> ventanas nuevas

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
    # R1 ('7704573729669451039') vetado el 9/11: salon con una piñata colgando, plano lejano
}
GFX = {'XA': 'app.png', 'XW': 'wpp.png'}


def casa2():
    p = f'{WK}/casa2_ok.txt'
    if not os.path.exists(p):
        return {}
    out, i = {}, 0
    for l in open(p):
        l = l.split('#')[0].strip()
        if not l:
            continue
        i += 1
        f = l.split()
        a = float(f[1]) if len(f) > 1 else 1.0
        b = float(f[2]) if len(f) > 2 else 58.0
        ex = dict(zoom=float(f[3]), ybias=1.0) if len(f) > 3 and f[3] != '-' else {}
        out[f'Z{i}'] = (f[0], a, b, ex, 'tiktoks2')
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
        tramos, t = [], a + (OFF if b - a > OFF + SEG + 1.8 else 0)
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

CREMA = '&H00F4F8FB&'
TINTA = '&H001C1A1C&'
FRAMBUESA = '&H005B3AB2&'
VERDE = '&H004F6B21&'

VIDEOS = [
    # ---------- 1: prueba social ----------
    dict(n=1, casa=True, words=3, cut=[1.8, 2.2, 2.7],
         hi=CREMA, hibox=FRAMBUESA,
         hook='150 mil mujeres bailan en su living', hook_until='abren.',
         first='Z3',
         anchors=[('aplicación,', 0, 'XA', 0), ('vivo.', 0, 'XW', 0)],
         last='XA',
         overlays=[
             dict(type='chip', word='ciento', text='+150 clases con profes de verdad', icon='✓', dur=2.6),
             dict(type='chip', word='cuándo.', text='Te marcan qué pie va y cuándo', icon='✓', dur=2.6),
             dict(type='tag', word='mensualidad.', text='Sin mensualidad · pago único', y=230, dur=3.0),
             dict(type='end', word='plan', head=['DANCEGO', 'CASI NINGUNA SABÍA BAILAR'],
                  sub='+150 CLASES · PASO A PASO', cta='Tocá Más información 👇', **FIN),
         ]),
    # ---------- 2: reencuadre del costo ----------
    dict(n=2, casa=True, words=2, cut=[1.4, 1.8, 2.2],
         hi=TINTA, hibox=CREMA,
         hook='No agregues nada: mové diez minutos de sillón', hook_until='van.',
         first='Z6',
         anchors=[('aplicación,', 0, 'XA', 0), ('paso:', 0, 'G1', 0)],
         last='XA',
         overlays=[
             dict(type='chip', word='minutos', text='Clases de 10 minutos', icon='✓', dur=2.4),
             dict(type='chip', word='ciento', text='+150 clases con profes de verdad', icon='✓', dur=2.6),
             dict(type='chip', word='horario.', text='Sin horario · cuando vos puedas', icon='✓', dur=2.4),
             dict(type='tag', word='mensualidad.', text='Sin mensualidad · queda tuyo', y=230, dur=3.0),
             dict(type='end', word='plan', head=['DANCEGO', 'DIEZ MINUTOS, EN TU LIVING'],
                  sub='SIN GIMNASIO · SIN HORARIO', cta='Empezá hoy 👇', **FIN),
         ]),
    # ---------- 3: el mecanismo emocional ----------
    dict(n=3, casa=True, words=4, cut=[2.2, 2.8, 3.4],
         hi=CREMA, hibox=VERDE,
         hook='No fue fuerza de voluntad: fue una canción', hook_until='está.',
         first='Z4',
         anchors=[('aplicación,', 0, 'XA', 0), ('vivo.', 0, 'XW', 0)],
         last='XA',
         overlays=[
             dict(type='chip', word='ciento', text='+150 clases con profes de verdad', icon='✓', dur=2.8),
             dict(type='chip', word='paso:', text='Paso a paso para principiantes', icon='✓', dur=2.8),
             dict(type='tag', word='mensualidad.', text='Sin mensualidad · pagás una vez', y=230, dur=3.0),
             dict(type='end', word='plan', head=['DANCEGO', 'BAILAR NO SE SIENTE COMO ENTRENAR'],
                  sub='+150 CLASES · DESAFÍO DE 28 DÍAS', cta='Mirá tu plan 👇', **FIN),
         ]),
]

EX = casa2()
for v in VIDEOS:
    pool, clips = pool_y_clips(EX if v['casa'] else None)
    fk = v['first']
    seg = next((s for s in pool if s[0] == fk), None)
    if seg is None:
        raise SystemExit(f"first {fk} no esta en el pool del video {v['n']}")
    anch = []
    for word, occ, key, _st in v['anchors']:
        s = next((s for s in pool if s[0] == key), None)
        if s is None:
            raise SystemExit(f"anchor {key} no esta en el pool del video {v['n']}")
        anch.append([word, occ, key, s[1]])
    plan = dict(
        vo=f"vo/Y{v['n']}.wav", script=f"Y{v['n']}.txt", lang='es',
        speed=1.30, silence=[0.26, 0.12], cut=v['cut'], words=v['words'],
        music='music/bed_activo.wav', music_db=-8,
        hi=v['hi'], hibox=v['hibox'], hibord=20, capy=1420,
        hook=v['hook'], hook_until=v['hook_until'],
        first=[seg[0], seg[1]], last=v['last'], seed=1500 + v['n'] * 307, usage='usage7.json',
        clips=clips, pool=pool, anchors=anch, overlays=v['overlays'])
    json.dump(plan, open(f"{WK}/Y{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print(f"Y{v['n']}.json  ({len(pool)} recortes de {len(clips)} clips)  first={seg[0]}@{seg[1]}  anchors={[a[2]+'@'+str(a[3]) for a in anch]}")
