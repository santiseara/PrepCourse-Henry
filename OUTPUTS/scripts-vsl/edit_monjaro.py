"""Edición del VSL de Monjaro Violeta: B-rolls, subtítulos, headlines, música y whooshes.

Entra `base123.mp4` (el VSL ya a 1.23x) y sale el VSL editado.

Criterio: poner poco y que lo poco sume.
  - B-roll solo donde la voz habla de preparar la bebida. Un B-roll de cocina
    mientras ella cuenta lo que sintió es relleno y se nota.
  - Headlines solo en los cuatro números que son la oferta. Si se subraya todo,
    no se subraya nada.
  - Música a -27 dB y con ducking: tiene que notarse que no hay silencio, no
    tiene que competir con la voz.
  - Whoosh solo al entrar al B-roll, no al salir: dos por corte cansa.

Las anclas se buscan POR TEXTO en la transcripción real, no por segundo fijo:
así siguen funcionando si se regenera la voz (regla de vsl-reglas-de-armado).

Uso: python3 edit_monjaro.py
"""
import json
import os
import subprocess
import unicodedata

FF = os.path.expanduser('~/bin/ffmpeg')
S = os.environ.get(
    'VSL_TMP',
    '/private/tmp/claude-501/-Users-santiagoseara-PrepCourse-Henry/'
    '89185bbb-7bd8-45cd-a4d9-37f0f3c92e34/scratchpad')
VSL = os.path.expanduser('~/Desktop/monjaro-violeta/vsl')
BR = os.path.join(VSL, 'brolls-raw')
# B1 quedo afuera: sus planos finales son los unicos con el producto terminado,
# pero en todos se cuela el torso del tipo de la musculosa, que rompe el relato
# de dos mujeres. Queda disponible por si aparece un corte limpio.
B1 = os.path.join(BR, 'WhatsApp Video 2026-11-04 at 15.05.59.mp4')
B3 = os.path.join(BR, 'WhatsApp Video 2026-11-04 at 15.07.01.mp4')
OUT = os.path.join(VSL, 'VSL-monjaro-violeta-EDITADO.mp4')

WORDS = json.load(open(f'{S}/words.json', encoding='utf-8'))


def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    return ''.join(c for c in s if c.isalnum() and unicodedata.category(c) != 'Mn')


NW = [norm(w['w']) for w in WORDS]


def ancla(frase, desde=0.0):
    """Devuelve (t0, t1) de la primera aparición de `frase` después de `desde`."""
    objetivo = [norm(x) for x in frase.split()]
    n = len(objetivo)
    for i in range(len(NW) - n + 1):
        if WORDS[i]['t0'] < desde:
            continue
        if NW[i:i + n] == objetivo:
            return WORDS[i]['t0'], WORDS[i + n - 1]['t1']
    raise SystemExit(f'ancla no encontrada: "{frase}"')


def dur(path):
    o = subprocess.run([FF, '-hide_banner', '-i', path],
                       capture_output=True, text=True).stderr
    d = o.split('Duration: ')[1].split(',')[0]
    h, m, s = d.split(':')
    return int(h) * 3600 + int(m) * 60 + float(s)


TOTAL = dur(f'{S}/base123.mp4')

# ---------- dónde va cada cosa ----------
# (frase ancla, archivo, segundo del broll, cuánto dura el corte)
# OJO: las frases son las de la TRANSCRIPCION, no las del guion. El TTS dice los
# numeros en letras pero el transcriptor los escribe en digitos ("3 minutos"), y
# ademas se come palabras ("ya tenian casa" por "ya tenia en casa").
PLAN_BROLL = [
    ('use ingredientes que ya',       B3, 1.5, 3.2),    # 30s · cortar remolacha
    ('lo haces en 3 minutos',         B3, 13.5, 3.0),   # 48s · el agua a la licuadora
    ('la receta del monjaro violeta', B3, 0.0, 2.8),    # 64s · el vaso de jugo violeta
    ('la lista de los alimentos',     B3, 8.5, 3.0),    # 118s · manzana y jengibre
    ('nace en tu cocina',             B3, 19.3, 3.4),   # 147s · el colado violeta
]
# El hueco de 66s a 118s es a proposito: ahi se dice el precio, y el precio va a
# cara. Tampoco hay B-roll sobre el CTA final por lo mismo.

# (frase ancla, texto del headline, cuánto queda en pantalla)
PLAN_HEAD = [
    ('baje 8 kilos',                 '8 KILOS EN 15 DÍAS', 2.6),
    ('lo haces en 3 minutos',        '3 MINUTOS AL DÍA', 2.4),
    ('que pague un solo pago',       'UN SOLO PAGO', 2.4),
    ('si en 30 dias no ves',         'GARANTÍA DE 30 DÍAS', 2.8),
]

# palabras que van en dorado dentro del subtítulo
CLAVE = {'kilos', 'ocho', 'quince', 'dieciseis', 'gratis', 'garantia', 'cocina',
         'espejo', 'panza', 'tres', 'minutos', 'regalo', 'hoy', 'nunca', 'pago',
         'cuotas', 'devuelvo', 'peso', 'pesos', 'riesgo', 'villanos', 'metabolismo'}


def t_ass(x):
    h = int(x // 3600)
    m = int(x % 3600 // 60)
    s = x % 60
    return '%d:%02d:%05.2f' % (h, m, s)


def construir_ass(cortes):
    """Subtítulos de a dos palabras + headlines. Durante un B-roll el subtítulo
    sube, para no tapar lo que se está mostrando."""
    cab = (
        '[Script Info]\nScriptType: v4.00+\nPlayResX: 1080\nPlayResY: 1920\nWrapStyle: 2\n\n'
        '[V4+ Styles]\nFormat: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,'
        'OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,'
        'Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding\n'
        # N: subtítulo normal · A: palabra clave en dorado · B: subtítulo arriba (sobre B-roll)
        'Style: N,Arial Black,84,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,1,0,0,0,100,100,0,0,1,7,3,2,40,40,360,1\n'
        'Style: A,Arial Black,84,&H0000D7FF,&H0000D7FF,&H00000000,&H00000000,1,0,0,0,100,100,0,0,1,7,3,2,40,40,360,1\n'
        'Style: B,Arial Black,84,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,1,0,0,0,100,100,0,0,1,7,3,2,40,40,360,1\n'
        # H: headline, magenta de la marca, arriba
        'Style: H,Arial Black,104,&H00C826E6,&H00C826E6,&H00FFFFFF,&H00000000,1,0,0,0,100,100,2,0,1,9,4,8,60,60,300,1\n\n'
        '[Events]\nFormat: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text\n')

    ev = []
    i = 0
    while i < len(WORDS):
        grupo = WORDS[i:i + 2]
        txt = ' '.join(g['w'] for g in grupo).upper().strip()
        if not txt:
            i += 2
            continue
        t0, t1 = grupo[0]['t0'], grupo[-1]['t1']
        if t1 - t0 > 2.2:
            t1 = t0 + 2.2
        est = 'A' if any(norm(g['w']) in CLAVE for g in grupo) else 'N'
        ev.append('Dialogue: 0,%s,%s,%s,,0,0,0,,%s'
                  % (t_ass(t0), t_ass(max(t1, t0 + 0.25)), est, txt))
        i += 2

    for t0, texto, d in cortes['headlines']:
        ev.append('Dialogue: 1,%s,%s,H,,0,0,0,,%s'
                  % (t_ass(t0), t_ass(t0 + d), texto))

    open(f'{S}/subs.ass', 'w', encoding='utf-8').write(cab + '\n'.join(ev) + '\n')
    return len(ev)


def main():
    # 1. resolver anclas
    brolls = []
    for frase, arch, t_in, largo in PLAN_BROLL:
        t0, _ = ancla(frase)
        brolls.append({'t': round(t0, 2), 'f': arch, 'in': t_in, 'd': largo})
    brolls.sort(key=lambda x: x['t'])

    headlines = []
    for frase, texto, d in PLAN_HEAD:
        t0, _ = ancla(frase)
        headlines.append((round(t0, 2), texto, d))

    print(f'VSL base: {TOTAL:.2f}s')
    print('B-rolls:')
    for b in brolls:
        print(f"  {b['t']:7.2f}s  +{b['d']}s  {os.path.basename(b['f'])[:34]} desde {b['in']}s")
    print('Headlines:')
    for t0, txt, d in headlines:
        print(f'  {t0:7.2f}s  +{d}s  {txt}')

    construir_ass({'headlines': headlines})

    # 2. filter_complex
    # entradas: 0 base · 1..n brolls · musica · whoosh
    entradas = ['-i', f'{S}/base123.mp4']
    fc = []
    vlab = '0:v'
    for k, b in enumerate(brolls):
        entradas += ['-ss', str(b['in']), '-t', str(b['d']), '-i', b['f']]
        idx = k + 1
        # escalar el broll (464x832) a 1080x1920 recortando lo que sobre, con zoom lento
        fc.append(
            f"[{idx}:v]scale=1188:2112:force_original_aspect_ratio=increase,"
            f"crop=1080:1920,setpts=PTS-STARTPTS+{b['t']}/TB,fps=25,format=yuva420p[b{k}]")
        nuevo = f'v{k}'
        fc.append(f"[{vlab}][b{k}]overlay=0:0:enable='between(t,{b['t']},{b['t'] + b['d']})'[{nuevo}]")
        vlab = nuevo

    subs = f'{S}/subs.ass'.replace(':', r'\:')
    fc.append(f"[{vlab}]ass='{subs}'[vout]")

    # audio: voz + musica bajita con ducking + un whoosh por entrada de broll
    n_br = len(brolls)
    i_mus = n_br + 1
    i_wh = n_br + 2
    entradas += ['-stream_loop', '-1', '-i', f'{S}/musica.wav']
    entradas += ['-i', f'{S}/sfx/whoosh_in.wav']

    fc.append(f'[{i_mus}:a]atrim=0:{TOTAL},volume=0.075,'
              f'afade=t=in:d=1.2,afade=t=out:st={TOTAL - 2.5}:d=2.5,aresample=48000[mus]')
    partes = []
    for k, b in enumerate(brolls):
        ms = int(max(0, b['t'] - 0.18) * 1000)
        fc.append(f'[{i_wh}:a]adelay={ms}|{ms},volume=0.5,aresample=48000[w{k}]')
        partes.append(f'[w{k}]')
    if partes:
        fc.append(''.join(partes) + f'amix=inputs={len(partes)}:normalize=0,apad[wh]')
    else:
        fc.append(f'anullsrc=r=48000:cl=stereo,atrim=0:{TOTAL}[wh]')

    # sidechain: la musica baja sola cuando hay voz
    fc.append('[0:a]aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,'
              'asplit=2[voz][llave]')
    fc.append('[mus][llave]sidechaincompress=threshold=0.05:ratio=7:attack=12:release=420[musd]')
    fc.append(f'[voz][musd][wh]amix=inputs=3:duration=first:normalize=0,'
              f'alimiter=limit=0.95,aresample=48000[aout]')

    cmd = [FF, '-v', 'error', '-y'] + entradas + [
        '-filter_complex', ';'.join(fc),
        '-map', '[vout]', '-map', '[aout]',
        '-c:v', 'libx264', '-preset', 'medium', '-crf', '19', '-pix_fmt', 'yuv420p',
        '-r', '25', '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', OUT]
    print('\nrenderizando…')
    subprocess.run(cmd, check=True)
    d = dur(OUT)
    m, s = divmod(round(d), 60)
    print(f'\n{os.path.basename(OUT)} · {m}:{s:02d} · {os.path.getsize(OUT)/1e6:.1f} MB')
    print(f'→ {OUT}')


if __name__ == '__main__':
    main()
