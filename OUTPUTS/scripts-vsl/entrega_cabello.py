#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Entrega de la tanda de Cabello Fuerte: de work/salida a anuncios/ con el
nombre del arranque del hook, mas los dos txt que Santiago abre al lado.

Uso: python3 entrega_cabello.py [DD-MM]
"""
import os, shutil, sys, unicodedata

OF = os.path.expanduser('~/Desktop/cabello-fuerte')
TANDA = sys.argv[1] if len(sys.argv) > 1 else '18-11'
SAL = os.path.join(OF, 'work', 'salida')
DST = os.path.join(OF, 'anuncios')

HOOKS = {
    1: 'Destrui tu caida de pelo esta misma noche',
    2: 'El aceite de ricino podes tirarlo a la basura',
    3: 'Lo que te esta tirando abajo el pelo no es la edad',
    4: 'El truco del ajo con limon frena la caida',
    5: 'Este es el pelo de mi mujer despues del ajo',
    6: 'Vos creeis que es caida de pelo normal',
    7: 'Gastaste un millon en tratamientos y se cayo igual',
    8: 'Tira a la basura estas tres cositas de tu bano',
}


def sinacento(t):
    return ''.join(c for c in unicodedata.normalize('NFD', t)
                   if unicodedata.category(c) != 'Mn')


def main():
    os.makedirs(DST, exist_ok=True)
    # la carpeta que el abre no lleva duplicados ni descartes de corridas viejas
    for f in os.listdir(DST):
        if f.endswith('.mp4'):
            os.remove(os.path.join(DST, f))
    for i in sorted(HOOKS):
        src = os.path.join(SAL, f'{i:02d}.mp4')
        if not os.path.exists(src) or os.path.getsize(src) < 200000:
            print(f'falta {i:02d}.mp4'); continue
        dst = os.path.join(DST, f'{TANDA} - {i} {sinacento(HOOKS[i])}.mp4')
        shutil.copy2(src, dst)
        print(f'{os.path.basename(dst)}  {os.path.getsize(dst)//1024//1024} MB')
    print('listo')


if __name__ == '__main__':
    main()
