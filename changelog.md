## 2026-10-30 — Piedras: tanda v33, "más, mejores, más potentes"
- Pedido después de la v32: *"Dame mas, mejores, mas potentes"*. Van 3 guiones nuevos (10, 11 y 12).
- Diagnóstico: la v32 ya abría con la promesa, pero la promesa **describía el negocio**. La v33 abre con una **afirmación que choca** y se explica en la línea siguiente.
- Ángulos: cada piedra vendida es un vendedor en la casa de otro · no te pagan por la piedra, te pagan por ocho semanas de aroma · todo el negocio entra en una caja de zapatos.
- Regla nueva anotada en `WIKI/guiones-y-anuncios.md` (registro del 30/10). `WIKI/scented-stones.md` actualizada con la v33 y el banco.
- Entregado en `OUTPUTS/2026-10-30-guiones-piedras-v33-mas-potentes.md`, inglés y español con voseo, copiado al portapapeles en RTF.

## 2026-10-30 — Piedras: tanda v32, tres guiones de promesa fuerte
- Pedido: "vamos con más guiones para piedras". Variable de algo que ya corre, así que van **3** (regla del 24/10).
- Se sigue la línea aprobada de la v31: **promesa concreta en la primera línea**, después el mecanismo del producto, los entregables con nombre y cierre con ventana de tiempo. La plata, como precio de mercado o en primera persona.
- Ángulos nuevos (7, 8 y 9): el pedido de casamiento de 150 piezas como un solo cliente grande, el aroma que se apaga a las seis semanas como reposición que vuelve sola, y la objeción "yo no sé vender" resuelta por el propio producto.
- Entregado en `OUTPUTS/2026-10-30-guiones-piedras-v32-promesa-fuerte.md`, en inglés y español con voseo, y copiado al portapapeles en RTF. `WIKI/scented-stones.md` actualizada con la v32 y el banco restante.

## 2026-10-30 — Skool AI: los 2 de voz en off sin una sola foto
- Santiago: *"no me gusta que tenga los B-rolls de imágenes… sacá todas las imágenes, quiero que todo sea B-roll, todo video. Los que pusiste están muy bien, quiero más de ese estilo"*. Fuera las páginas dibujadas (`ix_18`, `ix_38`), la placa de condiciones y los recortes del libro.
- **El índice pasó a ser una placa de texto encima del clip**: caja blanca con el titular y la pastilla naranja `PAGE NN` pisando la esquina (`png_badge` en `edit_skool_vo.py`). Sin número, sale solo la frase. **El editor ahora corta con error si un plano apunta a un `.png`/`.jpg`.**
- Pool nuevo: **745 links de 7 tags, 70 clips bajados, 10 limpios**. Sirvieron `#bookkeeping`, `#adminwork`, `#invoice` y `#filing`. No sirvieron `#taxseason` (sketches), `#officedesk` (showrooms y desk setups) ni `#shopowner`.
- Se cayeron `excel_033` y `accounting_005`: interfaz y cartel **en español** en un ad para mercado inglés. Regla nueva anotada en `WIKI/guiones-y-anuncios.md`.
- `SK-V5.mp4` (23,5 s, 6 planos) y `SK-V6.mp4` (28,2 s, 7 planos) re-renderizados, 100 % video. Planes en `OUTPUTS/scripts-vsl/gen_skool_vo_plans.py`. Costo cero, Higgsfield intacto (19,35).

## 2026-10-29 — Herrero de Finde: la tanda V43–V48 rehecha sin una sola foto
- Santiago: *"seguís poniendo fotos, tienen que ser todos de tiktok"*. **Regla nueva**: en un ad de voz en off ningún plano es una foto fija (ni fichas, ni hojas del producto, ni grabaciones de pantalla). El visual es 100 % B-roll de TikTok y el producto lo sostienen la voz y las placas de texto. Anotada en `WIKI/guiones-y-anuncios.md` y en `WIKI/herrero-de-finde.md`.
- `anuncios/work/plans/gen8.py` y **`gen9.py`**: pool solo de TikTok, `anchors: []`, sin stills ni demos de pantalla. Cada video pasó de ~6 fotos + 7 clips a **12–14 clips seguidos**.
- **Revisión completa del pool** (hoja de contactos de los 25 clips + `cropdetect`): fuera `V` entero (bandas negras), `T` hasta 36 s (bandas y cara a cámara), `M` hasta 73 s (logo de CapCut), `X` de 4,5 a 45 s (cartel "MESA PA SOLDAR" y "GRACIAS POR VER"), y huecos en `U`, `Z` (cartel "¿Qué dice la tuertita papá?"), `e`, `b` y `d`. Quedan 336 recortes sobre 24 clips.
- Los 6 entregables re-renderizados con los mismos nombres (43,1 · 44,3 · 43,5 · 45,0 · 41,2 · 41,3 s) y verificados frame por frame. Costo cero.

## 2026-10-29 — Skool AI: los 2 de voz en off rehechos con B-roll real de TikTok
- Santiago rechazó las visuales fijas. Se relevaron **1.381 links de 11 tags** y se bajaron 104 clips con tikwm; **7 quedaron limpios** y son los que se usan (`anuncios/work/tiktoks/`).
- Hallazgo: los tags de IA son inservibles (creador hablando a cámara); el material bueno está en los tags del oficio que nombra el guion: `#accountinglife`, `#paperwork`, `#excel`.
- `edit_skool_vo.py` ahora acepta **clips de video además de imágenes** en `pages`, con `ss`, `zoom` e `ybias` por plano.
- `SK-V5.mp4` (23,5 s, 6 planos) y `SK-V6.mp4` (28,2 s, 7 planos) re-renderizados. Costo cero.

## 2026-10-29 — Herrero de Finde: 6 renovaciones de voz en off (V43–V48) con edición v4
- **Seis formatos de hook nuevos**, ninguno repetido de la V34–V42, todos escritos contra el objetivo de la landing (primer millón con la soldadora que ya tenés, armarlo el sábado y venderlo antes de fin de mes): cronología, la cuenta del primer millón, el curso de soldadura incluido, los planos gratis que se cortan en el paso difícil, la proyección del martes cobrado y la garantía invertida. Guiones en `OUTPUTS/2026-10-29-renovaciones-herrero-v43-v48.md`.
- **Fichas nuevas** sacadas del motor del producto (ninguna de las dos tandas anteriores): BQ-009, FM-001, SH-001, ST-005, FN-014 y ST-004.
- **Edición v4, más simple**: `OUTPUTS/scripts-vsl/edit_herrero_v4.py` — apertura sin panel (el hook sobre el video), sin regla de medidas ni destellos, subtítulos sin palabra resaltada, cortes de 3,0 a 4,0 s, zoom suave y dos placas por video. Planes en `anuncios/work/plans/gen7.py`, una sola cama musical para la tanda.
- **Voces Enzo** en AI Studio (Gemini 3.8 Flash TTS, porque Enzo no está en el 3.1), las seis de una sola carga y verificadas por transcripción.
- **Clip `Y` vetado hasta el segundo 8,5** (cartel en inglés "Step by step instructions on how to build a Firepit").

## 2026-10-29 — Skool AI: los 2 ads de voz en off
- **V5 "el índice de la guía"** (23,5 s) y **V6 "dónde está esta guía"** (28,2 s), modelados de los dos formatos de voz en off del ganador. Guiones EN + ES en `OUTPUTS/2026-10-29-guiones-skool-ai-voz-en-off.md`.
- Voces de AI Studio (gratis): **Orus** y **Sulafat**, las dos ya validadas. `speed 1.30`, `silence [0.26, 0.12]`.
- **`gfx_skool_vo.py`**: páginas con el badge naranja "PAGE NN" (la firma del formato índice del ganador) y los planos del libro recortados de las fotos de los avatares por debajo del mentón, sin ninguna cara. Costo cero.
- **`edit_skool_vo.py`**: planos del producto encadenados, cada uno anclado a una palabra del guion, con la misma estética y la cama de Herrero a −8 dB.
- La tanda 1 queda completa: `~/Desktop/skool-ai/anuncios/SK-V1.mp4` … `SK-V6.mp4`.

## 2026-10-29 — Skool AI: los 4 testimonios rehechos con cortes de producto y música
- **Fuera el PIP con otra persona** (corrección de Santiago) y **dos cortes de 2 s a una página de la guía** en su lugar, que es lo que realmente mete el ganador en el medio: páginas internas y chips de herramientas, nunca otra cara.
- **`OUTPUTS/scripts-vsl/gfx_skool.py`**: dibuja las cuatro páginas (la fórmula maestra, la ruta de 7 días, con qué herramientas funciona y los prompts de ejemplo) con la paleta de la tapa. Costo cero, sin tocar los 19 créditos que quedan en Higgsfield.
- **Cama de Herrero a −8 dB** en los cuatro, medida entre −10 y −12 dB por debajo de la voz.
- Dos reglas nuevas en [[guiones-y-anuncios]]: el corte de un testimonio va al producto y nunca a otra persona, y el UGC con avatar tampoco se entrega pelado (dos cortes + música).

## 2026-10-29 — Skool AI: los 4 videos de testimonio producidos
- **4 avatares creados en HeyGen** (Rachel, Frank, Diane y Paul "Skool AI") desde las fotos de Santiago, con las voces ya validadas **Annie - Lifelike** y **Orson - Firm & Measured**. Avatar IV, 1080p vertical, **29 créditos** en total (quedan 326).
- **Velocidad resuelta dentro de HeyGen** con "Un poco más rápido" en el paso de entrega de voz: los cuatro quedaron en **25,4 a 27,6 s** sin tocar el lipsync.
- **Editor nuevo `OUTPUTS/scripts-vsl/edit_skool.py`**, copia de la edición del ganador: hook en caja blanca, subtítulo de una palabra, PIP abajo a la derecha con otro de los personajes y placa final de marca. Sin música ni efectos.
- Videos en `~/Desktop/skool-ai/anuncios/SK-V1.mp4` … `SK-V4.mp4`.
- Dos trampas anotadas en [[skool-ai]]: Chrome bloquea la segunda descarga de HeyGen en la misma pestaña (una pestaña nueva por video) y el CDN de HeyGen es CloudFront firmado, así que `curl` directo no sirve.

## 2026-10-29 — Skool AI: nombre, tanda 1 de testimonios y prompts de avatar
- La oferta se llama **Skool AI** (decisión de Santiago). `WIKI/master-ai-7-dias.md` renombrada a `WIKI/skool-ai.md`.
- **4 guiones de testimonio** (EN + ES con voseo) en `OUTPUTS/2026-10-29-guiones-skool-ai-testimonios.md`: contadora 49, dueño de taller 57, abogada 56 y reinvención a los 52. De 92 a 106 palabras → 24 a 26 s, el rango del ganador.
- **4 prompts de avatar** en `OUTPUTS/2026-10-29-prompts-avatares-skool-ai.md`, en formato selfie con la guía en la mano, como el original. Los arma Santiago y después van a HeyGen.
- Carpeta `~/Desktop/skool-ai/` creada con `imagenes/`, `landing/` y `anuncios/`.
- Voces decididas entre las ya validadas (Annie - Lifelike, Orson - Firm & Measured, voz roma), Avatar IV, ~45 créditos estimados, `speed 1.08` sin recorte de silencios para no romper el lipsync.

## 2026-10-29 — Master AI in 7 Days: análisis del ganador para el mercado inglés
- Relevados los **225 anuncios de más impresiones** de **Udemia.IA** (page id 1187693011097208, ~960 activos): 216 creativos distintos, 8 idiomas, el más viejo del **16/09 = 43 días**, casi todas las landings en ImpulTienda.
- **18 videos bajados y transcriptos** con faster-whisper + hoja de contactos de los 225 thumbnails para clasificar formato.
- Nueva página `WIKI/master-ai-7-dias.md`: los 3 formatos (85% testimonio UGC de 24-26 s, 15% voz en off, y la línea nueva de quiz por profesión), la DNA de cada uno, el patrón **vende tiempo y vigencia, nunca plata**, y el hallazgo de que **el mercado inglés está vacío** (1 solo ad en inglés, apuntado a India).
- Copia del análisis en `OUTPUTS/2026-10-29-analisis-udemia-ia-mercado-ingles.md`. Índice actualizado.

## 2026-10-29 (noche 7) — Brasil: banco de keywords de 4 nichos para cazar

- `OUTPUTS/2026-10-29-keywords-brasil-4-nichos.md`: ~250 keywords en portugués para la Biblioteca de Anuncios, ninguna repetida de los bancos del 26/10 y 27/10.
- **Renda extra, capa 3:** se sale de "faca e venda" y entra a los cuatro mercados que nadie modela — negativado/score, dinero dormido y del Estado (valores a receber, FGTS, BPC), empleo formal (currículo, vagas, concurso) y marketplace sin stock (Shopee, ML, TikTok Shop), más leilão y gig economy.
- **Emagrecimento (nuevo):** la regla es que "emagrecer" no sirve para cazar. Ejes por síntoma (inchaço, compulsão, intestino), por hormona y edad (+40, menopausa, tireoide), por formato (cardápio en PDF, airfryer, sopa de 7 días) y la ola caliente del **mounjaro natural / ozempic caseiro**.
- **Manifestação, capa 2:** los dos sub-mercados que faltaban en el banco del 27/10 — el **católico popular** (Santo Expedito, Santa Edwiges, novena, terço) y el de **señales y símbolos** (horas espelhadas, sueños, numerología del nombre), más objeto/gesto, audio subliminal y calendario.
- **Relacionamentos (nuevo):** cuatro sub-mercados que no se mezclan — reconquista y post-ruptura, pareja casada en crisis, el juego de a dos (el PDF de R$ 10 del nicho) y el masculino de conquista, más el eje cristiano.
- Cada nicho con sus 10 de arranque, su lista de **las que no usar** (las que traen marca personal o high ticket) y el aviso de política de Meta donde corresponde.

## 2026-10-29 (noche 6) — Solar Installer Pro: oferta nueva, 6 ads para el mercado inglés

- Oferta nueva: **Solar Installer Pro** (US$ 47, `solar-installer-pro.impultienda.ar`), curso de instalación solar en 20 días. Ficha completa, el ganador desarmado y la tanda en `WIKI/solar-installer-pro.md`.
- **Ganador modelado:** Mundo en Digital (page id 314381038431811), 4 ads activos, el más viejo **en circulación desde el 24 de agosto: 66 días**. Los 4 videos bajados de la Biblioteca y transcriptos: son **2 cuerpos** y los dos venden **claridad, no plata** (cero montos, cero plazos, prueba social de 3.200 y CTA suave). Mismo patrón anti-bloqueo que [[profesional-digital]], sostenido 66 días.
- **6 guiones** en inglés y español con voseo (`OUTPUTS/2026-10-29-guiones-solar-installer-pro.md`), cada uno con hook, cuerpo y CTA propios y la promesa en la primera línea: el orden que nadie te da · los instaladores son el cuello de botella · te dejan apuntes vs. una cotización · dimensionar es todo el oficio · la otra mitad arranca cuando dicen que sí · del día uno al día veinte.
- **6 videos de 27 a 35 s**, 9:16, en `~/Desktop/solar-installer-pro/anuncios/SIP-V1…V6.mp4`. Nombres para subir: 29/10 - 1 a 29/10 - 6.
- **Voz:** AI Studio (Gemini 3.1 Flash TTS Preview), voz **Orus**, Pace Natural, audio profile de instalador estadounidense de 40. Los seis WAV verificados con Whisper contra su guion.
- **Música:** 🔁 corregida. Iba la cama del propio ganador separada con demucs (`bed_A`) a −11 dB; Santiago la escuchó y pidió **la de Herrero, un poco más arriba** (*"te quedo muy baja, tampoco tan alta"*). Los seis re-renderizados con `bed_herrero.wav` a **−8 dB** (+3 dB) y **exactamente los mismos planos** (`usage.json` reseteado y V1→V6 en orden; verificado contra los `all.txt` de la primera pasada y PSNR mediano de 47 dB, o sea misma imagen).
- 🆕 **Regla nueva en `WIKI/vsl-reglas-de-armado.md`:** la **cama por defecto de los ads de voz en off es la de Herrero (`bed_A`) a `music_db: -8`**. −11 queda muy baja, −6 ya tapa la voz. Y el procedimiento para cambiarle solo la música a una tanda ya aprobada sin que se muevan los planos.
- **B-roll:** 132 TikToks bajados con tikwm de 4 tags de instalación solar; **21 limpios y usados**. Cero stock, cero créditos.
- 🆕 **Regla nueva en `WIKI/vsl-reglas-de-armado.md`:** en AI Studio, después de escribir el guion por JS **el primer clic en Run no dispara** (pasó en 3 de 6). Hay que comparar la duración del player contra la generación anterior antes de bajar, o el Download baja el audio viejo sin avisar.

## 2026-10-29 (noche 5) — Atlas de Cortes: producidos los 3 videos bizop elegidos

- Santiago eligió el **27, 28 y 29**. Listos en `~/Desktop/atlas-cortes/anuncios/`: **AT-V27** (29,9 s), **AT-V28** (26,2 s) y **AT-V29** (29,8 s), 9:16 1080x1920.
- Voces grabadas en AI Studio desde su Chrome (Gemini 3.8 Flash TTS, voz **Sulafat**, página muteada), bajadas y verificadas por duración y MD5: los tres audios distintos (38,6 / 33,6 / 38,6 s crudos).
- Editados con `edit_atlas.py`, `speed 1.30` y `silence [0.26, 0.12]`. Planes nuevos en `material/plans/gen.py` (seeds 270, 280, 290).
- **Revisión con hoja de contactos** a 1 cuadro cada 2 s: limpios, sin texto quemado ajeno ni caras a cámara.
- 🆕 **Dos trampas del editor anotadas en `WIKI/atlas-de-cortes.md`:** un `occ` inexistente descarta la placa en silencio (le pasó al V29, que quedó sin la página del mapa hasta que se corrigió), y un anchor sobre la última frase pierde contra la placa final.
- Nombres para subir: 29/10 - 1, 2 y 3.

## 2026-10-29 (noche 4) — Atlas de Cortes: rechazo de la v19–v24 y tanda bizop v25–v30

- **Rechazo:** *"muy malos, no me generan nada de interés. Te mando mi landing para que la veas y me hagas mejores guiones… acordate que el ángulo que busco es el de bizop"*.
- **Lo que hice mal:** escribí los seis **sin una palabra de plata a propósito**, apoyado en que el dato de la cuenta dice que el bizop rinde la mitad en esta oferta, cuando él ya había pedido bizop el 28/10. **Regla nueva en `WIKI/guiones-y-anuncios.md`:** el ángulo que fija Santiago manda sobre el dato; el dato se dice una vez y se ejecuta igual.
- **Landing nueva leída entera:** `women-s-cutting-atlas.impultienda.ar` (bajada con `curl` y limpiada, porque la herramienta de fetch corta la página y no transcribe literal). Ficha completa en `WIKI/atlas-de-cortes.md`: hero, los 5 dolores y los 5 beneficios con sus títulos, los 7 mapas de muestra, los 5 bonus con nombre y valor, el precio y los 6 testimonios.
- ⭐ **El hook bizop estaba escrito en su propia landing:** "How many cuts are you turning down because you can't remember the right sequence?". Otra regla nueva: antes de escribir una tanda, bajar y leer la landing entera y buscar ahí el hook.
- **Tanda v25–v30** (`OUTPUTS/2026-10-29-guiones-atlas-cortes-v25-v30-bizop.md`), 6 opciones para elegir 3, bizop duro, 106–135 palabras, EN + ES voseo: el mismo sillón con dos precios · tres servicios apagados · una copia para todo el salón (dueñas) · cada arreglo gratis es un turno regalado · el precio de un corte contra un curso con viaje · a tres minutos de acá.
- Recomendados 25, 30 y 27. Falta la elección para producir.

## 2026-10-29 (noche 3) — Atlas de Cortes: 6 guiones (v19 a v24) para elegir 3

- **Pedido:** *"Vamos con 3 videos para pelo. Dame guiones y yo elijo"* → 6 opciones, elige 3.
- `OUTPUTS/2026-10-29-guiones-atlas-cortes-v19-v24.md` (copia en la carpeta de la oferta). EN + ES voseo completos, 118–140 palabras, 9:16.
- Los seis en el territorio que vende (fricción durante el servicio con la clienta presente) y **sin una palabra de plata**: V16–V18 ya están testeando el bizop y acá rinde la mitad.
- **V19** el minuto del espejo ("no, I love it" con el no adelante) · **V20** nunca fue la tijera (el corte de dos horas te cuesta la clienta de las cuatro) · **V21** "ese no es lo mío" (la carta que se achica) · **V22** el remolino que descubrís al secar · **V23** "lo que te parezca" · **V24** la de 24 que lee una página antes de cada corte, variable del sleeper V6.
- V19 y V20 son los ángulos de las natives 6 y 7 pasados a video: el ad y la native cuentan lo mismo.
- Recomendados 19, 20 y 24. Falta la elección para producir.

## 2026-10-29 (noche 2) — Atlas de Cortes: natives 6 y 7

- **Pedido:** *"Vamos con la oferta de pelo, vamos con 2 natives"*.
- `OUTPUTS/2026-10-29-natives-atlas-cortes-6-y-7.md` (copia en `~/Desktop/atlas-cortes/anuncios/natives/2026-10-29-natives-tanda-3.md`).
- **6 · "The hand mirror"** — Dulcie Rayburn, 56, Jonesboro AR, 1.848 palabras. Ángulo nuevo: **el minuto del espejo**, no el del corte. El "no, I love it" de compromiso y la clienta que no se queja y no vuelve (Rosalind, el butterfly que terminó haciéndole otra).
- **7 · "Three pairs of shears, two of them nearly new"** — Verna Lee Stockard, 58, Owensboro KY, 1.600 palabras. Ángulo: el corte que se come el día (territorio del AT-V8). Dos horas diez en un hush cut bueno le costó dos clientas; el tiempo se va en recordar, no en cortar.
- Las dos **sin una palabra de plata ni de cuentas**: el ángulo de negocio rinde la mitad en esta oferta (V4 y V5 a $22 contra $11–17 de los de fricción).
- Arquitectura del nicho de pelo completa (número contado + objeto, credencial con dirección exacta, clienta-tragedia, el producto lo trae un tercero más joven, el mapa dice NO antes de decir SÍ, checklist de 5 criterios, tres P.S., cierre que vuelve a la foto). Narradoras, ciudades y objetos nuevos respecto de las natives 1 a 5.
- Faltan las imágenes: espera el OK para no gastar créditos.

## 2026-10-29 (mañana) — Herrero: los tres VSL de post-pago, producidos

- **Pedido:** *"Bien, armame los 3 vsl"*.
- Los tres videos quedaron en `~/Desktop/herrero-de-finde/pospagos/`: **`HF-OTO1-planos-a-medida.mp4` (4:53)**, **`HF-OTO2-asistente-1-a-1.mp4` (4:22)** y **`HF-OTO3-hierro-al-costo.mp4` (3:26)**. Duración decreciente, como pide la regla del embudo.
- Voz **Enzo** de Google AI Studio en seis bloques (dos por VSL), cada uno verificado por transcripción y por md5. Avatar **HERRERO** de HeyGen en **Avatar IV 1080p** con el audio ya acelerado a `atempo=1.12`. **204 créditos** de 600, por debajo de los ~230 avisados.
- **Bug de fondo encontrado revisando por hoja de contactos: el generador de planes y el editor normalizaban las palabras distinto** (el generador dejaba la puntuación, el editor la saca toda). Entonces `'pantalla:'` era única para el validador y **una de cinco** para el editor, que agarraba la primera. Resultado: el corte al celular del VSL 1 salía **a los 11 s** en vez de a 3:08, el chip de las 72 horas a 1:11 en vez de a 3:09, un corte del VSL 2 treinta segundos antes, y en el VSL 3 la placa de precio de $7.990 **a los 24 segundos**. Los tres renders decían "OK". **Se re-renderizaron los tres.**
- También: el sello que cae justo en el borde de un corte quedaba con duración negativa y **desaparecía en silencio**. `OUTPUTS/scripts-vsl/edit_herrero_avatar.py` ahora avisa cuando una placa queda con menos de 0,4 s.
- `pospagos/work/plans/gen_oto.py` ahora usa **el mismo `norm()` que el editor**, traduce el índice del ancla al que cuenta el editor, e imprime a qué palabra cayó cada una. Reglas nuevas en `WIKI/vsl-reglas-de-armado.md`.
- Producción documentada en `WIKI/herrero-de-finde.md`. Queda pendiente: los tres downsells con ruleta y rehacer las hojas genéricas `hoja-*.png`, que muestran números de otro plano.

## 2026-10-29 (noche) — Piedras: natives 35 y 36 escritas

- Santiago eligió **la 2 y la 3** de las 6 opciones. Escritas completas en `OUTPUTS/2026-10-29-natives-piedras-35-y-36.md` (prompt de imagen 3:4 + descripción larga en inglés).
- **35 · "The letter has been on my table for nine days"** — Imogene Bratcher, 60, Washington IN, 1.341 palabras. Deuda de 2019 cerrada en siete meses sin dejar la línea de empaque. Brecha: superficie y desmolde temprano. Error de negocio: tres meses comprando moldes en vez de separar una parte fija ("no estaba invirtiendo, estaba comprando").
- **36 · "Two suitcases by the door and one of them is new"** — Loveda Spain, 61, Gaffney SC, 1.108 palabras. Viajó a Tacoma a conocer a su nieto de 2 años. Brecha: el gris (agua) y la flor marrón (secado y momento). Error de negocio: frenó de tomar pedidos antes del viaje en vez de poner la fecha de vuelta.
- Sin montos de ingreso, sin precio del producto, sin URL en el cuerpo, sin caras, dos P.S. cada una con el segundo regalando un consejo práctico.
- Quedan sin generar las imágenes: espera el OK para no gastar créditos.

## 2026-10-29 (tarde 2) — Piedras: 6 opciones de native para elegir

- **Pedido:** *"Vamos con las native, dame 6 y elijo"*.
- **6 opciones** en `OUTPUTS/2026-10-29-natives-piedras-6-opciones-resultado.md`, con la arquitectura del nicho relevada el 28/10 y el eje resultado del 26/10: el teléfono con 9 pedidos sin contestar, la carta del banco con "PAID IN FULL", dos valijas en la puerta, el cartel de feria dado vuelta con "SOLD OUT - TAKING ORDERS", el aire acondicionado nuevo y los dos juegos de moldes de la hermana que no le creía.
- Cada una con objeto, voz con dirección exacta, resultado, prueba visible, número único, **error de negocio admitido** y cierre con frase de un tercero. Ninguna repite objeto con las natives 1 a 34; una sola es de feria.
- Aplicado el reclamo de hoy a los guiones: el resultado tiene que **entenderse sin leer** la descripción. Las más llamativas de un vistazo son la 1 y la 4; la 2, 3, 4 y 6 no llevan ninguna cifra de plata.
- Quedan sin escribir: espera la elección de Santiago para las completas (prompt 3:4 + descripción de 1.000 a 1.500 palabras, solo en inglés).

## 2026-10-29 (tarde) — Piedras: la v30 se cayó por flojа y salió la v31 con promesa fuerte

- **Rechazo de Santiago a la v30:** *"muy flojos, tienen que ser más llamativos, más prometedores"*.
- **Diagnóstico:** apliqué el aprendizaje del 28/10 (mecanismo y entregables, la plata al final y suave) también a la **apertura**, y ahí se murió. El Guion 1 abría con lo que sale mal, el 2 con el retrato de dos personas y el 3 con una lista de negaciones. Ninguno prometía nada hasta la mitad.
- **Regla nueva en `WIKI/guiones-y-anuncios.md`:** la promesa concreta y visual va en la **primera línea** siempre; el mecanismo, los entregables y la plata vienen después. "Suave" no es tibio.
- **Tanda v31** (`OUTPUTS/2026-10-29-guiones-piedras-v31-promesa-fuerte.md`), 3 guiones en inglés y español con voseo, 141–157 palabras:
  1. **Una bolsa de yeso se convierte en cuarenta cosas que un local paga a precio pleno.**
  2. **Cobrás antes de poner un peso tuyo** (el pedido paga el material; novias con la mitad adelantada, locales contra entrega, hoteles con caja mensual).
  3. **Las próximas seis semanas son las únicas que importan** (noviembre y diciembre compran por caja; en febrero te dicen que vuelvas el año que viene).
- Cifras enmarcadas en primera persona o como precio de mercado, no como ingreso prometido, para no comerse un bloqueo.
- La v30 queda marcada como rechazada en `WIKI/scented-stones.md` con sus tres ángulos ya usados. Entregado en bloque de código, guardado en `OUTPUTS/` y copiado al portapapeles en RTF.

## 2026-10-29 — Piedras: tanda v30, tres ángulos del banco del mercado inglés

- **Pedido de Santiago:** "vamos con más guiones para piedras". Variables de algo que ya corre → **3 guiones** (regla del 24/10).
- **Tanda v30** (`OUTPUTS/2026-10-29-guiones-piedras-v30-mercado-ingles.md`): 3 guiones completos en inglés y español con voseo, los tres ángulos salidos del banco de la v29 y ninguno usado de la v23 a la v29:
  1. **La primera tanda que se vea comprable** — gris, burbujas, rajadura y borde flojo, cada uno con su causa y su arreglo, con la *Troubleshooting Guide* como entregable (es el ángulo con el que el whale renovó el 27/10).
  2. **El doble avatar en un mismo guion** (modelo Iris Caldwell), abierto por el lado del cobro: la que quiere un sábado propio y la que quiere el ingreso terminan en el mismo lugar.
  3. **"Esto no es algo a lo que te sumás, es algo que hacés"** — lista de "no" con el *no MLM* adentro y los entregables por nombre (fórmula base, 100+ mezclas, calculadora de precios, camino al primer pedido).
- **Siguen las reglas del 28/10:** mecanismo y especificidad en vez de cuentas, entregables con nombre propio, la plata al final y suave. Estructura, bajada de producto y CTA propios en cada guion, sin una frase repetida entre ellos ni con la v29. 151–163 palabras (el rango de la v29).
- Entregado en bloque de código, guardado en `OUTPUTS/` y copiado al portapapeles en RTF.
- **Wiki:** ángulos usados anotados en `WIKI/scented-stones.md` y output enlazado en `WIKI/index.md`. Sin reglas nuevas (no hubo corrección).

## 2026-10-28 (noche 2) — Herrero: los guiones de los 3 VSL post-pago

- **Pedido de Santiago:** VSL para los post-pagos, *"los guiones tienen que tener relación con el orden de los pospagos, por ejemplo, no podemos decir felicitación en todos"*, de 3 a 5 minutos.
- **Tres guiones encadenados** en `OUTPUTS/2026-10-28-vsl-pospagos-herrero-de-finde.md`: Sistema de Planos a Medida ($24.990), Asistente Personalizado 1 a 1 ($15.990) y Sistema del Hierro al Costo ($7.990). **1.030 / 958 / 804 palabras → 4:50 · 4:30 · 3:46 a 1,3x**, duración decreciente.
- **Se felicita solo en el primero.** El 2 abre retomando el 1 y el 3 avisa que es la última pantalla. El hilo escala: qué fabricar → cualquier medida → quién te contesta → a cuánto comprás el hierro. El 1 y el 2 empujan a la pantalla siguiente.
- **Precios tal cual ImpulTienda** (captura de Santiago), tachados incluidos. ⚠️ Quedan descendentes: ya no se cumple *el ticket más alto va segundo* de `embudo-vsl-post-pago.md`.
- **Todos los números verificados contra el motor del producto:** el portón de 3,40 m no existe en la biblioteca (hay 3,00 y 3,66), el Escalador da $117.000 → $370.000-$480.000, la parrilla BQ-090 $406.000 → $1.030.000-$1.340.000 y el portón FM-068 lleva $124.000 de hierro.
- **Regla nueva medida** en `embudo-vsl-post-pago.md`: 0,28 s por palabra a 1,3x (1.000 palabras ≈ 4:45), sacada de las voces ya rendidas de Herrero (167 palabras = 48 s).
- Falta producirlos: avatar HERRERO en HeyGen con voz Enzo, y los downsells con ruleta.

## 2026-10-28 (noche) — Energía Vital: oferta nueva para LATAM, 6 videos

- **Oferta nueva:** Guía de Autocuración Energética (Digital World, AR), que Santiago lanza a **LATAM en español neutro a US$ 9,99**. Ficha completa en `WIKI/energia-vital.md`.
- **Análisis del ganador:** 54 ads activos en AR desde el 6/10. Se bajaron y transcribieron 4 de sus videos: hay **3 familias de hook** (el trabajo que afecta la salud, atención terapeutas de reiki, no es el típico libro espiritual) y **2 DNA de cuerpo** (esotérica dura y terapeuta a terapeuta).
- **6 guiones en español neutro, sin voseo**, uno por ángulo y con CTA propio: `OUTPUTS/2026-10-28-guiones-energia-vital-latam.md`. Escritos contra el hero de la landing ("raíz espiritual, no el síntoma", "recetas de 3.000 años", "lo aplicas en minutos", garantía de 30 días).
- **6 videos renderizados** de 39 a 44 s en `~/Desktop/energia-vital/anuncios/EV-V1…EV-V6`, con voz **Achernar** de AI Studio (3 opciones entregadas, eligió la 3), `speed 1.30` y `silence [0.26, 0.12]`.
- **Edición propia:** `OUTPUTS/scripts-vsl/edit_energia.py` + `gen_energia_plans.py`, con la paleta violeta y dorada de la tapa y la placa final de 80 fichas + 8 bonos. Se le agregó al editor que el recorte de silencios sea configurable y que el título de la placa final se achique hasta entrar en 1080 px.
- **B-roll de TikTok:** 110 clips bajados con tikwm de 4 tags del nicho; **solo 19 quedaron limpios**. Se descartaron dos ya renderizados (marca de `@usuario` que cambia de lugar) al mirar la hoja de contactos de los videos terminados.
- **Reglas nuevas en `WIKI/guiones-y-anuncios.md`:** oferta de AR que sale a LATAM va en neutro (guion y voz), cómo bajar y transcribir el video de un ad de la Biblioteca de Anuncios, y que el primer clic en Run de AI Studio no dispara.

## 2026-10-28 (tarde) — Herrero: las tres de voz en off de la tanda

- **V40–V42 renderizadas**: `HF-V40-nunca-mas-el-carton.mp4` (48 s), `HF-V41-el-cliente-senala-la-foto.mp4` (43 s) y `HF-V42-lo-que-cobra-un-dibujante.mp4` (44 s), en `~/Desktop/herrero-de-finde/anuncios/`. Completan la tanda del día: 3 con avatar + 3 de voz en off.
- **Hooks y fichas nuevas**, no renovación de los viejos: el cartón que no se dibuja más (portón de dos hojas FM-004), el cliente que señala una foto del catálogo (jaula de potencia GY-013) y lo que cobra un dibujante por un solo plano (invernadero ST-012). Guiones en `OUTPUTS/2026-10-28-renovaciones-herrero-v40-v42.md`.
- **Las fichas salen del motor del producto** (`mk_fichas.py` + `expansion.py`), con los números verificados por transcripción contra lo que dice la voz.
- **Voz Enzo** (la que eligió Santiago en la tanda con avatar) a 1,30, grabada en AI Studio con el Chrome muteado.
- **Bug viejo arreglado:** la línea `QUÉ CORTAR · CUÁNTO HIERRO · CUÁNTO COBRAR` de la placa final venía cortada desde la V34 porque no entraba en 1080 px. Ahora `edit_herrero_v3.py` y `edit_herrero_avatar.py` la achican hasta que entre.

## 2026-10-28 (mediodía) — Herrero: los tres primeros videos con avatar

- **Tanda A1–A3 terminada y renderizada**: `HF-A1-no-me-faltaba-mano.mp4` (51 s), `HF-A2-nunca-le-avise.mp4` (50 s) y `HF-A3-la-soldadora-juntaba-polvo.mp4` (46 s), en `~/Desktop/herrero-de-finde/anuncios/`. Son los guiones 34, 36 y 39 **reescritos en primera persona**; los otros tres de la tanda (35, 37, 38) siguen en voz en off.
- **Avatar "HERRERO" con dos looks** (parado y sentado) creado en HeyGen desde dos fotos de Santiago, con el prompt de `OUTPUTS/2026-10-28-prompt-avatar-herrero-de-finde.md`. Los looks se alternan cortando el guion en dos bloques: mismo costo que un render entero.
- **La voz no gasta créditos:** Avatar IV acepta subir el audio, así que la voz salió de AI Studio. Santiago eligió **Enzo** entre tres opciones (Knox, Daro, Enzo).
- **41 créditos los seis bloques**, de 600. Un bloque de 13 s cuesta 4.
- **Editor nuevo** `OUTPUTS/scripts-vsl/edit_herrero_avatar.py` + `gen_herrero_avatar_plans.py`: el avatar es la base y se corta a fichas, hojas y B-roll solo en las palabras marcadas.
- **Reglas nuevas** en `herrero-de-finde.md`: el audio se acelera antes de subirlo a HeyGen; mutear AI Studio suspendiendo el AudioContext cuelga el botón Run; verificar por transcripción qué voz se bajó; y cuando dos cortes se pisan manda el nuevo.
- **Regla de entrega** (`como-trabajar-con-santiago.md`): lo que Santiago tiene que elegir va numerado en una carpeta propia con solo las opciones; nunca se le abre una carpeta de trabajo.

## 2026-10-28 (noche 4) — Atlas de Cortes: los 3 videos de la tanda bizop

- **AT-V16, AT-V17 y AT-V18** listos en `~/Desktop/atlas-cortes/anuncios/` (31,7 / 32,5 / 39,1 s, 9:16, voz Sulafat), revisados con hoja de contactos a 1 cuadro cada 2 s.
- **AI Studio cambió de UI:** se entra por *Create new dialog*, la voz se busca en **Speaker settings** y la escena va en el desplegable **Style**; el modelo es Gemini 3.8 Flash TTS y el audio se baja con el botón del reproductor. ⚠️ Si se descarga antes de que cambie la duración del player, baja el audio anterior (me pasó con el V18: el archivo era el V17 con el mismo MD5).
- **`edit_atlas.py` ahora respeta `silence` del plan.** Esta tanda corre con `speed 1.30` y `silence [0.26, 0.12]`: la regla de voz en off del 24 y 26/10, que este editor venía ignorando con 0.6/0.35 fijo.
- **Primeras placas con el producto real:** `P_wolf`, `P_hush` y `P_butterfly` son las páginas 41, 35 y 34 del PDF, no el mockup con fotos. El V18 abre nombrando esos tres cortes y mostrando sus mapas.
- **Dos correcciones antes de entregar:** el emoji `⏱️` del hook del V17 salía como cuadraditos vacíos (se cambió por 💸) y su primer chip repetía el texto del hook (se cambió por "It's not slow hands").
- **Sobre el navegador:** la extensión me había enganchado al Chrome del socio de Santiago y por eso se caía la pestaña. Se reconectó a "MacBook Air de Santiago" y recién ahí salieron las voces.
- Wiki: `atlas-de-cortes.md` (sección *Tanda v16 a v18*, con los cambios de pipeline).

## 2026-10-28 (noche 3) — Atlas de Cortes: 3 variables en ángulo bizop

- **Pedido de Santiago:** *"tenemos que hacer 3 variables de esa oferta… apuntando al ángulo de bizop"*.
- **Se le avisó primero:** en esta cuenta el ángulo de plata es el que **peor** rindió (V5 $22,61 y V4 $22,38 contra $11–17 de los de fricción en el sillón). Decidió ir igual, así que se entregó con dos salvaguardas: **cero desglose de cuentas** (lo que hundía a V4 y V5, por la regla del bizop duro del 25/10) y el desculpabilizante *"no es tu técnica, es memoria"* intacto en los tres, porque está en los cuatro que venden.
- **Los tres ejes, todos nuevos para la cuenta:** **V16 "The rebook"** (lifetime value: la que ama su corte vuelve en seis semanas, la que lo ve caerse reserva en otro lado) · **V17 "The chair"** (la hora regalada: dos horas en un corte que cobrás como una, porque hacés y decidís el corte al mismo tiempo) · **V18 "The bookings nobody takes"** (demanda escondida: piden wolf cut, butterfly y hush cut por nombre y los sillones de la zona no los toman, con la lista de "no" y "nadie arriba tuyo" que salió del mercado inglés el 28/10).
- Un solo número por guion, 46 a 55 s, EN + ES voseo completos, y las frases fuertes del hero de la landing repetidas tal cual (regla del 27/10).
- ⚠️ Queda como **test del ángulo**: si estos tres vuelven a dar $22, el bizop se cierra para esta oferta.
- `OUTPUTS/2026-10-28-guiones-atlas-cortes-v16-v18-bizop.md` + `~/Desktop/atlas-cortes/anuncios/guiones/guiones-v16-v18-bizop.md`; wiki: `atlas-de-cortes.md` (sección nueva *Tanda v16 a v18*).

## 2026-10-28 (noche 2) — Herrero: el avatar del competidor, contado

- **Pregunta de Santiago:** *"la página original usa muchos videos con avatar, ¿no?"*. Se clasificaron **los 180 videos únicos** uno por uno (hojas de contacto de `anuncios/work/frames/` cruzadas con las copias de `rows.json`).
- **Respuesta:** avatar usan, pero es el **segundo** formato: 32 videos (17,8 %) y 120 de 631 copias (19 %). El principal sigue siendo el nuestro, voz en off sobre B-roll y fichas (122 videos, 64 % de las copias).
- **Tres cosas que lo vuelven importante igual:** el video **más copiado de toda la muestra es avatar** (002, 21 copias, y 6 del top 10); en los **30 videos más nuevos** el avatar es el 30 % y suman personajes nuevos (un pelirrojo con delantal, dos mujeres); y **el 77 % de los guiones de avatar arrancan en primera persona** contra el 24 % del resto — el avatar les habilita la confesión del herrero, que con voz en off anónima queda sin dueño (nuestro V1).
- **El formato que copian no es un talking head:** avatar recortado sin fondo, parado en la mitad inferior, presente todo el video, con el B-roll cambiando atrás y subtítulos de una palabra.
- **Propuesta pendiente de decisión:** tanda de 3 con avatar (el V7 en primera persona, "yo cotizaba a ojo" de su 004 y "¿qué más sabés hacer?" de su 011), Avatar IV + voz "damian", editor derivado de `edit_atlas_avatar.py`. No se gastó ningún crédito.
- Análisis en `OUTPUTS/2026-10-28-herrero-avatar-vs-voz-en-off.md`; wiki: `herrero-de-finde.md` (sección nueva *El avatar del competidor*).

## 2026-10-28 (noche) — Natives 33 y 34, y la ganadora propia de 67 días

- **Emma Carter y scentedstone.com son marcas de Santiago**, no competidores. La página Emma Carter corre desde el 22/08 (**67 días, 4 ads con el mismo texto**): es la **pieza con más gasto sostenido de toda la oferta**. DNA desarmada entera en `natives-ganadoras.md` — hook de reacción de un tercero con autoridad cotidiana (la agente inmobiliaria), escrita como diálogo con silencios, misma mesada antes y después, y cierre binario. ⚠️ Usa montos fuertes y funciona: contradice lo anotado el 23/10 a partir de Thrift AI. Lectura nueva: la cifra funciona cuando la trae la reacción de un tercero, no cuando abre sola.
- **Natives 33 y 34** (`OUTPUTS/2026-10-28-natives-piedras-33-y-34.md`), elegidas de las 5 opciones del 28/10: la mesa del comedor tomada por cajas hace seis meses (demanda que la desborda, 1.553 palabras) y la caja de las falladas que una mujer compró entera en la feria (1.327 palabras).
- Las dos estrenan los **upgrades del 28/10** sacados de la native de Iris Caldwell: el error admitido es de **negocio** (regalar el packaging de un pedido de 120; tirar producto propio y disculparse por el defecto antes de que lo noten), cierre que vuelve al objeto por boca de un tercero y **dos P.S.**, el segundo con un consejo práctico regalado. Brechas casero/vendible distintas entre las dos a propósito (yeso y peso / fragancia y sellado del dorso).
- Sin montos de dinero en ninguna de las dos: riesgo cero con Meta y la FTC.
- **Pendiente:** variables de la native de 67 días. Terceros con autoridad cotidiana sin usar: el contador, el del banco, el del crédito del auto, la maestra, el dueño del local.

## 2026-10-28 (tarde) — Natives de piedras: DNA del nicho y 5 opciones

- **scentedstone.com es la marca de Santiago**, no un competidor. Corregido en el mapa de competidores de `scented-stones.md`: no se cuenta nunca en el veredicto de competencia.
- **Pasada de natives de imagen del nicho** (browser con `media_type=image`, porque la tool del conector no devuelve el cuerpo del anuncio). Dos arquitecturas nuevas documentadas en `natives-ganadoras.md`:
  - **Iris Caldwell** (la que escala con 83 ads): objeto de apertura = herramienta humilde o error (el molde manchado que no lava desde marzo), el **error admitido es de negocio** (casi regala un descuento por cantidad antes de que se lo pidan), cierre que vuelve al objeto con una frase de un tercero y **dos P.S.**, el segundo con un consejo práctico regalado. Headline: "4 on a bathroom shelf. 120 for a wedding."
  - **Plaster Bloom**: familia de natives en segunda persona, una por falla del oficio, cada una con **un test que el lector puede hacer esta noche**. Sin validar (<100 impresiones). Le habla a quien ya hace piedras → banco de remarketing, no público frío de ingresos.
- **5 opciones nuevas eje RESULTADO** (`OUTPUTS/2026-10-28-natives-piedras-5-opciones-resultado-v2.md`), ningún objeto repetido de las natives 1 a 32. Pendiente que Santiago elija.
- **A verificar:** página "Emma Carter" corriendo desde el 22/08 (67 días, 4 ads con el mismo texto) con la native de la agente inmobiliaria. O es la native que más aguantó de la oferta, o es alguien usando la persona.

## 2026-10-28 — Piedras: investigación del mercado inglés y guiones v29

- **Los guiones v23–v28 (bizop duro) no están funcionando.** Santiago pidió analizar qué está corriendo de verdad en habla inglesa en el nicho de generar ingresos.
- **Barrido en la Biblioteca de Anuncios** (`ads_library_search` + lectura del copy real de cada snapshot en Chrome). Cuatro competidores sobre la misma oferta: **SCENT & STONE Studio** (60 ads activos, el más viejo del 13/09 → 45 días de gasto sostenido, corre en ImpulTienda), **Iris Caldwell Aroma Stones** (83 ads arrancados el 26/10, escalando de cero y ya en inglés, japonés y chino), **Plaster & Bloom** (murió en 22 h) y **The Scented Stone Method** (recién arrancado).
- **Hallazgo central:** ninguno de los que gasta en serio vende con margen pelado, cuentas ni CTA con fecha. El ad que le dio 45 días al whale no menciona plata ni una vez. Venden mecanismo del producto, entregables con nombre propio, lista de "no" (incluido "no MLM") y la demanda que ya existe y nadie abastece.
- **Tanda v29** (`OUTPUTS/2026-10-28-guiones-piedras-v29-mercado-ingles.md`): 3 guiones en inglés y español con voseo, uno por ganador distinto — el negocio del que casi nadie se dio cuenta, lo difícil es saber qué comprar, y el consumible que vuelve.
- **WIKI:** mapa del mercado inglés en `scented-stones.md`, registro del 28/10 con las reglas nuevas en `guiones-y-anuncios.md`, entrada en `index.md`.

## 2026-10-27 (noche) - 100 Paper Squishies: una sola cama musical en la tanda 1

- Santiago pidio que los 6 videos lleven la musica del V4 ("He came home with three he did not make"), que era el bed B.
- `gen_squishies_plans.py`: `MUS` pasa de `{1:A, 2:B, 3:C, 4:B, 5:A, 6:C}` a bed B en los seis.
- Se borro `usage.json` antes de re-renderizar para que el reparto de clips saliera identico; se verifico contra el backup y coincide. Mismos planos, mismas duraciones (21.5 / 17.5 / 15.0 / 15.8 / 16.7 / 24.3 s), solo cambia el audio de fondo.
- Regla nueva en `WIKI/guiones-y-anuncios.md`: una sola cama musical por tanda.

## 2026-10-27 (noche 2) — Herrero de Finde: renovaciones V34–V39 y edición nueva

- **Las renovaciones V22–V27 no funcionaron.** Diagnóstico anotado en [[herrero-de-finde]] y [[renovacion-de-creativos]]: 4 de 6 eran el mismo hook con otro objeto, la edición era idéntica a la del ganador y el cuerpo no coincidía con la promesa de la landing (el `landing → checkout` de 9,21 % del 26/10).
- **Tanda nueva V34–V39** (`OUTPUTS/2026-10-27-renovaciones-herrero-v34-v39.md`): seis formatos de hook distintos (frase de la landing, demo de pantalla, la pregunta del cliente, los cuatro números, ROI y la escalera del principiante), con las frases del hero repetidas tal cual y los números sacados del producto (FM-068, BQ-090, FN-022, SH-148, TK-024, BQ-007).
- **Edición v3 con la estética de la landing:** `OUTPUTS/scripts-vsl/edit_herrero_v3.py` + `anuncios/work/plans/gen5.py`. Paleta rust/ámbar/ink, placa de apertura tipo hero, etiquetas blueprint, cotización en panel oscuro, regla de medidas arriba, subtítulos de 3 palabras con la palabra activa en ámbar y cierre con la marca y la garantía.
- **Material nuevo:** `anuncios/work/stills/mk_demo.py` genera `demo-hojas.mp4` y `demo-scroll.mp4` — el plano real abierto en un celular. Voces Knox en AI Studio con las páginas muteadas.
- **Reglas nuevas** en [[guiones-y-anuncios]] (el ad se escribe contra la landing; renovar también es cambiar la edición) y en [[renovacion-de-creativos]] (checklist de por qué una renovación no mueve nada).

## 2026-10-27 (noche) — 100 Paper Squishies: oferta nueva y tanda 1 de 6 videos

- **Oferta nueva:** `100-paper-squishies.impultienda.ar` (US$ 16,99, **en inglés**), ebook de 100 diseños imprimibles de squishies de papel para chicos, con 3 bonos. Página nueva: [[100-paper-squishies]].
- **Competidor relevado: Hora de Papel** (page 1114598271746718). **94 anuncios activos en 12 días** (arrancó el 15/10), en español rioplatense, italiano y alemán. Videos de **9 a 25 s**, un solo texto principal por idioma y la variación en el video. Se bajaron y transcribieron los 77 videos.
- **7 familias de hook** mapeadas; la más escalada es el precio del kiosco ("$5.000 un squishy y a los dos días, roto", ~18 ads, relanzada hoy).
- **Tanda 1: 6 videos de 15 a 24 s**, uno por familia ganadora, en `~/Desktop/100-paper-squishies/anuncios/`. Guiones en inglés y español con voseo + texto principal: `OUTPUTS/2026-10-27-guiones-100-paper-squishies.md`.
- **Producción sin créditos:** voz Sulafat en AI Studio (mamá estadounidense de 35, speed 1.30), b-roll de 21 clips de TikTok del tag `#papersquishy` bajados con tikwm, stills de la landing. Editor nuevo `OUTPUTS/scripts-vsl/edit_squishies.py` (rojo #EA203A de la tapa).
- **Regla nueva en [[guiones-y-anuncios]]:** revisar los clips de TikTok con una hoja de contactos de 1 cuadro cada 2 s y mirar también la del video renderizado; con 6 cuadros por clip se colaron tres sucios y hubo que rehacer el render tres veces.

## 2026-10-27 (tarde) — Segunda pasada de caza: cazar por fecha, no por volumen

- **Corrección de Santiago** ("la mayoría con menos de 20 ads, todos iguales y con bajas impresiones"): tenía razón, 4 de 5 candidatas no pasaban ni el filtro propio. El error de método era contar ads activos como proxy de gasto.
- **Regla madre nueva en [[caza-de-ofertas]]**: cazar con `start_date[min]/[max]` + `sort_data[mode]=total_impressions`, y filtrar por fecha del ad más viejo y por escalera de fechas antes que por volumen.
- **Candidata real: Menopausa Cancelada** (ID 106449212160487) — 22 ads activos, uno corriendo desde junio de 2024 (873 días), escalera de 873/76/74/69/57 días más lote de hoy, sin marca personal, funnel de WhatsApp.
- **Por qué bajar de peso devuelve siempre caras:** en emagrecimento todo lo que lleva años es marca personal (Zanon Macedo, drvictorcutait, Géssica Andrade). En ese nicho la cara es la oferta; la excepción lo resuelve con WhatsApp.
- Informe ampliado en `OUTPUTS/2026-10-27-caza-ingresos-extra-y-bajar-de-peso.md` y copiado a `~/Desktop/calendario-cristiano/`.

## 2026-10-27 — Caza en Brasil: ingresos extra y bajar de peso

- **Caza nueva con criterio corregido** (`OUTPUTS/2026-10-27-caza-ingresos-extra-y-bajar-de-peso.md`): 16 keywords, barrido mundial, 14 fanpages contadas con `page_ids`, 2 verificadas en el navegador.
- **Candidata A: Viver é Cristo** — 55 ads activos sobre una sola oferta, el más viejo con 24 días, 44 copias del mismo creativo, sin marca personal. Calendário Cristão 2027 en moldes PDF, vendido por WhatsApp con el ángulo "pague só depois de receber tudo".
- **Bajar de peso: descartado por ahora** en PDF low ticket. En 8 keywords no apareció un anunciante que pase el filtro; lo que hay son nutricionistas con cara, suplementos y testers de hoy.
- **Livera (154 ads) no pasa**: todos en circulación desde el mismo día. Se guardó el ángulo del "teste da pinça de 5 segundos" y queda para revisar el 30/10.
- **Reglas nuevas en [[caza-de-ofertas]]** por su corrección ("las conoce todo el mundo y eran marcas personales"): descartar marca personal antes de contar el arsenal, arrancar por footprint de checkout y precio en vez de la keyword del nicho, decir cuando un nicho no da, y volumen sin antigüedad no es winner.

## 2026-10-27 — Keywords para cazar en Brasil: IA, renda extra y manifestação

- **Banco nuevo por nicho** (`OUTPUTS/2026-10-27-keywords-br-ia-renda-extra-manifestacao.md`): ~210 términos en portugués, por ejes, con top 10 de arranque y lista negra por nicho.
- **IA**: paquete de prompts, transformación de fotos (bebê/pet/3D), "sin aparecer / sin saber mexer", IA por oficio (el eje virgen) y producto digital hecho con IA.
- **Renda extra**: tanda que no repite el banco del 26/10 — servicio local, proveedores por ciudad, cobrar/precificar, capital cero.
- **Manifestação**: separado en los tres sub-mercados que no comparten copy (lei da atração, espiritualidade prática, cristão/evangélico) + aviso de política de Meta.
- Actualizados `WIKI/caza-de-ofertas.md` (sección Banco de keywords) y `WIKI/index.md` (Outputs).

## 2026-10-27 — Piedras: tanda v28 (6 guiones bizop) + natives 31 y 32

- **6 guiones bizop duro** (`OUTPUTS/2026-10-27-guiones-piedras-v28-bizop.md`), nombres `27/10 - 1` a `27/10 - 6`. Seis angulos nuevos, ninguno de la v23 a la v27: velocidad al primer peso, la fabricacion que pasa mientras dormis, el cliente que regala en vez de revender, nadie compra una sola (caja), el negocio sin algoritmo y los difusores de auto. EN + ES voseo, un solo numero por guion, CTA con accion y fecha.
- **5 opciones de native con eje RESULTADO** (`OUTPUTS/2026-10-27-natives-piedras-5-opciones-resultado.md`), una sola de feria. Eligio la 1 y la 4.
- **Natives 31 y 32 escritas completas** (`OUTPUTS/2026-10-27-natives-piedras-31-y-32.md`): el delantal del turno del sabado que sigue colgado (dejo el segundo trabajo) y el ticket de la cena de los 80 de su madre pagado por ella. Las dos sin un solo monto de dinero y con la brecha contada como **timing**, no como ingredientes.
- Sin reglas nuevas: la tanda aplica las del 24, 25 y 26/10 (bizop duro para video, resultado para native).

## 2026-10-27
- Arreglado el CTA de abajo del VSL: en teléfono la etiqueta se parte en dos líneas y la segunda quedaba a la izquierda. Falta `text-align:center` en `.btn`; `justify-content` solo no alcanza.
- **El logo del quiz quedó sin marca**: solo "CALISTENIA RUSA · Coach Santi". Probé cuatro íconos de calistenia y después las anillas ya puestas; eligió sacar todo. Regla nueva en [[quizzes-reglas-de-armado]].
- **El VSL entró al quiz.** Embed de Panda en el `<template>`, `SEGUNDOS_OFERTA: 290` (4:50 por reloj desde la última slide) y entrega autocontenida de 858 KB en `calistenia-rusa-quiz.txt`. Script nuevo: `inline_quiz.py`.
- **VSL de Calistenia Rusa rehecho entero (6:17).** Voz "damian", testimonio como chat de WhatsApp, avatar parado sin barras blancas y carpeta ordenada con `material/`. `SEGUNDOS_OFERTA = 295`.
- `validar_anclas.py`: valida contra la lista de palabras que arma el editor (transcripción alineada contra el guion), que no es ni el guion ni `words0.json`.
- ⚠️ El disco de Santiago está al 97% (194 de 228 GB). El primer render murió con "No space left on device".
- **Calistenia Rusa · la voz del VSL salió gallega.** Agustín (HeyGen, etiquetado "Spanish (Argentina)") no suena rioplatense. Regla nueva en [[vsl-reglas-de-armado]] §3: la voz de hombre argentino es **Knox en AI Studio** con el Style de Herrero de Finde + lipsync en HeyGen; la etiqueta de idioma de HeyGen no garantiza el acento; y no se estrena una voz en una entrega (muestra gratis primero). Misma regla general en [[como-trabajar-con-santiago]].
- La voz definitiva la eligió él: **"damian"**, que ya tenía clonada en Mis voces de HeyGen. Queda como voz predeterminada de los dos avatares del Coach. Knox + AI Studio sigue siendo la regla para voz en off sin avatar.
- También: el testimonio pasa a ser una **captura de chat de WhatsApp** hecha con Chrome headless, y el avatar parado se destara de las barras blancas que mete HeyGen.

## 2026-10-27 — Calistenia Rusa: VSL terminado

- **`CALISTENIA-RUSA-VSL.mp4`: 6:11, 1080×1920**, el mismo largo que el original. Más la versión web de 720×1280 (66 MB, faststart) para el quiz.
- **`SEGUNDOS_OFERTA = 287`** (4:47), medido sobre el video final con los silencios recortados y el 1,12x aplicados.
- 21 cortes de B-roll, 17 headlines, 26 efectos, subtítulos palabra por palabra y la música mezclada con ducking.
- **Dos errores encontrados al revisar la hoja de contactos y corregidos**: un B-roll que mostraba al coach del competidor con texto en español, y un plato de pan justo en el bloque del menú para bajar la panza. El plano de la balanza del VSL viejo no se pudo reusar porque trae el subtítulo quemado, así que se generó (5 créditos).
- Reglas nuevas en [[vsl-reglas-de-armado]]: §1c verificar las anclas contra la transcripción antes de renderizar (que existan, que el fin vaya después del inicio y que sean únicas; y nunca anclar en números, que Whisper escribe en cifras) y §1d mirar cada B-roll a tamaño real antes de montarlo.

## 2026-10-26 (noche, 6) — Calistenia Rusa: el VSL

- Santiago: *"quiero que sea el mismo vsl que el de esta pagina… el mismo guion, obviamente adaptado a lo mio, y brolls iguales o similares"*, con el avatar del Coach Santi que pasó en dos tomas.
- **El VSL original se bajó de Panda Video**: el HLS sale sin autenticación en `b-vz-XXXX.tv.pandavideo.com/<uuid>/playlist.m3u8`. Transcripto con faster-whisper (6:11, 1.205 palabras) y mapeado cuadro por cuadro para copiar los 17 B-rolls y las placas.
- **Guion adaptado de 1.162 palabras** con cuatro cambios avisados: el claim falso del reemplazo hormonal, la garantía de 7 a 30 días (para no contradecir al quiz), el testimonio leído por el Coach Santi en vez de fabricado, y el origen asiático milenario cambiado por la escuela rusa de preparación física.
- **Dos avatares nuevos en HeyGen** desde las fotos del jardín, intercalados por bloque (sentado = diagnóstico, parado = oferta). Voz Agustín (Spanish Argentina). Avatar IV, 9:16: **122 créditos** los dos bloques, más que los ~80 estimados.
- **B-rolls con 25 créditos de Higgsfield**: solo las 4 anatomías 3D se generaron; los otros 10 salieron de fotos que ya teníamos, animadas con zoompan.
- Placas, planes de edición y música generados con scripts nuevos en `OUTPUTS/scripts-vsl/`.
- Reglas nuevas en [[vsl-reglas-de-armado]]: §1b bajar un VSL de Panda, dos tomas una por bloque, voces argentinas de HeyGen, el costo real de Avatar IV y §3b-bis cómo cubrir los B-rolls casi sin créditos.

## 2026-10-26 (noche, 10) — La fórmula de los títulos de OTO

- Santiago mandó la pantalla de upsells de Scented Stones: *"son de otra oferta, pero asi son los titulos"* (*The First Customer Blueprint™ 🚀💰*, *Personalized 1-on-1 Assistant 🤖✨*…).
- Queda la fórmula: **nombre de producto que se entiende solo + ™ + dos emojis**, con el sustantivo de formato al final (Sistema, Blueprint, Assistant). Ni nombre de marca a explicar ni frase suelta.
- Los tres de Herrero quedaron: **El Sistema de Planos a Medida™ 📐💰**, **Asistente Personalizado 1 a 1 🤖✨** y **El Sistema del Hierro al Costo™ 🔩💰**.
- Se reescribió la regla del changelog anterior en [[aumento-de-aov]], que había quedado a medias ("describen, no bautizan"): el punto no era sacar el nombre, era que el nombre diga qué es.

## 2026-10-26 (noche, 9) — Los títulos de los OTO describen, no bautizan

- Santiago: *"los titulos tienen que describir de que trata el pos pago, por ejemplo, el herrero de guardia, en ningun momento se entiende que es un chat 1 a 1 personalizado"*.
- Los tres títulos pasaron de nombre de marca a descripción: *Adaptá cualquier plano a la medida que te pida el cliente*, *Chat 1 a 1 con un herrero experto, las 24 horas* y *Comprá el hierro al precio del distribuidor*. Descripciones también más cortas.
- Regla nueva en [[aumento-de-aov]]: en la pantalla del post-pago la persona decide en segundos y no hay quién le explique, así que el título dice qué es y qué hace; el nombre de marca va dentro de la descripción.
- Entregable en `OUTPUTS/2026-10-26-otos-herrero-titulo-precio-descripcion.md`.

## 2026-10-26 (noche, 8) — Herrero de Finde: los 3 OTO post-pago

- Santiago pidió los dos OTO que faltaban (el 2, el chat 1 a 1, ya lo tenía decidido), con la condición de que no se pisen con el producto ni con los 12 bonus.
- Se mapeó primero lo cubierto (qué fabricar, cortar, soldar, terminar, cobrar, vender, qué herramientas) para encontrar los sectores vírgenes: **la medida que el cliente pide y no existe** y **el precio al que compra el hierro**.
- Escalera: **A Tu Medida $24.990 → El Herrero de Guardia $29.990 → El Hierro al Costo $12.990**, con el ticket más alto segundo y downsells al ~50%. AOV proyectado $28.335 (ratio 1,89).
- El OTO 1 se apoya en `expansion.py` del generador, que ya re-escala las 60 familias paramétricas: costo marginal casi cero.
- Marcado: el post-pago no corre en Shopify con Mercado Pago, hace falta ImpulTienda.
- Nuevo: `OUTPUTS/2026-10-26-upsells-herrero-de-finde.md`. Actualizados [[herrero-de-finde]] y el índice.

## 2026-10-26 (noche, 7) — Herrero de Finde: CTA en el tramo muerto

- Santiago: *"vamos a hacer el ajuste de los cta, quiero que la landing quede exactamente igual, pero sumale los cta que me dijiste, actualizame el txt"*.
- **Dos botones nuevos** en el tramo 8%–32% (quedan al 17% y al 22%): debajo de la foto del portón vendido y debajo de *"¿Por qué no 5.000 planos?"*. Mismo markup y mismas clases que los existentes.
- **Barra de compra fija** con el precio y el botón, que aparece al pasar el primer CTA y se esconde sola cuando hay cualquier botón en pantalla. Probada en 10 posiciones de la página: nunca se superpone con un CTA ni tapa el footer.
- Aplicado a los tres archivos de `~/Desktop/herrero-de-finde/landing/` (liquid, txt y PRUEBA.html), con copias previas en `.backup-26oct/`. Actualizada también la copia de `OUTPUTS/2026-10-22-landing-herrero-de-finde.html`.
- Regla nueva en [[pagina-de-ventas]]: nunca más de dos pantallas seguidas sin botón de compra, y cómo montar la barra fija sin que compita con los CTA.

## 2026-10-26 (noche, 6) — Herrero de Finde: diagnóstico del embudo

- Santiago pasó el embudo del día: **695 landing → 64 checkout (9,21%) → 33 compras (51,56%)**, conversión total 4,75%, order bumps 0%. Pregunta: cómo hacer que llegue más gente al checkout.
- **Lectura:** el embudo está mal repartido, no roto. La conversión total duplica el objetivo y el cierre del checkout duplica el KPI; el único ratio malo es landing → checkout. Un cierre del 51% es la firma de una landing que sobre-filtra.
- **Medido en la landing publicada:** 21.706 px (29 pantallas), primer botón al 8% y el segundo al 32% (siete pantallas sin CTA), sin barra sticky, sin contador, LCP de 7,4 s con el H1 esperando la webfont.
- **Message match:** el V7 ganador vende una herramienta barata de taller y el hero abre con "Hacé tu primer $1.000.000". Dos niveles de conciencia distintos.
- Nuevo: `OUTPUTS/2026-10-26-embudo-herrero-diagnostico.md`. Actualizados [[herrero-de-finde]] (sección del embudo) y el índice.

## 2026-10-26 (noche, 5) — Calistenia Rusa: portada sin foto

- Santiago: *"saca la foto del principio, la del antes y despues"*.
- La portada arranca directo con el titular y las 4 tarjetas de edad, que ahora entran casi enteras en la primera pantalla. La bajada que apuntaba a la foto se reformuló.
- Regla nueva en [[quizzes-reglas-de-armado]] §4: si la primera pregunta ya tiene opciones con imagen, la portada va sin foto.

## 2026-10-26 (noche, 4) — Calistenia Rusa: dos pasos sin foto

- Santiago: *"esta imagen quedó muy mal, no quiero imagen ahí, y la del tipo durmiendo que pones desp tmb sacala"*.
- Se sacaron la foto del gimnasio oscuro de *"¿Ya probaste la calistenia rusa?"* y la del hombre sentado en la cama de *"¿Cuándo fue la última vez que sentiste orgullo de tu cuerpo?"*. Con las de objetivo, son tres pasos que quedan solo con opciones.
- Regla nueva en [[quizzes-reglas-de-armado]] §4: la foto de un paso va solo si muestra la opción o el test; la decorativa se saca.

## 2026-10-26 (noche, 3) — Calistenia Rusa: fotos de competidores, verde y resumen corto

- Tres correcciones de Santiago: *"las imágenes son muy malas, busca otros quiz de calistenia militar que tengan mejores fotos, y usa esas"*, *"la slide que muestra el resumen tiene mucha info, se hace muy larga"* y *"los colores reemplaza el rojo por un verde que quede bien, medio oscurito"*.
- **Fotos nuevas de competidores reales**, encontrados por la Biblioteca de Anuncios: **Menletics** (app de calistenia militar para hombres, ~22 ads en AR) dio el selector de edad, las flexiones y las fotos de gimnasio; **Muscle Booster** dio material de apoyo. Descartados: `quiz.calistenia.app` (sirve las siluetas a 96×96), `retomilitar21d.com` (caído), `calisteniatactica.com` (solo mujeres) y los funnels detrás de un "acepto términos" o de un token de API.
- **Las siluetas de cuerpo se arreglaron, no se reemplazaron:** eran WebP con alfa sucio y 342 px. Se recortaron al bounding box del alfa y se montaron en tarjetas de 600 px con degradé suave. Son las que más cambiaron.
- **Paleta a verde #1F6B47** (el mismo de [[secreto-de-la-insulina]]). Las barras de riesgo y el aviso de cupos quedan en rojo para que el verde no signifique "mal".
- **Resumen de 2.200 px a 1.234 px:** una tarjeta con las dos barras, 4 chips y 3 logros.
- Dos generaciones con Higgsfield: el mockup del celular en verde y el retrato del hombre de 65 que faltaba en el set de edades.
- Reglas nuevas en [[quizzes-reglas-de-armado]] §4 y §5. Ficha actualizada en [[calistenia-rusa]].

## 2026-10-26 (noche, 2) — Calistenia Rusa: oferta nueva y quiz armado

- Santiago: *"se me acaba de ocurrir un nuevo producto, Calistenia Rusa del Coach Santi, cuando todos venden calistenia militar, nosotros nos diferenciamos ahi, quiero que hagamos un quiz simple, porque va a tener vsl"*.
- **Modelo:** su propio quiz de `calisteniaasiaticahombres.impultienda.ar` (Calistenia Asiática H40+, Maestro Kaito). Es ImpulTienda con `custom_html` pero adentro trae un **funnel de InLead exportado sin cifrar** en `window.FUNNEL`: se bajó con `curl` y se parseó entero (38 pasos, 92 imágenes).
- **Recorte elegido por Santiago (opción media): de 21 preguntas a 14.** Se fueron los 9 bridges de texto, el biotipo, el bloque de hábitos (agua, sueño, alimentación, energía) y la segunda página de venta duplicada.
- **Tema ruso:** rojo #C8102E + grafito sobre blanco (el original es azul iOS), Oswald + Inter, estrella roja, Coach Santi en lugar del Maestro Kaito.
- **Imágenes:** 29 reusadas del original (ninguna con marca), la flecha azul del antes/después recoloreada a rojo con Pillow, y un **mockup nuevo** del celular con la app hecho en Higgsfield (gpt_image_2, 1k, High, 1:1).
- **Probado paso por paso en Chrome:** las 14 preguntas, los multi-select con opción excluyente, los tres medidores, el IMC con la bolita coherente con la etiqueta, el gráfico de previsión y la oferta con el orden de siempre (cuenta regresiva → cuotas → aviso de mail → botón).
- Entregables en `~/Desktop/calistenia-rusa/` (`landing/`, `imagenes/`) + copia en `OUTPUTS/2026-10-26-quiz-calistenia-rusa.html`.
- Reglas nuevas en [[quizzes-reglas-de-armado]]: cómo se saca un InLead exportado dentro de ImpulTienda, cómo se recorta un quiz cuando el embudo lleva VSL, el texto curvo de los sellos solo en el arco de arriba, y el recoloreo de imágenes reusadas cuando cambia la paleta.
- Página nueva: [[calistenia-rusa]].

## 2026-10-26 (noche) — 365 Actividades: visuales de TikTok y voz más rápida

- Santiago: *"quiero que saques visuales de tiktok, más alineado a lo que vendemos… recordá que sean sin subtítulos… no uses mucho de stock"* + *"metele un poquito de velocidad a la voz"*.
- **44 clips de TikTok bajados sin marca de agua** con tikwm (la búsqueda de TikTok tira error en el navegador: se entra por el perfil del creador). Se usan 27 de **@dccraftlab** y **@healthy.mum.and.b**; los **2 que pidió sí o sí** quedaron anclados en los seis videos.
- Filtrados a mano: carteles quemados, la cara del creador hablando a cámara y **dos clips con capturas de TikTok Studio** que se habían colado en el primer render. Del stock quedaron 5 clips, solo para caras de chicos.
- Voz de **1.22 a 1.30**. Los seis videos quedaron de 36 a 43 s (antes 38 a 46).
- Reglas nuevas en [[guiones-y-anuncios]]: de dónde salen las visuales y cómo se filtran, y la velocidad de la voz.

## 2026-10-26 (tarde, 4) — Herrero de Finde: 4 de los 6 videos de la tanda V28–V33

- **Producidos y listos para subir:** `HF-V28-electrodos`, `HF-V29-media-chapa`, `HF-V30-el-flete` y `HF-V31-sin-poner-un-peso`, de 46 a 57 segundos.
- **Fichas nuevas generadas desde el producto** (`anuncios/work/stills/mk_fichas.py`): el número que se dice en el guion es el mismo que se ve en pantalla. Se sumaron tres páginas reales del PDF como stills (hoja 1 con el precio, hoja 2 con las tres vistas, y una página del catálogo para clientes).
- **`gen4.py` valida las anclas** contra el texto de voz antes de renderizar: atajó `comprar.` por `compre.`.
- **Dos clips de B-roll vetados** después de mirar los frames: uno con cartel en inglés y otro con la marca de otra herrería. Reglas anotadas en [[herrero-de-finde]].
- **V32 y V33 terminados en el segundo intento:** la extensión de Chrome estaba desconectada, no colgada. `select_browser` con el deviceId devolvió la pestaña original con todo configurado. Los seis videos de la tanda quedaron listos.
- Regla nueva de Santiago: **mutear las páginas que uso** ([[como-trabajar-con-santiago]]).

## 2026-10-26 (tarde, 3) — Herrero de Finde: 3 variables y 3 de bizop

- **Guiones 28 a 30 (variables de la DNA del V7):** electrodos → el precio de venta sugerido (BQ-090), media chapa de 3 mm → las tres vistas con cada medida (FN-107) y el flete → la lista de compras sumada en barras (TK-024). Cada uno con cuerpo propio, una sola hoja del plano explicada y una ficha real.
- **Guiones 31 a 33 (bizop, generar ingresos):** el único laburo que arrancás sin poner un peso (el adelanto del 50 % paga el hierro, FM-068), la cuenta de cuatro sábados (BQ-007 + BQ-075 + FM-068) y la objeción "¿a quién se lo vendo?" (Marketplace, el catálogo para clientes y el vecino del cliente, FN-022).
- **Los números salen del producto nuevo**, no del banco de fichas viejo: son los que el comprador ve adentro del PDF.
- `OUTPUTS/2026-10-26-guiones-herrero-v28-v33.md`. De 59 a 69 segundos cada uno.

## 2026-10-26 (tarde) — 365 Actividades Imprimibles: análisis del competidor y 6 videos

- Santiago trajo su landing (`365-actividades-imprimibles.impultienda.ar`, US$ 15,99) y la biblioteca de **Croba** (page id 550882744784458) para modelar los ganadores.
- Relevados los **33 anuncios activos** de la página con `scrape.py`: es un vendedor multi-oferta y **15 son del kit de chicos, corriendo desde el 6 de agosto**. Los 33 videos se bajaron y transcribieron con Whisper.
- Hallazgo: **un solo texto principal en los 15 ads** (el que varía es el video) y **15 familias de hook** distintas, todas anotadas en [[365-actividades-imprimibles]] junto con la DNA del cuerpo y su formato de edición (montaje rápido, subtítulo de 1-3 palabras resaltadas, tapa del producto insertada).
- **6 guiones** en español neutro, uno por familia ganadora, con los números de nuestra oferta: `OUTPUTS/2026-10-26-guiones-365-actividades-imprimibles.md`.
- **6 videos** en `~/Desktop/365-actividades-imprimibles/anuncios/`: voz de AI Studio (Gacrux, mamá latina neutra) y edición con `OUTPUTS/scripts-vsl/edit_365.py` (azul #1D4ED8, subtítulo de 2 palabras con la activa en amarillo, cortes de 2 s, tapas del producto como placas). B-roll: 30 clips gratis de Mixkit + 16 imágenes de la landing. **Cero créditos gastados.**
- Nota de AI Studio: el botón de descarga del player es chico y un clic 20 px a la derecha no hace nada y **no avisa**; hay que verificar la fecha del WAV bajado antes de usarlo (se colaron audios viejos de Downloads hasta que se detectó).

## 2026-10-26 (tarde, 2) — Herrero de Finde: renovaciones del ganador

- Pasó los números del día: **CJTO 5 (el rollo de alambre, V7) con 5 ventas y CPA 3,10** y **CJTO 6 (si nunca cobraste, V10) con 4 ventas y CPA 3,71**, los dos a 40 USD por día. Los seis conjuntos nuevos del 26/10 todavía están en 450 a 890 de alcance. Frecuencia de 1,04 a 1,20: no hay saturación.
- Primera entrega equivocada: 40 hooks sueltos numerados. **Corrección de Santiago:** *"Porque pusiste muchos números, son 6 renovaciones las que hay que hacer. Dame 6 guiones."* Regla nueva en [[renovacion-de-creativos]] y en [[como-trabajar-con-santiago]]: una renovación se entrega como **6 guiones completos** (hook nuevo + cuerpo validado), nunca como lista de hooks; el resto va al banco.
- **Entregados los Guiones 22 a 27:** cuatro sobre el cuerpo del CJTO 5 (electrodos, el flete del hierro, media chapa de 3 mm, la careta nueva) y dos sobre el del CJTO 6 (nadie te encarga un portón si no te vieron soldar / dejá el portón para el mes que viene). `OUTPUTS/2026-10-26-renovaciones-herrero-v22-v27.md`.
- Se evitaron los consumibles ya en el aire: alambre tubular (V7), caja de discos (V13), tubo de mezcla (V14), recortes (V15) y nafta (V6).

## 2026-10-26 (noche, 3) — Herrero de Finde: la biblioteca en un solo PDF

- Santiago: *"subime el pdf con toda la información, saca todo lo demás, quiero el pdf y cada bono"*.
- La biblioteca dejó de estar partida en nueve archivos: ahora es **un PDF único de 4.866 páginas y 144 MB** con la guía, el índice de los 1.205 planos con su número de página, un separador por categoría y los planos. Los 12 bonus quedan cada uno en su archivo.
- En la carpeta quedan **13 archivos, 188 MB**. Los nueve archivos partidos se retiraron.
- `libro.construir_unico()` arma el PDF entero; `libro.construir_categoria()` sigue existiendo por si en algún momento conviene volver a partirlo.

## 2026-10-26 (tarde) — Protocolo Chía 28D: los 6 videos armados

- Santiago: *"vamos con esos, armame los videos"* y *"acordate de ir variando los clips, la edición la quiero similar a la original"*.
- **Voces**: AI Studio, Gemini 3.1 Flash TTS Preview, voz **Sulafat**, Pace Natural, Audio Profile de mujer latinoamericana de 35 en español neutro. Las 6 salieron de **una sola carga de página** (el modelo ya deja repetir) y se verificaron con `revisar_voz.py`: las 6 dicen su guion.
- **Editor nuevo `OUTPUTS/scripts-vsl/edit_chia.py`** (copia de `edit_herrero.py` con la estética del VSL): verde #1F6B47 en el hook, los chips y el botón, subtítulo de 3 palabras con la palabra activa en **amarillo**, chips de fase en el V6, barra de progreso verde, destello cada 4 cortes. Planes: `gen_chia_plans.py` con `usage.json` compartido para que no se repita ningún recorte entre los seis.
- **Entregados** en `~/Desktop/protocolo-chia-28d/anuncios/`: `CHIA-V1-vaso-antes-de-comer` (42 s), `V2-tres-frascos` (42 s), `V3-chia-seca` (42 s), `V4-antojo-de-la-noche` (40 s), `V5-no-es-una-pastilla` (37 s) y `V6-cuatro-semanas` (40 s), 1080x1920.
- Correcciones del camino: el plato final se enganchaba al *"cuando toca el agua"* del medio del guion (se pasó a `occ` 1); dos clips estaban mal nombrados (**c12 es un frasco de chía y c13 la animación 3D del intestino**, que ahora va donde se habla del estómago); y se saltearon los primeros segundos de `c10` porque se ve el envase de una marca de yogur.

## 2026-10-26 (noche, 2) — Herrero de Finde: el producto completo, 1.205 planos y los 12 bonus

- **Dos devoluciones de clientes:** faltaban los instructivos y "el xls de conversión de medidas para cortes", y que la publicación promete 1.200 planos y 12 bonus. Se ajustó el producto a las dos cosas.
- **La biblioteca pasó de 115 a 1.205 planos**, con las cantidades exactas por categoría que dice la landing (180 · 145 · 120 · 210 · 165 · 95 · 180 · 110). Se parametrizaron las 60 familias del generador (`expansion.py`): cada una produce todas las medidas, y los 115 planos curados conservan su código original.
- **Partido en archivos:** una guía con el índice general y ocho archivos de categoría, para abrir en el celular solo lo que estás fabricando.
- **Los 12 bonus, hechos:** la **Planilla de Cortes en Excel** (lista de cortes con barras necesarias, conversor mm ↔ pulgadas con fracción, presupuesto y factor único de actualización de precios; cero errores de fórmula verificados con un evaluador), seis instructivos escritos, el ranking de márgenes generado de los datos, tres packs de planos extra (120 + 150 + 10, ninguno repetido) y el Catálogo para Clientes con una ficha por trabajo.
- **Total: 21 archivos, 1.485 planos, 6.143 páginas, 189 MB** en `~/Desktop/herrero-de-finde/productos/`.
- **Lo único que falta es el curso de soldadura en video (Bonus 8):** se entrega el manual escrito con el mismo nombre. Queda la decisión de producirlo o cambiar ese texto de la landing ([[herrero-de-finde]]).

## 2026-10-26 — Tai Chi Fit: revive la oferta, con quiz nuevo

- Santiago: *"tuve una oferta de Tai Chi, Tai Chi Fit, que me generó muchísimo dinero… la idea es revivirla, pero tengo que hacer mejores embudos, mejores anuncios"*. Mandó el ad de **Calistenia Militar Femenina** para copiarle el quiz (*"cortito, simple y directo"*) y adaptarlo a Tai Chi.
- El original resultó ser **HTML propio** (no InLead): se bajó entero con `curl` de `calisteniafeminina.site`, con sus 10 pasos, su `vsl.html` y su sales page.
- **Quiz armado y probado paso por paso**: 10 pasos, pantalla de análisis, VSL arriba del último paso y la oferta oculta hasta `SEGUNDOS_OFERTA`. Español con voseo, $14.990 con cuotas de Mercado Pago y checkout de ImpulTienda. Entregables en `~/Desktop/tai-chi-fit/` y copia en `OUTPUTS/2026-10-26-quiz-tai-chi-fit.html`.
- Imágenes: 10 reusadas del original (sin marca) y 2 nuevas con Higgsfield (hero de Tai Chi al amanecer y retrato de la Maestra Valentina), porque las del original tenían la marca FEMME FORCE y ropa militar.
- Páginas nuevas/actualizadas: [[tai-chi-fit]] (nueva), [[quizzes-reglas-de-armado]] (cómo sacar el contenido de un quiz en HTML propio + regla de cómo se cambia el **tema** de un quiz modelado sin tocar sus pasos) e índice.
- **Pendiente:** el VSL (Santiago va a mandar la página de calistenia asiática para hombres de donde sale el guion) y confirmar el link de checkout.

## 2026-10-26 — Protocolo Chía 28D: los primeros 6 anuncios

- Santiago: *"vamos a hacer anuncios para la oferta de chia, metete en la pagina original que te mande y armemos variables, no los quiero igual a la competencia, quiero variables bien hechas, que no me los rechacen"*. Dejó 13 clips de recetas de chía como visuales.
- Revisada la página viva (`protocolo-chia-28d.impultienda.ar`) y su checkout. **6 guiones** en español neutro: `OUTPUTS/2026-10-26-guiones-protocolo-chia-28d.md` + 3 textos principales para rotar.
- Los 13 clips quedaron renombrados en `~/Desktop/protocolo-chia-28d/anuncios/broll/` con `INVENTARIO.md` (qué clip va en cada guion, cuáles van mudos, cuál tiene subtítulo quemado).
- Reglas anti-bloqueo del nicho de peso anotadas en [[protocolo-chia-28d]], con el aviso de que el titular de la landing ("Baja hasta más de 20 kilos con el Mounjaro de chía") es el mayor riesgo de rechazo.

## 2026-10-26 (noche) — Herrero de Finde: el producto, generado por código

- Santiago pidió **el producto de la oferta de herrería**, completo y solo el PDF terminado en la carpeta.
- Se leyó la landing entera para mapear cada promesa (4 hojas por plano, mm + pulgadas, lista de cortes sumada en barras de 6 m, orden de soldadura con dibujo, precio de venta sugerido, 8 categorías) y se armó un **motor propio en Python + reportlab**: `OUTPUTS/scripts-producto/` (geometría 3D, isométrico sombreado, tres vistas a la misma escala, cotas en mm y pulgadas, lista de cortes automática, nesting en barras de 6 m, costos y precio sugerido).
- **Entregable:** `~/Desktop/herrero-de-finde/productos/Herrero de Finde - Biblioteca de planos - Volumen 1.pdf` — **472 páginas, 115 planos, 16 MB**, todo vectorial. Portada, cómo se lee un plano, tabla de la casa de hierros, cómo cobrar, control previo al corte, índice con página y los 30 trabajos que más dejan.
- Los códigos que ya se usaron en los ads (BQ-028, BQ-053, TR-072, TR-129, FM-068, SH-148, TK-082, ST-015, ST-064, GY-020, GY-096, FN-022, FN-107…) existen adentro con el trabajo que les corresponde.
- Anotado en [[herrero-de-finde]]: los precios del producto son más bajos que los del banco de fichas (que venían de convertir dólares ×1.000) y el PDF dice 115 planos, no 1.200.

## 2026-10-26 (tarde) — Banco de keywords para cazar ingresos en BR y AR

- Pidió palabras clave no comunes para la Biblioteca de Anuncios, nicho generar ingresos, Brasil y Argentina: que no caigan marcas personales ni las ofertas que ve todo el mundo.
- **Banco nuevo en 6 ejes** con ~180 keywords, sin repetir las 12 de la caza del 24/10: footprints de checkout poco usados (cakto, kirvano, greenn, hubla, tribopay, doppus, celetus, mpago.la), mecánica de entrega, oficio + vender, oficios concretos, **atajos sin oficio** (lista de fornecedores, precificação, CV, cobrar en dólares) y empaquetado/precio. Más la lista negra de términos de gurú. `OUTPUTS/2026-10-26-keywords-caza-ingresos-br-ar.md`.
- Reglas técnicas anotadas: `keyword_exact_phrase` para frases de 2-3 palabras y `country=ALL` antes de filtrar por país.
- 20 keywords de arranque al portapapeles.

## 2026-10-26 — Piedras: 6 guiones nuevos y la regla de qué es una native

- **Guiones v26 (26/10 - 1 a 3), bizop duro:** el consumible que vuelve solo (el aroma se agota y te repiten), cobrás antes de fabricar (cero riesgo de mercadería) y la barrera de entrada de cualquier otro oficio contra una noche. `OUTPUTS/2026-10-26-guiones-piedras-v26-bizop.md`.
- **Guiones v27 (26/10 - 4 a 6), orgánicos tipo TikTok** a pedido suyo: ronda de reposición en tres locales, "este mueble es toda mi fábrica" y volcá una tanda conmigo + cómo apareció el primer pedido. Abren con una acción y muestran el margen en vez de declararlo. `OUTPUTS/2026-10-26-guiones-piedras-v27-organicos.md`.
- **Corrección grande sobre natives:** rechazó las 10 situaciones con eje de mecanismo (florería, iglesia, consignación, "local makers wanted"): *"la idea de una native es transmitir algún resultado bueno"*. La feria es el ángulo más ganador que tuvo la oferta y el otro validado es la madre que pudo comprarle los regalos a los hijos. Regla nueva en [[natives-ganadoras]].
- **Lista nueva de 10 situaciones de resultado:** regalos en el placard, mesa de feria agotada a las once, resumen con "PAID IN FULL", los 19 mensajes del lunes, la foto de la boda, las pilas de efectivo rotuladas, la credencial de la feria grande, la compra del mes, la hermana que ahora cobra y el viaje a la costa. `OUTPUTS/2026-10-26-natives-piedras-10-situaciones-resultado.md`.

## 2026-10-26 (madrugada) — Herrero de Finde: el V7 es el ganador y sale la tanda de 6

- Santiago pasó el dato: el **V7 ("Un rollo de alambre tubular…") hizo 6 ventas en el día con CPA de 1 USD**. La tanda 1 entera había hecho 7 ventas a 10,94 de promedio.
- **Diagnóstico de por qué gana:** compara contra un **consumible del oficio** (no contra la nafta, que entiende cualquiera), con el giro consumible → activo. La jerga filtra el público en la primera palabra y por eso baja el CPA. DNA completa en [[herrero-de-finde]].
- **Tanda producida (6 videos):** 3 variables propias de esa DNA (caja de discos / tubo de mezcla / hierro tirado en recortes) y 3 de **ganadores del competidor sin avatar**, elegidos por copias y verificados por frames: su 011 ("qué más sabés hacer", 9 copias), sus 030 y 041 ("ellos vs. nosotros", 6) y su 100 ("cuánto le cobrás a tu amigo", 5). Se descartaron 051 (avatar PIP), 016 (dibujos animados) y 036 (podcast).
- Guiones: `OUTPUTS/2026-10-25-guiones-herrero-de-finde-tanda-v13-v21.md`. Voces en AI Studio (Knox), videos `anuncios/HF-V13…HF-V21.mp4`. Banco sin producir: V16, V17 y V18.
- **Banco de fichas verificadas** sumado a la wiki: 18 planos leídos de las imágenes con su material, precio de venta y horas. Antes de poner un número en un guion, sale de ahí.
- **Reglas nuevas:** anclas y hooks con tilde validados contra el `.txt` de voz antes de renderizar; verificar por md5 que el wav descargado de AI Studio sea el nuevo (el del V19 bajó repetido); Voice Design es de pago, el camino gratis es Create new dialog.
- **Regla de trabajo:** *"acordate de laburar en mi compu SIEMPRE"* → [[como-trabajar-con-santiago]].

## 2026-10-25 (noche, 2) — El VSL de Panda ya está pegado en el quiz

- Santiago subió el VSL a **Panda Video** (`d96e9c95-796d-4deb-ad81-ae68f42c23ad`) y pasó el embed.
- Embed puesto dentro de `<template id="vsl-template">` y `VIDEO_URL` vacío: el quiz usa el camino de reproductor externo.
- Probado de punta a punta: el player **arranca solo** al llegar al último paso y llegan los `panda_timeupdate`, así que **el botón de los 16:00 sale por el tiempo real del video**. Verificado con una copia de prueba en 8 s.
- Panda arranca **en silencio** con su propio cartel azul "Pulse aquí para activar el sonido". Eso se configura en el panel de Panda, no en el HTML.
- El MP4 propio (`landing/Protocolo-Chia-28D-VSL-web.mp4`, 146 MB) queda guardado como alternativa: alcanza con poner su dirección en `VIDEO_URL`.

## 2026-10-25 (noche) — El VSL adentro del quiz, con botón a los 16 minutos

- Santiago: *"poneme el vsl en el quiz, y quiero que el botón de cta aparezca a los 16 minutos, el video tiene que arrancar de una"*.
- Se armó **`landing/Protocolo-Chia-28D-VSL-web.mp4`**: 720x1280, CRF 25, AAC 96k, `+faststart`. 17:16 en **146 MB** (del master de 1,0 GB).
- El `<template id="vsl-template">` dejó de ser un hueco para el embed: ahora tiene **player propio** sin controles ni barra de progreso, que arranca solo al llegar al último paso e intenta reproducir **con sonido**; si el navegador lo rechaza, pasa a silencio y muestra "TOCA PARA ACTIVAR EL SONIDO".
- **El botón sale a los 960 s del video, no del reloj** (`timeupdate` + `currentTime`), con respaldo por reloj para el caso de embed externo. Antes eran 795 s de reloj.
- Probado de punta a punta en Chrome sobre un server local: el video arranca solo y sin silencio, y el botón aparece cuando el video cruza el umbral (se verificó con una copia de prueba en 8 s).
- Regla nueva en [[quizzes-reglas-de-armado]] §7b.

## 2026-10-25 — Protocolo Chía 28D: voz nueva (Achernar) y render 50 veces más rápido

- Santiago: *"la voz de la experta no me gustó nada"* → se eligió **Achernar** de las 3 pruebas y se rehízo el VSL entero con esa voz.
- **Voz en Google AI Studio** (gratis, 5 bloques de ~580 palabras) y **HeyGen solo para el lipsync** sobre ese audio (Avatar IV, 720p, **286 créditos**). Al final se le pone el WAV original encima del video, así que no queda la pérdida del MP3 que se sube.
- Revisión palabra por palabra con `revisar_voz.py`: se encontraron y corrigieron 2 errores reales (un bloque se comía "hambre", otro leía mal "SSL").
- **Render por segmentos en paralelo** (`RAPIDO=1` + `render_rapido.py`): de **8 horas a 9 minutos**. Detalle en [[vsl-reglas-de-armado]] §4f.
- Los b-rolls quedaron limpios **en el archivo**: se recortó la presentadora del competidor de 16 clips, se borraron los subtítulos en voseo del checkout y se cambiaron los 2 planos del cierre que tenían quemado el "$24.999".
- **`Protocolo-Chia-28D-VSL.mp4` final: 17:16.** El precio pasó a las 12:59, así que el botón del quiz pasó a **795 s**.

## 2026-10-25 — Protocolo Chía 28D: VSL terminado (18:45) y quiz listo

- **`~/Desktop/protocolo-chia-28d/vsl/Protocolo-Chia-28D-VSL.mp4`**: 18:45, 1080x1920, 820 MB. 45 b-rolls, 25 placas, 9 efectos, música, subtítulo palabra por palabra y el bloque de 3 testimonios insertado a los 8:49.
- **HeyGen se comió dos tramos del guion** (la empatía del minuto 2:27 y el anclaje de 140/97 dólares). Se regeneraron esas frases con Avatar IV (~8 créditos) y se pegaron en el crudo.
- **El recorte de silencios se había comido 10 s de voz real** porque el guion de referencia tenía esas frases en otro orden y el alineador las tomó por invento de Whisper. Se reordenó el guion y se rehízo el recorte.
- **18 de 45 b-rolls traían a la presentadora del competidor en las puntas.** Detector nuevo (`OUTPUTS/scripts-vsl/detectar_presentadora.py`) + parche por ventana con el tramo limpio del propio clip y los subtítulos re-quemados. También se sacaron el cartel "$24.999", el badge fijo del competidor y los subtítulos en voseo del checkout, y se rehizo la placa final (se salía de pantalla y decía "Desbloqueá").
- **Quiz** en `landing/` (ImpulTienda + PRUEBA.html), en neutro, a US$ 17, con el botón a los 860 s.
- Script nuevo `insertar_bloque.py`, `TRIM_PRESET` en `edit_vsl_quiz.py` (el recorte pasó de 90 a 4 minutos) y §4e nueva en [[vsl-reglas-de-armado]].

## 2026-10-25 — Natives piedras: 10 opciones bizop + las 27 y 28 escritas

- `OUTPUTS/2026-10-25-natives-piedras-10-opciones-bizop.md`: diez opciones con la arquitectura del nicho y el eje corrido a oportunidad (el objeto de apertura es la oportunidad, sin pérdida, sin desgloses, un mecanismo por opción).
- Eligió la 1 y pidió una de feria: `OUTPUTS/2026-10-25-natives-piedras-27-y-28.md`. **27** = la etiqueta de $28 en una cadena de deco (la demanda ya probada por el retail). **28** = la caja del dinero al cierre de la feria con tres papeles encima (la feria es donde te encuentran los compradores por volumen, no el día de ventas).
- WIKI: tanda registrada en [[natives-ganadoras]] y outputs enlazados en `index.md`.

## 2026-10-25 — Piedras v25: bizop duro (y regla nueva)

- Santiago rechazó la v24: *"No me gustaron, acordate lo que te dije del bizop, tenemos que apuntar a eso"*. Diagnóstico: escena o tesis en la primera línea y varios números por guion (el desglose que la regla del 24/10 ya prohibía).
- **Regla nueva en [[guiones-y-anuncios]] (bizop duro):** oportunidad en crudo en la primera línea, **un solo número en todo el guion**, el negocio en tres verbos cortos y CTA con acción concreta y fecha.
- `OUTPUTS/2026-10-25-guiones-piedras-v25-bizop-duro.md` (25/10 - 4 a 6), EN + ES: la demanda que ya existe sin proveedor, un cliente de 150 piezas y el mercado protegido (el yeso pesa y se rompe).
- WIKI: registro en [[guiones-y-anuncios]], v24 marcada como rechazada en [[scented-stones]], output enlazado en `index.md`.

## 2026-10-25 — Piedras v24: 3 variables bizop

- Pedido: *"Vamos con mas guiones para piedras"*. Al ser variables de algo que ya corre, la tanda es de **3** (regla del 24/10), con el formato **BIZOP** vigente desde la v23.
- `OUTPUTS/2026-10-25-guiones-piedras-v24-bizop.md` (25/10 - 1 a 3), EN + ES, 45–55 s, ángulos nuevos: la demanda ya probada por el retail ($28 la etiqueta en las cadenas), el cliente que compra 150 de una (novias, hoteles, inmobiliarias, empresas) y el poder de precio sin fábrica que pueda competir. CTAs distintos entre sí y distintos de la v23. Banco con 4 ángulos más al final del archivo.
- WIKI: ángulos usados anotados en [[scented-stones]] y output enlazado en `index.md`.

## 2026-10-24 — Protocolo Chía 28D: testimonios, pantallas de la app/checkout y quiz

- Santiago: *"Armalos vos o pone los mismos, esa oferta original es mia"* y *"usa los de la original"*. Se dejan de tratar como material ajeno: se reusan los **3 testimonios** y las pantallas de la **app** y del **checkout** del VSL viejo.
- **`testimonios/TESTIMONIOS.mp4` (1:22):** los 3 testimonios del original (8:18–9:46) sin las menciones a la marca vieja. Se cortó "el protocolo Chía 4S" y "Alejandra" del audio y, donde el subtítulo quemado los seguía mostrando, se borró la banda con `rmsubs.py` y se escribió "GRACIAS DOCTORA" con el mismo estilo.
- **10 b-rolls nuevos** de la app (`b0637 b0645 b0650 b0656 b0661 b0666`) y del checkout (`b0810 b0816 b0824 b0833`), limpios de subtítulos y sumados a `plan.json` (45 entradas).
- **Script nuevo `OUTPUTS/scripts-vsl/insertar_bloque.py`:** mete un bloque con su propio audio adentro del render final, en un segundo exacto.
- **Quiz armado:** `~/Desktop/protocolo-chia-28d/landing/protocolo-chia-28d-quiz.txt` + `PRUEBA.html` (probado en Chrome, los 5 pasos y el CTA). Copia del quiz original (ImpulTienda, `custom_html`), en español neutro y a **US$ 17**, con el botón a los **840 s** porque el VSL dice el precio a las 13:46.
- WIKI: §4d nueva en [[vsl-reglas-de-armado]], fuente `custom_html` y registro en [[quizzes-reglas-de-armado]], avance en [[protocolo-chia-28d]].

## 2026-10-24 — Profesional Digital: los 6 videos, re-renderizados más rápidos

- Santiago: *"necesito que a todos les metas un poco más de velocidad y cortes bien los silencios, quedaron lentos"*.
- `work/edit_pd.py` ahora lee `silence: [stop_duration, stop_silence]` del plan (antes estaba fijo en 0.6/0.35). Los 6 planes pasaron a `speed: 1.22`, `silence: [0.26, 0.12]` y `cut: [1.9, 2.4, 2.9]`.
- Los 6 MP4 se reemplazaron en `~/Desktop/profesional-digital/anuncios/`; los viejos quedaron en `work/old/`. Bajaron de 39–44 s a 33–38 s.
- WIKI: regla fija nueva en [[guiones-y-anuncios]], detalle técnico en [[ugc-y-video-generativo]] y registro en [[profesional-digital]].

## 2026-10-24 — Primera caza con la skill: renda extra + emagrecimento black (Brasil)

- Barrido mundial (12 keywords, 25+ consultas por API) **+ auditoría de 11 fanpages en la Biblioteca web**, con fechas de inicio, dominios, precios y copys verificados.
- **Ganadora 4/4: el subnicho de "adesivos para panos de prato".** PDF de +37 calcomanías para repasadores a **R$ 6,90–10**, vendido por WhatsApp. ~240 ads activos entre 9 anunciantes; **Pinturas da Sueli con 97 ads corriendo desde el 10 de julio (106 días)**, Mais Você 79 días, Roberta Carvalho 45 ads / 35 días. Veredicto: **arbitrar al mercado inglés**, mismo avatar que Scented Stones.
- **Maria Alice (69 ads, 26 días): el modelo de negocio a copiar.** Stack de ofertas de **R$ 10 por oficio**, cada una en su dominio `.shop` (licores, partituras de sax, cifras litúrgicas, uno en holandés) y **+500 proyectos de parrillas para fabricar** = Herrero de Finde en Brasil. Dos bullets suyos para robar.
- **Emagrecimento: Isadora Nogueira** (130 ads, 36 días, gasto sostenido en 18 fechas distintas, "Protocolo Restart" en desafiorestart.com.br) y **Carlão Silva** (92 ads, 27 días, dos dominios para la misma oferta).
- **Corrección sobre el "whale" de 510 ads:** al abrirlo en el navegador resultó ser **calistenia asiática para hombres +40** (lastafit.site) y con solo **9 días** de antigüedad. Descartado. Dra Lidiane Nutri (230 ads, 43 días) vende un **encapsulado manipulado**, no infoproducto.
- Informe completo en `OUTPUTS/2026-10-24-caza-renda-extra-y-emagrecimento-brasil.md`.
- **Método: `WIKI/caza-de-ofertas.md` tiene ahora un Paso 3 obligatorio** — auditar en la Biblioteca web con `country=ALL`, porque la API no da fechas de inicio, dominios ni precios, y **el ranking por volumen sale al revés sin las fechas**.

## 2026-10-24 — La skill `cazar` entra al cerebro

- Santiago cargó `SKILL-2.md` (la skill **cazar**) → copiada a `RAW/2026-10-24-skill-cazar.md`. Es idéntica a la que ya está instalada en las sesiones, así que no hubo que instalar nada.
- Nueva página `WIKI/caza-de-ofertas.md` con la skill entera: barrido mundial con `ads_library_search`, los 4 ejes de keywords, el conteo de arsenal con `page_ids`, el filtro madre (50+ ads activos con 3+ días), la escalera de certeza hasta WHALE, el veredicto (ENTRAR / SUBNICHO / DESCARTAR / WHALE), el arbitraje multi-mercado y el score de 4 señales.
- **Criterio nuevo de Santiago (registro):** busca ofertas **low ticket, escondidas (no las comunes que ve todo el mundo), sin marca personal, ya escaladas o empezando a escalar, y que vendan.** Sumado a `caza-de-ofertas.md` y a `como-trabajar-con-santiago.md`.
- Tabla comparando los dos filtros que conviven: el de la skill (50+ ads, 3+ días, todo el mundo) y el de la formación ([[funnel-hacking]]: 10–15 ads, 1 semana, mismo URL, sin marca personal). Se usan combinados.
- Enlaces cruzados actualizados en `index.md`, `funnel-hacking.md`, `como-trabajar-con-santiago.md` y `claude-con-meta-ads.md`.

## 2026-10-24 — Protocolo Chía 28D: avatar, bloque 1 del VSL y regla de créditos

- Avatar **"Valeria Chia 28D"** creado en HeyGen desde la foto de Santiago, con voz neutra de México ("Buddy - Voice 3").
- Guion dividido en 4 bloques por el tope de 5.000 caracteres del cuadro de Creación rápida. **Bloque 1 generado** (4:48, 1080x1920): `~/Desktop/protocolo-chia-28d/vsl/HEYGEN-parte01.mp4`.
- ⚠️ El bloque 1 se llevó **231 de los 237 créditos** porque salió con Avatar 6 Pro (~48 créditos por minuto). Los bloques 2, 3 y 4 quedaron rechazados por saldo.
- Santiago: *"Usa el avatar IV siempre, me gastaste todos los creditos"*. Regla fija en `WIKI/vsl-reglas-de-armado.md` §3c y en `WIKI/como-trabajar-con-santiago.md`: siempre Avatar IV y avisar el costo antes de una tanda larga.
- **55 b-rolls** recortados del original y limpiados de subtítulos quemados con `rmsubs.py`: `~/Desktop/protocolo-chia-28d/vsl/brolls/clean/`.

## 2026-10-24 — Protocolo Chía 28D: análisis del VSL competidor y arranque del clon

- Santiago trajo el VSL de **Protocolo Chía 4S** (Argentina, +700 anuncios prendidos) para clonarlo en LATAM con acento neutro, misma edición y mismos b-rolls, bajo el nombre **Protocolo Chía 28D**.
- Video transcripto con Whisper (17:46) y edición mapeada con hojas de contacto: estructura en 16 bloques, inventario de b-rolls y catálogo de placas en `OUTPUTS/2026-10-24-protocolo-chia-28d-analisis-y-plan-vsl.md`.
- Nueva página `WIKI/protocolo-chia-28d.md`.
- Entregado el prompt del avatar (`~/Desktop/protocolo-chia-28d/vsl/PROMPT-AVATAR.txt`) y el guion neutro 1 a 1 con el original (`GUION-VSL-CHIA-28D-v1.txt`, 2.960 palabras) con los precios como marcadores hasta ver la página.
- Pendiente de Santiago: la página original, país/moneda/precio, si hay quiz y si hay testimonios propios.

## 2026-10-24 — Profesional Digital: análisis de Elevada Digital y 6 videos anti-bloqueo

- Pedido de Santiago: modelar los ganadores de Elevada Digital para Argentina **con guiones que no se bloqueen** (en LATAM le rechazaron todos los anuncios por prometer de más).
- Relevados 274 anuncios activos, 239 videos bajados y 163 únicos transcriptos con Whisper. Patrones (hooks, formato visual, duplicados, días activos) en `WIKI/profesional-digital.md`.
- Reglas anti-bloqueo nuevas (sin montos ni plazos, sin atributos personales, resultado en primera persona y chico, anti-hype, CTA limpio) en `WIKI/profesional-digital.md`.
- 6 guiones en `OUTPUTS/2026-10-24-guiones-profesional-digital.md` y 6 videos de voz en off (Sulafat porteña + b-roll de Mixkit + tapas de la landing) en `~/Desktop/profesional-digital/anuncios/PD-V1…V6.mp4`.
- Alerta: la landing tiene el pie y las reseñas del competidor ("Candamil Digital Ventures LLC · elevadadigital.com", capturas de "elevada_digital").
- Santiago: *"Acordate que solo son 6 videos los que tenés que hacer."* Para el lanzamiento de una oferta nueva la tanda es de 6.

## 2026-10-24 — Herrero de Finde: los 6 videos V7–V12, terminados

- Las 6 voces grabadas en AI Studio (Knox + Style argentino) y los 6 videos renderizados: `~/Desktop/herrero-de-finde/anuncios/HF-V7…HF-V12-*.mp4`, de 46 a 61 s.
- **Tres arreglos durante el render:** el V8 se cortaba por una palabra ancla con ocurrencia mal contada ("cinco" es también la primera palabra del guion); las fichas se recortaban a lo ancho por el zoom constante (`fit_w` pasó de 1,2 a 0,86); y un clip de B-roll lleva el cartel en inglés "And that's how you do that" desde el segundo 97 (`LIMITE = {'Y': 96}` en `gen2.py`).
- **Corrección de Santiago:** *"¿Cuántos videos estás haciendo? Solo quería 3."* Regla nueva en `WIKI/guiones-y-anuncios.md` y en la memoria: **la tanda es de 3**; el máximo de 6 es un tope. Para subir van el V7, el V8 y el V11; V9, V10 y V12 quedan de banco.

## 2026-10-24 — Scented Stones: natives 24, 25 y 26 con el ángulo BIZOP

- Santiago: *"Ahora vamos con las natives, apuntando a esto que hablamos."* Se aplicó la regla del 24/10 (bizop, sin historia larga ni cálculos) **sin perder** la arquitectura del nicho Thrift AI ni el largo de 900–1.200 palabras.
- **Qué cambió respecto de las natives 22 y 23:** el objeto de apertura ya es la oportunidad (un mostrador vacío, un calendario de pedidos, la góndola de ambientadores), desaparece el tramo de pérdida que ocupaba media native y no hay un solo desglose de cuentas. El bloque de honestidad y el tercero más joven se mantienen porque son los que dan credibilidad.
- `OUTPUTS/2026-10-24-natives-piedras-24-25-26-bizop.md` (+ copia en `~/Desktop/scented-stones-ad/anuncios/`): **24** el canasto con la tarjeta "LOCAL MAKERS - ASK FOR DIANE" (Marcie Dalton, Kirksville MO) · **25** el calendario de la heladera con "MONROE WEDDING - 120 FAVORS" (Paula Renfro, Chillicothe OH) · **26** la góndola de plug-ins contra una piedra en la mano (Sharon Kimbrough, Hattiesburg MS).
- Fichas de las tres en `WIKI/natives-ganadoras.md`.

## 2026-10-24 — Scented Stones: regla nueva de formato BIZOP y tanda v23

- Santiago rechazó la v22 completa: *"esos guiones no me están gustando para nada. Son mucha historia, mucha vuelta. A la gente le aburre eso… vendelo más como un bizop, como un business opportunity… todos esos cálculos son los que los aburren a los clientes. Tenemos que buscar que se vea súper llamativo lo que ofrecemos."*
- **Regla nueva** anotada en `WIKI/guiones-y-anuncios.md` (registro 2026-10-24) y marcada en `WIKI/scented-stones.md`: oportunidad en la primera línea, segunda persona, 45–55 s, **un solo número llamativo y cero desgloses**, estructura margen → facilidad → quién compra → por qué ahora → CTA duro. Manda sobre la DNA en primera persona de los ganadores.
- **Tanda v23** en `OUTPUTS/2026-10-24-guiones-piedras-v23-bizop.md` (+ copia en `~/Desktop/scented-stones-ad/anuncios/`): margen absurdo declarado · demanda sin oferta en tu ciudad · la lista de "sin" · el negocio en 3 pasos · reemplazar un turno de fin de semana · la temporada que cierra en febrero. Entre 47 y 54 segundos.

## 2026-10-24 — Scented Stones: tanda v22 de guiones (ingresos extra) y relectura de la landing

- Santiago: *"Vamos con mas guiones para piedras. Armemos guiones ganadores, que apunten a mi publico"* + la URL de la landing de nuevo.
- **Relectura de `scentedstone.lovable.app`:** aparecen el catálogo con precio por tipo de pieza (colgantes marmoladas $6–10, terrazzo $7–12, cuarzo con vena dorada $9–14, difusores de auto y placard $6–9, sets $18–35) y las cifras de los 4 testimonios. Anotado en `WIKI/scented-stones.md`.
- **Tanda v22** en `OUTPUTS/2026-10-24-guiones-piedras-v22-ingresos.md` (+ copia en `~/Desktop/scented-stones-ad/anuncios/`): 6 guiones de **mecánica de negocio**, ninguno de los ángulos de las tandas v15–v21. La habilitación que no necesitás · el costo mayorista que duplica la ganancia · fabricante vs. revendedora de comisión · vender en sets en vez de sueltas · el P&L honesto de octubre · la competencia del pueblo como prueba de demanda.
- Todos entre 78 y 83 segundos (tope de 1:30), estructura y CTA propios por guion, sin precio de la guía salvo como "baratísimo / dirt cheap", sin Etsy.
- Banco al final del archivo: feria de navidad, el pedido que no pude cumplir, nostalgia de la abuela, FREE today y el testimonio del escéptico.

## 2026-10-23 — Herrero de Finde: material de los videos V7–V12 listo (faltan las voces)

- Santiago: *"Armame los videos."* Quedó todo armado menos la voz en off: **la extensión de Chrome pierde la pestaña entre llamada y llamada** (el grupo de pestañas desaparece después del primer click), así que no se pudieron grabar las 6 voces en AI Studio.
- **Textos de voz** en `anuncios/work/vo/V7.txt` a `V12.txt`.
- **Fichas nuevas:** las 4 hojas de un plano en español generadas por código (`anuncios/work/stills/mk_hojas.py`): el dibujo, la lista de compras, la lista de cortes y el orden de soldadura. Las `hdf-pagina-*.webp` del original no sirven para el ad: están en inglés y llevan la marca del competidor.
- **Planes de edición** `V7.json` a `V12.json` con `anuncios/work/plans/gen2.py`, verificados (todas las palabras ancla existen en su guion).
- **Corrección de números:** el V8 y el V9 tenían precios inventados. Se cambiaron por planos reales de la landing (protector de cabina, botellero, hoja de portón, escalera, pérgola). Regla anotada en `WIKI/herrero-de-finde.md`.

## 2026-10-23 — Herrero de Finde: lectura de la primera tanda y 6 variables nuevas

- Santiago pasó los números de los 6 conjuntos del 23/10: **76,57 USD, 7 compras, CPA 10,94**. *"Consiguió ventas, pero tampoco tanto, hay que agarrar lo que funcionó y mejorarlo."*
- **Diagnóstico:** los conjuntos que vendieron abren con plata o un número en el primer segundo. Gana la **comparación de costo** (V6, "menos que un tanque de nafta", CPA 7,05) y después las **listas costo de material → precio de venta** (V5, V4, V3). El único con cero ventas es el V1, el de la anécdota. El V2 se apagó con el segundo mejor CPA (8,70) y un solo presupuesto gastado.
- **Tanda V7–V12** en `OUTPUTS/2026-10-23-guiones-herrero-de-finde-v7-v12.md` (+ copia en `~/Desktop/herrero-de-finde/anuncios/guiones-v7-v12.md`): comparación de costo con el alambre tubular, 5 trabajos que te piden y nunca cotizás, un portón corredizo en un finde, escalera para el que nunca vendió, inventario del garage y recorrido de lo que hay adentro. Cada una con estructura y CTA propios, todas bajo 1:30.
- Resultados y regla nueva anotados en `WIKI/herrero-de-finde.md`; tabla completa en `OUTPUTS/2026-10-23-registro-herrero-de-finde.md`.

## 2026-10-23 — The Women's Cutting Atlas: primera tanda de natives (3, en inglés)

- Santiago: *"Ahora quiero que armemos natives, pero para pelo... Investiga a ver qué es lo que está funcionando."* Se relevó la Ads Library a mano (la tool `ads_library_search` del conector no devuelve el cuerpo del anuncio y el matching trae basura: para natives hay que ir por browser con `media_type=image`).
- **Dos hallazgos:** no existe una sola native de copy largo apuntada a peluqueras en todo el mundo (el nicho corre 100% video), y la voz que ya gana en el mundo del pelo es la **cosmetóloga veterana con dirección exacta**, con 15+ páginas corriéndola hoy pero vendiéndole al consumidor final (caída de pelo).
- Arquitectura desarmada en 19 puntos sobre la ganadora de Donna Whitfield (~3.900 palabras) en `OUTPUTS/2026-10-23-analisis-natives-nicho-pelo.md` y en `WIKI/natives-ganadoras.md`.
- **Corrección de Santiago:** la URL de la landing no va dentro del texto de la native (se quitaron las 14 apariciones; queda una referencia suave sin dirección en el CTA). Regla anotada en `WIKI/natives-ganadoras.md`.
- **3 natives nuevas** en `OUTPUTS/2026-10-23-natives-atlas-cortes.md` (+ copia en `~/Desktop/atlas-cortes/anuncios/natives/`): las once hojas laminadas en el cajón del sillón, los dos montoncitos de pelo distintos al barrer y la de 24 años que se quedó con el corte que ella negó. Las tres con el desculpabilizante "no es tu técnica, es memoria", sin plata y sin precio.

## 2026-10-23 — The Women's Cutting Atlas: carpeta ordenada por entregable

- Santiago: *"Me lo tenés que mandar en PDF. No sé en dónde lo dejaste. Ordename la carpeta de la oferta. Ordenámelo por anuncios producto."* El PDF estaba enterrado en `producto/out/`.
- `~/Desktop/atlas-cortes/` quedó con **dos carpetas y un `LEEME.md`**: `producto/` (el PDF en la raíz + `muestras/` + `fuente/`) y `anuncios/` (los 12 `AT-V*.mp4` + `guiones/` + `material/` con todo el crudo).
- `render.py` ahora escribe el PDF en `producto/` y el HTML intermedio en `fuente/`. Reconstruido y verificado: 56 páginas, 2,1 MB.
- Regla nueva en `WIKI/atlas-de-cortes.md` (**Orden de la carpeta**) y en la memoria `carpeta-por-oferta`: el entregable final va en la raíz de su carpeta con el nombre del producto, el crudo en `material/` o `fuente/`.

## 2026-10-23 — The Women's Cutting Atlas: el producto principal, armado por código

- Se armó el producto completo de la oferta de pelo: **`~/Desktop/atlas-cortes/producto/The-Womens-Cutting-Atlas.pdf`**, 56 páginas A4, 25 mapas de corte, 6 módulos y sección de referencia.
- **Todas las ilustraciones son SVG generado por código** (`producto/fuente/heads.py`): cuatro vistas de la cabeza, siluetas de pelo por corte, diagramas de elevación con transportador, patrones de sección y mechas con tijera. Cero fotos, cero Higgsfield, cero HeyGen.
- El PDF se arma con Chrome headless desde HTML + CSS (`render.py`, `style.css`, `content_01..04.py`, `main.py`), así que cualquier corrección se re-renderiza en segundos.
- La estructura de cada mapa copia la que la landing muestra de muestra (Technical data, 8 pasos, Ideal for, Common mistakes, Final check, Pro tip) y están incluidos todos los cortes que la landing enseña antes de pagar.
- Detalles en `WIKI/atlas-de-cortes.md`, sección **El producto principal**, con los dos pendientes: rehacer los mockups de la landing con páginas reales y armar los 5 bonus.

## 2026-10-23 — Pilates sin Vueltas: las 6 voces rehechas con acento argentino

- Santiago: "tiene una voz que habla muy neutro y parece que son videos para LATAM, pero necesito que sean videos para acento argentino". Se regeneraron las seis voces en Google AI Studio con el modelo **Gemini 3.1 Flash TTS Preview**, voz Sulafat y un **Audio Profile** porteño (sh en ll/y, s aspirada, melodía italiana, voseo) + Scene en Buenos Aires. Pace en **Natural**, porque el default leía lento.
- Guion 1 corregido: **"Me operaron la rodilla" → "Me operé de la rodilla"** (el TTS pronunciaba "operaron" raro). Cambiado también en `OUTPUTS/2026-10-22-guiones-pilates-sin-vueltas-v2.md`.
- **PSV-V1 a PSV-V6 remontados** (62 a 69 s, 19 a 22 planos). Las voces viejas quedaron en `work/vo/V1_neutro.wav.bak` y el `usage.json` anterior en `usage.json.bak`.
- Dos hallazgos nuevos en `WIKI/vsl-reglas-de-armado.md` y `WIKI/pilates-sin-vueltas.md`: con el modelo 3.1 **el botón Download ya baja el WAV** (no hace falta receptor local) y **hay que confirmar que cada generación arrancó** — la mitad de los envíos no disparó y el Download bajó de nuevo el audio anterior, sin aviso. Se detectó comparando md5 y transcribiendo con Whisper.

## 2026-10-23 — Atlas de Cortes: AT-V14, el UGC con avatar de HeyGen

- **AT-V14.mp4** (34,5 s, 12 planos) terminado: avatar "Emily Carter - Cutting Atlas" con voz Annie - Lifelike, generado en HeyGen y bajado con el botón de descarga de la tarjeta (el `fetch` al `<video>` falla por CORS).
- Nuevo editor **`OUTPUTS/scripts-vsl/edit_atlas_avatar.py`**: la base es el video del avatar y se corta a B-roll o al producto solo en las palabras marcadas. Video y audio se aceleran juntos (1,08) para no romper el lipsync; mantiene subtítulos fucsia, chips y placa final del Atlas. Plan en `work/plans/gen14.py` + `V14.json`, guion en `work/vo/V14.txt`.
- Regla nueva en `WIKI/atlas-de-cortes.md`: antes de anclar un chip hay que buscar la palabra en todo el guion. "Nobody ever noticed" salía en el segundo 1 porque "noticed" también está en la primera frase; se arregla con `occ`.

## 2026-10-23 — Atlas de Cortes: tanda de 3 y dos videos terminados

- Se eligieron los 3 mejores de la v10–v15: V10 ("same as last time"), V12 ("scissors in the air") y V14 (UGC con avatar, variable del V6).
- **AT-V10.mp4** (29,1 s) y **AT-V12.mp4** (36,5 s) hechos con voz Sulafat y `edit_atlas.py`. Planes nuevos en `work/plans/gen.py`.
- Nuevo: `OUTPUTS/2026-10-23-guion-ugc-avatar-atlas.md` con el guion UGC en primera persona y el prompt de la imagen base del avatar de HeyGen.
- Mejora del editor: opción **`noflip`** en `edit_atlas.py` para los clips con números o texto en pantalla (el ángulo "45" salía espejado). Anotado en `WIKI/atlas-de-cortes.md`.

## 2026-10-23 — Atlas de Cortes: análisis de los ads que venden y tanda v10 a v15

- Santiago pasó la captura de los 10 conjuntos activos del Women's Cutting Atlas (~23 compras, ~390 USD, frecuencia 1,08–1,16).
- Se sumó a `WIKI/atlas-de-cortes.md` la sección **Resultados reales de la cuenta** con la tabla CJTO por CJTO y el diagnóstico: vende el momento de fricción concreto durante el servicio; el ángulo de plata (V4 y V5) rinde la mitad; V6 (prueba social, la carpetita) es el sleeper; sub-segmentar (V9 rizado) y la foto de Pinterest no venden.
- Nuevo: `OUTPUTS/2026-10-23-guiones-atlas-cortes-v10-v15.md`, 6 variables EN + ES con momento, mecanismo y CTA propios, más banco de 3 ángulos.
- Pendiente: pedirle a Santiago los guiones de los CJTO 10, 11 y 12 (no son nuestros y los 10 y 12 son los de mejor CPA).

## 2026-10-23 (tarde II) — Natives 22 y 23 de piedras

- Eligió la 2 y la 8 de las diez opciones. `OUTPUTS/2026-10-23-natives-piedras-22-y-23.md`, 1.528 palabras cada una, solo en inglés.
- Primeras natives escritas con la arquitectura de Thrift AI: abren con un objeto (una piedra vieja en el cajón de una mesa de luz, un mail de rechazo pegado dentro de un armario), el método lo trae una mujer de 34, la demo dice primero lo que está mal y después lo que va, los números son chicos (180 y 140 el primer mes) y el cierre vuelve a la imagen del principio.
- **Voz nueva en cada una** (Cheryl, 57, Zanesville OH y Brenda, 58, Elkhart IN) en vez de Emma Carter: las cuatro ganadoras del nicho usan un nombre y un pueblo distintos por native, y Emma ya es expositora de feria en nuestras natives, así que la 23 se contradecía.

## 2026-10-23 (tarde) — Natives: relevamiento del nicho y 10 opciones nuevas

- **Corrección de Santiago:** rechazó las 5 ideas de natives que le propuse de mi propio banco. "Ponete a investigar las mejores natives del nicho". Regla nueva en `WIKI/natives-ganadoras.md`: las ideas se modelan de la Ads Library del nicho, no se inventan.
- **Relevamiento:** página **Side Hustle Radar** (780046011848027), ~75 ads activos del producto **Thrift AI**, bajada con el truco de Chrome headless `--dump-dom`. Cuatro natives de 1.500 a 2.500 palabras, mismo avatar que el nuestro, con una arquitectura de 12 pasos documentada en `OUTPUTS/2026-10-23-analisis-natives-ganadoras-nicho-thrift-ai.md`.
- **Hallazgo central:** abren con una pérdida y un objeto que no se entiende, nunca con la cifra; el método lo trae siempre un tercero más joven; los números son chicos (340 el primer mes) y van con un bloque de honestidad; el cierre vuelve a la imagen del principio y el CTA es una línea sola. Nuestras tres ganadoras hacen lo contrario en cuatro de esos puntos.
- **Entregado:** `OUTPUTS/2026-10-23-natives-piedras-10-opciones-v4.md`, 10 situaciones con esa arquitectura para que elija.

## 2026-10-23 — Piedras: tanda v21 de guiones

- **Entregado:** `OUTPUTS/2026-10-23-guiones-piedras-v21-ingresos.md`, 6 guiones EN + ES de 56 a 63 s (23/10 - 1 a 6).
- Seis ángulos que no estaban usados, todos en el carril de ingresos extra que pidió el 21/10: demanda del local por encima de la capacidad, un pedido grande que cubre un gasto fijo, la reposición mensual como ingreso recurrente, vender sin mostrar la cara, la jubilada de 61 y la cuenta del riesgo real de probar.
- Estructura y CTA propios en cada uno, y los números tomados de la landing (yeso, menos de $15 para arrancar, 40-60 piedras por noche de vertido, $6 por mayor, pedido de casamiento de 120 piezas).
- `WIKI/scented-stones.md`: marcadas como usadas las ideas de próxima tanda que entraron en esta v21 y las que siguen libres.

## 2026-10-22 (tarde III) — The Group Work Playbook: la descripción definitiva

- Pidió **una** descripción para los ads (no una tanda). `OUTPUTS/2026-10-22-descripcion-ads-group-work-playbook-definitiva.md`, EN + ES, con el molde que ya usamos en el Atlas de Cortes: verdad del avatar → el momento del documento en blanco → reframe → una ficha por dinámica con bullets de íconos → los 5 bonos → frase de estado nuevo → CTA sin precio.
- Ángulo elegido: **saber sostener un grupo ≠ tener la hora armada**. Sirve para los seis videos de la tanda, así que reemplaza a las 9 descripciones anteriores como primary text por defecto.
- Sin frases repetidas de `2026-10-22-descripciones-ads-group-work-playbook.md` ni de su v2.

## 2026-10-22 (tarde II) — Pilates sin Vueltas: guiones v2 y los 6 videos

- **Corrección de Santiago:** los guiones v1 copiaban la plantilla fija del competidor. Regla nueva en `WIKI/guiones-y-anuncios.md`: se modela **el ángulo ganador**, no la plantilla; cada guion con estructura y cierre propios.
- **Guiones v2:** `OUTPUTS/2026-10-22-guiones-pilates-sin-vueltas-v2.md`. Seis variables del ángulo "la alumna que te rompe la clase", de 69 a 74 s.
- **Videos:** pipeline de [[group-work-playbook]] reusado (`edit_gwp.py` + `gen_pilates_plans.py` nuevo) en `~/Desktop/pilates-sin-vueltas/anuncios/work/`. Cero créditos: voz de AI Studio, b-roll de Mixkit (serie 48544-48567, estudio de reformers en 1080p) y las fichas de la propia landing.
- **Aprendizajes nuevos** anotados en `WIKI/pilates-sin-vueltas.md`: la interfaz de AI Studio cambió (no hay Scene ni persona, el acento va en **Style**), las voces en español son de pago, los anchors llevan tilde y qué clips sirven para abrir.

## 2026-10-22 — Pilates sin Vueltas: relevamiento de Centerline Pilates y tanda 1

- **Oferta nueva:** `WIKI/pilates-sin-vueltas.md`. Biblioteca de clases **para instructoras** (no para alumnas: no confundir con [[pilates-hormonal]]). Clon de **Centerline Pilates**, 41 anuncios activos en inglés sobre ImpulTienda .ar a US$ 27.
- **Relevamiento:** 38 videos descargados y transcriptos con faster_whisper desde la Ads Library (page 998425433348426). Hallazgo central: el 1/10 corrían cortos de 30 s, y la tanda del 20/10 son 10 videos de ~2 minutos, todos con la misma DNA de "alumna imposible". Abandonaron el formato corto.
- **Entregado:** `OUTPUTS/2026-10-22-guiones-pilates-sin-vueltas.md` — 6 guiones en voseo de 1:19 a 1:26, uno por escena, más el primary text y un banco de 4 ángulos.
- **Reglas nuevas:** tope de **1:30 por video** en `WIKI/guiones-y-anuncios.md` y `WIKI/como-trabajar-con-santiago.md`.
- **Competencia detectada:** ClaseLista · Para Instructoras, 3 ads desde el 12/10 en español, 150 clases por US$ 9,90. A revisar en 2 o 3 días.
- Carpeta `~/Desktop/pilates-sin-vueltas/` creada con `imagenes/`, `landing/` y `anuncios/`.

## 2026-10-22 (tarde II) — Atlas de Cortes: 3 variables de los dos ganadores

- Santiago avisó que de la tanda del 21/10 los que mejor rindieron son **V2 ("Ever finish a cut and one side came out different?")** y **V3 ("You're halfway through the cut…")**. Queda anotado en la wiki como la DNA a variar en esta oferta.
- Tres variables nuevas con esa onda y situación, mecanismo y CTA propios: **AT-V7** (viernes a la noche mirando tutoriales), **AT-V8** (el corte salió bárbaro pero llevó una hora cuarenta) y **AT-V9** (se secó y el rulo subió). De 28 a 29 s, voz Sulafat, misma edición.
- Guiones en `OUTPUTS/2026-10-22-guiones-atlas-cortes-v7-v9-variables.md`; videos en `~/Desktop/atlas-cortes/`.

## 2026-10-22 (tarde) — The Group Work Playbook: análisis de cero con el audio del competidor

- **Relevado de nuevo** el competidor (page 1423115024221032) sin la extensión de Chrome, que estuvo caída casi todo el rato: Chrome headless clásico con `--dump-dom` para la Ads Library, `curl` para los videos, `faster_whisper` para el audio y `ffmpeg` para los frames. El método quedó anotado en la wiki.
- **Transcriptos los 9 videos ganadores.** Hasta ahora nadie había escuchado el audio del competidor: los guiones de la v1 y la v2 se habían escrito solo desde el hook. Quedó la receta real de 6 bloques.
- **Relevada la edición frame por frame.** Corrige dos cosas que estaban mal en la wiki: el chip calificador es blanco, no amarillo, y los subtítulos van en texto blanco sin caja, no en caja violeta.
- **Nueva tanda de 6 guiones de voz en off** (EN + ES voseo), calcados a la receta del competidor, de 28 a 31 s: `OUTPUTS/2026-10-22-guiones-group-work-playbook-v3-voz-en-off.md`.
- **`edit_gwp.py` y `gen_gwp_plans.py` alineados a la edición real** y validados con un render de prueba: chip blanco desde el frame 0, hook en cajas violetas una por línea, subtítulos sin caja que arrancan al irse el hook, más peso de producto que de b-roll, y b-roll curado (fuera los clips corporativos y los que cambian de escena después del segundo 5).
- **Los 6 videos montados**: `~/Desktop/the-group-work-playbook/anuncios/GWP-V1.mp4` a `GWP-V6.mp4`, de 25 a 30 s. Voces de AI Studio (Sulafat) verificadas una por una contra su guion.
- Anotado en la wiki cómo sacar el audio de AI Studio, que fue lo que más costó (CSP, clipboard y descargas bloqueadas).

# Changelog

## 2026-10-22 — The Group Work Playbook: pipeline de video con la edición del competidor
- **Pedido de Santiago:** "la original hace todo con voz en off… la edición tiene que ser similar a la de la original también, la idea es utilizar lo que ya funciona".
- **Relevado:** frame de apertura del ad #1 de Talleres Listos (b-roll de stock, chip amarillo calificador arriba, hook en cajas violetas, chip blanco con el claim). Anotado en `WIKI/group-work-playbook.md` con lo que quedó sin verificar.
- **Creado:** `OUTPUTS/scripts-vsl/edit_gwp.py` (copia de edit_herrero.py con esa paleta), `~/Desktop/the-group-work-playbook/anuncios/work/gen_gwp_plans.py` + los 6 `plans/V*.json`, los 6 `vo/V*.txt` y los stills de la landing en `landing/`.
- **Falta para montar:** las 6 voces en inglés (.wav) y el b-roll de talleres.

## 2026-10-22 — Regla fija: máximo 6 videos por tanda
- **Pedido de Santiago:** "son un montón, te voy a dar otra regla para que te la guardes, siempre son máximo 6 videos, nunca son más. Elegí los mejores 6 y hacelos".
- **Cambiado:** `WIKI/guiones-y-anuncios.md` (registro de preferencias) y `WIKI/como-trabajar-con-santiago.md` (reemplaza el viejo "5 a 10 anuncios por tanda").
- **Aplicado:** la tanda de The Group Work Playbook bajó de 10 a 6 guiones (9, 10, 12, 14, 17 y 18); los 4 descartados quedaron como banco al final del archivo. Las 6 descripciones se reparearon con los 6 videos.

## 2026-10-22 — The Group Work Playbook: análisis del competidor y tanda completa
- **Pedido de Santiago:** "hacé el mismo análisis que venís haciendo siempre para detectar los mejores anuncios. Y después armar todos los anuncios".
- **Analizado:** Facebook Ads Library de Talleres Listos (page 1423115024221032, ~160 ads activos) ordenada por impresiones totales, y la landing propia en inglés.
- **Creado:** `OUTPUTS/2026-10-22-analisis-ads-talleres-listos.md` (ranking de 16 ganadores + 5 patrones + 5 huecos), `OUTPUTS/2026-10-22-guiones-group-work-playbook-v2.md` (10 guiones EN + ES), `OUTPUTS/2026-10-22-descripciones-ads-group-work-playbook-v2.md` (6 primary text EN + ES), `OUTPUTS/2026-10-22-natives-group-work-playbook.md` (10 natives en inglés), `WIKI/group-work-playbook.md`.
- **Cambiado:** `WIKI/index.md`.
- **Carpeta:** `~/Desktop/the-group-work-playbook/` con `imagenes/`, `landing/` y `anuncios/`.

## 2026-10-22 — Atlas de Cortes: descripción de ads definitiva
- **Pedido de Santiago:** "dame la descripción para la de pelo".
- **Creado:** `OUTPUTS/2026-10-22-descripcion-ads-atlas-cortes.md` (EN + ES) y copia en `~/Desktop/atlas-cortes/descripcion-ads.md`.
- **Cambiado:** `WIKI/atlas-de-cortes.md`, `WIKI/index.md`.

## 2026-10-22 — Herrero de Finde: videos v2 con más ritmo
- **Corrección de Santiago:** "está medio aburrida".
- **Cambiado:** `OUTPUTS/scripts-vsl/edit_herrero.py` (música de sus ads, zoom y golpe en cada corte, destello + whoosh, placas que saltan, sello VENDIDA, barra de progreso), `anuncios/work/plans/gen.py`, los 6 `HF-V*.mp4` re-renderizados, `WIKI/herrero-de-finde.md` (cómo se arman + registro de correcciones).

## 2026-10-22 — Herrero de Finde: 6 videos de voz en off
- **Pedido de Santiago:** "armame los videos" (los 6 guiones aprobados).
- **Creado:** `~/Desktop/herrero-de-finde/anuncios/HF-V1…V6-*.mp4`, `OUTPUTS/scripts-vsl/edit_herrero.py`, `anuncios/work/plans/gen.py`.
- **Cambiado:** `WIKI/herrero-de-finde.md` (cómo se arman).

## 2026-10-22 — Herrero de Finde: análisis de 180 ads y 6 guiones
- **Pedido de Santiago:** analizar a fondo sus +300 ads, encontrar patrones (hooks y ediciones que repiten) y hacer 6 de voz en off con B-roll, traducidos casi igual.
- **Creado:** `OUTPUTS/2026-10-22-guiones-herrero-de-finde.md`, carpeta `~/Desktop/herrero-de-finde/anuncios/work/`.
- **Cambiado:** `WIKI/herrero-de-finde.md`.

## 2026-10-22 — Herrero de Finde: botones al carrito
- **Pedido de Santiago:** "yo quiero que vaya directo al carrito" (el permalink `/cart/variante:1` salteaba el carrito).
- **Cambiado:** `herrero-de-finde-shopify.liquid` (`/cart/add.js` → `/cart`), `WIKI/herrero-de-finde.md`, `WIKI/shopify-y-checkout.md`.

## 2026-10-22 — Herrero de Finde: versión Liquid para Shopify
- **Pedido de Santiago:** paso a paso para cargar la landing en Shopify.
- **Creado:** `~/Desktop/herrero-de-finde/landing/herrero-de-finde-shopify.liquid` e imágenes con prefijo `hdf-` en `imagenes/`.
- **Cambiado:** `WIKI/herrero-de-finde.md`.

## 2026-10-22 — Herrero de Finde: hero centrado
- **Pedido de Santiago:** "los primeros textos, que estén alineados al centro".
- **Cambiado:** landing (`~/Desktop/herrero-de-finde/landing/` y `OUTPUTS/2026-10-22-landing-herrero-de-finde.html`), `WIKI/herrero-de-finde.md`, `WIKI/quizzes-reglas-de-armado.md`.

## 2026-10-22 — Regla: una carpeta por oferta en el Escritorio
- **Pedido de Santiago:** cada oferta en su carpeta con `imagenes/`, `landing/` y `anuncios/`, sin nada suelto.
- **Cambiado:** `WIKI/como-trabajar-con-santiago.md`, `WIKI/quizzes-reglas-de-armado.md` (§8), `WIKI/herrero-de-finde.md`. Herrero de Finde reordenado en `~/Desktop/herrero-de-finde/`.

## 2026-10-22 — Herrero de Finde: landing en español (clon de The Weekend Fabricator)
- **Pedido de Santiago:** analizar la oferta en inglés de The Weekend Fabricator y armar la página en español para Argentina.
- **Creado:** `WIKI/herrero-de-finde.md`, `OUTPUTS/2026-10-22-landing-herrero-de-finde.html`.
- **Cambiado:** `WIKI/index.md`.

## 2026-10-22 — Women's Cutting Atlas: super prompt para otro Claude
- **Pedido de Santiago:** prompt con todo el contexto de la oferta del pelo y de cómo se editaron los videos.
- **Creado:** `OUTPUTS/2026-10-22-super-prompt-atlas-cortes.md`.
- **Cambiado:** `WIKI/index.md`.

## 2026-10-22 — Scented Stones: natives 20 y 21 (opciones v2, 4 y 8)
- **Pedido de Santiago:** "4 y 8".
- **Creado:** `OUTPUTS/2026-10-22-natives-piedras-curso-y-cartero.md` (solo inglés).
- **Cambiado:** `WIKI/natives-ganadoras.md`, `WIKI/index.md`.

## 2026-10-22 — Scented Stones: opciones v2 para natives
- **Pedido de Santiago:** "dame opciones y yo elijo".
- **Creado:** `OUTPUTS/2026-10-22-natives-piedras-opciones-v2.md` (a la espera de que elija).
- **Cambiado:** `WIKI/index.md`.

## 2026-10-22 — Scented Stones: guiones v20 con hooks ganadores investigados
- **Pedido de Santiago:** "quiero que sean ganadores, investigá hooks ganadores en el nicho".
- **Investigado:** Virlo (hooks virales con vistas), OpusClip, Webtonic, Gethookd.
- **Creado:** `OUTPUTS/2026-10-22-guiones-piedras-v20-hooks-ganadores.md` (EN + ES).
- **Cambiado:** `WIKI/hooks.md` (sección de investigación), `WIKI/index.md`.

## 2026-10-21 — Meta Ads: reglas de armado del anuncio
- **Corrección de Santiago:** sacar "Anuncios multianunciante"; el texto va separado: texto principal = descripción, título = "Tap the button below", descripción = 5 estrellas.
- **Cambiado:** `WIKI/claude-con-meta-ads.md` (sección "Reglas de armado del anuncio": multianunciante, campos de texto, IA de Meta apagada, error de Threads #4588023, cuenta Reset FIT sin conector).

## 2026-10-21 — Women's Cutting Atlas: V2 rehecho
- **Corrección de Santiago:** "el 2 es igual al 1, hacémelo distinto".
- **Cambiado:** `OUTPUTS/2026-10-21-guiones-atlas-cortes.md` (Guion 2 nuevo: "un lado te quedó distinto al otro"), `~/Desktop/atlas-cortes/AT-V2.mp4`, `WIKI/guiones-y-anuncios.md` (registro), `WIKI/atlas-de-cortes.md`.

## 2026-10-21 — Women's Cutting Atlas: 6 videos producidos
- **Pedido de Santiago:** mandó los mockups del pack y de la colección para hacer los videos.
- **Creado:** `OUTPUTS/scripts-vsl/edit_atlas.py` (editor con la estética del competidor) y los videos `~/Desktop/atlas-cortes/AT-V1..V6.mp4`.
- **Cambiado:** `WIKI/atlas-de-cortes.md` (cómo se arma un video, fuentes de B-roll y activos).

## 2026-10-21 — Women's Cutting Atlas: landing leída y guiones ajustados
- **Pedido de Santiago:** "Acá te dejo la info de mi página, agarrá todo de ahí" (HTML de la landing).
- **Cambiado:** `WIKI/atlas-de-cortes.md` (ficha de la landing: nombre, Cut Maps, oferta y bonus), `OUTPUTS/2026-10-21-guiones-atlas-cortes.md` (6 guiones con los términos del producto), `WIKI/index.md`.

## 2026-10-21 — Atlas Visual de Cortes: oferta nueva y 6 guiones
- **Pedido de Santiago:** ads en inglés a partir de los ganadores de Estilismo Con Propósito (los que llevan más tiempo y los más duplicados): 4 como los de ellos y 2 variables nuestras.
- **Creado:** `WIKI/atlas-de-cortes.md` (DNA de 13 videos transcritos), `OUTPUTS/2026-10-21-guiones-atlas-cortes.md` (6 guiones, EN + ES con voseo).
- **Cambiado:** `WIKI/index.md`.

## 2026-10-21 — Scented Stones: natives 18 y 19 (situaciones 1 y 6)
- **Pedido de Santiago:** "Vamos con la 1 y la 6".
- **Creado:** `OUTPUTS/2026-10-21-natives-piedras-ortodoncia-y-periodista.md` (solo inglés, 1.006 y 928 palabras).
- **Cambiado:** `WIKI/natives-ganadoras.md`, `WIKI/index.md`.

## 2026-10-21 — Scented Stones: 10 situaciones nuevas para natives
- **Pedido de Santiago:** "quiero natives nuevas, no quiero más las de siempre, dame 10 situaciones solamente".
- **Creado:** `OUTPUTS/2026-10-21-natives-piedras-10-situaciones.md` (a la espera de que elija).
- **Cambiado:** `WIKI/index.md`.

## 2026-10-21 — Scented Stones: guion 1.000 al mes, corregido
- **Corrección de Santiago:** "quiero el mismo que el anterior pero solo con 1000".
- **Cambiado:** `OUTPUTS/2026-10-21-guion-piedras-1000-al-mes.md` (vuelve a la estructura del 1 de la v19), `WIKI/guiones-y-anuncios.md`, `WIKI/index.md`.

## 2026-10-21 — Scented Stones: guion 1.000 al mes (rehecho del 1 de la v19)
- **Pedido de Santiago:** "no compares tres números, hacelo solo con 1000 y aportá valor".
- **Creado:** `OUTPUTS/2026-10-21-guion-piedras-1000-al-mes.md` (EN + ES).
- **Cambiado:** `WIKI/guiones-y-anuncios.md` (registro de preferencias), `WIKI/index.md`.

## 2026-10-21 — Scented Stones: guiones v19 (nicho ingresos extra)
- **Corrección de Santiago a la v18:** "apuntá más a guiones del nicho generar ingresos, me estás haciendo situaciones que no traen el público que quiero".
- **Creado:** `OUTPUTS/2026-10-21-guiones-piedras-v19-ingresos.md` (EN + ES).
- **Cambiado:** `WIKI/guiones-y-anuncios.md` (registro de preferencias: público de ingresos extra), `WIKI/index.md`.

## 2026-10-21 — Scented Stones: guiones v18 (6 ángulos nuevos)
- **Pedido de Santiago:** "Vamos con mas guiones para piedras".
- **Creado:** `OUTPUTS/2026-10-21-guiones-piedras-v18.md` (EN + ES).
- **Cambiado:** `WIKI/index.md`.

## 2026-10-20 — Corrección: no generar tandas sin pedido
- **Corrección de Santiago:** "¿Por qué me hacés 11 videos si te dije 2?".
- **Cambiado:** `WIKI/guiones-y-anuncios.md` (registro de preferencias).

## 2026-10-20 — Scented Stones: 6 videos UGC v3 (variables de los videos 1 y 2)
- **Pedido de Santiago:** le gustaron el 1 (pedido para boutique) y el 2 (tres errores).
- **Creado:** `OUTPUTS/2026-10-20-guiones-piedras-ugc-avatar-v3.md` (EN + ES) y `~/Desktop/scented-stones-ad/SS-UGC-v3-*.mp4`.
- **Cambiado:** `WIKI/guiones-y-anuncios.md` (registro de preferencias), `WIKI/index.md`.

## 2026-10-20 — Scented Stones: 5 videos UGC con PERRITA RICA
- **Pedido de Santiago:** más videos con el avatar de la oferta, buena edición, variedad de formatos, efectos de sonido y que sean entretenidos.
- **Creado:** `OUTPUTS/2026-10-20-guiones-piedras-ugc-avatar-v2.md` (EN + ES) y `~/Desktop/scented-stones-ad/SS-UGC-1..5-*.mp4`.
- **Cambiado:** `OUTPUTS/scripts-vsl/sfx.py` (buzzer, redoble, tic-tac, lápiz), `OUTPUTS/scripts-vsl/edit_ugc_pip.py` (efecto sin headline), `WIKI/vsl-reglas-de-armado.md`, `WIKI/index.md`.

## 2026-10-20 — Natives piedras feria v6
- **Pedido de Santiago:** más natives.
- **Creado:** `OUTPUTS/2026-10-20-natives-piedras-feria-v6.md` (natives feria 15, 16 y 17, de 900 a 970 palabras).
- **Cambiado:** `WIKI/index.md`, `WIKI/natives-ganadoras.md`.

## 2026-10-20 — Guiones piedras v17 (virales)
- **Pedido de Santiago:** más guiones, mejores y más virales.
- **Creado:** `OUTPUTS/2026-10-20-guiones-piedras-v17-virales.md`.
- **Cambiado:** `WIKI/index.md`.

## 2026-10-20 — Guiones piedras v16
- **Pedido de Santiago:** más guiones para piedras.
- **Creado:** `OUTPUTS/2026-10-20-guiones-piedras-v16.md`.
- **Cambiado:** `WIKI/index.md`.

## 2026-10-19 — Infinity 3D: descripciones para ads
- **Creado:** `OUTPUTS/2026-10-19-descripciones-ads-infinity-3d.md` (3 descripciones, EN + ES).
- **Cambiado:** `WIKI/infinity-3d.md`.

## 2026-10-19 — Infinity 3D: arreglo de audio cortado y video trabado
- **Pedido de Santiago:** los videos le gustaron, pero el audio se corta y algunos se ven trabados.
- **Cambiado:** `OUTPUTS/scripts-vsl/edit_infinity.py` (recorte de silencios suave, sin zoom en los clips y zoom de fotos al doble de resolución), los 6 videos rehechos y `WIKI/infinity-3d.md` (registro de correcciones).

## 2026-10-19 — Infinity 3D (mesas infinitas EN): 6 videos
- **Pedido de Santiago:** pasar al inglés su oferta de mesas (página Infinity 3D), con 6 videos parecidos a los suyos, no iguales, editados con su mismo estilo, usando 7 TikToks como B-roll y rotándolos.
- **Creado:** `WIKI/infinity-3d.md`, `OUTPUTS/2026-10-19-guiones-infinity-3d-en.md` (EN + ES), `OUTPUTS/scripts-vsl/edit_infinity.py` y `~/Desktop/mesas-resina/IN-V1..V6.mp4`.
- **Cambiado:** `WIKI/index.md`.

## 2026-10-19 — Pan Sin Picos: videos 4 a 6 con voces de Google AI Studio
- **Pedido de Santiago:** 3 videos más, con las voces de Google AI Studio.
- **Creado:** `OUTPUTS/2026-10-19-guiones-pan-sin-picos-v2.md` y `~/Desktop/pan-sin-picos/PSP-Ad4..6.mp4`.
- **Cambiado:** `WIKI/vsl-reglas-de-armado.md` (§0b, voces con AI Studio), `WIKI/pan-sin-picos.md`, `WIKI/index.md`.

## 2026-10-19 — Pan Sin Picos: 3 videos de voz en off (v1)
- **Pedido de Santiago:** anuncios para la oferta de diabetes con sus visuales (6 videos de recetas en un zip), variables mejores que los ads top de Mesa y Sabor, 3 videos.
- **Creado:** `OUTPUTS/2026-10-19-guiones-pan-sin-picos-v1.md`, `OUTPUTS/scripts-vsl/edit_voclips.py` y `~/Desktop/pan-sin-picos/PSP-Ad1..3.mp4` + `guiones-ads.md`.
- **Cambiado:** `WIKI/pan-sin-picos.md` (sección Anuncios con el análisis de sus ads), `WIKI/index.md`.

## 2026-10-19 — Bachas de concreto: video UGC con Mark Ross
- **Pedido de Santiago:** armar el video con la avatar de HeyGen "Mark Ross", con buena edición (pantalla dividida, avatar chiquito sin fondo, etc.).
- **Creado:** `~/Desktop/bachas-concreto/BC-UGC-Mark-Ross.mp4` y la carpeta `work-mark/`.
- **Cambiado:** `WIKI/bachas-de-concreto.md`.

## 2026-10-19 — Bachas de concreto: guion UGC para la avatar Mark Ross
- **Pedido de Santiago:** guion tipo UGC para la avatar de HeyGen "Mark Ross".
- **Creado:** `OUTPUTS/2026-10-19-guion-ugc-mark-ross-bachas.md`.
- **Cambiado:** `WIKI/bachas-de-concreto.md`, `WIKI/index.md`.

## 2026-10-19 — Bachas de concreto: videos B3 y B5
- **Pedido de Santiago:** armar con buena edición el B3 y el B5 (después viene uno con avatar).
- **Creado:** `~/Desktop/bachas-concreto/BC-B3-estres-y-vecino.mp4` y `BC-B5-garaje-de-papa.mp4` (voz Knox, 4 TikToks nuevos de B-roll).
- **Cambiado:** `OUTPUTS/scripts-vsl/edit_broll.py` (anchors: plano según la palabra), `WIKI/bachas-de-concreto.md`.

## 2026-10-19 — Bachas de concreto: variables B3 a B7 del ganador
- **Pedido de Santiago:** al Guion B ("What started…") le va muy bien (4 ventas); hacer variables con la misma estructura y el mismo ángulo.
- **Creado:** `OUTPUTS/2026-10-19-variables-bachas-B-what-started.md` (B3 a B7, en inglés y español).
- **Cambiado:** `WIKI/bachas-de-concreto.md` (ganador y su estructura), `WIKI/index.md`.

## 2026-10-19 — Natives piedras feria v5
- **Pedido de Santiago:** más natives.
- **Creado:** `OUTPUTS/2026-10-19-natives-piedras-feria-v5.md` (natives feria 12, 13 y 14, de 900 a 970 palabras).
- **Cambiado:** `WIKI/index.md`, `WIKI/natives-ganadoras.md`.

## 2026-10-19 — Guiones piedras v15 (ángulos nuevos)
- **Pedido de Santiago:** la v14 eran todos parecidos, con el mismo CTA; innovar con ángulos nuevos.
- **Creado:** `OUTPUTS/2026-10-19-guiones-piedras-v15-angulos-nuevos.md`.
- **Cambiado:** `WIKI/index.md`, `WIKI/guiones-y-anuncios.md` (regla nueva).

## 2026-10-19 — Guiones piedras v14
- **Pedido de Santiago:** más guiones para piedras.
- **Creado:** `OUTPUTS/2026-10-19-guiones-piedras-v14.md`.
- **Cambiado:** `WIKI/index.md`.

## 2026-10-18 — Pan Sin Picos: link de checkout
- Todos los CTAs de la oferta van a https://pan-sin-picos.impultienda.ar/checkout (con UTMs). Actualizados el .txt, PRUEBA, zip y la ficha de la oferta (WIKI/pan-sin-picos.md).

## 2026-10-18 — Pan Sin Picos: fotos profesionales en el quiz
- **Corrección de Santiago:** "las imágenes son muy malas, me dan ganas de irme del quiz, se ve muy low ticket".
- **Hecho:** 11 fotos con GPT Image 1.5 (Higgsfield) en portada, género, "qué extrañás", recetas recomendadas, receta de regalo, celular y una galería nueva en la oferta. Los electrodomésticos pasan a lista.
- **Cambiado:** `WIKI/quizzes-reglas-de-armado.md` (§4 + registro), `WIKI/pan-sin-picos.md`, `OUTPUTS/2026-10-18-quiz-pan-sin-picos.html`.

## 2026-10-18 — Oferta nueva: Pan Sin Picos (quiz para diabéticos)
- **Pedido de Santiago:** quiz de unas 10 preguntas, lindo y que aporte valor, para vender en Argentina un recetario de panes para diabéticos modelado de Mesa y Sabor (que vende por WhatsApp).
- **Creado:** `WIKI/pan-sin-picos.md`, `OUTPUTS/2026-10-18-quiz-pan-sin-picos.html`. Entregables en `~/Desktop/pan-sin-picos/`.
- **Cambiado:** `WIKI/index.md`.

## 2026-10-18 — Bachas de concreto: B-roll sin repetir, efectos puntuales y 3 variables
- **Correcciones de Santiago:** no repetir B-roll y sacar el whoosh de cada corte (cha-ching en la plata).
- **Cambiado:** `OUTPUTS/scripts-vsl/edit_broll.py` (modo pool con `usage.json`, espejado al reusar, efectos por palabra), `WIKI/bachas-de-concreto.md`, `WIKI/index.md`.
- **Creado:** `OUTPUTS/2026-10-18-variables-bachas-concreto-en.md` (A2, B2 y C2 en inglés y español). Los 6 videos se rehicieron en `~/Desktop/bachas-concreto/`.

## 2026-10-18 — Bachas de concreto: voz de hombre + Mark Ross
- **Corrección de Santiago:** la voz tiene que ser de un hombre de unos 40, y el experto es Mark Ross (se lo puede nombrar).
- **Rehecho:** las 3 voces con Knox (Google AI Studio) y los 3 videos. Mark Ross aparece en A y B ("Mark Ross's method") y en C ("I'm Mark Ross").
- **Cambiado:** `WIKI/bachas-de-concreto.md` (voz, experto, registro de correcciones) y `OUTPUTS/2026-10-18-guiones-bachas-concreto-en.md` (español en masculino).

## 2026-10-18 — Oferta nueva: bachas de concreto (EN)
- **Pedido de Santiago:** traducir al inglés los mejores ads de "Martin Ferreyra" (De Cemento a Negocio) y editarlos con visuales de 7 TikToks, cambiando de plano cada 4–5 s y con voz de Google AI Studio.
- **Creado:** `WIKI/bachas-de-concreto.md`, `OUTPUTS/2026-10-18-guiones-bachas-concreto-en.md`, `OUTPUTS/scripts-vsl/edit_broll.py`. Videos en `~/Desktop/bachas-concreto/`.
- **Cambiado:** `WIKI/index.md`.

## 2026-10-18 — Natives piedras feria v4
- **Pedido de Santiago:** más natives.
- **Creado:** `OUTPUTS/2026-10-18-natives-piedras-feria-v4.md` (natives feria 9, 10 y 11, de 900 a 1.000 palabras).
- **Cambiado:** `WIKI/index.md`, `WIKI/natives-ganadoras.md`.

## 2026-10-18 — Guiones piedras v13
- **Pedido de Santiago:** más guiones para piedras.
- **Creado:** `OUTPUTS/2026-10-18-guiones-piedras-v13.md`.
- **Cambiado:** `WIKI/index.md`.

## 2026-10-17 — Quiz en Shopify
- `WIKI/shopify-y-checkout.md`: cómo subir un quiz HTML pesado como plantilla Liquid (`layout none`, `content_for_header`, imágenes con `file_url`).

## 2026-10-17 — Patitas Felices: variables 4A–4D rehechas
- 4 videos nuevos con guion y visual base distintos, que reemplazan a los anteriores. Voz generada con HeyGen (Karina, voz roma) porque ElevenLabs se quedó sin créditos.
- `WIKI/patitas-felices.md`: resultados y flujo de voz por HeyGen.

## 2026-10-17 — Patitas Felices: corrección de variables
- **Corrección de Santiago:** las variables cambian el guion entero y la visual base, no solo el hook (registrada en `WIKI/patitas-felices.md`).
- **Creado:** `OUTPUTS/2026-10-17-variables-guion-4-patitas.md` (4 variables nuevas del Guion 4).

## 2026-10-17 — Patitas Felices: variables 4C y 4D
- 2 hooks más sobre el cuerpo del Guion 4: 4C (comida de verdad o ultraprocesado) y 4D (texto en pantalla, sin voz). Se usó audio de Roma reciclado porque ElevenLabs se quedó sin créditos.
- `OUTPUTS/2026-10-17-renovacion-guion-4-patitas-v2.md` y `WIKI/patitas-felices.md`.

## 2026-10-17 — Patitas Felices: renovación del Guion 4
- El Guion 4 vendió 2: 2 variables de hook con el mismo cuerpo (4A y 4B), con voz Roma y videos en `~/Desktop/patitas-felices/final/`.
- `OUTPUTS/2026-10-17-renovacion-guion-4-patitas.md` y sección *Resultados* en `WIKI/patitas-felices.md`.

## 2026-10-17 — Secreto de la Insulina: Remix 1 a 6
- **Correcciones de Santiago:** el principio del video no puede ser estático, y todo va en una sola carpeta (sin subcarpetas).
- **Creado:** `OUTPUTS/2026-10-17-videos-secreto-insulina-remix-1-6.md` y los videos SI-Remix1..6 en `~/Desktop/secreto-insulina/`.
- **Cambiado:** `WIKI/secreto-de-la-insulina.md` (registro de correcciones, voces en una sola tirada, carpeta plana), `OUTPUTS/scripts-vsl/edit_remix.py` (zoom más marcado) e `index.md`.

## 2026-10-17 — Native piedras: variable "Ever heard of"
- **Pedido de Santiago:** una variable de la descripción "Ever heard of Scented Aroma Stones?".
- **Creado:** `OUTPUTS/2026-10-17-native-piedras-descripcion-ever-heard.md`.
- **Cambiado:** `WIKI/index.md`.

## 2026-10-17 — Secreto de la Insulina: primer video (remix)
- **Pedido de Santiago:** un video con la opción A (sus visuales), sin HeyGen ni Higgsfield, con una variable del guion.
- **Creado:** `WIKI/secreto-de-la-insulina.md`, `OUTPUTS/scripts-vsl/edit_remix.py`, `OUTPUTS/2026-10-17-video-secreto-insulina-remix-1.md` y el video en el escritorio.
- **Cambiado:** `WIKI/index.md`.

## 2026-10-17 — Quiz Secreto de la Insulina (AR)
- **Pedido de Santiago:** el quiz igual al del competidor validado, en verde, promesa con los kilos deseados en 21 días, peso y altura con barra, $14.990.
- **Creado:** `OUTPUTS/2026-10-17-quiz-secreto-de-la-insulina.html` (+ `.txt`, PRUEBA e imágenes en el escritorio).
- **Cambiado:** `WIKI/quizzes-reglas-de-armado.md` (4 correcciones nuevas: copiar el validado, paleta verde, promesa sin inflar, barras siempre) e `index.md`.

## 2026-10-17 — Caza de ofertas escaladas en Brasil
- **Pedido de Santiago:** ofertas low ticket digitales escaladas (60+ ads, sin marca personal) en emagrecimento y renda extra, en la Ads Library de BR.
- **Creado:** `OUTPUTS/2026-10-17-caza-ofertas-brasil.md` + doc en Claude Docs con la tabla de estadísticas.
- **Cambiado:** `WIKI/index.md` (Outputs).

## 2026-10-17 — Natives Piedras: feria v3
- **Corrección de Santiago:** las natives no tan cortas.
- **Creado:** `OUTPUTS/2026-10-17-natives-piedras-feria-v3.md` (natives 6 a 8, de 900 a 1.200 palabras, solo EN).
- **Cambiado:** `WIKI/natives-ganadoras.md` (cuándo va la corta y cuándo la larga) e `index.md`.

## 2026-10-17 — Guiones Piedras v12 (públicos nuevos)
- **Pedido de Santiago:** apuntar a públicos nuevos porque los de siempre están explotados.
- **Creado:** `OUTPUTS/2026-10-17-guiones-piedras-v12-publicos-nuevos.md` (6 guiones EN/ES, uno por público nuevo).
- **Cambiado:** `WIKI/index.md` (Outputs).

## 2026-10-16 — Patitas Felices: 6 videos en HD
- **Correcciones de Santiago:** visuales en HD, nada de texto en portugués (o traducido) y variar la edición entre anuncios.
- **Cambiado:** `WIKI/patitas-felices.md` (registro de correcciones), `OUTPUTS/scripts-vsl/ad_edit.py` (estilos, insertos, ancla por frase, zoom, barra, título) y `rmsubs.py` (modo `white`).

## 2026-10-16 — Kit Patitas Felices: oferta nueva y primer video
- **Creado:** `WIKI/patitas-felices.md` (análisis de los 55 ads de Tigela Cheia, pipeline y correcciones), `OUTPUTS/2026-10-16-guiones-patitas-felices.md` (9 guiones), `-v2.md` (10 y 11), `OUTPUTS/scripts-vsl/rmsubs.py` y `ad_edit.py`.
- **Correcciones de Santiago:** no repetir la plantilla en una tanda, y voz con silencios recortados a 1.2x.
- **Cambiado:** `WIKI/index.md`.

## 2026-10-16 — Natives Piedras: receta gratis tanda 2
- **Creado:** `OUTPUTS/2026-10-16-natives-piedras-receta-gratis-v2.md` (natives 4 a 6 con prompt de imagen y descripción, solo EN).
- **Cambiado:** `WIKI/index.md` (Outputs).

## 2026-10-16 — Guiones Piedras v11 (receta gratis)
- **Feedback de Santiago:** le gustó el Guion 1 de la v10 ("esa onda").
- **Creado:** `OUTPUTS/2026-10-16-guiones-piedras-v11-receta-gratis.md` (5 variables EN/ES).
- **Cambiado:** `WIKI/guiones-y-anuncios.md` (ángulo que le gustó) e `index.md`.

## 2026-10-16 — Guiones Piedras v10
- **Creado:** `OUTPUTS/2026-10-16-guiones-piedras-v10.md` (5 guiones EN/ES; los 2 primeros pasan a video el ángulo de la native ganadora "receta gratis"; material sal y harina).
- **Cambiado:** `WIKI/index.md` (Outputs).

## 2026-10-15 — Dos videos variables de "I thought" (Scented Stones)
- **Creado:** `~/Desktop/scented-stones-ad/Scented-Stones-Ad-Budget.mp4` (hook "fuera de mi presupuesto") y `Scented-Stones-Ad-12-Dollars.mp4` (hook "12 dólares por una piedra"). Avatar PERRITA RICA (voz roma), edición mixta gs/full/pip con los B-rolls existentes, 4 headlines. Una sola generación de HeyGen por video.
- **Cambiado:** `OUTPUTS/2026-10-15-guion-piedras-i-thought-variable.md` (+ Guion 2), `WIKI/vsl-reglas-de-armado.md` §6 (avatar del ad "I thought" y regla "no gastar créditos de más").

## 2026-10-15 — Guiones Chupetines v10 (virales)
- **Creado:** `OUTPUTS/2026-10-15-guiones-chupetines-v10-virales.md` (5 guiones de ~45 s con hooks de identificación).
- **Cambiado:** `WIKI/index.md` (Outputs).

## 2026-10-15 — Variable del video "I thought" (Scented Stones)
- **Creado:** `OUTPUTS/2026-10-15-guion-piedras-i-thought-variable.md` (transcripción del video `~/Downloads/I thought scented.mp4`, que no estaba registrado, + hook nuevo con el mismo body y CTA, EN/ES).
- **Cambiado:** `WIKI/index.md` (Outputs).

## 2026-10-15 — Quiz Chinese Embroidery: garantía y foto de Juliana
- Garantía rediseñada en la paleta del quiz (tarjeta crema, sello dorado de 112 px, título en Fraunces). La foto redonda de Juliana sale de una versión sin texto, con plano abierto y sin agrandar. Reglas en `WIKI/quizzes-reglas-de-armado.md` §4.

## 2026-10-15 — Quiz Chinese Embroidery: checkout y precio
- Checkout `https://chinese-embroidery.impultienda.ar/checkout` en todos los CTAs (con UTMs). Precio 27 USD en la caja de precio y en el tachado del popup. Registro en `WIKI/quizzes-reglas-de-armado.md`.

## 2026-10-15 — Quiz Chinese Embroidery (Juliana Alves, mercado en inglés)
- **Creado:** `OUTPUTS/2026-10-15-quiz-chinese-embroidery.html`, modelado del quiz brasileño de Bordado Chinês (vivendodebordadochines.lovable.app). Tapa rehecha con Pillow (Juliana Alves), chats de WhatsApp, garantía y pago seguro en HTML en inglés.
- **Cambiado:** `WIKI/quizzes-reglas-de-armado.md` (cómo sacar un quiz de Lovable, localización al inglés, recortes de la tapa editada) e `index.md`.

## 2026-10-15 — Post-pagos de Mounjaro Humilde
- Escalera: Anti-Antojos $14.990 → GPT $29.990 → Rostro $9.990 → Reafirmante $6.990. Reglas para los VSL de OTO en `WIKI/embudo-vsl-post-pago.md` (felicitar solo en el 1.º, encadenados, sin repetir, 4–5 min). Guion del OTO 1 en `OUTPUTS/2026-10-15-vsl-oto1-anti-antojos-guion.md`.

## 2026-10-15 — Natives Piedras: variables de "receta gratis"
- **Creado:** `OUTPUTS/2026-10-15-natives-piedras-receta-gratis.md` (texto de la ganadora, estructura y 2 variables con prompt de imagen, solo EN).
- **Cambiado:** `WIKI/natives-ganadoras.md` (ganadora corta de ~250 palabras) e `index.md`.

## 2026-10-15 — Guiones Piedras v9 (formatos del nicho)
- **Creado:** `OUTPUTS/2026-10-15-guiones-piedras-v9-formatos-del-nicho.md` (resumen de la investigación de formatos de ingresos extra + 6 guiones EN/ES).
- **Cambiado:** `WIKI/index.md` (Outputs).

## 2026-10-15 — Guiones Piedras v8 (que se sientan reflejadas)
- **Creado:** `OUTPUTS/2026-10-15-guiones-piedras-v8-reflejados.md` (5 guiones EN/ES: hooks de identificación + beneficios apilados, precios de la landing).
- **Cambiado:** `WIKI/index.md` (Outputs).

## 2026-10-15 — Quiz Mounjaro Humilde sin el paso del e-mail
- Se saca el paso del e-mail (se pide en el checkout). Nueva regla en `WIKI/quizzes-reglas-de-armado.md`: no pedir datos de contacto en el quiz.

## 2026-10-14 — VSL final de Mounjaro Humilde + VSL de la nutri en el quiz
- Quiz: VSL final de Panda en el último paso, con "QUIERO MI PLAN" al 1:20 hacia el checkout de ImpulTienda.
- Quiz: embed de Panda en el paso 12 (Continuar a los 30 s) y sin audio en la página de resultados. Link actualizado.
- VSL final (1:28): nutri + testimonio de Karina ($19.990) + garantía de 30 días + placa "Tocá en QUIERO MI PLAN". Opciones nuevas en `edit_vsl_quiz.py` y §8 en `WIKI/vsl-reglas-de-armado.md`.

## 2026-10-14 — VSL de la nutri de Mounjaro Humilde
- Video de 42 s con la avatar Nutri Mounjaro (HeyGen) y el mismo guion que el de Brasil, adaptado a voseo. Pantalla dividida con capturas del quiz, B-rolls del té, antes y después, subtítulos de a una palabra y 3 palabras en verde.
- Nuevo script `OUTPUTS/scripts-vsl/edit_vsl_quiz.py` y §7 en `WIKI/vsl-reglas-de-armado.md`.

## 2026-10-14 — Guiones Chupetines v9
- **Corrección de Santiago:** la v8 era "muy corta".
- **Creado:** `OUTPUTS/2026-10-14-guiones-chupetines-v9.md` (5 guiones de ~45 s, estructura del ganador).
- **Cambiado:** `WIKI/guiones-y-anuncios.md` (largo de referencia: el ganador) e `index.md`.

## 2026-10-14 — Guiones Chupetines v8 cortos
- **Corrección de Santiago:** "mejores y sin tanto rollo".
- **Creado:** `OUTPUTS/2026-10-14-guiones-chupetines-v8-cortos.md` (5 guiones de 25-30 s).
- **Cambiado:** `WIKI/guiones-y-anuncios.md` (regla de guiones cortos para chupetines) e `index.md`.

## 2026-10-14 — Guiones Chupetines v7
- **Creado:** `OUTPUTS/2026-10-14-guiones-chupetines-v7.md` (5 guiones con los elementos del ganador "Si hace 6 meses" y ángulos nuevos).
- **Cambiado:** `WIKI/index.md` (Outputs).

## 2026-10-14 — Descripción para ads de Resina Rentable
- **Creado:** `OUTPUTS/2026-10-14-descripcion-resina-rentable.md`.
- **Cambiado:** `WIKI/resina-rentable.md` e `index.md`.

## 2026-10-14 — Quiz Mounjaro Humilde (modelado de "Mounjaro de Pobre", Brasil)
- Quiz completo en español con voseo: `~/Desktop/mounjaro-humilde/` (HTML con imágenes embebidas, .txt, `imagenes/`, `original/`, `trabajo/` con los scripts). Copia: `OUTPUTS/2026-10-14-quiz-mounjaro-humilde.html`.
- Imágenes: tapa nueva con GPT Image 1.5 ("MOUNJARO HUMILDE"); logo, diagrama, HOMBRE/MUJER y DESPUÉS rehechos con Pillow; el resto, del original a 2x.
- VSL vacíos con botón Continuar; botón final a `LINK_CHECKOUT`.
- Ronda 2: zonas (Caderas, sin Flancos), sin marca de agua en "Todavía no sé", barra del IMC en Sobrepeso, y medidores para peso y altura (nueva §4b).
- Correcciones en `WIKI/quizzes-reglas-de-armado.md`: sin la pantalla de elegir WhatsApp/e-mail, y armar más rápido desde el JSON.

## 2026-10-14 — Guiones Chupetines v6
- **Creado:** `OUTPUTS/2026-10-14-guiones-chupetines-v6.md` (5 guiones con los elementos del ganador "Si hace 6 meses" + ángulos de piedras: mes desglosado por canal y "Tres cosas").
- **Cambiado:** `WIKI/index.md` (Outputs; se corrigieron las líneas del UGC con avatar y de las natives de feria).

## 2026-10-14 — Ad de Pilates "sin saltar ni correr" (rodillas)
- **Corrección de Santiago:** visuales que no se noten tan IA; B-rolls nuevos solo si es súper necesario.
- **Creado:** `~/Desktop/pilates-hormonal-ad/Pilates-Hormonal-Ad-Rodillas.mp4` (27 s, pantalla dividida con Caro, B-rolls existentes con look de celular).
- **Cambiado:**
  - `OUTPUTS/scripts-vsl/edit_ugc_pip.py`: modo `split`, `ORGANIC`, recorte por clip, una carpeta de caché por video, headlines como argumento, filtro de palabras inventadas antes del recorte de silencios.
  - `WIKI/vsl-reglas-de-armado.md` §6.

## 2026-10-14 — Guiones UGC Pilates Hormonal v2 (bajar de peso)
- **Creado:** `OUTPUTS/2026-10-14-guiones-ugc-pilates-hormonal-v2.md` (guiones 6 a 10, voz de la experta, foco en pérdida de peso; temas tomados de las keywords de `OUTPUTS/2026-10-12-top10-keywords-bajar-de-peso.md`).
- **Cambiado:** `WIKI/pilates-hormonal.md` e `index.md`.

## 2026-10-14 — Ad de Pilates "mujeres de 60 en Asia" (formato 3)
- **Corrección de Santiago:** variar la edición, sin la avatar chica.
- **Creado:** `~/Desktop/pilates-hormonal-ad/Pilates-Hormonal-Ad-Asia.mp4` (28 s: cortes a B-roll de pantalla completa y Caro recortada en grande delante del B-roll). Lleva 5 B-rolls nuevos de Higgsfield (Kling 2.6, 25 créditos).
- **Cambiado:**
  - `OUTPUTS/scripts-vsl/edit_ugc_pip.py`: modos `full` y `gs`, plan como argumento, descarta palabras inventadas por Whisper.
  - `WIKI/vsl-reglas-de-armado.md` §6.

## 2026-10-14 — Ad orgánico de Pilates Hormonal (cortisol, Caro Pilates)
- **Creado:** `~/Desktop/pilates-hormonal-ad/Pilates-Hormonal-Ad-Cortisol.mp4` (28 s, formato 2: avatar sin fondo en la esquina, B-rolls del VSL, 4 headlines).
- **Cambiado:**
  - `OUTPUTS/scripts-vsl/edit_ugc_pip.py`: idioma como argumento, modelo RVM en la carpeta de trabajo, subtítulos sin "…" ni ":".
  - `WIKI/vsl-reglas-de-armado.md` §6: dónde quedaron los B-rolls de Pilates.

## 2026-10-14 — Guiones UGC Pilates Hormonal con la experta
- **Corrección de Santiago:** en los UGC habla la experta, no alumnas.
- **Cambiado:** `OUTPUTS/2026-10-14-guiones-ugc-pilates-hormonal.md` (5 guiones reescritos en voz de la Maestra Caro) y `WIKI/pilates-hormonal.md` (regla de voz).

## 2026-10-14 — Pilates Hormonal: página en la WIKI + guiones UGC
- **Creado:** `WIKI/pilates-hormonal.md` (ficha juntando VSL, quiz, descripciones y contexto maestro) y `OUTPUTS/2026-10-14-guiones-ugc-pilates-hormonal.md` (5 guiones UGC).
- **Cambiado:** `WIKI/index.md`.

## 2026-10-14 — Ad UGC "orgánico de TikTok" ($2.000 en un mes, Scented Stones)
- **Corrección de Santiago:** variar las ediciones y poner pocos headlines, solo en los puntos importantes ("el efecto de sonido cansa").
- **Creado:**
  - `OUTPUTS/scripts-vsl/edit_ugc_pip.py`: B-roll a pantalla completa con la avatar recortada sin fondo en la esquina, zoom de salto, 4 headlines, subtítulos con la plata en cifras amarillas.
  - `OUTPUTS/scripts-vsl/matte.py`: saca el fondo con Robust Video Matting en ONNX.
  - Video: `~/Desktop/scented-stones-ad/Scented-Stones-Ad-2000-Month.mp4` (41 s).
- **Cambiado:** `WIKI/vsl-reglas-de-armado.md` (§6: corrección de headlines, formato 2 y registro).

## 2026-10-14 — Guion "Así generé más de 2.000 dólares en un mes"
- **Creado:** `OUTPUTS/2026-10-14-guion-piedras-2000-en-un-mes.md` (hook de Santiago + desglose del mes por canal, EN/ES).
- **Cambiado:** `WIKI/index.md` (Outputs).

## 2026-10-14 — Ad UGC con pantalla dividida (Scented Stones, bridal shower)
- **Creado:** `OUTPUTS/scripts-vsl/edit_ugc_split.py` (edición de ad corto: pantalla dividida con degradé, headlines rojos, subtítulos de 2 palabras, pop, cha-ching, whoosh y música). Video: `~/Desktop/scented-stones-ad/Scented-Stones-Ad-Bridal.mp4` (36 s, avatar Adsda con la voz Roma en HeyGen).
- **Cambiado:** `WIKI/vsl-reglas-de-armado.md` (§6 Anuncios UGC con pantalla dividida: estilo de las referencias y receta).

## 2026-10-14 — Corrección: UGC sin "respuesta a comentario"
- **Corrección de Santiago:** no quiere guiones con formato de respuesta a un comentario.
- **Cambiado:** `WIKI/guiones-y-anuncios.md` (registro de preferencias), `OUTPUTS/2026-10-14-guion-piedras-ugc-avatar.md` (v2: caja de pedido para una despedida de soltera).

## 2026-10-14 — Guion UGC con avatar (piedras)
- **Creado:** `OUTPUTS/2026-10-14-guion-piedras-ugc-avatar.md` (formato respuesta a comentario, EN/ES, ~40 s, + prompt de imagen base del avatar en 9:16).
- **Cambiado:** `WIKI/index.md` (Outputs).

## 2026-10-14 — Corrección: natives solo en inglés
- **Corrección de Santiago:** las descripciones de las natives van siempre en inglés, sin versión en español.
- **Cambiado:** `WIKI/natives-ganadoras.md` (plantilla, correcciones y tanda 14/10), `WIKI/como-trabajar-con-santiago.md` (excepción a la regla de idiomas), `OUTPUTS/2026-10-14-natives-piedras-feria-v2.md` (sin las versiones ES).

## 2026-10-14 — Natives de feria v2
- **Creado:** `OUTPUTS/2026-10-14-natives-piedras-feria-v2.md` (natives de feria 3 a 5: el baúl cargado a las 6:40, la planilla de la hija, la planilla de encargos de Navidad). Prompt de imagen 3:4 + descripción EN/ES, continuidad con las de feria del 12/10.
- **Cambiado:** `WIKI/index.md` (Outputs).

## 2026-10-14 — Piedras: "Three things" con hook 2
- **Creado:** `OUTPUTS/2026-10-14-guion-piedras-three-things-hook-2.md` (guion 6: cuerpo del ganador + hook 2, EN/ES).
- **Cambiado:** `WIKI/index.md` (Outputs).

## 2026-10-14 — Piedras: ganador "Three things" + variables
- **Fuente:** video `~/Downloads/Three things.MOV` (transcripto localmente).
- **Creado:** `OUTPUTS/2026-10-14-guiones-piedras-v7-three-things.md` (transcripción, 5 guiones variables EN/ES y 6 hooks).
- **Cambiado:** `WIKI/scented-stones.md` (ganador y su estructura), `WIKI/index.md` (Outputs).

## 2026-10-14 — Guiones Resina Rentable v6
- **Creado:** `OUTPUTS/2026-10-14-guiones-resina-rentable-v6.md` (guiones 21 a 24, apuntados al problema y al objetivo del cliente).
- **Cambiado:** `WIKI/resina-rentable.md` (tandas) e `index.md`.

## 2026-10-14 — Guiones Resina Rentable v5 + regla "la onda, no la copia"
- **Corrección de Santiago:** cuando le gusta un guion quiere esa onda, no guiones iguales.
- **Creado:** `OUTPUTS/2026-10-14-guiones-resina-rentable-v5.md` (guiones 17 a 20).
- **Cambiado:** `WIKI/guiones-y-anuncios.md` (registro), `WIKI/como-trabajar-con-santiago.md` (regla de interacción), `WIKI/resina-rentable.md` (lo que gustó, tandas) e `index.md`.

## 2026-10-13 — Chupetines: ganador "Si hace 6 meses" + variables
- **Fuente:** video `~/Downloads/si hace 6.mov` (transcripto localmente).
- **Creado:** `OUTPUTS/2026-10-13-guiones-chupetines-v5-si-hace-6-meses.md` (transcripción, 5 guiones variables y 8 hooks).
- **Cambiado:** `WIKI/ofertas.md` (ganador y su estructura), `WIKI/index.md` (Outputs).

## 2026-10-13 — Guiones Chupetines v4
- **Creado:** `OUTPUTS/2026-10-13-guiones-chupetines-v4.md` (3 guiones: Día de la Madre con la florería, la anfitriona de cabañas que repone cada viernes, el regalo de cumpleaños que trae pedidos). Siguen la DNA ganadora y el formato limpio.
- **Cambiado:** `WIKI/index.md` (Outputs).

## 2026-10-13 — Guiones Resina Rentable v4 + regla de bodies
- **Corrección de Santiago:** los bodies no pueden ser teoría ni mini-clase; tienen que seguir la DNA ganadora y convertir.
- **Creado:** `OUTPUTS/2026-10-13-guiones-resina-rentable-v4.md` (guiones 13 a 16).
- **Cambiado:** `WIKI/guiones-y-anuncios.md` (registro de preferencias), `WIKI/resina-rentable.md` e `index.md`.

## 2026-10-13 — Guiones Resina Rentable v3
- **Creado:** `OUTPUTS/2026-10-13-guiones-resina-rentable-v3.md`: guiones 9 a 12 con el copy textual de la landing.
- **Cambiado:** `WIKI/resina-rentable.md` (tandas) e `index.md`.

## 2026-10-13 — Guiones Resina Rentable v2
- **Creado:** `OUTPUTS/2026-10-13-guiones-resina-rentable-v2.md`: guion 2 armado con el hook 2 + guiones 5 a 8.
- **Cambiado:** `WIKI/resina-rentable.md` (tandas) e `index.md`.

## 2026-10-13 — Landing Palabras de la Obediencia (Argentina)
- Copia de la landing de VSL de LATAM, con voseo y el VSL de Panda. Sin footer, popup ni back-redirect. Botón verde "COMPRAR AHORA" a los 2:45, que lleva al checkout de ImpulTienda con los UTMs. Archivo: `OUTPUTS/2026-10-13-landing-palabras-de-la-obediencia.html`.

## 2026-10-13 — VSL Las Tres Conexiones (Argentina)
- Guion adaptado del VSL de LATAM ("VSL Mama") con voseo, experta Juliana Alves y precio $15.990: `OUTPUTS/2026-10-13-vsl-tres-conexiones-argentina-guion.md`.
- Avatar nueva en HeyGen y render de 4:20 (84 créditos). B-rolls: 11 recortes de TikTok sin marca de agua, 4 clips de Higgsfield que ya existían y 5 nuevos en Kling 2.6 (25 créditos).
- Script de edición nuevo: `OUTPUTS/scripts-vsl/edit_tres_conexiones.py`. Subtítulos de a una palabra corregidos contra el guion, placas, música con ducking y efectos. Final de 3:02 a 1.3x en `~/Desktop/mama-vsl/`.
- `WIKI/vsl-reglas-de-armado.md`: datos de Juliana, cómo subir archivos a HeyGen y edición del VSL de crianza (§4a).

## 2026-10-13 — Descripciones para ads de Pilates Hormonal
- **Fuentes:** `OUTPUTS/2026-10-12-vsl-pilates-hormonal-guion.md` (mecanismo, avatar y bonos) + reglas de primary text de `WIKI/guiones-y-anuncios.md`.
- **Creado:** `OUTPUTS/2026-10-13-descripciones-pilates-hormonal.md`: 3 primary text cortos con emojis, sin precio, CTA al test gratis de 1 minuto.
- **Cambiado:** `WIKI/index.md` (outputs) y `WIKI/ofertas.md` (Pilates Hormonal está activa otra vez, no es historial).

## 2026-10-13 — Regla: TikToks sin marca de agua
- `WIKI/vsl-reglas-de-armado.md`: los B-rolls de TikTok se bajan sin marca de agua (API tikwm) y se revisan los cuadros.

## 2026-10-13 — Regla: guiones sin B-roll
- **Corrección de Santiago:** tampoco quiere las líneas `[BROLL]` en la entrega; solo el título y el texto que se lee.
- **Cambiado:** `WIKI/como-trabajar-con-santiago.md`, `WIKI/guiones-y-anuncios.md`, `WIKI/resina-rentable.md` y `OUTPUTS/2026-10-13-guiones-resina-rentable.md`.

## 2026-10-13 — Regla: guiones limpios
- **Corrección de Santiago:** sin etiquetas de estructura ni segundos en los guiones; solo **Guion N** en negrita y subrayado y abajo el guion.
- **Cambiado:** `WIKI/como-trabajar-con-santiago.md` (regla de formato), `WIKI/guiones-y-anuncios.md` (registro), `WIKI/resina-rentable.md` y `OUTPUTS/2026-10-13-guiones-resina-rentable.md` (reentregado limpio).

## 2026-10-13 — Guiones Resina Rentable
- **Investigado:** contenido de resina en TikTok (lo que engancha es el proceso y las inclusiones; no hay ranking de hooks) y los errores que nombran los competidores.
- **Creado:** `WIKI/resina-rentable.md` (ficha de la oferta nueva a partir del brief del chat) y `OUTPUTS/2026-10-13-guiones-resina-rentable.md` (4 guiones + 5 hooks alternativos).
- **Cambiado:** `WIKI/index.md`.

## 2026-10-13 — Natives piedras orgánicas
- **Creado:** `OUTPUTS/2026-10-13-natives-piedras-organicas.md`: 3 natives (prompt de imagen + descripción EN y ES) en la línea orgánica del guion "empaquetá un pedido conmigo".
- **Cambiado:** `WIKI/guiones-y-anuncios.md` (preferencia: orgánico gana), `WIKI/natives-ganadoras.md` (tanda 13/10) e `index.md`.

## 2026-10-13 — Guiones piedras v6 (TikTok)
- **Investigado:** formatos virales de TikTok para pequeños negocios. No hay un viral propio de piedras aromáticas (contenido de nicho, hasta ~1.900 likes); se trajeron formatos de otros nichos.
- **Creado:** `OUTPUTS/2026-10-13-guiones-piedras-v6-tiktok.md`: 3 guiones con primer frame ("nunca más compro X", proceso satisfactorio + adiviná el costo, pack an order with me).
- **Cambiado:** `WIKI/index.md`.

## 2026-10-13 — Guiones piedras v5
- **Creado:** `OUTPUTS/2026-10-13-guiones-piedras-v5.md`: 3 guiones originales (inmobiliaria, recompra cada 8 semanas, canasta de la peluquería) con la estructura del guion de Navidad.
- **Cambiado:** `WIKI/guiones-y-anuncios.md` (registro de preferencias: originalidad > tema) e `index.md`.

## 2026-10-13 — Guiones piedras v4
- **Creado:** `OUTPUTS/2026-10-13-guiones-piedras-v4.md`: 3 guiones originales de Scented Stones en inglés y español con voseo. Ángulos nuevos: estacionalidad de Navidad, reacción del marido que hace las cuentas, pedido puntual de casamiento.
- **Cambiado:** `WIKI/index.md` (outputs).

## 2026-10-13 — VSL de Pilates Hormonal
- **Fuentes:** VSL original de Calistenia Asiática (~/Downloads, 6:13) y foto de la Maestra Caro. Conversación con Santiago.
- **Creado:**
  - `WIKI/vsl-reglas-de-armado.md`: tono hablado ("Soy la Maestra Caro"), HeyGen, créditos de Higgsfield (intercalar modelos baratos), receta de producción.
  - `OUTPUTS/2026-10-12-vsl-pilates-hormonal-guion.md`: el guion.
  - `OUTPUTS/scripts-vsl/` (`edit.py`, `mkgfx.py`).
- **Entregable:** `~/Desktop/pilates-hormonal-vsl/VSL-Pilates-Hormonal-1.3x.mp4` (4:45, 1080×1920).
- **Cambiado:** `CLAUDE.md` (leer las reglas de VSL) e `index.md`.
- **Créditos:** HeyGen 108 · Higgsfield ~105 (Kling 3.0) + 15 (Kling 2.6).

## 2026-10-12 — Quiz de Pilates Hormonal y reglas para armar quizzes
- **Fuentes:** conversación con Santiago (sin archivos nuevos en RAW). Modelo: el quiz de Sana Pilates que él corre en Argentina (InLead).
- **Creado:**
  - `WIKI/quizzes-reglas-de-armado.md`: reglas, registro de correcciones con fecha y checklist de entrega. Se mantiene viva.
  - `OUTPUTS/2026-10-12-quiz-pilates-hormonal.html`: el quiz final.
- **Cambiado:**
  - `CLAUDE.md`: leer las reglas de quizzes antes de armar uno y anotar cada corrección en el momento.
  - `como-trabajar-con-santiago.md` e `index.md` (tema nuevo y el output).
  - `quiz-funnel.md`: enlace a la página nueva.
- **Correcciones registradas:** sin encabezados de relleno, más espaciado, precio $14.990, tachado $49.990 y cuotas de $4.997, mockup de celular en vez de libros, testimonios y garantía en HTML, notificaciones discretas con cupos que solo bajan, CTAs a `pilates-hormonal.impultienda.ar/checkout`.

## 2026-10-11 — Quiz de Chupetines para Bebidas
- **Último procesado:** 2026-10-11
- **Fuentes procesadas:** `RAW/2026-10-11-quiz-chupetines-para-bebidas.md` (solo la pantalla de entrada).
- **Creado:** `OUTPUTS/2026-10-11-guiones-chupetines.md` (3 guiones y 9 hooks, en español con voseo).
- **Cambiado:** `ofertas.md` (nota sobre el estado de Chupetines).
- **Conexiones inesperadas:**
  1. **El estado de Chupetines no coincide:** `ofertas.md` la tiene en historial sin resultados y el contexto maestro la marca como activa.
  2. **El quiz promete más de $2.000.000 ARS al mes** frente a un precio de 14.999 ARS. Es un claim de ingresos que tiene que tener respaldo.
  3. **Alcohol:** el quiz habla de tragos y licores. Meta restringe esa categoría.

## 2026-10-11 — Natives ganadoras de Scented Stones
- **Último procesado:** 2026-10-11
- **Fuentes procesadas:** `RAW/2026-10-11-natives-ganadoras-scented-stones.md` y `RAW/natives/` (3 imágenes + 3 descripciones).
- **Creado:** `WIKI/natives-ganadoras.md` (patrones y plantilla) y `OUTPUTS/2026-10-11-natives-piedras.md` (4 natives nuevas, con prompt y descripción en inglés y español).
- **Cambiado:**
  - `guiones-y-anuncios.md`: la descripción pasa de 400–500 a 900–1.200 palabras y la regla de "sin cara" tiene una excepción.
  - `scented-stones.md` e `index.md`: enlaces a la nueva página.
- **Conexiones inesperadas:**
  1. **Las descripciones ganadoras miden casi el doble de lo que decía la wiki.** 907, 883 y 1.174 palabras.
  2. **La descripción narra la imagen casi pieza por pieza:** 47 vendidas + 25 que quedan = las 72 piedras del texto; el cartel "$12 for $30" es el precio del texto.
  3. **La native 1 dice sal y harina y las natives 2 y 3 dicen yeso.** Las natives, igual que los guiones, no coinciden con la landing.
  4. **La native 2 afirma que las piedras son seguras para mascotas.** Los aceites esenciales pueden ser tóxicos para perros y gatos. No lo repito.
  5. **La ganadora 2 muestra una cara**, así que "sin cara" no es una regla absoluta.

## 2026-10-11 — Landing de Scented Stones
- **Último procesado:** 2026-10-11
- **Fuentes procesadas:** `RAW/2026-10-11-landing-scented-stones.md` (scentedstone.lovable.app). El texto quedó cortado en la FAQ.
- **Cambiado:**
  - `scented-stones.md`: sección Landing, producto real (yeso) y choque de ingredientes resuelto.
  - `index.md`: gap 2.
  - `CLAUDE.md` y `como-trabajar-con-santiago.md`: regla fija de entrega (inglés y español, listo para copiar).
- **Creado:** `OUTPUTS/2026-10-11-guiones-piedras.md` (tanda 11/10) y los guiones de Leather Blueprint Vault del 10/10.
- **Conexiones inesperadas:**
  1. **Los ads y la landing describen productos distintos.** Los ganadores dicen sal + harina y la landing vende yeso, aceite de fragancia y molde de silicona.
  2. **La landing ya trae ángulos que los ganadores no usan:** miedo a perder ahorros, jubilada, pedidos de boda de 80–150 piezas y reposición mensual de boutiques.
  3. **Los testimonios de la landing tienen cifras fuertes ($200–$380) que no se pueden verificar.** No los uso como claims propios.
  4. **El primer botón está en el Hero**, la causa 1 de checkouts falsos de tu propio diagnóstico.

## 2026-10-10 — Carpeta RAW/prompts/ completa (23 de 23)
- **Último procesado:** 2026-10-10
- **Fuentes procesadas:** `RAW/prompts/` (prompt-optimizar-carga-web-html, prompt-testimonios-sora-2, prompt-variacion-de-guiones-winners, prompt-vsl-oto-post-purchase).
- **Cambiado:**
  - `biblioteca-de-prompts.md`: tabla completa de los 23 prompts, con riesgos marcados.
  - `scented-stones.md`: paso 1 con el prompt de variación de winners.
  - `index.md`: gaps reordenados (los documentos de investigación pasan al número 1).
- **Conexiones inesperadas:**
  1. **`prompt-variacion-de-guiones-winners` es la versión completa del análisis de DNA** que ya se hizo a mano para piedras (diagnóstico + 6 categorías). Solo le falta la landing.
  2. **11 de los 23 prompts piden los documentos de investigación.** Todo el sistema depende de ellos.
  3. **Tres prompts empujan hacia claims que no se pueden sostener:** "explicación pseudo-científica" y "fue denunciado" (VSL OTO), testimonios de clientes hechos con IA (Sora 2) y comentarios inventados (IG). Quedan marcados. Uso la estructura con claims reales.
  4. **El prompt de VSL OTO pide una garantía de 30 días o más:** quinta fuente a favor de una garantía larga.
  5. **El prompt de optimización de carga está pensado para Shopify.** Para Lovable sirve todo menos los parámetros del CDN.

## 2026-10-10 — 5 prompts más a RAW/prompts/ (19 de 23)
- **Último procesado:** 2026-10-10
- **Fuentes procesadas:** `RAW/prompts/` (prompt-imagenes-ads, prompt-magic-patterns, prompt-meta-ads-primary-text, prompt-modelar-ofertas, prompt-one-shot-mockups).
- **Cambiado:**
  - `biblioteca-de-prompts.md`: 19 de 23, con sus choques marcados.
  - `como-trabajar-con-santiago.md`: nueva sección "Prioridad de reglas" (tus reglas personales le ganan a los prompts).
  - `guiones-y-anuncios.md`: el primary text sigue la estructura del prompt, filtrada por tus reglas.
  - `index.md`: actualizado.
- **Conexiones inesperadas:**
  1. **`prompt-meta-ads-primary-text` choca de frente con tus reglas.** "Es tu culpa si…" y el sesgo de negatividad van contra "no catastrófico". "Por solo $[Precio]" va contra "sin precio en el ad". Queda fijado que ganan tus reglas.
  2. **`prompt-magic-patterns` genera React + Tailwind, igual que Lovable.** Tu herramienta de landings puede usarlo casi sin cambios.
  3. **`prompt-imagenes-ads` pide "modelos realistas"** y tus natives son sin cara. Para natives ganan tus reglas.
  4. **Ya son 8 prompts que piden los documentos de investigación.** Es por lejos el cuello de botella número 1.
  5. **`prompt-one-shot-mockups` trae un ejemplo olvidado en el input** ("297 Evaluaciones…"): hay que reemplazarlo antes de usarlo.

## 2026-10-10 — 5 prompts más a RAW/prompts/ (14 de 23)
- **Último procesado:** 2026-10-10
- **Fuentes procesadas:** `RAW/prompts/` (prompt-generador-de-prompts-maestros, prompt-guiones-7-pasos, prompt-guiones-30-segundos, prompt-guiones-por-nivel-de-conciencia, prompt-html-google-ai-studio).
- **Cambiado:**
  - `biblioteca-de-prompts.md`: tabla de estado con 14 de 23.
  - `guiones-y-anuncios.md`: criterio para el choque entre "3 completos" y "1 + 2 modular".
  - `scented-stones.md`: landing en español, remarketing y nivel de conciencia de los ganadores.
  - `index.md`: actualizado.
- **Conexiones inesperadas:**
  1. **Tus prompts de guiones entregan "1 completo + 2 solo de hook"** y tu regla personal pide "3 completos distintos". Criterio: si pedís "guiones", van 3 completos; si pedís "hooks" o "renovar", va el formato modular.
  2. **"30 segundos ≈ 75 palabras"** (prompt) coincide con tu regla de ~150 palabras por minuto.
  3. **Los ganadores de piedras le hablan al nivel "inconsciente":** no sabían que esto era una oportunidad. Los niveles 2 a 5 casi no están explorados. El 5 sirve para remarketing, y piedras no tiene remarketing.
  4. **`prompt-html-google-ai-studio` es la herramienta de la expansión:** adapta la landing que ya funciona a otro idioma sin tocar la estructura.
  5. **Ya son 5 prompts que exigen los documentos de investigación.** Es el cuello de botella número 1 para producir con tu sistema.
  6. **El meta-prompt prohíbe "Actúa como"**, pero 6 de tus prompts arrancan así. Es solo estilo, no afecta el resultado.

## 2026-10-10 — 5 prompts más a RAW/prompts/
- **Último procesado:** 2026-10-10
- **Fuentes procesadas:** `RAW/prompts/` (prompt-crear-mockups, prompt-crear-upsells, prompt-ebook-con-claude, prompt-educar-chatgpt, prompt-escribir-sales-page). Ya hay 9 de 23 prompts con texto.
- **Cambiado:**
  - `biblioteca-de-prompts.md`: tabla de estado con qué pide cada prompt y sus alertas.
  - `embudo-vsl-post-pago.md`: **corregido** el borrador de OTO 1 de piedras, de videocurso a PDF.
  - `scented-stones.md`: sección de prompts listos.
  - `como-trabajar-con-santiago.md`: regla de upsells y bonus solo en PDF.
  - `index.md`: actualizado.
- **Conexiones inesperadas:**
  1. **Me corrijo otra vez:** había propuesto un videocurso como OTO 1 de piedras, y `prompt-crear-upsells` prohíbe los videocursos porque no se graban. Ahora es una "Pro Finish Bible" en PDF.
  2. **Ted's Woodworking, la carta modelo, ya trae el ángulo de dinero:** un bonus "How To Start A Woodworking Business" y la FAQ "Can I sell what I make?". Es el segmento "ganá plata con un oficio".
  3. **Hipótesis:** los Blueprint Vault de Santiago (Welder's, Leather) siguen el molde de Ted's (miles de planos). Se habrían vendido como "colección de planos" y no como "ingreso", que es lo que diferencia a piedras. Falta confirmarlo.
  4. **Cuarta fuente a favor de una garantía larga:** Ted's ofrece 60 días.
  5. **El molde "Herrería" pone el botón en el Hero**, contra la causa 1 de checkouts falsos de tu propio diagnóstico.
  6. **Ya son 3 prompts que exigen los 4 documentos de investigación** (upsells, mockups, ángulos Launch Expert): es el cuello de botella para producir con tus prompts.
  7. **Testimonios con "foto simulada"** en el prompt de sales page: mismo riesgo que los comentarios fabricados.

## 2026-10-10 — Primeros prompts a RAW/prompts/
- **Último procesado:** 2026-10-10
- **Fuentes procesadas:** `RAW/prompts/` (_indice, prompt-ads-storytelling-largos-publico-frio, prompt-angulos-manuales-launch-expert, prompt-angulos, prompt-comentarios-positivos-ig). Van a `RAW/prompts/` con los nombres exactos que cita la WIKI, así las referencias `RAW/prompts/...` de varios temas ya resuelven.
- **Cambiado:**
  - `biblioteca-de-prompts.md`: sección "Estado de la carpeta" con qué pide cada prompt disponible y cómo aplicarlo.
  - `scented-stones.md`: sección de riesgo por claims de ingresos.
  - `guiones-de-video-ads.md`: marca el prompt de storytelling como disponible.
  - `index.md`: actualizado.
- **Conexiones inesperadas:**
  1. **El prompt de storytelling ya trae la voz "juez que se redime".** Es la contadora del guión 3 de piedras: la versión larga sale casi directa.
  2. **`prompt-angulos-manuales-launch-expert` no arranca sin los 4 documentos de investigación.** Sube la prioridad de generarlos para piedras.
  3. **Tu propio prompt de storytelling pide claims realistas y en primera persona** cuando se toca dinero. Es justo la protección que necesitan los claims de ingresos de los ganadores de piedras frente a FTC y Meta.
  4. **`prompt-comentarios-positivos-ig` fabrica prueba social** (comentarios con nombres y fotos inventados). Queda marcado como riesgo legal y de cuenta. No lo voy a usar para presentar testimonios falsos como reales.

## 2026-10-10 — Catálogo, testeo de creativos, tracking, UGC y validación
- **Último procesado:** 2026-10-10
- **Fuentes procesadas:** `RAW/2026-10-10-wiki-previa/` (subir-ads-con-metodo-catalogo, testeo-de-creativos, tracking-y-atribucion, ugc-y-video-generativo, validacion-de-oferta).
- **Creado:** 5 temas en `WIKI/`. Contenido íntegro, más resumen, fuente y "Conexiones con tu operación actual".
- **Cambiado:**
  - `scented-stones.md`: fase actual, concepto "venta directa", testimonio de 14 s, avatar Susana.
  - `como-trabajar-con-santiago.md`: reglas de UGC para prompts de video.
  - `index.md`: actualizado.
- **Conexiones inesperadas:**
  1. **"Los creativos son el 95%" (2026-08) contra "casi nunca es el anuncio, es la landing" (2026-09, con datos).** Conviven: el creativo prevende; si no hay ganancia, se diagnostica landing → pago.
  2. **Scented Stones ya está validada.** Según el método, el paso siguiente es backend → escalar. Coincide con el gap que se venía marcando.
  3. **El concepto "venta directa"** (últimos cupos, garantía de 30 días) es el tercer concepto del testeo post-Andrómeda, y ninguno de los 3 ganadores lo usa.
  4. **Susana (56, maestra jubilada)** encaja con la variable "anti-hustle jubilada" propuesta para piedras.
  5. **Decisión abierta sobre Emma Carter:** hoy no tiene cara. Hacerla avatar de HeyGen cambiaría la estética de las natives.
  6. **"Mínimo 20 anuncios antes de abandonar"** plantea la duda de si las craft que no funcionaron llegaron a ese mínimo.

## 2026-10-10 — Renovación, segmentos, selección de oferta, setup y Shopify/checkout
- **Último procesado:** 2026-10-10
- **Fuentes procesadas:** `RAW/2026-10-10-wiki-previa/` (renovacion-de-creativos, segmentos-de-mercado, seleccion-y-modelado-de-oferta, setup-de-campanas, shopify-y-checkout).
- **Creado:** 5 temas en `WIKI/`. Contenido íntegro, más resumen, fuente y "Conexiones con tu operación actual".
- **Cambiado:**
  - `angulos-publicitarios.md` y `scented-stones.md`: **corregida** la sugerencia de probar un ángulo "hobby".
  - `guiones-de-video-ads.md`: queda resuelto el choque del body.
  - `ofertas.md`: explicación por segmentos.
  - `como-trabajar-con-santiago.md`: qué significa "renovar".
  - `index.md`: actualizado.
- **Conexiones inesperadas:**
  1. **El segmento explica por qué piedras funcionó y las otras craft no.** Piedras se vende como "ganá plata con un oficio", la prioridad 1 evergreen. Las demás se parecen a "crochet por hobby", que no tiene urgencia de compra.
  2. **Me corrijo:** la idea de vender piedras por "hobby o aromaterapia" choca con segmentos. Si se explora, tiene que ser salud con mecanismo.
  3. **Se resuelve el choque del body.** El body fijo es para renovar un ganador; el body variable es para conceptos nuevos.
  4. **"Respetar el formato al modelar" y "rotar formatos" son dos etapas distintas:** lanzar y después diversificar.
  5. **Impultienda resuelve el backend de piedras:** OTOs nativos cobrando en USD. Es una recomendación no neutral, porque Santiago tiene código de referido.
  6. **Tu precio en AR (14.999–15.990) coincide con el mínimo de 15.000 pesos** del material. La escalera sugiere subir a 19.000.

## 2026-10-10 — Página de ventas, problemas de cuentas, procesadores, psicología del comprador y quiz funnel
- **Último procesado:** 2026-10-10
- **Fuentes procesadas:** `RAW/2026-10-10-wiki-previa/` (pagina-de-ventas, problemas-de-cuentas-meta, procesadores-de-pago, psicologia-del-comprador, quiz-funnel).
- **Creado:** 5 temas en `WIKI/`. Contenido íntegro, más resumen, fuente y "Conexiones con tu operación actual".
- **Links restaurados:** `[[pagina-de-ventas]]` vuelve a apuntar a su página en 10 temas; antes iba a `landings-funnels-y-upsells`.
- **Cambiado:**
  - `landings-funnels-y-upsells.md`: links a quiz-funnel y pagina-de-ventas.
  - `scented-stones.md`: checklist de auditoría de la landing.
  - `guiones-y-anuncios.md`: sección de primary text con la regla de emojis y rechazos. Se arregló la intro duplicada.
  - `index.md`: actualizado.
- **Conexiones inesperadas:**
  1. **Los 3 guiones ganadores de Scented Stones cubren los 3 tipos de comprador.** Emocional ("easiest money"), lógico ("do the quick math") y FOMO (temporada de bodas, boutiques que cierran proveedores). Puede ser parte de por qué funciona y las otras craft no.
  2. **La garantía de 30 días ya aparece en 3 fuentes** (página de ventas, optimización de ROAS, psicología del comprador) contra tu estándar de 7 días.
  3. **Tu estructura de Lovable y la de referencia difieren en dónde va el primer botón.** La de referencia lo pone después del producto, y el botón en el Hero es la causa 1 de checkouts falsos.
  4. **El quiz funnel es tu formato de la etapa fitness.** Tolera un CPC de 1 USD, así que podría servir para piedras en Tier 1 (test: "How much could you make from your kitchen table?").
  5. **"Menos emojis" para evitar rechazos choca con tu primary text con emojis.** Queda como primera palanca si una cuenta rechaza.
  6. **Whop permite cobrar en USD sin LLC**: es una opción para la pregunta abierta de cómo cobra piedras.

## 2026-10-10 — Métricas, modelo low ticket, nomenclatura, optimización de ROAS y organización
- **Último procesado:** 2026-10-10
- **Fuentes procesadas:** `RAW/2026-10-10-wiki-previa/` (metricas-y-kpis, modelo-low-ticket, nomenclatura-del-metodo, optimizacion-de-roas, organizacion-y-registro).
- **Creado:** 5 temas en `WIKI/`. Contenido íntegro, más resumen, fuente y "Conexiones con tu operación actual".
- **Links restaurados:** `[[modelo-low-ticket]]` vuelve a apuntar a su página en 8 temas; antes iba a `perfil-y-negocio`.
- **Cambiado:**
  - `CLAUDE.md`: el registro diario de operación va en `OUTPUTS/`.
  - `guiones-y-anuncios.md`: la regla de 30 segundos queda marcada como "por defecto" a confirmar.
  - `scented-stones.md`: reloj de caducidad y palancas.
  - `como-trabajar-con-santiago.md`: registro y nombres.
  - `perfil-y-negocio.md`: link al modelo.
  - `index.md`: actualizado.
- **Conexiones inesperadas:**
  1. **El reloj de Scented Stones está corriendo.** Las ofertas caducan a los 3 o 4 meses y no sé desde cuándo está activa piedras. Replicarla en otros mercados le alarga la vida.
  2. **Fitia tenía sentido según el propio modelo.** La única excepción a la caducidad es la marca personal propia. El objetivo de romper el ciclo "test → burn" sigue vigente aunque esa oferta no haya funcionado.
  3. **Ya son 3 páginas** (ángulos, guiones de video y optimización de ROAS) **que piden probar creativos de 1:30 a 3 minutos**, contra la regla de 30 segundos máximo.
  4. **"Nunca nombrar al experto" es una regla de guión, no de landing.** En la landing, Emma suma autoridad (palanca 2).
  5. **La skill `ad-builder` se cita y no está en este repo.**
  6. **"Cargá en RAW y pedí procesá RAW"** aparece en tu propio material: es el flujo de este segundo cerebro.

## 2026-10-10 — Internacionalización, investigación, lectura de resultados, LLC y método V3
- **Último procesado:** 2026-10-10
- **Fuentes procesadas:** `RAW/2026-10-10-wiki-previa/` (internacionalizacion, investigacion-de-mercado, lectura-de-resultados, llc-banca-y-fiscal, metodo-v3).
- **Creado:** 5 temas en `WIKI/`. Contenido íntegro, más resumen, fuente y "Conexiones con tu operación actual".
- **Cambiado:**
  - `scented-stones.md`: sección de expansión y lanzamiento.
  - `como-trabajar-con-santiago.md`: tamaño de tanda de 5 a 10 anuncios.
  - `perfil-y-negocio.md`: multi-geo y pregunta de cobro.
  - `index.md`: estados ✅/⏳ y gaps.
- **Conexiones inesperadas:**
  1. **"No necesitás más de una oferta":** la jugada de más palanca con Scented Stones es replicarla en otros mercados, no buscar otra.
  2. **Santiago lo hizo al revés del manual.** El winner nació en Tier 1 inglés, el mercado "no recomendado para empezar". La expansión natural ahora es hacia abajo: LatAm y AR, con Carmela Vega como persona.
  3. **Choque de volumen resuelto:** "3 guiones por tanda" es la base creativa; el conjunto V3 pide de 5 a 10 anuncios. Se multiplican los guiones por hooks o B-rolls, y nunca se mezcla imagen con video.
  4. **El "Tap Learn more" del guión 3 coincide con el botón estándar de V3** ("Más información").
  5. **El abandono del alemán** es el "si no agarra, no le insistas" de internacionalización.
  6. **Lectura de resultados equilibra el foco en ads:** cuando falla, casi siempre es landing → pago.

## 2026-10-10 — Guiones, hooks, IA, imágenes e índice previo
- **Último procesado:** 2026-10-10
- **Fuentes procesadas:** `RAW/2026-10-10-wiki-previa/` (guiones-de-video-ads, hooks, ia-en-el-flujo-de-trabajo, imagenes-y-mockups, `_index-wiki-previa.md`).
- **Creado:** 4 temas en `WIKI/`. Contenido íntegro, más resumen, fuente y "Conexiones con tu operación actual".
- **Cambiado:**
  - `index.md`: rehecho con las categorías de la wiki previa. Muestra los 19 temas ✅ y los 27 ⏳ pendientes con su descripción, más los gaps.
  - Se restauran los links `[[guiones-de-video-ads]]` en angulos-publicitarios, biblioteca-de-prompts, embudo-vsl-post-pago y escalado-en-meta-ads (antes apuntaban a `guiones-y-anuncios` porque la página no existía).
  - `guiones-y-anuncios.md`: separa las reglas personales del método general.
  - `scented-stones.md`: 4 variables nuevas.
  - `como-trabajar-con-santiago.md`: "verdad, no consuelo" y diagnosticar antes de variar.
  - `perfil-y-negocio.md`: Impultienda como plataforma actual.
  - `landings-funnels-y-upsells.md`: referencia a quiz-funnel.
- **Conexiones inesperadas:**
  1. **El guión 3 de Scented Stones calza en la variante (b) del storytelling largo** ("alguien que la juzgaba y se redime"). Da para una versión de 1:30 para público frío.
  2. **Choque:** la regla modular dice que el body queda igual y tu contexto maestro dice que los bodies tienen que variar. Se resuelve con modular dentro del concepto y body nuevo entre conceptos.
  3. **El hook de eliminación de objeciones** ("sin azúcar, sin harina, sin horno") se traslada a piedras: "No kiln. No fancy tools. No experience."
  4. **El índice previo resuelve el conflicto de stack:** Impultienda es la plataforma actual; Shopify y Hotmart eran referencia.
  5. **Natives contra mockups son dos estéticas opuestas** (UGC boho contra premium editorial) y no se mezclan.
  6. **Este repo es exactamente la "carpeta local como segundo cerebro"** que recomienda `ia-en-el-flujo-de-trabajo`.

## 2026-10-10 — Escalado, CBO, filosofía, WhatsApp y funnel hacking
- **Último procesado:** 2026-10-10
- **Fuentes procesadas:** `RAW/2026-10-10-wiki-previa/` (escalado-en-meta-ads, estructuras-cbo, filosofia-de-marketing, funnel-de-whatsapp, funnel-hacking).
- **Creado:** 5 temas en `WIKI/`. Contenido íntegro, más resumen, fuente y "Conexiones con tu operación actual".
- **Cambiado:**
  - `como-trabajar-con-santiago.md`: estándar de copy (nada de frases de IA, transformación, volumen) y filtros de cazar.
  - `guiones-y-anuncios.md`: no mezclar imagen y video, crudo pero positivo.
  - `perfil-y-negocio.md`: links al ciclo.
  - `scented-stones.md`: palanca de escala.
  - `index.md`: temas, pendientes recalculados y gap 1.
- **Conexiones inesperadas:**
  1. **"De 6 ofertas validadas, escala 1"** explica tu catálogo: de unas 20 ofertas, Scented Stones es la que funciona. Es lo esperable.
  2. **"Más anuncios, no más ofertas"**: la palanca de piedras es el volumen de variables. Pero el ritmo de 10 creativos por día choca con la regla de 3 guiones por tanda.
  3. **Los dos filtros de cazar no coinciden.** La skill usa 50+ ads y 3+ días; funnel hacking usa mismo URL, 1 semana o más y sin marca personal. Se complementan.
  4. **Para una oferta en inglés se espía en AR, LATAM y BR**, al revés de tu flujo habitual BR → AR.
  5. **"Crudo" contra "no catastrófico"** no se contradicen: crudo en el tono, positivo en la promesa.
  6. **El bid "valor más alto" necesita backend.** Otra razón para montar el post-pago de Scented Stones.

## 2026-10-10 — 5 páginas más de la wiki previa
- **Último procesado:** 2026-10-10
- **Fuentes procesadas:** `RAW/2026-10-10-wiki-previa/` (creacion-de-productos-digitales, diagnostico-de-checkout, disputas-y-reembolsos, email-y-automatizaciones, embudo-vsl-post-pago).
- **Creado:** 5 temas en `WIKI/`. Contenido íntegro, más resumen, fuente y "Conexiones con tu operación actual".
- **Cambiado:**
  - `aumento-de-aov.md`: vuelve el link original a `embudo-vsl-post-pago`, que ya existe.
  - `landings-funnels-y-upsells.md`: alerta sobre el orden de la escalera y link al diagnóstico de checkout.
  - `scented-stones.md`: escalera post-pago y recupero por email y SMS.
  - `index.md`: temas nuevos, pendientes recalculados y gaps.
- **Conexiones inesperadas:**
  1. **Scented Stones está en el nicho más fácil para upsellear** (ingreso extra). Quedó un borrador de 4 OTOs: $37 → $97 GPT "Emma" → $27 kit de venta → $17 packaging.
  2. **Tu escalera en ARS pone el ticket más alto al final** (29.990). La regla del embudo VSL es que el más alto va segundo.
  3. **El post-pago vende más que el mismo producto como bump.** Varias ideas de bumps de `aumento-de-aov` rinden más como OTO.
  4. **Hay dos usos de WhatsApp que no hay que mezclar.** Como canal de venta de la persona en el ad (Emma) es un recurso de copy. Como remarketing tuyo, en inglés rinden más el email y el SMS.
  5. **Este repo es el "segundo cerebro" que la página de disputas propone usar** para pelear contracargos con Claude Code. Faltaría conectar Stripe o MercadoPago.
  6. **Etsy aparece como referencia de temario** en creación de productos. La prohibición es solo para nombrarlo en los ads.

## 2026-10-10 — 5 páginas de la wiki previa
- **Último procesado:** 2026-10-10
- **Fuentes procesadas:** `RAW/2026-10-10-wiki-previa/` (angulos-publicitarios, aumento-de-aov, biblioteca-de-prompts, claude-con-meta-ads, contingencia-de-cuentas), guardadas tal cual en `RAW/`.
- **Creado:** 5 temas en `WIKI/` con el mismo nombre. Contenido íntegro, más resumen, fuente y una sección "Conexiones con tu operación actual".
- **Links adaptados:** `guiones-de-video-ads` → `guiones-y-anuncios`, `modelo-low-ticket` → `perfil-y-negocio`, `pagina-de-ventas` y `embudo-vsl-post-pago` → `landings-funnels-y-upsells`. Los otros 22 temas citados quedan listados en el índice como pendientes.
- **Cambiado:**
  - `guiones-y-anuncios.md`: sección de variación real.
  - `landings-funnels-y-upsells.md` y `perfil-y-negocio.md`: links al backend y stack ampliado.
  - `como-trabajar-con-santiago.md`: herramientas y regla de pausa en Meta.
  - `scented-stones.md`: próximos pasos.
  - `index.md`: temas y gaps.
- **Conexiones inesperadas:**
  1. El "contador" aparece en el downsell modelo de AOV ("mi contador me prohibiría") y en el guión ganador 3. Es un personaje recurrente que funciona.
  2. Scented Stones solo se vende por el gran nicho "dinero". "Un producto, dos mercados" abre el ángulo salud o hobby (aromaterapia, regalo).
  3. Las reglas de copy chocan con la wiki previa. La regla de 30 segundos máximo choca con "rotar formatos y largos". La de no ser catastrófico choca con "dolor central emocional".
  4. El stack de checkout no coincide. El contexto maestro dice Hotmart, Kiwify, Monetizze y Lovable; la página de AOV dice Shopify, SellEasy y Aftersell.
  5. La tienda de referencia con front de $27 y AOV de 39,44 podría ser Scented Stones.

## 2026-10-10 — Guiones ganadores de Scented Stones + reconstrucción de la WIKI
- **Último procesado:** 2026-10-10
- **Fuentes procesadas:** todo `RAW/`, incluido `RAW/2026-10-10-guiones-ganadores-scented-stones.md` (nuevo: 3 guiones + notas de Santiago).
- **Creado:** `WIKI/scented-stones.md` (ficha, DNA de los 3 guiones, choques con las reglas, ideas de variables).
- **Cambiado:**
  - Los links pasan a formato `[[nombre-tema]]` en toda la WIKI y en `CLAUDE.md`.
  - `ofertas.md`: Scented Stones es la única activa; el resto pasa a historial sin resultados.
  - `guiones-y-anuncios.md`: 3 ángulos nuevos y la excepción del precio como ROI.
  - `index.md`: una línea por tema y gaps nuevos (se quitó el gap de métricas a pedido de Santiago).
- **Eliminado:** `WIKI/fitia.md`, que pasa a una fila del historial en `ofertas.md`.
- **Conexiones inesperadas:**
  1. **Los ganadores rompen 2 reglas fijas.** Dicen "$27 guide" y "Emma's guide". El precio funciona cuando se presenta como ROI ("lo recuperé con la primera venta"). Puede que la regla de no mencionar el precio aplique al precio de venta y no al de la guía.
  2. **El funnel de quiz es herencia de fitness.** El único winner manda directo a la guía con "link below / Learn more", no a un quiz.
  3. **Ad vs. catálogo:** los ads describen masa de sal (salt + flour) y el catálogo dice yeso.
  4. **Bodas y eventos aparecen en dos lugares:** son el canal de venta en el guión 3 y también el nombre de las OTOs en ARS ("eventos", "agenda llena"). El patrón ganador es un producto que se vende físicamente a terceros en ocasiones especiales. Conecta además con la native de feria "LAST ONE".
  5. **Los ángulos de fitness se trasladan a craft con otra forma.** La "reacción familiar" pasa a "reacción de la contadora"; el "humblebrag con edad" pasa a "ingreso accidental, nunca quise un negocio".
  6. **Lo que tiene Scented Stones y no tienen las craft que fallaron:** todas tienen el mismo precio, ancla y persona. La diferencia está en el ángulo, que es ingreso extra con margen por pieza visible, y no en la oferta.

## 2026-10-10 — Contexto maestro del negocio
- **Último procesado:** 2026-10-10
- **Fuentes procesadas:** `RAW/2026-10-10-contexto-maestro-santiago.md` (lo añadió Claude a pedido de Santiago).
- **Creado:** `WIKI/como-trabajar-con-santiago.md`, `WIKI/perfil-y-negocio.md`, `WIKI/ofertas.md`, `WIKI/guiones-y-anuncios.md`, `WIKI/landings-funnels-y-upsells.md`, `WIKI/fitia.md`.
- **Cambiado:** `WIKI/index.md` (temas agrupados por área y gaps nuevos), `CLAUDE.md` (rol de experto en low ticket y voseo).

## 2026-10-10 — Configuración inicial
- **Último procesado:** 2026-10-10
- **Fuentes procesadas:** `README.md`, `_CarpetaHenry_/`, historial de git (RAW/ estaba vacío).
- **Creado:**
  - `CLAUDE.md` con las reglas del bibliotecario (leer, organizar, responder, guardar, mejorar).
  - Carpetas `RAW/` (con README de uso), `WIKI/`, `OUTPUTS/`.
  - `WIKI/index.md` con tabla de temas, sección de outputs y top 3 gaps.
  - `WIKI/prep-course-henry.md` — primer tema.
