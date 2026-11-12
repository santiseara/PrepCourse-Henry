# -*- coding: utf-8 -*-
"""Placas de los VSL de pospago: pocas y solo en los puntos que deciden la venta.

El anclaje se saca de la transcripcion real (words_<V>.json), no del guion: Whisper
escribe "$97" donde la voz dice "ninety seven dollars", asi que una frase copiada del
guion no se encuentra nunca. Formato de cada placa: [frase, texto, efecto, segundos].
El efecto va SIEMPRE vacio: cero SFX (Manual de Edicion IA, regla de oro 1).

Uso: python3 gen_vsl_heads.py <V1|V2|V3|V4> <carpeta_trabajo>
"""
import json, os, re, sys

PLACAS = {           # (regex sobre la transcripcion, texto de la placa, segundos)
    'V1': [(r'\$\s?97',  '$97 · ONE PAYMENT',  4.0), (r'30\s*-?\s*day\s+guarantee', '30-DAY GUARANTEE', 3.5)],
    'V2': [(r'\$\s?37',  '$37 · ONE PAYMENT',  4.0), (r'30\s*-?\s*day\s+guarantee', '30-DAY GUARANTEE', 3.5)],
    'V3': [(r'\$\s?27',  '$27 · ONE PAYMENT',  4.0)],
    'V4': [(r'\$\s?17',  '$17 · ONE PAYMENT',  4.0), (r'30\s*-?\s*day\s+guarantee', '30-DAY GUARANTEE', 3.5)],
}


def main():
    v, wd = sys.argv[1], sys.argv[2]
    # misma regla que gen_vsl_plans: si el editor ya transcribio, manda SU lista
    del_editor = os.path.join(wd, f'edit_{v}', 'words0.json')
    fuente = del_editor if os.path.exists(del_editor) else os.path.join(wd, f'words_{v}.json')
    W = json.load(open(fuente))
    pal = [w['w'] for w in W]
    # Whisper deja la puntuacion pegada ("$27," / "guarantee."): para buscar se limpia,
    # pero el anclaje se arma con la palabra TAL CUAL, que es lo que find() compara
    limpio = [re.sub(r'^[^\w$]+|[^\w]+$', '', w) for w in pal]
    heads = []
    for rx, texto, dur in PLACAS.get(v, []):
        hallado = None
        for i in range(len(pal)):
            # se prueban ventanas de 1 a 3 palabras, por si Whisper partio "30 -day"
            for n in (1, 2, 3):
                if i + n > len(pal):
                    break
                if re.fullmatch(rx, ' '.join(limpio[i:i + n]), re.I):
                    hallado = (i, n); break
            if hallado:
                break
        if not hallado:
            print(f'  OJO: no encontre "{texto}" en {v}, la placa no va')
            continue
        i, n = hallado
        # el anclaje son las palabras EXACTAS de la transcripcion, asi find() las ubica
        frase = ' '.join(pal[i:i + max(n, 2)])
        heads.append([frase, texto, '', dur])
        print(f'  {texto}  ->  "{frase}"  en {W[i]["s"]:.1f}s')
    json.dump(heads, open(os.path.join(wd, f'heads_{v}.json'), 'w'), indent=1)
    print(f'{v}: {len(heads)} placas')


if __name__ == '__main__':
    main()
