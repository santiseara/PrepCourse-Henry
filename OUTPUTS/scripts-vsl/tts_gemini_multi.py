# -*- coding: utf-8 -*-
"""Voz en off de DOS personajes con Gemini TTS (multiSpeakerVoiceConfig).
Uso: TTS_MODEL=.. python3 tts_gemini_multi.py guion.txt salida.wav style.txt Speaker1=Orus Speaker2=Sulafat
El guion lleva una linea por intervencion, con el prefijo "Speaker1: ".
Las voces fijas siguen siendo Orus (hombre) y Sulafat (mujer)."""
import base64, json, os, sys, urllib.request, wave

KEY = os.environ["GEMINI_API_KEY"]
MODEL = os.environ.get("TTS_MODEL", "gemini-2.5-flash-preview-tts")

txt_path, out_path, style_path = sys.argv[1], sys.argv[2], sys.argv[3]
pairs = [a.split('=') for a in sys.argv[4:]]
text = open(txt_path).read().strip()
style = open(style_path).read().rstrip()
prompt = style + "\n\n" + text

body = {
    "contents": [{"parts": [{"text": prompt}]}],
    "generationConfig": {
        "responseModalities": ["AUDIO"],
        "temperature": float(os.environ.get("TTS_TEMP", 1.0)),
        "speechConfig": {"multiSpeakerVoiceConfig": {"speakerVoiceConfigs": [
            {"speaker": s, "voiceConfig": {"prebuiltVoiceConfig": {"voiceName": v}}} for s, v in pairs]}},
    },
}
req = urllib.request.Request(
    f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={KEY}",
    data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
with urllib.request.urlopen(req, timeout=300) as r:
    d = json.load(r)
pcm, rate = b"", 24000
for p in d["candidates"][0]["content"]["parts"]:
    inl = p.get("inlineData") or p.get("inline_data")
    if inl:
        pcm += base64.b64decode(inl["data"])
        mt = inl.get("mimeType", inl.get("mime_type", ""))
        if "rate=" in mt: rate = int(mt.split("rate=")[1].split(";")[0])
if not pcm: raise SystemExit("sin audio: " + json.dumps(d)[:800])
with wave.open(out_path, "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(rate); w.writeframes(pcm)
print(out_path, round(len(pcm)/2/rate, 2), "s")
