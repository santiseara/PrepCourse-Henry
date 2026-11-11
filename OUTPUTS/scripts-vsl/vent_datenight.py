# -*- coding: utf-8 -*-
"""Ventanas limpias del pool de Noche de Citas Cristiana (2026-11-10).

Historia del pool, que vale para toda oferta cristiana o de pareja:
  - Los tags en espanol del nicho (#parejascristianas, #matrimoniocristiano, #juegosenpareja,
    #juegosdemesaenpareja, #biblia, #devocionaldiario) estan PODRIDOS: de 74 + 61 clips
    bajados, TODOS traian texto quemado (versiculos sobre paisajes, retos tipo "POV",
    frases del creador). Se descartaron los dos pools enteros.
  - Lo que si rinde son los tags de OBJETO, que no tienen idioma: #juegodecartas, #cardgames,
    #boardgamenight, #cozynight. De ahi salen manos repartiendo cartas en una mesa de madera,
    parejas jugando y la casa a la noche con velas.

Verificadas con cuadros cada 1 s entre el segundo 1 y el 10.
VENT[clave] = (nombre del archivo sin .mp4, inicio, fin, extras)
"""
VENT = {
    # --- manos y cartas sobre la mesa ---
    'c1': ('7619853134319373575', 1.0, 10.0, dict(fam='cartasrosa')),     # cartas rosas, mesa de madera
    'c2': ('7621226417145089312', 1.0, 10.0, dict(fam='mazonegro')),      # abanico de cartas, camisa negra
    'c3': ('7632183197169716513', 1.0, 10.0, dict(fam='mazodorado')),     # mazo ilustrado, fondo rojo
    'c4': ('7653195270758370592', 2.0, 9.0, dict(fam='mazoazul')),        # mazo azul en penumbra
    'c5': ('7654997781920156936', 1.0, 10.0, dict(fam='uno')),            # UNO sobre mesa de madera
    'c6': ('7656575766209006855', 1.0, 10.0, dict(fam='repartir')),       # reparte cartas, dos manos
    'c7': ('7681407747639774497', 1.0, 10.0, dict(fam='floreo')),         # floreo de cartas, primer plano
    # --- pareja jugando ---
    'p1': ('7704457134116850957', 1.0, 10.0, dict(fam='espiral')),        # pareja, juego de papel en espiral
    'p2': ('7704696722877877518', 1.0, 10.0, dict(fam='tablero')),        # pareja, tablero azul
    'p3': ('7690421424762129678', 1.0, 10.0, dict(fam='globos')),         # pareja, juego de globos
    # --- la casa a la noche ---
    'a1': ('7690598213983816982', 1.0, 8.5, dict(fam='chocolate')),       # velas, manta y chocolate caliente
    # --- suplentes (tienen texto chico en escena: entran solo si falta material) ---
    'p4': ('7705576042659859726', 1.0, 9.0, dict(fam='lapiz')),           # pareja escribiendo (hoja en ingles)
    'p5': ('7706342446006947085', 1.0, 10.0, dict(fam='metegol')),        # pareja, metegol con marcador
}
