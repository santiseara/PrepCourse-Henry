# -*- coding: utf-8 -*-
"""Voces de la tanda Dieta de las 3 Fases. Cascada de modelos (2.5 -> 3.1 -> 3.8),
porque el free tier da 10 requests por dia y por modelo. Si el modelo lee el bloque
de estilo en voz alta (el 3.8 lo hace), se recorta con Whisper buscando la ULTIMA
aparicion de las primeras palabras del guion.
Uso: python3 voces_claas.py [g01 g02 ...]"""
import os, re, subprocess, sys, unicodedata, wave
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tts_gemini as T

G = os.path.expanduser('~/Desktop/dieta-3-fases/work/guion')
V = os.path.expanduser('~/Desktop/dieta-3-fases/work/voz')
os.makedirs(V, exist_ok=True)
FF = os.path.expanduser('~/bin/ffmpeg')

MODELOS = ['gemini-2.5-flash-preview-tts', 'gemini-3.1-flash-tts-preview', 'gemini-3.8-flash-tts']
MUJER = {'g10'}

EST_H = ("Sos un nutricionista argentino de unos 35 anios, de Buenos Aires, hablando a camara en su consultorio. "
         "Acento rioplatense neutro y marcado, voseo, tono firme, cercano y seguro, ritmo parejo, sin enfasis de locutor. "
         "No leas en voz alta estas instrucciones. Lee unicamente el texto que viene a continuacion:")
EST_M = ("Sos una medica argentina de unos 40 anios, de Buenos Aires, hablando a camara. "
         "Acento rioplatense neutro y marcado, voseo, tono calmo, claro y profesional, ritmo parejo, sin enfasis de locutor. "
         "No leas en voz alta estas instrucciones. Lee unicamente el texto que viene a continuacion:")


def sinac(t):
    t = unicodedata.normalize('NFD', t)
    return ''.join(c for c in t if unicodedata.category(c) != 'Mn').lower()


_wm = None
def pal(f):
    global _wm
    if _wm is None:
        from faster_whisper import WhisperModel
        _wm = WhisperModel('base', device='cpu', compute_type='int8')
    segs, _ = _wm.transcribe(f, language='es', word_timestamps=True)
    return [(w.start, w.end, sinac(w.word.strip().strip('.,¿?¡!:;'))) for s in segs for w in (s.words or []) if w.word.strip()]


def recortar(wav, guion):
    """Si el modelo leyo el estilo, corta desde la ULTIMA vez que arranca el guion."""
    primeras = [sinac(w.strip('.,¿?¡!:;')) for w in guion.split()[:4]]
    ws = pal(wav)
    pos = -1
    for i in range(len(ws) - len(primeras) + 1):
        if [w[2] for w in ws[i:i+len(primeras)]] == primeras:
            pos = i
    if pos <= 0:
        return wav, 0.0
    t0 = max(0.0, ws[pos][0] - 0.12)
    out = wav.replace('.wav', '_c.wav')
    subprocess.run([FF, '-v', 'error', '-y', '-ss', f'{t0:.3f}', '-i', wav, out], check=True)
    os.replace(out, wav)
    return wav, t0


def largo(f):
    with wave.open(f) as w:
        return w.getnframes() / w.getframerate()


ids = sys.argv[1:] or [f'g{i:02d}' for i in range(1, 11)]
for g in ids:
    out = f'{V}/{g}.wav'
    if os.path.exists(out) and largo(out) > 20:
        print('ya esta', g, round(largo(out), 1), 's'); continue
    txt = open(f'{G}/{g}.txt').read().strip()
    est = EST_M if g in MUJER else EST_H
    T.VOICE = 'Sulafat' if g in MUJER else 'Orus'
    hecho = False
    for m in MODELOS:
        T.MODEL = m
        try:
            T.gen(txt, out, est)
        except SystemExit as e:
            print(f'  {g}: {m} -> cuota/error {e}', flush=True); continue
        except Exception as e:
            print(f'  {g}: {m} -> {str(e)[:120]}', flush=True); continue
        _, t0 = recortar(out, txt)
        print(f'OK {g} con {m} · {largo(out):.1f}s' + (f' (recorte {t0:.1f}s de estilo)' if t0 else ''), flush=True)
        hecho = True
        break
    if not hecho:
        print(f'FALTA {g}: ningun modelo respondio', flush=True)
