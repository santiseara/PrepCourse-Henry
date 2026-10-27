"""Deja la carpeta de un VSL con lo fundamental a la vista y el resto en material/.
No borra nada: mueve. Uso: python3 ordenar_carpeta_vsl.py <carpeta>
"""
import os, shutil, sys

W = os.path.abspath(os.path.expanduser(sys.argv[1]))
MAT = os.path.join(W, 'material')

# lo único que queda arriba: el video, la revisión y las instrucciones
A_LA_VISTA = {'material'}
def fundamental(n):
    return (n.endswith('.mp4') and n.upper().startswith('CALISTENIA')) or \
           n.startswith('REVISION-') or n in {'LEEME.txt', 'guion.txt'}

os.makedirs(MAT, exist_ok=True)
movidos = []
for n in sorted(os.listdir(W)):
    if n.startswith('.') or n in A_LA_VISTA or fundamental(n):
        continue
    dst = os.path.join(MAT, n)
    if os.path.exists(dst):
        shutil.rmtree(dst) if os.path.isdir(dst) else os.remove(dst)
    shutil.move(os.path.join(W, n), dst)
    movidos.append(n)

print('a la vista:', ', '.join(sorted(n for n in os.listdir(W) if not n.startswith('.'))))
print(f'a material/: {len(movidos)} cosas —', ', '.join(movidos))
