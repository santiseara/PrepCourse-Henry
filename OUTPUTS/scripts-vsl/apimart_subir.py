"""Sube fotos y voces al almacenamiento propio de ApiMart (el mismo proveedor que despues las procesa)
y deja la URL cargada en subidas.json, que es de donde lee comun.subir() de la skill.
Asi no hace falta KIE_API_KEY ni ningun hosting publico de terceros.
Uso: python3 ../subir.py img/foto.png voces/mujer.mp3 ...   (desde la carpeta del proyecto)"""
import json, os, subprocess, sys, time

KEY = os.environ["APIMART_API_KEY"]
C = os.path.join(os.getcwd(), "subidas.json")
cache = json.load(open(C)) if os.path.exists(C) else {}
TIPO = {".png": "images", ".jpg": "images", ".jpeg": "images", ".webp": "images",
        ".mp3": "audios", ".wav": "audios", ".m4a": "audios",
        ".mp4": "videos", ".mov": "videos", ".webm": "videos"}

for rel in sys.argv[1:]:
    e = cache.get(rel)
    if isinstance(e, dict) and time.time() - e["t"] < 2 * 86400:
        print("ya estaba", rel); continue
    p = os.path.join(os.getcwd(), rel)
    tipo = TIPO[os.path.splitext(p)[1].lower()]
    r = subprocess.run(["curl", "-sS", "--max-time", "300", "-X", "POST",
                        f"https://api.apimart.ai/v1/uploads/{tipo}?retention_days=3",
                        "-H", f"Authorization: Bearer {KEY}", "-F", f"file=@{p}"],
                       capture_output=True, text=True)
    try:
        u = json.loads(r.stdout)["url"]
    except Exception:
        print("ERROR", rel, r.stdout[:300]); continue
    cache[rel] = {"u": u, "t": time.time()}
    print("OK", rel)
json.dump(cache, open(C, "w"), indent=1)
