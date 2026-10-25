"""Une las partes de HeyGen de un VSL largo en un solo mp4 vertical 1080x1920.
Uso: python3 unir_partes.py salida.mp4 parte1.mp4 parte2.mp4 ...
Normaliza resolución (720p y 1080p mezclados), fps y audio antes de concatenar."""
import subprocess, sys, os, tempfile
FF = os.path.expanduser('~/bin/ffmpeg')
out, partes = sys.argv[1], sys.argv[2:]
tmp = tempfile.mkdtemp()
norm = []
for i, p in enumerate(partes):
    o = os.path.join(tmp, f'n{i}.mp4')
    subprocess.run([FF, '-y', '-v', 'error', '-i', p,
                    '-vf', 'scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2,fps=30',
                    '-c:v', 'libx264', '-crf', '17', '-preset', 'medium',
                    '-c:a', 'aac', '-ar', '48000', '-ac', '2', '-b:a', '192k', o], check=True)
    norm.append(o); print('normalizada', os.path.basename(p), flush=True)
lst = os.path.join(tmp, 'list.txt')
open(lst, 'w').write('\n'.join(f"file '{p}'" for p in norm))
subprocess.run([FF, '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', out], check=True)
print('listo:', out)
