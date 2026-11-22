#!/usr/bin/env python3
"""Montaje del VSL de Desparasitacion Articular (AR, 2026-11-22).

Clon del VSL ganador de Protocolo Chia 4S: avatar a pantalla completa, cortes secos a
b-roll a pantalla completa, subtitulos de 2-3 palabras en mayuscula con una palabra en
amarillo, placas sobre el avatar y cama de suspenso con ducking.

  python3 edit_parasitos_vsl.py <carpeta_trabajo> <salida.mp4>

La carpeta de trabajo tiene:
  heygen/B1.mp4 .. B6.mp4   los bloques bajados de HeyGen, en orden
  visuales/*.mp4            el pool de b-rolls, nombrados NN-descripcion
  gfx/*.png                 las placas
  guion.txt                 el guion completo, el mismo que se le dio a HeyGen

⚠️ El pool viene a 480x848 (WhatsApp): los cortes van de 2 a 3 s, nunca mas, porque
escalado 2,25x se ve mas blando que el avatar (regla del 22/11).
"""
import sys, os, json, subprocess, unicodedata, difflib

FF   = os.path.expanduser('~/bin/ffmpeg')
WORK = os.path.abspath(sys.argv[1])
OUT  = os.path.abspath(sys.argv[2])
TMP  = os.path.join(WORK, '_tmp'); os.makedirs(TMP, exist_ok=True)

SPEED    = float(os.environ.get('SPEED', 1.0))
GAP_MAX  = float(os.environ.get('GAP_MAX', 0.40))
GAP_KEEP = float(os.environ.get('GAP_KEEP', 0.18))
CORTE    = float(os.environ.get('CORTE', 2.6))     # largo de cada b-roll
CAP_Y    = 1220                                     # 63,5 % del alto, igual que los ads de la oferta
MUS      = os.path.expanduser('~/Downloads/u_6niyix0m9h-musica-de-suspense-335486.mp3.mpeg')

GUION = open(os.path.join(WORK, 'guion.txt'), encoding='utf-8').read()

# ───────────────────────────────────────────── plan: (ancla, clip) y (ancla, placa, seg)
BROLL = [
 ("al levantarte de la cama",                 "03-pies-al-borde-de-la-cama"),
 ("en los hombros o en las manos",            "22-manos-artriticas"),
 ("No necesitás infiltraciones",              "11-rodilla-infiltracion-jeringa"),
 ("Y no necesitás gastar una fortuna",                    "24-hombre-mayor-punado-pastillas"),
 ("adentro de tu intestino y te está robando","29-colonoscopia-ascaris"),
 ("se alimenta del colágeno que tendría",     "09-intestino-3d-con-parasito"),
 ("libera toxinas que viajan por la sangre",  "04-cuerpo-3d-nervios-rojos"),
 ("Por eso tu articulación se traba",         "40-hueso-3d-poroso"),
 ("el hueso termina raspando",                "48-femur-sano-vs-carcomido"),
 ("el parásito se empieza a soltar",          "31-digestivo-3d-banado-dorado"),
 ("tres minutos sentado en la cama",          "27-muy-mayor-encorvada-en-cama"),
 ("bajar la escalera de costado",             "26-mujer-mayor-baja-escalera"),
 ("agacharte a atarte los cordones",          "23-pie-3d-espolon"),
 ("darte vuelta mil veces en la cama",        "07-desvelado-de-noche"),
 ("que te digan que es la edad",              "21-mujer-mayor-agotada"),
 ("tu cuerpo se quedó sin colágeno",          "39-rodilla-3d-cristales"),
 ("viven parásitos que se alimentan",         "05-rodilla-3d-gusano-cartilago"),
 ("tu rodilla queda seca",                    "06-rodilla-3d-deposito"),
 ("Tus manos se ponen rígidas",               "02-manos-mayor-mesa"),
 ("llena de bacterias buenas",                "30-bacterias-en-tejido"),
 ("los años de antiinflamatorios",            "32-estomago-3d-pastillas"),
 ("Te irritan la mucosa del intestino",       "33-digestivo-3d-inflamado"),
 ("se instala y empieza a comer",             "28-intestino-3d-completo"),
 ("Pasa a la sangre",                         "35-espalda-3d-nervios"),
 ("tu columna, tu rodilla y tu cadera",       "37-ciatico-3d-gluteo"),
 ("Esos nervios se inflaman",                 "47-lumbar-3d-encendida"),
 ("hinchado, sin energía",                    "13-mano-blister-y-vaso"),
 ("tomás el remedio, mejorás dos días",       "45-columna-3d-capsula"),
 ("lo único que queda es la cirugía",         "25-camina-con-bastones"),
 ("Agarrá un carozo de palta",                "19-manos-carozo-de-palta"),
 ("Rallalo adentro de un vaso",               "20-rallando-carozo-en-vaso"),
 ("El agua se volvió dorada",                 "10-vaso-liquido-dorado"),
 ("los taninos del carozo saliendo",          "18-dorado-cayendo-paltas"),
 ("recubre la pared del intestino",           "08-intestino-3d-liquido-dorado"),
 ("metiéndote una aguja",                     "41-rodilla-3d-roja"),
 ("comer carozo de palta solo no sirve",      "17-botella-y-carozo-de-palta"),
 ("lo despega de la pared del intestino",     "09-intestino-3d-con-parasito"),
 ("la primera noche ya duerme de corrido",    "16-taza-te-con-semillas"),
 ("Baja la inflamación de los nervios",             "31-digestivo-3d-banado-dorado"),
 ("del glúteo hasta el pie",                  "36-pierna-3d-rodilla-azul"),
 ("La rodilla se lubrica",                    "38-rodilla-3d-destello"),
 ("El cartílago empieza a recuperar",         "43-rodilla-3d-azul"),
 ("subís una escalera entera",                "14-mujer-mayor-sube-escalera"),
 ("lo conseguís en la verdulería",            "19-manos-carozo-de-palta"),
 ("se hace en menos de dos minutos",          "20-rallando-carozo-en-vaso"),
 ("apoyás los dos pies en el piso",           "34-cuerpo-3d-en-cuclillas"),
 ("Bajás la escalera de frente",              "26-mujer-mayor-baja-escalera"),
 ("ves el blíster de ibuprofeno ahí",         "12-mesita-de-luz-blister"),
 ("Tu nieto te pide que lo alces",            "15-hombre-y-senora-mayor-felices"),
]
PLACAS = [
 ("Tu Protocolo de Desparasitación Articular", "titulo",  3.2),
 ("Días uno, dos y tres",                      "etapa1",  4.5),
 ("Días cuatro, cinco y seis",                 "etapa2",  4.5),
 ("Días siete, ocho y nueve",                  "etapa3",  4.5),
 ("Hugo Benítez, de Córdoba",                  "resena1", 9.0),
 ("Teresa Ferreyra, de Mendoza",               "resena2", 11.0),
 ("Y Antonio Rivas, de Tucumán",               "resena3", 10.0),
 ("La preparación para la",    "stack",   30.0),
 ("Sí, escuchaste bien",                       "precio",  7.0),
 ("El botón está justo acá abajo",             "boton",   6.0),
 ("Tocá el botón de abajo ahora mismo",       "cierre",  5.5),
]
# tramos donde NO entra b-roll: el precio y el cierre venden con la cara
PROHIBIDO = [("La preparación para la", "Tocalo y en dos minutos"),
             ("Yo ya hice mi parte", "Te espero adentro")]

# ───────────────────────────────────────────── utilidades
def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode: print(r.stderr[-3000:]); sys.exit(1)

def dur(p):
    s = subprocess.run([FF, '-i', p], capture_output=True, text=True).stderr.split('Duration: ')[1].split(',')[0]
    h, m, x = s.split(':'); return int(h)*3600 + int(m)*60 + float(x)

def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    return ''.join(c for c in s if c.isalnum() and unicodedata.category(c) != 'Mn')

def ts(t): return f'{int(t//3600)}:{int(t%3600//60):02d}:{t%60:05.2f}'

# ───────────────────────────────────────────── 1 · unir los bloques
src = os.path.join(TMP, 'avatar.mp4')
if not os.path.exists(src):
    hg = sorted(f for f in os.listdir(os.path.join(WORK, 'heygen')) if f.endswith('.mp4'))
    assert hg, 'no hay bloques en heygen/'
    lst = os.path.join(TMP, 'lista.txt')
    with open(lst, 'w') as fh:
        for f in hg:
            fh.write(f"file '{os.path.join(WORK,'heygen',f)}'\n")
    run([FF, '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst,
         '-vf', 'scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30',
         '-c:v', 'libx264', '-crf', '16', '-preset', 'fast', '-c:a', 'aac', '-b:a', '192k', src])
    print('unidos', len(hg), 'bloques ->', round(dur(src), 1), 's')

# ───────────────────────────────────────────── 2 · transcribir y alinear
cache = os.path.join(TMP, 'words0.json')
if os.path.exists(cache):
    words0 = json.load(open(cache))
else:
    from faster_whisper import WhisperModel
    wav = os.path.join(TMP, 'a.wav')
    run([FF, '-v', 'error', '-y', '-i', src, '-ac', '1', '-ar', '16000', wav])
    m = WhisperModel('small', device='cpu', compute_type='int8', cpu_threads=6)
    segs, _ = m.transcribe(wav, language='es', word_timestamps=True, beam_size=5)
    words0 = [{'w': w.word.strip(), 's': w.start, 'e': w.end} for s in segs for w in s.words]
    json.dump(words0, open(cache, 'w'), ensure_ascii=False)
print('palabras transcriptas:', len(words0))

ops = difflib.SequenceMatcher(None, [norm(w['w']) for w in words0],
                              [norm(x) for x in GUION.split()], autojunk=False).get_opcodes()
bad = {i for op, i1, i2, _, _ in ops if op == 'delete' for i in range(i1, i2)}
if bad: print('inventadas por Whisper:', ' '.join(words0[i]['w'] for i in sorted(bad))[:300])
words0 = [w for i, w in enumerate(words0) if i not in bad]

dur0 = dur(src)
keep, cur = [], 0.0
for a, b in zip(words0, words0[1:]):
    if b['s'] - a['e'] > GAP_MAX:
        keep.append((cur, min(a['e'] + GAP_KEEP/2, b['s'] - 0.05)))
        cur = b['s'] - GAP_KEEP/2
keep.append((cur, min(dur0, words0[-1]['e'] + 0.5)))

def mapt(t):
    acc = 0.0
    for a, b in keep:
        if t < a: return acc
        if t <= b: return acc + (t - a)
        acc += b - a
    return acc

trimmed = os.path.join(TMP, 'trimmed.mp4')
if not os.path.exists(trimmed):
    expr = '+'.join(f'between(t,{a:.3f},{b:.3f})' for a, b in keep)
    sel = os.path.join(TMP, 'sel.txt')
    at = f",atempo={SPEED}" if abs(SPEED - 1.0) > 1e-3 else ''
    pt = f"*{1/SPEED:.6f}" if abs(SPEED - 1.0) > 1e-3 else ''
    open(sel, 'w').write(
        f"[0:v]select='{expr}',setpts=N/FRAME_RATE/TB{pt}[v];[0:a]aselect='{expr}',asetpts=N/SR/TB{at}[a]")
    run([FF, '-v', 'error', '-y', '-i', src, '-filter_complex_script', sel, '-map', '[v]', '-map', '[a]',
         '-c:v', 'libx264', '-crf', '16', '-preset', 'fast', '-r', '30', '-c:a', 'aac', '-b:a', '192k', trimmed])
total = dur(trimmed)
print('despues del recorte:', round(total, 1), 's  (', round(total/60, 2), 'min )')

words = []
for w in words0:
    x = {'w': w['w'], 's': mapt(w['s'])/SPEED, 'e': mapt(w['e'])/SPEED}
    if words and x['w'][:1] == '-':
        words[-1] = {**words[-1], 'w': words[-1]['w'] + x['w'], 'e': x['e']}
    else: words.append(x)
gt = GUION.split()
a_, b_ = [norm(w['w']) for w in words], [norm(x) for x in gt]
# 2026-11-22 · Los bloques de LARGO DISTINTO tambien se reescriben con el texto del guion.
# Whisper escribe los precios en cifras ("17 ,990" por "diecisiete mil novecientos noventa") y
# oye "desparacitacion" donde el guion dice "desparasitacion": si no se reparten, el subtitulo
# quemado sale con el error a la vista y el ancla no engancha. Se reparte el tramo de tiempo
# entre las palabras del guion, a prorrata del largo de cada una.
rec = []
for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a_, b_, autojunk=False).get_opcodes():
    if op in ('equal', 'replace') and i2 - i1 == j2 - j1:
        for i, j in zip(range(i1, i2), range(j1, j2)):
            rec.append({**words[i], 'w': gt[j]})
    elif op == 'replace' and i2 - i1 <= 6 and j2 - j1 <= 12:
        a, b = words[i1]['s'], words[i2-1]['e']
        pes = [max(1, len(x)) for x in gt[j1:j2]]; tot = sum(pes); acc = 0.0
        for x, pe in zip(gt[j1:j2], pes):
            d1 = (b - a) * acc / tot; d2 = (b - a) * (acc + pe) / tot; acc += pe
            rec.append({'w': x, 's': a + d1, 'e': a + d2})
    elif op == 'replace':
        rec += [dict(words[i]) for i in range(i1, i2)]
words = rec
N = [norm(w['w']) for w in words]

def find(frase, fin=False):
    toks = [t for t in (norm(x) for x in frase.split()) if t]
    hits = [i for i in range(len(N)-len(toks)+1) if N[i:i+len(toks)] == toks]
    if not hits:
        print('  ⚠ NO ENCONTRADO:', frase); return None
    if len(hits) > 1: print('  · ambigua (%d):' % len(hits), frase)
    i = hits[0]
    return words[i+len(toks)-1]['e'] if fin else words[i]['s']

# ───────────────────────────────────────────── 3 · resolver anclas
veda = []
for a, b in PROHIBIDO:
    ta, tb = find(a), find(b, True)
    if ta is not None and tb is not None: veda.append((ta, tb))
def vedado(t): return any(a - 0.3 <= t <= b + 0.3 for a, b in veda)

cortes = []
for frase, clip in BROLL:
    t = find(frase)
    if t is None: continue
    if vedado(t): print('  · salteado (zona de cara):', frase); continue
    if cortes and t - cortes[-1][0] < 8.0:
        print('  · salteado (a menos de 8 s del anterior):', frase); continue
    cortes.append((t, clip))
print('b-rolls:', len(cortes), 'de', len(BROLL))

placas = []
for frase, png, seg in PLACAS:
    t = find(frase)
    if t is None: continue
    placas.append((t, png, seg))
print('placas:', len(placas), 'de', len(PLACAS))

json.dump({'total': total, 'cortes': cortes, 'placas': placas},
          open(os.path.join(TMP, 'plan.json'), 'w'), ensure_ascii=False, indent=1)

# ───────────────────────────────────────────── 4 · subtitulos
CLAVE = {norm(x) for x in (
 'parásito parásitos colágeno nueve días dolor intestino cirugía ibuprofeno gratis garantía '
 'carozo palta cúrcuma soltar limpiar reconstruir rodilla columna escalera nieto nunca '
 'ahora hoy gratis protocolo').split()}
# Placas que cubren la banda de subtitulos (y 1220): ahi el subtitulo se calla.
SIN_SUBS = {'resena1', 'resena2', 'resena3', 'stack', 'boton', 'cierre'}
mudo = [(t, t + seg) for t, png, seg in placas if png in SIN_SUBS]
def tapado(a, b): return any(a < y and x < b for x, y in mudo)

ev, i = [], 0
while i < len(words):
    grp = [words[i]]
    while (i + len(grp) < len(words) and len(grp) < 3
           and grp[-1]['w'][-1:] not in '.,?!…:;'
           and len(' '.join(w['w'] for w in grp)) + len(words[i+len(grp)]['w']) <= 20):
        grp.append(words[i+len(grp)])
    a = grp[0]['s']; i += len(grp)
    b = min(words[i]['s'] if i < len(words) else grp[-1]['e'] + 0.3, grp[-1]['e'] + 0.4)
    partes = []
    pinto = False
    for w in grp:
        t = w['w'].rstrip('.,?!…:;').upper()
        if not pinto and norm(w['w']) in CLAVE:
            partes.append('{\\c&H00D6FA&}' + t + '{\\r}'); pinto = True
        else: partes.append(t)
    if tapado(a, b): continue
    ev.append(f'Dialogue: 0,{ts(a)},{ts(b)},Cap,,0,0,0,,'
              f'{{\\pos(540,{CAP_Y})\\fscx88\\fscy88\\t(0,80,\\fscx100\\fscy100)}}' + ' '.join(partes))
ass = os.path.join(TMP, 'subs.ass')
open(ass, 'w', encoding='utf-8').write("""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Arial Black,76,&H00FFFFFF&,&H00FFFFFF&,&H00000000,&H64000000,0,0,0,0,100,100,1,0,1,7,3,5,60,60,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""" + '\n'.join(ev) + '\n')
print('subtitulos:', len(ev), 'bloques')

# ───────────────────────────────────────────── 5 · montaje por segmentos (§4f de la wiki)
# Un filtro unico con 60 capas sobre 16 min tarda horas: se parte la linea de tiempo en
# los bordes de cada b-roll y cada placa, y render_rapido.py los arma de a 8 en paralelo.
HERE  = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.expanduser('~/Library/Fonts')
LOOK  = 'eq=saturation=0.94:contrast=1.03,unsharp=5:5:0.6,'
vid   = os.path.join(TMP, 'video_voz.mkv')

json.dump({'trimmed': trimmed, 'ass': ass, 'fonts': FONTS, 'total': total,
           'tmp': os.path.join(TMP, 'segs'), 'split_y': 0, 'split_mask': '',
           'look': LOOK, 'zoom': [],
           'brolls': [[os.path.join(WORK, 'visuales', c + '.mp4'),
                       round(t, 3), round(t + CORTE, 3), 0.0, 'full', 0]
                      for t, c in cortes],
           'stickers': [[os.path.join(WORK, 'gfx', p + '.png'), round(t, 3), seg, 0, 0, 1080]
                        for t, p, seg in placas]},
          open(os.path.join(TMP, 'render.json'), 'w'), indent=1)
run(['python3', os.path.join(HERE, 'render_rapido.py'), os.path.join(TMP, 'render.json'), vid])

# ───────────────────────────────────────────── 6 · audio: voz + cama de suspenso con ducking
af = ["[0:a]loudnorm=I=-14:TP=-1.5:LRA=11,asplit=2[voz][sc]",
      "[1:a]volume=0.19,loudnorm=I=-33:TP=-9[mus]",
      "[mus][sc]sidechaincompress=threshold=0.03:ratio=3:attack=20:release=400[duck]",
      "[voz][duck]amix=inputs=2:normalize=0:duration=first,alimiter=limit=0.95[aout]"]
aff = os.path.join(TMP, 'af.txt'); open(aff, 'w').write(';\n'.join(af))
run([FF, '-v', 'error', '-y', '-i', vid, '-stream_loop', '-1', '-i', MUS,
     '-filter_complex_script', aff, '-map', '0:v', '-map', '[aout]',
     '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000',
     '-t', f'{total:.2f}', '-movflags', '+faststart', OUT])
print('LISTO:', OUT, round(dur(OUT), 1), 's  (', round(dur(OUT)/60, 2), 'min )')
