# -*- coding: utf-8 -*-
"""Genera una imagen con los modelos de imagen de Gemini, con imagenes de referencia opcionales.
Uso: IMG_MODEL=gemini-3.1-flash-image python3 img_gemini.py prompt.txt salida.png [ref1.jpg ref2.jpg ...]
El modelo barato es el flash; si el texto en castellano sale mal, se sube a gemini-3-pro-image."""
import base64, json, mimetypes, os, sys, urllib.request, urllib.error

KEY = [l.split('=', 1)[1].strip().strip('"').strip("'")
       for l in open(os.path.expanduser('~/.keys/gemini.env')) if 'GEMINI_API_KEY=' in l][0]
MODEL = os.environ.get('IMG_MODEL', 'gemini-3.1-flash-image')
prompt_path, out_path, refs = sys.argv[1], sys.argv[2], sys.argv[3:]

parts = []
for r in refs:
    parts.append({'inline_data': {'mime_type': mimetypes.guess_type(r)[0] or 'image/jpeg',
                                  'data': base64.b64encode(open(r, 'rb').read()).decode()}})
parts.append({'text': open(prompt_path, encoding='utf-8').read()})
body = {'contents': [{'parts': parts}],
        'generationConfig': {'responseModalities': ['IMAGE'],
                             'imageConfig': {'aspectRatio': os.environ.get('IMG_AR', '9:16')}}}
req = urllib.request.Request(
    f'https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={KEY}',
    data=json.dumps(body).encode(), headers={'Content-Type': 'application/json'})
try:
    d = json.load(urllib.request.urlopen(req, timeout=600))
except urllib.error.HTTPError as e:
    raise SystemExit('HTTP %d: %s' % (e.code, e.read().decode()[:600]))
c = d['candidates'][0]
if 'content' not in c:
    raise SystemExit('sin imagen, finishReason=%s' % c.get('finishReason'))
for p in c['content']['parts']:
    inl = p.get('inlineData') or p.get('inline_data')
    if inl:
        open(out_path, 'wb').write(base64.b64decode(inl['data']))
        print(out_path, os.path.getsize(out_path) // 1024, 'KB', '·', MODEL)
        break
else:
    raise SystemExit('la respuesta no trajo imagen: ' + json.dumps(d)[:500])
