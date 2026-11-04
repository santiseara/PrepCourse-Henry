# Manual de Edición IA · Launch Expert Academia

> Pegá este archivo entero en tu segundo cerebro (proyecto de Claude, Obsidian, Notion o el CLAUDE.md de tu carpeta).
> Cuando le pidas a tu IA que genere, monte, corrija o revise un anuncio o una VSL con avatar IA, decile:
> **"Seguí el Manual de Edición IA al pie de la letra."**
> Costos y precios medidos en octubre de 2026. Cambian seguido: verificalos antes de presupuestar.

---

## 0. Instrucción para la IA que lee este archivo

Sos mi editor de creativos con IA. Antes de generar, recortar, empalmar, montar o entregar cualquier anuncio o VSL con avatar IA:
1. Seguí las **Reglas de oro** (sección 1). No son negociables.
2. Elegí la ruta con la **tabla de rutas** (sección 2) y avisame el costo estimado antes de gastar.
3. Hacé **1 clip de prueba** y mostramelo antes del lote.
4. No entregues nada que no haya pasado el **Control final** (sección 11). Si algo no lo verificaste, decímelo.
5. Respetá los **Límites** (sección 12) aunque yo insista.

---

## 1. Reglas de oro (no negociables)

1. **Cero efectos de sonido (SFX)** entre clips, tarjetas o b-rolls. Ni pop, ni whoosh, ni buzzer. Solo música de fondo baja con ducking. (Excepción: si estás doblando un anuncio que ya trae SFX propios, se mantienen los del original.)
2. **Una sola voz fija por video**, elegida según el país del público. Nunca mezclar voces ni dejar que la tonada cambie entre clips.
3. **Los bordes de cada clip salen de alineación forzada contra el guion, nunca de Whisper.** Whisper pone la primera palabra en 0,00 s y estira duraciones: arrastra sílabas sueltas ("te cuento, te cuento").
4. **Las pausas internas se cortan por la energía real del audio**, no por los tiempos de Whisper.
5. **1 clip de prueba antes del lote.** Verificar voz, cara y guion. Recién después, el lote.
6. **Regenerar solo los clips malos**, con la lista exacta. Nunca el lote entero.
7. **Nunca regenerar porque falló la descarga.** Re-bajar con reanudación (`curl -C -`). Regenerar cobra dos veces.
8. **Recortar cada clip al mínimo entre la duración del audio y la del video** (si no, el video se congela al final).
9. **Re-renderizar antes de analizar.** Nunca revisar un MP4 viejo después de un cambio.
10. **Control completo antes de entregar** (sección 11), clip por clip y el video entero.

---

## 2. Qué ruta usar según lo que querés hacer

| Querés… | Ruta recomendada | Por qué |
|---|---|---|
| Avatar que habla a cámara (UGC selfie, experta, presentadora) con voz fija | **wan2.7-r2v por ApiMart** con `reference_voice` | Misma cara (primer cuadro = tu foto), misma voz en todos los clips, guion exacto. ~US$0,06/s |
| Avatar que habla, rápido y barato, aceptando que la voz puede variar un poco | **Omni Flash 1.1 ext por ApiMart** | ~US$0,036/s (US$0,24-0,40 por clip). La voz sale de una descripción y puede cambiar de tonada |
| Diálogo en español con buena boca, pocos clips | **Veo 3.1 Lite** (Higgsfield) | Guion exacto y buen lip sync. ~12 créditos por 8 s |
| B-roll sin diálogo (manos, producto, paisaje, movimiento de cámara) | **Grok Imagine video por ApiMart** | US$0,05-0,11 por toma de 6 s. El más barato |
| B-roll con más calidad o recreado desde un cuadro limpio | **Kling 2.5/2.6** image-to-video | ~US$0,17 por toma. Deforma letras: no lo uses para pantallas con texto |
| Fotos de arranque del avatar y escenas | **GPT Image 2** o **Nano Banana** | Antes/después con la misma cara y el mismo fondo sale muy bien |
| Traducir o doblar un anuncio ganador a otro idioma o tonada, misma edición | **HeyGen Video Translation con SRT propio** | Clona cada voz, hace lip sync y deja la edición idéntica cuadro por cuadro. ~12 créditos/min |
| Limpiar subtítulos o la persona de un tramo de video para reusar el fondo | **wan2.7-videoedit** | Fondo perfecto, ~US$2 cada 10 s. No sirve con documentos ni cápsulas de texto |
| Voz en off + b-roll + subtítulos + placa final | Voz por **ElevenLabs** + b-rolls IA + montaje local | Formato barato y muy rendidor para catálogos/infoproductos |
| VSL larga con presentadora fija | wan2.7-r2v (o Omni) + montaje automático | Ver sección 9 |

**Lo que NO funcionó (no pierdas plata):**
- Kling con audio: pronuncia mal y el lip sync es malo. Úsalo solo para tomas mudas.
- Seedance con audio: cambia palabras e inventa idiomas. Caro (~US$1 por 8 s).
- Veo 3.1 completo: ~32 créditos por clip, demasiado caro para 10+ clips.
- Veo por Kie con fotos de personas: Google suele bloquear la animación.
- Omni completo (no Flash): 4 veces más caro y se come frases.

---

## 3. La voz

- **Se elige por proyecto según el país**: rioplatense (voseo), México, Chile, España, Colombia, etc. Si el público es argentino pero el funnel habla de "tú", respetá el registro del funnel.
- **Una sola fuente fija**: una muestra de referencia, no una descripción repetida en cada prompt (cada clip "reinventa" la voz y cambia la tonada).
- **Cómo hacer la muestra:** generá 1-2 clips con la voz descrita para el país, elegí el que tenga la tonada perfecta, recortá ~9,5 s de audio limpio (máx. 10 s) y subilo a un hosting público. Esa URL va como `reference_voice` en TODOS los clips.
- Antes de producir: prueba de 2-3 clips con la misma muestra, escuchar si la tonada se mantiene, mostrárselo al dueño del proyecto.
- Si igual hay saltos de tono: medir el tono medio (F0) de cada clip y regenerar los que se salen del rango (±8 %).

**Ritmos de habla medidos (para calcular duración):**
| Fuente | Ritmo |
|---|---|
| wan2.7 en español | duración = palabras / 4,1 + 0,6 s (más rápido se come palabras) |
| wan2.7 en idiomas de palabras largas | ~2,6-2,8 palabras/s |
| ElevenLabs en español | ~161 palabras/min |
| HeyGen a speed 1,05 | ~175 palabras/min |
| Voces en inglés rápidas | ~190 palabras/min |

---

## 4. Del guion a los clips (plan)

- **Una frase por clip.** Ads: ~18-20 palabras por clip de 8 s. VSL: hasta ~22 palabras.
- **Cortar solo en coma o punto**, nunca a mitad de frase. Los fragmentos sueltos al inicio o fin se los come el modelo.
- **Nada de clips de menos de 6 palabras**: el modelo inventa para rellenar.
- **Cifras en letras** ("diecinueve", no "19") en el texto que se manda al modelo.
- **Listas con conectores**: no "recetas, compras" sino "recetas fáciles, la lista de compras y…".
- **Palabras raras o marcas difíciles**: probar cómo suenan; si se pronuncian mal, reescribir la frase.
- **Duración del clip**: calculala con la fórmula del ritmo. Si sobra tiempo, el modelo inventa palabras al final; si falta, se come la última.
- Pedir en el prompt: terminar la última palabra y quedarse callada un momento.
- Alternar planos (A/B/C: selfie de escritorio, de pie junto a ventana, plano medio) cada 2-3 clips para dar ritmo.

**Prompt base del clip (adaptar):**
```
One single continuous shot, no jump zooms, no cuts. [Persona] speaks directly to camera in [idioma/país],
natural gestures, [gesto del clip]. No subtitles, no text on screen. Phone NOT visible, first-person selfie POV.
She finishes the last word and stays silent for a moment.
```
- Para fotos de arranque tipo selfie: "phone NOT visible, first-person selfie POV" (si no, aparece el celular en mano).
- Sacar "on a tripod" del prompt: a veces mete un trípode en el borde.
- Si la referencia es 9:16, la foto también tiene que ser 9:16, con la cara en el tercio superior.

---

## 5. El filtro de seguridad (bloqueos que no cobran)

Los modelos de video bloquean frases de **presión de venta**. Los bloqueos no se cobran: probá variantes antes de reintentar a ciegas.

| Bloquea | Pasa |
|---|---|
| "A un precio que no vas a volver a ver" | "Solo en esta página" |
| "Si cerrás esta página no la vas a volver a ver" | "Esta oferta está acá, en esta página" |
| "Página de pago 100 % segura" | (sacarlo del clip, ponerlo como texto en pantalla) |
| "Hoy son X. Pago único." / "Es tuyo por X" | "Lo tenés por X, en un solo pago." / "Son X." |
| "Por un único pago de X" | "Por X, en un solo pago" |
| Botón + "una sola vez" en el mismo clip | "…y te llega junto con lo demás" |
| Comillas internas en el texto del prompt | Sacarlas |

Si un clip falla 4 veces seguidas, cambiá el gesto o el prompt. No insistas igual.

---

## 6. Generación sin tirar plata

1. Clip de prueba → revisar → recién ahí el lote.
2. Guardá el ID de cada tarea apenas la mandás (así, si se corta el script, no la pagás dos veces).
3. Descargas: siempre con reanudación y timeouts. Los CDN cortan.
4. Después del lote: correr los detectores (sección 7) y armar **la lista exacta** de malos. Revisá esa lista antes de regenerar.
5. Regenerar hasta 3-4 vueltas solo los malos. Si alguno sigue mal, reescribir la frase.
6. Verificá que los procesos viejos realmente murieron antes de lanzar otro lote.
7. Antes de una tanda grande en HeyGen: hacé la cuenta de créditos (1080p ≈ 20-45 créditos/min de avatar; 720p ≈ 8/min). Si un render tarda muchísimo, suele ser falta de crédito.

---

## 7. Defectos de los clips IA que hay que buscar SIEMPRE

| Defecto | Cómo se detecta |
|---|---|
| Ignora la foto (pasa hasta ~45 % en Omni): otra mujer, plano abierto, trípode | Correlación del primer cuadro contra la foto de referencia (bueno ≈ 1,0; malo ≈ 0,5; corte en 0,93) |
| Corte o zoom interno dentro del clip | Diferencia entre cuadros mayor a 6 veces la mediana. Si cae en coma/punto, queda como punch-in; si es a mitad de frase, regenerar |
| Subtítulos quemados por el modelo (blanco sobre blanco) | OCR sobre la mitad inferior de 3 cuadros. Detectar bordes NO sirve |
| Sílabas sueltas al inicio o fin | Alineación forzada + transcribir el clip YA recortado, aislado |
| Tartamudeos y repeticiones ("duda, duda") | Whisper **medium** (el small no las oye) |
| Clip mudo o cortado en frases de precio/escasez | Transcripción por clip contra el guion |
| Palabras cambiadas o inventadas | Comparar guion vs. transcripción. Si dos pasadas (temperatura 0 y 0,4) oyen lo mismo, el error es real |
| Voz que cambia de tono | Medir F0 por clip |
| Última palabra cortada en clips cortos | Pasar de 4 s a 6 s |
| Muchas inspiraciones largas (~1 s) | Recorte por energía |

**Falsos positivos de Whisper:** confunde términos técnicos y nombres (siglas, marcas y palabras poco comunes) y alucina "subtítulos de Amara.org" o "suscribite" en los silencios. Revisá a mano antes de "arreglar".

---

## 8. Montaje: cortes limpios

**Bordes del clip:** alineación forzada contra el guion (por ejemplo `torchaudio` MMS_FA, precisión 20 ms). Dejar 0,10 s de aire antes de la primera palabra y 0,16 s después de la última.

**Pausas internas por energía:** calcular la envolvente del audio; es voz lo que supera ~10-20 % del percentil 95. Recortar solo silencios mayores a GAP + 2·KEEP.

| Parámetro | VSL | Ads |
|---|---|---|
| SP (velocidad) | 1,12-1,15 | 1,0-1,15 |
| GAP (silencio mínimo a recortar) | 0,30 s | 0,60 s |
| KEEP (aire que se deja a cada lado) | 0,14 s | 0,20 s |

- Cortar silencios saca ~11-14 % del bruto.
- Repeticiones en el medio del clip: sacar los tiempos de lo que se OYE (alineación forzada con el texto oído) y cargarlas como cortes internos. Si la frase está tartamudeada, regenerar.
- Acelerar voz y video juntos (atempo + setpts), nunca solo uno.
- **Música:** volumen 0,05-0,08 bajo la voz con ducking, sube en la placa final.
- **Audio final:** loudnorm a -14 LUFS.
- **Formato:** 1080x1920 (9:16), 30 fps.

---

## 9. Estilo visual

### Anuncios (UGC con avatar, 30-90 s)
- **Gancho en los primeros 2-3 s**: texto grande + la frase más fuerte.
- **Jump cut** en cada pausa recortada, alternando zoom 1,0 / 1,15-1,3.
- **Subtítulos de 2-3 palabras**, MAYÚSCULAS, fuente pesada (Anton, Poppins Black, Montserrat 900), contorno grueso. Palabra activa o clave en **amarillo**, pop de entrada (72 → 110 → 100 %). Centro de pantalla o a la altura de las manos (62-68 % del alto): tapa el movimiento delator del avatar.
- Stickers y píldoras con emoji a tiempo de palabra (con moderación).
- Pantalla dividida para antes/después.
- Barra de progreso arriba.
- **Botón CTA** que late, con una mano señalando, y placa final con la oferta.
- Sin SFX.

### Voz en off + b-roll (catálogos, infoproductos)
- Cortes anclados a palabras (80 ms antes).
- Push-in / pull-out alternado de ~7 % en cada toma.
- El producto entra con pop en la palabra que lo nombra.
- Destello cálido que tapa el corte a la placa final; la placa entra desenfocada y se enfoca.

### VSL (3-20 min)
- Subtítulos karaoke (palabra activa resaltada), tamaño moderado: si son enormes, cansan.
- Píldoras por palabra clave, listas que crecen ítem por ítem, chats tipo WhatsApp para objeciones.
- **B-roll cada 3-5 s** en los tramos explicativos, full screen ~3 s, pegado al empalme entre clips.
- Punch-in en cada cambio de plano.
- Tarjeta de precio, tarjeta de garantía, botón CTA.
- Captura real del checkout para el tramo de compra.

---

## 10. VSL post-pago (OTO y downsell)

- **Delay del botón en la página = segundo exacto en que se dice el precio en el video final ya editado** (no un número fijo). Medilo después del render.
- Escalera: el OTO1 es el más caro y de ahí baja. Cada OTO con su downsell. El detalle está en el Manual del Embudo Post-Compra.
- En la página: leer el `currentTime` del player cada 500 ms para mostrar el botón, con respaldo por reloj solo si el video nunca arrancó. Probar siempre en incógnito.
- HeyGen: límite de 5.000 **bytes** por render (con tildes, cortá en ~4.300 caracteres). Partí la VSL en la transición a la oferta: la costura queda invisible.
- Si los productos se adaptan a otro país, el producto entregado tiene que contener lo que promete el guion.

---

## 11. Control final (en este orden)

1. Guion por clip (transcripción vs. guion) → cara (primer cuadro) → saltos internos → texto quemado. Regenerar solo los malos.
2. Bordes por alineación forzada → transcribir cada clip recortado aislado con Whisper medium. Arreglar todo lo que aparezca.
3. **Re-renderizar** (el render tiene que abortar si falla el audio).
4. Analizar el MP4: voz dentro de lo recortado, cuadros negros, cuadros congelados, saltos no previstos.
5. Transcribir el MP4 entero contra el guion (Whisper medium). Ojo: el MP4 entero NO ve las sílabas sueltas de los bordes; por eso va el paso 2.
6. Mirar el video completo con auriculares. Ningún script reemplaza escucharlo.
7. Reportar qué se encontró y qué se corrigió. Si algo no se verificó, decirlo.

---

## 12. Doblar o traducir un anuncio ganador

**Regla:** lo que vende es guion + ritmo + identidad, no el idioma. No se toca la estructura ni los ángulos.

1. **Transcrear, no traducir.** Armá un corpus de ~100 frases reales de nativos del mercado (anuncios, reseñas, foros) y una guía del traductor (tratamiento tú/usted/vos/vous, puntuación local, moneda). Escribí el guion lado a lado y validalo con un corrector + traducción de vuelta.
2. **Adaptá el marco local**: moneda, referencias culturales, ejemplos y datos del país. Sacá lo que no existe allá.
3. **Medí la velocidad**: si una línea pasa ~6,3 sílabas/s respecto del tramo original, HeyGen la acelera y se come palabras. Acortala ANTES del primer doblaje (re-doblar cuesta lo mismo).
4. **HeyGen Video Translation** con `srt` + `srtRole: "output"` (dice tu guion palabra por palabra) y `enableDynamicDuration: false` (si no, estira el video en cámara lenta y rompe la edición).
5. **Borrar los subtítulos originales**: OCR en modo preciso (el rápido pierde texto en ~30 % de los cuadros), inpaint por caja; si los subtítulos van en cápsula, repintar la cápsula por dentro. Para fondos con persona, regenerar el fondo limpio con videoedit.
6. **Subtítulos nuevos** con el mismo estilo, fuente y colores del original.
7. QC: Whisper del final vs guion. Si Whisper "pierde" frases por la música, confirmá con la voz sola.

---

## 13. Límites (aunque te lo pidan)

- **No fabricar testimonios** (resultados atribuidos a clientas inventadas). Reemplazá la escena por una demostración.
- **No prensa ni avales falsos**: nada de tapas de medios conocidos, avales de universidades, documentales, estudios inventados ni cifras sin fuente.
- **No marcas registradas ajenas** en el nombre del producto.
- **No prometer resultados médicos** (cifras de resultado en X días, "sin efectos secundarios").
- Evitar ángulos de autopercepción negativa y amenazas: Meta los rechaza.
- Testimonios reales solo con consentimiento.
- Un avatar IA no es una profesional real: no inventarle títulos ni credenciales.

---

## 14. Estructura de carpeta recomendada por proyecto

```
proyecto/
  guion/        guion.md (una línea = un clip; [B: ...] = b-roll)
  img/          fotos de referencia del avatar (planos A/B/C, 9:16)
  voz/          muestra de referencia + URL
  clips/        clips generados
  clips_malos/  los descartados
  broll/
  prod/         plan.json, scripts, config del montaje
  final/        MP4 + LEEME (duración, delay del botón, qué se verificó)
```