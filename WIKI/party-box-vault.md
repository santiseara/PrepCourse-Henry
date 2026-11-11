# The Party Box Vault

> Oferta nueva para **mercado inglés** (US, CA, AU, UK, NZ): **+300 moldes imprimibles de cajitas de souvenir**, editables en Canva. Clon de **Moldes Prontos / caixinha cenário**, la ballena brasileña que corre 51 ads activos desde el 1 de septiembre de 2026. Tanda 1 de 6 videos del 10/11, en inglés y español con voseo. (fuente: Biblioteca de Anuncios, page id 1288335281030909)

## Ideas clave
- **El producto:** más de 300 moldes de cajitas de souvenir (*party favor boxes*) listos para imprimir, ordenados por tema, con las medidas ya hechas. Se imprimen en una impresora común, se cortan con tijera y se arman en diez minutos. **No hace falta máquina de corte.**
- **El avatar:** mujer que quiere ingresos desde la casa y ya tiene impresora, papel y tijera. El vehículo es la papelería personalizada; el motor es el ingreso extra.
- **El precio del original:** R$10 el plan básico (sin bonos) y un plan completo con 10 bonos. En nuestros ads **no va el precio** (regla de [[guiones-y-anuncios]]): va *dirt cheap*.
- **Por qué el nicho aguanta:** la demanda la fabrica el calendario. Todos los meses hay cumpleaños, baby showers, bautismos, egresados, Halloween y Navidad, y todos terminan con alguien repartiendo una cajita en la puerta.

## La radiografía del ganador
- **51 ads activos**, 8 copies distintos. El que más corre (**21 ads, desde el 5 de septiembre**) es el de *caixinha cenário*; el segundo (**9 ads, desde el 1 de septiembre**) es el de **cajas para taza**. Hay una tercera línea, **caja explosión** (60 moldes).
- Tres dominios distintos con la misma oferta: `moldescaixacenario.vercel.app`, `caixinhacaneca.vercel.app`, `moldecaixaexplosao.vercel.app`. **Landing en Vercel, no en una plataforma de checkout.**
- **La landing:** hero con el contador, grilla de modelos, los dos ítems del producto (los +300 moldes y la videoclase de armado), 5 razones, la lista de "ideal para vos que…" (necesitás plata rápido, no sabés por dónde empezar, querés ingresos sin salir de casa), **10 bonos** con precio tachado y dos planes (básico R$10 / completo con todo).
- Los 10 bonos del original: Polaroids de amor, porta taza corazón, cuadro de recuerdos, caja cara mitad, **Kit Primera Venta**, 100 formas de postear + planner de 30 días, **100 mensajes listos para vender**, +400 figuritas, topos de torta, moldes de rompecabezas.

### Las 6 familias ganadoras (una por video de la tanda 1)
| # | Familia | Frase eje del original |
|---|---|---|
| 1 | **La impresora parada** | *"Dueña de gráfica, estás dejando de ganar plata solo por no tener estos moldes"* |
| 2 | **Me salvó el atelier** | *"Las cajas cenário fueron lo que salvó mi atelier"* |
| 3 | **Producto con salida todo el año** | *"Hay producto que todos los meses tiene salida"* |
| 4 | **La caja vale más que el regalo** | *"Antes de ver la taza, ella va a ver la caja"* |
| 5 | **Te quedaste atrás** | *"¿Sentís que estás atrasada en la papelería? Seguís guardando referencias"* |
| 6 | **Querer dominar Canva primero** | *"Hay mujeres tratando de dominar Canva antes de vender la primera pieza"* |

### La edición del ganador (hoja de contactos de 10 de sus videos)
- **Subtítulos de UNA palabra**, texto negro dentro de una **caja amarilla**, abajo al centro. Sin caja de hook, sin placa de apertura.
- B-roll de **manos armando y llenando cajitas**: el producto en pantalla todo el tiempo.
- **Insertos del producto**: la carpeta de PDFs con los moldes y la vista de Canva, con un chip grande encima (*"+100 MOLDES"*).
- Voz en off **de mujer**, 28 a 51 segundos, cierre con *"Clicá en Saber más"*.

## Lo que hicimos nosotros
- **Nombre de trabajo: The Party Box Vault.** Los 6 guiones no lo nombran (regla de no nombrar al experto), así que si la landing sale con otro nombre **solo hay que rehacer los insertos**, no los guiones ni las voces.
- **Voz:** Sulafat (mujer), inglés americano, `speed 1.30`. `gemini-2.5-flash-preview-tts` dio 429 a la segunda request, así que la tanda salió con **`gemini-3.1-flash-tts-preview`**, verificada con Whisper (no lee el Style en voz alta).
- **B-roll:** 84 clips bajados de `#partyfavorbox`, `#explosionbox`, `#treatboxes` y `#papercraftbusiness`; 43 revisados, **28 limpios**. Es el mejor rinde de tag que tuvimos: el nicho filma el proceso sin hablar. El filtro final no fue la hoja de contactos sino el **OCR de Vision sobre cada ventana** (`scan_carteles.py`), que cazó cinco leyendas blancas sobre fondo claro y una marca de agua que la miniatura escondía.
- **Listado de las visuales** con cuenta, link de TikTok y tramo usado de cada clip: `OUTPUTS/2026-11-10-visuales-tiktok-party-box-vault.md` y `~/Desktop/party-box-vault/anuncios/visuales-tiktok.md`.
- **Insertos por código** (`gfx_boxes.py`): la librería de moldes con los dielines dibujados en SVG, el celular con el índice, la página del armado y el calendario de la demanda. Cuestan cero y no hace falta que el producto exista.
- **Entregables con nombre propio** en los guiones (regla del mercado inglés): *300+ box templates*, *step by step assembly video*, *the First Sale Kit*, *100 ready messages*, *30 day posting planner*. Son los bonos del original traducidos, así que coinciden cuando se clone la landing.

## Tanda 2 — tres renovaciones leyendo la cuenta (2026-11-11)
Santiago pasó la captura de los 6 conjuntos: **$63,22 de gasto, 3 compras**.

| Conjunto | Guion | Compras | CPA | Gastado |
|---|---|---|---|---|
| 3 | el calendario / la demanda | **2** | **$7,12** | $14,24 |
| 5 | la carpeta de guardados vs. la mesa vacía | 1 | $14,10 | $14,10 |
| 6 | la mitad difícil ya viene hecha | 0 | — | $7,65 |
| 2 | storytime de los doce souvenirs | 0 | — | $8,58 |
| 1 | ya tenés la fábrica / la impresora | 0 | — | $8,21 |
| 4 | nadie fotografía el regalo | 0 | — | $10,44 |

**Lo que dice la lectura:** vendió **la demanda** (hay fiesta todos los meses y esa parte no la hace nadie) y, en segundo lugar, la **comparación social con catálogo**. Murieron los dos ángulos de **mecanismo** (la impresora, "no hace falta diseñar") y los dos **emocionales** (la caja contra el regalo, el storytime). **Frecuencia 1,39**: no hay fatiga de público, así que se renueva el hook.

⚠️ Con $63 de gasto y 3 ventas la lectura es fina; la dirección es clara pero no es un veredicto.

**Las tres (`11-11 - 1` a `11-11 - 3`, de 30 a 31 s), cuerpo del CJTO 3 copiado textual:**
| # | Formato del hook | Hook |
|---|---|---|
| 1 | El trabajo que nadie tomó | *"At every party in your town, three people got paid and one job stayed empty"* |
| 2 | La escena de la puerta | *"Stand by the door when a kid's party ends and watch what the mother hands out"* |
| 3 | El cliente que vuelve | *"The same mother is going to buy from you four times this year and she does not know it yet"* |

- **La estética también cambia:** la caja del subtítulo deja de ser amarilla en los tres y pasa a **un color por creativo** (coral, verde, violeta), corte de 1,6-2,6 s y planos nuevos con **offset de +1,4 s** y TOPE 10 sobre las mismas ventanas ya revisadas, con `usage.json` penalizando lo usado.
- 🐞 **El `first` fijo rompió los tres renders.** Con el offset nuevo el primer tramo de cada clip ya no arranca en el borde de la ventana, así que `first=['i', 0.0]` no existía en el pool y el editor murió con `StopIteration`. Ahora el generador resuelve el `first` contra el pool (`_first()`), que es a prueba de cambios de offset.
- Guiones en `OUTPUTS/2026-11-11-renovaciones-party-box-vault.md`. Planes: `OUTPUTS/scripts-vsl/gen_boxes_plans_11.py`.
- **Lo que sigue:** el cuerpo del CJTO 5 es el segundo validado. Si estas tres rinden, la próxima tanda renueva ese.

## Pospagos - 3 escaleras propuestas (2026-11-11)
Propuesta completa en `OUTPUTS/2026-11-11-pospagos-party-box-vault.md`, **pendiente del OK de Santiago** (seccion 0.3 del Manual del Embudo Post-Compra). Armada con [[aumento-de-aov]] y [[embudo-vsl-post-pago]].

- **Los ejes que el front ya se come** (y que ningun OTO puede pisar): mas moldes y temas, el video de armado, el First Sale Kit, los 100 ready messages y el 30 day posting planner. Los 10 bonos del original son casi todos de "vender", asi que **cada bono clonado mata un eje de backend**: la recomendacion es no sumar mas bonos de venta al front.
- **Los 7 huecos** que quedan: cuanto cobrar, nadie le contesta a ella, el cliente que vuelve 4 veces al ano, cuando pre-vender cada tema, los 12 pedidos juntos, vender el archivo en vez de la cajita, y las otras dos categorias del ganador (explosion y taza).
- **Las tres escaleras** comparten la matematica (97 / 37 / 27 / 20 con downsells al 50/53/47/55 %) y cambian quien va primero a 97: **A** el asistente 1 a 1 (patron de [[scented-stones]], la validada), **B** los derechos de reventa (mas valor percibido, pero el front ya dice "imprimi y vende"), **C** el sistema de proveedora mayorista (el unico angulo que ya vendio con plata: la demanda / el cliente que vuelve).
- **AOV:** 51 USD con las tasas del manual (ratio 1,90) y 39 USD en el escenario conservador (ratio 1,45, el numero real de su tienda de 27).
- Todos los entregables son **PDF, HTML offline y un Gem compartido**: cero video, cero creditos.
- **Títulos y descripciones de los 8**, listos para la pantalla de upsells: `OUTPUTS/2026-11-11-otos-titulos-descripciones-party-box-vault.md`, en inglés (el que se pega) y en español con voseo. Molde de 3 renglones de [[aumento-de-aov]]. **El Repeat Order System ($37) y el Party Supplier System ($97) son el mismo eje en dos tamaños: nunca van juntos en la misma escalera.**
- ⚠️ **Orden sensato: landing primero.** Sin la landing las 8 paginas de OTO/DS no tienen identidad visual (regla de marca del manual) y el front sigue prometiendo un *step by step assembly video* que no esta producido.

## La landing real: Party Box Profits (leida el 2026-11-11)
`https://party-box-profits.impultienda.ar` · **front 19,99 USD**, ancla 97, pago unico, acceso de por vida, garantia de 30 dias, 4,9 estrellas de 6.195 vendedoras. Headline: *"Print a $3 party box tonight. Sell it for $35 this weekend."* **Sin order bumps en el checkout** (hueco abierto).

**El stack:** 300+ moldes en **8 colecciones** con cartelitos de nombre personalizados y updates gratis · los add-ons que ya vienen incluidos (**cake toppers, cuadros de recuerdo, polaroids y cajas rompecabezas**) · **step by step assembly video** · acceso de por vida en cualquier dispositivo.

**Los 4 bonos (con su valor cantado):** The First Sale Playbook ($47: a quien mensajear, que cobrar y como tomar el pedido) · 100 Copy-and-Send Sales Messages ($39) · 30-Day Content Planner ($35) · **The Pricing & Profit Calculator ($29)**.

⚠️ **Los valores de los bonos suman $150 y la pagina canta $97 de valor total del combo.** Conviene alinearlo antes de escalar.

### ⛔ 2026-11-11 · No se proponen pospagos sin leer la landing
Santiago, sobre la v1: *"No me gustaron, el unico que va es el asistente, pero los demas, el 37 y el de 27 ya estan en los bonos, analiza la landing y haceme pospagos potentes que se vean irresistibles"*.
- Yo habia mapeado los ejes del front **desde los entregables que nombran los guiones** porque la wiki decia "falta la landing". La landing ya existia, y adentro estaban **la calculadora de precios** (mi OTO3 de $27) y buena parte de **el cliente que vuelve** (mi OTO2 de $37, que choca con el First Sale Playbook).
- **Regla:** antes de proponer backend se abre la landing y se transcribe el stack completo con cada bono y su valor. Es la misma familia que la regla de [[monjaro-violeta]]: *lo que tiene una oferta no se deduce*. Deducir los ejes desde los ads alcanza para escribir ads, no para armar pospagos.
- **Y los OTOs tienen que verse irresistibles**, no solo no pisar un eje: cada uno arranca con la escena del problema que ella va a tener **esta noche**, no con la categoria del producto.

### Pospagos v2 (la que va)
`OUTPUTS/2026-11-11-pospagos-party-box-profits-v2.md`, en ingles (el que se pega) y espanol con voseo. Escalera **97 / 47 / 37 / 27** con downsells al 50/53/47/55 %.

| | Producto | USD | El hueco que la landing abre y no cierra |
|---|---|---|---|
| OTO1 | **Personalized 1-on-1 Assistant** 🤖✨ | 97 | nadie le contesta a ella (el unico aprobado de la v1) |
| OTO2 | **The Any-Theme Studio™** 🎨♾️ | 47 | el tema que la clienta pide y no esta en las 8 colecciones |
| OTO3 | **The One-Link Order Shop™** 🛍️📲 | 37 | contestar "cuanto sale" cuarenta veces; la vidriera que no tiene |
| OTO4 | **The Phone Photo Studio™** 📸✨ | 27 | la foto arriba de la mesa de la cocina es lo unico que la clienta ve |

- **Backend $27,42 por comprador** con las tasas del manual → AOV **$47,41 (ratio 2,37)**; conservador (mitad de tasas) AOV **$33,70 (ratio 1,69)**. Con un front de $19,99 el backend no es un extra: es el negocio. El CPA tolerable pasa de 20 a 34-47 dolares.
- Todo sale en **PDF, HTML offline y un Gem**: cero video, cero creditos. Los dielines en blanco del OTO2 se dibujan con `gfx_boxes.py`, que ya existe.
- **Banco:** The Batch Production System™ ($20, OTO4 alternativo) y The Resale Rights Kit™ ($97, el unico que le pelea el puesto al asistente, pero necesita aclarar en 20 segundos la diferencia con el "imprimi y vende" del front).
- 🕳️ **El checkout no tiene order bumps.** Es la palanca mas barata que queda y no pisa ningun eje de los 4 OTOs.

## Preguntas abiertas
- ~~Falta la landing~~ **Resuelto el 11/11: `party-box-profits.impultienda.ar`.** La marca es **Party Box Profits**, asi que los insertos de los videos que dicen *The Party Box Vault* hay que rehacerlos con el nombre real (los guiones y las voces no se tocan).
- ¿Se clonan también las otras dos líneas del ganador (**cajas para taza** y **caja explosión**) como ofertas aparte, o entran como temas adentro de ésta?
- ¿El plan de dos precios (básico sin bonos / completo con los 10) se copia tal cual?
- ¿Se produce la escalera v2 completa o solo el asistente para empezar? ¿Y cuál de las tres escaleras de la v1 se descarta del todo?
- (v1, superada) ¿Cuál de las tres escaleras de pospago se produce? De eso depende si **caja explosión y caja para taza** entran como OTO3 (opción C) o salen como ofertas aparte.

## Relacionado
[[guiones-y-anuncios]] · [[caza-de-ofertas]] · [[100-paper-squishies]] · [[calendarios-2027]] · [[internacionalizacion]] · [[como-trabajar-con-santiago]]

## Fuentes
- Biblioteca de Anuncios, page id 1288335281030909 (51 ads activos, leídos el 2026-11-10)
- `moldescaixacenario.vercel.app`, `caixinhacaneca.vercel.app`, `moldecaixaexplosao.vercel.app`
- OUTPUTS/2026-11-10-guiones-party-box-vault-tanda1.md
