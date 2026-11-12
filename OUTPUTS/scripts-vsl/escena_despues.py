"""Genera la escena del DESPUES editando el cuadro del ANTES: misma pieza, mismo encuadre, mismos muebles.
Uso: python3 escena_despues.py <proyecto> <letra_antes> <letra_despues> <personaje_despues> "<que cambia>" """
import os, sys
sys.path.insert(0, os.path.expanduser("~/.claude/skills/mini-novela/scripts"))
import comun as C

P, G = C.proyecto(sys.argv[1])
a, b, pers, cambio = sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
IE, IP = f"{P}/img/escenas", f"{P}/img/personajes"
out = f"{IE}/{b}.png"
if os.path.exists(out): sys.exit("ya existe " + out)
pr = ("Keep reference image 1 exactly as it is: the same room, the same camera angle and framing, the same furniture, the same objects "
      "and the same light. Change only the woman, who is the same person as in reference image 2: " + cambio +
      " She keeps the exact same face, the same hair and the same clothes as in reference image 1. "
      + getattr(G, "CUADRO", "") )
body = {"model": "gemini-nano-banana-2.1-ext", "prompt": pr, "resolution": "2K", "size": "9:16",
        "image_urls": [C.subir(f"{IE}/{a}.png"), C.subir(f"{IP}/{pers}.png")]}
C.imagen(body, out, f"{P}/costos.jsonl")
print("OK", out)
