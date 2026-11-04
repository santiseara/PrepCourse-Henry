import base64, json, os, sys, time, urllib.request, urllib.error, wave
k = os.environ["GEMINI_API_KEY"]
S = os.path.dirname(os.path.abspath(__file__))
V = os.path.expanduser("~/Desktop/monjaro-violeta/vsl/voz")
style = open(f"{S}/style_mariela2.txt").read().rstrip()
text = open(f"{V}/bloque2.txt").read().strip()
out = f"{V}/bloque2-Gacrux.wav"
# el filtro marca SAFETY por las cifras de descenso de peso: falso positivo
# sobre un testimonio de marketing. Se baja el umbral de las cuatro categorias.
safety = [{"category": c, "threshold": "BLOCK_NONE"} for c in
          ["HARM_CATEGORY_HARASSMENT", "HARM_CATEGORY_HATE_SPEECH",
           "HARM_CATEGORY_SEXUALLY_EXPLICIT", "HARM_CATEGORY_DANGEROUS_CONTENT"]]
body = {"contents": [{"parts": [{"text": style + "\n\n" + text}]}],
        "safetySettings": safety,
        "generationConfig": {"responseModalities": ["AUDIO"], "temperature": 1.0,
                             "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": "Gacrux"}}}}}
for i in range(1, 13):
    try:
        req = urllib.request.Request(
            "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-tts-preview:generateContent?key=" + k,
            data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
        d = json.load(urllib.request.urlopen(req, timeout=300))
        c = d["candidates"][0]
        if "content" not in c:
            print(f"intento {i}: vacio, finishReason={c.get('finishReason')}", flush=True)
            time.sleep(120); continue
        pcm, rate = b"", 24000
        for p in c["content"]["parts"]:
            inl = p.get("inlineData") or p.get("inline_data")
            if inl:
                pcm += base64.b64decode(inl["data"])
                mt = inl.get("mimeType", inl.get("mime_type", ""))
                if "rate=" in mt:
                    rate = int(mt.split("rate=")[1].split(";")[0])
        if not pcm:
            print(f"intento {i}: sin pcm", flush=True); time.sleep(120); continue
        with wave.open(out, "wb") as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(rate); w.writeframes(pcm)
        print(f"LISTO intento {i}: {round(len(pcm)/2/rate,1)}s", flush=True); break
    except urllib.error.HTTPError as e:
        print(f"intento {i}: HTTP {e.code}", flush=True); time.sleep(120)
