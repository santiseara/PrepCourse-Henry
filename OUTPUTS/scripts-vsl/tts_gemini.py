import base64, json, os, sys, urllib.request, wave

KEY = os.environ["GEMINI_API_KEY"]
MODEL = os.environ.get("TTS_MODEL", "gemini-3.8-flash-tts")
VOICE = os.environ.get("TTS_VOICE", "Orus")

def gen(text, out, style=None, temperature=1.0):
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
    with urllib.request.urlopen(req, timeout=300) as r:
        d = json.load(r)
    parts = d["candidates"][0]["content"]["parts"]
    pcm = b""
    rate = 24000
    for p in parts:
        inl = p.get("inlineData") or p.get("inline_data")
        if inl:
            pcm += base64.b64decode(inl["data"])
            mt = inl.get("mimeType", inl.get("mime_type", ""))
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
