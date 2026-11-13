# -*- coding: utf-8 -*-
"""Planes de los 6 ads del Kit de Radiestesia (LATAM, 2026-11-13).

Competidor: Regarte (page 1342388312284290, 116 ads activos). De sus 12 videos mas vistos,
7 son ella a camara y 5 son voz en off; se clona el unico formato sin persona: las laminas y los
biometros en pantalla sobre fondo violeta, paso por paso, con subtitulo blanco de una palabra.
Las laminas se dibujan con gfx_pendulo.py porque el nicho no tiene b-roll limpio en TikTok
(104 clips bajados, 2 sirvieron, y esos dos entran como respiro).

Uso: python3 gen_pendulo_plans.py   -> escribe V1.json .. V6.json en work/
"""
import os, json

WK = os.path.expanduser('~/Desktop/kit-radiestesia/anuncios/work')
HI = '&H00FFFFFF&'       # palabra activa: blanca, como el ganador (sin color)
HIBOX = '&H00000000&'    # borde negro, sin caja

# los dos unicos clips de TikTok que pasaron el filtro
CLIP_PEND = '7550667569720610064'   # pendulos de cristal colgando sobre tela blanca
CLIP_MANO = '7551588054801108238'   # manos con un pendulo de cristal negro

CIERRE = dict(type='end', word='abajo', occ=0,
              head=['KIT DE', 'RADIESTESIA'],
              sub='37 biómetros · 52 gráficos · 7 circuitos',
              cta='Toca en Descargar',
              sub2='Listo para imprimir en A4 · Acceso inmediato por correo · 14 días de garantía',
              img='gfx/portada.png')


def armar(laminas, clips_tiktok=()):
    """clips = laminas estaticas + los clips de tiktok; pool = dos entradas por lamina."""
    clips, pool = {}, []
    for i, nom in enumerate(laminas):
        k = chr(ord('a') + i)
        clips[k] = dict(src=f'gfx/{nom}.png', still=True)
        pool += [[k, round(0.4 * j, 2), round(0.4 * j + 3.4, 2)] for j in range(5)]
    for j, vid in enumerate(clips_tiktok):
        k = f't{j}'
        clips[k] = dict(src=f'clips/{vid}.mp4')
        pool += [[k, 0.5, 3.3], [k, 4.0, 6.8], [k, 7.5, 10.3]]
    return clips, pool


VIDEOS = [
    # 1) el pendulo en el cajon
    dict(n=1, seed=161, seq=list('afbcde'),
         laminas=['portada', 'bio_chakras', 'graf_kit', 'cuerpo_7', 'bio_pct_alto', 'graf_desorden'],
         tiktok=[CLIP_PEND, CLIP_MANO],
         anchors=[('cajón', 0, 'f', 0), ('preguntarle', 0, 'b', 0), ('biómetros', 0, 'c', 0),
                  ('lámina', 0, 'b', 0), ('porcentaje', 0, 'e', 0), ('imprimes', 0, 'c', 0)]),
    # 2) la pregunta mal hecha
    dict(n=2, seed=262,
         laminas=['preg_mal', 'preg_bien', 'preg_dos', 'bio_chakras', 'graf_kit', 'portada'],
         tiktok=[CLIP_MANO],
         anchors=[('confusa', 0, 'a', 0), ('enormes', 0, 'a', 0), ('entrevista', 0, 'b', 0),
                  ('quedo', 0, 'c', 0), ('impresa', 0, 'd', 0), ('treinta', 0, 'e', 0)]),
    # 3) los tres pasos
    dict(n=3, seed=363, seq=list('abcdefgh'),
         laminas=['paso1', 'bio_chakras_corazon', 'bio_pct_bajo', 'paso2', 'bio_bloqueo_aisl',
                  'paso3', 'bio_pct_sube', 'cuerpo_7'],
         tiktok=[CLIP_PEND],
         anchors=[('uno', 0, 'a', 0), ('chakras', 1, 'b', 0), ('porcentaje', 0, 'c', 0),
                  ('dos', 0, 'd', 0), ('bloqueando', 0, 'e', 0), ('tres', 0, 'f', 0),
                  ('subió', 0, 'g', 0)]),
    # 4) los diez chakras del animal
    dict(n=4, seed=464,
         laminas=['animal_7', 'animal_10', 'cuerpo_7', 'graf_kit', 'portada'],
         tiktok=[CLIP_MANO],
         anchors=[('siete', 0, 'a', 0), ('diez', 0, 'b', 0), ('braquial', 0, 'b', 0),
                  ('patas', 0, 'b', 0), ('lámina', 0, 'b', 0), ('Kit', 0, 'd', 0)]),
    # 5) los graficos sueltos
    dict(n=5, seed=565,
         laminas=['graf_desorden', 'graf_kit', 'bio_chakras', 'portada'],
         tiktok=[CLIP_PEND, CLIP_MANO],
         anchors=[('celular', 0, 'a', 0), ('desorden', 0, 'a', 0), ('junté', 0, 'b', 0),
                  ('impresa', 0, 'c', 0), ('carpeta', 0, 'b', 0)]),
    # 6) la casa, ambiente por ambiente
    dict(n=6, seed=666, seq=list('abcde'),
         laminas=['hogar', 'hogar_pct', 'bio_pct_sube', 'graf_kit', 'portada'],
         tiktok=[CLIP_PEND],
         anchors=[('ambiente', 0, 'a', 0), ('porcentaje', 0, 'b', 0), ('subir', 0, 'c', 0),
                  ('impresa', 0, 'd', 0)]),
]

for v in VIDEOS:
    clips, pool = armar(v['laminas'], v['tiktok'])
    plan = dict(
        vo='vo/V%d.wav' % v['n'], script='V%d.txt' % v['n'], lang='es',
        speed=1.30, silence=[0.26, 0.12], cut=[2.2, 2.8, 3.4], words=1,
        music='music/bed.wav', music_db=-11,
        hi=HI, hibox=HIBOX, hibord=8, capy=1680,
        seed=v['seed'], usage='usage.json', nosfx=True,
        clips=clips, pool=pool,
        anchors=[a for a in v['anchors'] if a[2]],
        overlays=[dict(CIERRE)],
        first=[chr(ord('a')), 0],
    )
    if v.get('seq'):
        plan['seq'] = v['seq']
    json.dump(plan, open(os.path.join(WK, 'V%d.json' % v['n']), 'w'), indent=1)
    print('V%d  %d laminas + %d clips  %d tramos' % (v['n'], len(v['laminas']), len(v['tiktok']), len(pool)))
