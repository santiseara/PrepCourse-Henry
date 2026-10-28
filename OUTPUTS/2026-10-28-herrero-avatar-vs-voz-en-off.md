# Herrero de Finde — ¿cuánto avatar usa el competidor? (2026-10-28)

Conteo visual de los **180 videos únicos** de The Weekend Fabricator (page id 964653193405481),
clasificados uno por uno mirando hojas de contacto de `anuncios/work/frames/` y cruzados con las
copias de `anuncios/work/rows.json` (631 copias en total: cuántas veces duplican el mismo video en
distintos conjuntos, que es nuestra señal de ganador).

## El reparto real

| Estilo | Videos | % | Copias | % |
|---|---|---|---|---|
| Voz en off + B-roll + fichas (**lo que hacemos nosotros**) | 122 | 67,8 % | 406 | 64,3 % |
| **Avatar de IA a cámara** | 32 | 17,8 % | **120** | **19,0 %** |
| Podcast de dos herreros | 8 | 4,4 % | 41 | 6,5 % |
| UGC con persona (chicas, tipos con gorra) | 12 | 6,7 % | 39 | 6,2 % |
| Dibujos animados (Buck) | 6 | 3,3 % | 25 | 4,0 % |

**Respuesta corta:** avatar usan, pero no es su formato principal — es el segundo, uno de cada seis.
El principal sigue siendo el nuestro. Tres cosas igual lo vuelven importante:

1. **El video más copiado de todos es avatar.** El 002 tiene **21 copias**, el doble que cualquier
   otro salvo el 003 (20, ese sí B-roll). Del top 10 por copias, 6 son avatar.
2. **Es a donde están migrando.** En los últimos 30 videos de la muestra (150–179, los más nuevos)
   hay **9 con avatar**, el 30 %, contra el 17,8 % del total. Y aparecen **personajes nuevos**: además
   del herrero de camisa oscura con logo, un pelirrojo con delantal de cuero (151, 168, 179) y dos
   mujeres (139, 153).
3. **El avatar les habilita un registro de guion que la voz en off no puede sostener.**
   **24 de 31 guiones de avatar (77 %) arrancan en primera persona** ("yo cotizaba a ojo y perdía
   plata en la mitad de los trabajos"), contra **24 % del resto**. Una confesión necesita una cara que
   se haga cargo; con voz en off anónima queda sin dueño. Es exactamente lo que nos pasó con el V1
   (anécdota, único conjunto con cero ventas).

## El formato exacto que más copian (el 002)

No es un talking head. Es **el avatar recortado, sin fondo, parado en la mitad inferior de la
pantalla, presente todo el video**, mientras atrás va cambiando el B-roll (escuadra sobre el hierro,
amoladora, el plano abierto en el celular, una moto de agua). Subtítulos de **una sola palabra**
abajo del avatar. Mismo esquema en el 040, 046, 051, 056, 062, 079, 140 y 149.

Para nosotros es el formato más barato de todos los que tenemos a mano: el fondo ya lo producimos
(B-roll + fichas), solo se suma la capa del avatar.

## Qué propongo probar

La renovación V22–V27 falló por repetir formato y la V34–V39 cambió la edición pero sigue siendo
voz en off. **El avatar es el cambio de formato más grande que tenemos disponible y es el único que
el competidor valida con plata.**

Tanda de 3 (regla de variables = 3):

| | Guion | Formato |
|---|---|---|
| **A1** | El V7 reescrito en primera persona (el rollo de alambre tubular, confesión del herrero) | Avatar recortado sobre el B-roll de siempre, estética v3 |
| **A2** | "Yo cotizaba a ojo" (su 004, 9 copias) con el precio sugerido y una ficha real | Ídem |
| **A3** | "El cliente me preguntó qué más sabía hacer" (su 011, 9 copias) con el Catálogo para Clientes | Ídem |

**Cómo se produce, con lo que ya tenemos:**
- Avatar de HeyGen creado desde una foto de un herrero argentino de unos 45 (el flujo de foto → avatar
  está documentado en [[atlas-de-cortes]]). **Avatar IV**, 9:16, 1080p.
- **Voz "damian"** (Mis voces de HeyGen, el clon que Santiago aprobó en Calistenia Rusa). Las voces de
  AI Studio no sirven acá porque el lipsync tiene que salir del mismo render.
- Editor: `edit_atlas_avatar.py` ya resuelve el caso "la voz viene del video del avatar" (no se
  recortan silencios, video y audio se aceleran juntos para no romper el lipsync). Hay que hacerle una
  copia con la paleta v3 de Herrero y la capa de recorte del avatar sobre el B-roll.
- **Lo que falta verificar antes:** que HeyGen exporte el avatar con fondo transparente o verde. Si no,
  se recorta con `rembg` cuadro a cuadro (más lento pero sale).
- **Costo:** Avatar IV en vertical salió ~122 créditos por 2 bloques de ~2,5 min en Calistenia. Tres
  videos de 55 s deberían andar en **50–60 créditos**. Hay que mirar el saldo antes.

## Fuentes
- `~/Desktop/herrero-de-finde/anuncios/work/rows.json` y `frames/` (muestra del 2026-10-22)
- Hojas de contacto de los 180 videos, 6 planchas de 30
