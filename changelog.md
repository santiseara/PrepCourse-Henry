## 2026-11-10 (8ª pasada) — Noche de Citas Cristiana: los 3 orgánicos con voz de mujer y cama activa

- Pedido de Santiago: *"Los 3 que hiciste mas originales, me gustaria que tengan voz en off, de una mujer, y con musica activa, no me pongas la de siempre, quiero musica activa"*.
- **Voz Sulafat** con Style de mujer argentina contándole algo a una amiga, `speed 1.30` y pausas recortadas. Las tres se verificaron con Whisper: arrancan por la primera palabra y no leen el Style. La 2.5 dio **429** después de la primera, así que las otras dos salieron con `gemini-3.1-flash-tts-preview` (la regla de reemplazo del 2/11).
- 🆕 **Cama musical nueva y propia: `OUTPUTS/scripts-vsl/music_activa.py`** — 104 BPM, pluck de marimba, bajo redondo, palmas y hi-hat, Do–Sol–Lam–Fa. Hermana de `music_calma.py`. Se escribió porque pidió música activa **que no sea la de siempre**: no se reusó `bed_activo`.
- **El largo del video lo manda la locución**: los orgánicos quedaron en 14,87 / 17,47 / 13,93 s (los clones siguen en 15,40). Con voz quedan **dos carteles** en vez de tres: el de apertura y el del CTA.
- `edit_datenight.py` ahora acepta `vo` y mezcla sin normalizar (`amix normalize=0`), con la cama a 0,22. Comprobado transcribiendo el audio final de los tres: la voz se entiende entera por encima de la música.

## 2026-11-10 (7ª pasada) — Noche de Citas Cristiana: oferta nueva para Argentina y tanda 1 de 6 ads

- Pedido de Santiago, con el link de la Biblioteca: *"Tenemos que hacer 6 ads... 3 como los de ellos, tipo copiándoles todo el formato"* y los otros 3 *"más originales y orgánicos"*, estilo TikTok y **sin subtítulos**. Mercado: **Argentina, voseo**.
- **Radiografía del ganador** ([[noche-de-citas-cristiana]]): la página es **Ana Cristina**, vende **Date Night Cristão** (`dateparacasais.com.br`, R$ 19,90), **16 ads activos** desde el 12/8. Se bajaron los 12 videos: **6 creativos distintos**, todos de **15,4 s**, y **ninguno tiene locución** (transcriptos con faster-whisper: audio vacío). Venden con **dos carteles fijos y una caja blanca de CTA** sobre b-roll de celular y las hojas del producto.
- **Competencia:** en portugués el nicho tiene **~100 ads** y 8 anunciantes; **en español no lo corre nadie** (lo que aparece son mazos físicos argentinos, que prueban la demanda). Arbitraje limpio.
- **Las 7 hojas del producto se dibujaron por código** (`gfx_datenight.py`): cartas de la gratitud, preguntále a tu pareja, devocional, oraciones guiadas, desafíos de conexión, bingo y verdad o desafío, en la paleta de ellos. El producto todavía no existe y la tanda se puede testear igual.
- **Editor nuevo sin voz:** `edit_datenight.py` + `gen_datenight_plans.py` + `vent_datenight.py`, con la cama `bed_calma`. Los 6 videos quedaron en `~/Desktop/date-night/anuncios/` como `10-11 - 1` a `10-11 - 6` (15,40 s, 1080×1920).
- 🆕 **Regla nueva en [[guiones-y-anuncios]]: un nicho entero de TikTok puede estar podrido.** 135 clips de los tags cristianos y de pareja en español se tiraron enteros (todos con texto quemado); los limpios salieron de **tags de objeto**, que no tienen idioma (`#juegodecartas`, `#cardgames`, `#boardgamenight`, `#cozynight`). 11 limpios de 65.
- 🐞 **Y otra: `zoompan` emite `d` cuadros por cuadro de entrada.** Las hojas armadas con `-loop 1 -t 2` duraban 120 s y los seis ads mostraban siempre la misma página. Se corrige con una sola imagen de entrada y `-frames:v N`.

## 2026-11-10 (7ª pasada) — The Party Box Vault: oferta nueva para el mercado inglés, tanda 1 de 6 videos

- Pedido de Santiago: *"Necesito que hagamos 6 testeos para esta oferta… la vamos a tirar en inglés, acordate de hacer lo mismo de siempre para los ads"*, con el link a la Biblioteca de Anuncios de la page `1288335281030909`.
- **Quién es:** **Moldes Prontos / caixinha cenário** (BR), **51 ads activos**, 8 copies distintos. El que más corre son **21 ads con el mismo texto desde el 5 de septiembre**; el segundo, 9 ads de cajas para taza desde el 1 de septiembre. Vende **+300 moldes imprimibles de cajitas de souvenir** editables en Canva a R$10, con landing en Vercel y tres dominios.
- **Se desarmó el ganador entero**, no solo el copy: se bajaron **10 de sus 51 videos** (muestra, no todos), se transcribieron con Whisper y se le hizo la hoja de contactos a su edición. Salieron **6 familias de hook** (la impresora parada · me salvó el atelier · producto con salida todo el año · la caja vale más que el regalo · te quedaste atrás · querer dominar Canva primero) y un montaje muy marcado: **subtítulo de UNA palabra, negro dentro de caja amarilla**, b-roll de manos armando cajitas y el inserto de la carpeta de moldes con un chip grande encima.
- **Entregados los 6 guiones** (`OUTPUTS/2026-11-10-guiones-party-box-vault-tanda1.md`), uno por familia, en **inglés y español con voseo**, 132 a 152 palabras cada uno. Sin precio: la plata va como *dirt cheap* y los entregables con nombre propio (*300+ box templates*, *assembly video*, *First Sale Kit*, *100 ready messages*), que es lo que pide la regla del mercado inglés del 28/10.
- **Los 6 videos**, con la edición del ganador clonada: subtítulos de una palabra en caja amarilla, voz Sulafat en inglés a `speed 1.30`, cama `bed_activo`, insertos dibujados por código (`gfx_boxes.py`: la librería de moldes con los **dielines en SVG**, el celular con el índice, la página de armado y el calendario de la demanda).
- **B-roll:** 84 clips bajados de `#partyfavorbox`, `#explosionbox`, `#treatboxes` y `#papercraftbusiness`; 43 revisados, **28 limpios**. Es el mejor rinde de tag de todas las ofertas: el nicho filma el proceso sin hablar a cámara.
- 🆕 **La hoja de contactos del render volvió a atrapar dos clips que el pool había dejado pasar**, los dos por cartel quemado que entra *después* del tramo revisado: `#partyfavorbox` 22591 ("TOY STORY PARTY FAVOR BOXES" arriba a la izquierda, a los 30 s) y `#explosionbox` 14198 ("Cut another square with added 5cm on each side", a los 35 s de un tutorial largo). Los dos se cayeron enteros y la tanda se rehízo. Es la misma regla del 10/11 de [[pisos-epoxi]]: en un nicho de manualidades el clip se mira entero, no la ventana.
- **TTS:** `gemini-2.5-flash-preview-tts` devolvió **429 en la segunda request** (la cuota del día ya estaba gastada por las tandas de Carteras y Epoxi). La tanda salió con **`gemini-3.1-flash-tts-preview`**, verificada con Whisper: no lee el Style en voz alta. Se rehízo también la V1 que había salido con el modelo 2.5, para que las seis voces vengan del mismo modelo.
- 🐞 **Dos descargadores de tikwm corriendo a la vez.** El `nohup … &` del primer intento sobrevivió al shell y quedó bajando en paralelo con el segundo: aparecieron `.part` duplicados en la carpeta de clips. Se mató el viejo y se limpiaron los `.part` antes de renderizar.
- 🆕 **Herramienta nueva: OCR del pool antes de renderizar** (`OUTPUTS/scripts-vsl/ocr_vision.swift` + `scan_carteles.py`). Dos renders salieron sucios con carteles que la hoja de contactos no mostraba, porque eran **blancos sobre fondo claro**. Pasándole el OCR de Vision de macOS a un cuadro por segundo de cada ventana aparecieron, en una sola pasada, cinco leyendas de creador y una marca de agua (*Kgoodessentials*) que dura los 70 segundos de su clip. Quedó como regla en [[guiones-y-anuncios]]: el OCR caza el texto, la hoja de contactos juzga el plano. Es gratis, Vision viene con el sistema.
- El pool final quedó en **28 clips**: se cayeron enteros 22591, 14198 y 33119, y siete ventanas arrancan más tarde con el segundo medido por OCR, no a ojo.
- ⚠️ **Falta la landing.** Los insertos se dibujaron con nombre de trabajo (*The Party Box Vault*); los guiones no nombran la marca, así que si la landing sale con otro nombre solo hay que rehacer los insertos.
- Nueva página [[party-box-vault]] con la radiografía del ganador, sus 6 familias, su edición y los 10 bonos de su landing. Índice al día.

## 2026-11-10 (6ª pasada) — El Secreto de la Chía: el precio del quiz argentino a $17.990

- Pedido de Santiago: *"Ajustame el precio del quiz, lo vendemos a 17.990"*.
- Cambiado en el único lugar donde vive (`QUIZ_CONFIG.precio`: `$ 24.900` → `$ 17.990`), con la cuenta de ocurrencias antes y después en los cuatro archivos (`.txt`, `.html`, `PRUEBA.html` y la copia de OUTPUTS: 1 antes, 1 después, 0 del viejo). El `.txt` quedó en el portapapeles.
- **El ancla no se tocó** (`TODO ESTO DE $ 38.999`), así que el descuento que muestra el quiz pasó de 36 % a 54 %: queda avisado, es decisión de Santiago.
- **Reverificado en el navegador** a 390 px con UTMs en la URL, caminando los 27 clics hasta la oferta: `TODO ESTO DE $ 38.999 / POR SOLO / $ 17.990`, los dos CTA al checkout propio, cero desborde, cero imágenes rotas, cero errores de JS.
- 🆕 **Regla nueva en [[quizzes-reglas-de-armado]]: el caminador por código tiene que respetar el `disabled`.** El recorrido se colgó dos veces (82 clics en una opción, después 82 en un `Continuar` apagado) antes de que saliera el orden correcto: input → `[data-next]` no `disabled` → primera `.opt` → esperar. Y el bucle largo va lanzado en segundo plano contra `window.__st`, porque un `javascript_tool` que espera 70 s muere con `Detached while handling command`.

## 2026-11-10 (5ª pasada) — El Secreto de la Chía: el checkout propio del quiz argentino

- Pedido de Santiago: *"Este es mi checkout, agregalo https://el-secreto-de-la-chia.impultienda.ar/checkout"*.
- **Verificado 200 con `curl -sIL` antes de tocar nada** (regla de Tai Chi Fit) y cambiado en el único lugar donde vive la URL: `QUIZ_CONFIG.checkout`. Rehechos el `.txt`, el `.html` y el `PRUEBA.html`, más la copia en OUTPUTS y el portapapeles.
- **Comprobado en el navegador** a 390 px, recorriendo el quiz entero: los dos CTA del último paso (`QUIERO EMPEZAR 🥰` y `¡QUIERO EMPEZAR AHORA! 🔥`) salen con el checkout nuevo, cero desborde y cero errores de JS en el camino hacia adelante.
- 🐞 **Encontrado un bug del motor, en las dos versiones (AR y BR):** en las pantallas de carga el `setInterval` de la barra se limpia solo dentro del `setTimeout` final, y esos pasos llevan la flechita de volver. Tocando `‹` ahí, el intervalo tira un error cada 100 ms (**82 medidos**) y a los 8,5 s el `setTimeout` **arrastra a la persona a la oferta aunque había vuelto atrás**. **No se tocó** — el pedido era el checkout — y quedó anotado en [[secreto-de-la-chia]] y en [[quizzes-reglas-de-armado]].
- ✏️ **Corrección de lo que dije en la pasada anterior:** había anotado que esos errores de JS los inventaba mi recorrido del iframe. El recorrido ensucia la medición, pero el error era real. La regla quedó reescrita: un error repetido se persigue hasta el stack antes de descartarlo.

## 2026-11-10 (4ª pasada) — Keywords de "generar ingresos" en Brasil: tanda nueva

- Pedido de Santiago: *"Dame palabras clave en brasil para buscar ofertas de generar ingresos"*, y después *"Necesito palabras nada mas, no me armes una investigacion"*.
- **8 keywords que pescan**, ninguna repite las 9 del banco del 8/11: `material completo` (9.100), `aulas gravadas` (5.000), `com as próprias mãos` (4.700), `produzir e vender` (670), `sem nenhuma experiência` (360), `sem patrão` (210), `tabela de precificação` (180), `vender por encomenda` (170).
- **Tachadas con el motivo:** `com certificado por apenas` (18, frase de 4 palabras), `montar seu negócio` (mayoristas y institutos de belleza locales), `quanto cobrar pelo` (todo QuintoAndar), `qualquer pessoa aprende` (ecommerce y marca personal).
- 🆕 **Regla técnica nueva en [[caza-de-ofertas]]: las keywords NO se corren por la API de la Biblioteca.** `ads_library_search` no tiene frase exacta y rankea por relevancia solo las primeras filas: las 6 primeras pruebas volvieron 100 % DramaBox, Vega TV y AI-Talera. Hay que correrlas en la **UI con `search_type=keyword_exact_phrase`**, y el conteo se lee del DOM después de que el SPA resuelve la consulta (el HTML que devuelve `fetch` no lo trae, y el endpoint viejo `async/search_ads` da 404).
- Nuevo: `OUTPUTS/2026-11-10-keywords-br-ingresos-tanda-nueva.md`.

## 2026-11-10 (3ª pasada) — El Secreto de la Chía: la versión argentina del quiz, autocontenida

- Pedido de Santiago, después de que le recordara el quiz brasileño: *"necesito que hagamos exactamente el mismo quiz pero en español argentino"*.
- **El quiz argentino ya existía y es el original.** Corre en `chauinflamacion.com/pages/chia` y **ya estaba entero en voseo**: los únicos `puedes` del HTML en vivo son strings del tema de Shopify. No hubo traducción — lo que faltaba era el **mismo paquete que se armó para Brasil el 9/11**, pero argentino.
- **Diff contra el brasileño: 139 líneas**, todas de idioma, marca, precio, checkout y la variable `Bs` del artículo portugués. Mismo motor, **28 pasos** (`TOTAL=29`), las **mismas 10 imágenes**.
- **Entregado:** `~/Desktop/el-secreto-de-la-chia/` con `landing/` (`.txt` de 40 KB para pegar en el `custom_html`, el `.html` y el `PRUEBA.html` de 1 MB con las fotos embebidas) e `imagenes/` con las 10 fotos renombradas en castellano. Copia en `OUTPUTS/2026-11-10-quiz-el-secreto-de-la-chia-ar.html` y en el portapapeles.
- ⚠️ **Checkout pendiente:** Santiago dijo *"después te lo paso"*, así que quedó el que corre hoy (`chauinflamacion.impultienda.ar/checkout/chia`). Vive en un solo lugar del CONFIG y los dos CTA lo leen de ahí: cambiarlo es una línea, y se verifica con `curl -sIL` antes de entregar.
- **Verificado** por código en un iframe de 390 px: los 28 pasos hasta la oferta, cero desborde, cero imágenes rotas, cero errores de JS, todos los `.btn` centrados y los dos CTA saliendo del CONFIG.
- **Regla nueva en [[quizzes-reglas-de-armado]]:** recorrer el quiz dos veces en el mismo iframe inventa errores de JS que no existen. Antes de cada verificación se recarga con `?x=Date.now()`.

## 2026-11-10 (2ª pasada) — Carteras Maison: oferta nueva para Argentina, clonada de Maison Luxe Bags

- Pedido de Santiago: *"Quiero que hagamos ahora anuncios para esta otra oferta… Esta oferta es para Argentina. Seguí los mismos procesos que seguimos en toda para hacer los 6 testeos"*, con el link de la Biblioteca de Anuncios de `maisonluxebags.impultienda.ar`. Nombre del producto, decidido por él: **"Usa el original, carteras maison"**.
- **Radiografía del competidor** (Maison Luxe Bags / *The Riviera Method* de Sophie Hart, US$27 con ancla US$54): **55 ads activos**, el más viejo del **28/10** → 13 días, y **490 ads contando los muertos**. Corre en **ImpulTienda**, igual que nosotros. Se bajaron y transcribieron sus **14 ads de más impresiones**.
- **Arbitraje confirmado:** el mismo producto ya corre en `maisonluxebags-italy` y `maisonluxebags-japan`, pero **no en español**. La búsqueda `cañamazo` en todo el mundo devuelve 37 ads y son escuelas de bordado y capacitaciones por WhatsApp: ningún infoproducto low ticket con checkout.
- **Lo que repite en sus 55 ads:** **dos cuerpos fijos** con el hook rotando. Cuerpo A = *"una cartera por noche"* (salió del laburo en un local, la cuenta con el planificador, la renuncia). Cuerpo B = *"el secreto no es el material, son los detalles"* (cañamazo firme, cada agujerito tapado, forro adentro, herrajes dorados). Más materiales/objeción, día en mi vida, la apuesta de 3 días y la variedad de modelos.
- **Tanda 1 de 6 guiones**, uno por familia, en **voseo argentino** y con situaciones locales (la mercería, la plaza, el colegio, la mesada). **Etsy afuera** (el original manda a Amazon y Etsy). La cifra va en pesos porque es un solo país: la cartera a **cincuenta mil pesos** — ⚠️ a validar con Santiago.
- **Se clonó también la edición:** subtítulos de **2 palabras en mayúscula** con la palabra activa en **magenta #D4356F sin caja**, placas de texto arriba, los **insertos del producto dibujados por código** (`gfx_carteras.py`: la tapa del libro con carteras reales, la página de 250+ moldes en 5 capítulos, la lista de materiales, los 5 bonos y el celular) y placa de cierre tinta → vino con el celular adentro.
- **Pool de TikTok:** 87 ids de `#plasticcanvasbag` y `#plasticcanvas`, 60 bajados y revisados a 1,5 s. Quedaron **22**. Se cayeron los de cara a cámara, los de subtítulo quemado y, sobre todo, **seis creadores que promocionan su propio curso o kit** (*"Aprende ingresando al link de mi perfil"*, *"Comenta MALLA y aprende"*, *"SEMINARIO PRESENCIAL de Plastic Canvas"*, *"DM/WHATSAPP TO ORDER"*): el nicho del b-roll también vende cursos, igual que en pisos epoxi.
- Voz **Sulafat** por API a `speed 1.30`, cama `bed_activo`. V1–V4 con `gemini-2.5-flash-preview-tts`; **V5 y V6 dieron 429 y salieron con `gemini-3.1-flash-tts-preview`**, verificadas con Whisper: arrancan por la primera palabra del guion, sin leer el Style.
- Nuevo: `WIKI/carteras-maison.md`, `OUTPUTS/2026-11-10-guiones-carteras-maison-tanda1.md`, `OUTPUTS/2026-11-10-descripcion-carteras-maison.md`, `OUTPUTS/scripts-vsl/{gfx_carteras.py, edit_carteras.py, gen_carteras_plans.py, vent_carteras.py}`. Entrega en `~/Desktop/carteras-maison/anuncios/`.
- ⚠️ Pendiente: **falta la landing en español** (los guiones y el inserto se escribieron contra la del competidor) y el backend post-compra.

## 2026-11-10 — Pisos Epoxi: oferta nueva LATAM a $17, clonada de Hands & Home

- Pedido de Santiago: *"Vamos con una oferta nueva… quiero que hagamos anuncios para LATAM… con buena edición, sacando todo lo ganador… el producto lo vamos a cobrar $17"*, con el link de la Biblioteca de Anuncios de `handshome.impultienda.ar`.
- **Radiografía del competidor** (Emma Girard / Hands & Home, *The Epoxy Floor Playbook*, US$26.99): **61 ads activos**, el más viejo del **6/10** → 35 días. Corre en **ImpulTienda**, igual que nosotros. Se bajaron y transcribieron sus **10 ads de más impresiones** y se armó la hoja de contactos de su edición.
- **Lo que no cambia en sus 61 ads:** una sola descripción y un **bloque de producto idéntico palabra por palabra**. Lo único que rota es el hook, en **6 familias**: el 80% antes de abrir el tarro (3 de 10 = la principal), el vecino al que se le levantó, el que vive de arreglar pisos ajenos, el pintor que dice "no hago pisos", un garage/un fin de semana y la ventana que se cierra.
- **Tanda 1 de 6 guiones**, uno por familia, con **cuerpo y cierre propios** (regla del 22/10: del ganador se toma el ángulo, no la plantilla). Español **neutro** y **cero cifras en moneda** porque sale a varios países (regla del 8/11): el margen va como múltiplo. El `$17` queda para la landing.
- **Se clonó también la edición:** subtítulos de 3 palabras con la palabra activa en **cobre #C06A2C** sin caja, chips oscuros arriba, **pastillas blancas con cruz roja** para los defectos, panel "EL SISTEMA" que se va tildando, los **insertos del producto dibujados por código** (`gfx_epoxi.py`: la página paso a paso con fotos reales de los clips, la Tabla de Soluciones, la tabla de cuánto cobrar, los 3 bonos y el celular) y placa de cierre marrón → cobre con el celular adentro.
- **Pool de TikTok:** 61 clips bajados de `#pisoepoxi` y `#epoxyfloor`, revisados a 1,5 s + mitad inferior. Quedaron **30**, y de dos de ellos se acortó la ventana. Se cayeron los de subtítulo quemado, los de marca de agua centrada y **una cuenta entera de renders de IA** (pisos con nubes adentro, árboles sumergidos): llamativos pero no son trabajo real.
- **La hoja de contactos del render atrapó cinco cosas que la del pool no:** un clip que a los 27 s levanta un cartel con **la tapa de otra guía de pisos** ("Puedes aprender con nuestro Libro digital…") y un `BEFORE` en inglés que entra a los 21 s. También un clip con **publicidad de otro infoproducto de pisos** en pantalla ("Puedes aprender con nuestro Libro digital" + la tapa de una guía de porcelanato líquido), dos con **carteles del creador** a mitad del clip ("Si te interesa saber más acerca de resina epóxica SEGUINOS", "Limpiamos bien la superficie"), uno con **marca de agua centrada** que el zoom no alcanza, un operario con **"EPOXY LIKE A PRO!" en la espalda** (texto en inglés en un ad en español) y un clip que **arranca en negro**. Los que repiten el cartel se cayeron enteros; a los demás se les acortó la ventana. Hicieron falta **tres rondas de render** para llegar a los 6 limpios. Regla nueva en [[guiones-y-anuncios]].
- Voz **Orus** por API (`gemini-2.5-flash-preview-tts`) a `speed 1.30`, cama `bed_activo`. Videos de 38 a 44 s.
- Nuevo: `WIKI/pisos-epoxi.md`, `OUTPUTS/2026-11-10-guiones-pisos-epoxi-tanda1.md`, `OUTPUTS/2026-11-10-descripcion-pisos-epoxi.md`, `OUTPUTS/scripts-vsl/{gfx_epoxi.py, edit_epoxi.py, gen_epoxi_plans.py, vent_epoxi.py}`. Entrega en `~/Desktop/pisos-epoxi/anuncios/`.
- ⚠️ Pendiente: **falta la landing en español** (el inserto y los guiones se escribieron contra la del competidor traducida) y el backend post-compra.

## 2026-11-09 (7ª pasada) — Origen Pilates: el .txt del quiz listo para ImpulTienda y la descripción de la tanda

- Pedido de Santiago: *"Necesito que me des el txt del quiz de origen pilates. Y necesito que me des una descripcion para los ads"*.
- **Se cerraron los tres pendientes del quiz antes de generar el .txt**: checkout propio verificado (`origen-pilates.impultienda.ar/checkout` → 200, los 4 CTAs del paso 19 pasan por `comprar()`), **voseo cerrado** (20 formas de tuteo heredadas del original traducido) y **claims de kilos afuera** (se cayó *"de 75 a 71 kg en 28 dias"* y *"resultados visibles en 28 DIAS"*).
- **Dos cosas que el clon traía y no se veían leyendo el HTML**: las cuatro reseñas con **nombres italianos** (Francesca Rossi, Laura Bianchi…), ahora con nombre + ciudad argentina; y los **sliders en 180 cm / 70 kg** (hombre promedio) para una oferta de mujeres +40, ahora 160 / 72 / 65.
- **El .txt bajó de 3,2 MB a 1,24 MB**: `inline_quiz.py` ahora lee `ANCHO_MAX` y `CALIDAD` del entorno y se corrió con 700/74. Sin diferencia visible en el teléfono.
- **Probado los 19 pasos por código** en un iframe de 390 px servido por `http.server`: 29 imágenes sin romper, cero overflow horizontal, la carga de 15 s pasa sola y la oferta se ve al entrar al paso 19.
- **Una sola descripción para los 7 videos** (177 palabras, formato corto del 6/11), igual que Sana Pilates con sus 92 ads: mecanismo de los músculos profundos, 3 bullets, entregables, bonos, garantía y CTA al test. Sin precio, sin kilos, sin plazo de resultado y sin segunda persona sobre el cuerpo de quien mira. Cierra con la estacionalidad pre-verano.
- Nuevo: `OUTPUTS/2026-11-09-descripcion-ads-origen-pilates.md`, `OUTPUTS/2026-11-09-quiz-origen-pilates-fuente.html`; reemplazado `OUTPUTS/2026-11-09-quiz-origen-pilates.html`. Entrega en `~/Desktop/origen-pilates/landing/origen-pilates-quiz.txt` + `origen-pilates-PRUEBA.html` y `~/Desktop/origen-pilates/anuncios/descripcion-ads.txt`.
- ⚠️ Pendiente: el peso objetivo sigue sin previsión con fecha, el resultado del quiz no es personalizado y falta el VSL.

## 2026-11-09 (6ª pasada) — Deco Magic: oferta nueva modelada para LATAM, tanda 1 de 6 videos

- Pedido de Santiago: *"te mando una nueva oferta que está en el mercado inglés y quiero modelarla para el mercado de LATAM… vamos a hacer 6 anuncios de testeo… español neutro como LATAM"*, con el link de la Biblioteca de Anuncios de `www.decomagic.shop`.
- **Radiografía del competidor** (Magic Deco / DECO MAGIC, Amaya Digital LLC): ~35 ads activos en dos páginas, el más viejo del 26/10, $17/$37, landing en 6 idiomas. Se bajaron y transcribieron sus **10 ads de más impresiones** y se armó la hoja de contactos de su edición.
- **La DNA que repiten los 6 ganadores:** hook de una línea → el mecanismo en cuatro verbos (*escribís la temática → aparece el set completo → le cambiás el nombre en Canva gratis → imprimís en casa*) → enumeración de piezas → lista de "no" → el catálogo como prueba → cierre literal. **Cero cifras de plata en el audio** y **nunca nombran una marca registrada**.
- **Dos avatares en paralelo:** la mamá que organiza el cumpleaños y la que vende decoración de fiestas. El ad de más impresiones es del lado bizop. La tanda sale 4 + 2.
- **Se clonó también la edición:** pastillas rosas redondeadas arriba, subtítulos blancos de 3 palabras con la palabra activa adentro de una **caja magenta**, inserts de la app y de Canva anclados a la palabra, y placa de cierre con su degradado **#7E3D96 → #E74FA4** (`edit_deco.py`, `gfx_deco.py`).
- **Español neutro sin voseo** y **sin cifras en moneda** (LATAM multipaís, regla del 8/11). Voz Sulafat; V6 salió con `gemini-3.1-flash-tts-preview` porque el 2.5 dio 429.
- **Pool de TikTok:** 154 clips de 7 tags (`#mesadedulces`, `#cajitasdedulces`, `#golosinaspersonalizadas`, `#souvenirspersonalizados`, `#toppersparatortas`, `#imprimiblesparafiestas`, `#bolsitasdegolosinas`), revisados a 1,5 s + verificación a 1 s de cada ventana. Quedaron **28**. Se cayeron las mesas de pastelería fina (no muestran lo que vendemos) y un clip con una **Cricut** en pantalla, justo cuando el ad dice que no hace falta máquina de corte.
- Nuevo: `WIKI/deco-magic.md`, `OUTPUTS/2026-11-09-analisis-deco-magic.md`, `OUTPUTS/2026-11-09-guiones-deco-magic-latam.md`, `OUTPUTS/2026-11-09-descripcion-ads-deco-magic.md`, `OUTPUTS/scripts-vsl/edit_deco.py`, `gfx_deco.py`, `gen_deco_plans.py`, `vent_deco.py`. Entrega en `~/Desktop/deco-magic/anuncios/` (`9-11 - 1` a `9-11 - 6`).
- ⚠️ Pendiente: falta la landing y el nombre del producto propio. Los guiones dicen "la app" y los inserts salieron sin marca.

## 2026-11-09 (5ª pasada) — Piedras: tres anuncios más en portugués (BR6–BR8)

- Pedido de Santiago: *"ahora haceme estos 3 ads en portugues, exactamente iguales pero en portugues"*, con tres MOV/MP4 de Scented Stones en inglés.
- **Clonados 1:1**: misma imagen, misma cama de audio, misma duración (58,20 / 44,29 / 36,60 s). Lo nuevo es la voz Sulafat brasileña y los subtítulos en portugués.
- **Los tres originales tenían estilos de subtítulo distintos**, así que cada uno se midió aparte: karaoke de mayúsculas con palabra amarilla (BR6), píldora magenta con palabras que se suman (BR7) y píldora magenta con una palabra grande por vez (BR8).
- **Tres trampas nuevas, anotadas en [[internacionalizacion]]:** la fuente se identifica por el ancho de una frase a altura de mayúscula fija (ganó Nunito 800 para BR6 y Montserrat ExtraBold 148 para BR8); la franja de inpaint tiene que tener **altura par** o libx264 corta el pipe; y `demucs` sin `--two-stems=vocals` no deja `no_vocals.wav` — se arma sumando bass+drums+other.
- Voz: dos tomas por anuncio verificadas con whisper medium; se eligió la `a` en los tres (tempos 1,03 · 1,01 · 1,05).
- Nuevo: `OUTPUTS/2026-11-09-guiones-piedras-portugues-BR6-BR8.md`, `OUTPUTS/scripts-vsl/render_pt2.py`. Entrega en `~/Desktop/scented-stones-ad/anuncios/portugues/`.

## 2026-11-09 (4ª pasada) — DanceGo: tanda 3, tres renovaciones del ganador

- Pedido de Santiago: *"Necesito que hagamos mas renovaciones para dancego. 3"*.
- **Tres renovaciones del mismo ganador** (`6-11 - 1`, "Hay un gimnasio adentro de la tele de tu living") con el **cuerpo validado copiado textual** y **tres formatos de hook distintos**: pregunta del cliente ("¿y si no sé bailar?"), storytime en primera persona (la puerta del living cerrada) y lista de tres (lo que no necesitás). La tanda del 7/11 habían sido cuatro declaraciones sobre el mismo objeto, que es lo que el checklist del 27/10 marca como error.
- **Estética nueva**: caja de subtítulo crema sobre tinta / ciruela / petróleo, tres ritmos de corte y 2, 4 y 3 palabras por placa. Los tres abren con living.
- **Pool ampliado sin bajar un solo clip**: offset +2 s y tope de 9 recortes por clip sobre las ventanas ya revisadas → de ~130 a **228 recortes**. Se revisó el pool entero en hojas de contactos y se vetó **`R1`** (salón con una piñata colgando).
- **Dos reglas nuevas** en [[renovacion-de-creativos]] y en [[dancego]]: la palabra que ancla la placa final se elige entre las que aparecen **una sola vez** (el `end` del video 1 arrancó en el segundo 6 porque el hook repetía "mirá"), y el texto quemado de un clip no es motivo de veto si el `zoom` con `ybias 1.0` lo recorta.
- Voz Sulafat por API (`gemini-2.5-flash-preview-tts`, speed 1.30), acento verificado con **`gemini-3.5-flash`** (el `2.5-flash` ya devuelve 404 para cuentas nuevas).
- Nuevo: `OUTPUTS/2026-11-09-guiones-dancego-tanda-9-11.md`, `OUTPUTS/scripts-vsl/gen_dancego_plans_9.py`. Entrega: `~/Desktop/dancego/anuncios/9-11 - 1` a `9-11 - 3`.

## 2026-11-09 (4ª pasada) — Origen Pilates: quiz terminado y los dos ads de voz en off rehechos

- **Quiz cerrado:** checkout propio `origen-pilates.impultienda.ar` en los 5 CTA (responde 200), **logo rehecho** (loto más grande, `display:block` a 76 px para que centre de verdad) y **las siluetas dibujadas reemplazadas por fotos reales**: 4 reusadas del quiz de la chía y 9 nuevas en ese mismo estilo de catálogo sobre fondo crema. Las 29 imágenes están en `landing/img/`.
- 🐛 **Bug del cliente de ApiMart:** `bajar()` usaba `curl -C -`, que **continúa** la descarga en vez de reemplazar. Como los archivos ya existían con ese nombre, pegó los bytes nuevos detrás de la imagen vieja y quedaron corruptos (una silueta de 10 KB pesando 550 KB). Arreglado: borra el destino antes de bajar.
- **Los dos ads de voz en off se rehicieron.** Santiago: *"son muy malos, clips horribles, muy poco variado, todo repetitivo"*. El pool era de 6 clips para dos videos.
- ⚠️ **Medición completa de la caza: 191 clips bajados en 5 tags para 8 limpios.** El nicho de pilates en TikTok está tomado por creadoras que queman el título de la rutina, en todos los idiomas, y `#pilatesemcasa` en portugués se solapa casi entero con el tag en español: la regla de "buscar el producto en otro idioma" no aplica acá. Lo que sirvió fueron `#wallpilates` y `#pilatesathome`, que traen planos de piso de cuerpo entero donde no se lee la edad. Detalle en [[origen-pilates]].
- 🆕 **tikwm entrega de a poco:** un pase da 12 de 75, tres pases dan 47 de 49. Hay que dejarlo correr con reintentos, no darlo por perdido.
- Los 7 videos quedaron con **pico normalizado en −1,3 dB** y de 34 a 41 s.

## 2026-11-09 (3ª pasada) — El quiz de la chia clonado a Brasil

- Pedido de Santiago: *"Necesito que me hagas exactamente este mismo quiz, pero para el mercado de Brasil… con las imágenes, con todo"*, con el link de `chauinflamacion.com/pages/chia`.
- **El quiz viaja en texto plano** dentro de un `custom_liquid` de Shopify: se bajó con `curl -sL` y se cortó desde el primer `<script>` (el comentario de apertura sale repetido 4 veces por Liquid).
- **Las 10 imágenes se reusan tal cual**: hoja de contactos con Pillow antes de planificar nada, y ninguna tiene texto quemado. Eso convirtió el trabajo en una localización de copy.
- **Entregado:** `~/Desktop/o-segredo-da-chia/` con `landing/` (`.txt` para pegar, `.html` y `PRUEBA.html` con las fotos embebidas) e `imagenes/` con las 10 fotos renombradas. Copia en `OUTPUTS/2026-11-09-quiz-o-segredo-da-chia-br.html`.
- Decisiones de Santiago: precio **R$ 67** (tachado R$ 147) y checkout **`https://o-segredo-da-chia.impultienda.ar/checkout`**, que pasó en el mismo día: verificado 200 con `curl -sIL`, puesto en el único lugar del archivo donde vive la URL y comprobado en el navegador que los dos CTA de la última pantalla lo leen.
- **Regla nueva en [[quizzes-reglas-de-armado]]:** al clonar a portugués, una marca que empieza con artículo (*O Segredo da Chia*) duplica el artículo en todos los textos que la nombran después de una preposición. Se resuelve con una variable `Bs` (marca sin artículo) y se detecta por código recorriendo el quiz.
- Página nueva [[secreto-de-la-chia]] con la ficha de las dos versiones; nota de localización sumada a [[internacionalizacion]].
- Verificado en Chrome a 390 px: los 28 pasos, cero desborde, cero errores de JS y los dos CTA leyendo el CONFIG.

## 2026-11-09 (3ª pasada) — Origen Pilates: los 7 ads de la tanda 1 y el quiz sin VSL

- **7 videos entregados** en `~/Desktop/origen-pilates/anuncios/` (`9-11 - 1` a `9-11 - 7`): 5 de avatar IA con Veo 3.1 y 2 de voz en off. **US$4,90 de ApiMart en total.**
- **Se calcó la estructura de escenas de Sana Pilates**, no el molde brasileño: su ad de 53 s son 4 escenas + placa y el de 75 s, 7 + placa, y **el bloque de oferta lo dice siempre la misma presentadora**. Santiago: *"si ellos hacen un video que tiene 3 escenas… lo quiero así"* y después *"en un video se puede máximo 4 escenas, no quiero más que eso"*. Repertorio y reglas en [[origen-pilates]].
- 🆕 **El filtro de Veo rechaza (y no cobra) las referencias con ropa ceñida o color piel**, la mujer sola en un dormitorio y el hombre fuera de cuadro abordando a una mujer en la calle. Se cayeron 5 tomas; con ropa holgada pasan. Las imágenes de referencia van siempre cubiertas.
- 🆕 **La subida de imágenes se hace en serie y con reintentos.** Subir cinco en paralelo a `/v1/uploads/images` hizo fallar la subida y, como estaba fuera del `try`, se llevó tres hilos en silencio: la tanda "terminó" con 3 de 14 generadas.
- **Ajuste pedido después:** `speed 1.2`, silencios de más de 0,26 s recortados a 0,12 s y **cama `bed_activo`** a −12 dB con ducking, todo re-montado desde las tomas ya generadas (cero créditos). Niveles normalizados a pico −1,3 dB. Los subtítulos se re-alinean contra el audio acelerado, no se estiran.
- ⚠️ **Los tags de pilates en español están podridos para b-roll:** 84 clips bajados, **6 limpios**. Texto de la rutina quemado, hombres, o chicas de 20 que no son el avatar. `#pilatesemcasa` en portugués se solapa casi entero con el español, así que esta vez la regla de "buscar el producto en otro idioma" no sirvió.
- **Quiz sin VSL** y con la oferta de entrada (`SEGUNDOS_OFERTA: 0`), **precio $9.990 y 3 cuotas de $3.330**, y **las 29 imágenes rehechas de cero**: 17 por código (logo, siluetas, mockup, placas) y 12 fotos con nano-banana. Entregable en `OUTPUTS/2026-11-09-quiz-origen-pilates.html`.
- Pendientes: el checkout nuevo, pasar el quiz a voseo cerrado y sacar los claims de kilos que venían de la versión vieja.

## 2026-11-09 (2ª pasada) — Origen Pilates: despiece de los ads y la tanda 1 con Veo 3.1

- Santiago cerró las decisiones: nombre **Origen Pilates**, precio **$7.999**, y la tanda 1 con **5 videos de avatar IA (Veo 3 por [[apimart]], créditos que él cargó) + 2 de voz en off**. Pidió analizar los ads a fondo antes de generar nada.
- **Despiece frame por frame en `OUTPUTS/2026-11-09-despiece-ads-sana-pilates.md`:** 22 videos con detección de cortes, medición de audio y de ritmo, el estilo exacto de subtítulo, el banco de píldoras, las 7 aperturas que usan, el mecanismo en sus palabras y la lista de lo que no se copia.
  - **Ritmo real: 166 palabras por minuto de mediana** (rango 138-190). Nuestra regla decía 150 y el molde brasileño iba a 185: los guiones de esta oferta se calculan a **170 ppm**.
  - ⚠️ **Corrección al supuesto de partida:** sus ads **no** son "casi todos con IA". Verificado en resolución grande, lo único generado es el bloque de la profesora en la cocina (se delata por la mano con los dedos fusionados y por los planos de 7,4 a 9,9 s). La presentadora del sillón, Marta de 63 y la entrevista del shopping son **personas reales**. El 100 % IA es el competidor brasileño.
- **Guiones de la tanda 1** en `OUTPUTS/2026-11-09-guiones-origen-pilates-tanda-1.md`: 7 guiones de 44 a 50 s, sin kilos, sin plazos de resultado y sin segunda persona sobre el cuerpo.
- **Receta de video validada con una prueba antes de la tanda** (anotada en [[origen-pilates]]): `veo3.1-fast`, 8 s, 9:16, `generation_type: frame` desde una imagen de referencia, **US$0,14 la toma**; imágenes con `gemini-nano-banana-2.1-ext` a **US$0,014**. El clip de prueba salió con manos correctas, lipsync bueno y el texto exacto.
  - 🆕 **La subida de imágenes va por `POST /v1/uploads/images` del propio ApiMart** (multipart, campo `file`). No hace falta catbox ni ningún host de terceros. `image_urls` rechaza los data URI en base64.
  - 🆕 **Un clip de 8 s entra 23 a 25 palabras**, así que un video de 6 tomas son ~130 palabras y ~48 s.
  - 🆕 **Para una escena con dos personas se genera una imagen de escena** pasando los dos retratos como `image_urls`: así el "día 1" y el "día 28" salen con el mismo departamento, el mismo encuadre y la misma madre.
- Carpeta renombrada a `~/Desktop/origen-pilates/` y quiz dejado en `landing/quiz.html` para que lo mire.
- Página de la WIKI renombrada a [[origen-pilates]] con las decisiones y la receta de producción.

## 2026-11-09 — Pilates Asiático: Sana Pilates desarmada y el nicho en Brasil

- Santiago pasó la Biblioteca de Anuncios de **Sana Pilates** (AR) para armar una oferta de pilates propia, con el mismo quiz y mejor diseño, y pidió analizar el nicho en Brasil y en Argentina y decidir qué hacer con los anuncios (los de ellos son casi todos con IA).
- **El hallazgo que cambia el encuadre: no es una oferta nueva.** Sana Pilates es la misma oferta que ya está armada como [[pilates-hormonal]] desde el 12/10 (el índice ya decía "modelado de Sana Pilates"): los **tres bonos coinciden palabra por palabra**, igual el reto de 28 días, el avatar, el mecanismo del abdomen profundo y la garantía. Lo que falta definir es nombre, precio y la tanda de ads.
- **Página nueva [[origen-pilates]]** y análisis completo en `OUTPUTS/2026-11-09-analisis-pilates-asiatico-sana-pilates.md`.
- **La ballena:** página `982998884899600`, **~92 ads activos**, el más viejo del **26/8** (75 días), **un solo primary text para los 92**. Quiz en **InLead** sobre `sanaspilates.com` con cloaker, checkout en **Shopify** + Mercado Pago, **$7.999 ARS** (ancla $39.000, 3 cuotas de $2.666), **sin VSL**. Están **solos en la categoría en AR** (los 28 resultados de "pilates asiático" son suyos) y **perdieron un dominio con los ads corriendo**: `sanapilates.com` hoy es un parking de GoDaddy.
- **Quiz de 17 pasos mapeado paso por paso**, con las 9 cosas a corregir al clonarlo (el idioma baila entre vos/tú/usted, faltan tildes, los sliders arrancan en 180 cm y 70 kg, el peso objetivo no calcula nada, el resultado no personaliza, no hay VSL).
- **22 videos bajados y transcriptos**, 8 familias de creativos identificadas. **El hallazgo grande: no escriben guiones, permutan píldoras** — un banco de ~15 micro-clips de 5-10 s que se reordenan, siempre con el mismo bloque de oferta al final. Por eso sostienen 92 anuncios con un solo copy.
- **Brasil:** "21 Day Challenge" (241 ads) **no es modelo**, es BetterMe. El que sí importa es **"Calistenia Japonesa 28 Dias"** (50 ads en 5 días), con **mini-novelas 3D estilo Pixar 100 % IA**, y **"Camila Oliveira"** (14 ads, arrancó hoy) con el **ángulo de la vergüenza** que falta en Argentina.
- **Plan de ads propuesto:** tanda de 6 en 3 carriles (mini-novela 3D con IA ×2, avatar IA a cámara de 90 s ×2, voz en off sobre TikTok ×2), más la estacionalidad de pre-verano que ellos ya usan y nosotros no.
- Material en `~/Desktop/pilates-asiatico/anuncios/competidor/` y `/competidor-br/`.

## 2026-11-08 — Piedras BR5: el ad «I never» clonado a portugués

- Santiago pasó `~/Downloads/i never.mp4` (20,67 s, 1080x1920) y pidió el mismo video en portugués, tal cual. Se reusó la imagen y la cama del fuente: no se tocó ni un corte.
- **Formato nuevo de subtítulo** (no es el de BR1–BR4): Courier Bold blanco con contorno negro y palabra activa en amarillo, bloques de hasta 2 líneas de 24 caracteres. Se midió sobre el original (28 px por carácter, interlineado 56, baselines 1429/1485/1457, amarillo #EBD414) en vez de inventarlo.
- Guion inglés leído de los subtítulos quemados; el original termina cortado en «Inside is the exact formula» y se dejó igual.
- Voz Sulafat, 4 tomas (27,20 / 25,24 / 23,64 / 26,12 s): la b dijo «pra» y «tá» en vez de «para» y «está» → se usó la c, la más corta y fiel, tempo 1,152. 80/80 palabras alineadas.
- Entrega: `~/Desktop/scented-stones-ad/anuncios/portugues/SS-PT-5-nunca-quis.mp4` + `OUTPUTS/2026-11-08-guion-piedras-portugues-BR5.md` + script en `OUTPUTS/scripts-vsl/render_never_pt.py`.

## 2026-11-08 — Piedras: los hooks en inglés de los 4 videos de Brasil

- Santiago pidió los hooks en inglés de los 4 ads que se localizaron a portugués (BR1–BR4). No estaban escritos en ningún lado: los originales son los 4 MP4 de `~/Downloads` y los guiones ingleses nunca se transcribieron.
- Se leyeron de los **subtítulos quemados** de cada fuente (frames cada 0,4 s recortados a la banda de subtítulos), sin whisper: `I'm 58 and I'd never sold a thing in my life…` · `In the next 30 seconds…` · `My accountant called me yesterday, worried…` · `Okay, I need to tell you guys this story…`
- Entrega: `OUTPUTS/2026-11-08-hooks-ingles-piedras-brasil.md`, EN + ES con voseo, enlazado en `WIKI/index.md`.

## 2026-11-08 (46ª pasada) — Keywords de los 3 nichos de siempre, y la vara de qué es un buen nicho

- Santiago, sobre el banco de los 4 nichos nuevos: *"Muy malos nichos, quiero de bajar de peso, ingresos extra y manifestacion, pero no me des tantas, maximo 10 por nicho"*. Queda como regla: **no se proponen nichos nuevos** y un nicho con mucho volumen no es bueno si él no lo vende.
- 22 keywords corridas en la Biblioteca. Entrega: **10 / 9 / 10** con el número de ads activos y la oferta que destapa cada una.
- **Emagrecimento:** la puerta es la **receta en PDF** — `receitas na airfryer` (877) y `receitas proteicas` (576) dan R$10 con el mismo título repetido 8 a 15 veces; `mounjaro natural` (680) sigue viva.
- **Manifestação:** `mapa astral` (931) es lo más low ticket del día, **R$9,00 / R$27 / R$29,90 en el título**, varias páginas corriendo lo mismo; `lei da atração` (986) destapa la flota de Kamily Rebelatto en 4 fanpages.
- **Renda extra:** quedan las 8 generales validadas el 05/11 más `uma profissão em casa` (3.686). Son 9 a propósito.
- **Muertas:** `ozempic caseiro` (0), `áudio subliminar` (1), `oração a Santo Expedito` (4), `numerologia do nome` (222.226 de basura), `carteira do dinheiro` (305.599), `hora espelhada` y `quem nunca vendeu nada` (microdramas), `cardápio de 7 dias` (apps de delivery).
- Nuevo: `OUTPUTS/2026-11-08-keywords-br-peso-ingresos-manifestacion.md`. Actualizado: `WIKI/caza-de-ofertas.md`, `WIKI/index.md`.

## 2026-11-08 (45ª pasada) — Keywords de Brasil: 4 nichos nuevos y la corrección de que keywords no es cazar

- Pedido de Santiago: *"Dame palabras clave para buscar ofertas low ticket en Brasil, las mejores palabras, Quiero que me des de los mejores 4 nichos"*.
- **Los 4 nichos nuevos** (ninguno estaba en los bancos del 12/10, 26/10, 27/10, 29/10 ni 05/11): **infantil imprimible** (`atividades para imprimir`, 7.051 ads), **fe / infantil cristiano** (`ministério infantil`, 882; `escola bíblica dominical`, 246; `devocional para imprimir`, 219), **material para profesionales** (`alinhado à BNCC`, 638; `recursos terapêuticos`, 1.071) y **cocina que da plata** (`receitas para vender`, 4.842; `salgados para vender`, 569).
- Las 22 keywords se corrieron una por una en la Biblioteca: el banco separa las que pescan de **las 9 que probé y no sirven**, con el motivo de cada una.
- **Tres reglas nuevas de keywords:** 2-3 palabras (la frase larga devuelve 8 resultados); la frase emotiva en primera persona está **quemada por los microdramas** (DramaBox compra todo el inventario de "meu filho não fala"); terapia, dolor y adiestramiento son **servicio local**, así que al infoproducto se entra por el formato o por el profesional que lo compra.
- **Corrección de Santiago, anotada como regla:** *"Acordate que solo te pedí palabras clave, no la skill cazar"*. Le había sumado candidatas, filtro madre y links de fanpages; se recortó el archivo y queda la regla de que un pedido de keywords se entrega como keywords y nada más.
- Nuevo: `OUTPUTS/2026-11-08-keywords-brasil-4-nichos-nuevos.md`. Actualizado: `WIKI/caza-de-ofertas.md` (dos registros del 08/11), `WIKI/index.md`.

## 2026-11-08 (44ª pasada) — Nail Designer: radiografía de la ballena brasileña de uñas y tanda 1 de 6 ads en inglés

- Pedido de Santiago, con el link de la Biblioteca de Anuncios: *"Tengo una nueva oferta… 6 anuncios para testear… la vamos a tirar en Inglés, acordate del acento… agarremos todo lo validado, todo lo ganador… no inventar la rueda… sacá los b-rolls de TikTok… es una marca personal la que lo ofrece, lo importante que agarramos acá es los anuncios"*.
- **La oferta:** curso de **alargado de uñas** de **Fabiana Rodrigues** (Brasil), R$9,90 el plan básico y R$25 el Pro, destino `fabianajunyarodriguesnails.com`, hero *"Faça unhas de casa e fature de R$3 a R$5 mil por mês"*.
- **Radiografía:** **162 ads activos** y el más viejo del **9 de junio** — cinco meses corriendo, la pieza más longeva que vimos en una caza. Se bajaron y transcribieron los **10 de más impresiones** y se armaron sus hojas de contacto.
- **Las 4 familias:** "en una hora, sin curso de dos mil reales" (5 de los 10 ads, es el whale) · "sin empleo, sin plata: antes de mandar el próximo currículum" · "una clienta te paga R$120 por un alargado y aprender te sale menos de 10" · tres **demos técnicas** puras (cuadrada perfecta, el punto cero, el mínimo de lijado) que recién al final pivotean a la oferta.
- **Su DNA:** el número siempre es el **precio de mercado del servicio**, nunca un ingreso prometido; el precio del curso se ancla contra *"menos que un lanche"*; *"desde cero, aunque nunca hayas hecho un alargado"*; entregables con nombre (15 clases, certificado internacional, guía para atraer clientas); escasez dura de **"solo 5 vagas"**; 19 a 47 s.
- **La edición clonada:** el whale es **100 % macro de la uña en construcción** — ni una cara, ni una placa, ni un subtítulo, ni una foto fija. Nuestra versión mantiene el visual y suma subtítulos de 3 palabras con **un color de caja por creativo**, una sola cama y pastilla de CTA, sin placa oscura.
- **La tanda:** 6 guiones, uno por hook, en **inglés y español con voseo**, con la cifra como precio de salón (sesenta a noventa dólares la mano) y nunca como ingreso prometido.
- **El b-roll:** 76 clips bajados. **`#polygelnails` se midió medio podrido** (academias hispanohablantes con subtítulos quemados); **`#nailextensions` es el bueno** para mercado inglés. Pool final de **42 ventanas**. Tres clips se cayeron recién en la hoja de contactos del render (`DND #880`, `Save & Subscribe`, `Builder Gel`) y se recortaron o sacaron.
- **Voz Sulafat** por API, estilo mujer estadounidense de 35, `speed 1.30`. El V6 salió con `gemini-3.1-flash-tts-preview` por cuota del 2.5.
- Nuevo: `WIKI/nail-designer.md` · `OUTPUTS/2026-11-08-guiones-nail-designer-tanda1.md` · `OUTPUTS/scripts-vsl/edit_nails.py`, `gen_nails_plans.py`. Entrega en `~/Desktop/nail-designer/anuncios/` (`8-11 - 1` a `8-11 - 6`).

## 2026-11-08 (43ª pasada) — Quesos: radiografía de Queijo de Casa (BR) y tanda 1 de 6 ads para LATAM

- Pedido de Santiago, con el link de la Biblioteca de Anuncios: *"Tengo una nueva oferta… 6 anuncios para testear… la vamos a tirar en LATAM, acordate del acento… agarremos todo lo validado… no inventar la rueda… sacá los b-rolls de TikTok"*.
- **La oferta:** la **Cartilha Receitas Lucrativas do Leite** (cuadernillo *OURO BRANCO*) de **Queijo de Casa** / Karla Gonçalves, Hotmart, R$67 con ancla R$478, destino `cartilha.queijeiradevalor.com`.
- **Radiografía:** 34 ads activos desde el **8 de octubre**, **todos con el cuerpo del anuncio vacío** (todo el peso en el video). Se bajaron y transcribieron con faster-whisper los **10 de más impresiones** y se armaron sus hojas de contacto.
- **El avatar no es un curioso: es quien ya produce queso y no saca margen.** La landing abre con *"estás cansada de no tener la ganancia que quisieras"* y con el dolor de bajar el precio.
- **Las familias ganadoras:** dejar de pelear precio con queso relleno (el más viejo y el de más impresiones) · el suero que se tira (ricota, crema de ricota, bebida láctea) · diez litros de leche rinden el triple · la carta completa · los cinco rellenos que más vende · el producto que vende todos los días. La mitad de sus creativos son de **contenido** (defectos de maduración, congelar el requeijão) con CTA de seguir.
- **La edición clonada:** POV cenital de manos, el queso relleno cortado al medio como plano héroe, el cuadernillo con un celular encima en la segunda mitad, subtítulos de 3 palabras en mayúscula **blancos sin resalte de color** (a diferencia de meliponicultura), sin placas y sin efectos.
- **La tanda:** 6 guiones en **español neutro con tuteo**, uno por familia, **sin cifras en moneda local** (sale a varios países) y **sin plazo de resultado**, por la regla de bloqueos de LATAM. El rendimiento se cuenta como múltiplo, no en plata.
- **El b-roll:** 396 clips bajados de TikTok. **`#quesorelleno` se midió podrido** (reseñas de supermercado, caras y subtítulos quemados): no entró ni uno. El plano héroe salió de **`#queijorecheado`** — el b-roll sin texto no tiene idioma. Pool final de 26 ventanas de `#comohacerqueso`, `#quesoartesanal`, `#queijorecheado` e `#iogurtecaseiro`.
- **Voz Sulafat** por API, acento latino neutro verificado contra Gemini (*"Colombia, neutro latinoamericano"*), `speed 1.30`. Inserts del cuadernillo dibujados por código (`gfx_quesos.py`).
- Nuevo: `WIKI/quesos-latam.md` · `OUTPUTS/2026-11-08-analisis-queijo-de-casa.md` · `OUTPUTS/2026-11-08-guiones-quesos-latam.md` · `OUTPUTS/2026-11-08-descripcion-ads-quesos.md` · `OUTPUTS/scripts-vsl/gfx_quesos.py`, `gen_quesos_plans.py`, `vent_quesos.py`, `edit_quesos.py`. Entrega en `~/Desktop/quesos/anuncios/`.

## 2026-11-08 (42ª pasada) — Tres skills nuevas de video con IA guardadas e instaladas

- Pedido de Santiago: *"Te voy a adjuntar 3 skills nuevas para que las guardes en el segundo cerebro, y si algún día te pido algo relacionado a las skills, las tengas a mano"* — los zips `skill-antes-despues-ia`, `skill-fruti-novela` y `skill-mini-novela-v2`.
- **Instaladas en `~/.claude/skills/`** (`antes-despues-ia`, `fruti-novela`, `mini-novela`) y ya aparecen en la lista de skills activas: se cargan solas cuando la tarea las toca, no hay que pegarlas en el chat.
- **Las tres hacen un anuncio de punta a punta** (guion → MP4 vertical) generando con **ApiMart** y montando local con ffmpeg: `antes-despues-ia` el formato selfie "día 01 / día 21" con wan2.7-r2v y voz por muestra de referencia (~US$9 por video); `mini-novela` y `fruti-novela` novelas de 3-4 min con **Veo 3.1 Fast** (US$8-12), la segunda en 3D estilo Pixar con personas con cabeza de fruta.
- **Lo más valioso que traen y no estaba escrito:** la **arquitectura de 7 partes** de la novela brasileña (hook de resultado → placa "X MESES ANTES" → la amiga que revela el mecanismo → tomas mudas → **las escenas del antes repetidas pero resueltas** → un tercero pregunta → la experta a cámara) y la variante **"la apuesta"** de la fruti (humillación pública → apuesta con plazo → el intento que falla → mentora → transformación → revancha → CTA). El mecanismo se cuenta **dos veces** en las dos.
- **El truco barato:** reutilizar una novela cambiando **solo el mecanismo** — son las tomas de la mentora y las de la protagonista, se regeneran esas y nada más, **≈US$2** por una novela nueva.
- **Voces cruzadas, el problema central de Veo:** una línea y un solo personaje por toma, `POS` por escena con lugar + ropa (en la fruti, **fruta + ropa**), voces separadas por tono y edad, `voces.py` con speechbrain para marcar CRUCE/GENERO/MEZCLA y `partir.py` para arreglar. Dos frutas del mismo color en una escena = voces cruzadas.
- **Coinciden con reglas que ya tenías:** piloto obligatorio antes del lote, regenerar solo lo malo, bordes por alineación forzada y no por Whisper, cero música y cero SFX, −14 LUFS, y no entregar si el parecido guion/audio baja de 0,97 o si una cara cambia entre tomas.
- **Dónde chocan:** generan la voz pegada al clip (no se puede sustituir por Sulafat/Orus sin romper el labial — es la excepción a [[estilo-de-video-ia]]) y el visual es 100 % IA, no clip de TikTok: son **otro formato**, no se mezclan las dos recetas en el mismo video. Para tandas sigue mandando la regla de 3/6 videos: una novela es **un** creativo, no una tanda.
- **Lo que falta para que estén operativas:** cargar saldo en ApiMart (al 4/11 era US$0,00) y cargar `~/.config/apimart/env` en la shell (`set -a; . ~/.config/apimart/env; set +a` en `~/.zshrc`) — la variable ya se llama `APIMART_API_KEY`, solo no se exporta. Más los requisitos de Python (faster-whisper, torch, speechbrain, librosa).
- Nuevo: `WIKI/skills-de-video-ia.md` · `RAW/2026-11-08-skills-video-ia/` (los 3 zips + los 3 SKILL.md en texto). Actualizado: `WIKI/apimart.md` (cómo la toman las skills, Veo 3.1 Fast y Hailuo 2.3 fuera de tabla) y `WIKI/index.md`.

## 2026-11-07 (41ª pasada) — Meliponicultura: radiografía del original brasileño y tanda 1 de 6 ads para LATAM

- Pedido de Santiago, con el link de la Biblioteca de Anuncios: *"Quiero que hagamos los anuncios para esta oferta, la vamos a tirar en LATAM, hacé el mismo análisis para hacer las mejores variaciones, quiero que copiemos todo lo que le funciona"*.
- **La oferta:** la guía completa de crianza de **abejas sin aguijón** de **Meliponicultura Essencial** (BR), página faceless que manda a `saberessencial.com/meliponicultura`. Detrás está Carlos Almeida (Yraptã), con su propio ecosistema de cursos con marca personal.
- **Radiografía:** 17 resultados, **14 creativos únicos bajados y transcriptos** con faster-whisper. **8 corren desde el 17 de agosto** (casi 3 meses) y renueva de a uno o dos por mes. El cuerpo es **idéntico palabra por palabra en 11 de los 14**: lo único que cambia es el hook.
- **Lo que vende:** **13 de 14 hooks son un error de manejo, no plata** (el agua mal ofrecida, el limón del jarabe, la época equivocada, la caja trampa colgada en cualquier lado, no saber cuándo florece tu región). El entregable que repite en todos es el **calendario de manejo mes a mes**, y el enemigo declarado no es otro curso: es **la información suelta de YouTube y los grupos**. Las dos familias que estrenó en noviembre son floración y caja trampa.
- **La edición clonada:** POV de manos con el cuadernillo en pantalla casi la mitad del tiempo, **siempre abierto en la página que nombra la voz**; b-roll real de meliponario para el resto; subtítulos en mayúscula de pocas palabras con la palabra activa en **verde lima o amarillo sin caja**; y placa roja de cierre. Cero cara hablando a cámara en 14 videos.
- **La ventana en español está abierta entera:** `abejas sin aguijón` da ~26 ads y **ninguno es un infoproducto** (son meliponarios vendiendo miel y cajas); `curso meliponicultura`, 12 resultados y todos en portugués del mismo autor.
- **Tanda 1 entregada: 6 videos de 38 a 47 s**, uno por familia ganadora, en **español neutro con tuteo** y sin una frase repetida entre guiones: el agua bien ofrecida · la época equivocada y el calendario · la caja trampa en el lugar correcto · con cuál especie arrancar · cuándo florece tu región · la renta del patio.
- **Voz Orus** por API; `gemini-2.5-flash-preview-tts` para V1, V2 y V4, y **429 de cuota** → `gemini-3.1-flash-tts-preview` para V3, V5 y V6. Acento latino neutro dirigido desde el Style, `speed 1.30`, verificada con Whisper.
- **Visual 100 % TikTok:** 58 clips bajados de `#meliponicultura` y **23 entraron al pool**. Se cayeron los de texto quemado en portugués (el tag está lleno de meliponicultores brasileños que titulan el video), los de cara a cámara, uno con bandas negras laterales y un meme de chicos bailando.
- **Las 7 páginas del cuadernillo se dibujan por código** (`gfx_meliponi.py`): tapa, calendario mes a mes, floraciones, especies, dónde colgar la caja trampa, el agua y cosecha y venta. **No hace falta que el producto exista para lanzar.**
- **Tres cosas se cayeron en la revisión del render, no en la del pool:** el botón de CTA de V2 enganchaba el primer *"toca"* del guion (*"qué toca hacer"*) y aparecía a los 26 s; el de V3 apuntaba a una ocurrencia que no existía y no salía nunca; y el clip del enjambre volando tenía **una nena en cuadro**. Se corrigieron las anclas, se sacó el clip y se rehízo la tanda entera con `usage.json` borrado y los mismos seeds.
- Nuevo: `WIKI/meliponicultura.md` · `OUTPUTS/2026-11-07-analisis-meliponicultura-essencial.md` · `OUTPUTS/2026-11-07-guiones-meliponicultura-latam.md` · `OUTPUTS/2026-11-07-descripcion-ads-meliponicultura.md` · `OUTPUTS/2026-11-07-visuales-tiktok-meliponicultura.md` · `OUTPUTS/scripts-vsl/gfx_meliponi.py`, `gen_meliponi_plans.py`, `edit_meliponi.py`. Actualizado: `WIKI/index.md`.
- **Entrega:** `~/Desktop/meliponicultura/anuncios/` — `7-11 - 1.mp4` a `7-11 - 6.mp4` (41,4 · 46,6 · 42,0 · 40,8 · 46,0 · 38,1 s), más los guiones, la descripción, el análisis y el listado de visuales.
- Pendiente: la landing y el checkout (la del original es un lead de libro físico con cierre por WhatsApp), el nombre y el precio del producto, y en qué países se abre.

## 2026-11-07 (40ª pasada) — Piedras: los mismos 4 anuncios, ahora en portugués de Brasil

- Pedido de Santiago: *"los videos de piedras, los que te había dicho la última vez que eran los mejores… los mismos que me hiciste para el ruso. Esos quiero que me los hagas en portugués para tirarlos en Brasil. Exactamente los mismos."*
- **Tercer idioma del mismo video ganador** (después del ruso del 2/11 y el polaco del 3/11): misma imagen, misma música, mismos subtítulos quemados y **duración idéntica al original** en los cuatro (40,27 · 50,43 · 42,50 · 63,07 s).
- **No se rehizo nada del video**, como manda la regla del segundo idioma: se reusaron los `band.mp4` y los stems de demucs. Lo único nuevo fue guion + voz + subtítulos.
- **Localización, no traducción:** moneda en **real** (R$ 10.000/mes, piedra a menos de R$ 5, se vende a R$ 30–60), **WhatsApp Business se queda** (en Brasil sí es la referencia, al revés que en Polonia), **amigo secreto** en la lista de ocasiones, y **se sacó "primavera"**: las estaciones están invertidas, así que la urgencia pasó a ser **"antes das festas"** (el Natal). CTA con el botón real de Meta: *Toque em Saiba mais*.
- **Voz Sulafat** por API, `gemini-3.1-flash-tts-preview`, Style que pide explícito *"sem acento de Portugal"*. Dos tomas por anuncio y **se eligió por texto correcto, no por largo**: la toma A del 3 se comía el *minha* de "minha contadora", y la B del 4 decía *mole essencial* y *se eu vindo* — se generaron dos tomas más y la D salió limpia y la más corta.
- **Primera vez con tempos por debajo de 1.0** (0.967 y 0.981 en los anuncios 1 y 3): el portugués salió más corto que el video, así que ahí se elige la toma **más larga**, no la más corta — estirar la voz se escucha más que acelerarla. Tempos finales: 0.967 · 1.279 · 0.981 · 1.087. Palabras alineadas: 136/136, 229/229, 155/155, 250/250.
- **Un defecto encontrado en la revisión, heredado del pase ruso:** el `band.mp4` del anuncio 4 traía un **fantasma rosa** de la caja magenta inglesa. El inpaint TELEA se había comido el núcleo saturado pero no el antialias, y rellenó propagando ese rosa. En ruso y polaco el texto lo tapaba por casualidad; en portugués, con otro largo de línea, quedó a la vista. Se rehizo la banda con la receta de [[habilidades-perdidas]]: máscara del magenta más laxa (de `S>110` a `S>35`) + doble inpaint + blur difuminado. En el primer intento se perdió el filtro de "blanco **y** borde oscuro juntos" y el blur se comió la tela blanca del video: el fantasma se iba pero el fondo quedaba lavado. Con el filtro restaurado, la máscara cubre ~20 % de la banda y las flores y la cuerda siguen nítidas.
- **Insumos durables movidos a `_assets`:** los stems de demucs vivían en un scratchpad de sesión. Ahora están en `~/Desktop/scented-stones-ad/anuncios/_assets/stems/htdemucs/`, junto a las fuentes, y el script los busca ahí.
- Glifos `ã õ ç á é í ó ú â ê ô à` verificados en Bitter, Montserrat ExtraBold y Nunito antes de renderizar: ninguna dibuja tofu.
- Nuevo: `OUTPUTS/2026-11-07-guiones-piedras-portugues-BR1-BR4.md` · `OUTPUTS/scripts-vsl/render_idioma_pt.py`. Actualizado: `WIKI/internacionalizacion.md` (7 correcciones nuevas) y `WIKI/index.md`.
- **Entrega:** `~/Desktop/scented-stones-ad/anuncios/portugues/` — `SS-PT-1-tenho-58.mp4` · `SS-PT-2-trinta-segundos.mp4` · `SS-PT-3-contadora.mp4` · `SS-PT-4-vizinha.mp4`.

## 2026-11-07 (39ª pasada) — A Tu Medida: lectura de la tanda 1 y 3 renovaciones

- Pedido de Santiago, con la captura de los 6 conjuntos: *"hace un análisis profundo, y hagamos las renovaciones… ahí vas a poder ver qué videos están funcionando y cuáles no, para que no repitamos los mismos errores"*.
- **Lectura:** $43,01 de gasto, 4 ventas, ROAS total 1,26, ticket real US$ 14,38. Gana el **CJTO 3 (G5, la cuenta de la modista)** con 3 ventas, CPA $3,82 y **ROAS 3,77**; segundo el CJTO 1 (G2, el cuerpo real) con 1 venta y ROAS 1,94. Los otros cuatro, cero.
- **El hallazgo:** los dos que vendieron **califican al avatar y nombran la plata que ya se está yendo en la primera frase**. Y el mecanismo que Stitched Fits usa en 10 de sus 12 mejores ads ("coser y arreglar son dos habilidades distintas") es el eje de los **tres guiones que vendieron cero** ($19,29 juntos): en AR funciona como giro en el medio, no como hook.
- **Honestidad del dato:** con un CPA real de $10,75, un conjunto sano tiene ~54% de chances de no vender nada con $6 de gasto, y el corte sano son ~$28. Los ceros son direccionales, no una condena ([[lectura-de-resultados]]).
- **Tanda 2 entregada:** V7 la máquina apagada · V8 el placard de plata muerta · V9 el arreglo que pagás a ciegas. Mismo eje ganador, calificador en la primera línea, y estructura, bajada de producto y cierre propios, sin una frase repetida entre ellas ni con el ganador.
- **Estética nueva sin bajar un clip:** se revisaron los 112 del banco. Los 44 de `#clothingalterations` dieron **1 limpio de 44** (thrift-flippers con texto quemado); los 68 sin usar de `#hemming` y `#bridalalterations` dieron **11 limpios**, con los dos bordes de cada ventana verificados a 0,5 s. Como `usage.json` penaliza por uso, los videos se armaron casi enteros con material nuevo (el V8, entero).
- Subtítulos de **4 palabras** (antes 3) y tres colores de caja nuevos: naranja, rojo, turquesa. Script nuevo: `OUTPUTS/scripts-vsl/gen_arreglos_plans_v2.py`.
- **Voz Sulafat** por API, `gemini-2.5-flash-preview-tts`, las tres verificadas con Whisper. El hook del V7 se reescribió: la TTS decía "está apagada" y Whisper (small y medium) leía "está pagada" — en castellano la sinalefa los vuelve homófonos y el hook significaba lo contrario. Quedó "Está tapada con una funda, en un rincón".
- Nuevo: `OUTPUTS/2026-11-07-lectura-tanda-1-a-tu-medida.md` · `OUTPUTS/2026-11-07-guiones-a-tu-medida-v7-v9.md`. Actualizado: `WIKI/arreglos-de-ropa.md`, `WIKI/guiones-y-anuncios.md` (4 reglas nuevas) y `WIKI/index.md`.
- **Entrega:** `~/Desktop/arreglos-de-ropa/anuncios/videos/7-11 - 1.mp4` a `7-11 - 3.mp4` (61,2 · 53,5 · 53,0 s), un archivo por pieza.
- **Tres clips se cayeron en la revisión del render**, no en la del pool: marca de agua al medio-derecha (el zoom solo recorta bordes), el creador hombre de cuerpo entero en una oferta de avatar mujer, y un primer plano de escote sobre piel por riesgo de rechazo en Meta. Dos reglas nuevas en [[guiones-y-anuncios]].
- Pendiente: decidir si se cortan los cuatro conjuntos en cero antes de llegar al corte sano de ~$28, y subirle presupuesto al CJTO 3.

## 2026-11-06 (38ª pasada) — DanceGo: radiografía del original y tanda 1 de 3 ads

- Pedido de Santiago: *"metete a la página de Go, la original, fijate el estilo de video que están haciendo y hagamos variables… tres renovaciones siguiendo los patrones ganadores del original"*.
- **Radiografía:** página DanceGo en la Biblioteca de Anuncios, **31 ads activos**, los 4 más viejos corriendo desde el **7 de enero de 2026** (diez meses). Se bajaron los 16 videos que daba la página, **9 únicos**, y se transcribieron con faster-whisper. Resultado: **un solo guion** repetido palabra por palabra en los cuatro creativos viejos, y **4 formatos en paralelo** (UGC + b-roll de 80 s, clip crudo con dos bandas de 37 s, voz en off rápida de 48 s y split PIP de 60 s). La frase que está en **todos** sus ads: *"la primera semana lo vas a sentir, la segunda lo vas a ver, la tercera lo van a ver los demás"*. Detalle en [[dancego]].
- **Tanda 1 entregada:** 3 ads de voz en off de 45 a 47 s, con la DNA del ganador pero **sin una frase repetida entre ellos** (regla del 22/10): el gimnasio en la tele del living, diez minutos mientras se hace la cena, y en tu casa nadie te ve aprender.
- **Edición clonada** de ellos con nuestra paleta: banda de hook de dos líneas desde el cuadro cero, placas de beneficio ancladas a la palabra, insertos de la app y de la comunidad, y placa final con el CTA y la flecha. Scripts nuevos: `gfx_dancego.py`, `gen_dancego_plans.py`, `edit_dancego.py`.
- **Voz Sulafat** por API; `gemini-2.5-flash-preview-tts` dio 429 y salió con el de reemplazo `gemini-3.1-flash-tts-preview`. Acento rioplatense verificado y los 3 videos transcriptos contra el guion.
- **B-roll:** 47 clips de `#bailoterapia` y `#zumbaencasa`, **28 sobrevivieron**. Se cayeron un clip con marca de agua en el medio del cuadro, dos recortes que quedaban en la cadera y todos los de `#bailarencasa` (baile social random en seis idiomas). Tres reglas nuevas en [[guiones-y-anuncios]].
- Entrega en `~/Desktop/dancego/anuncios/` como `6-11 - 1` a `6-11 - 3` · `OUTPUTS/2026-11-06-guiones-dancego.md`.
- Pendiente: la descripción para ads, el precio final y decidir si sumamos el formato B del original (clip crudo + dos bandas, sin voz).

## 2026-11-07
- **A Tu Medida — las visuales de la tanda 1, con fuente.** Se reconstruyó desde los `V*.json` el pool real de la tanda del 5/11: **los 6 ads usan los mismos 21 clips de TikTok** (cambia el seed del orden de cortes, el color del subtítulo y la voz). Se resolvió la cuenta y el link de cada ID por tikwm y se verificaron los 21 links (200). Reparto: 13 de arreglos sobre prenda real, 6 de bridal y 2 de ruedos, más los 2 insertos de `gfx_arreglos.py`.
- Nuevo: `OUTPUTS/2026-11-07-visuales-tiktok-a-tu-medida.md` (+ copia en `~/Desktop/arreglos-de-ropa/anuncios/visuales-tiktok.md`), armado para pasárselo al socio.
- Actualizado: `WIKI/arreglos-de-ropa.md` (sección «Los 21 clips del pool») y `WIKI/index.md`.
- **DanceGo — las visuales de la tanda 1, con fuente.** Mismo trabajo sobre los `V*.json` del 6/11: **los 3 ads comparten un pool de 26 clips** de `#bailoterapia` y `#zumbaencasa`, con cuenta y link resueltos por tikwm y verificados. Reparto corregido respecto de lo anotado antes: **19 de clase grupal + 7 del plano firma** (mujer sola en el living), no 28 clips con 6 de firma. En la carpeta hay 29 bajados; 3 quedaron afuera del corte.
- Nuevo: `OUTPUTS/2026-11-07-visuales-tiktok-dancego.md` (+ copia en `~/Desktop/dancego/anuncios/visuales-tiktok.md`).
- Actualizado: `WIKI/dancego.md` (el reparto real del pool y las cuentas que más aportaron).
- **DanceGo — 4 testeos sobre el ganador `6-11 - 1`** (*"Hay un gimnasio adentro de la tele de tu living"*, que hoy está rindiendo fuerte). Dos variables cercanas (hook nuevo + cuerpo validado) y dos videos nuevos con cuerpo propio sobre el mismo ángulo. Entregados como `7-11 - 1` a `7-11 - 4` (36 a 43 s) en `~/Desktop/dancego/anuncios/`.
- Se cazaron 67 clips de `#zumbaencasa` por Chrome y **sobrevivieron 8** (el tag está lleno de texto quemado y memes de gatos); van en los videos 3 y 4, que son los que necesitaban el plano firma del living.
- Nuevo: `OUTPUTS/2026-11-07-guiones-dancego-tanda-7-11.md`, `OUTPUTS/scripts-vsl/gen_dancego_plans_7.py`.
- Reglas nuevas en `WIKI/dancego.md`: el zoom tiene que recortar más alto que el cartel (1.30 no alcanzó, 1.52 sí) y el contador de claves del pool no puede salir de `enumerate` sobre un archivo con comentarios.

## 2026-11-06 (37ª pasada) — A Tu Medida: descripción para ads

- Descripción única para los 6 videos de [[arreglos-de-ropa]], al estilo de Stitched Fits (un solo copy para toda la flota).
- Entregada primero en 330 palabras y rehecha en **152** a pedido de Santiago: *"más corta, más optimizada"*. Quedó como regla en [[guiones-y-anuncios]]: la descripción para ads es corta por defecto; las 900-1.200 palabras son el storytime UGC de una native, no el primary text de un video.
- `OUTPUTS/2026-11-06-descripcion-ads-a-tu-medida.md` y `~/Desktop/arreglos-de-ropa/anuncios/descripcion-ads.txt`.

## 2026-11-06 (36ª pasada) — Cámaras frigoríficas: los 6 ads de voz en off

- Santiago eligió **los 6 con voz en off**, no con avatar. Se produjo la tanda entera de [[camaras-frigorificas]]: 6 videos de **32,8 a 37,6 s**, en el rango del ganador.
- **Voces:** Orus por API con Style de técnico estadounidense, las 6 verificadas con Whisper contra el guion. V6 dio 429 y salió al reintentar con el mismo modelo, sin pasar al de reemplazo.
- **B-roll:** 39 clips bajados con tikwm de los tags del producto y del oficio; **13 sobrevivieron** a la revisión. Se cayeron el explicador CGI de TXV (subtitulado entero), el cold room con el precio quemado, `#atlascool` (marca de agua) y un root cellar subtitulado. `#hvacrlife` no sirvió: puro meme y cara a cámara.
- **Scripts nuevos:** `OUTPUTS/scripts-vsl/gfx_walkin.py` (tapa, lámina del ciclo de refrigeración y tarjeta de oferta, dibujadas con la landing real en la mano y sin precio) y `OUTPUTS/scripts-vsl/gen_walkin_plans.py`. El montaje reusa `edit_arreglos.py` con `lang='en'`.
- **Un color de caja de subtítulo por creativo** (amarillo, verde, celeste, naranja, magenta, rojo), sin caja de hook ni placa final, cierre siempre sobre la tarjeta de oferta.
- ⚠️ Se coló un cartel azul de 0,5 s al arranque de un clip de fábrica que la hoja de contactos de 1,5 s no mostró. Se corrigió la ventana y se re-renderizó la tanda completa.
- Entrega en `~/Desktop/walk-in-coolers-freezers/anuncios/` como `6-11 - 1` a `6-11 - 6`, un archivo por pieza.
- Pendiente: la descripción para ads y definir países y presupuesto.

## 2026-11-06 (35ª pasada) — Cámaras frigoríficas: el manual visual al mercado inglés

- Pedido de Santiago: anuncios para `visual-handbook-of-walk-in-coolers-freezers.impultienda.ar` modelando al competidor español `camaras-frigarificas.impultienda.ar`, **sin bajar todo** y usando **los 7 pasos del segundo cerebro**.
- **Radiografía del ganador:** página Carlos Medina, **72 ads activos**, el más viejo en circulación desde el **5/10/2026** (32 días). Sube tandas de 6 a 13 creativos cada 4 o 5 días y **un solo primary text para los 72**. Testea **dos formatos en paralelo**: de los 8 creativos del 5/10, **4 son b-roll puro** con subtítulo palabra por palabra (y un estilo de resalte distinto por creativo), **3 son avatar de IA** a fondo fijo sin subtítulos ni cortes, y **1 es híbrido** (avatar recortado sobre b-roll). El avatar nunca lleva subtítulos; el b-roll siempre.
- Se bajaron y transcribieron con faster-whisper **los 8 creativos más viejos** (los del 5/10, todos vivos), no los 72. De ahí salieron las 8 familias de guion y los dolores del avatar.
- **Tanda 1 entregada:** 6 guiones EN + ES voseo con la estructura de 7 pasos, uno por ganador distinto y con cuerpo propio cada uno — demanda escondida, el trabajo mejor pagado, el error que mata compresores, la puerta, no cambies piezas sin diagnosticar y el llamado de emergencia. Banco: el recorrido del índice y la obra real documentada.
- Nuevo: `WIKI/camaras-frigorificas.md` · `OUTPUTS/2026-11-06-guiones-camaras-frigorificas-ingles.md` · `~/Desktop/walk-in-coolers-freezers/` con `imagenes/`, `landing/` y `anuncios/`.
- Pendiente: elegir el reparto de formatos de la tanda (propuesta: 4 con voz en off + b-roll de TikTok y 2 con avatar de HeyGen Avatar IV, que es lo que hace el ganador) y definir países y presupuesto.

## 2026-11-06 (34ª pasada) — Tu Primer Autómata de Madera: la tanda inglesa clonada a Argentina

- Pedido de Santiago: **"quiero que me hagas, exactamente los mismos ads, pero para argentina, todo igual"**. Se clonó entera la tanda del 5/11 de [[orzzen-automatas]] al mercado argentino, sin tocar la estructura: mismos 6 guiones (la versión ES que ya estaba escrita), mismo pool de TikToks, mismos seeds, mismos primeros planos y mismo color de subtítulo por creativo.
- **Voces:** Orus por API con Style rioplatense (voseo), el guion 2 a dos voces con Sulafat. Las 6 salieron con `gemini-2.5-flash-preview-tts`. Acento verificado con Gemini sobre V1 y V2: español argentino, voseo auténtico, sin leer instrucciones de estilo. De paso: `gemini-2.5-flash` ya no está disponible para la clave, el verificador ahora usa `gemini-3.8-flash`.
- **Scripts nuevos:** `OUTPUTS/scripts-vsl/gfx_automata_ar.py` (los 5 inserts con todos los textos en español) y `OUTPUTS/scripts-vsl/gen_automata_plans_ar.py` (`lang='es'`, anchors en la palabra española, botón `QUIERO EMPEZAR`, chips traducidos).
- **Entrega:** `~/Desktop/wooden-automaton/anuncios/videos-ar/6-11 - 1..6.mp4` (24,6 a 33,7 s), más `OUTPUTS/2026-11-06-guiones-automatas-argentina.md` y `OUTPUTS/2026-11-06-descripcion-ads-automatas-argentina.md` (un solo copy para los 6, el mismo de la tanda inglesa en español).
- **Avisado:** Orzzen corre en Argentina, así que esta tanda compite de frente contra el dueño de la oferta, con sus guiones y su prueba social. Queda anotado en la wiki junto a los dos defectos que se replicaron a propósito (el anchor de la app que choca en el guion 3 y el cartel de precios en libras del clip del cerdo volador).
- **Wiki:** `orzzen-automatas` con la sección "Tanda 2 — Argentina (6/11)" y las fuentes nuevas; `index` con los dos outputs.

## 2026-11-06 (33ª pasada) — el surfeo es duplicar cada 2 horas, y las CBO no son estructuras de escalado

- Corrección de Santiago, con captura del documento 3 a la vista: **"esto está mal, las cbo de Santi no son de escalado. La única cbo son las pocket. El surfeo es duplicar presupuestos cada 2 horas, nada más."**
- **Afuera la tabla de surfeo por tramos de CBO** (+30% cada 3-4 h debajo de 500 USD/día, +30% una vez por día arriba, una sola subida con ROAS bajo 2), el "nunca más de 30% por vez" con la progresión 10 → 12,5 → 16 → 20 → 26, y la **tabla de ayer y hoy** (+30% / quieta / −30% de tirón de oreja / surfeo agresivo).
- **Adentro, una sola regla:** *el surfeo es duplicar el presupuesto cada 2 horas; mientras el CPA aguante, se vuelve a duplicar*. Y se aclara sobre qué se surfea: **Cost Cap, Bid Cap y Pocket**. La campaña de testeo no se surfea.
- Las reglas que acompañan se mantienen: no surfear con 1 venta (3 a 5 ventas con ROAS 2,5+), si el CPA sube se baja el bid y no el presupuesto, duplicar hasta que suba el CPM, quieta si dejó de vender, reseteo nocturno.
- De paso, en el Claude Doc 3 quedaba una atribución suelta ("el manual da otra referencia para arrancar") → ahora dice "hay otra referencia para arrancar".
- Actualizados: `OUTPUTS/2026-11-05-meta-ads-3-escalado.md`, el Claude Doc (rev 27, mismo link) y **un Google Doc nuevo** ([Meta Ads 3](https://docs.google.com/document/d/1_Lgwoz4qtx15WjEiY4LSjdCOs4aMYuynS3sI2vVOQVA/edit)); el anterior, a la papelera.
- **Wiki (`escalado-en-meta-ads`):** la sección "Escala vertical" reescrita con la corrección fechada y los ritmos de +25-30% / +15% archivados; el bullet del surfeo cada ~2 horas ahora dice duplicar, a secas. Marcadas con ⚠️ las dos piezas que quedaron desalineadas: la skill **`manejo-cbo`** (trae el surfeo viejo de +30%) y el bot **`surfing-scale`** (está armado con ±30%).

## 2026-11-06 (32ª pasada) — Meta Ads 3: la Bid Cap es ABO, y los bids del mercado inglés

- Corrección de Santiago sobre el documento de escalado: **"la bidcap es abo. Los bid de la bidcap, en inglés son de 17 para arriba, 7 cjtos, o sea hasta 24. En Argentina está bien como está. Si fuera cbo no se le puede meter los bid, la única cbo es la pocket, que se le pone 35usd a la campaña."**
- **La Bid Cap pasa de CBO a ABO.** Decía "CBO con límite de puja y entrega acelerada"; ahora dice **campaña ABO**. La razón, que queda escrita como regla en el documento: **a una CBO no se le pueden poner bids**, así que Cost Cap y Bid Cap van las dos en ABO.
- **Los bids de la Bid Cap, por mercado:** **7 conjuntos** con los bids escalonados · **Argentina y LatAm: front × 1,3** (queda como estaba) · **mercado inglés: desde 17 USD y de uno en uno hasta 24**, uno por conjunto.
- **La Pocket es la única CBO del escalado** y su presupuesto son **35 USD a la campaña** (antes figuraba el 75% del front, también en el cuadro de operación de la Pocket).
- Ajustes de coherencia que arrastraba el cambio: la intrapuja de Bid Cap ya no "arranca en el precio del front y baja de uno en uno", va **sobre el escalón que ganó entre los 7 conjuntos**; la tarea pide el bid de Bid Cap con los dos mercados y armarla **como ABO de 7 conjuntos**; el criterio de aprobación ahora incluye **cuál de las tres estructuras es CBO y por qué**.
- Actualizados: `OUTPUTS/2026-11-05-meta-ads-3-escalado.md`, el Claude Doc (rev 25, mismo link) y **un Google Doc nuevo** ([Meta Ads 3](https://docs.google.com/document/d/1_Lgwoz4qtx15WjEiY4LSjdCOs4aMYuynS3sI2vVOQVA/edit)); el anterior se mandó a la papelera de Drive y su link se reemplazó en toda la wiki.
- **Wiki:** `escalado-en-meta-ads` (la BidCap reescrita como ABO + bloque de corrección fechado, la aclaración de que la puja manual solo existe en ABO, y los 35 USD de la Pocket en los dos lugares donde figuraba el 75%), `estructuras-cbo` (la Pocket en la tabla de estructuras + nota de corrección), `metodo-v3` y `skills-launch-expert` (el bid de Bid Cap con los dos mercados y la aclaración de ABO).

## 2026-11-06 (31ª pasada) — Meta Ads 2: las métricas se explican como cuatro preguntas

- Corrección de Santiago sobre el arranque del documento 2: **"hacés mucho énfasis en el costo por visita, cuando en realidad lo único que importa es: ¿está llegando gente a la landing? ¿están llegando al checkout? ¿están comprando? ¿cuánto generamos y cuánto gastamos? Nadie mira el costo por visita."**
- **Se rehizo la primera parte del documento.** Afuera: el blockquote de "todo el negocio son dos números", la fórmula en bloque de código de costo/revenue por visita, el ejemplo de 100 USD y 200 visitas y la sección "Qué se mira, y en qué orden" que arrancaba con el costo por visita (0,30 contra 1 USD). Adentro: **"Las cuatro preguntas"** con un cuadro de 4 filas (la pregunta · dónde se ve · está sano si · si está mal, el problema es) y **"Las primeras horas, con las cuatro preguntas en la mano"** (no entra gente → es el anuncio; no llegan al checkout → la landing o la oferta; no compran → precio, medios de pago, rechazos; compran → costo por compra contra lo que entra neto).
- **Reescritos los tres puentes que quedaban colgando del marco viejo:** las métricas de anuncio ahora "responden la pregunta 1", las de conversión "la 2 y la 3", y el CPC pasó de *"la métrica por excelencia"* a **"el precio de la pregunta 1: lo que te cuesta traer a cada persona a la landing"**.
- Los números y los KPIs no se tocaron: el documento sigue en ~1.400 palabras y conserva las referencias (CTR 1,5–2%, visita → checkout 10%, checkout → compra 25–30%, AOV ÷ front 1,5).
- Actualizados: `OUTPUTS/2026-11-05-meta-ads-2-oferta-validada.md`, el Claude Doc (rev 16, mismo link) y **un Google Doc nuevo** ([Meta Ads 2](https://docs.google.com/document/d/1sdeRe8hRzSNtJnUDmZ1MkoLG3G-PIK295OD5SiFwhZo/edit)); el anterior se mandó a la papelera de Drive y su link se reemplazó en toda la wiki, incluida la entrada de la 28ª pasada.
- Regla nueva en `WIKI/mentoria.md`: **un KPI se explica diciendo qué pregunta del embudo contesta y qué se arregla si está mal; un ratio sin pregunta atrás no entra al documento.**

## 2026-11-06 (30ª pasada) — la vara baja a 50 ads: dos ofertas del mercado inglés pasan el filtro

- Santiago, después del no-send de la pasada anterior: **"Te voy a bajar un poco la vara, mínimo 50 ads"**. El piso queda en **50 ads activos** y reemplaza al 70 que había fijado horas antes. El resto del filtro no se mueve: solo infoproducto low ticket, nada de marcas personales, nada de físico, mínimo 5 ofertas o se avisa.
- **Pasan con 50:** **Emily Makes → cutifystudio.com** (130 ads, **$39**, biblioteca de 150.000 SVG con licencia comercial, advertorial largo con el ingreso de Etsy como consecuencia) y **Tina Ghazi Digital** (142 ads, **$17**, Canva Crash Course con Master Resell Rights, corriendo desde julio 2026; la fanpage va con nombre propio, eso queda avisado).
- **Adyacentes** (low ticket digital pero nicho hobby, sin promesa de ingreso): The Crochet Nook 215 ads, Master Crafts DIY 208 ads.
- **Se cayeron por el otro lado del filtro, aun con arsenal grande:** Alina Bond 1.250 ads (es Zeely.ai, app con suscripción), 30 Second Clients 262 (Max Tornow: marca personal → high ticket), Norman Calloway 143 (advertoriales de abogado de DUI), Al Crayfish 83 (embudo a grupo de WhatsApp sin producto), Highland Growth 61 (página con ofertas mezcladas).
- **Medidos y abajo de 50:** Entrepedia 36, PLR Printables Store 30, PodFriendly 19, UGC Creator Accelerator 15, Prime Finds With Jill 40, Winclip 13, Bhs2020 12, Razvan Paraschiv 11, Work Beyond 9 to 5 11, AI Accelerator System 10, DigitalOriginal 10, Woodworthy 7, Nancy Badillo 6, Bob's Woodworking 6, Career Opportunity Network 6, Wood Atlas Plans 5, Woodplanshop 5, American Talent Network 4, AI Tool Report 4, Planning Made Personal 4, Kaizen Marketing Agency 3, Wonderheets 3, Intentionally Elevated 3, Craft By Melanie Smith 2, Hiring Team USA 2, Arlette S.Digital 2, Lunabloomcreative 1, Bloom Digital Products 1, Clickstoincome 1, Stars Crafts Designs 1.
- **El molde que hay que modelar** (anotado en la WIKI): advertorial largo en primera persona → bundle digital de $17-$39 con licencia comercial, vendido a hobbistas con la máquina parada, no a gente buscando "ganar plata online". Villano abstracto nombrable ("alquilar archivos" vs "tener la biblioteca"), gasto hundido del equipo, matemática explícita, y el ingreso como consecuencia.
- **Hallazgo de búsqueda:** las frases de promesa y de precio (`keep 100% of the profit`, `read this if you own a`, `extra $500 a month`) devuelven entre 5.000 y 5.400.000 resultados de apps de novelas y gyms. Solo sirven las frases de **producto** angostas, y después buscar los hermanos por el patrón del bundle.

Páginas actualizadas: [[caza-de-ofertas]]

## 2026-11-06 (29ª pasada) — caza del mercado inglés en ingresos extra: ninguna pasó el filtro

- Santiago pidió una investigación de mercado con la skill `cazar`: **mercado inglés, nicho "generar ingresos extra", solo infoproductos low ticket, mínimo 70 ads activos, nada de marcas personales, nada de productos físicos, mínimo 5 ofertas o que no le mande nada**. Y que lo guarde en memoria para no tener que repetirlo.
- **Resultado: no se manda nada.** ~20 búsquedas angostas por los ejes del nicho (PLR/resell rights, faceless digital marketing, printables de Etsy, Amazon influencer, freight dispatcher, flipping, AI side hustle, encuestas pagas, blueprints de ingreso) y ninguna oferta cumplió los 4 filtros a la vez. Arsenales reales: Prime Finds With Jill 40, Bizzoso 18, Sarah Clarke 13, Sofia Mercado 9, Copy Paste Paid 7, Faceless After Fifty 7, Appisi 4. Los únicos dos de 70+ se caen por otro lado: **Credit Secrets** (77) es reparación de crédito y **SSAcademy** (170) es embudo de high ticket con masterclass gratis.
- **Reglas nuevas, obligatorias de acá en adelante:** piso de **70 ads** (reemplaza el 40/50 del manual), **mínimo 5 o no se manda nada**, solo infoproducto low ticket y cero marcas personales — los cuatro se aplican **antes** de escribir la shortlist.
- **Dos hallazgos técnicos de la herramienta:** `page_ids` con `limit: 1` ya devuelve el `estimated_total_count` = arsenal exacto, por ~300 tokens en vez de ~10.000 (la forma correcta de screenear en lote). Y `ads_library_search` solo rankea por relevancia las primeras ~5-10 filas: con keywords amplias se cae a orden por fecha y devuelve ruido de apps de novelas y dramas cortos, así que van frases angostas y literales de 3-4 palabras con `limit: 10-12` y `countries` siempre puesto.
- Páginas actualizadas: [[caza-de-ofertas]] (filtro madre con el piso de 70 + registro del 06/11 con los dos hallazgos técnicos y la lectura del mercado).

## 2026-11-05 (28ª pasada) — Meta Ads 1 más corto y los documentos sin atribución

- Santiago, sobre el primer documento: *"te quedó un poco largo. Acortémoslo un poco, tampoco tanto"* y *"no podemos decir como dice Bilbao. Claramente es una mentoría mía… Pongámoslo, pero no aclares eso"*. Después: *"Y hacelo en doc de google drive"*.
- **Meta Ads 1 acortado** de ~1.800 a ~1.100 palabras sin perder un número: fuera los subtítulos intermedios, los cuadros que repetían un bullet, la media página de pre-testeo y los recordatorios duplicados en la lista de errores (de 7 a 5).
- **Atribución fuera de los tres documentos.** Se reescribieron todas las menciones (3 en el primero, 6 en el segundo, 7 en el tercero): *"Bilbao usa 7, 8 o 10"* → *"dentro de ese rango es criterio propio"*; *"Bilbao exige >50 %"* y *"él exige >10 %"* → *"acá el piso es…"*; *"Bilbao la arranca en 500"* → *"lo normal es arrancar en 500"*; *"el ejemplo del material"* → *"un caso real"*; *"a un alumno se le dispararon 150 USD"* → *"sin regla se pueden disparar 150 USD"*. Las citas textuales quedan, sin decir quién las dijo. Tampoco se escribe en primera persona sobre Santiago.
- **Tres Google Docs nuevos** en su Drive (el conector solo crea, no edita, así que cada corrección va a dar un link nuevo): [Meta Ads 1](https://docs.google.com/document/d/1N943ljltNzis4Kpkg930njF4t-imDHm1TQsoIiljTwk/edit) · [Meta Ads 2](https://docs.google.com/document/d/1sdeRe8hRzSNtJnUDmZ1MkoLG3G-PIK295OD5SiFwhZo/edit) · [Meta Ads 3](https://docs.google.com/document/d/1_Lgwoz4qtx15WjEiY4LSjdCOs4aMYuynS3sI2vVOQVA/edit). En las tablas van sin `**` y sin `~` (el importador los rompe), y los tres Claude Docs mantienen su link de siempre.
- Páginas actualizadas: [[mentoria]] (sección ⭐ nueva con las dos reglas y los links de Drive en la tabla de los tres videos).

## 2026-11-05 (27ª pasada) — El módulo de Meta Ads, en tres documentos

- Santiago: *"ahora quiero que me armes un documento para la clase de Meta Ads… vamos a dividir el módulo de Meta Ads en varios videos"*. Quedaron **3 videos y 3 documentos**: (1) introducción + campañas de testeo, (2) cómo leer las métricas para saber si la oferta está validada, (3) campañas de escalado. El de métricas va **en el medio** a propósito: no se escala nada antes de saber leer.
- **Meta Ads 1** (https://claude.ai/artifact/TZ8mp6qzBtL4b19HLu214R): ABO = presupuesto en el conjunto, CBO = en la campaña y se lee **siempre a nivel campaña**; la notación 1-1-1 / 1-1-5 / 1-3-1 / 1-8-1; el ajuste de **"compartir hasta un 20 %"** que convierte una ABO en CBO; la **ABO 1-1-1 con 5 a 10 USD por conjunto** (tabla por ticket) y el setup completo; la **CBO de testeo post-Andrómeda** (3 conceptos, contenido flexible, 35 USD y 4 campañas/día); el **CPA medio = ticket ÷ 2** con los tres modos y la regla de corte; y la cuenta con **solo dos campañas fijas**.
- **Meta Ads 2** (https://claude.ai/artifact/TRb1YibGiWkMCCWg7pVo8A): costo por visita contra revenue por visita, el **CPA break-even**, los **100 USD y una semana** contra el **mínimo de 20 anuncios**, oferta validada contra creativo validado (5 conversiones), los KPIs con los números de Bilbao (hook >50 %, retention >10 %, comprate 2,5 %), y el **orden de diagnóstico de 6 pasos** con los datos reales (los ganadores llevan ~15 de cada 100 al pago, los perdedores ~10).
- **Meta Ads 3** (https://claude.ai/artifact/MokxS6UHE3HtrbbVaehM3G): el surfeo **+30 %** con el ritmo atado al presupuesto y la tabla ayer/hoy, el techo de la cuenta, puja manual contra automática y la **regla de reparto** (todo en manual no se puede), **Cost Cap** de 7 conjuntos con bids escalonados y 4 revisiones por día, **Bid Cap** acelerada (front × 1,3), la **intrapuja** y su atajo, y las **dos Pocket** (1-8-1 al 75 % del front y Launch Pocket 1-10-N a 3-5×).
- Estaba todo en el cerebro: no hizo falta pedirle ninguna estructura. **Pocket incluida** ([[estructuras-cbo]], [[escalado-en-meta-ads]]).
- Actualizadas: [[mentoria]] (tabla de módulos y la decisión de partir Meta Ads en 3), [[index]].

## 2026-11-05 (25ª pasada) — A Tu Medida: cama musical activa

- Santiago: *"Estan muy bien, pero no pongas mas esa musica, necesito una musica mas activa, cambiale solo eso"*.
- Se midieron las 7 camas que hay en el disco: la que veníamos usando es un **pad sin pulso** (4,5 % de graves, pulso 0,25). Se cambió por la de **`music.py`** (118 BPM con bombo, la validada en [[scented-stones]] y [[atlas-cortes]]): 78 % de graves y pulso 0,76.
- **Los 6 re-renderizados** con `usage.json` borrado y los mismos seeds. Verificado: `usage.json` final **idéntico** al anterior y un cuadro del segundo 20 de cada video **pixel por pixel igual**. En el mix la tanda pasó de 2 % a 17 % de graves sin subir el volumen general (rms 0,095 → 0,098).
- Páginas actualizadas: [[arreglos-de-ropa]] · [[guiones-y-anuncios]] (2 reglas nuevas).

## 2026-11-05 (24ª pasada) — A Tu Medida: los 6 ads clonados de Stitched Fits

- Santiago: *"Dale, haceme los videos"*. Y en el medio pasó la landing real: *"aca te dejo mi landing por si necesitas info, o si no coincide la info ajustalo"*.
- La oferta se llama **A Tu Medida** (marca *Arreglala Vos Misma*), $19.999 de $32.499, 9 clases base + 25 videos, 3 bonos bizop. Se rehicieron **los 6 guiones, los 2 insertos y las 6 voces** con los datos y el vocabulario de la landing (modista, marcar con alfileres, líneas de costura, el calce).
- **6 ads producidos**, de 52 a 66 s, en `~/Desktop/arreglos-de-ropa/anuncios/videos/` (`5-11 - 1.mp4` a `5-11 - 6.mp4`).
- Voz **Sulafat** por API; el modelo 2.5 dio 429 y salió con `gemini-3.1-flash-tts-preview`. Acento rioplatense con voseo verificado contra el audio.
- **Edición clonada de Stitched Fits**, no solo el guion: subtítulos **en itálica** con la palabra activa adentro de una **caja de color** (un color por creativo), sin caja de hook, sin placa final, y cierre sobre un inserto de la **página de ventas** dibujado por código.
- **Pool de 21 clips** de TikTok. `#clothingalterations` rindió **13 limpios de 57** (tag tomado por thrift-flippers con subtítulo quemado en inglés); `#bridalalterations` y `#hemming` salvaron la tanda.
- Scripts nuevos: `edit_arreglos.py`, `gen_arreglos_plans.py`, `gfx_arreglos.py`, `dl_tikwm.py`.
- Páginas actualizadas: [[arreglos-de-ropa]] · [[guiones-y-anuncios]] (3 reglas nuevas) · [[index]].

## 2026-11-05 (26ª pasada) — El módulo impositivo, corto

- Santiago, sobre la primera versión: *"me lo hiciste re largo y re complicado. **No quiero que sea como si estuviera hablando un contador**… es simplemente para que aquella persona que está desde cero sepa que si vende tiene que facturar, de que todos los meses tiene que pagar ingresos brutos, de que está exento de IVA porque vende libros y de que si es responsable inscripto no tiene límite de facturación"*.
- Reescrito: de **17 secciones y ~3.500 palabras a 4 secciones y ~500**, con dos cuadros chicos. Cierre fijo: **contador apenas empezás a vender**, porque si no aparecen **bloqueos en plataformas de pago, billeteras y bancos**. El Claude Doc mantiene el link; el Google Doc es nuevo (https://docs.google.com/document/d/1trq1-VkZVP157-O3IjPFYCMNz7TDg1I45fzBwUEda2s/edit) porque el conector de Drive crea archivos pero no los edita.
- **Incorporadas sus ediciones a mano del doc largo**, que son reglas de estilo: hablar siempre de nuestro caso y no del universo de casos (fuera "salvo exento" y "según el comprador"); manda la **frecuencia** (IIBB 1 vez por mes, Ganancias y lo de afuera 1 vez al año); Ganancias dicho como **30–35% de la facturación**; **números en pesos de hoy** aunque sean aproximados (autónomos ~$80.000); **Whop/Stripe en la misma bolsa**, sin presentar la LLC como etapa; y borrar la fila de un impuesto que no pagamos.
- La versión larga queda como **respaldo** en `OUTPUTS/2026-11-05-modulo-7-impuestos-argentina-y-exterior.md`; la guía de clase, en `OUTPUTS/2026-11-05-modulo-7-guia-de-clase.md`. El detalle verificado sigue viviendo en [[impuestos-en-argentina]] y [[llc-banca-y-fiscal]], no en el documento de clase.
- Actualizadas: [[mentoria]] (regla nueva: el documento ordena, no enseña la materia), [[index]].

## 2026-11-05 (25ª pasada) — Módulo impositivo de la mentoría (Argentina + exterior)

- Santiago: *"un documento que sea sobre todo el módulo impositivo en el negocio de los infoproductos… dividido en dos partes. Primero, ¿qué pasa cuando vendemos en Argentina? Y después la parte de todo lo que es vender afuera con Whop, con LLC"*, con el pedido explícito de **verificar los datos** (topes de monotributo, etc.) en vez de darlos de memoria.
- Entregado en **formato guía** (el de [[mentoria]]): 17 secciones, dos partes, 11 cuadros. **Claude Doc** https://claude.ai/artifact/2y1AdsWcAioGyRfuakKkeB + **Google Doc en su Drive** https://docs.google.com/document/d/1VTJ43kFjoFyq4CHUcawiI1L_XG9Uhle1UmUY0A2NEgY/edit + copia en `OUTPUTS/2026-11-05-modulo-7-impuestos-argentina-y-exterior.md`.
- **Datos verificados con fuente:** tabla de monotributo vigente desde **agosto de 2026** (tope de K: **$126.610.830**, cuota $1.614.446); **Monotributo Unificado CABA** desde enero de 2026 ($22.485 en A, $237.015 en K); IIBB CABA **3 % / 5 %**; **RG 5554/2024** derogó las retenciones de IVA y Ganancias de la RG 4622 (quedan SIRTAC y SIRCUPA, que sí aplican al monotributista).
- **Tres cosas que corregimos de lo que traía:** (1) el IVA no se cae por ser digital — el **libro** está exento (art. 7 inc. a + **Dictamen 70/2010**, vale incluso descargándolo de la web), pero **curso, membresía o software pagan 21 %**; (2) en EE.UU. no pagar income tax **no es** no presentar: **Form 5472 + 1120 pro forma con multa de 25.000 USD** por año aunque la LLC no facture nada; (3) el **sales tax de productos digitales sí existe** por estado (economic nexus, ~100.000 USD o 200 transacciones) y el VAT de UK/UE se debe desde la primera venta — de ahí el modo "Whop cobra y declara" al 2 %.
- Sumado también: los **tres modos de impuestos de Whop** y sus cláusulas duras (1 % de disputas, reservas de hasta el 100 %), la exención de **BOI** de FinCEN del 26/3/2025, y el lado argentino de la **renta mundial** y el origen de fondos.
- Páginas nuevas: [[impuestos-en-argentina]]. Actualizadas: [[llc-banca-y-fiscal]], [[mentoria]], [[index]].

## 2026-11-05 (24ª pasada) — Descripción para los ads de Your First Wooden Automaton

- Santiago: *"Dame una descripcion para los ads de la oferta de madera que hicimos recien"*.
- Un **solo copy para los 6 videos** de la tanda del 5/11, en **inglés y español con voseo** (la oferta corre en el mercado inglés), siguiendo el molde de oferta directa de [[group-work-playbook]] y [[herrero-de-finde]].
- Contenido alineado a la landing de Orzzen: el golpe de "es madera y no tiene motor", el mecanismo pieza por pieza, la **app simuladora**, la biblioteca de **+20 mecanismos**, las 18 lecciones, los proyectos con nombre, **+1.400 compradores y 4.9★**, garantía de 30 días, acceso de por vida, **sin precio**, y CTA a *Más información* con la promesa de 5 a 7 días.
- Guardada en `OUTPUTS/2026-11-05-descripcion-ads-wooden-automaton.md`, copiada a `~/Desktop/wooden-automaton/anuncios/descripcion-ads.md` y al portapapeles.
- Actualizadas: [[orzzen-automatas]], [[index]].

## 2026-11-05 (23ª pasada) — Stitched Fits: la ballena de arreglos de ropa para Argentina

- Santiago: *"Quiero que analices esta oferta… la voy a tirar en argentina, la idea es clonar sus mejores anuncios, clonando guiones y edicion, las visuales vamos a tener que usar de tiktok, pero quiero que utilices las mismas o muy similares"*.
- Radiografía de **Stitched Fits / Alter It Yourself** (UK): ~340 ads activos, el más viejo del **3 de mayo de 2026** (6 meses), 19 creativos de mayo todavía gastando. £99 → £59, 5.000+ alumnos, embudo simple sin quiz ni VSL.
- **12 videos top bajados y transcriptos** con faster-whisper → **8 familias de guion**; dos cuerpos repetidos (coser≠arreglar y "pagás dos veces") marcan los ganadores.
- **Edición relevada con hojas de contactos:** 100 % b-roll, sin caja de hook, subtítulos karaoke de 3 a 6 palabras con **un color de resalte por creativo**, cama musical continua, cortes de 2 a 3 s y el inserto de producto como **grabación de pantalla de la página de ventas**, no mockup.
- **Competencia en AR: cero.** "curso arreglos de ropa" da 0 activos en la Ads Library argentina.
- Entregada la **tanda 1: 6 guiones en voseo**, uno por familia ganadora, todos bajo 1:30. E y G quedan de banco.
- Páginas nuevas: [[arreglos-de-ropa]]. Actualizadas: [[index]].

## 2026-11-05 (22ª pasada) — La edición de los 6 ads, clonada de Orzzen

- Santiago: *"¿Copiaste tal cual los guiones como te dije? ¿Y la edición?"*. Los guiones sí eran literales; **la edición no**: estaba con nuestro formato de siempre. Eligió *"pegate a la edición de ellos"* y dejar el CTA que le agregué al guion 4.
- Se armó la hoja de contactos de 5 ads de Orzzen y se copió el montaje: **sin caja de hook, sin placa final**, cierre con **la tapa del ebook + botón ámbar**, subtítulos de **3 palabras** y **un color por creativo**.
- **5 inserts de producto dibujados por código** (`gfx_automata.py`): tapa, hoja de planos con cut list y medidas en mm, biblioteca de 20+ mecanismos, las 6 fases y la pantalla de la app simuladora. Van anclados a la palabra que los nombra.
- Editor: overlay `button` y parámetro `last` (último plano fijo, para que el cierre no quede tapado).
- Los 6 re-renderizados y revisados en `~/Desktop/wooden-automaton/anuncios/videos/` (`5-11 - 1.mp4` a `5-11 - 6.mp4`), un archivo por pieza.
- Páginas actualizadas: [[orzzen-automatas]] · [[guiones-y-anuncios]] (3 reglas nuevas).

## 2026-11-05 (21ª pasada) — En la carpeta de entrega va un archivo por pieza

- Santiago: *"Porque tengo muchos videos, dejame solo los que van"*. Había dejado los renders crudos (`V1.mp4`…`V6.mp4`) junto a las copias numeradas (`5-11 - 1.mp4`…): doce archivos para seis videos.
- Se borraron los duplicados y los `_tmp` del editor. La carpeta pasó de **949 MB a 219 MB** y quedan los 6 videos y el `.md` de los guiones.
- Regla nueva en [[como-trabajar-con-santiago]]: el render se **mueve**, no se copia; en lo que él abre va un solo archivo por pieza, con el nombre de tanda.

## 2026-11-05 (20ª pasada) — Los 6 videos de Your First Wooden Automaton

- Santiago: *"Dale, haceme los videos, son 6 videos los que necesito"*.
- **6 ads de voz en off producidos**, de 25 a 38 s, en `~/Desktop/wooden-automaton/anuncios/videos/` (`5-11 - 1.mp4` a `5-11 - 6.mp4`).
- Voz **Orus** por API; el guion 2 va a **dos voces** (Orus + Sulafat) con el nuevo `tts_gemini_multi.py`. Dos de las seis salieron con `gemini-3.1-flash-tts-preview` por 429 del modelo 2.5.
- Pool de **19 clips de TikTok** del tag `#woodenautomata`, todos de makers reales. Tres pasadas de render: la primera desbordaba la placa final, la segunda coló un *"link in bio"* y el subtítulo de las gallinas, la tercera un texto en español.
- Scripts nuevos: `gen_automata_plans.py`, `edit_automata.py`, `tts_gemini_multi.py`.
- Páginas actualizadas: [[orzzen-automatas]] · [[guiones-y-anuncios]] (3 reglas nuevas).

## 2026-11-05 (18ª pasada) — Habilidades Perdidas: 6 ads del competidor doblados a español neutro

- Santiago: *"hagamos 6 anuncios agarrando los 6 mejores ads… únicamente blurrees sus subtítulos y metas el idioma en español neutro de LATAM… las visuales no quiero que cambies nada… no blurrees uno que está hablando un avatar porque no va a tener sincronización los labios"*.
- **Se descubrió que la cuenta tiene solo 8 creativos distintos**: los 22 ads mejor rankeados son 8 archivos resubidos (el control, 5 subidas × 8 copias = 40 instancias). De esos 8, **tres tienen presentador hablando** y quedaron afuera por el labial; se tomaron los 6 que son 100 % voz en off.
- **Cadena nueva, `OUTPUTS/scripts-vsl/render_hp.py`** (sobre la lógica de `render_idioma.py` del pase ruso): detección de la banda de subtítulos por perfil de texto con borde, máscara por componentes conexas, inpaint TELEA en dos pasadas, **blur gaussiano difuminado encima** y subtítulos karaoke nuevos en la misma posición. Los carteles (`Big offer incoming!`, `They Don't You To Know About This…`, `76% OFF DISCOUNT`, `+3 FREE GIFTS`, los stickers de comentario) se taparon con caja opaca que cubre el rectángulo original entero.
- **Tres correcciones durante el control:** el inpaint solo deja fantasma en cajas sólidas grandes (hay que taparlas, no borrarlas); los subtítulos del competidor **a veces son de dos líneas** y la banda hay que medirla por máximo histórico, no por promedio; y el rectángulo de un sticker medido por umbral se queda corto (en A4 dejaba afuera la foto de perfil).
- Voz **Orus**, `gemini-2.5-flash-preview-tts`, calzada al largo exacto de cada video. Cama musical del original separada con demucs. Verificado con Whisper: los 6 dan `es 1.00`, sin resto de la voz inglesa.
- Entregado en `OUTPUTS/2026-11-05-guiones-habilidades-perdidas-es.md`, los MP4 en `~/Desktop/habilidades-perdidas/anuncios/` y al portapapeles.
- Páginas actualizadas: [[habilidades-perdidas]] · [[index]].

## 2026-11-05 (19ª pasada) — Orzzen: autómatas de madera al mercado inglés

- Santiago: *"la vamos a tirar la misma oferta, pero en el mercado inglés… 6 testeos… los guiones quiero que sean exactamente los mismos, pero en inglés"*. Y en el medio: *"No descargues todo"* → se cortó la descarga en **14 de los 32** ads.
- Radiografía de `orzzen.impultienda.ar`: 32 ads activos, el más viejo del **13 oct. 2026** (23 días), un solo producto (AR$ 19.976 con 60% off, garantía 30 días, +1.400 compradores).
- **7 familias de guion** transcriptas con faster-whisper. La madre, *"Podés construir esto aunque…"*, corre con 6 variantes que solo cambian la objeción del hook.
- Entregada la **tanda 1: 6 guiones EN + ES**, traducción exacta de las 6 familias que están gastando. El estacional de Navidad y las 4 variantes de hook quedaron de banco.
- Archivos: `OUTPUTS/2026-11-05-guiones-orzzen-automatas-ingles.md`, copia en `~/Desktop/wooden-automaton/anuncios/` y al portapapeles.
- Páginas actualizadas: [[orzzen-automatas]] (nueva) · [[index]].

## 2026-11-05 (18ª pasada) — The Lost Skills of Independence: radiografía y plan para LATAM

- Santiago: *"tengo esta oferta que quiero que analices de arriba abajo. No quiero que descargues absolutamente todos sus anuncios… los que hace más tiempo están corriendo, los que tienen patrones en común… después me des ideas de los tipos de videos… La oferta la vamos a tirar en LATAM"*.
- **Muestra, no descarga masiva:** 206 tarjetas leídas de las 722 activas (264 creativos únicos, 874 instancias) y **15 videos vistos cuadro a cuadro** con hojas de contacto armadas en el navegador. El más viejo activo es del **19 jun. 2026**.
- **Un solo copy** (735 de 874 instancias: *"Why don't they make books like this anymore?"*) y **un solo creativo ganador**: *"How to Pull Water from Thin Air"*, 43 s, **resubido 8 veces con 12 copias cada vez**. No testean copy, testean creativo.
- **Hallazgo grande:** la versión en español **ya existe y es digital**. Flota de `Marina cardozo` (156 ads, ES+IT) y `Adriana Garven` (207 ads, FR) → `habilidades-es.impultienda.ar`, de **Emmanuel Bilbao**, con checkout geo-adaptado: **US$ 109,90 → US$ 21,90** desde Argentina. España, Italia y Francia están tomadas; LATAM no.
- Entregado en `OUTPUTS/2026-11-05-analisis-lost-skills-of-independence.md`, en `~/Desktop/habilidades-perdidas/` (con el video de referencia del 20/6) y al portapapeles.
- Páginas actualizadas: [[habilidades-perdidas]] (nueva) · [[index]].

## 2026-11-05 (17ª pasada) — Corrección: las keywords de renda extra van en genérico

- Santiago: *"no quiero que en las de renda extra me pongas específicamente qué tipos de trabajo… quiero palabras generales de renda extra, o sea, no algo súper específico"*.
- Se reemplazó la sección de renda extra del banco por **8 keywords generales validadas**, y las de oficio (`chaveiro`, `piscineiro`, `conserto de celular`…) quedaron anotadas aparte, fuera del pedido.
- **La mejor: `mesmo começando do zero`** — destapó *"Curso Completo de Tranças por Apenas R$ 27!"* y *"Curso de chinelos por R$ 10"*, con precio en el título y sin cara. La ventaja de la general sobre la específica: **no hay que saber el oficio para encontrar la oferta**.
- Las otras 7: `curso por apenas`, `aprender uma profissão` (Humdiarista, "ENTRE NO GRUPO VIP" x7), `não é pirâmide`, `só copiar e colar`, `nas horas vagas`, `fazer um bico`, `grana extra`.
- **Quemadas, con su número:** `caiu no pix` 186.399 · `depois do expediente` 537.439 · `comece a vender` 372.147 · `aprenda do zero` 296.097 · `complementar a renda` 164.942 · `grupo VIP` 64.128.
- La regla quedó en [[caza-de-ofertas]]: las cuatro formas de decir dinero sin nombrar el oficio (objeción, precio/formato, oficio en genérico, mecánica).
- Páginas actualizadas: [[caza-de-ofertas]].

## 2026-11-05 (17ª pasada) — Caza en Brasil: keywords ocultas de emagrecimento y renda extra

- Santiago: *"Quiero que hagamos una buena investigación de mercado en el mercado de Brasil… Dame 10 palabras claves del nicho de bajar de peso, pero no las típicas… Quiero encontrar ofertas ocultas, ofertas que no ve nadie"*, y después *"Dame palabras clave tmb, asi busco, distintas a las que estas utilizando vos"* y *"Labura en mi compu"*.
- **20 keywords validadas una por una** en la Biblioteca (conector oficial de Meta, BR, solo activos), ninguna repetida de los bancos del 12/10, 26/10 y 29/10. Se listan también **las 11 que no sirven**, con el número que devolvieron.
- **Hallazgos:** una ballena de **132 anuncios activos** en drenaje (page_id `702881226395611`, todos con el título `⭐⭐⭐⭐⭐ (5/5)`), la **flota de cuidador de idosos** (Beatriz Rocha con 38 ads + 3 fronts con nombres de mujer genéricos) y *Atlas de Auriculoterapia* con **100 mapas por R$19,90**. Ninguna se recomienda todavía: falta abrir landing y checkout (paso 7 del Manual).
- **Dos reglas técnicas nuevas** en [[caza-de-ofertas]]: las frases de 4+ palabras devuelven 0 o ruido (pescan las de 2–3), y las terapias manuales en BR están tomadas por clínicas locales — el infoproducto se separa por formato en el título (atlas, mapas, catálogo digital), moneda USD y fanpage sin ciudad. Se afinó además la señal de front faceless: nombre de persona *genérico* y repetido entre páginas no es marca personal, es flota.
- Entregado en `OUTPUTS/2026-11-05-caza-brasil-keywords-ocultas.md`, en `~/Desktop/caza-brasil-05-11/` (`caza-completa.txt` + `TUS-20-KEYWORDS.txt` con el set que Santiago busca en paralelo) y al portapapeles.
- Páginas actualizadas: [[caza-de-ofertas]] · [[index]].

## 2026-11-05 (17ª pasada) — Descripción para los ads de Tai Chi Fit

- Santiago: *"Bien, dame una descripcion para los ads"* (después de corregir el checkout del quiz).
- **Una sola descripción** para toda la tanda, con el molde de la casa para quiz funnel en Argentina (el de [[monjaro-violeta]] y Mounjaro Humilde): mecanismo en la primera línea, 4 bullets de beneficio, bloque de lo que incluye con la garantía, y CTA al test gratis de 1 minuto.
- **La promesa es la del Tai Chi, no la de las dietas:** energía, equilibrio y flexibilidad, "tu raíz" como mecanismo y el cuerpo que vive en alerta como villano — igual que el VSL. Sin kilos con plazo, sin precio ("baratísimo") y sin claim médico.
- Lo que incluye se leyó de la caja de oferta del quiz y del guion del VSL: plan día por día, movimientos filmados con su versión adaptada, las tres fases (Raíz, Fluir, Grulla), Aprendiz → Maestra, soporte prioritario y la garantía de 30 días. **No se menciona WhatsApp**: esta oferta no lo tiene.
- Entregada en `OUTPUTS/2026-11-05-descripcion-ads-tai-chi-fit.md`, en `~/Desktop/tai-chi-fit/anuncios/descripcion-ads.txt` y al portapapeles.
- Páginas actualizadas: [[index]].

## 2026-11-05 (17ª pasada) — El checkout de Tai Chi Fit, corregido en todos los CTAs

- Santiago: *"Actualizame el txt del quiz de taichi, quiero que todos los botones del cta de la ultima slide redirijan a este checkout: https://taichi-fit.impultienda.ar/checkout"*.
- El quiz tenía `tai-chi-fit.impultienda.ar` (con guion), que era justamente el link que daba **"Tienda no encontrada"**. El real es **`taichi-fit.impultienda.ar/checkout`** y responde **200**.
- Como la URL vive en un solo lugar (`CONFIG.LINK_CHECKOUT`), fue una línea: cambiada en `~/Desktop/tai-chi-fit/landing/tai-chi-fit-quiz.txt`, en `tai-chi-fit-quiz.html`, en `tai-chi-fit-PRUEBA.html` y en la copia `OUTPUTS/2026-11-04-quiz-tai-chi-fit.html`. Nada más del quiz se tocó.
- **Verificado en el navegador** con `?utm_source=test&utm_campaign=cta`: los **6 botones `data-cta`** (el de abajo del VSL, los tres del recorrido, el de la caja de oferta y el de la barra fija) apuntan a `taichi-fit.impultienda.ar/checkout` y arrastran los UTMs. En la última slide no quedó ningún `<a>` ni `<button>` sin link.
- El `.txt` quedó copiado al portapapeles, listo para pegar en ImpulTienda.
- Páginas actualizadas: [[tai-chi-fit]] (checkout confirmado, se fue la pregunta abierta), [[quizzes-reglas-de-armado]] (regla: el subdominio de ImpulTienda no se deduce del nombre, se confirma o se verifica con 200).

## 2026-11-04 (16ª pasada) — Descripción para los ads de Monjaro Rojo

- Santiago: *"Dame una descripcion para los ads de monjaro"*.
- **Una sola descripción** para toda la tanda, con el molde de la casa para quiz funnel de peso en Argentina (el de Mounjaro Humilde y Protocolo Chía 28D): mecanismo en la primera línea, 4 bullets de beneficio, bloque de lo que incluye con la garantía, y CTA al test gratis de 1 minuto.
- **Sin precio y sin promesa de kilos con plazo**, y el hook en tercera persona ("muchas argentinas están tomando") en vez de afirmar una condición del que mira. La landing ya carga con los tres motivos de rechazo que marca [[protocolo-chia-28d]]; el ad no suma ninguno.
- Lo que incluye se leyó de la caja de oferta del quiz y del VSL, sin inventar nada.
- Entregada en `OUTPUTS/2026-11-04-descripcion-ads-monjaro-rojo.md`, en `~/Desktop/monjaro-violeta/anuncios/` y al portapapeles.
- Páginas actualizadas: [[monjaro-violeta]], [[index]].

## 2026-11-04 (16ª pasada) — Los CTA de DanceGo, blindados al checkout

- Santiago: *"Ajustame algo del quiz, todos los botones de cta de la ultima slide, tienen que redirigir a este checkout: https://dancego.impultienda.ar/checkout"*.
- El link **ya era ese** (`CONFIG.LINK_CHECKOUT`, línea 16) y los 4 CTAs del último paso ya salían de ahí. Lo que se hizo fue sacarle los puntos flojos:
  - **Selector más ancho** en `ligarCTAs()`: entra también cualquier `button.btn` que se agregue más adelante, además de los `a.btn` y los `.js-cta`.
  - **`ligarCTAs()` también en el arranque**: los `href` quedan puestos desde que carga la página, no recién cuando se monta la oferta.
  - **Idempotente** (`dataset.cta`): antes, si se llamaba dos veces (arranque + oferta, o la oferta destapada por `SEGUNDOS_OFERTA`), se sumaban dos listeners y el pixel disparaba **dos `AddToCart` por clic**.
  - `rel="noopener"` en los `<a>` del checkout.
- **Verificado en Chrome** sobre el último paso: los 4 CTAs (3 botones + la chapita **HOY: GRATIS**) van al checkout, ninguno quedó con `href="#"`, y con `?utm_source=fb&utm_campaign=x1` en la URL el link final arrastra los dos parámetros.
- Entregable regenerado: `~/Desktop/dancego/dancego-quiz.txt` (713 KB, 16 imágenes embebidas), más `dancego-PRUEBA.html` y `OUTPUTS/2026-11-04-quiz-dancego.html`. Copiado al portapapeles.
- WIKI: regla nueva del 2026-11-04 en [[quizzes-reglas-de-armado]] (los CTA del último paso: uno solo los engancha a todos) + fila en el registro de correcciones; en [[dancego]] el checkout pasa de provisorio a **confirmado**.

## 2026-11-04 (15ª pasada) — El checkout de Monjaro Rojo, confirmado

- Santiago: *"Ajustame el txt, todos los botones de cta que aparecen al final, tienen que redirigir a este checkout: https://monjaro-rojo-japones.impultienda.ar/checkout"*.
- **`LINK_CHECKOUT` cambiado** a `https://monjaro-rojo-japones.impultienda.ar/checkout` en los tres archivos del quiz (`.html`, `.txt` y `-PRUEBA.html`), que se mantienen idénticos.
- Los **4 botones de CTA** (el de abajo del VSL, el de la caja de oferta, el del cierre y el del footer) no tienen el link escrito a mano: todos llevan `data-cta` y el script les pone `checkoutURL()`, que sale de `LINK_CHECKOUT` y le pega las UTMs de la URL. Una sola línea arrastra los cuatro.
- Queda cerrado el pendiente del dominio. Lo único que sigue abierto del cambio de nombre es el **VSL, que todavía dice "Monjaro Violeta" 5 veces en la voz de las avatares**.
- Páginas actualizadas: [[monjaro-violeta]].

## 2026-11-04 (13ª pasada) — El producto pasa a llamarse Monjaro Rojo

- Santiago: *"Cambiame el monjaro violeta, por el rojo"*.
- **Quiz cambiado**: 22 apariciones por archivo, en los tres. Verificado en Chrome: cero "violeta" en pantalla, título y caja de oferta con el nombre nuevo.
- **La palabra "ROJO" se repintó de violeta a rojo** en el lockup de portada y en la barra de progreso. Escrita en violeta se leía como un error. El resto del magenta del quiz quedó igual.
- ⛔ **No se tocó el dominio del checkout** (`monjaro-violeta.impultienda.ar`): si la tienda sigue con ese nombre, cambiarlo rompe el pago. Falta que Santiago confirme.
- ⛔ **El VSL sigue diciendo "Monjaro Violeta" 5 veces, en la voz de las avatares.** No se arregla editando: pide regenerar voces + 3 renders de HeyGen (~39 créditos) + montaje + Panda.
- Páginas actualizadas: [[monjaro-violeta]].

## 2026-11-04 (14ª pasada) — DanceGo: de 35 pasos a 26, y sin el paso de los ritmos

- Santiago: *"Lo de los estilos de musica sacalo te dije. El emoji de las baterias se ve muy mal. Saca algunas preguntas que esten de mas."*
- ⚠️ **Corrección mía:** en la pasada anterior había pedido *"las del tipo de musica sacalas"* y le saqué **solo las imágenes**, dejando el paso con una tarjeta tipográfica. Quería el **paso entero**. Regla nueva en la WIKI: cuando pide sacar algo de un quiz, por defecto es el paso completo; si es solo la imagen, lo aclara.
- 🆕 **Un emoji repetido no es un ícono.** Las 🔋 / 🔋🔋 / 🔋🔋🔋 del nivel de energía se veían amateur dentro de la chapita de 34 px. Regla: un emoji por opción, nunca una fila para representar una escala; si hace falta un nivel, va un medidor en CSS.
- **9 pasos afuera, de 35 a 26:** estilos de música, el bloque de hábitos entero (agua, sueño, rutina de trabajo, qué tan activa, energía), "nivel en el baile" (duplicaba "¿probaste baile antes?"), la edad exacta (ya se pregunta en la portada) y "tu mejor cuerpo" (no personalizaba nada). Con energía se fue el emoji de pilas.
- Al sacar el paso se barrió todo el código huérfano: el array `RITMOS`, la rama del `render`, la función `swipe()`, su CSS y el campo en `state`.
- 🐛 **Un proceso ajeno estaba escuchando en el puerto 8777** (una página "relay" del propio Santiago): el servidor de prueba no levantaba y Chrome mostraba esa página en vez del quiz. Se pasó al 8911. Conviene chequear con `lsof -nP -iTCP:<puerto> -sTCP:LISTEN` antes de dar por bueno un 200.
- 📁 Regenerado: `~/Desktop/dancego/dancego-quiz.txt` (713 KB, copiado al portapapeles), `dancego-PRUEBA.html`, `landing/dancego-quiz.html`. Copia en `OUTPUTS/2026-11-04-quiz-dancego.html`.
- Recorrido entero verificado en un `<iframe>` de 390 px: 26 pasos, cero desborde, cero imágenes rotas.
- Páginas actualizadas: [[dancego]], [[quizzes-reglas-de-armado]].

## 2026-11-04 (12ª pasada) — El VSL enchufado al quiz y el CTA a los 2:30

- Santiago pasó el embed de Panda: *"quiero que lo metas al final del quiz, y que al minuto 2:30 aparezca el boton de cta"*.
- **Embed pegado** en `<template id="vsl-template">` de los tres archivos del quiz. Player `player-vz-c3e8527f-c25.tv.pandavideo.com`, video `0f41879a…`.
- **Se pega el `<div>` envolvente además del `<iframe>`**: ese div trae el `padding-top:177.77%` que sostiene el 9:16. Verificado en el navegador: 522×928, ratio 0,563.
- **`SEGUNDOS_OFERTA` = 150.** Es cuando la Abuela Mei dice "tocá el botón de acá abajo". Aviso dado: el precio se dice antes, en el 1:33, así que la oferta sale 57 s después del precio.
- **Probado de verdad en Chrome:** a los 149 s oculta, a los 151 s aparecen la caja de oferta y el botón. Los 3 CTA resuelven a `/checkout` con las UTMs. Consola limpia.
- ⚠️ **Anotado un falso negativo propio:** probar el disparo con `?oferta=1` no sirve, porque ese atajo ya llamó a `showOffer()` y la función tiene un guard `offerShown`. Hay que probar con una copia sin ese `showOffer()`.
- Páginas actualizadas: [[monjaro-violeta]], [[quizzes-reglas-de-armado]].

## 2026-11-04 (13ª pasada) — DanceGo: la portada no necesitaba fotos nuevas, necesitaba un recorte

- Santiago: *"Las imagenes del principio son muy malas, usa algunas que ya hayamos usado y que se vean mejor, hacelo mas llamativo, las del tipo de musica sacalas."*
- ⭐ **Las 4 fotos de edad eran buenas; el encuadre era malo.** Retratos de estudio de 1024×1024 en los que la persona ocupaba un tercio de la tarjeta y el resto era gris vacío: a 170 px las cuatro parecían **la misma mujer**. Con un recorte apretado a la cara (zoom 1.95, centro vertical 0.26, salida 720×960 en 3:4) se ven las arrugas, el pelo cano y la edad de cada una. **Cero imágenes nuevas, cero créditos.**
- **Portada más llamativa sin volver a lo colorido:** chapita oscura *+155 mil mujeres bailando* con punto verde, titular a 2.05rem y las fotos **a sangre** con la edad encima, sobre una banda oscura, en vez de una franja blanca debajo. En un teléfono de 390 px entra todo en la primera pantalla (677 px de 798).
- **Los 7 ritmos quedaron sin imagen**, como pidió: tarjeta tipográfica sola (eyebrow + nombre en la serif + descripción).
- 🔎 **Se buscó un set de edades mejor en las otras ofertas y no existe:** las de [[monjaro-violeta]] son parejas (hombre + mujer) recortadas sobre negro a 300 px. Queda anotado que conviene mirar antes de prometer un reuso.
- 📁 Regenerado: `~/Desktop/dancego/dancego-quiz.txt` (719 KB, copiado al portapapeles), `dancego-PRUEBA.html`, `landing/dancego-quiz.html`, `imagenes/edad-1..4.webp`. Copia en `OUTPUTS/2026-11-04-quiz-dancego.html`.
- Recorrido entero verificado en un `<iframe>` de 390 px: cero desborde, cero imágenes rotas.
- Páginas actualizadas: [[dancego]], [[quizzes-reglas-de-armado]].

## 2026-11-04 (12ª pasada) — DanceGo: el quiz brasileño clonado, en voseo y despintado

- Santiago: *"Quiero que me hagas este quiz, en español argentino… Mejoramelo, no quiero que se vea recontra colorido, quiero que las imagenes se vean bien."* (`funilv1.appdancego.com`)
- ⭐ **El hallazgo: las fotos del original estaban bien, lo feo era el overlay.** Las 4 fotos de edad y las 8 de tipo de cuerpo son tomas de estudio, fondo gris, ropa deportiva neutra y mismo encuadre — se veían espantosas porque tenían encima un **degradé rosa/violeta/verde/naranja**. Reusadas sin el overlay, el set entero queda premium **sin generar una sola imagen con IA**.
- **Paleta nueva:** papel crema `#FBF8F4` + tinta `#1C1A19` + **un** acento frambuesa `#B23A5B`. El verde `#216B4F` solo significa "bien"/comprar y el rojo solo "riesgo". Se fueron los títulos de cuatro colores palabra por palabra y el amarillo chillón de los botones.
- **Lo que se rehízo en HTML en vez de copiar capturas:** el perfil de Instagram de las 155 mil seguidoras, el chat de la comunidad de WhatsApp, la maqueta del celular con la app (el original tenía la UI en portugués) y las **7 tapas de los ritmos**, que eran carteles neón de IA con el texto quemado.
- **Localización:** sertanejo universitario y funk brasileño no se escuchan acá → **cumbia y cuarteto**; gospel → **salsa y bachata**. Se sacó el paso del e-mail (va en el checkout).
- 🆕 **Dos bugs de maquetado que no se ven en el escritorio**, anotados en la WIKI: el atributo `height=""` del `<img>` **le gana al `aspect-ratio`** (el antes/después salía de 853 px de alto) y las grillas de dos columnas se desbordan 4 px a 373 px. Se chequea recorriendo el quiz entero por código dentro de un `<iframe>` de 390 px.
- 🆕 **Lovable con Supabase propio:** si el bundle tiene `from("funnel_steps")` y panel de administración, el quiz **no** viaja en texto plano; se recorre en Chrome. Las imágenes sí están todas listadas (81 archivos en `/lovable-uploads/`) y conviene mirarlas juntas en una hoja de contactos.
- 📁 **Entregado** en `~/Desktop/dancego/`: `dancego-quiz.txt` (718 KB, 16 imágenes embebidas, copiado al portapapeles), `dancego-PRUEBA.html`, `landing/dancego-quiz.html` e `imagenes/` (16 webp). Copia en `OUTPUTS/2026-11-04-quiz-dancego.html`.
- ⏳ **Falta** el precio final, el link real de checkout y definir si lleva VSL. Los valores del `CONFIG` son provisorios ($14.990 / $49.990 / 3 cuotas).
- Páginas nuevas o actualizadas: [[dancego]], [[quizzes-reglas-de-armado]], [[index]].

## 2026-11-04 (11ª pasada) — La música audible de verdad, y la carpeta del VSL limpia

- Santiago: *"Subime un poco mas la musica, SOLO ESO… quiero que quede solo el vsl terminado, todo lo demas sacalo"*.
- ⭐ **La música estaba a 27 dB bajo la voz, o sea inaudible.** `volume=0.075` parecía razonable pero nunca se había medido. Pasó a **`0.19` = 18,6 dB bajo la voz**, que es donde una cama musical se escucha sin tapar. La regla ahora es calcular el volumen, no tantearlo.
- **Dos errores de medición propios, anotados para no repetirlos:** medir el RMS global de la mezcla no sirve (la voz lo domina y el número no se mueve), y medir "en un silencio" tampoco, porque este VSL **no tiene ni un hueco** de 0,45 s. Se mide la cola final, donde queda la música sola.
- 🆕 **Cambiar solo el audio no pide re-renderizar el video:** se rehace la mezcla y se pega con `-c:v copy`. Segundos en vez de cuatro minutos.
- 📁 **`~/Desktop/monjaro-violeta/vsl/` quedó con un solo archivo**: `VSL-monjaro-violeta.mp4` (2:40, 1080×1920, 174 MB). Todo lo demás se movió a **`vsl-fuentes/`** en vez de borrarse: los bloques de HeyGen costaron 39 créditos y las voces, la cuota diaria del TTS.
- Páginas actualizadas: [[monjaro-violeta]], [[vsl-reglas-de-armado]].

## 2026-11-04 (11ª pasada) — Calendarios 2027: los 6 ads rehechos con b-roll que sí muestra calendarios

- ⭐ **Santiago rechazó la tanda entera:** *"usaste cualquier visual, no tienen nada q ver con lo que vendemos, son calendarios hechos a mano, no hay un puto calendario"*. Tenía razón: el pool estaba buscado por las **escenas del guion** (flores de papel, tijera, impresora, feria) y en ningún plano se veía un calendario.
- **Regla corregida en `WIKI/guiones-y-anuncios.md`:** la de la pasada anterior ("el tag se elige por la escena, no por el nombre del producto") estaba **mal** y quedó reescrita. El tag se arma con el **nombre del producto**; la escena solo completa un pool que ya lo muestra. Primer filtro de todo clip: *¿se ve lo que vendemos?*
- **Regla nueva:** si el producto lleva año impreso, un `2025`/`2026` legible mata el ad. Hay material **2027** en TikTok, hay que buscarlo.
- **Pool v3:** tags `deskcalendar`, `diycalendar`, `papercalendar`, `handmadecalendar`. De 166 candidatos bajaron 147 y quedaron **17 ventanas de 15 clips** (`anuncios/work/tiktoks3/`).
- **Los tres clips clave:** `7679474945889455380` (calendario de papel con forma de florero con ramo, en caballete, **2027** impreso — es el producto), `7585091358939942166` (tulipanes de papel parados sobre la base de un calendario) y `7466996351692295431` (calendarios chicos de escritorio con flores que se abren).
- **Tres rondas de render** hasta limpiar: se cayeron `7684630906363006229` (cartel arriba *y* "DO NOT RE-UPLOAD" abajo, ningún zoom los saca, más una página 2026) y `7593073970606345494`; se subió el zoom de la HP a 1.6 y se partieron las ventanas de `7675332899951906056` (el "7cm x 11cm" del medio) y `7589850087459736863` (el "calendar for my bf" del principio).
- **Entregado:** `~/Desktop/calendarios-2027-en/anuncios/CAL-V1..V6.mp4` (0:30 / 0:29 / 0:23 / 0:28 / 0:26 / 0:57).
- ⏳ **Sigue faltando** el nombre comercial, el precio y el checkout: la placa final usa el provisorio `2027 CALENDAR PACK`.

## 2026-11-04 (10ª pasada) — El VSL de Monjaro, editado: 2:40 con B-rolls, música y headlines

- Santiago: *"metele 1.23 de velocidad… una musica activa bajita… algunos brolls… subtitulos, efectos de sonido, algunos headlines… Ponele onda, no lo llenes de cosas"*.
- **Entregado:** `vsl/VSL-monjaro-violeta-EDITADO.mp4`, **2:40, 1080×1920, 166 MB**.
- ⭐ **Medido: a 1,23x la abuela pasa de 45-55 a 40-50 años, y compensar el tono lo empeora** (bajarlo 4% la deja en 35-45). Va con `atempo` limpio. Confirma la regla del atempo que rejuvenece.
- **Música activa propia** (`music_activa.py`): 96 BPM con shaker, kick, marimba y pad, sin melodía para no competir con la locución. Sidechain contra la voz, -24 dBFS en los silencios.
- **5 B-rolls de ~3 s**, todos del tercer clip. Los otros dos quedaron afuera: uno tiene "Beetroot ginger shots" quemado en inglés en el centro, el otro muestra a un hombre a cámara que rompe el relato de dos mujeres.
- ⭐ **Regla nueva: nunca B-roll sobre el precio ni sobre el CTA.** Quedó un hueco deliberado de 52 s alrededor del precio.
- ⭐ **Las anclas se escriben como habla el transcriptor, no como habla el guion:** las cinco fallaron porque el TTS dice los números en letras y el transcriptor los escribe en dígitos ("3 minutos", "8 kilos").
- **Falsa alarma resuelta:** Santiago avisó que no podía abrir el video; estaba a medio escribir por el re-render (el MP4 guarda el índice al final). Chequeados los 10 mp4 de la carpeta: ninguno roto, no se borró nada.
- Scripts nuevos: `edit_monjaro.py`, `music_activa.py`, `sfx_whoosh.py`.
- ⏳ Falta subir a Panda Video la versión EDITADA y pegar el embed.
- Páginas actualizadas: [[monjaro-violeta]], [[vsl-reglas-de-armado]].

## 2026-11-04 (9ª pasada) — El VSL de Monjaro Violeta, terminado: 3:17 con dos personajes

- **Entregado:** `~/Desktop/monjaro-violeta/vsl/VSL-monjaro-violeta.mp4`, **3:17, 1080×1920**. Abuela Mei 0:18 → Mariela 2:23 → Abuela Mei 0:36. **39 créditos** de HeyGen con Avatar IV (quedan ~3.185).
- **Avatares:** los generó Santiago con su ChatGPT desde los prompts entregados. Recortados a 9:16 exacto para que HeyGen no meta barras blancas.
- **Voces:** Abuela Mei con **Vindemiatrix a 160 ppm**, Mariela con **Gacrux a 170 ppm**. Santiago: *"una voz mayor de 40 años"* para la testimonial — Sulafat daba 35-45 y se cambió.
- ⭐ **Hallazgo que cambia una regla: el atempo rejuvenece la voz.** Sobre el mismo wav, 134 ppm suena a 60-70 años y 180 ppm a 40-50. Los 210 ppm de Tai Chi Fit le habrían sacado 20 años a la abuela. **En un personaje mayor el ppm se fija por la edad, no por el reloj.**
- ⭐ **El TTS bloqueaba el testimonio por `finishReason=SAFETY`** (cifras de descenso de peso). Con `safetySettings` en `BLOCK_NONE` salió al primer intento. Vale para toda oferta de salud o peso.
- **HeyGen: cambiar de avatar resetea el modelo** a Avatar 6 Pro. Pasó dos veces y se agarró antes de generar las dos.
- **`SEGUNDOS_OFERTA` = 114**, medido sobre el video terminado (el precio se dice en el 1:54). Ya está en los tres archivos del quiz.
- **Sin "mi flor"**: era `minha flor` traducido literal del brasileño.
- Scripts nuevos: `ritmo_monjaro.py`, `montar_monjaro.py`, `tts_gemini_safe.py`, `nano_banana.py`.
- ⏳ Falta subir el VSL a Panda Video y pegar el embed en `<template id="vsl-template">`.
- Páginas actualizadas: [[monjaro-violeta]], [[vsl-reglas-de-armado]], [[como-trabajar-con-santiago]].

## 2026-11-04 (9ª pasada) — "TODOS LOS BOTONES": lo que parece botón también va al checkout

- Santiago pegó la versión corregida (verificado en vivo: los 5 CTA resuelven a `/checkout`, y el clic real en *QUIERO EMPEZAR A DIBUJAR* termina en "Checkout - Dibujo Creativo"). Pero mandó una captura de la caja de regalos: *"Esos botones también tienen que redirigir, TODOS LOS BOTONES"*.
- **Lo que tocó no era un botón:** la chapa verde **"HOY: GRATIS"** es un `<i class="free">` decorativo. Parece botón (fondo verde, `border-radius:999px`) y no hacía nada. Lo mismo la caja de regalos entera.
- **Cambios:** el botón del hero `VER TODO LO QUE INCLUYE` deja de ser ancla a `#incluye` y pasa a `js-cta` → `/checkout` (eran 5 CTA, ahora son **6**); y una **red de seguridad 2** en el JS le pone `cursor:pointer` y un clic al checkout a `.regalos`, `.free` y cualquier `[data-checkout]` que no esté dentro de un `<a>`, sin duplicar el evento cuando un padre ya lo cubre.
- **Verificado contra la página publicada**, parcheando el DOM en vivo con el mismo código: los 6 botones resuelven a `/checkout` arrastrando las UTMs, y el clic en la chapita "hoy: gratis" termina en `/checkout?utm_source=…`.
- El `.txt` queda en **38.081 bytes**, los tres archivos sincronizados y copiado al portapapeles.
- ⚠️ Avisado, no tocado: los 4 links del pie (Términos, Privacidad, Reembolsos, Contacto) siguen en `href="#"`. No son botones de compra, así que no se mandan al checkout; hay que apuntarlos a las páginas de la tienda.
- Páginas actualizadas: [[quizzes-reglas-de-armado]].

## 2026-11-04 (8ª pasada) — La landing corregida sigue sin pegarse, y el alcance de un arreglo

- Se perdió el contexto de la terminal; se reconstruyó el estado desde el `changelog.md`, los `OUTPUTS/` y los archivos del Escritorio.
- **Verificado con `curl` sobre `dibujo-creativoo.impultienda.ar`: la tienda sigue sirviendo la versión vieja.** Los 5 CTA están en `href="#"`, el JS todavía hace `a.href = C.LINK_CHECKOUT` con `LINK_CHECKOUT: "https://dibujo-creativoo.impultienda.ar"` (la home, que es la landing) y hay un solo `{{price}}`. Es exactamente el "me manda al principio de la landing".
- **El archivo local está correcto y sincronizado** (mismo md5 en `landing.html`, `landing-impultienda.txt` y `PRUEBA.html`, 37.346 bytes): 5 CTA a `/checkout`, 18 tokens de precio, red de seguridad en el JS. Copiado al portapapeles para que lo pegue Santiago.
- **Hallazgo sobre las imágenes del CDN del original** (avisado, no tocado): el `mockup` lleva la marca del competidor (**UNIVERSO CREATIVO**) y la URL de `materiales` **hoy devuelve otra foto** (una selfie en una cocina), así que la página publicada la está mostrando. Las 7 quedaron bajadas y optimizadas en `~/Desktop/dibujo-creativo/imagenes/web/` (506 KB) por si se decide reemplazarlas.
- **Corrección de Santiago:** *"Si la página ya estaba terminada, no tenías que cambiar nada más que los botones de CTA redirijan al checkout"*. Regla nueva: un arreglo puntual toca solo eso; lo que se encuentre de paso se avisa en una línea y se espera, aunque figure como pendiente en el changelog.
- Páginas actualizadas: [[como-trabajar-con-santiago]] (sección nueva), [[quizzes-reglas-de-armado]] (registro de correcciones).

## 2026-11-04 (8ª pasada) — Calendarios 2027: la tanda 1 de 6 ads en inglés, montada

- Se retomó donde había quedado: guiones EN/ES listos, las 6 voces de Sulafat generadas y 17 clips de TikTok bajados.
- **Los 17 clips no servían.** El tag `printablecalendar` trae impresión 3D (calendarios perpetuos en PLA, relojes flip) y hasta chicos bailando. Se barrió de nuevo por **escena** y no por producto: `popupcard`, `paperflowers`, `craftfair` y `epsonecotank`. De ~95 candidatos bajaron 71 y **quedaron 23 limpios**.
- **Los 6 ads renderizados** en `~/Desktop/calendarios-2027-en/anuncios/`: CAL-V1 (0:30 feria), CAL-V2 (0:29 escuela), CAL-V3 (0:23 oferta), CAL-V4 (0:28 "61 años"), CAL-V5 (0:26 fin de semana) y CAL-V6 (0:57 Navidad).
- **Paleta nueva** en `edit_cal.py`: ámbar #EFA93C (hook, botón y palabra que suena), verde hoja #15694A (chips) y crema #FBF7F0 (placa final).
- **Tres reglas nuevas de b-roll** anotadas en [[guiones-y-anuncios]]: el tag se elige por la escena; tikwm rate-limitea y pisa archivos si se baja mientras se renderiza; y la hoja de contactos va a **1 cuadro cada 1,5 s**, porque a cada 3 s se cuelan los carteles de 2 segundos (pasó con el "20 cm x 20 cm" y el "14x14 cm sheet", que aparecieron recién en el primer render).
- ⚠️ **La placa final dice `2027 CALENDAR PACK` con un nombre provisorio**: faltan nombre comercial, precio y checkout. Faltan también los 50 diseños propios y la landing.
- Páginas nuevas/actualizadas: [[calendarios-2027]], [[guiones-y-anuncios]], [[index]].

## 2026-11-04 (8ª pasada) — Las imágenes no se pagan más: ChatGPT y Nano Banana, nunca Higgsfield

- Santiago, después de que las fotos de avatar del VSL de Monjaro salieran de Higgsfield: *"Podes usar mi chatgpt, nano banana, o alguna gratuita, no uses nada que cobre"*.
- **El gasto:** 4 de los 4,35 créditos que quedaban, en 4 fotos (GPT Image 2, calidad media, 1 crédito c/u). En alta son 3,5 y no entraban dos. **GPT Image 1.5 ya no existe** en Higgsfield: ahora son GPT Image 2 y 2.5.
- ⛔ **Hallazgo: la API de Gemini no genera imágenes gratis.** `gemini-2.5-flash-image`, `gemini-3.1-flash-image`, `-lite` y `-preview` devuelven los cuatro **429 con `limit: 0`** sobre `generate_content_free_tier_requests`. El tier gratis cubre texto y **TTS** (por eso la voz sí sale por API) pero **cero** imagen. Nano Banana solo sirve **desde el navegador**. El cliente quedó escrito igual en `OUTPUTS/scripts-vsl/nano_banana.py`.
- **Avatar de la Abuela Mei resuelto:** Santiago generó la foto con su ChatGPT desde el prompt entregado y quedó mejor que las de Higgsfield (más foto, menos render). Guardada como `~/Desktop/monjaro-violeta/vsl/avatar-abuela-mei.png` (942×1670, 9:16 exacto, no necesita reencuadre para HeyGen).
- **Mariela (la testimonial):** prompt entregado y dos opciones generadas en `~/Desktop/monjaro-violeta/vsl/opciones-avatar/`. Falta que elija.
- El guion quedó partido en `vsl/voz/bloque1-3.txt`: **50, 405 y 98 palabras**. El bloque 2 trae una enumeración (WhatsApp, grupo, menús, ejercicios), que es justo lo que el TTS se come: hay que verificarlo con `revisar_voz.py`.
- ⏳ **Pendiente de decisión: la voz de Mariela.** La regla fija es mujer → Sulafat, pero la Abuela Mei también es mujer y hablan una atrás de la otra en el mismo VSL.
- Páginas actualizadas: [[como-trabajar-con-santiago]].

## 2026-11-04 (7ª pasada) — El botón que "recargaba la landing": el link de la tienda no es el checkout

- Santiago: *"cuando hago clic en el botón de CTA me manda al principio de la landing"*.
- **Causa:** `https://dibujo-creativoo.impultienda.ar` **es la home de la tienda, y la home es la landing**. Al poner ese dominio en los botones, el clic recargaba la misma página. El checkout real es `<dominio>/checkout` (verificado: title "Checkout - Dibujo Creativo", con formulario de pago).
- **Segundo hallazgo, bajando el HTML con `curl`:** la tienda tenía publicada una versión anterior de la landing (los 5 CTA en `href="#"`, `LINK_CHECKOUT` con el dominio, cero tokens). El txt corregido no se había pegado todavía.
- Agregada una **red de seguridad** en el script: si un `.js-cta` carga con `href` vacío, `#` o un placeholder, se fuerza `/checkout`.
- Verificado en Chrome: los 5 CTA resuelven a la ruta `/checkout` del origen donde esté publicada la página.
- Páginas actualizadas: [[shopify-y-checkout]].

## 2026-11-04 (6ª pasada) — Monjaro Violeta: el acompañamiento vuelve al guion y la oferta del quiz no se toca

- Dos correcciones de Santiago sobre el VSL:
  1. *"Si tenemos todo eso que sacaste, no lo saques, lo tenemos"*. Yo había sacado el soporte por WhatsApp, el grupo, los menús, los ejercicios y la consultoría aplicando la regla de Tai Chi. **Vuelven todos al guion**, con el anclaje del original convertido: la consulta con la Abuela Mei "sale más de ciento veinte mil pesos". Regla nueva: **lo que tiene una oferta no se deduce de otra oferta, se pregunta**.
  2. *"Dejala así tal cual como está, no le cambies nada a lo que ofrece"*. Había alineado la caja de oferta del quiz con el VSL (sumando el acompañamiento y dos regalos más, $205.400). **Revertido entero**: la caja vuelve a sus 5 regalos y $73.500. La caja de oferta no se edita si no lo pide.
- El guion queda en **2:41 y 553 palabras** y **`SEGUNDOS_OFERTA` pasa a 101** (el precio se dice en el 1:37).
- **Prompt del avatar de Mariela** (la testimonial, 52 años, canas y anteojos) escrito: `OUTPUTS/2026-11-04-prompt-avatar-mariela.md`. Son dos avatares, uno por personaje.
- ⚠️ Queda por definir quién atiende la consultoría que promete la Abuela Mei, que es un avatar.

## 2026-11-04 (6ª pasada) — Academia del Trazo: la landing enchufada al checkout de Impultienda

- Santiago: *"me sigue sin dejar, todos los botones de cta tienen que redirigir al checkout"*, y pasó las instrucciones de Impultienda.
- El error era poner el dominio de la tienda (`https://dibujo-creativoo.impultienda.ar`) en `LINK_CHECKOUT`. Dentro de Impultienda el botón va **relativo**: `href="/checkout"`.
- **Los 5 CTA de `~/Desktop/dibujo-creativo/landing/` apuntan a `/checkout`** (hero de la oferta, "empezar hoy", oferta, cierre y la barra fija). El JS ya no reescribe el destino: solo le arrastra las UTMs y dispara el `AddToCart`.
- **Precios por token de Impultienda**: `{{price}}`, `{{original_price}}` y `{{savings}}` en los 18 lugares donde había precio. El JS quedó solo como respaldo para cuando la página se abre fuera de Impultienda.
- **Las cuotas ya no muestran importe** ("hasta 3 cuotas con Mercado Pago"): el monto dependía del precio en ARS y rompía la multidivisa.
- Verificado en Chrome sobre un server local: 5 botones a `/checkout`, UTMs pegadas, ningún nodo de precio vacío, consola limpia.
- Los tres archivos quedaron sincronizados: `landing-impultienda.txt` (el que se pega), `landing.html` y `PRUEBA.html`.
- Pendiente: las imágenes siguen apuntando al CDN del competidor y `PIXEL_ID` está vacío.
- Páginas actualizadas: [[shopify-y-checkout]].

## 2026-11-04 (5ª pasada) — Monjaro Violeta: el VSL del original, destripado y reescrito

- Santiago: *"entrá de nuevo al quiz original, fijate que en la última slide hay un VSL, descargalo y armemos uno nuestro exactamente igual"*.
- **Los dos videos bajados.** El player es de **ConverteAI/VTurb**: el `player.js` trae el id del video y el master vive en `cdn.converteai.net/<cuenta>/<video>/main.m3u8`, sin autenticación. VSL final: **2:29**. Video corto del paso 11: **1:39**.
- **El VSL dura 2:30 y tiene 431 palabras.** Lo hablan **dos personajes**: la Abuela Mei abre (11 s) y cierra (30 s), y el **70% del medio es el testimonio de otra mujer filmado en su cocina real, formato UGC**. Eso es lo que hay que replicar: no es un VSL de experta a cámara.
- **Guion nuestro escrito: 2:35, 530 palabras, tres bloques de HeyGen**, con los 10 beats del testimonio en el mismo orden.
- **Se sacó todo lo que no tenemos** (soporte por WhatsApp, grupo, menús, ejercicios, consultoría individual) y entraron los entregables reales del quiz y los 5 regalos. El anclaje pasa de "una consulta sale R$ 700" al valor de los regalos.
- **`SEGUNDOS_OFERTA` queda en 92**: el precio se dice en el 1:28.
- **Prompt del avatar de la Abuela Mei** listo, con las reglas del 3/11: sentada, plano medio, fondo liso y vacío, look de foto de celular y sin las palabras que empujan al render de stock.
- Páginas actualizadas: [[monjaro-violeta]], [[index]].

## 2026-11-04 (4ª pasada) — Monjaro Violeta Japonés: el quiz entero, clonado del brasileño

- Santiago pasó la Biblioteca de Anuncios de **Vovó Mei** (~37 ads activos): oferta brasileña de "Mounjaro Roxo Japonês", una bebida de remolacha con protocolo de 30 días. Destino real `monja-roxo.lovable.app`. Va para **Argentina**.
- **El funnel salió sin abrir el navegador:** Lovable deja el quiz en texto plano en `assets/routes-*.js`. Son **68 pasos = 34 reales**, duplicados en rama mujer/hombre desde la pregunta de género.
- **Entregado: quiz de 27 pasos** (30 si declara una condición de salud) en `~/Desktop/monjaro-violeta/`, con rama por género, IMC con barra y alerta por franja, 3 medidores, pantallas de carga, comparativa antes/objetivo y la oferta oculta hasta `SEGUNDOS_OFERTA`.
- **Sacados los 4 pasos de WhatsApp y e-mail** (regla fija: los datos de contacto se piden en el checkout).
- **Imágenes: 27 webp, 458 KB; el `.txt` embebido pesa 679 KB.** La portada se recortó y se le puso un alfa en diagonal para sacarle el cartel en portugués, y el lockup "MONJARO VIOLETA JAPONÉS" se rehízo en HTML. Las chapas `MULHER`/`HOMEM` se repintaron a `MUJER`/`HOMBRE` con Pillow. La infografía "COMO FUNCIONA" pasó a una placa de 3 pasos en HTML.
- **Las siluetas de tipo de cuerpo del original son de 96×80 px y no existen más grandes** (probados todos los sufijos de tamaño de InLead): esas dos preguntas quedaron con tarjetas de emoji y descripción.
- **Token `{{o}}`** para que los textos concuerden con el género ("¿estás lista?", "Quedate tranquila", "Lista, Ana").
- **Probado paso por paso en el navegador**, sin errores de consola, incluida la rama de condición de salud y la oferta completa con contador, cupos y notificaciones.
- ⏳ Falta el VSL (`SEGUNDOS_OFERTA` en 230 de prueba), el video corto de la Abuela Mei del paso 11 —si el `<template>` queda vacío el paso se saltea solo— y confirmar nombre, precio y checkout.
- ⚠️ **Aviso anti-bloqueo:** la portada promete "10 kg en 30 días", hay antes/después y el nombre de un fármaco deformado. Es lo que en [[protocolo-chia-28d]] hizo rechazar anuncios aunque el guion estuviera limpio.
- Páginas nuevas/actualizadas: [[monjaro-violeta]], [[quizzes-reglas-de-armado]] (§3 InLead dentro de Lovable, §4 portada y chapas, §4b concordancia de género), [[index]].

## 2026-11-04 (6ª pasada) — El ad brasileño de pilates, destripado frame por frame

- Santiago dejó un ad de Brasil (88 s, pilates 50+) y pidió analizarlo entero *"para que cuando yo pida un video con IA se entienda que quiero de esto… la onda de los videos de IA"*.
- **No hay ffmpeg en la Mac.** Se armó un cliente propio en Swift + AVFoundation (`scratchpad/bin/vid`) para metadata, detección de cortes, hojas de contactos, recortes ampliados y exportación de audio. Transcripción con Gemini 3.6 Flash (los 2.5/3.8 dan 404 o 503).
- **Hallazgo principal: el ad es 100 % IA y se puede probar.** Los 11 planos miden entre 6,3 y 8,2 s (clips de 8 s); los 8 planos de la presentadora arrancan en la misma pose porque **todos salen de la misma imagen de referencia**; y el "DIA 01 / DIA 49" es el mismo plano regenerado —en el día 49 aparece una manta en el sofá que antes no estaba—.
- **Guion medido:** 270 palabras, **185 ppm**, voz el **99 %** del tiempo, un solo freno antes de la prueba y cierre a 290 ppm. Subtítulos karaoke de 2-4 palabras cada 1,1-1,3 s. Una sola transición (flash de 0,4 s). Fotos reales del testimonio a pantalla completa con el avatar en PiP hablando.
- **Lip sync medido:** visemas coherentes cuadro a cuadro y correlación boca/audio con pico en −100 ms: sin desfase grosero.
- Página nueva [[estilo-de-video-ia]] (las 8 reglas de oro + estructura de 90 s + checklist de control) y despiece completo en `OUTPUTS/2026-11-04-analisis-ad-pilates-brasil.md`. El video y las hojas de contactos quedaron en `~/Desktop/referencias-video-ia/pilates-brasil/`.

## 2026-11-04 (5ª pasada) — APIMart instalada en el segundo cerebro

- Santiago: *"Quiero que instales apimart en mi segundo cerebro, utiliza claude in chrome y instalalo vos"*.
- **Cuenta ya existía** (login con Google, creada hoy 10:36) con su clave por defecto, cuota ilimitada y acceso a todos los modelos.
- **Clave guardada en `~/.config/apimart/env`** (chmod 600, fuera del repo). Se copió con el botón de la propia página al portapapeles y se escribió al archivo sin pasar por el chat.
- **Cliente nuevo `scripts/apimart.sh`**: `saldo`, `avatar` (wan2.7-r2v con `reference_voice`), `broll` (grok-imagine-video), `video` crudo, `tarea` y `esperar` (baja el mp4 con `curl -C -`).
- **Probado:** la autenticación funciona; la API responde 402 porque el saldo es **US$0,00**. Falta que Santiago cargue créditos en apimart.ai/es/pricing.
- Página nueva [[apimart]] con endpoints, el flujo asíncrono y los precios al día. **Dos correcciones al Manual de Edición IA:** wan2.7-r2v hoy sale US$0,066/s y Omni Flash 720P US$0,088/s (el precio que el manual recordaba, US$0,036/s, hoy es el de 360P).

## 2026-11-04 (4ª pasada) — Tai Chi Fit: la oferta a los 4 minutos y un CTA pegado al video

- Santiago: *"quiero que todo eso aparezca recién a los 4 minutos… y abajo del VSL ya les pongas un botón de CTA que los redirija directo a checkout, como para que no tengan que deslizar tanto"*. (Arrancó pidiendo sacar todo lo que hay debajo del video y se corrigió solo: *"No, dejalo, dejalo"*.)
- **`SEGUNDOS_OFERTA` pasa de 438 a 240.** Ya no se ata al segundo en que el VSL dice el precio (7:18), sino a los 4 minutos redondos que pidió.
- **Bloque nuevo `#cta-vsl`**: botón "🔥 Quiero empezar ahora" + "pago único de $14.990 · acceso inmediato", a 40 px debajo del player. Aparece con el mismo disparador que la oferta y lleva `data-cta`, así que hereda el checkout y los UTMs como los otros cinco.
- **Probado en el navegador:** los dos arrancan ocultos y aparecen juntos con un `panda_timeupdate` de 241 s.
- 🔴 **Hallazgo:** `tai-chi-fit.impultienda.ar/checkout` devuelve **"Tienda no encontrada"**. Los seis CTAs del quiz apuntan ahí.
- Reglas nuevas en [[quizzes-reglas-de-armado]].

## 2026-11-04 (3ª pasada) — Tai Chi Fit: el VSL montado en el quiz

- Santiago pasó el embed de Panda. Va dentro de `<template id="vsl-template">` y **`SEGUNDOS_OFERTA` queda en 438** (7:18, cuando el VSL dice el precio).
- **Probado paso por paso en el navegador:** el embed carga en 9:16 (396x704), la oferta arranca oculta (`display:none`), se destraba con un `panda_timeupdate` de 439 s —el camino real, no el reloj de respaldo— y los **5 CTAs** apuntan a `tai-chi-fit.impultienda.ar/checkout`.
- **Resto del quiz militar encontrado:** el apelativo por defecto era **"Guerrera"** y se veía tres veces en el último paso ("Guerrera, tu reto de 28 días", "Listo, Guerrera", "seguí así, guerrera"). Pasó a **"Aprendiz"**, el primer nivel del propio quiz. También se limpiaron dos comentarios del CSS ("loading recluta", "cuartel digital"). Regla nueva en [[quizzes-reglas-de-armado]].
- **Aviso:** el player de Panda arranca mudo con su cartel "Pulse aquí para activar el sonido". Eso se configura en el panel de Panda, no desde el HTML (§7).
- Entregables actualizados: `~/Desktop/tai-chi-fit/landing/` (quiz.html, .txt y PRUEBA.html) y `OUTPUTS/2026-11-04-quiz-tai-chi-fit.html`.

## 2026-11-04 (2ª pasada) — Tai Chi Fit: la voz rehecha pareja, y tres bonos que se habían perdido

- Santiago: *"Porque usas voces distintas todo el tiempo? … encima cambia el tono cada dos minutos, le queda muy mal esa voz"*. La voz era Sulafat en todos los bloques, pero **dos salieron con un modelo de TTS y dos con otro** porque se agotó la cuota a mitad de tanda: mismo nombre de voz, otro timbre y otro ritmo (156 vs 132 ppm), justo en el medio del VSL.
- **Rehecho:** cinco bloques parejos (450–500 palabras), **todos con el mismo modelo**, y **todos igualados a 210 ppm** calculando el atempo de cada uno después del recorte de silencios (con el 1.3x fijo quedaban entre 199 y 235).
- **Hallazgo grave en el camino:** el bloque de los bonos **decía el primero y saltaba al quinto**. Se perdían Alivio Oriental, el Té del Monasterio y el Nivel Maestra. El conteo de palabras de `revisar_voz.py` no lo detectaba (los números en cifras tapan la diferencia): ahora se verifica con una **lista de frases obligatorias por bloque**. La lista de bonos quedó en un bloque propio y corto.
- **Otro:** un bloque retomado desde un borrador de HeyGen **perdió la selección de modelo** y salió con Avatar 6 (32 créditos contra 16). Rehecho con el modelo barato.
- Reglas nuevas en [[vsl-reglas-de-armado]] §0b. Entregable actualizado: **8:43**, `SEGUNDOS_OFERTA` pasa a **438**.

## 2026-11-04 — Tai Chi Fit: el VSL entero, armado y editado

- Santiago: *"Arma el video para que quede bien, hace toda la edicion, no quiero videos de stock"*. Entregado: **`~/Desktop/tai-chi-fit/vsl/Tai-Chi-Fit-VSL.mp4`, 8:51, 1080x1920, 155 MB**.
- **Avatar Maestra Valentina** creado en HeyGen con la foto que mandó (9:16 exacto, sin barras blancas). **Voz Sulafat** en cuatro bloques por API, gratis.
- **63 créditos de HeyGen en total.** El selector de modelo venía en **Turbo (Avatar 6)**, el prohibido: se cambió a **"Sincronización de labios"** en cada bloque, que con el audio propio cuesta ~7 créditos por minuto en vez de ~25. Regla nueva en [[vsl-reglas-de-armado]] §3d.
- **La voz se procesa antes de subirla** (recorte de silencios + 1.3x): 12:19 de voz cruda pasaron a 8:51 de video, así no se paga por pausas que después se tiran (§3e).
- **Cero stock y cero imágenes fijas:** los 14 B-rolls son clips reales de TikTok bajados con `yt_dlp` (tikwm quedó detrás de Cloudflare). De 34 clips bajados, **la mayoría venían con texto quemado o la marca de otro anunciante**: se recortaron las franjas y se eligieron a ojo contra una hoja de contactos.
- **Tres fallas del editor nuevo, documentadas en §4g:** el recorte del `.ass` se comía el campo de estilo (video entero sin subtítulos y sin un solo error en el log), las placas PNG sin `-loop 1 -t` hacían fallar el segmento completo, y las placas color papel eran ilegibles sobre la pared beige del dojo.
- **El TTS alucinó** en un bloque al que le toqué el Style para apurarlo: se puso a improvisar diálogo y dijo 324 de 678 palabras. Regla nueva: el Style no se toca para corregir ritmo y ningún bloque pasa de ~550 palabras (§0b).
- **Los subtítulos se alinean contra el guion**, con el caso de palabras pegadas incluido: Whisper escribía *"LO CORROYO"* por *"lo corro yo"* justo sobre el sello de garantía (§4h).
- Script nuevo: `OUTPUTS/scripts-vsl/edit_taichi.py` (render por segmentos en paralelo, 46 segmentos).
- Páginas actualizadas: [[tai-chi-fit]], [[vsl-reglas-de-armado]].

## 2026-11-03 (noche, 9ª pasada) — Tai Chi Fit: la Maestra Valentina queda asiática y sentada

- Santiago, sobre la v2 de la foto del avatar: *"Esta mejor, pero hacela un poco mas asiatica, y que este sentada, porque el fondo quedo medio raro"*.
- **Regla nueva en [[vsl-reglas-de-armado]] §3:** el fondo de la foto de un avatar va **liso y vacío** (nada de ventanas, plantas ni muebles: son tres cosas más para que el generador se equivoque, y es lo primero que delata la imagen) y la avatar va **sentada**, que estabiliza la pose y deja la cara grande en el cuadro.
- **Personaje definido** en [[tai-chi-fit]]: Maestra Valentina, asiática, unos 50 años, sentada, plano medio.

## 2026-11-03 (noche, 9ª pasada) — Las 7 skills de Launch Expert, bajadas e instaladas

- Santiago: *"Quiero que abras todas y que las instales todas en el segundo cerebro, para que tengas absolutamente toda la informacion y trabajemos de la mejor manera"*, sobre `lp.santiagobilbao.com/sk`.
- **Cómo se bajaron:** las 6 primeras son artifacts de claude.ai que renderizan el manual con `marked` desde un `<script type="text/plain" id="md">`; leídas con la herramienta de artifacts solo devuelven la portada ("Cargando el manual…"), así que el texto salió de ese bloque embebido en el HTML. La 07 es un `.zip` con `SKILL.md` + scripts.
- **Instaladas en `~/.claude/skills/`** (7 carpetas, cada una con el manual entero como `SKILL.md`): `edicion-ia`, `embudo-post-compra`, `caza-de-ofertas`, `manejo-cbo`, `pujas-search-scale`, `surfing-scale`, `disputas`. Las dos de los bots y la de disputas traen su código (Python, JS, Swift). Verificado: las 7 quedaron cargadas y activas en la sesión.
- **Detalle técnico que costó una pasada:** el `description` del frontmatter llevaba `: ` sin comillas y eso rompe el YAML. Van entre comillas simples. Si alguna skill nueva no aparece, revisar eso primero.
- **Originales en** `RAW/2026-11-03-skills-launch-expert/` (los 6 `.md` + el `.zip`). Quedaron commiteados dentro de `f8e4507` porque la sesión de Tai Chi Fit corrió `git add -A` en paralelo.
- **Página nueva:** [[skills-launch-expert]] — las 7, qué agrega cada una sobre la wiki, dónde choca con las reglas de Santiago y qué falta para que estén operativas.
- **Páginas ampliadas:** [[caza-de-ofertas]] (arbitraje de sofisticación, los 5 niveles y la tabla de los **tres** filtros que ahora conviven), [[metodo-v3]] (presupuestos en tickets, los primeros 3 días, gasto mínimo de la renovación, ritmo del surfeo atado al presupuesto, Cost Cap / Bid Cap), [[embudo-vsl-post-pago]] (espiar el backend del competidor, ruletas 50/53/47/55, DS conectados en las dos ramas, tabla única para las 8 páginas), [[ugc-y-video-generativo]] y [[vsl-reglas-de-armado]] (rutas de modelo con costo, parámetros SP/GAP/KEEP, defectos de clips IA y control final), [[disputas-y-reembolsos]] (la skill y sus reglas duras), [[estructuras-cbo]], [[escalado-en-meta-ads]], [[aumento-de-aov]], [[funnel-hacking]], [[ia-en-el-flujo-de-trabajo]] e `index.md`.
- **Choques resueltos a favor de Santiago, anotados en cada página:** la voz va **Sulafat / Orus** por API de Google AI Studio y no "una por país"; el visual es **clip de TikTok** y los ads de voz en off a **speed 1.30**; y en la caza manda la **regla madre del 27/10** (fecha e impresiones antes que volumen, marca personal descartada antes de contar el arsenal), con el 40+ ads / semana del manual como piso.
- **Pendiente:** los dos bots quedaron instalados pero **no desplegados** (token de Meta, webhook de Impultienda, servidor y OK para prender) y `disputas` necesita su `.env` y la sección 8 completada.

## 2026-11-03 (noche, 8ª pasada) — Tai Chi Fit: el guion contra el quiz y la foto del avatar

- Santiago: *"Fijate que el mecanismo coincida con lo que decimos en el quiz"*. Tenía razón: **seis cosas no coincidían**. El quiz promete un **manuscrito** y el guion no lo nombraba; **Fluir** es *core y glúteo* y el guion decía "cadera"; faltaban **el espacio de una toalla**, el *"no se trata de terminar reventada, se trata de volverte fuerte"* y la **versión adaptada** de cada movimiento; y **"tu raíz"** (el mecanismo) chocaba con la **Fase Raíz** sin que nadie explicara la relación. Arreglados los seis.
- El guion quedó en **1.830 palabras (~8:55)** y se repartió en **tres bloques** de 3.335, 3.641 y 2.929 caracteres: con los ajustes, dos bloques ya no entraban en el tope de 5.000 de HeyGen.
- Santiago, sobre la foto del avatar: *"no quiero que sea cuerpo completo, se ve super IA, nada organico, muy mala"*. **Regla nueva en [[vsl-reglas-de-armado]] §3:** la foto de un avatar va en **plano medio**, el único requisito duro es el 9:16, el prompt pide una foto casual de celular y quedan **prohibidas** las palabras `cinematic`, `photorealistic`, `85mm`, `shallow depth of field` y `professional photography`. Lo de "full body in frame" era una confusión con la regla de los B-rolls de anatomía.
- Páginas actualizadas: [[vsl-reglas-de-armado]], [[tai-chi-fit]].

## 2026-11-03 (noche, 7ª pasada) — Tai Chi Fit: el guion del VSL, 8 minutos

- Santiago: *"Hagamoslo de 8 minutos, asi es mas completo, armame el guion completo"*. Sube de los 4–6 que había pedido antes.
- **Medida la tasa real del pipeline antes de escribir:** Pilates Hormonal 1.503 palabras → 6:44 y Calistenia Rusa 1.162 → 6:00, o sea **~205 palabras por minuto**. La regla de §0 de [[vsl-reglas-de-armado]] ("850 palabras = 4–5 min") subestima y habría dado un VSL de 5 minutos.
- **Guion entregado:** 1.730 palabras en dos bloques de 4.461 y 4.910 caracteres, los dos por debajo del tope de 5.000 de la Creación rápida de HeyGen. `OUTPUTS/2026-11-03-vsl-tai-chi-fit-guion.md` + `~/Desktop/tai-chi-fit/vsl/`.
- **Decisiones de guion:** mecanismo propio **"tu raíz"** (en vez del "motor metabólico femenino"), villano **el cuerpo en alerta** en vez del cortisol (sin claim médico), se mantiene el open loop del error de los primeros cinco minutos del día, y entran los 5 bonos del quiz con sus valores, el precio con cuotas y la garantía, todo en palabras para la voz.
- **Fuera, como estaba previsto:** el soporte por WhatsApp, el Ozempic, los dos testimonios largos y las "8.000 mujeres".
- Páginas actualizadas: [[tai-chi-fit]].

## 2026-11-03 (noche, 6ª pasada) — Tai Chi Fit: el VSL del original, bajado y mapeado

- Santiago: *"ahora tenemos que hacer el vsl, tiene que durar entre 4 y 6 minutos, que podemos hacer?"*. La página de calistenia asiática para hombres (de donde iba a salir el guion desde el 26/10) nunca llegó, así que el molde pasa a ser **el VSL que corre detrás del mismo quiz** de Calistenia Militar Femenina.
- **Bajado entero:** el player VSLwave esconde un **A/B de dos VSL** detrás del `data-id` del HTML; se resuelve en `cdn.vslwave.site/c/<id>.json` y el master real necesita video id **+ media id**. 18:33, 4.709 palabras, 4:5.
- **Hallazgos:** es un VSL brasileño traducido (dice *"Bloco uno"* en el 18:03 y termina cortado a mitad de frase); la edición está partida al medio (B-roll denso hasta 7:30, después **diez minutos de talking head** con toda la oferta); subtítulos sin franja negra con la palabra clave en amarillo.
- **Mapa de los 20 bloques** con minutos, el destilado a ~1.000 palabras y las alertas (soporte por WhatsApp que no tenemos, las "8.000 mujeres", el Ozempic): `OUTPUTS/2026-11-03-mapa-vsl-original-calistenia-militar.md` + la transcripción con tiempos.
- Plan propuesto y pendiente de su OK: estructura del original, largo y ritmo de nuestro molde propio (Pilates Hormonal / Calistenia Rusa), voz **Sulafat** por API, **Avatar IV** (~125 créditos) y B-rolls a **0 créditos** (TikTok + las imágenes del quiz con zoom).
- Páginas actualizadas: [[tai-chi-fit]].

## 2026-11-03 (noche, 5ª pasada) — Academia del Trazo: CTA en el hero y caja de oferta completa

- Santiago: *"Quiero que pongas un botón de cta entre medio de esos textos, porque sino queda re abajo el botón para comprar… que no lleve al checkout, sino que lleve a la presentación de la oferta, para que vean todo lo que incluye"*.
- **Botón nuevo en el hero**, debajo de los chips: **VER TODO LO QUE INCLUYE** → ancla a la sección "Qué vas a recibir" (`#incluye`), que es la que lista los 6 módulos y desemboca en la caja de precio. **No lleva `js-cta`**, así que el JS no le pisa el href con el checkout ni dispara `AddToCart`.
- Después: *"Esto quedó re peruano, necesito que sea más completo, con toda la información de lo que se lleva, el producto, los bonos"*, con referencia propia: el bloque *Launch Promotion* de `scentedstone.lovable.app`.
- **Caja de oferta rehecha con ese layout** (adaptada a la paleta ocre y al voseo): chapita ★ PRECIO DE LANZAMIENTO ★ montada sobre el borde → nombre del producto en Fraunces + "El método de las 3 capas" → $64.400 tachado → chapita verde del ahorro → **$16.990** gigante → cuotas de Mercado Pago → caja crema **"Todo lo que te llevás"** con un ✓ por módulo y el **acceso de por vida destacado aparte** → caja punteada con 🎁 "+ 4 regalos incluidos, sin costo · Valor $45.600 · HOY: GRATIS" → botón ancho → pago seguro y acceso por mail.
- Todos los precios salen de los `data-` del CONFIG; se sumó `data-cuotas` (antes las cuotas se escribían solo en `#mp-cuotas`, un id único que no se podía repetir).
- **Verificado en el navegador:** el botón del hero apunta a una sección que existe y no al checkout, y la caja no desborda a 350, 420, 560 ni 720 px de contenedor.
- Dos reglas nuevas en [[quizzes-reglas-de-armado]]. Archivos actualizados y copiados al portapapeles.

## 2026-11-03 (noche, 4ª pasada) — Academia del Trazo: el mockup del hero ya no se corta

- Santiago: *"Ajustame esto de la landing de dibujo creativo, fijate que la foto queda cortada y no se ve lo del costado"*.
- **Causa:** el `<img>` del mockup estaba declarado `width="460" height="460"` siendo el archivo **1122×1402**. Con esos atributos, cualquier plantilla que los respete mete la foto en un box cuadrado y le recorta los costados: se perdía el cuarto badge, **"+ CURSO EN VIDEO"**.
- **Arreglo:** dimensiones reales en el tag y blindaje CSS del hero (`width:100%;max-width:520px;height:auto!important;aspect-ratio:auto!important;object-fit:contain!important`). De paso la foto pasó de 460 a **520 px**, así los cuatro badges se leen.
- **Verificado en el navegador:** ratio renderizado 0.8 = ratio natural a 300, 350, 520 y 720 px de contenedor, y aguanta CSS hostil (`img{height:520px;aspect-ratio:1/1;object-fit:cover}`) sin recortarse.
- Actualizados `landing.html`, `PRUEBA.html` y `landing-impultienda.txt` en `~/Desktop/dibujo-creativo/landing/`, y copiado al portapapeles. Regla nueva en [[quizzes-reglas-de-armado]].
- **Dos cosas avisadas:** el mockup sigue siendo el **del competidor** (dice *Universo Creativo* y *Academia de Dibujo Creativo*), y `dibujo-creativo.impultienda.ar` tiene publicada **otra landing** ("29 cursos de dibujo", garantía de 7 días, otro mockup), no la de Academia del Trazo.

## 2026-11-03 (noche, 3ª pasada) — Piedras aromáticas: los 4 anuncios clonados al polaco

- Santiago: *"Ahora hacemelos en polaco"*, sobre los cuatro anuncios de piedras que el 2/11 se habían pasado al ruso.
- **Los cuatro entregados con la misma imagen, la misma cama musical y la duración exacta del original**: PL1 40,27 s · PL2 50,43 s · PL3 42,50 s · PL4 63,07 s. En `~/Desktop/scented-stones-ad/anuncios/polaco/`.
- **El tercer idioma salió en minutos porque no se rehizo nada del video:** las bandas ya limpias de subtítulos (`band.mp4`) y los stems de demucs del pase ruso no dependen del idioma, así que esta tanda fue solo guion + voz + subtítulos. Regla nueva en [[internacionalizacion]], más las fuentes y la cama guardadas en `~/Desktop/scented-stones-ad/anuncios/_assets/`.
- **Localizado, no traducido:** złoty en lugar de dólares (8.000 zł/mes, piedra a menos de 3 zł, se vende a 25–50), **OLX** en lugar de WhatsApp Business, **imieniny** en la lista de ocasiones y el CTA con el texto real del botón de Meta en polaco (*Dowiedz się więcej*). Polonia además se targetea directo, a diferencia de Rusia.
- **Hallazgo de producción: el tempo lo manda el Style, no el largo del texto.** PL2 y PL4 obligaban a acelerar 1.45 (el ruso había quedado en 1.38 como techo). Agregando *"mów bardzo szybko, w tempie reklamy, bez pauz między zdaniami"* al Style, el mismo texto bajó de 73 s a 56 s y de 91 s a 72 s: tempo final **1.12 y 1.14**. Recortar el guion antes había movido casi nada (PL4 recortado 5 % salió igual de largo).
- **Glifos verificados antes de renderizar:** Bitter, Montserrat ExtraBold y Nunito tienen `ą ć ę ł ń ó ś ź ż`; ninguna dibuja tofu. Es la regla de los emojis de [[guiones-y-anuncios]] aplicada a idiomas.
- Voz Sulafat por API con `gemini-3.1-flash-tts-preview` (el `2.5` volvió a dar 429), verificada con Gemini: nativa polaca, sin acento extranjero, sin leer el Style en voz alta.
- Output: `OUTPUTS/2026-11-03-guiones-piedras-polaco-PL1-PL4.md`. Script: `~/Desktop/scented-stones-ad/anuncios/polaco/work/render_pl.py`.

## 2026-11-03 (noche, 2ª pasada) — The Drawing World: landing propia leída y los 6 videos renderizados

- Santiago pasó su landing: *"te mando mi pagina por si queres ajustar algo: https://drawing-world.impultienda.ar/. Haceme los videos"*.
- **Los guiones se ajustaron contra la landing** (regla del 27/10): garantía de **10 días** y no 30, los PDFs con los nombres reales (**The Starter Guide**, **The Practice Workbook**, **21 Days of Anatomy**, **The 250-Project Collection**), fuera el certificado (su página no lo ofrece) y dos frases del hero repetidas tal cual en los ads (*"work you're proud to show"* y *"how many drawings have you left unfinished because you didn't know what the next step was"*).
- **Dos errores avisados de la landing:** el footer todavía dice **GrowithApp, LLC** con la dirección de Newark (es la LLC del competidor, viene del molde de ImpulTienda) y el soporte quedó como el placeholder **[email protected]**.
- **6 videos renderizados** (`DW-V1` a `DW-V6`, ~60 s cada uno) en `~/Desktop/drawing-world/anuncios/`: voz **Sulafat por API** con Style de mujer norteamericana, `speed 1.30`, `silence [0.26, 0.12]`, una sola cama a -8, subtítulos de 2 palabras con la activa en ámbar, chips azules y placa final THE DRAWING WORLD con botón ámbar.
- **Sin bajar un clip nuevo:** se reutilizó el pool de 15 clips de TikTok de manos dibujando de [[academia-del-trazo]], con las mismas ventanas y vetos ya revisados.
- Scripts nuevos reutilizables: `OUTPUTS/scripts-vsl/gen_dw_plans.py` y `OUTPUTS/scripts-vsl/edit_dw.py` (paleta azul #1D3F78 + ámbar #F59E0B de la landing propia).
- **Duraciones finales:** V1 61,7 s · V2 52,4 s · V3 51,8 s · V4 46,7 s · V5 50,1 s · V6 47,4 s (19 a 25 planos, promedio 2,4–2,5 s por plano).
- **Corrección vista en la hoja de contactos del render:** el chip de V2 llevaba flechas `→`, que BarlowCondensed no tiene y salían como cuadraditos. Se cambiaron por `·` y se rehízo solo ese video. Regla nueva en [[guiones-y-anuncios]].
- **Nota de producción:** el TTS `gemini-2.5-flash-preview-tts` volvió a dar 429 y se usó `gemini-3.1-flash-tts-preview`, que con Sulafat no leyó el Style en voz alta (verificado con Gemini: acento americano, sin instrucciones leídas).

## 2026-11-03 (noche) — Academia del Trazo: precio a $16.990 y tanda 1 de 6 videos

- **Precio.** Front de $19.900 → **$16.990 ARS** en la landing (`landing.html`, `PRUEBA.html`,
  `landing-impultienda.txt`): ahorro $47.410, 3 cuotas de $5.664. Actualizado también en
  `WIKI/academia-del-trazo.md` y en el plan de testeo.
- **Los 6 videos de la tanda 1**, renderizados en `~/Desktop/dibujo-creativo/anuncios/`
  (`ADT-V1-las-tres-capas` … `ADT-V6-dia-1-vs-dia-21`, 40–46 s cada uno). Voz Sulafat por API,
  speed 1.30, pool de 101 recortes de **15 clips de TikTok** de manos dibujando, placa final
  ACADEMIA DEL TRAZO. Nuevos scripts: `OUTPUTS/scripts-vsl/gen_trazo_plans.py` y `edit_trazo.py`.
- **Corrección de método registrada:** el modelo `gemini-3.8-flash-tts` **recita el Style en voz alta**
  (la primera tanda de voces salió con 22 s de instrucciones habladas). El que obedece es
  `gemini-2.5-flash-preview-tts`, como ya decía la memoria. Además el free tier es de
  **10 requests por día y por modelo**: conviene no quemarlas en pruebas.
- `tts_gemini.py` acepta ahora `TTS_TEMP` para bajar la temperatura.
- **Cama musical tranquila.** *"Haceme 3 con una música más tranquila"*: script nuevo
  `OUTPUTS/scripts-vsl/music_calma.py` (piano de fieltro + pad, 64 BPM, Am–F–C–G, sin percusión,
  reverb corta) y V1, V2 y V3 re-renderizados como `…-calma.mp4` con los mismos planos. La tanda quedó
  **3 y 3** (V1–V3 tranquila, V4–V6 Herrero): la cama pasa a ser la segunda variable del test y es una
  excepción consciente a la regla de una sola cama por tanda.

## 2026-11-03 (noche) — Lumea Desenului: análisis completo y tanda 1 en inglés (Draw in 21)

- Santiago pasó la Biblioteca de `lumea-desenului-pl.impultienda.ar`: *"Vamos a armar ads para una oferta, la vamos a tirar en ingles… vamos a hacer un analisis completo y despues armamos los ads"*. Durante el trabajo fijó: **la experta es Juliana Alves** y el **costo 19,99**.
- **430 ads leídos** de la fanpage **Elena Popescu** (217 activos, 213 pausados), todos lanzados en **13 días** desde el 21/10. Una sola fanpage, un solo producto y **9 mercados en paralelo** con un subdominio de ImpulTienda cada uno: PL 32, IT 32, RO 17, CZ 9, FR 8, **ZA en inglés 8**, PT 3, GR 1, TR 1.
- **El hallazgo:** el inglés lo probó recién el 30/10 y solo en Sudáfrica. US/CA/AU/UK/NZ están vacíos, y el nicho exacto también (en inglés solo hay arte digital con marca personal —FunWithDrawing/Charly Clements, Procreate— y libros de 21-Draw).
- **Es el mismo PLR que [[academia-del-trazo]]**: en un video se ve la tablet con las tapas en español *"Naturaleza Muerta"* y *"Academia de Dibujo Creativo"*. Y usa **nuestro mismo stack**: ImpulTienda con los comentarios del HTML en español, Stripe en USD, `/checkout?upsells=2` con dos upsells pre-tildados y exit-intent anti-YouTube del 15%.
- **10 videos transcriptos** con Gemini. La familia que más duplica es el **día por día (Day 1 → Day 21)** con un resultado concreto por día y el remate *"la mayoría no le sale porque empieza por el día 24"*; después el **orden/anti-YouTube**, el **talento es práctica que no viste**, el **se aprende dibujando y no es la edad** y el **error nº1 de saltarse la esfera**.
- **Sus agujeros**: checkout con labels en español sobre contenido en inglés, 74 lecciones en los ads contra 54 en la landing, garantía de 10 días en la página y 7 en el video, prueba social del molde (*"only in South Africa"*).
- **Tanda 1 de 6 guiones** (oferta nueva = 6), uno por familia ganadora, EN + ES voseo, con garantía de 30 días, entregables con nombre y el mecanismo bautizado **Shape-First Order**. Carpeta nueva `~/Desktop/draw-in-21/`.
- Outputs: `OUTPUTS/2026-11-03-analisis-lumea-desenului.md`, `OUTPUTS/2026-11-03-guiones-draw-in-21.md`. Página nueva: `WIKI/draw-in-21.md`.

## 2026-11-03 (tarde) — Academia del Trazo: landing propia + análisis de los 80 ads del original

- Santiago pasó la Biblioteca de la página 1153035077882881 (Academia de Dibujo Creativo / Universo Creativo, de Valentina Restrepo) para modelarla en Argentina: *"la landing no me gusta mucho… tratemos de mejorar eso. Primero armemos la landing y después vamos con los anuncios."*
- **Leídos los 80 ads activos** uno por uno desde la Biblioteca: 38 videos únicos + 42 imágenes, dos primary text para todo, línea de tiempo completa (control del 14/7, 48 ads del 15 al 22/9, tanda nueva el 27/10).
- **9 videos transcriptos y analizados** con Gemini (`gemini-3.5-flash`, video inline). Formato único: voz en off femenina + b-roll de manos dibujando, 9:16, subtítulos palabra por palabra, piano, 40–57 s. Cuatro de nueve son el mismo ángulo ("el talento no existe").
- **Corrección de Santiago en el momento:** *"No descargues absolutamente todos los ads, ya te dije eso"*. Se cortó la bajada y se quedó una muestra de 10 que cubre todas las fechas y duraciones. Regla sumada a `WIKI/funnel-hacking.md`.
- **Landing nueva armada y probada en Chrome**, en `~/Desktop/dibujo-creativo/landing/`: promesa con número, dolores, mecanismo propio (Método de las 3 Capas), producto, bonus x4, oferta con contador y cuotas, garantía de 30 días, barra de compra fija y notificaciones discretas. Un solo producto, sin bundles, y el ahorro en pesos en vez de "50% OFF".
- **Tanda 1 de 6 guiones + 2 descripciones** con ángulos que el original no corre, y plan de testeo V3 para Argentina.
- Outputs: `OUTPUTS/2026-11-03-analisis-academia-dibujo-creativo.md`, `OUTPUTS/2026-11-03-plan-de-testeo-academia-del-trazo.md`, `OUTPUTS/2026-11-03-guiones-academia-del-trazo.md`. Página nueva: `WIKI/academia-del-trazo.md`.

## 2026-11-03 — Atlas de Cortes: 3 renovaciones (V49–V51) con la cuenta leída antes

- Santiago: *"Vamos con 3 renovaciones para pelo, fijate que esta funcionando y armemos"*.
- **Se leyó la cuenta de escalado por MCP (`1791862825108056`, 7 días):** la que manda es **NATIVE 1**, la native **corta** ($16 de CPA, $11,87 en su mejor conjunto, 25 compras); **NATIVE 6** confirma el formato ($17,50, dos conjuntos abajo de $12,50); **NATIVE 3 (nuestra native 1, la larga) se cayó a $45** y toca renovarla. CTR de 32 a 47 % en todas: el problema no es el enganche, es el CPA.
- **La cuenta donde se testean los videos de pelo sigue sin poder leerse** (las dos candidatas del portfolio Reset FIT están fuera del MCP o sin liquidar): de los V37 al V51 no hay CPA propio. Quedó como gap número 1 en `WIKI/index.md`.
- **Entregadas las renovaciones V49–V51**: hooks nuevos sobre los tres cuerpos del 2/11 (los únicos en la DNA validada), en tres formatos distintos — declaración de mecanismo (el brushing dura cuatro días), lista (los cortes que esquiva, hook sacado del testimonio de la landing) y UGC en primera persona (el formato de la native que escala). EN + ES voseo.
- **Videos listos:** `AT-V49.mp4` (36,2 s), `AT-V50.mp4` (35,6 s) y `AT-V51.mp4` (39,0 s), voz Sulafat **por API** (primera tanda del Atlas sin AI Studio) y verificación de que no lee el Style con `gemini-3.5-transcribe`.
- **Pool renovado sin bajar un clip:** el clip principal dura 8:21 y solo se usaban 2:33; revisando a 1 cuadro por segundo entraron 15 recortes nuevos (87 → 102) y se vetaron tres tramos con texto quemado, un frasco de producto y una placa final en vietnamita.
- Reglas nuevas: *"fijate qué está funcionando" = leer la cuenta por MCP antes de escribir* (`WIKI/guiones-y-anuncios.md`) y *una renovación se ve distinta aunque no bajes un clip nuevo* (`WIKI/renovacion-de-creativos.md`).
- Output: `OUTPUTS/2026-11-03-renovaciones-atlas-cortes-v49-v51.md`. Videos y guiones en `~/Desktop/atlas-cortes/anuncios/`.

## 2026-11-02 (noche, 4ª pasada) — Los 4 anuncios de piedras, clonados al ruso

- Santiago pasó cuatro anuncios suyos en inglés (`Im 58…`, `In the next 30`, `My accountant…`, `Ok I need`) y pidió *"estos mismos anuncios pero en ruso, todo igual"*.
- Se entregaron los cuatro con **la misma imagen, la misma cama musical y la misma duración exacta**: solo cambia la voz (Sulafat en ruso) y los subtítulos, rehechos con la misma tipografía, color de caja y posición que el original.
- Pipeline nuevo y reutilizable: transcribir con Gemini → separar la música con demucs → guion ruso medido → voz por API → borrar los subtítulos ingleses por inpainting → quemar los rusos. Documentado en `WIKI/internacionalizacion.md` y guardado en `~/Desktop/scented-stones-ad/anuncios/ruso/work/render_ru.py`.
- **Regla nueva:** si el TTS `gemini-2.5-flash-preview-tts` devuelve 429, el reemplazo es `gemini-3.1-flash-tts-preview` (no lee el Style en voz alta). En `WIKI/como-trabajar-con-santiago.md`.
- Output: `OUTPUTS/2026-11-02-guiones-piedras-ruso-RU1-RU4.md`. Videos en `~/Desktop/scented-stones-ad/anuncios/ruso/`.

## 2026-11-02 (noche, 3ª pasada) — La misma caza en inglés: tres que cumplen todo

- Santiago eligió **mantener la VSL y cambiar de mercado**. Con los criterios intactos (infoproducto digital + VSL + 50+ ads + no marca personal + salud/renta extra), en EE.UU. salieron **tres en la primera pasada**, contra cero en Brasil.
- **SSAcademy** (124 ads, 52 días sin pausar, VSL 1:46–2:57, ClickFunnels, renta extra, faceless) es **4/4 y candidata A**. Atrás: **V Shred** (440 ads en US, 3,5 meses, quiz→VSL, infoproducto de fitness) y **30 Second Clients** (151 ads, VSL 1:01–2:09, renta extra), ambas 3/4.
- **Regla nueva a la WIKI:** en salud la VSL es casi siempre **producto físico** — las dos mejores VSL de salud en inglés venden una crema (Sciatica Center, 184 ads) y una máscara térmica (Sinus Relief Insider, 97 ads, activa desde el 25/05). El infoproducto con VSL vive en renta extra.
- Footprints en inglés que funcionaron: `instant access` (infoproducto digital), `faceless` (renta extra sin cara), `free presentation` (VSL). El discriminador universal sigue siendo la duración del creativo en el UI: 1:00–3:00 = VSL.
- Output: `OUTPUTS/2026-11-02-caza-infoproductos-vsl-ingles.md`, registro en `WIKI/caza-de-ofertas.md`, enlazado en `WIKI/index.md`.

## 2026-11-02 (noche, 2ª pasada) — Caza de infoproductos con VSL en Brasil: la celda vacía

- Santiago rechazó la primera pasada: *"ninguno es un infoproducto, ademas, son marcas personales o marcas reconocidas, son productos fisicos, no es nada de lo que te pedi, hace bien la busqueda, tarda lo que tengas que tardar"*. Tenía razón: LIQUIDZ y DRM Plus son producto físico y Venda Sem Estoque es marca personal.
- Segunda pasada apuntada solo a **infoproducto digital con VSL**: ~40 búsquedas y ~2.000 anuncios escaneados. **No existe ninguna oferta que cumpla los cuatro criterios a la vez** (infoproducto + VSL + 50 ads + no marca personal, en salud o renta extra en Brasil).
- **El hallazgo:** la VSL está prácticamente extinta en Meta Brasil — de 321 anuncios de video activos muestreados, solo 4 anunciantes pasan los 110 s y ninguno tiene volumen. El mercado corre creativo corto → WhatsApp / Instagram / checkout directo. Y el filtro de 50+ ads por fanpage excluye por construcción al infoproducto low ticket, que rota decenas de fanpages con 1–48 ads cada una.
- Mejor oferta del perfil pedido: **Arquivos que encantam** (48 ads, 18 días, Kit Lembrancinhas a R$10, página no personal), sin VSL. Cluster "que encantam": 194 ads activos.
- WIKI: registro largo en `caza-de-ofertas.md` con los footprints que aíslan infoproducto (`kiwify`, `hotmart`, precio en el link title), el que aísla VSL (duración del creativo en el UI), los que solo traen ruido en Brasil, y la trampa del **display link falso** de la Biblioteca de Anuncios. Queda resuelta la pregunta abierta del umbral de ads para nichos chicos.
- Output: `OUTPUTS/2026-11-02-caza-infoproductos-vsl-brasil.md`, enlazado en `WIKI/index.md`.

## 2026-11-02 (noche) — Caza de VSL en Brasil: salud y renta extra

- Pedido de Santiago: *"usemos la skill de cazar y quiero que encontremos únicamente ofertas con VSL … validadas, que no sean de marcas personales, que tengan más de 50 anuncios y dame mínimo 3 … nicho de salud o de renta extra en Brasil"*.
- Barrido con el conector oficial de Meta (`ads_library_search`) + verificación visual de cada candidato en la Biblioteca de Anuncios y de las landings en Chrome. **No hay 3 que cumplan todo:** de los que pasan 50+ anuncios activos en esos nichos, solo **Venda Sem Estoque** (~110 ads, `site.marcelowedrop.com`, "A aula está liberada", 6 semanas sin pausar) tiene VSL. **LIQUIDZ** (~670 ads, activos desde ago 2025) es e-commerce y **DRM Plus** (~130 ads, zumbido/sueño, $5) manda a WhatsApp, igual que la flota de 16 fanpages de **Dra. Caroline Townsend**.
- Hallazgo de mercado: en Brasil el gasto grande de salud migró a embudos de WhatsApp; el cluster de VSL de salud con 50+ ads no existe hoy.
- Output: `OUTPUTS/2026-11-02-caza-vsl-brasil-salud-renta-extra.md` (tabla de descartados con número, veredicto y los footprints de búsqueda que sí trajeron VSL), enlazado en `WIKI/index.md`.

## 2026-11-02 (tarde) — Herrero LATAM: una sola cama musical (`bed_B`) en los 10

- Santiago escucho los 10 videos de la tanda LATAM: *"Ajusta la musica, en algunos se escucha muy mal, quiero todos con la musica del que empieza con: Piensan..."*. Ese es el **L3** ("Piensa en el martes en la noche..."), que llevaba `bed_B`; los otros nueve iban con `bed_A` y `bed_C` rotados.
- `MUS` en `anuncios/work/plans/gen12.py` pasa a **`bed_B` fijo** para los diez. Los 10 videos re-renderizados restaurando `usage_pre_latam.json` y rehaciendo L1->L10 en orden: **mismos clips y mismos subtitulos, solo cambia la cama**. Verificado comparando un cuadro de cada video antes/despues (los 10 identicos) y el `usage.json` final con el de la primera pasada (identico). Correlacion del arranque de cada mezcla contra las tres camas: los 10 dan `bed_B`.
- `bed_A` y `bed_C` quedan descartados para esta voz. La costura del loop de `bed_B` (44 s) revisada en los videos de mas de 44 s: sin salto de nivel.
- WIKI: regla nueva en `guiones-y-anuncios.md` (**el generador de planes no rota beds nunca**, refuerzo de la del 27/10), cama por defecto de Herrero actualizada en `vsl-reglas-de-armado.md` y nota de armado en `herrero-de-finde.md`.

## 2026-11-02 — Herrero: salto a LATAM con "Herrero de Ocio", 10 videos en español neutro

- **Pedido de Santiago:** *"vamos a poner los anuncios para LATAM … un idioma con acento neutro … acordate lo que funcionó … replicámoslos … mismo anuncio, mismos visuales, mismo guión … armame 10 videos"*, más un ad de la biblioteca para replicar y su clave de API de Google AI Studio.
- **La tanda es el banco de ganadores, no guiónes nuevos:** V7 (CPA 1,00) → L2, V47 (4,00) → L3, V48 (5,53) → L4, V46 (6,85) → L5, V6 (7,05) → L6, V2 (8,70) → L10, V3 (10,71) → L9, V5 (11,39) → L7, V4 (13,56) → L8. Los que no vendieron (V1, V43, V44, V45) quedaron afuera.
- **L1 es la réplica del ad que mandó** (ad library 1705765621113551, 30/10, 34 s): *"$2,400 in steel. $4,730 for the camping trailer. Two weekends"*. Es la plantilla más duplicada de la cuenta — aparece en 10 de los 180 videos de la muestra — y la página pasó de 367 a **447 anuncios activos** desde el 22/10.
- **Lo que cambia de AR a LATAM:** acento latino neutro con tuteo (verificado mandándole el wav a Gemini: *"latino neutro, sin marcas regionales"*, 9/10), **números en dólares** (los pesos eran los dólares del original ×1.000), léxico neutro (fin de semana, dinero, gasolina, esmeriladora, tronzadora, ferretería, acero, brasero) y la marca del cierre pasa a **HERRERO DE OCIO**.
- **Las voces salen por API, no por el navegador.** `OUTPUTS/scripts-vsl/tts_gemini.py` + `gemini-2.5-flash-preview-tts` + voz **Orus**: las diez en una corrida, sin pestañas ni el límite de una generación por carga. Los TTS 3.x **recitan las instrucciones de estilo** por API, así que no sirven. La clave vive en `~/.config/herrero/gemini.env`, fuera del repo.
- **10 y no 6:** lo pidió explícito; se le marcó que la regla de tanda es 6, pero acá son nueve creativos ya validados más una réplica.
- **Pendiente del embudo:** la landing y el checkout siguen en pesos y con Mercado Pago, que no vende multipaís. Los ads no dicen precio, así que no bloquean el testeo.
- **Los 10 videos producidos** en `~/Desktop/herrero-de-finde/anuncios/latam/`, de 0:30 a 1:02 (el L2, que es el V7, es el más largo). Verificados sobre el render: los diez cierres dicen HERRERO DE OCIO, los hooks con tilde, los chips en la palabra, sin tramos vetados ni avisos de ancla.
- Entregado en `OUTPUTS/2026-11-02-guiones-herrero-latam-L1-L10.md`, `~/Desktop/herrero-de-finde/anuncios/guiones-latam-L1-L10.md` y al portapapeles. Planes en `anuncios/work/plans/gen12.py`.
- Sin archivos de RAW procesados.

## 2026-11-02 — Atlas de Cortes: tanda v46–v48, vuelta a la DNA que validó la cuenta

- **Pedido de Santiago:** *"vamos con ads para pelo, no están funcionando los que hicimos, repasá las cosas que te dije que funcionaron en la oferta, y armemos 3 nuevos."*
- **Diagnóstico:** de la V25 a la V45 todo fue bizop (el ángulo que fijó el 28/10). Lo que la cuenta validó dos veces es **fricción durante el servicio con la clienta sentada** + *"no es tu técnica, es memoria"*: V2 $18,61 (5 compras), V3 $17,47 (6 compras), V8 y los dos ads ajenos de $11. Los dos peores de la cuenta son los dos de plata en el hook (V4 $22,38 y V5 $22,61). El sleeper V6 (la carpetita, $13,39 con volumen) seguía sin explotar desde el 23/10.
- **3 guiones nuevos** con el hook en territorio validado y el bizop al final y suave: **V46** el "no, I love it" de compromiso (territorio V2 + minuto del espejo), **V47** el congelamiento a mitad del corte (territorio V3, el de más volumen) y **V48** "she just reads it first" (el V6 / la carpetita, permiso y prueba social, la línea que ya corre en las natives que escalan). EN + ES voseo, nombres **2/11 - 1, 2 y 3**.
- **Regla nueva en `WIKI/guiones-y-anuncios.md` (2026-11-02):** *"no están funcionando" = volver a lo validado, no a otra variable del mismo eje*. El ángulo que él fija no se tira: baja al final del guion, sin cifras. Modula la regla del 29/10.
- **Los 3 videos producidos:** `AT-V46.mp4` (40,6 s), `AT-V47.mp4` (37,5 s) y `AT-V48.mp4` (37,1 s), voz Sulafat, `speed 1.30`, hojas de contactos revisadas.
- **Natives, tanda 7 (15 y 16):** una larga (Dell Hausman, Muscatine IA, la foto descolorida del espejo — el AT-V47 en native) y una corta (el "no, me encanta" de compromiso — el AT-V46 en native), las dos en el territorio validado. `OUTPUTS/2026-11-02-natives-atlas-cortes-15-y-16.md`.
- Entregado en `OUTPUTS/2026-11-02-guiones-atlas-cortes-v46-v48.md`, `~/Desktop/atlas-cortes/anuncios/guiones/guiones-v46-v48.md` y al portapapeles.
- **Regla nueva (Santiago, 2/11):** *"Dame los prompt y descripciones, no me sirve que me las mandes así"*. Las natives se entregan con **el prompt de imagen y la descripción completos en bloques de código en el chat**, no con un resumen y el link al archivo. Queda en `WIKI/como-trabajar-con-santiago.md`.
- Sin archivos de RAW procesados.

## 2026-11-01 — Mentoría: Módulo 1 pasado a formato guía (corrección de Santiago)

- **Corrección de Santiago sobre el formato de los documentos de la mentoría:** *"Quedó muy bien, pero fuiste demasiado al detalle. Los títulos, el orden, los cuadros están genial, pero ir súper detallado en las explicaciones no me gustó tanto, porque eso me da poco margen para improvisar y hablar, entonces solo termino leyendo. Hacelo más como guía, que tenga lo más importante."*
- **Regla nueva (queda en `WIKI/mentoria.md`):** el documento de cada módulo es una **guía, no un ensayo**. Se mantienen títulos, orden y cuadros; las explicaciones van en viñetas cortas con el dato clave adentro. Medida práctica: **~2.000–2.500 palabras por módulo**, no 7.000. Si hace falta teoría larga, va en un doc de respaldo aparte.
- **Módulo 1 reescrito como guía de clase** (2.438 palabras, 9 secciones, de 7.058 que tenía): el punto del módulo · qué es una oferta ganadora · la Biblioteca de Anuncios · cómo se lee si vende · las otras plataformas · nichos y mercados · auditar al competidor · el scorecard y la ficha · errores, rutina y tarea. Se conservaron los dos cuadros de URLs listas y la ficha de oferta en ASCII.
- Entregado en los tres formatos: Claude Doc https://claude.ai/artifact/41sAqcCnPCRasmRxmyo75U · `~/Desktop/Mentoria/Modulo 1 - Guia de clase.docx` · `OUTPUTS/2026-11-01-modulo-1-guia-de-clase.md`.
- El doc detallado anterior **no se borró**: pasó a llamarse *"Módulo 1 — Teoría completa (respaldo, no para dar la clase)"* (mismo link, https://claude.ai/artifact/9q5Vd2ZNRXVuyXKMfdpRMm).
- Sin archivos de RAW procesados.

## 2026-11-01 — BarberPro: los 6 videos producidos + regla de voces fijas
- **Regla nueva (Santiago): las voces son fijas.** *"Usa las voces que siempre usas, si es de hombre usa de hombre, si es mujer usa mujer, no quiero una nueva por cada oferta, si la quisiera te lo voy a decir."* **Mujer = Sulafat, hombre = Orus.** No se mandan opciones a elegir; lo único que se decide por oferta es el género del avatar. Queda en `WIKI/como-trabajar-con-santiago.md` y `WIKI/vsl-reglas-de-armado.md`.
- Los 6 ads producidos con **Orus**: `~/Desktop/barber-pro/anuncios/BP-V1.mp4` a `BP-V6.mp4` (22,8 a 27,6 s, 9:16, 9 a 12 planos), `speed 1.30`, `silence [0.26, 0.12]`.
- Editor nuevo `OUTPUTS/scripts-vsl/edit_barber.py` (paleta negro + ámbar de la landing) y generador `OUTPUTS/scripts-vsl/gen_barber_plans.py` (valida que el primer plano exista en el pool).
- Pool de 9 clips de TikTok limpios; 11 descartados por texto quemado y 2 más cazados en la hoja del render ("LEVER OPEN").
- Descripción para ads: `OUTPUTS/2026-11-01-descripcion-ads-barber-pro.md` (principal + corta en inglés, 3 titulares de 30 caracteres y la versión en español de referencia). Copia en `~/Desktop/barber-pro/anuncios/descripcion-ads.md`.
- Trampas nuevas anotadas en `WIKI/barber-pro.md` y `WIKI/vsl-reglas-de-armado.md`: el Run de AI Studio queda bloqueado hasta que el audio termina de sonar, el Style se come el texto si el desplegable está abierto, la placa final no entra si se ancla en la última palabra, y el cuadro final hay que sacarlo por timestamp absoluto.

## 2026-11-01 — Mentoría: Módulo 1 (búsqueda de ofertas ganadoras)
- Santiago arranca su propia **mentoría** de infoproductos low ticket, tomando como referencia la School de Santiago Bilbao. Un documento detallado y editable por módulo; da la clase con el documento en pantalla y los ejemplos en vivo.
- **No hay documento de introducción** (lo pidió explícito): el video de intro va sin doc y se arranca directo en el Módulo 1.
- **Módulo 1 entregado:** 7.000 palabras con toda la teoría de cómo encontrar ofertas ganadoras. Secciones: las 5 condiciones de una oferta ganadora · modelar ≠ clonar y la regla de nunca modelar en el mismo mercado · la Biblioteca de Anuncios paso a paso (URLs listas, `country=ALL`, `start_date`, `sort_data[mode]=total_impressions`, los 4 ejes de keywords con footprints de checkout) · las señales (la fecha antes que el volumen, la regla de los 3 días, escalera de certeza, descartes automáticos) · las otras plataformas y marketplaces · mapa de nichos × mercados · auditoría del competidor en 5 pasos (incluido comprarle) · scorecard de 4 señales y veredicto ENTRAR/SUBNICHO/DESCARTAR/WHALE · los 12 errores que matan la cacería · rutina semanal y dos plantillas · tarea y criterio de aprobación.
- Entregado en tres formatos: Claude Doc editable (https://claude.ai/artifact/9q5Vd2ZNRXVuyXKMfdpRMm), `.docx` en `~/Desktop/Mentoria/` para su Drive, y `OUTPUTS/2026-11-01-modulo-1-busqueda-de-ofertas-ganadoras.md`.
- Nueva página `WIKI/mentoria.md` con la regla fija de entrega de módulos, el orden propuesto (2 a 6 sin confirmar) y las preguntas abiertas.
- No se procesaron archivos de RAW: el módulo se armó con la WIKI existente ([[funnel-hacking]], [[caza-de-ofertas]], [[seleccion-y-modelado-de-oferta]], [[validacion-de-oferta]], [[segmentos-de-mercado]], [[modelo-low-ticket]], [[internacionalizacion]]).

## 2026-11-01 — Vence al Parkinson: oferta nueva, análisis del competidor y tanda 1
- Oferta nueva para **Argentina** (Santiago lo confirmó: "es para Argentina", así que va todo en voseo). Landing propia `vence-al-parkinson.impultienda.ar` bajada con curl y leída entera.
- Competidor: página **Tom Miller**, misma plataforma (ImpulTienda). **30 ads activos**, el más viejo del 5/10 (27 días). Los 30 videos bajados de la Biblioteca de Anuncios y transcriptos con faster-whisper: **un solo cuerpo repetido palabra por palabra y 21 hooks distintos**. El hook campeón (7 copias) es el miedo a que la familia tenga que hacer por vos lo que hoy hacés solo; el más viejo (4 copias) es el stack de síntomas.
- Tanda 1 de 6 guiones, uno por familia ganadora, cada uno con cuerpo y cierre propios: `OUTPUTS/2026-11-01-guiones-vence-al-parkinson-v1-v6.md`.
- Nueva página `WIKI/vence-al-parkinson.md` con la DNA del ganador, su edición plano por plano y el riesgo de atributos personales de Meta.
- Material en `~/Desktop/vence-al-parkinson/anuncios/work/ganadores/` (30 MP4, transcripciones y hojas de contacto).
- **Voces:** 3 opciones en AI Studio (Sulafat cálida, Algieba hombre, Gacrux mujer grande). Eligió la **1 y la 3** y pidió alternarlas: V1/V3/V5 con Sulafat, V2/V4/V6 con Gacrux.
- **B-roll:** 145 clips de TikTok de 4 tags + 76 de los perfiles de los creadores que pasaron el filtro. **Rendimiento bajísimo** (el nicho es educativo: casi todo con subtítulo quemado o cara a cámara): quedaron 16 limpios.
- **Videos:** 6 renders de voz en off con `edit_parkinson.py` (nuevo), con el look del ganador: placas blancas con la palabra clave en dorado. Parche al editor: el reparto del pool ahora usa `fam` (creador) y no la primera letra del nombre del archivo.
- Regla nueva en `WIKI/vsl-reglas-de-armado.md`: en AI Studio, **después de bajar un audio el primer Run no dispara** (el Download vuelve a traer el anterior con el mismo md5).

## 2026-11-01 — BarberPro MegaPack: oferta nueva, análisis del competidor y tanda 1
- Oferta nueva en inglés. Landing propia `barber-pro.impultienda.ar` bajada con curl y leída entera; competidor "Barbería Online" (page 544737342047119) relevado: 58 ads activos, 28 en inglés.
- Los 28 ads en inglés bajados y transcriptos con faster-whisper: **un solo cuerpo repetido palabra por palabra y 28 hooks distintos**. Seis familias de hook, la de "replay / lo ves una sola vez" es la ganadora (los 3 ads del 1/11 son de esa).
- Tanda 1 de 6 guiones, EN + ES voseo, cada uno con cuerpo propio: `OUTPUTS/2026-11-01-guiones-barber-pro-v1-v6.md` y `~/Desktop/barber-pro/anuncios/guiones/`.
- Tres opciones de voz masculina (Arlo, Daro, Enzo) en `~/Desktop/barber-pro/anuncios/voces/`, ya a speed 1.30, para que elija.
- Nueva página `WIKI/barber-pro.md`. **Regla nueva en `WIKI/guiones-y-anuncios.md`: "Estándar de producción de video"** — visuales 100% de TikTok, prohibido el stock y la foto fija, clips limpios, velocidad y revisión obligatoria. Queda fija para no repetirla.

## 2026-11-01 — Atlas de Cortes: natives 13 y 14
- Tanda 6 de natives, solo en inglés: `OUTPUTS/2026-11-01-natives-atlas-cortes-13-y-14.md`. Una larga (1.940 palabras) y una corta (641), las dos en ángulo bizop y emparejadas con los videos de hoy.
- 13: Earlene Pankey (59, Bluefield WV) y el rollo de papel de la registradora con los once nombres que mandó a otro lado en diciembre — el AT-V43 pasado a native.
- 14: la clienta para la que vas a trabajar gratis esta semana — el AT-V45 en el formato corto que escala, con bonus y garantía y sin precio.
- Copia en `~/Desktop/atlas-cortes/anuncios/natives/2026-11-01-natives-tanda-6.md`. `WIKI/atlas-de-cortes.md` y `WIKI/index.md` al día.

## 2026-11-01 — Atlas de Cortes: renovaciones v43–v45
- Tres renovaciones (hook nuevo sobre cuerpo validado), ángulo bizop fijo: `OUTPUTS/2026-11-01-renovaciones-atlas-cortes-v43-v45.md`, EN + ES voseo.
- Cuerpos elegidos: los tres que no se renovaron ayer — V34 (ventana de las fiestas, que arranca hoy), V39/V36 (la única publicidad gratis) y V28 (la corrección gratis como turno regalado).
- Hooks con la regla del 30/10 (la primera línea afirma algo que choca y se explica recién en la siguiente), un solo número por guion y Cut Maps con nombre propio.
- Copia en `~/Desktop/atlas-cortes/anuncios/guiones/renovaciones-v43-v45.md`. Nombres para subir: 1/11 - 1, 2 y 3.
- **Videos producidos:** `AT-V43.mp4` (34,8 s), `AT-V44.mp4` (35,7 s) y `AT-V45.mp4` (35,2 s) en `~/Desktop/atlas-cortes/anuncios/`, 9:16, voz Sulafat a 1,30, los tres con hoja de contactos revisada.
- Dos trampas nuevas en `WIKI/atlas-de-cortes.md`: una palabra repetida ("week", 3 veces) ancló la placa final a los 15 s y dejó el V45 en un solo plano, y dos chips a menos de 1 s se pisaron en pantalla.

## 2026-11-01 — Piedras: guiones v36 "potentes y de bizop" (19 a 21)
- Tanda de 3 variables, inglés y español con voseo: `OUTPUTS/2026-11-01-guiones-piedras-v36-potentes-bizop.md`, 50 a 55 s.
- Misma apertura "afirmación que suena imposible" de la v33–v35, con el cuerpo entero empujado al bizop: velocidad al primer peso (martes/sábado), el lavadero de autos como cliente mensual (la piedra como consumible, no como decoración) y el catálogo que son solo tres aromas.
- Un solo número de plata por guion y como precio de mercado; la plata que se nombra es la de la persona que mira el anuncio, no la de un negocio visto desde arriba (regla del 30/10).
- `WIKI/scented-stones.md` y `WIKI/index.md` al día con la tanda y el banco restante. Sin reglas nuevas: no hubo correcciones.

## 2026-10-31 — Perles Merveilles 3D: tanda 2, 3 variables producidas
- Tres guiones nuevos (no solo hooks nuevos: cambian ángulo y emoción): `OUTPUTS/2026-10-31-guiones-perles-merveilles-v7-v9.md`, inglés y español con voseo.
- Producidos `PM-V7-which-shop-is-it-from.mp4`, `PM-V8-same-two-movements.mp4` y `PM-V9-forty-minutes.mp4` en `~/Desktop/perles-merveilles-3d/anuncios/`, 9:16, voz Sulafat a 1,30 y B-roll 100% de TikTok.
- Planes en `anuncios/work/plans/gen2.py` con `usage.json` compartido con la tanda 1, así que ningún recorte se repite entre las dos tandas.
- Dos reglas nuevas en `WIKI/vsl-reglas-de-armado.md`, las dos arregladas en `edit_perles.py`: una placa de más de 24 caracteres salía cortada a los dos lados (ahora se le achica el cuerpo hasta que entra) y un emoji fuera del rango `1F300-1FAFF`/`2600-27BF` salía como cuadradito en el hook (ahora entran también los relojes, `231A-23FA`).
- La WIKI de la oferta queda con las dos tandas y con las descripciones de ads enlazadas (faltan las natives).

## 2026-10-31 — Atlas de Cortes: natives 11 y 12
- Tanda 5 de natives: `OUTPUTS/2026-10-31-natives-atlas-cortes-11-y-12.md`. La 11 es larga (Charlene Ostrander, Bucyrus OH, la columna de la agenda que dice "trim" nueve años seguidos) y la 12 es corta (651 palabras), en el formato que la cuenta ya escala y que no era nuestro.
- Las dos con prompt de imagen 3:4 sin caras ni texto legible, solo en inglés, sin precio.

## 2026-10-31 — Atlas de Cortes: renovaciones v40-v42 producidas
- Tres renovaciones (hook nuevo sobre cuerpo validado) de los ángulos que ya rinden: "Are you"/V33, V37 y V38. `OUTPUTS/2026-10-31-renovaciones-atlas-cortes-v40-v42.md`.
- Videos `AT-V40.mp4` (39,0 s), `AT-V41.mp4` (31,9 s) y `AT-V42.mp4` (34,1 s) en `~/Desktop/atlas-cortes/anuncios/`, voz Sulafat, speed 1,30, los tres MD5 distintos y hojas de contactos revisadas.
- Trampa nueva en `WIKI/atlas-de-cortes.md`: el clip D del pool tenía texto quemado en español en varios tramos (el V40 abría con él). Se sacaron [36,42], [63,66], [78,84] y [90,96] y se rehicieron los tres.

## 2026-10-31 — Piedras: guiones v35 "más potentes" (16 a 18)
- Segunda tanda del día, en inglés y español con voseo: `OUTPUTS/2026-10-31-guiones-piedras-v35-mas-potentes.md`, 50 a 55 s. Con la v34 queda cerrado el tope de 6 videos del día.
- Ángulos nuevos: los cuatro gramos de agua (competencia técnica, la línea del whale de 45 días), el stock que no se puede echar a perder y "no hace falta una gota de talento manual", que cubre la objeción "I'm not crafty" que figuraba sin explorar.
- `WIKI/scented-stones.md` y `WIKI/index.md` al día con la tanda y el banco restante.

## 2026-10-31 — Piedras: guiones v34 "más potentes" (13 a 15)
- Tres guiones nuevos de Scented Stones en inglés y español con voseo: `OUTPUTS/2026-10-31-guiones-piedras-v34-mas-potentes.md`, 50 a 55 s.
- Ángulos sacados del banco: mi mejor cliente nunca revendió ni una (inmobiliarias, clínicas y hoteles que compran para regalar), no hay nada en este negocio que se gaste (el molde como activo) y te vas a quedar sin capacidad antes de quedarte sin clientes.
- Se mantiene la regla del 30/10: primera línea que afirma algo imposible, mecanismo del producto como prueba, un solo número de plata como precio de mercado y cierre con una acción concreta de esta semana.
- `WIKI/scented-stones.md` y `WIKI/index.md` al día con la tanda y el banco restante.

## 2026-10-30 — Perles Merveilles 3D: tanda 1 producida (6 videos)
- Oferta nueva en inglés (83 figuras en mostacillas 3D, US$ 24,65). Guiones V1-V6 del 30/10 llevados a video: `PM-V1-start-with-the-snail.mp4` a `PM-V6-the-nativity-that-comes-back.mp4` en `~/Desktop/perles-merveilles-3d/anuncios/`, de 33 a 42 s, 9:16.
- Voz **Sulafat** (AI Studio, Gemini 3.1 Flash TTS Preview, Pace Natural), los 6 MD5 distintos; `speed 1.30`, `silence [0.26, 0.12]`.
- Visual **100% clips de TikTok**: 28 bajados, 24 en el pool después de descartar 4 (subtítulos quemados, cajas de comentarios y marca de agua ajena).
- Editor nuevo `OUTPUTS/scripts-vsl/edit_perles.py` (paleta rojo/dorado/verde pino, placa final PERLES MERVEILLES 3D) y planes en `anuncios/work/plans/gen.py`.
- Página nueva `WIKI/perles-merveilles-3d.md` con la oferta, la DNA del original francés y **dos trampas nuevas**: el pool se come la tanda si no se topea por clip (ahora hay tope de 8 recortes y familias visuales) y la marca de agua que no se ve en la hoja de contactos chica.
- También: los intermedios del editor ya no se escriben en el Escritorio (iCloud le cortaba la lectura a ffmpeg con "Operation timed out"); van al scratchpad con `VSL_TMP`.

## 2026-10-30 — Herrero de Finde: variables V52-V54 (segunda vuelta)
- Tres variables más sobre los mismos tres cuerpos ganadores, con el segundo hook de cada uno: `OUTPUTS/2026-10-30-renovaciones-herrero-v52-v54.md`.
- Producidos `HF-V52-cada-auto-en-la-calle.mp4`, `HF-V53-esa-cocina-no-discute.mp4` y `HF-V54-ese-te-aviso.mp4` con `gen11.py` y voz Enzo a 1,30.
- Regla nueva en `WIKI/herrero-de-finde.md`: si el hook nombra el trabajo, el ancla del TAG va con `occ=1` o la placa pisa la apertura.

## 2026-10-30 — Herrero de Finde: testeo del 30/10 y variables V49-V51
- Lectura de la captura de Meta: de la tanda V43-V48 vendieron tres conjuntos el primer día — **CJTO 5 (V47 isla, 2 compras a 4,00)**, CJTO 6 (V48 cochera, 1 a 5,53) y CJTO 4 (V46 escalera, 1 a 6,85). Los tres que no vendieron abren con promesa de ingreso o con la objeción del principiante.
- `OUTPUTS/2026-10-30-renovaciones-herrero-v49-v51.md`: tres variables con el **cuerpo textual** de los tres que vendieron y **hook nuevo** (pedido de Santiago), más banco de hooks. Edición v4, la misma de la tanda que corrió.
- Producidos `HF-V49-la-maquina-mas-cara.mp4`, `HF-V50-200-mil-en-900-mil.mp4` y `HF-V51-no-te-pagan-por-soldar.mp4` en `~/Desktop/herrero-de-finde/anuncios/`, con `anuncios/work/plans/gen10.py` y voz Enzo a 1,30.
- Reglas nuevas: en `WIKI/renovacion-de-creativos.md`, **dónde termina el hook y empieza el cuerpo validado** (la frase que explica el hook se va con el hook; la bisagra se mira siempre); en `WIKI/vsl-reglas-de-armado.md`, **Gemini 3.8 Flash TTS da una sola generación por carga de página** (Run queda `aria-disabled`, hay que recargar y rehacer voz + Style).

## 2026-10-30 — Atlas de Cortes: natives 8, 9 y 10 (variables de las ganadoras leídas de la cuenta)
- Se identificó por MCP la cuenta de escalado de la oferta de pelo (`1791862825108056`, "Cuenta en Ingles 2", portfolio Reset FIT) y las tres natives que hoy puso en POCKET: **NATIVE 3 = nuestra native 1** (Rhonda, las once hojas), **NATIVE 8 = nuestra native 5** (Darlene, el maniquí) y **NATIVE 1 = una native corta de ~700 palabras que no es nuestra** (escena en el sillón, con precio y bonus).
- `OUTPUTS/2026-10-30-natives-atlas-cortes-8-9-10.md` + `~/Desktop/atlas-cortes/anuncios/natives/2026-10-30-natives-tanda-4.md`: una variable de cada una (las 640 fotos de nucas; el difusor todavía en la bolsa; la corta del hush cut un martes a las 9:40).
- Reglas nuevas en `WIKI/natives-ganadoras.md` y `WIKI/atlas-de-cortes.md`: en la oferta de pelo la native **corta** también vende (la tanda puede mezclar 2 largas + 1 corta) y el MCP sí lee la cuenta de escalado (lo del 23/10 valía para la de testeo, que sigue sin identificar).

## 2026-10-30 — Atlas de Cortes: producidos AT-V37, V38 y V39
- Tres videos 9:16 con voz Sulafat y B-roll de TikTok: 34,0 s / 32,6 s / 28,4 s, en `~/Desktop/atlas-cortes/anuncios/`.
- Dos trampas nuevas anotadas en `WIKI/atlas-de-cortes.md`: el anchor de la placa final con una palabra repetida **corta el video a la mitad sin avisar** (le pasó al V38 con "is"), y el techo real de un chip es ~28 caracteres (dos se salieron del borde y hubo que rehacer V38 y V39).
- AI Studio volvió a bajar el audio anterior en el tercero; se detectó por MD5 y se regeneró.
- Hojas de contactos revisadas a 1 cuadro cada 2 s: limpias.

## 2026-10-30 — Atlas de Cortes: v37–v39, hooks reescritos
- Rechazo de la v34–v36 por hooks débiles. Aperturas nuevas que chocan: "sos la cosa más cara de tu salón y hacés el trabajo más barato", "el corte que te pidió tiene nombre, lista de espera y precio, vos la mandaste con capas largas" y "nadie subió nunca la foto de un despunte".
- Regla nueva en `WIKI/guiones-y-anuncios.md`: hook débil = primera línea que describe; la buena afirma algo casi imposible y se explica en la línea siguiente. Es la misma corrección que la de piedras de hoy, ahora generalizada.
- `OUTPUTS/2026-10-30-guiones-atlas-cortes-v37-v39.md`, copia en la carpeta de la oferta, portapapeles en RTF.

## 2026-10-30 — Atlas de Cortes: v34–v36, bizop a la estilista
- Santiago corrigió la v31–v33: *"anda más por el bizop, dejá de hablar de enseñarle a tus empleadas, o cosas así"*. Se caen el V31 (la aprendiza) y el V32 (los tres sillones del salón); el V33 queda en pie.
- Tres guiones nuevos, todos a ella y a su plata: la ventana de seis semanas de diciembre, el sillón lleno con la plata planchada (problema de carta) y el corte de transformación como la única publicidad gratis.
- Regla nueva en `WIKI/guiones-y-anuncios.md`: el bizop le habla al que compra, nunca a su jefe ni al negocio visto desde arriba.
- `OUTPUTS/2026-10-30-guiones-atlas-cortes-v34-v36.md`, copia en la carpeta de la oferta, portapapeles en RTF.

## 2026-10-30 — Atlas de Cortes: testeo del 30/10 y variables v31–v33
- Captura de Santiago con 5 conjuntos en aprendizaje. **Las natives rinden el doble que los videos**: NATIVE 11 a $6,97 con ROAS 16,14 (una compra de $112,50, con bump u OTO) y NATIVE 10 a $7,37, contra $14,04 de "Are you" y $14,83 de "One copy".
- Reconocidos: "One copy" = V27 de la tanda bizop del 29/10 · "Are you" = el hook de la landing "How many cuts are you turning down…". **Natives 9, 10 y 11 no están mapeadas** (las nuestras van de la 1 a la 7): se le pidió el dato.
- Tres variables nuevas en bizop duro: la aprendiza como capacidad barata, el sillón que le toca a la clienta y el corte rechazado que se lleva color, brushing y rebook.
- `OUTPUTS/2026-10-30-guiones-atlas-cortes-v31-v33.md`, copia en `~/Desktop/atlas-cortes/anuncios/guiones/`, portapapeles en RTF. `WIKI/atlas-de-cortes.md` actualizada con la tabla del testeo.

## 2026-10-30 — Piedras: natives 37 y 38
- Escritas las dos opciones que habían quedado marcadas como las más llamativas de un vistazo en la lista del 29/10: el teléfono con nueve pedidos sin contestar (la demanda la desborda) y el cartel de feria dado vuelta con "SOLD OUT - TAKING ORDERS" a las 11:40.
- Brechas casero/vendible **nuevas**, sin repetir las natives 27 a 36: el peso de la piedra y el alcance del aroma (37), que las doce piezas salgan hermanas y el amarilleo de ciertas fragancias (38).
- Errores de negocio: producir de a un pedido por vez en vez de juntar la bandeja y dar fecha (37), y llevar todo suelto sin una sola caja de regalo (38).
- Sin montos de ingreso, sin precio, sin URL en el cuerpo, sin caras, solo en inglés. `OUTPUTS/2026-10-30-natives-piedras-37-y-38.md`, copiadas al portapapeles en RTF. `WIKI/natives-ganadoras.md` actualizada.

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
