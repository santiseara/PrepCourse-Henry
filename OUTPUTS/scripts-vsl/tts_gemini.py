import base64, json, os, sys, urllib.request, wave

KEY = os.environ["GEMINI_API_KEY"]
MODEL = os.environ.get("TTS_MODEL", "gemini-3.8-flash-tts")
VOICE = os.environ.get("TTS_VOICE", "Orus")

def gen(text, out, style=None, temperature=float(os.environ.get("TTS_TEMP", 1.0))):
    # el estilo va pegado adelante del texto y terminando en dos puntos:
    # systemInstruction da 400 "Developer instruction is not enabled for this model" (11/11/2026),
    # y el 3.8-flash-tts lee en voz alta cualquier estilo que no termine en dos puntos
    prompt = (style.rstrip() + "\n\n" + text) if style else text
    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseModalities": ["AUDIO"],
            "temperature": temperature,
            "speechConfig": {
                "voiceConfig": {"prebuiltVoiceConfig": {"voiceName": VOICE}}
            },
        },
    }
    req = urllib.request.Request(
        f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={KEY}",
        data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            d = json.load(r)
    except urllib.error.HTTPError as e:
        msg = e.read().decode("utf-8", "replace")
        sys.stderr.write(f"HTTP {e.code}: {msg[:500]}\n")
        # 2 = cuota del DIA agotada (reintentar no sirve) · 3 = cuota por minuto · 4 = otro error
        if e.code == 429:
            raise SystemExit(2 if "per day" in msg else 3)
        raise SystemExit(4)
    parts = d["candidates"][0]["content"]["parts"]
    pcm = b""
    rate = 24000
    for p in parts:
        inl = p.get("inlineData") or p.get("inline_data")
        if not inl:
            continue
        raw = base64.b64decode(inl["data"])
        mt = inl.get("mimeType", inl.get("mime_type", ""))
        if raw[:4] == b"RIFF":
            # los modelos 3.8 devuelven un WAV entero: sacarle la cabecera,
            # si no el RIFF se escribe como audio y queda un clic al inicio
            import io
            with wave.open(io.BytesIO(raw), "rb") as rw:
                rate = rw.getframerate()
                pcm += rw.readframes(rw.getnframes())
        else:
            pcm += raw
            if "rate=" in mt:
                rate = int(mt.split("rate=")[1].split(";")[0])
    if not pcm:
        raise SystemExit("sin audio: " + json.dumps(d)[:800])
    with wave.open(out, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(rate)
        w.writeframes(pcm)
    print(out, round(len(pcm)/2/rate, 2), "s")

if __name__ == "__main__":
    txt_path, out_path = sys.argv[1], sys.argv[2]
    style_path = sys.argv[3] if len(sys.argv) > 3 else None
    style = open(style_path).read() if style_path else None
    gen(open(txt_path).read().strip(), out_path, style)
