# Comprime cada imagen segun el tamano real en el que se ve en el quiz
import os, glob, json
from PIL import Image
D=os.path.expanduser('~/Desktop/helados/landing/imagenes')
OUT=os.path.expanduser('~/Desktop/helados/landing/img_min')
os.makedirs(OUT, exist_ok=True)
# ancho objetivo por rol
GRANDE={'1'}                                   # portada
MEDIO={'2','12','3','4','13','25'}             # mockups y fotos de puente
# el resto son miniaturas (sabores, testimonios, tapas)
tot=0
for f in sorted(glob.glob(D+'/*.webp')):
    k=os.path.basename(f).split('-')[0]
    if k in GRANDE: w,q=720,70
    elif k in MEDIO: w,q=620,66
    else: w,q=420,64
    im=Image.open(f).convert('RGB')
    if im.width>w:
        im=im.resize((w,round(im.height*w/im.width)), Image.LANCZOS)
    o=OUT+'/'+os.path.basename(f)
    im.save(o,'WEBP',quality=q,method=6)
    tot+=os.path.getsize(o)
print('total', tot//1024, 'KB  ->  base64', int(tot*4/3)//1024, 'KB')
