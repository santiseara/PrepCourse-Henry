# -*- coding: utf-8 -*-
"""Ventanas limpias del pool de Color Exacto (Argentina, 2026-11-15).

36 clips revisados con hoja de contactos (6 cuadros por clip) de los tags #balayage,
#coloracioncapilar, #mechascabello y #babylights. El nicho de color es MUCHO mas limpio que
el de cerrajeria: la mayoria son planos de espalda, manos y pelo, sin cara y sin subtitulo.

Lo que se cayo (16): chicos bailando en el salon, creadoras hablando a camara (el formato
"mi cambio de look"), clips con subtitulo quemado de punta a punta en espanol o portugues
("Tu senal para pintarte el cabello de color cafe", "Every transformation starts...",
"Cardado al 15%"), dos con bandas negras y uno con emoji quemado todo el clip.

Lo que SI se deja es el texto de OBJETO, que ademas aca juega a favor: el clip 43329 muestra
los tubos "8.46 + 8.60" y la palabra CHOCO AVELLANA, que es exactamente la fórmula de la que
habla el guion. Va con zoom para sacarle la marca de agua de arriba.

VENT[clave] = (id del archivo, inicio, fin, extras)
"""
VENT = {
    'a': ('7691053116682243329', 5.4, 9.0,  dict(fam='43329', zoom=1.22, ybias=1.0, noflip=True)),  # tubos 8.46 + 8.60: la formula escrita
    'b': ('7695893084374043935', 5.6, 8.8,  dict(fam='43935', noflip=True)),                        # bowl, tinte y guantes: la mezcla
    'c': ('7675431875535572255', 2.0, 17.5, dict(fam='72255')),                        # rojo cereza, manos, sin texto
    'd': ('7696209031576210710', 0.0, 0.0,  dict(fam='10710')),                        # FUERA: "Autumn hair loading" + cara
    'e': ('7691044487925189906', 0.0, 0.0,  dict(fam='89906')),                        # FUERA: emoji quemado todo el clip
    'f': ('7560008333684411659', 4.5, 13.3, dict(fam='11659')),                        # castano chocolate (texto hasta 4 s)
    'g': ('7644922489319001351', 3.0, 15.5, dict(fam='01351')),                        # chocolate con caramelo, ondas
    'h': ('7644707030128807175', 2.0, 13.4, dict(fam='07175')),                        # balayage caramelo, peinado final
    'i': ('7662404401142729991', 0.0, 17.9, dict(fam='29991')),                        # rubio balayage peinandose: limpio entero
    'j': ('7644348960487853333', 1.5, 10.7, dict(fam='53333')),                        # balayage rubio, trenza y resultado
    'k': ('7673297511553027336', 0.0, 0.0,  dict(fam='27336')),                        # FUERA: plano general borroso + banner
    'l': ('7695118008695491871', 0.0, 0.0,  dict(fam='91871')),                        # FUERA: bandas negras, color fantasia
    'm': ('7577856184586145031', 2.0, 7.7,  dict(fam='45031')),                        # pelo largo, manos, balayage: limpio
    'n': ('7572101905149627703', 0.0, 0.0,  dict(fam='27703')),                        # FUERA: cara a camara, violeta
    'o': ('7551098630837456184', 2.0, 7.7,  dict(fam='56184')),                        # castano, trenza y brillo (texto hasta 2 s)
    'p': ('7578291226970017031', 2.0, 12.0, dict(fam='17031')),                        # espalda, resultado castano con mechas
    'q': ('7667272265012153621', 0.0, 0.0,  dict(fam='53621')),                        # FUERA: "Pencil Grey / StayMyx" quemado
    'r': ('7522607089353592070', 2.5, 20.4, dict(fam='92070')),                        # mechas amarillas de decoloracion y rubio
    's': ('7613197620617481493', 0.0, 0.0,  dict(fam='81493')),                        # FUERA: subtitulo quemado todo el clip
    't': ('7669188234961833229', 0.0, 0.0,  dict(fam='33229')),                        # FUERA: texto en ingles todo el clip
    'u': ('7695818637994626312', 0.0, 14.3, dict(fam='26312')),                        # rubio perlado y peine: limpio entero
    'v': ('7695552129821412615', 0.0, 0.0,  dict(fam='12615')),                        # FUERA: cara a camara
    'w': ('7667771306754067730', 0.0, 0.0,  dict(fam='67730')),                        # FUERA: creadoras a camara
    'x': ('7697009365923958032', 4.0, 18.8, dict(fam='58032')),                        # decoloracion con mechones y rubio final
    'y': ('7697009365923958032', 0.0, 0.0,  dict(fam='43935b')),                       # (libre)
    'z': ('7698886659051375893', 0.0, 7.6,  dict(fam='75893')),                        # rubio balayage corto: limpio entero
    'A': ('7659901035883842834', 2.5, 18.5, dict(fam='42834')),                        # decoloracion, mechones y rubio
    'B': ('7655809788747582753', 0.0, 0.0,  dict(fam='82753')),                        # FUERA: bandas negras
    'C': ('7703648240264088853', 4.0, 14.3, dict(fam='88853')),                        # castano a rubio, resultado peinado
    'D': ('7671656192250285343', 0.0, 13.2, dict(fam='85343')),                        # COBRE sobre rubio, ondas: limpio entero
    'E': ('7667771306754067730', 0.0, 0.0,  dict(fam='x')),                            # (libre)
    'F': ('7447292176809168134', 0.0, 10.8, dict(fam='68134')),                        # pelo largo y balayage ondulado: limpio
    'G': ('7423911478949924101', 3.0, 14.8, dict(fam='24101')),                        # salon, mechas en pelo largo
}
VENT = {k: v for k, v in VENT.items() if v[2] > v[1]}
