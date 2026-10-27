"""Revisa el VSL final de Calistenia Rusa: hoja de contactos, cuadros a resolución completa
y el segundo exacto en que se dice el precio (para SEGUNDOS_OFERTA del quiz).
Uso: python3 revisar_calistenia_rusa.py
"""
import os, re, subprocess, json, glob, unicodedata

FF = os.path.expanduser('~/bin/ffmpeg')
W = os.path.expanduser('~/Desktop/calistenia-rusa/vsl')
FINAL = f'{W}/CALISTENIA-RUSA-VSL.mp4'
TMP = f'{W}/work/revision'
os.makedirs(TMP, exist_ok=True)

def dur(p):
    s = subprocess.run([FF, '-i', p], capture_output=True, text=True).stderr
    h, m, x = re.search(r'Duration: (\d+):(\d+):([\d.]+)', s).groups()
    return int(h) * 3600 + int(m) * 60 + float(x)

total = dur(FINAL)
print(f'VSL final: {total:.1f}s ({int(total//60)}:{int(total%60):02d}) · {os.path.getsize(FINAL)//1024//1024} MB')

# ---- 1. hoja de contactos: un cuadro cada 3 s ----
for f in glob.glob(f'{TMP}/c*.jpg'):
    os.remove(f)
subprocess.run([FF, '-y', '-v', 'error', '-i', FINAL, '-vf', 'fps=1/3,scale=180:-1',
                f'{TMP}/c%03d.jpg'], check=True)
from PIL import Image, ImageDraw
fs = sorted(glob.glob(f'{TMP}/c*.jpg'))
TW = 180; TH = int(Image.open(fs[0]).height)
COLS = 12; rows = (len(fs) + COLS - 1) // COLS
sh = Image.new('RGB', (COLS * TW, rows * (TH + 16)), 'white')
d = ImageDraw.Draw(sh)
for i, f in enumerate(fs):
    sh.paste(Image.open(f).convert('RGB'), ((i % COLS) * TW, (i // COLS) * (TH + 16) + 16))
    d.text(((i % COLS) * TW + 3, (i // COLS) * (TH + 16) + 3), f'{i*3}s', fill='red')
sh.save(f'{W}/REVISION-hoja-de-contactos.jpg', quality=88)
print('hoja de contactos:', f'{W}/REVISION-hoja-de-contactos.jpg', sh.size)

# ---- 2. el segundo exacto del precio ----
def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    return ''.join(c for c in s if c.isalnum() and unicodedata.category(c) != 'Mn')

cache = f'{TMP}/words_final.json'
if os.path.exists(cache):
    words = json.load(open(cache))
else:
    from faster_whisper import WhisperModel
    wav = f'{TMP}/final16k.wav'
    subprocess.run([FF, '-y', '-v', 'error', '-i', FINAL, '-ac', '1', '-ar', '16000', wav], check=True)
    m = WhisperModel('small', device='cpu', compute_type='int8')
    segs, _ = m.transcribe(wav, language='es', word_timestamps=True, beam_size=5)
    words = [{'w': w.word.strip(), 's': w.start, 'e': w.end} for s in segs for w in s.words]
    json.dump(words, open(cache, 'w'), ensure_ascii=False)

N = [norm(w['w']) for w in words]
def buscar(frase):
    toks = [t for t in (norm(x) for x in frase.split()) if t]
    return [words[i]['s'] for i in range(len(N) - len(toks) + 1) if N[i:i + len(toks)] == toks]

print(f'\ntranscripción del final: {len(words)} palabras, {words[-1]["e"]:.1f}s')
hitos = [
    ('precio tachado',  ['normalmente cuesta', 'cuarenta y siete', '47']),
    ('PRECIO',          ['por solo diecisiete', 'diecisiete mil', '17']),
    ('garantía',        ['te devuelvo cada peso']),
    ('cierre',          ['hacé clic en el botón', 'hace clic en el boton']),
]
precio_t = None
for nombre, alts in hitos:
    for a in alts:
        t = buscar(a)
        if t:
            print(f'  {nombre:16} {t[0]:6.1f}s  ({int(t[0]//60)}:{int(t[0]%60):02d})  «{a}»')
            if nombre == 'PRECIO' and precio_t is None:
                precio_t = t[0]
            break
    else:
        print(f'  {nombre:16} no encontrado')

if precio_t:
    seg = int(precio_t) + 3    # la oferta aparece unos segundos después de que lo dice
    print(f'\n>>> SEGUNDOS_OFERTA = {seg}   ({int(seg//60)}:{int(seg%60):02d})')
    print('    (el segundo en que dice el precio, + 3 s de aire)')
