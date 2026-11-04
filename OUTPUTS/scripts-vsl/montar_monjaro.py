"""Une los tres bloques de HeyGen en el VSL final de Monjaro Violeta.

Dos cuidados:
  1. A cada bloque se le devuelve el WAV original en vez del audio que trae el
     video, que es el MP3 de 192k que se subio para el lipsync. Misma duracion,
     calce exacto, y se evita la doble compresion.
  2. Los intermedios NO van al Escritorio: esta sincronizado con iCloud y el
     concat de ffmpeg falla al abrir un archivo recien escrito. Van al
     scratchpad, que es disco local (regla de vsl-reglas-de-armado §0c).

Uso: python3 montar_monjaro.py
"""
import os
import subprocess
import tempfile

FF = os.path.expanduser('~/bin/ffmpeg')
VSL = os.path.expanduser('~/Desktop/monjaro-violeta/vsl')
TMP = os.environ.get('VSL_TMP') or tempfile.mkdtemp(prefix='monjaro_')

BLOQUES = [
    ('bloques/bloque1-mei.mp4',     'voz/bloque1-Vindemiatrix-final.wav'),
    ('bloques/bloque2-mariela.mp4', 'voz/bloque2-Gacrux-final.wav'),
    ('bloques/bloque3-mei.mp4',     'voz/bloque3-Vindemiatrix-final.wav'),
]


def run(cmd):
    subprocess.run(cmd, check=True)


def dur(path):
    out = subprocess.run(
        [FF, '-hide_banner', '-i', path], capture_output=True, text=True).stderr
    for line in out.splitlines():
        if 'Duration:' in line:
            h, m, s = line.split('Duration:')[1].split(',')[0].strip().split(':')
            return int(h) * 3600 + int(m) * 60 + float(s)
    return 0.0


def main():
    partes = []
    for i, (vid, wav) in enumerate(BLOQUES, 1):
        v, a = os.path.join(VSL, vid), os.path.join(VSL, wav)
        for p in (v, a):
            if not os.path.exists(p):
                raise SystemExit(f'falta {p}')
        dv, da = dur(v), dur(a)
        print(f'bloque{i}: video {dv:6.2f}s  audio {da:6.2f}s  desfase {dv-da:+.2f}s')

        out = os.path.join(TMP, f'b{i}.mp4')
        # el video manda: si el wav quedara un pelo mas largo, se corta con -shortest
        run([FF, '-v', 'error', '-y', '-i', v, '-i', a,
             '-map', '0:v:0', '-map', '1:a:0',
             '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000',
             '-shortest', out])
        partes.append(out)

    lista = os.path.join(TMP, 'lista.txt')
    with open(lista, 'w') as f:
        for p in partes:
            f.write(f"file '{p}'\n")

    final = os.path.join(VSL, 'VSL-monjaro-violeta.mp4')
    run([FF, '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lista,
         '-c', 'copy', final])
    d = dur(final)
    m, s = divmod(round(d), 60)
    print(f'\nVSL-monjaro-violeta.mp4 · {m}:{s:02d} · {os.path.getsize(final)/1e6:.1f} MB')
    print(f'→ {final}')


if __name__ == '__main__':
    main()
