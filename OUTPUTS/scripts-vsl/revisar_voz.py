"""Revisa un WAV de voz contra su guion: palabras mal dichas, de más, de menos, estiradas y huecos.
Uso: python3 revisar_voz.py audio.wav guion.txt"""
import sys, os, subprocess, difflib, unicodedata, tempfile
from faster_whisper import WhisperModel
FF = os.path.expanduser('~/bin/ffmpeg')
wav, guion = sys.argv[1], sys.argv[2]
txt = open(guion, encoding='utf-8').read()
def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    return ''.join(c for c in s if c.isalnum() and unicodedata.category(c) != 'Mn')
tmp = os.path.join(tempfile.gettempdir(), 'rev16k.wav')
subprocess.run([FF, '-y', '-v', 'error', '-i', wav, '-ac', '1', '-ar', '16000', tmp], check=True)
m = WhisperModel('small', device='cpu', compute_type='int8')
segs, _ = m.transcribe(tmp, language='es', word_timestamps=True, vad_filter=False, beam_size=5)
W = [{'w': w.word.strip(), 's': w.start, 'e': w.end} for s in segs for w in s.words]
A, B = [norm(x['w']) for x in W], [norm(x) for x in txt.split()]
G = txt.split()
problemas = []
for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, A, B, autojunk=False).get_opcodes():
    if op == 'equal': continue
    dicho = ' '.join(x['w'] for x in W[i1:i2]) or '—'
    guionp = ' '.join(G[j1:j2]) or '—'
    t = W[i1]['s'] if i1 < len(W) else (W[-1]['e'] if W else 0)
    problemas.append((t, op, guionp, dicho))
largas = [(x['s'], x['w'], x['e'] - x['s']) for x in W if x['e'] - x['s'] > 1.1 and len(x['w']) > 2]
huecos = [(W[i]['e'], W[i + 1]['s'] - W[i]['e'], W[i]['w'], W[i + 1]['w'])
          for i in range(len(W) - 1) if W[i + 1]['s'] - W[i]['e'] > 1.3]
dur = W[-1]['e'] if W else 0
print(f'== {os.path.basename(wav)} · {len(W)} palabras dichas / {len(G)} del guion · {dur:.1f}s · {len(W)/max(dur,1)*60:.0f} ppm')
if problemas:
    print(f'  DIFERENCIAS ({len(problemas)}):')
    for t, op, g, d in problemas[:25]: print(f'   {t:7.1f}s  {op:9s} guion="{g}"  dijo="{d}"')
else:
    print('  texto: OK, dice exactamente el guion')
if largas:
    print(f'  PALABRAS ESTIRADAS ({len(largas)}):', ', '.join(f'{w} {d:.1f}s@{t:.0f}s' for t, w, d in largas[:12]))
if huecos:
    print(f'  HUECOS ({len(huecos)}):', ', '.join(f'{d:.1f}s entre "{a}" y "{b}"@{t:.0f}s' for t, d, a, b in huecos[:12]))
if not largas and not huecos: print('  ritmo: OK, sin estiramientos ni silencios raros')
