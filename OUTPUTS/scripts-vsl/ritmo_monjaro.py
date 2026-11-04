"""Empareja el ritmo de los bloques de voz de un VSL antes de mandarlos a HeyGen.

Hace tres cosas por bloque, en este orden:
  1. recorta las pausas largas (no las colas de palabras),
  2. mide los ppm reales DESPUES del recorte,
  3. calcula el atempo propio de ese bloque para llegar al objetivo.

El paso 2 es el que importa: el mismo atempo para todos deja los bloques
descompensados, porque el recorte de silencios le saca distinta cantidad a cada
uno (regla de vsl-reglas-de-armado §2).

Acelerar aca y no en el montaje tambien abarata HeyGen, que cobra por segundo
de video renderizado.

Uso: python3 ritmo_monjaro.py <ppm_objetivo> <wav_entrada> [<wav_entrada> ...]
Escribe <nombre>-final.wav al lado de cada entrada.
"""
import os
import subprocess
import sys
import wave

FF = os.path.expanduser('~/bin/ffmpeg')
TRIM = ('silenceremove=start_periods=1:start_threshold=-55dB:'
        'stop_periods=-1:stop_duration=0.26:stop_threshold=-55dB:stop_silence=0.12')


def run(cmd):
    subprocess.run(cmd, check=True)


def dur(path):
    with wave.open(path) as w:
        return w.getnframes() / w.getframerate()


def palabras(wav):
    """Las palabras del guion que le corresponde a este wav."""
    base = os.path.basename(wav).split('-')[0]          # bloque2-Sulafat.wav -> bloque2
    txt = os.path.join(os.path.dirname(wav), base + '.txt')
    return len(open(txt, encoding='utf-8').read().split())


def main():
    objetivo = float(sys.argv[1])
    total = 0.0
    for src in sys.argv[2:]:
        n = palabras(src)
        tmp = src.replace('.wav', '-trim.wav')
        run([FF, '-v', 'error', '-y', '-i', src, '-af', TRIM, '-ar', '24000', '-ac', '1', tmp])

        d_trim = dur(tmp)
        ppm_trim = n / (d_trim / 60)
        tempo = ppm_trim and objetivo / ppm_trim

        # ffmpeg solo acepta atempo entre 0.5 y 2.0; encadenar si hiciera falta
        cadena, t = [], tempo
        while t > 2.0:
            cadena.append(2.0)
            t /= 2.0
        while t < 0.5:
            cadena.append(0.5)
            t /= 0.5
        cadena.append(t)
        af = ','.join(f'atempo={x:.4f}' for x in cadena)

        out = src.replace('.wav', '-final.wav')
        run([FF, '-v', 'error', '-y', '-i', tmp, '-af', f'{af},aresample=24000',
             '-ar', '24000', '-ac', '1', out])
        os.remove(tmp)

        d_fin = dur(out)
        total += d_fin
        print(f'{os.path.basename(src):32s} {n:4d} pal  '
              f'crudo {dur(src):6.1f}s  recortado {d_trim:6.1f}s ({ppm_trim:5.1f} ppm)  '
              f'atempo {tempo:.3f}  final {d_fin:6.1f}s ({n/(d_fin/60):5.1f} ppm)')
    m, s = divmod(round(total), 60)
    print(f'\nVSL final: {m}:{s:02d} ({total:.1f} s)')


if __name__ == '__main__':
    main()
