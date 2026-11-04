import base64, json, os, sys, urllib.request
KEY = os.environ["GEMINI_API_KEY"]
MODEL = os.environ.get("IMG_MODEL", "gemini-3.1-flash-image")
AR = os.environ.get("IMG_AR", "9:16")
def gen(prompt, out):
    body = {"contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"responseModalities": ["IMAGE"],
                                 "imageConfig": {"aspectRatio": AR}}}
    req = urllib.request.Request(
        f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={KEY}",
        data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        d = json.load(r)
    for p in d["candidates"][0]["content"]["parts"]:
        inl = p.get("inlineData") or p.get("inline_data")
        if inl:
            open(out, "wb").write(base64.b64decode(inl["data"]))
            print("OK", out); return
    raise SystemExit("sin imagen: " + json.dumps(d)[:600])
if __name__ == "__main__":
    gen(open(sys.argv[1]).read().strip(), sys.argv[2])
