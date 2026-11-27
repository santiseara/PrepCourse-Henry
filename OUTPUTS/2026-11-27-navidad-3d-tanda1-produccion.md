# Navidad 3D (AR) — tanda 1 de producción

6 videos de 38,9 a 46,9 s, 9:16, en `~/Desktop/navidad-3d/anuncios/` (`27-11 - 1.mp4` a `- 6.mp4`).

| # | Guion | Largo | Planos |
|---|---|---|---|
| 1 | El aguinaldo lo gasta alguien | 42,8 s | 20 |
| 2 | Treinta piezas de un solo pedido | 40,5 s | 19 |
| 3 | Cobrá antes de imprimir | 39,4 s | 19 |
| 4 | El puesto de la feria | 43,4 s | 20 |
| 5 | Las publicaciones que ya están vendiendo | 38,9 s | 19 |
| 6 | Quinientos pesos de plástico | 46,9 s | 22 |

## Voz

**Sulafat (mujer)**, `gemini-2.5-flash-preview-tts`, estilo de porteña de treintipico grabándose con
el celular (seseo, SH en LL/Y, "no está leyendo: está hablando"). Las 6 verificadas contra el guion:
dicen el texto exacto y ninguna leyó el bloque de estilo. Crudo 176-210 ppm; el montaje apunta a
**200 ppm**, que es como leen los dos ganadores del nicho, así que el `speed` sale de dividir y da
**0,98 a 1,15**.

⚠️ Tres voces se regeneraron de gusto: `revisar_voz.py` (Whisper `small`) marcaba *"imprimices"*,
*"reino"* y *"pagada"*, y las tres salieron **iguales** la segunda vez. Transcriptas con Gemini
dicen el guion palabra por palabra: era el ASR. Regla en [[guiones-y-anuncios]].

## Montaje (clon de Ateliê 3D)

Banner de dos pastillas arriba (roja `#D81C1B` + amarilla `#FDD400`): *+400 ARCHIVOS STL DE
NAVIDAD · PAGO ÚNICO · ACCESO INMEDIATO*, **en y=270 (14 % del alto, debajo de la UI de Reels) y
apagado a los 12 s** por pedido de Santiago del 27/11; el titular baja a y=500 para no pisarse. Titular de dos renglones con el segundo en pastilla roja.
**Pastilla verde para cada cifra de plata**, pastilla con ícono para el beneficio. Subtítulos de 3
palabras con la que suena en amarillo. Barra de progreso abajo. Cierre *ACCESO INMEDIATO / Tocá Más
información* los últimos 4,2 s, medido desde el final.

Música: `atlasaudio-advertising-marketing-617541.mp3` (la pista de Santiago para oficio y taller),
rebalanceada con `cama_acm.py` a 14,6/25,8/31,2/22,1/5,8 % por banda — cruda tenía **36 % abajo de
90 Hz**, que en un parlante de teléfono no existe.

## Pool de visuales

148 TikToks de `#3dprintedchristmas` → **77** pasaron el filtro denso → **56** tras el pase a ojo,
más **22** del pool de impresión 3D de [[the-3d-method]] (máquina y filamento) → 78 → dedupe y tope
de ventana → 72 → **51 tras la pasada densa de 6 cuadros**.

## Lo que se cayó, y por qué (vale para cualquier tanda)

- **Dos ads de competidores enteros**, con su marca y su CTA quemados: uno argentino con placa final
  *"TENDENCIA EN 3D · @tendenciaen3d.ok"*, y otro con *"Escribinos por WhatsApp"* y *"¡Vuelven a
  estar disponibles en nuestra web!"*.
- **Personajes con licencia**: Minnie Mouse, un fondo de Super Mario, Bob Esponja en un pegboard,
  Pikachu en una maceta, un Nazgûl, el Grinch (x3), Snoopy, R2-D2, Rudolph y un elfo de *Elf on the
  Shelf*.
- **Texto quemado del creador** que el OCR de la ventana no vio: *"I 3D Printed The WORST Christmas
  Gift!"*, *"christmas tree fidget toy!!"*, *"Día 3 imprimiendo cositas 3D para Navidad"*,
  *"FILAMENT ~15.5 G"*, *"Want to print it? Comment REINDEER for the STL"*.
- Una **captura del slicer**, un clip de planos negros, un dispensador con calabaza de Halloween.

## Los dos bugs de esta tanda

1. ⛔ **El concat con `-c copy` congela el fondo en la composición.** En el V3 quedaron **17 segundos
   de un mismo plano** y el cierre entró 17 s antes de tiempo. Los cortes sueltos y el `cat.mp4`
   estaban perfectos: el defecto nace al superponer, porque los PTS irregulares del concat hacen que
   el filtro `fps` repita cuadro. Se arregla re-encodeando el concat a **CFR real**
   (`-fps_mode cfr -r 30 -c:v libx264 -preset veryfast -crf 16`), que cuesta segundos.
   Editor nuevo: `scripts-vsl/edit_n3d.py`.
2. 🔢 **Whisper escribe los números como dígitos**, así que una placa anclada en `word='cuarenta'`
   nunca aparece (su transcripción dice "40"). Las anclas van en la palabra vecina que no sea número.

## Cómo se verifica que no hay plano eterno

El detector por hash **no sirve**: si la mano se mueve un poco, los cuadros difieren y pasa. Lo que
lo caza es comparar el **tamaño** de cuadros consecutivos extraídos **por número de cuadro**
(`select='not(mod(n,15))'`, sin seek): un plano quieto da variación menor al 2 %. En los seis el
tramo más quieto quedó en **2,0 a 2,5 s**, que es el largo normal de un plano.

## Scripts nuevos

`scripts-vsl/edit_n3d.py` (el editor con el concat a CFR), `gen_n3d_plans.py`, `ventanas_n3d.py`.
