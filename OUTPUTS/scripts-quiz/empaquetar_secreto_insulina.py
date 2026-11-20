# -*- coding: utf-8 -*-
"""Deja UN solo archivo: el quiz de El Secreto de la Insulina (AR) con las
   14 fotos adentro en base64, listo para pegar en ImpulTienda."""
import base64, os, re

L = os.path.expanduser('~/Desktop/secreto-insulina/landing')
I = os.path.expanduser('~/Desktop/secreto-insulina/imagenes')
doc = open(L + '/quiz.html', encoding='utf-8').read()

# cada "clave: "../imagenes/archivo.webp"" pasa a "clave: "data:image/webp;base64,..."
rutas = re.findall(r'"\.\./imagenes/([^"]+)"', doc)
assert rutas, 'no encontre ninguna ruta de imagen'
for nombre in sorted(set(rutas)):
    p = os.path.join(I, nombre)
    assert os.path.exists(p), 'falta ' + p
    uri = 'data:image/webp;base64,' + base64.b64encode(open(p, 'rb').read()).decode()
    doc = doc.replace('"../imagenes/%s"' % nombre, '"%s"' % uri)

assert '../imagenes/' not in doc, 'quedo una ruta sin embeber'

cab = """<!--
  ===========================================================================
  EL SECRETO DE LA INSULINA — quiz para ARGENTINA — 20/11/2026
  Calcado de segredo-insulina-quiz.vercel.app (la version brasilena propia).
  Todo adentro de este archivo: no hay que subir ninguna imagen.
  Precio: $16.990 (6 cuotas de $2.832) · Checkout: relativo /checkout
  Para poner el checkout definitivo: CONFIG.CHECKOUT, arriba de todo.
  ===========================================================================
-->
"""
out = cab + doc
open(L + '/secreto-insulina-quiz.txt', 'w', encoding='utf-8').write(out)
open(L + '/secreto-insulina-PRUEBA.html', 'w', encoding='utf-8').write(out)
print('archivo', len(out) // 1024, 'KB')
print('data: URIs', out.count('data:image/webp'))
print('imagenes distintas', len(set(rutas)))
