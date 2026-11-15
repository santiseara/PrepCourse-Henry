# -*- coding: utf-8 -*-
"""Arma los 6 plan.json de Color Exacto (Argentina) a partir de vent.py.
Uso: python3 planes.py"""
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

BOTON = {"type": "button", "text": "TOCÁ MÁS INFORMACIÓN", "size": 58, "y": 1530}
V = {
 1: dict(seed=11, hook="¿QUEDÓ NARANJA?", hook_until="mano",
         anchors=[["naranja", 0, "D"], ["pomo", 0, "a"], ["escrita", 0, "b"]],
         overlays=[{"type": "chip", "word": "mano", "occ": 0, "text": "NO FUE TU MANO", "dur": 2.0},
                   {"type": "tag", "word": "Cien", "occ": 0, "text": "100 FÓRMULAS · 40 CLASES", "y": 230, "dur": 2.4},
                   dict(BOTON, word="Tocá", occ=0)], last="F"),
 2: dict(seed=23, hook="¿RUBIO AMARILLO?", hook_until="matizador",
         anchors=[["amarillo", 0, "r"], ["mezclar", 0, "b"], ["ceniza", 0, "u"]],
         overlays=[{"type": "chip", "word": "vuelve", "occ": 0, "text": "VUELVE A LOS 3 LAVADOS", "dur": 2.0},
                   {"type": "tag", "word": "Cien", "occ": 0, "text": "FÓRMULA ESCRITA PARA CADA RUBIO", "y": 230, "dur": 2.4},
                   dict(BOTON, word="link", occ=0, text="LINK ABAJO 👇")], last="z"),
 3: dict(seed=37, hook="10 ALTURAS DE TONO", hook_until="ojo",
         anchors=[["carta", 0, "a"], ["raíz", 0, "G"], ["oxidante", 0, "b"]],
         overlays=[{"type": "tag", "word": "quince", "occ": 0, "text": "15 MÓDULOS · 40 CLASES", "y": 230, "dur": 2.4},
                   {"type": "chip", "word": "ojo", "occ": 0, "text": "SE ACABÓ EL TEÑIR A OJO", "dur": 2.0},
                   dict(BOTON, word="Tocá", occ=0)], last="u"),
 4: dict(seed=41, hook="¿MIEDO AL COLOR?", hook_until="frena",
         anchors=[["canas", 0, "p"], ["mechas", 0, "r"], ["balayage", 0, "j"]],
         overlays=[{"type": "chip", "word": "frena", "occ": 0, "text": "NO ES FALTA DE MANO", "dur": 2.0},
                   {"type": "tag", "word": "Cuarenta", "occ": 0, "text": "DESDE CERO + CERTIFICADO", "y": 230, "dur": 2.4},
                   dict(BOTON, word="Tocá", occ=0)], last="i"),
 5: dict(seed=53, hook="LO QUE MÁS TE PIDEN", hook_until="pedir",
         anchors=[["cobres", 0, "D"], ["canas", 0, "C"], ["reflejo", 0, "x"]],
         overlays=[{"type": "tag", "word": "Cien", "occ": 0, "text": "100 FÓRMULAS · CASO POR CASO", "y": 230, "dur": 2.4},
                   {"type": "chip", "word": "paga", "occ": 0, "text": "Y SE VA A OTRO SALÓN", "dur": 2.0},
                   dict(BOTON, word="Tocá", occ=0)], last="u"),
 6: dict(seed=67, hook="¿SE TE APAGA EL COBRE?", hook_until="suerte",
         anchors=[["cobre", 0, "D"], ["oxidante", 0, "b"], ["carta", 0, "a"]],
         overlays=[{"type": "chip", "word": "suerte", "occ": 0, "text": "NO ES MALA SUERTE", "dur": 2.0},
                   {"type": "tag", "word": "Cien", "occ": 0, "text": "TINTE · OXIDANTE · MINUTOS", "y": 230, "dur": 2.4},
                   dict(BOTON, word="Tocá", occ=0)], last="c"),
}
for n, cfg in V.items():
    anchors = [[w, o, k, next(s[1] for s in pool if s[0] == k)] for w, o, k in cfg["anchors"] if any(s[0] == k for s in pool)]
    plan = {
        "vo": f"../vo/V{n}.wav", "script": f"V{n}.txt", "lang": "es",
        "speed": 1.30, "silence": [0.26, 0.12], "cut": [1.9, 2.4, 2.9],
        "words": 2, "hi": "&H0018C5F5&", "hibox": "&H00000000&", "hibord": 8,
        "capy": 1430, "seed": cfg["seed"], "usage": "usage.json",
        "hook": cfg["hook"], "hook_until": cfg["hook_until"],
        "clips": clips, "pool": pool, "anchors": anchors,
        "last": cfg["last"], "overlays": cfg["overlays"],
    }
    json.dump(plan, open(f"V{n}.json", "w"), ensure_ascii=False, indent=1)
    print(f"V{n}.json | ventanas {len(pool)} | anchors {len(anchors)}")
