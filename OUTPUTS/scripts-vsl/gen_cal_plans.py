# -*- coding: utf-8 -*-
"""Planes de los 6 ads de voz en off de los Calendarios 2027 (mercado ingles, 2026-11-04).
Pool propio de TikTok: flores de papel, tarjetas pop-up, tijera sobre cartulina, impresora en casa y
puestos de feria artesanal (tags popupcard, paperflowers, craftfair, epsonecotank). Revisados uno por uno
en hojas de contactos: los que traen cartel quemado arriba van con zoom/ybias, los de cara a camara,
marca de agua grande, texto en espanol o personajes con copyright quedaron afuera.
Uso: python3 gen_cal_plans.py   -> escribe V1.json .. V6.json en ~/Desktop/calendarios-2027-en/anuncios/work/"""
import os, json

WK = os.path.expanduser('~/Desktop/calendarios-2027-en/anuncios/work')

# letra -> (id de TikTok, inicio util, fin util, extras). Las ventanas se cortan en el segundo 18 salvo
# que la hoja de contactos llegue mas lejos: mas alla no esta revisado y no se usa.
VENT = {
    'A': ('7406973554031349024', 0, 18, {}),    # ramito de papel en una maceta (el plano mas parecido al producto)
    'B': ('7353181601632718112', 9, 18, {}),    # peonias rosas sobre marmol (pasado el titulo y el '14x14 cm')
    'C': ('7154390858614230277', 0, 18, {}),    # flor de papel crepe fucsia sobre madera oscura
    'D': ('7198505262062374146', 2, 18, {}),    # petalos celestes y tijera (pasado el '15 cm')
    'E': ('7476871315576671510', 5, 18, {}),    # flores rosas de papel sobre marmol (arranca pasado el titulo)
    'F': ('7561014489638784274', 4, 18, {}),    # peonia de papel contra una pared de laminas floreadas
    'G': ('7472045629850717462', 7, 18, {}),    # ramo de lirios rosas (arranca pasado el cartel)
    'H': ('7478344202502343958', 6, 18, {}),    # ramo con notas adhesivas (pasado el cartel del tutorial)
    'I': ('7498413681454124310', 0, 18, {}),    # papel crepe naranja plegandose
    'J': ('7270833831572262146', 2, 10, {}),    # flor lila plegada (sin la cara del principio ni el espejo del final)
    'K': ('7595134402204634423', 2, 7, {}),     # arbol pop-up de corazones que se para solo (sin la cara)
    'L': ('7627188333420104982', 6, 18, {}),    # ramo de papel contra una pared verde (pasado el 'lily edition')
    'M': ('7580325766869667093', 2, 18, {}),    # rosas rojas de papel sobre madera clara
    'N': ('7630809210464374049', 0, 18, {}),    # tarjeta blanca con flores de cerezo
    'O': ('7420032349016018209', 2, 18, {}),    # medir y cortar cartulina (arranca pasado el '20 cm x 20 cm')
    'P': ('7098341355826449670', 5, 16, {}),    # tarjeta pop-up naranja (pasado el cartel 'pop-up card')
    'R': ('7550750236625538306', 4, 18, {}),    # flores blancas de papel para el arbol de Navidad
    'T': ('7627971471704427790', 0, 14, dict(zoom=1.28, ybias=1.0)),   # armado del puesto (mismo recorte)
    'U': ('7633701522836131103', 6, 17, {}),    # carpa de feria artesanal (arranca pasado el cartel de abajo)
    'V': ('7605285503511842056', 5, 13, {}),    # la impresora escupiendo las hojas impresas
    'W': ('7644739823948942600', 0, 4, {}),     # hoja saliendo de la impresora (corta antes de los personajes con copyright)
    'X': ('7585999522237664534', 4, 12, {}),    # cucurucho de papel con el ramito adentro
    'Y': ('7633038973954477334', 0, 18, dict(zoom=1.25, ybias=1.0)),   # tijera sobre cartulina crema (cartel arriba)
}
SEG = 4.5
TOPE = 6          # maximo de recortes por clip


def pool_y_clips():
    pool, clips = [], {}
    for k, (vid, a, b, ex) in VENT.items():
        clips[k] = dict(src=f'tiktoks2/{vid}.mp4', fam=vid, **ex)
        tramos, t = [], a
        while t < b - 1.8:
            tramos.append([k, round(t, 2), round(min(t + SEG, b), 2)])
            t += SEG
        if len(tramos) > TOPE:
            paso = len(tramos) / TOPE
            tramos = [tramos[int(i * paso)] for i in range(TOPE)]
        pool += tramos
    return pool, clips


FIN = dict(type='end', head=['2027 CALENDAR', 'PACK'],
           sub='50 PRINTABLE DESIGNS · PRICING APP',
           sub2='INSTANT DOWNLOAD · REPRINT FOREVER',
           cta='Tap Learn more 👇')

VIDEOS = [
    dict(n=1, hook='SOLD OUT ON DAY ONE AT THE CRAFT FAIR', hook_until='business', first=['U', 6],
         overlays=[dict(type='chip', text='PRINT AT HOME · CUT WITH SCISSORS', icon='✓', word='scissors', dur=2.4),
                   dict(type='chip', text='ONE FILE · REPRINT IT FOREVER', icon='✓', word='profit', dur=2.4),
                   dict(FIN=1, word='below')]),
    dict(n=2, hook='THE SCHOOL MUMS TOOK EVERY ONE', hook_until='business', first=['A', 0],
         overlays=[dict(type='chip', text='PRINT AT HOME · CUT WITH SCISSORS', icon='✓', word='scissors', dur=2.4),
                   dict(type='chip', text='50 DESIGNS FOR 2027', icon='✓', word='profit', dur=2.4),
                   dict(FIN=1, word='below')]),
    dict(n=3, hook='50 DESIGNS + THE APP THAT PRICES THEM', hook_until='printables', first=['K', 2],
         overlays=[dict(type='chip', text='PRINT · CUT · STACK · SELL', icon='✓', word='table', dur=2.4),
                   dict(type='chip', text='THE APP SAVES EVERY ORDER', icon='✓', word='orders', dur=2.4),
                   dict(FIN=1, word='Tap')]),
    dict(n=4, hook='61, HOPELESS WITH COMPUTERS, STILL SELLING', hook_until='calendars', first=['F', 4],
         overlays=[dict(type='chip', text='NO CUTTING MACHINE · NO DESIGN SKILLS', icon='✓', word='Cricut', dur=2.4),
                   dict(type='chip', text='REPRINT FOR THE PRICE OF A SHEET', icon='✓', word='profit', dur=2.4),
                   dict(FIN=1, word='Tap')]),
    dict(n=5, hook='WHAT I SOLD THIS WEEKEND', hook_until='scissors', first=['T', 0],
         overlays=[dict(type='chip', text='TOOK 15 · CAME HOME WITH NONE', icon='✓', word='none', dur=2.4),
                   dict(type='chip', text='50 DESIGNS · NO MACHINE NEEDED', icon='✓', word='machine', dur=2.4),
                   dict(FIN=1, word='Tap')]),
    dict(n=6, hook='THESE CALENDARS PAID FOR CHRISTMAS DINNER', hook_until='stretch', first=['R', 4],
         overlays=[dict(type='chip', text='NAME STICKERS INCLUDED', icon='✓', word='stickers', dur=2.4),
                   dict(type='chip', text='DIGITAL · NO STOCK, NO SHIPPING', icon='✓', word='profit', dur=2.4),
                   dict(FIN=1, word='below')]),
]

for v in VIDEOS:
    pool, clips = pool_y_clips()
    ovs = [dict(FIN, word=o['word'], occ=o.get('occ', 0)) if o.get('FIN') else o for o in v['overlays']]
    first = v['first']
    if not any(x[0] == first[0] and x[1] == first[1] for x in pool):
        raise SystemExit(f"V{v['n']}: el primer plano {first} no esta en el pool.")
    plan = dict(
        vo=f"vo/V{v['n']}.wav", script=f"V{v['n']}.txt", lang='en',
        speed=1.30, silence=[0.26, 0.12], cut=[1.9, 2.4, 2.9], words=2,
        music='music/bed.wav', music_db=-8,
        hi='&H003CA9EF&', capy=1380,
        hook=v['hook'], hook_until=v['hook_until'],
        first=first, seed=v['n'] * 97,
        clips=clips, pool=pool, anchors=v.get('anchors', []), overlays=ovs)
    json.dump(plan, open(f"{WK}/V{v['n']}.json", 'w'), ensure_ascii=False, indent=1)
    print(f"V{v['n']}.json  ({len(pool)} recortes de {len(clips)} clips)")
