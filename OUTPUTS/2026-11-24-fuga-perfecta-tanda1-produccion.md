# Fuga Perfecta — la tanda 1 producida (10 creativos)

> 24 de noviembre de 2026 · Argentina · clon de la edición de `casocriminal.shop` y `atwistofdate.co.uk`,
> medida sobre 22 de sus anuncios activos.

## Qué copia cada video

| # | Formato | Ángulo | Público | Dur. | Planos |
|---|---|---|---|---|---|
| 1 | Voz en off | Contra Netflix (el que más corren: 27 de 87) | Pareja | 31,8 s | 16 |
| 2 | Voz en off | **El traidor** — nuestro ángulo exclusivo | Amigos | 26,3 s | 15 |
| 3 | Voz en off · **listicle con placas numeradas** | Las 3 salas, una por una | Grupo | 28,3 s | 15 |
| 4 | Voz en off | Sin pantallas en la sobremesa | Familia | 26,0 s | 15 |
| 5 | Voz en off | Reacción de un tercero (lo probé con amigos) | Amigos | 25,1 s | 14 |
| 6 | Voz en off · **comparación** | Las cuentas contra una sala física | Grupo | 25,3 s | 13 |
| 7 | Voz en off | La objeción (pensé que era una boludez) | Pareja | 25,1 s | 16 |
| 8 | **Sin voz** · POV | Contra Netflix, el vagón | Pareja | 12,0 s | 10 |
| 9 | **Sin voz** · POV | No necesitás tablero | Todos | 10,0 s | 10 |
| 10 | **Sin voz** · POV, caja negra | Una hora sin celular | Familia | 14,0 s | 11 |

Los 7 de voz calcan el **molde largo de A Twist Of Date** (20-35 s, voz de mujer joven entusiasta,
cortes de 1,6 a 1,9 s, subtítulos palabra por palabra, sin placa final). Los 3 sin voz calcan el
**molde corto de Caso Criminal** (7-16 s, música sola, una placa POV arriba fija y el banner de oferta
abajo, jump cuts de 1 a 1,3 s).

## Producción

- **Voz:** Sulafat, `speed 1.20`, estilo de amiga porteña con energía. Los guiones 1 a 4 con
  `gemini-2.5-flash-preview-tts`, los 5 a 7 con `gemini-3.1-flash-tts-preview` (la cuota diaria es por
  modelo). Todas entre **169 y 185 ppm**, o sea limpias: ninguna leyó el bloque de estilo.
- **Música:** los de voz llevan la cama de `music.py` a −11 dB, por debajo de la locución. Los 3 sin voz
  llevan `music_activa.py` (marimba, bajo y palmas a 104 BPM) al frente, que es lo más parecido al pop
  acústico con palmas que corren ellos.
- **Editores nuevos:** `edit_fuga.py` (molde largo) y `edit_fuga_pov.py` (molde corto).
- **Banner de oferta** fijo abajo en los 10, igual que ellos: *HOY 4X1: 3 SALAS COMPLETAS + 7 DESAFÍOS
  EXPRESS / SE DESCARGA, SE IMPRIME Y SE JUEGA ESTA NOCHE*.

## Las visuales

Los 10 salen de **las 8 visuales que pasó Santiago**, convertidas en **16 encuadres y 46 ventanas**: de
cada clip se saca un plano abierto y un plano de detalle (el sello de lacre, la pantalla del cronómetro,
el candado, la lupa). Es el mismo truco de `twist-07`, que son 9 planos distintos del mismo kit.

Dos reencuadres obligados: **v7** (las hojas de los desafíos) va a `zoom 1.55` y **v7z** a `1.95` porque
la IA escribió *"DESAFÃO EXPRESS"* con la tilde rota, y así queda fuera de cuadro.

## ⛔ TikTok no sirvió para esta oferta

Se raspraron **8 tags y 407 ids**, se bajaron **155 clips** y se filtraron uno por uno contra hojas de
contactos: **sirvieron 0**. El nicho en TikTok son caras hablando a cámara, Monopoly, juegos de vasos y
texto quemado en todos los cuadros. Los 4 que pasaron el filtro grueso se cayeron al mirarlos a un cuadro
por segundo. Detalle y la regla que sale de ahí en [[guiones-y-anuncios]] y [[fuga-perfecta]].

**Lo que falta para variar visuales de verdad:** generar b-roll nuevo con IA, del mismo estilo que las 8
que ya hay (familias y amigos alrededor de la mesa, manos abriendo sobres, el grupo festejando al salir).

## Dos cosas que costaron un re-render

1. **El b-roll con texto del producto no se espeja.** El editor da vuelta un plano cuando lo repite; con
   nuestros clips eso escribía *"AÑABAC AL"* por *"LA CABAÑA"* y daba vuelta "ETAPA 5" y el cronómetro.
   Se arregló con `"flip": false` por clip. Se ve recién en la hoja del render.
2. **El texto mal escrito por la IA se arregla reencuadrando, no tirando el clip.**
