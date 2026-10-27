"""Une las dos partes del VSL de Calistenia Rusa y le mezcla la música con ducking.
Las partes se editan con NOMUSIC=1 y la música se pone una sola vez al final, sobre el video entero.
Uso: python3 finish_calistenia_rusa.py
"""
import os, subprocess, sys, re

FF = os.path.expanduser('~/bin/ffmpeg')
HERE = os.path.dirname(os.path.abspath(__file__))
W = os.path.expanduser('~/Desktop/calistenia-rusa/vsl')
WORK = f'{W}/work'
P1, P2 = f'{WORK}/parte1.mp4', f'{WORK}/parte2.mp4'
UNIDO = f'{WORK}/unido.mp4'
FINAL = f'{W}/CALISTENIA-RUSA-VSL.mp4'

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-2500:]); sys.exit(1)
    return r

def dur(p):
    s = subprocess.run([FF, '-i', p], capture_output=True, text=True).stderr
    h, m, x = re.search(r'Duration: (\d+):(\d+):([\d.]+)', s).groups()
    return int(h) * 3600 + int(m) * 60 + float(x)

for p in (P1, P2):
    if not os.path.exists(p):
        print('falta', p); sys.exit(1)
print(f'parte 1: {dur(P1):.1f}s · parte 2: {dur(P2):.1f}s')

# 1. unir
run(['python3', os.path.join(HERE, 'unir_partes.py'), UNIDO, P1, P2])
total = dur(UNIDO)
print(f'unido: {total:.1f}s ({int(total//60)}:{int(total%60):02d})')

# 2. música original del largo exacto
mus = f'{WORK}/music/bed_full.wav'
run(['python3', os.path.join(HERE, 'music.py'), f'{total + 1:.1f}', mus])

# 3. mezcla: voz a -14 LUFS, música a -33 con ducking por sidechain
af = (
    "[0:a]loudnorm=I=-14:TP=-1.5:LRA=11,asplit=2[voz][sc];"
    "[1:a]loudnorm=I=-33:TP=-9[mus];"
    "[mus][sc]sidechaincompress=threshold=0.03:ratio=3:attack=20:release=400[duck];"
    "[voz][duck]amix=inputs=2:normalize=0:duration=first,alimiter=limit=0.95[aout]"
)
run([FF, '-v', 'error', '-y', '-i', UNIDO, '-i', mus, '-filter_complex', af,
     '-map', '0:v', '-map', '[aout]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
     '-ar', '48000', '-t', f'{total:.2f}', '-movflags', '+faststart', FINAL])

# 4. versión liviana para el quiz (720x1280, CRF 25, faststart)
WEB = f'{W}/CALISTENIA-RUSA-VSL-web.mp4'
run([FF, '-v', 'error', '-y', '-i', FINAL, '-vf', 'scale=720:1280', '-c:v', 'libx264',
     '-crf', '25', '-preset', 'medium', '-c:a', 'aac', '-b:a', '96k',
     '-movflags', '+faststart', WEB])

print('FINAL:', FINAL, f'{dur(FINAL):.1f}s', f'{os.path.getsize(FINAL)//1024//1024} MB')
print('WEB  :', WEB, f'{os.path.getsize(WEB)//1024//1024} MB')
