# -*- coding: utf-8 -*-
"""Deja UN solo archivo: el quiz con todas las fotos adentro, listo para pegar."""
import base64, json, os, re
L=os.path.expanduser('~/Desktop/helados/landing')
doc=open(L+'/quiz_latam.html',encoding='utf-8').read()
mapa=json.load(open('/tmp/mapa.json'))          # clave -> nombre de archivo

def uri(f):
    return 'data:image/webp;base64,'+base64.b64encode(open(L+'/img_min/'+f,'rb').read()).decode()

# archivos unicos y a que claves corresponden
porarch={}
for k,f in mapa.items(): porarch.setdefault(f,[]).append(k)
lineas, alias = [], []
for f,ks in sorted(porarch.items(), key=lambda kv: int(kv[1][0])):
    ks=sorted(ks,key=int)
    lineas.append("%s: '%s'" % (ks[0], uri(f)))
    for k in ks[1:]: alias.append("d[%s]=d[%s];" % (k, ks[0]))

bloque = ('imagenes: (function(){var d={\n' + ',\n'.join(lineas) + '\n};\n' + ' '.join(alias) + '\nreturn d;})(),')
i=doc.index('imagenes: {'); j=doc.index('\n}', i)
doc = doc[:i] + bloque + doc[j+2:]

# ya no hace falta la carpeta de recursos
doc = doc.replace("baseImagenes: 'PEGA_ACA_LA_CARPETA_DE_RECURSOS/',   // ej: https://cdn.impultienda.ar/store-resources/<tu-id>/\n", "")
doc = doc.replace("\nif (url && url.indexOf('http') !== 0 && url.indexOf('data:') !== 0) url = (CONFIG.baseImagenes || '') + url;", "")
doc = doc.replace('src="PEGA_ACA_LA_CARPETA_DE_RECURSOS/sello-pago.webp"', 'src="%s"' % uri('sello-pago.webp'))

cab = """<!--
  ===========================================================================
  HELADOS QUE VENDEN - quiz para LATAM (espanol neutro) - 19/11/2026
  Todo adentro de este archivo: no hay que subir ninguna imagen.
  Checkout: https://helados-que-vendenn.impultienda.ar/checkout - Precio: US$ 12
  ===========================================================================
-->
"""
out = cab + doc
open(L+'/helados-que-venden-LATAM-quiz.txt','w',encoding='utf-8').write(out)
print('archivo', len(out)//1024, 'KB')
print('data: URIs', out.count('data:image/webp'))
print('placeholders que quedan:', out.count('PEGA_ACA'))
