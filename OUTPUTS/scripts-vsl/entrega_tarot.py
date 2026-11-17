"""Entrega de la tanda de tarot: mueve los renders de work/ a anuncios/ con el nombre de tanda
y deja un archivo por pieza (regla del 5/11: en la carpeta que el abre no hay duplicados).

Uso: python3 entrega_tarot.py <dir_oferta> <DD-M>
"""
import os, shutil, sys

OF = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser('~/Desktop/tarot-2-dias')
TANDA = sys.argv[2] if len(sys.argv) > 2 else '17-11'

WORK = os.path.join(OF, 'anuncios', 'work')
DST = os.path.join(OF, 'anuncios')
os.makedirs(DST, exist_ok=True)

# nombre por el arranque del hook, para el Drive
HOOKS = {
    'V1': 'If this card scares you',
    'V2': 'Do you think Death means somebody is going to die',
    'V3': 'Pick a card one two or three',
    'V4': 'You bought a tarot deck and it is still in the box',
    'V5': 'If you have been wanting to learn tarot',
    'V6': 'POV the tarot guide that finally made it click',
}

for i, v in enumerate(['V1', 'V2', 'V3', 'V4', 'V5', 'V6'], start=1):
    src = os.path.join(WORK, f'{v}.mp4')
    if not os.path.exists(src):
        print(f'falta {v}.mp4'); continue
    dst = os.path.join(DST, f'{TANDA} - {i}.mp4')
    shutil.move(src, dst)                      # se MUEVE, no se copia
    print(f'{v} -> {os.path.basename(dst)}  ({HOOKS[v]})')

# limpiar los _tmp del editor
for d in os.listdir(WORK):
    p = os.path.join(WORK, d)
    if d.endswith('_tmp') and os.path.isdir(p):
        shutil.rmtree(p); print('borrado', d)
print('listo')
