#!/usr/bin/env python3
"""
Arma subtitulos.json para el ad del carozo de palta, en el estilo de la casa:
bloques de 3 palabras, blanco con una palabra clave en amarillo, a 63,5 % del alto.

Entrada: /tmp/ts_avatar.txt con lineas "[inicio -> fin] texto"
Salida : ~/Desktop/limpia-dolor/work/c25/subtitulos.json
"""
import json, os, re, sys

W = os.path.expanduser("~/Desktop/limpia-dolor/work")
PAL = 3  # palabras por bloque

# palabras que merecen el amarillo (claves del guion)
CLAVES = {
    "artrosis", "carozo", "palta", "nueve", "días", "noche", "rodilla", "deshincha",
    "dolor", "persina", "antiinflamatoria", "inflamación", "movilidad", "día",
    "levantás", "caerte", "fondo", "quinto", "noveno", "parásito", "intestinal",
    "colágeno", "estudio", "sustancias", "atacan", "parásitos", "raíz", "dolores",
    "fuertes", "crudo", "pacientes", "rallás", "mezclás", "caliente", "receta",
    "cientos", "ibuprofeno", "tramadol", "casa", "terrible", "vasos", "botón",
    "completa", "probalo", "funciona", "tía",
}


def leer(path):
    frases = []
    for ln in open(path, encoding="utf-8"):
        m = re.match(r"\s*\[\s*([\d.]+)\s*->\s*([\d.]+)\s*\]\s*(.+)", ln.strip())
        if m:
            frases.append((float(m.group(1)), float(m.group(2)), m.group(3).strip()))
    return frases


def limpiar(p):
    return re.sub(r"[^\wáéíóúüñ]", "", p.lower())


def bloques(frases):
    out = []
    for t0, t1, txt in frases:
        pals = txt.split()
        if not pals:
            continue
        grupos = [pals[i:i + PAL] for i in range(0, len(pals), PAL)]
        # si el ultimo grupo queda de 1 palabra, lo pego al anterior
        if len(grupos) > 1 and len(grupos[-1]) == 1:
            grupos[-2] += grupos[-1]
            grupos.pop()
        total = sum(len(" ".join(g)) for g in grupos) or 1
        t = t0
        for g in grupos:
            dur = (t1 - t0) * len(" ".join(g)) / total
            texto = " ".join(g)
            clave = ""
            for p in g:
                if limpiar(p) in CLAVES:
                    clave = p
                    break
            out.append({"t0": round(t, 2), "t1": round(t + dur, 2),
                        "texto": texto, "clave": clave})
            t += dur
    return out


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "/tmp/ts_avatar.txt"
    frases = leer(src)
    if not frases:
        print("sin frases en", src)
        sys.exit(1)
    subs = bloques(frases)
    dest = os.path.join(W, "c25/subtitulos.json")
    json.dump(subs, open(dest, "w"), ensure_ascii=False, indent=1)
    print(f"{len(frases)} frases -> {len(subs)} subtitulos   {subs[0]['t0']}s a {subs[-1]['t1']}s")
    print("escrito:", dest)
