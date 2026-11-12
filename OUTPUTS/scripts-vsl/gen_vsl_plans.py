# -*- coding: utf-8 -*-
"""Planes de b-roll de los 4 VSL de pospago de Party Box Profits (mercado ingles, 2026-11-11).

Por que se genera desde la transcripcion y no a mano: los anclajes del editor son FRASES, y una
frase escrita a ojo contra el guion no cae donde cae en el render (la voz contrae, Whisper parte
distinto). Aca se transcribe el MP4 de HeyGen, se parte por oracion y cada tramo explicativo se
llena con el clip que habla de ESE tema (el papel con las piezas troqueladas, el precio con la
caja de billetes, la foto con la caja al sol).

Reglas que respeta (Manual de Edicion IA, seccion 9, VSL):
  - b-roll cada 3-5 s en los tramos explicativos, no encima de los momentos a camara
  - alterna split / full / gs / pip, nunca dos iguales seguidos ni el mismo clip pegado
  - los momentos de precio, garantia y boton quedan SIN b-roll: ahi la cara vende
  - cero SFX (el 3.er campo de los headlines va siempre vacio)

Uso: python3 gen_vsl_plans.py <V1|V2|V3|V4> <heygen.mp4> <carpeta_trabajo>
     -> escribe <carpeta>/plan_<V>.json, <carpeta>/heads_<V>.json y corta los b-rolls en brolls/
"""
import os, sys, json, re, subprocess

FF = os.path.expanduser('~/bin/ffmpeg')
HERE = os.path.dirname(os.path.abspath(__file__))
CLIPS = os.path.expanduser('~/Desktop/party-box-vault/anuncios/work/clips')

VENT = {}
exec(open(os.path.join(HERE, 'vent_boxes.py')).read())

# tema -> clips que lo muestran de verdad (clave del pool revisado de vent_boxes.py)
TEMAS = [
    (r'paper|cardstock|pound|cover|sheet|print|printer|ink',      ['u', 'E', 'm']),
    (r'fold|close|tab|crease|glue|scissor|cut',                   ['k', 'm', 'D', 'h']),
    (r'price|charge|dollar|money|deposit|pay|cost|cent|quote',    ['r', 'j']),
    (r'twelve|pink|name|daughter|personal',                       ['c', 'a', 's']),
    (r'template|librar|collection|theme|catalog',                 ['i', 'q', 'w', 's']),
    (r'photo|picture|stor(y|ies)|frame|camera|phone|scroll',      ['l', 't', 'o']),
    (r'birthday|baptism|shower|fundraiser|party|favor|table',     ['t', 'n', 'v', 'x', 'h']),
    (r'christmas|season|holiday|mother|graduat|communion|calend', ['f', 'e', 'o']),
    (r'fill|ribbon|bow|box(es)? (sitting|on)',                    ['b', 'g', 'A', 'C']),
]
RONDA = ['g', 'b', 'q', 'v', 'n', 'A', 'w', 'x', 'C', 'i', 'o', 'l', 'h', 'd', 'p', 'f', 't', 's']
MODOS = ['split', 'pip', 'full', 'gs']

# frases donde la cara TIENE que estar sola: precio, garantia, cierre y boton
SIN_BROLL = re.compile(
    r'ninety seven|thirty seven|twenty seven|seventeen dollars|one single payment|one payment|'
    r'guarantee|every cent back|tap the button|button below|line under|congratulations|'
    r'my name is megan|go print your first box|nothing renews|nothing changes', re.I)


def duracion(p):
    s = subprocess.run([FF, '-i', p], capture_output=True, text=True).stderr
    s = s.split('Duration: ')[1].split(',')[0]
    h, m, x = s.split(':')
    return int(h) * 3600 + int(m) * 60 + float(x)


def transcribir(mp4, cache, guion):
    # el editor guarda su propia transcripcion en <wd>/edit_<nombre>/words0.json. Es la que
    # usa find() para ubicar cada frase, asi que si existe se usa ESA: transcribir por
    # separado da palabras distintas ("take" vs "pick") y los anclajes no se encuentran.
    del_editor = os.path.join(os.path.dirname(cache),
                              'edit_' + os.path.splitext(os.path.basename(mp4))[0], 'words0.json')
    if os.path.exists(del_editor):
        return json.load(open(del_editor))
    if os.path.exists(cache):
        return json.load(open(cache))
    from faster_whisper import WhisperModel
    wav = cache + '.wav'
    subprocess.run([FF, '-v', 'error', '-y', '-i', mp4, '-ac', '1', '-ar', '16000', wav], check=True)
    m = WhisperModel('small', device='cpu', compute_type='int8')
    segs, _ = m.transcribe(wav, language='en', word_timestamps=True, beam_size=5, initial_prompt=guion)
    W = [{'w': w.word.strip(), 's': w.start, 'e': w.end} for s in segs for w in s.words]
    json.dump(W, open(cache, 'w'), ensure_ascii=False)
    return W


def oraciones(W):
    """Parte la transcripcion en oraciones: (inicio, fin, texto, [palabras])."""
    out, cur = [], []
    for w in W:
        cur.append(w)
        if w['w'][-1:] in '.?!':
            out.append((cur[0]['s'], cur[-1]['e'], ' '.join(x['w'] for x in cur), cur))
            cur = []
    if cur:
        out.append((cur[0]['s'], cur[-1]['e'], ' '.join(x['w'] for x in cur), cur))
    return out


def clip_del_tema(texto, usados):
    """Devuelve el clip del tema de la oracion, o None si no hay nada concreto que mostrar."""
    for rx, keys in TEMAS:
        if re.search(rx, texto, re.I):
            for k in keys:
                if k not in usados[-3:]:
                    return k
            return keys[0]
    return None          # oracion abstracta: va la cara sola, no se inventa un b-roll


def relleno(usados):
    for k in RONDA:
        if k not in usados[-6:]:
            return k
    return RONDA[len(usados) % len(RONDA)]


def ancla(palabras, desde=0, n=3):
    """Frase corta y textual para que find() del editor la encuentre sin ambiguedad."""
    sel = palabras[desde:desde + n]
    return ' '.join(x['w'] for x in sel).strip()


def main():
    vsl, mp4, wd = sys.argv[1], sys.argv[2], sys.argv[3]
    guion = open(os.path.join(wd, 'txt', vsl + '_full.txt'), encoding='utf-8').read()
    br = os.path.join(wd, 'brolls'); os.makedirs(br, exist_ok=True)
    W = transcribir(mp4, os.path.join(wd, f'words_{vsl}.json'), guion)
    ORS = oraciones(W)

    plan, heads, usados = [], [], []
    modo_actual, quedan_en_modo, i_modo = MODOS[0], 0, 0
    ARRANQUE = 12.0        # los primeros 12 s son la cara: ahi se gana la confianza
    sin_broll_seguidas = 0
    for (a, b, txt, pal) in ORS:
        if SIN_BROLL.search(txt) or b < ARRANQUE:   # cara limpia: precio, garantia, boton, apertura
            sin_broll_seguidas += 1
            continue
        dur = b - a
        if dur < 1.8:                      # oracion muy corta: no se corta nada encima
            continue
        k0 = clip_del_tema(txt, usados)
        if k0 is None:
            # nada concreto que mostrar. Se deja la cara, salvo que ya lleve 3 oraciones
            # seguidas sin b-roll: ahi entra uno de relleno para que no se vuelva una charla
            if sin_broll_seguidas < 3:
                sin_broll_seguidas += 1
                continue
            k0 = relleno(usados)
        sin_broll_seguidas = 0
        # cada 3-5 s un clip nuevo dentro de la misma oracion
        n = max(1, min(4, int(dur // 4.0) + (1 if dur % 4.0 > 2.0 else 0)))
        paso = len(pal) / n
        for j in range(n):
            p_ini = int(j * paso)
            p_fin = min(len(pal) - 1, int((j + 1) * paso) - 1)
            if p_fin - p_ini < 1:
                continue
            k = k0 if j == 0 else clip_del_tema(txt, usados) or relleno(usados)
            usados.append(k)
            fn, w0, w1, _ = VENT[k]
            largo = min(6.5, w1 - w0)
            off = w0 + (len(usados) * 1.7) % max(0.1, (w1 - w0 - largo))
            nombre = f'{vsl}_{len(plan):02d}'
            dst = os.path.join(br, nombre + '.mp4')
            if not os.path.exists(dst):
                subprocess.run([FF, '-v', 'error', '-y', '-ss', f'{off:.2f}', '-i',
                                os.path.join(CLIPS, fn + '.mp4'), '-t', f'{largo:.2f}',
                                '-an', '-vf', 'scale=1080:-2', '-r', '30',
                                '-c:v', 'libx264', '-crf', '20', '-pix_fmt', 'yuv420p', dst],
                               check=True)
            # el formato se sostiene 2-3 tramos seguidos: cambiarlo en cada corte se nota armado
            if quedan_en_modo <= 0:
                modo_actual = MODOS[i_modo % len(MODOS)]; i_modo += 1
                quedan_en_modo = 2 if modo_actual == 'full' else 3
            quedan_en_modo -= 1
            plan.append([nombre, ancla(pal, p_ini, 3), ancla(pal, max(p_ini, p_fin - 2), 3), 0.0, modo_actual])

    json.dump(plan, open(os.path.join(wd, f'plan_{vsl}.json'), 'w'), indent=1)
    # las placas NO se tocan aca: las escribe gen_vsl_heads.py. Escribir una lista vacia
    # pisaba las placas de precio y garantia y el render salia sin ellas (11/11/2026).
    print(f'{vsl}: {len(plan)} tramos de b-roll, {len(ORS)} oraciones, '
          f'{sum(1 for o in ORS if SIN_BROLL.search(o[2]))} oraciones a cara limpia')


if __name__ == '__main__':
    main()
