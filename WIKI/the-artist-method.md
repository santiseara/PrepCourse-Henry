# The Artist Method (dibujo a lápiz desde cero, mercado inglés)

> Oferta de dibujo paso a paso modelada de **Método Artista** (metododibujar.online, Argentina) para correr en inglés en US/CA/AU/UK/NZ. El nombre lo puso Santiago el 25/11/2026. Análisis completo del competidor y del mercado en `OUTPUTS/2026-11-25-analisis-metodo-artista-y-mercado-ingles.md`.

## Ideas clave
- **El original está vivo y escalando.** ~20 ads activos desde el 4/11/2026, con tandas nuevas el 11, 15, 17 y 23/11. Una sola fanpage, una sola landing, un solo producto, sin marca personal.
- **Su ángulo nº1 es el ritual anti-celular:** *"hacé esto antes de dormir en vez de mirar el celular"*. **4 de sus 5 ads de más impresiones** corren ese ángulo. No vende "aprender a dibujar", vende **apagar la cabeza**.
- **En inglés el nicho sigue vacío** (verificado el 25/11, tres semanas después de [[drawing-world]]): solo marcas personales (Kirsty Partridge, Charly Clements), arte digital con Procreate, libros (21 Draw), apps y nichos angostos (Japanese Doodling Class, Draw Fantasy Maps). Nadie corre el ebook low ticket de lápiz desde cero.
- **Y el ángulo de la calma tampoco existe en inglés sobre dibujo.** Los ingleses lo venden como hobby o como skill, nunca como pausa sin pantalla. Ese es el hueco que ataca esta oferta.
- **Lo que sí ya funciona en inglés** y conviene robarle a Pigment & Papier / Japanese Doodling Class: *"never knew where to start"*, *"it was the drawing holding you back, not talent"*, *"the first thing I've made in years that I'm actually proud of"*, *"something that's just yours"*.

## Nuestra oferta
- **The Artist Method.** Mecanismo: **shapes → outline → shadows**, en **8 niveles** que suben de dificultad.
- **220 proyectos paso a paso** (un solo número en todas las piezas; el original dice 200 en los ads y 220 en la landing) + **5 bonos en PDF**.
- **Garantía 30 días** contra los 7 del original.
- Mercado: US/CA/AU/UK/NZ, ABO $10 por conjunto ([[testeo-de-creativos]]).
- ⚠️ **Pendiente: no tiene landing todavía.** Santiago eligió "marca nueva" sin landing en esta tanda. Los videos cierran con placa THE ARTIST METHOD y "Tap Learn more".

## El formato de video (copiado del ganador, no se cambia)
9:16 · 36–48 s · b-roll real de manos dibujando a lápiz a pantalla completa, **ni una foto fija** ([[estilo-de-video-ia]]) · voz en off femenina calma y cercana · cama musical suave continua · subtítulos de 2 palabras en mayúscula con la activa en **ámbar #F0B24B** · caja de hook y chips en **terracota #C0632E** · placa final THE ARTIST METHOD con botón terracota.

## Tanda 1 (2026-11-25): 6 guiones y 6 videos
Guiones en `OUTPUTS/2026-11-25-guiones-the-artist-method.md` (EN + ES voseo completos). Cinco modelados sobre sus ángulos ganadores y uno nuevo sacado del mercado inglés:

1. El ritual de la noche / soltá el celular — *su ángulo nº1*
2. Media hora de pantalla contra diez minutos de lápiz — *contraste del nº1*
3. Diez minutos de paz / el paisaje — *su ángulo nº2*
4. El peor consejo: "practicá todos los días" — *su único ángulo de método*
5. Nunca es tarde (el león) — *sus ángulos nº3 y nº4 fundidos*
6. **Nunca supiste por dónde empezar / lo primero en años de lo que estás orgullosa** — *nuevo, del mercado inglés; el original no lo corre*

## Producción
- **Voz: Sulafat**, estilo de mujer norteamericana **hablando rápido y vivo, a volumen normal** (el de [[fuga-perfecta]] del 24/11 traducido al inglés, con los negativos explícitos: *never breathy, never whispered, never a soft bedtime voice*). V1, V2, V4, V5 y V6 por API con `gemini-3.1-flash-tts-preview`; **V3 por AI Studio desde su Chrome** con el mismo modelo, porque la cuota de API se agotó.
- ⚠️ **La primera tanda salió susurrada** y Santiago la rebotó: *"Porque susurra la voz, que suene normal"*. La causa era mi bloque de Style (*"softly and close to the microphone"*), no la voz. Detalle y regla en [[como-trabajar-con-santiago]].
- ⚠️ **V3 hay que forzarlo**: su texto habla de calma y silencio, y el modelo lee el ánimo del contenido. Sale bien solo con el contraste escrito a propósito (*"the words talk about calm, but SHE IS NOT CALM: full chest voice throughout"*).
- **El speed es por video, no fijo.** `gen_tam_plans.py` mide cada wav y despeja el speed para que el montaje final caiga en **167-188 ppm**, la banda que validó Santiago. En esta tanda dio 0,86 a 1,24. `silence [0.26, 0.12]`, cortes de 2,4 s, subtítulos de 2 palabras.
- **Cama musical:** `music_calma.py` (piano de fieltro + pad, 64 BPM, Am–F–C–G, sin percusión) a **−11 dB**, más baja que el default porque el formato es calmo.
- **Pool:** los mismos **15 clips de TikTok** de manos dibujando de [[academia-del-trazo]] / [[drawing-world]] (ventanas y vetos ya revisados), 101 recortes.
- **Efectos de sonido:** `papel` (la lista de proyectos) y `ding` (la placa final), los dos de `~/SFX/alias` ([[efectos-de-sonido]]). Nada más: el formato es calmo y el original no usa efectos.
- Scripts: `OUTPUTS/scripts-vsl/gen_tam_plans.py` y `edit_tam.py` (copia de `edit_dw.py` con la paleta terracota del ganador y los efectos de la biblioteca de Santiago).
- Carpeta: `~/Desktop/the-artist-method/` con `anuncios/`, `imagenes/` y `landing/`.

## Preguntas abiertas
- **¿Se arma la landing?** Hoy los ads no tienen dónde caer. Hace falta decidir precio (sugerido US$ 19.99 de US$ 97, como [[drawing-world]]), checkout y dominio.
- ¿Los 220 proyectos y los 5 bonos salen del mismo PLR que [[academia-del-trazo]] o hay que armarlos?
- ¿Se corre también una tanda de estáticos? El original tiene uno por ángulo.

## Relacionado
[[drawing-world]] · [[academia-del-trazo]] · [[funnel-hacking]] · [[internacionalizacion]] · [[testeo-de-creativos]] · [[guiones-y-anuncios]] · [[efectos-de-sonido]] · [[seleccion-y-modelado-de-oferta]]

## Fuentes
- Biblioteca de anuncios, fanpage Método Artista 1421486194373583 (20 ads, 9 videos transcriptos el 2026-11-25)
- metododibujar.online
- OUTPUTS/2026-11-25-analisis-metodo-artista-y-mercado-ingles.md
