# -*- coding: utf-8 -*-
"""Arma los 6 plan.json de The Ceramic Glaze Recipe Bible (ingles) a partir de vent.py."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vent import VENT

VENTANA = 3.4
clips = {k: dict(src=f"../tiktoks/{v[0]}.mp4", **v[3]) for k, v in VENT.items()}
pool = []
for k, (vid, ini, fin, ex) in VENT.items():
    t = ini
    while t + 2.6 <= fin:
        pool.append([k, round(t, 2), round(min(t + VENTANA, fin), 2)])
        t += VENTANA

BOTON = {"type": "button", "text": "TAP LEARN MORE", "size": 58, "y": 1530}
TAG200 = {"type": "tag", "text": "200 RECIPES · 5 BONUS MANUALS", "y": 230, "dur": 2.6}
V = {
 1: dict(seed=101, hook="WHAT'S IN THE JAR?", hook_until="water",
         anchors=[["jar", 0, "m"], ["sieve", 0, "g"], ["safe", 0, "h"]],
         overlays=[{"type": "chip", "word": "shipping", "occ": 0, "text": "YOU PAY FOR WATER", "dur": 2.2},
                   dict(TAG200, word="hundred", occ=0), dict(BOTON, word="Tap", occ=0)], last="j"),
 2: dict(seed=202, hook="IT CAME OUT GREY", hook_until="grey",
         anchors=[["kiln", 0, "p"], ["blue", 1, "j"], ["test", 0, "a"]],
         overlays=[{"type": "chip", "word": "half", "occ": 0, "text": "HALF A RECIPE", "dur": 2.2},
                   {"type": "tag", "word": "hundred", "occ": 0, "text": "CONE · ATMOSPHERE · FOOD SAFE", "y": 230, "dur": 2.6},
                   dict(BOTON, word="tap", occ=0)], last="n"),
 3: dict(seed=303, hook="SAME THREE COLORS", hook_until="creativity",
         anchors=[["shelf", 0, "c"], ["mix", 0, "e"], ["layering", 0, "f"]],
         overlays=[{"type": "chip", "word": "cupboard", "occ": 0, "text": "ANOTHER JAR IN THE CUPBOARD", "dur": 2.2},
                   dict(TAG200, word="hundred", occ=0), dict(BOTON, word="Tap", occ=0)], last="q"),
 4: dict(seed=404, hook="STILL IN THE CUPBOARD", hook_until="laziness",
         anchors=[["oxide", 0, "m"], ["test", 0, "a"], ["fire", 1, "p"]],
         overlays=[{"type": "chip", "word": "scary", "occ": 0, "text": "TESTING BLIND IS SCARY", "dur": 2.2},
                   dict(TAG200, word="hundred", occ=0), dict(BOTON, word="Tap", occ=0)], last="f"),
 5: dict(seed=505, hook="IS IT FOOD SAFE?", hook_until="honestly",
         anchors=[["mug", 0, "i"], ["table", 0, "d"], ["firing", 0, "p"]],
         overlays=[{"type": "chip", "word": "forget", "occ": 0, "text": "THE RECIPE NEVER SAYS", "dur": 2.2},
                   dict(TAG200, word="hundred", occ=0), dict(BOTON, word="Tap", occ=0)], last="j"),
 6: dict(seed=606, hook="NOTHING LEFT AT THE END", hook_until="left",
         anchors=[["jars", 0, "m"], ["powders", 0, "g"], ["color", 2, "e"]],
         overlays=[{"type": "chip", "word": "jar", 'occ': 1, "text": "EVERY COLOR, ANOTHER JAR", "dur": 2.2},
                   dict(TAG200, word="hundred", occ=0), dict(BOTON, word="tap", occ=0)], last="n"),
}
for n, cfg in V.items():
    anchors = [[w, o, k, next(s[1] for s in pool if s[0] == k)] for w, o, k in cfg["anchors"] if any(s[0] == k for s in pool)]
    plan = {
        "vo": f"../vo/V{n}.wav", "script": f"V{n}.txt", "lang": "en",
        "speed": 1.20, "silence": [0.26, 0.12], "cut": [1.9, 2.4, 2.9],
        "words": 2, "hi": "&H009D6BFF&", "hibox": "&H00000000&", "hibord": 8,
        "capy": 1430, "seed": cfg["seed"], "usage": "usage.json",
        "music": "music/bed_activo.wav", "music_db": -9,
        "hook": cfg["hook"], "hook_until": cfg["hook_until"],
        "clips": clips, "pool": pool, "anchors": anchors,
        "last": cfg["last"], "overlays": cfg["overlays"],
    }
    json.dump(plan, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"V{n}.json"), "w"), ensure_ascii=False, indent=1)
    print(f"V{n}.json | ventanas {len(pool)} | anchors {len(anchors)}")
