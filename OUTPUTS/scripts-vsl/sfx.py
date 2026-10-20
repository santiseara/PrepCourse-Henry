"""Efectos de sonido sintetizados (originales, sin licencias). Uso: python3 sfx.py <carpeta>"""
import sys, os, numpy as np
from scipy.signal import butter, sosfilt
from scipy.io import wavfile
SR = 44100
rng = np.random.default_rng(3)
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
def bp(x, lo, hi): return sosfilt(butter(2, [lo, hi], 'band', fs=SR, output='sos'), x)
def hp(x, f): return sosfilt(butter(2, f, 'high', fs=SR, output='sos'), x)
def t_(d): return np.arange(int(d * SR)) / SR
def bell(f, d, decay, partials=((1, 1), (2.76, .5), (5.4, .25), (8.93, .12))):
    t = t_(d)
    return sum(a * np.sin(2 * np.pi * f * m * t) * np.exp(-t / (decay / m ** .5)) for m, a in partials)
def save(name, x):
    x = x / np.max(np.abs(x)) * 0.9
    wavfile.write(os.path.join(out, name), SR, (np.stack([x, x], 1) * 32767).astype(np.int16))

# cha-ching: golpe metálico corto + campana brillante + monedas
d = 1.3; x = np.zeros(int(d * SR))
cha = hp(rng.standard_normal(int(.06 * SR)), 3000) * np.exp(-t_(.06) / .015) * .6
x[:len(cha)] += cha
c1 = bell(2093, .25, .05) * .5; x[int(.0 * SR):int(.0 * SR) + len(c1)] += c1
ching = bell(2637, 1.1, .45) * .9 + bell(3136, 1.1, .35) * .6
i = int(.12 * SR); x[i:i + len(ching)] += ching[:len(x) - i]
for k in range(10):   # monedas
    j = int((.14 + rng.uniform(0, .35)) * SR); c = bell(rng.uniform(4000, 6500), .12, .03) * .18
    x[j:j + len(c)] += c[:len(x) - j]
save('chaching.wav', x)

# ding suave
save('ding.wav', bell(1568, 1.2, .5) * .8 + bell(2349, 1.2, .35) * .3)

# pop + brillo (regalo)
t = t_(.35); f = 900 * np.exp(-t / .05) + 220
pop = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / .06)
spark = sum(bell(fq, .35, .12) for fq in (3520, 4186, 5274)) * .12
save('pop.wav', pop + spark)

# whoosh
t = t_(.6); n = rng.standard_normal(len(t))
w = np.zeros_like(t)
seg = 1024
for s in range(0, len(t), seg):
    fc = 400 + 5000 * (s / len(t)) ** 1.5
    w[s:s + seg] = bp(n[s:s + seg + 0], fc * .7, min(fc * 1.4, 18000))[:len(w[s:s + seg])]
e = np.sin(np.pi * np.clip(t / .6, 0, 1)) ** 2
save('whoosh.wav', w * e)

# sello (garantía): golpe grave + ding
t = t_(1.0); thump = np.sin(2 * np.pi * (60 + 80 * np.exp(-t / .03)) * t) * np.exp(-t / .1)
save('sello.wav', thump * .9 + bell(1318, 1.0, .4) * .35)
print('ok')
# Efectos para ads entretenidos (2026-10-20): pocos y en momentos clave
# buzzer de "error" (lista de errores)
t = t_(.45); bz = np.sign(np.sin(2 * np.pi * 110 * t)) * .5 + np.sign(np.sin(2 * np.pi * 116 * t)) * .5
save('buzzer.wav', bp(bz, 150, 3000) * np.minimum(1, (.45 - t) / .08))

# redoble corto antes de una revelación (redoble de tambor que crece)
d = 1.4; t = t_(d); x = np.zeros(len(t))
k, step = 0.0, .07
while k < d - .05:
    j = int(k * SR); hit = bp(rng.standard_normal(int(.05 * SR)), 900, 6000) * np.exp(-t_(.05) / .012)
    x[j:j + len(hit)] += hit[:len(x) - j] * (.35 + .65 * k / d); k += step; step = max(.03, step * .93)
save('drumroll.wav', x)

# tic-tac de reloj (pregunta "adiviná")
x = np.zeros(int(1.2 * SR))
for i, f in enumerate((2400, 1800, 2400, 1800)):
    j = int(i * .3 * SR); c = bell(f, .04, .008); x[j:j + len(c)] += c
save('tick.wav', x)

# lápiz que escribe (cuentas en la servilleta)
t = t_(.9); n = bp(rng.standard_normal(len(t)), 2500, 8000)
save('scribble.wav', n * (.4 + .6 * np.abs(np.sin(2 * np.pi * 7 * t))) * np.minimum(1, (.9 - t) / .1))
print('ok extra')

