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

**21 clips base, 32 encuadres, 94 ventanas.** Son las **8 que pasó Santiago** (el producto: sobres con
lacre, cronómetro, candado, las hojas de los desafíos, el sobre del SABOTEADOR) más **12 generados el
mismo día** con el b-roll de gente, que es lo que faltaba:

| clip | qué es | para qué público |
|---|---|---|
| g01 | cuatro amigos discutiendo sobre el mapa | amigos |
| g02 | pareja aburrida en el sofá con el control y la pizza | pareja (el hook contra Netflix) |
| g03 | manos rompiendo el lacre a la luz de velas | todos |
| g04 | grupo festejando, brazos arriba y choque de manos | el cierre |
| g05 | mano escribiendo en una servilleta junto a la copa | todos |
| g06fam | familia sobre la mesa con los sobres | familia |
| g07 | cenital de la mesa: manos, mapa, sobres y café | todos |
| g08 | pareja en el sillón leyendo una hoja | pareja |
| g09 | el pinboard con hilos rojos y los amigos mirando | amigos |
| g10 | dos amigas agarrándose la cabeza | amigos |
| g11 | mano apoyando el celular contra una pila de libros | todos |
| g12 | familia festejando | familia |

**Cada video tiene su propio pool:** el producto siempre, más el b-roll del público de ese ángulo. Por eso
el de familia abre con la familia y el de amigos con los amigos, y ninguno repite el reparto del anterior.

**Generados con `seedance_2_0_mini` en Higgsfield: 8 créditos por clip de 8 s a 720x1280** — el mismo
formato exacto que los 8 del cliente. Doce clips, **96 créditos de los 915** disponibles. El
`seedance_2_5` cuesta 56 por clip, siete veces más, y no hacía falta.

Dos reencuadres obligados en los del cliente: **v7** a `zoom 1.55` y **v7z** a `1.95`, porque la IA
escribió *"DESAFÃO EXPRESS"* con la tilde rota y así queda fuera de cuadro.

## La música

Sale **del audio de sus propios anuncios**, no de un generador:

- **Los 7 con voz** llevan la pista de intriga con cuerdas de `caso-05`, instrumental y sin voz cantada,
  a −10 dB por debajo de la locución.
- **Los 3 sin voz** llevan la de `caso-01`, pop indie con vocal femenina y cambio de energía en el
  segundo 8, al frente. Dura 15,6 s, así que cubre los tres videos sin repetirse ni una vez.

🐞 La Biblioteca sirve el audio en **HE-AAC a 48 kbps**: suena opaco. Se levanta por encima de 4,5 kHz y
se le saca algo de 200-500 Hz (`scripts-vsl/cama2.py`). Para alargar no se busca el período del compás
—estas pistas no cierran en loop y el empalme salta—: se repite entera con crossfade largo de 2 s.

## ⛔ TikTok no sirvió para esta oferta

Se probaron **dos enfoques y 177 clips**: por producto (8 tags de juegos y escape rooms, 155 clips) y por
ambiente (`cozynight`, `winenight`, `candlelight`, `cozyevening`, 22 clips). **Sirvieron 0 y 4
respectivamente**, y los 4 de ambiente eran lámparas y chimeneas sin gente. El nicho en TikTok son caras
hablando a cámara, Monopoly, juegos de vasos y texto quemado en todos los cuadros. Por eso el b-roll de
gente se generó.

## Dos cosas que costaron un re-render

1. **El b-roll con texto del producto no se espeja.** El editor da vuelta un plano cuando lo repite; con
   nuestros clips eso escribía *"AÑABAC AL"* por *"LA CABAÑA"* y daba vuelta "ETAPA 5" y el cronómetro.
   Se arregló con `"flip": false` por clip. Se ve recién en la hoja del render.
2. **El texto mal escrito por la IA se arregla reencuadrando, no tirando el clip.**
