# Cámaras frigoríficas (Walk-In Coolers & Freezers)

> Oferta de arbitraje: manual visual de cámaras frigoríficas para técnicos de refrigeración. El ganador corre en **español** (Carlos Medina, `camaras-frigarificas.impultienda.ar`, 72 ads activos) y nosotros lo clonamos al **mercado inglés** con `visual-handbook-of-walk-in-coolers-freezers.impultienda.ar`. (fuente: Biblioteca de Anuncios + las dos landings, 2026-11-06)

## El competidor
- **Página:** Carlos Medina (`570406022821396`). **72 anuncios activos**, el más viejo en circulación desde el **5 de octubre de 2026** → 32 días vivo. Whale según los filtros de [[caza-de-ofertas]].
- **Tandas:** sube de a 6–13 creativos cada 4 o 5 días (5/10, 7/10, 9/10, 10/10, 15/10, 16/10, 23/10, 5/11). Los de octubre siguen activos: no renueva porque se le caen, renueva encima de los que funcionan.
- **Un solo primary text para los 72 anuncios.** Toda la variación está en el video. El copy abre con *"¿Te llaman para reparar una cámara frigorífica y no sabes por dónde empezar? 🥶"*, sigue con los negocios que dependen de la cámara, siete bullets con tilde (uno por módulo) y cierra con "60 páginas visuales".
- **Testea dos formatos en paralelo, no uno.** De los 8 creativos del 5/10 (hoja de contactos de los 8, 6/11): **3 son avatar de IA puro**, **1 es híbrido** (avatar recortado sobre b-roll que cambia) y **4 son b-roll puro** con subtítulo. Todos entre 18 y 60 segundos.
  - **Avatar:** técnico de remera negra con manómetros colgando, parado delante de la puerta de una cámara o de una sala de máquinas. **Fondo fijo, sin cortes, sin subtítulos, sin música, sin placas.** Rota tres caras (uno joven de pelo oscuro, uno canoso, uno de barba) y dos fondos.
  - **B-roll:** clips reales de obra (ampliación de una cámara, una cámara podrida con productos pegados al evaporador, manómetros y pinza amperométrica, recorrido del índice con split screen de dos clips) con **subtítulo palabra por palabra** y un estilo distinto por creativo: caja azul, blanco con la palabra en verde, blanco con borde más flechas rojas y zoom, caja negra. Uno lleva además un chip amarillo fijo arriba con `CÁMARAS FRIGORÍFICAS`.
  - **La regla que sí se cumple siempre: el avatar nunca lleva subtítulos y nunca tiene cortes; el b-roll siempre los lleva. No mezcla los dos sistemas dentro de un mismo creativo.**
- **CTA siempre igual:** "Toca en más información para acceder al manual completo".

## Los 6 ganadores modelados (transcriptos el 6/11)
| # | Ángulo | Dolor que activa | Frase central |
|---|---|---|---|
| 1 | **Demanda escondida** | Pasar por la puerta de todos esos negocios sin poder venderles | "Todos estos negocios tienen algo en común y casi nadie sabe repararlo" |
| 2 | **El trabajo mejor pagado** | Rechazar la cotización por no saber dimensionar | "Estás frente a uno de los trabajos mejor pagados de la refrigeración" |
| 3 | **El error que mata compresores** | Vergüenza profesional: lo cometen técnicos con años | "Dejar que entre refrigerante líquido al compresor" |
| 4 | **Dato contraintuitivo: la puerta** | El equipo trabaja el doble y nadie sabe por qué | "La mayor pérdida no está en el equipo, está en la puerta" |
| 5 | **Regla de oro del diagnóstico** | Cambiar piezas a ciegas delante del cliente | "No cambies componentes sin confirmar la causa" |
| 6 | **El llamado de emergencia** | El dueño pierde mercadería en horas y paga lo que sea | "Si se detiene, pierden mercadería en horas" |

Banco: el recorrido del índice ("60 páginas, cero relleno") y la obra real documentada (ampliación de cámara en un día).

## Dolores del avatar (los mismos en las dos landings)
Rechazar trabajos de cámara por no saber por dónde empezar · no poder calcular la carga térmica ni elegir el equipo · la cámara que no baja de temperatura, se llena de escarcha o el compresor que no para · cambiar repuestos a ciegas · saber que cuando una cámara se para el dueño paga lo que sea y ese técnico no sos vos.

## Nuestra landing (inglés)
- `visual-handbook-of-walk-in-coolers-freezers.impultienda.ar` — **$86.99 tachado → $19.99**, pago único, acceso de por vida, garantía de 30 días.
- **8 módulos, 46 temas, 60 páginas** + 3 bonos: Commissioning Checklist, Preventive Maintenance Plan, Quick Guide to Common Faults.
- Testimonios firmados en **US, Canadá, Reino Unido, Australia y Nueva Zelanda** → coincide con el set de países de [[internacionalizacion]].
- Vocabulario que hay que repetir en los ads: *heat load calculation · superheat and subcooling · won't pull down, ices up, compressor never cycles off · pull a vacuum and charge refrigerant · panel assembly · defrost control · butcher shops, produce stores, restaurants, supermarkets*.

## Decisiones de la tanda del 6/11
- **6 guiones** (oferta nueva = 6, [[guiones-y-anuncios]]), uno por ganador distinto, con estructura de 7 pasos de [[guiones-de-video-ads]] y cuerpo propio cada uno: ninguno repite la frase central de otro.
- **Inglés + español con voseo**, las dos versiones completas.
- **Sin precio en el ad** (el ganador tampoco lo dice). Se usa "less than one wasted service call".
- **Sin montos de ingreso ni plazos**, por la regla de [[profesional-digital]]: el oficio se vende como acceso a trabajos de mayor valor, no como plata prometida.
- **Voz: Orus** (hombre), la fija de [[como-trabajar-con-santiago]].
- Entregados en `OUTPUTS/2026-11-06-guiones-camaras-frigorificas-ingles.md` y en `~/Desktop/walk-in-coolers-freezers/anuncios/`.

## La tanda 1 de videos (6/11) — los 6 de voz en off
Santiago eligió **los 6 con voz en off + b-roll de TikTok** (la mitad b-roll del ganador), no avatar.

- **Voz Orus** por API (`tts_gemini.py`, `gemini-2.5-flash-preview-tts`) con un Style de técnico estadounidense de 40 y pico hablándole a otro técnico en la obra. Las 6 verificadas con Whisper contra el guion: sin errores de lectura. **V6 dio 429 en la primera vuelta y salió bien al reintentar con el mismo modelo**, así que antes de saltar al modelo de reemplazo conviene reintentar.
- **13 clips** de TikTok, bajados con tikwm de los tags del producto (`#walkincooler`, `#walkinfreezer`, `#coldroom`) y del oficio (`#refrigerationtech`): interior de cámara con mercadería, timelapses de armado de paneles, búsqueda de fugas, instalación de evaporador y condensadora, cold storage grande, rack de supermercado cargando 404A, deshielo con soplete, limpieza de condensador sucio, sala de máquinas.
- **Descartados por texto quemado:** el explicador CGI de TXV (subtitulado de punta a punta), el cold room chino con el precio en pantalla, `#atlascool` (marca de agua en todos los cuadros) y un clip de root cellar con subtítulos completos. De `#hvacrlife` no salió nada: es puro meme y cara a cámara.
- **Edición:** subtítulo de 3 palabras en itálica con la palabra activa adentro de una caja de color, **un color por creativo** (amarillo, verde, celeste, naranja, magenta, rojo), sin caja de hook y sin placa final, `speed 1.30`, `silence [0.26, 0.12]`, cortes de 1,9 a 2,9 s y la cama `bed_activo` a -8. Reusa `edit_arreglos.py` con `lang='en'`.
- **Inserts de producto** dibujados por código (`gfx_walkin.py`, con la landing real en la mano): tapa del manual, lámina interior del ciclo de refrigeración y tarjeta de oferta. **Sin precio.** La tapa se ancla donde el guion dice "handbook", la lámina donde nombra una página o un módulo, y la tarjeta cierra siempre.
- **Largo: 32,8 a 37,6 s**, justo en el rango del ganador (18 a 38 s).
- Entregados en `~/Desktop/walk-in-coolers-freezers/anuncios/` como `6-11 - 1` a `6-11 - 6`.
- ⚠️ **Registro del 6/11:** el clip de la fábrica china (`7657470569218166046`) abre con un cartel azul de especificaciones que **dura 0,5 s**: no apareció en la hoja de contactos de 1,5 s y se coló en el render del V2. Confirma la regla del 5/11 ([[guiones-y-anuncios]]): los bordes de la ventana se verifican con cuadros cada 0,5 s. Se arregló moviendo el arranque de la ventana a 1,0 s y re-renderizando la tanda entera.

## Preguntas abiertas
- Falta la **descripción para ads** (el ganador usa un solo primary text para sus 72 anuncios).
- Falta decidir países y presupuesto del testeo.

## Relacionado
[[guiones-y-anuncios]] · [[guiones-de-video-ads]] · [[caza-de-ofertas]] · [[internacionalizacion]] · [[profesional-digital]] · [[solar-installer-pro]]

## Fuentes
- Biblioteca de Anuncios de Meta, keyword `camaras-frigarificas.impultienda.ar` (6/11/2026)
- Transcripción de los 8 creativos más viejos con faster-whisper
- `camaras-frigarificas.impultienda.ar` y `visual-handbook-of-walk-in-coolers-freezers.impultienda.ar`
