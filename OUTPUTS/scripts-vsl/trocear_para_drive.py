# -*- coding: utf-8 -*-
"""Parte los MP4 de una tanda en trozos que SÍ entran por `file_upload`, para subirlos a Drive.

Por qué existe: desde el 2026-11-17 `file_upload` corta la conexión con cualquier archivo de más de
unos 800 KB ("the connection was lost before its result came back"). Un ad de 30-45 s pesa 7-10 MB,
así que no entra. La salida es mandarlo en partes y **recomponerlo dentro del navegador**, que no
tiene ese límite.

Uso: python3 trocear_para_drive.py <carpeta_con_mp4> <carpeta_de_partes> [bytes_por_parte]

Después, en la pestaña de Drive (ver WIKI/organizacion-y-registro.md):
  1. Parchear `HTMLInputElement.prototype.click` para capturar el input de Drive en `window.__cap`.
  2. Crear un input propio `window.__acum` con un listener que empuje cada archivo a `window.__acc`.
  3. Subir las partes de UN video con `file_upload` (hasta 8 por llamada de `browser_batch`).
  4. Recomponer:  new File([...partes ordenadas], '<nombre>.mp4', {type:'video/mp4'})
     y guardarlo en `window.__files`. Verificar con SHA-256 contra el archivo de disco.
  5. Con todos los videos armados: Nuevo -> Subir archivo, DataTransfer con `window.__files`,
     `inp.files = dt.files` y disparar `input` + `change`.

Medido el 17/11 con la tanda de macetas: 6 videos, 72 partes, 13 llamadas de `browser_batch`, y los
seis SHA-256 dieron idénticos a los del disco.
"""
import os, sys, glob

src = sys.argv[1]
dst = sys.argv[2]
CH = int(sys.argv[3]) if len(sys.argv) > 3 else 700_000

os.makedirs(dst, exist_ok=True)
for n, f in enumerate(sorted(glob.glob(os.path.join(src, '*.mp4'))), 1):
    d = open(f, 'rb').read()
    partes = [d[i:i + CH] for i in range(0, len(d), CH)]
    for k, p in enumerate(partes):
        open(os.path.join(dst, f'v{n}_{k:02d}.part'), 'wb').write(p)
    print(f'v{n}  {os.path.basename(f)}  {len(d)/1048576:.1f}MB -> {len(partes)} partes')
print('Las partes se ordenan por nombre: al recomponer, ordenar por f.name antes de armar el File.')
