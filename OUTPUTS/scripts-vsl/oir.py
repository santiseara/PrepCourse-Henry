# -*- coding: utf-8 -*-
"""Le manda un wav a Gemini y le pregunta que variedad de espanol escucha.
Control gratis antes de renderizar una tanda (regla del 2/11/2026).
Uso: python3 oir.py <wav> [pregunta]
"""
import base64, json, os, sys, urllib.request
KEY = os.environ['GEMINI_API_KEY']
MODEL = os.environ.get('OIR_MODEL', 'gemini-3.5-flash')
wav = sys.argv[1]
q = sys.argv[2] if len(sys.argv) > 2 else (
    'Escucha este audio. 1) Que variedad de espanol habla (pais y region)? '
    '2) Suena natural o robotico/leido? 3) Transcribi lo que dice. Se breve y directo.')
body = {'contents': [{'parts': [
    {'text': q},
    {'inlineData': {'mimeType': 'audio/wav', 'data': base64.b64encode(open(wav, 'rb').read()).decode()}}]}]}
req = urllib.request.Request(
    f'https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={KEY}',
    data=json.dumps(body).encode(), headers={'Content-Type': 'application/json'})
with urllib.request.urlopen(req, timeout=180) as r:
    d = json.load(r)
print('\n'.join(p.get('text', '') for p in d['candidates'][0]['content']['parts']))
