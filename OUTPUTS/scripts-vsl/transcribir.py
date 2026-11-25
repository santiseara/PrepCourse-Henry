import base64, json, os, sys, urllib.request

KEY = os.environ["GEMINI_API_KEY"]
MODEL = os.environ.get("ASR_MODEL", "gemini-2.5-flash")
PROMPT = os.environ.get("ASR_PROMPT",
    "Transcribi literalmente la voz en off de este audio, en español. "
    "Devolve SOLO el texto hablado, sin comillas, sin comentarios, sin timestamps. "
    "Si hay texto en pantalla no lo inventes: solo lo que se escucha.")

def tr(path):
    data = base64.b64encode(open(path, "rb").read()).decode()
    mime = "audio/mpeg" if path.endswith(".mp3") else "audio/wav"
    body = {"contents": [{"parts": [
        {"text": PROMPT},
        {"inline_data": {"mime_type": mime, "data": data}},
    ]}], "generationConfig": {"temperature": 0}}
    req = urllib.request.Request(
        f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={KEY}",
        data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            d = json.load(r)
    except urllib.error.HTTPError as e:
        return "ERROR " + str(e.code) + " " + e.read().decode("utf-8", "replace")[:300]
    try:
        return "".join(p.get("text", "") for p in d["candidates"][0]["content"]["parts"]).strip()
    except Exception:
        return "ERROR_PARSE " + json.dumps(d)[:300]

if __name__ == "__main__":
    for p in sys.argv[1:]:
        print("=== " + os.path.basename(p))
        print(tr(p))
        print()
