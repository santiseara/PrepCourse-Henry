# -*- coding: utf-8 -*-
"""Saca la voz de un ad ajeno y deja SOLO la cama musical (htdemucs, dos stems).
No se usa el CLI de demucs: lee el audio con ffprobe y en esta Mac ffprobe es un shim que
solo devuelve duracion, asi que el JSON revienta. Aca el wav entra por soundfile.
Uso: python3 stems.py entrada.wav salida_instrumental.wav"""
import sys, numpy as np, soundfile as sf, torch
from demucs.pretrained import get_model
from demucs.apply import apply_model

ent, sal = sys.argv[1], sys.argv[2]
x, sr = sf.read(ent, dtype='float32')
if x.ndim == 1: x = np.stack([x, x], 1)
m = get_model('htdemucs')
m.eval()
if sr != m.samplerate:
    raise SystemExit(f'el modelo quiere {m.samplerate} Hz y el wav tiene {sr}')
wav = torch.from_numpy(x.T)[None]
ref = wav.mean(1, keepdim=True)
mean, std = ref.mean(), ref.std()
with torch.no_grad():
    out = apply_model(m, (wav - mean) / std, device='cpu', split=True, overlap=0.25, progress=False)[0]
out = out * std + mean
src = dict(zip(m.sources, out))                      # drums bass other vocals
inst = (src['drums'] + src['bass'] + src['other']).numpy().T
sf.write(sal, inst, sr)
print(f'{sal} {len(inst)/sr:.1f} s instrumental')
