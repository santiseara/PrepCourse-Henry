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
- **Insertos por código** (`gfx_boxes.py`): la librería de moldes con los dielines dibujados en SVG, el celular con el índice, la página del armado y el calendario de la demanda. Cuestan cero y no hace falta que el producto exista.
- **Entregables con nombre propio** en los guiones (regla del mercado inglés): *300+ box templates*, *step by step assembly video*, *the First Sale Kit*, *100 ready messages*, *30 day posting planner*. Son los bonos del original traducidos, así que coinciden cuando se clone la landing.

## Preguntas abiertas
- **Falta la landing.** Sin ella los insertos van con nombre de trabajo y vocabulario propio (regla del 5/11 de [[arreglos-de-ropa]]: el inserto se dibuja con la landing en la mano).
- ¿Se clonan también las otras dos líneas del ganador (**cajas para taza** y **caja explosión**) como ofertas aparte, o entran como temas adentro de ésta?
- ¿El plan de dos precios (básico sin bonos / completo con los 10) se copia tal cual?

## Relacionado
[[guiones-y-anuncios]] · [[caza-de-ofertas]] · [[100-paper-squishies]] · [[calendarios-2027]] · [[internacionalizacion]] · [[como-trabajar-con-santiago]]

## Fuentes
- Biblioteca de Anuncios, page id 1288335281030909 (51 ads activos, leídos el 2026-11-10)
- `moldescaixacenario.vercel.app`, `caixinhacaneca.vercel.app`, `moldecaixaexplosao.vercel.app`
- OUTPUTS/2026-11-10-guiones-party-box-vault-tanda1.md
