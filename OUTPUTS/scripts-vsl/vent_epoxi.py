# -*- coding: utf-8 -*-
"""Ventanas limpias de los clips de TikTok del pool de Pisos Epoxi (2026-11-10).

Revisadas con hoja de contactos a 1 cuadro cada 1,5 s + cuadro grande de la mitad inferior.
Se cayeron: los de subtitulo quemado (26935 @epoxyfreaks, 80140 ResinaWorld, 64690, 53076,
39156, 79984, 81940, 04020, 66599, 29414, 79432), los de marca de agua centrada o en esquina
(06258 JPierre Art), el que promociona OTRO infoproducto de pisos en pantalla (13702: "Puedes aprender
con nuestro Libro digital" + la tapa de una guia de porcelanato liquido, lo atrapo la hoja del render),
los que llevan cartel del creador en medio del clip (84774 "Si te interesa saber mas acerca de resina
#  epoxica SEGUINOS" y "el piso debe de estar limpio", 16038 "Limpiamos bien la superficie"), el de marca
#  de agua centrada que el zoom no alcanza (34037 Interiors in Motion), la captura con UI de carrusel (86094) y la cuenta de renders de IA
(83954, 32853, 42701, 00744, 24916, 32309), que no son trabajo real.

VENT[clave] = (nombre del archivo sin .mp4, inicio, fin, extras del clip)
"""
VENT = {
    # --- limpios de punta a punta ---
    'a': ('7236380073614429486', 0.0, 13.5, dict(fam='miamiepoxypro')),      # marmol blanco terminado
    'b': ('7254692320103337262', 0.0, 30.0, dict(fam='theepoxypros')),       # vertido negro sobre blanco
    'c': ('7309521805998378283', 0.0, 25.0, dict(fam='theepoxypros')),       # desbaste, maquina, concreto
    'd': ('7319543741189082373', 0.0, 32.0, dict(fam='jesusortperz')),       # rasqueta gris sobre concreto
    'e': ('7372388803509538094', 0.0, 7.5, dict(fam='kalkreatess')),         # oceano 3D azul
    'f': ('7382701697358974213', 0.0, 18.0, dict(fam='mostudio')),           # flake gris con rasqueta
    'g': ('7446159050632449322', 6.0, 30.0, dict(fam='glossygrounds')),      # hexagonos, negro y blanco
    'h': ('7453180852730613035', 0.0, 20.0, dict(fam='housinginfo')),        # marmol negro (a los 21 s entra un cartel BEFORE)
    'i': ('7463651418583436587', 0.0, 20.0, dict(fam='epoxy239')),           # operario (a los 21 s se le lee EPOXY LIKE A PRO en la espalda)
    'j': ('7476461685880982827', 0.0, 21.0, dict(fam='novaconcrete')),       # rasqueta gris, taller
    'k': ('7516507097886936342', 0.0, 19.0, dict(fam='pureresin')),          # rodillo negro sobre cobre
    'l': ('7522634326903737630', 0.0, 6.5, dict(fam='chasesly')),            # garage de autos de lujo
    'm': ('7524501604293348638', 0.0, 26.0, dict(fam='texasresin')),         # rasqueta azul y blanco
    'n': ('7562243133396749590', 0.0, 30.0, dict(fam='royalresin')),         # obra, piso perlado
    'o': ('7573734410961308959', 0.0, 11.5, dict(fam='odditymall')),         # rodajas de madera y piedras
    'p': ('7576901323870850325', 0.0, 13.5, dict(fam='wholesale')),          # flake con rasqueta
    'q': ('7585415391309090061', 0.0, 29.0, dict(fam='originalcozy')),       # obra grande, piso de rio
    'r': ('7609537062785600799', 0.0, 17.5, dict(fam='resinempire')),        # metalizado con rodillo de espigas
    's': ('7613598095422623006', 0.0, 12.5, dict(fam='gelatvvde')),          # llana sobre flake + local
    't': ('7615755477317602591', 0.0, 8.5, dict(fam='freshepoxy')),          # violeta neon con hexagonos
    'u': ('7627187298035076374', 0.0, 13.5, dict(fam='royalresin')),         # metalizado perlado en casa
    'v': ('7638896421130800415', 0.0, 24.0, dict(fam='jindoupaint')),        # vertido dorado, mano
    'w': ('7658971492469755156', 0.0, 12.5, dict(fam='resinworkss')),        # negro y blanco con luces hex
    'x': ('7662794728483638549', 0.0, 13.5, dict(fam='resinworkss')),        # perlado blanco, local
    'y': ('7696202366634315021', 0.0, 15.5, dict(fam='legendary')),          # cobre y ambar
    'z': ('7698269468174126350', 0.0, 12.5, dict(fam='user2947')),           # llana con granito sobre baldosa
    # --- parciales: la ventana arranca despues del cartel del creador ---
    'A': ('7424844754111761697', 7.0, 16.0, dict(fam='dualspec')),           # varios pisos (arranca en negro hasta 7 s)
    'E': ('7421200090829704454', 5.0, 19.0, dict(fam='promaster')),          # departamento, resina blanca
    'G': ('7663288347565051154', 8.0, 25.0, dict(fam='raptorresin')),        # vertido dorado y hexagonos
    'H': ('7685303020552310024', 0.0, 22.0, dict(fam='umbrella', zoom=1.30, ybias=1.0)),   # logo arriba: se recorta
}
