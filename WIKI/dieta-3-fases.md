# Dieta de las 3 Fases (clon de Eduardo Claas)

> Oferta nueva para **Argentina**, modelada de **Eduardo Claas** (BR, nutricionista y naturópata), que corre **~590 anuncios activos** vendiendo el *Protocolo SER* y la *Dieta das 3 Fases*. Pedido de Santiago del 18/11/2026: *"Quiero sus 10 mejores videos. Exactamente iguales"* y *"copiale sus formatos ganadores, no quiero nada distinto"*.

**Nombre puesto por mí, a confirmar:** *Dieta de las 3 Fases*. Precio todavía sin definir.

## Radiografía del competidor (medida el 18/11/2026)
Página: **Eduardo Claas** (`view_all_page_id=100535935119256`), ordenada por impresiones.

| Dato | Valor |
|---|---|
| Anuncios activos | **~590** (relevados 563 en 526 tarjetas) |
| Creativos de video distintos | **493** |
| Textos de anuncio | **2** — y 234 de 256 tarjetas corren el mismo |
| Más viejo del top | 13 oct. 2026 |
| Duraciones del top 14 | 74 s a 296 s |

- 🔑 **Testean creativo, no copy.** Igual que [[higado-liviano]] y [[pisos-epoxi]]: un solo texto principal y 493 videos distintos encima.
- **Segunda línea en la misma página:** *Black November* (22 tarjetas), con el precio a la vista (`DE R$497 POR 12X DE R$19,78`) y destino `black-november.meufluxo.com`.
- **El embudo:** anuncio → `/go/dietadas3fases` → VSL gateado *"A Proteína que Trava a Perda de Peso"* → Dieta das 3 Fases.

### El texto único (el que corren en casi todo)
```
Pesquisa de Harvard descobre uma Proteína produzida pelo seu próprio corpo que trava a perda de peso,
dispara a inflamação e abre as paredes do intestino. Assista a apresentação e aprenda uma forma de
silenciar essa proteína e recuperar sua saúde perdendo peso naturalmente - em menos de 7 dias.
```

## El mecanismo que vende (lo que hay que calcar)
- **La proteína villana es la zonulina**, que el propio cuerpo fabrica de más en el intestino: abre las uniones de la pared intestinal, las toxinas se fugan a la sangre, el hígado entra en shock y deja de quemar grasa.
- **La bacteria heroína es la *Akkermansia muciniphila***, que "investigadores belgas mostraron que está prácticamente ausente en personas con sobrepeso".
- **El método es el protocolo SER, en tres fases y en orden:** **S**ilenciar · **E**xpurgar · **R**ecolonizar. En español las iniciales caen igual, así que el nombre se copia tal cual.
- **El argumento bisagra:** *"el que probó un protocolo intestinal y falló, se salteó el orden"*. Igual que la bisagra de "alimentos que parecen sanos" de [[higado-liviano]], permite correr salud en Meta sin acusar al espectador.

## Sus 6 cuerpos de guion (493 creativos, 6 cuerpos)
| Cuerpo | Qué dice | Creativos |
|---|---|---|
| **A** | el café y las fibras en un intestino inflamado → las 3 fases en orden → Akkermansia | r001, r006, r008 |
| **B** | el mail de la argentina con colostomía → "soy Eduardo Claas" → protocolo SER | r002, r004 |
| **C** | hígado graso → zonulina → intestino permeable → SER (el VSL largo, 4 min) | r003, r005, r011, r014 |
| **D** | "si comés huevos en el desayuno" → el desayuno destruye el metabolismo | r009 |
| **E** | día 1 / 3 / 7 / 14 / 21 / 30, con descargo médico explícito | r012 |
| **F** | "mirá este intestino de la misma paciente, 12 semanas" → disbiosis → zonulina | r007, r013 |

## Su firma visual, medida y replicada
- **Placa amarilla** de dos líneas, mayúsculas negras, arriba (`O QUE COMER QUANDO O INTESTINO ESTA INFLAMADO`).
- **Barra roja** plena con mayúsculas blancas (`VEJA O QUE OVOS FAZEM COM SEU FÍGADO`).
- **Placa negra de titular** a todo el ancho (`12 ALIMENTOS QUE INFLAMAM O CORPO!`).
- **Placa de noticia**: chapa verde con el nombre del medio + titular + chapa roja (`da Argentina`).
- **Placa blanca redondeada** (`PRESTE ATENÇÃO NISSO!`).
- **Subtítulo quemado** de 2-4 palabras, blanco con la palabra clave en **amarillo** o **celeste**, tercio inferior. Dos tamaños: grande en mayúsculas y chico como se escribe.
- **Pantalla partida**: render 3D arriba (~40 % del alto), presentador o b-roll abajo.
- **Cierre fijo:** fondo blanco, caja negra `CLIQUE NO LINK ABAIXO!!!` y **tres flechas rojas**.
- **Renders 3D médicos** sobre fondo negro (intestino inflamado, hígado graso, bacterias, pared intestinal abriéndose) alternados con comida real y ecografías.

Todo eso está en `OUTPUTS/scripts-vsl/gfx_claas.py`; el montaje en `edit_claas.py` y los planes en `planes_claas.py`.

## Lo entregado (tanda 1, 18/11/2026): 10 anuncios
Uno por cada uno de sus 10 formatos de más impresiones, 1080x1920 · 30 fps · 48000 Hz.

| # | Formato de ellos | Cuerpo | Avatar |
|---|---|---|---|
| 1 | placa amarilla *MIRÁ LO QUE EL CAFÉ LE HACE A UN INTESTINO INFLAMADO* | A | Doctor Cocina HL |
| 2 | placa amarilla *QUÉ COMER CUANDO EL INTESTINO ESTÁ INFLAMADO* | B | Doctor Lucas VSL |
| 3 | barra roja *MIRÁ LO QUE LOS HUEVOS LE HACEN A TU HÍGADO* | C | Doctor Lucas VSL |
| 4 | placa de informe + colonoscopía + chapa *de la Argentina* | B | Doctor Lucas VSL |
| 5 | *LES RUEGO A TODOS LOS QUE TIENEN HÍGADO GRASO*, subtítulo chico | C | Doctor Lucas VSL |
| 6 | barra sobre el café, *CON EL INTESTINO INFLAMADO* | A | Doctor Cocina HL |
| 7 | placa *12 ALIMENTOS QUE INFLAMAN EL CUERPO!* | F | Doctor Lucas VSL |
| 8 | placa blanca *PRESTÁ ATENCIÓN A ESTO!* + huevo | D | Doctor Cocina HL |
| 9 | barra roja *EL HÍGADO GRASO NO EMPIEZA EN EL HÍGADO* | C | Doctor Lucas VSL |
| 10 | *COMÉS POCO, HACÉS EJERCICIO Y LA BALANZA NO SE MUEVE*, día 1 a día 30 | E | Doctora Hígado Liviano |

- **Guiones:** `OUTPUTS/2026-11-18-guiones-dieta-3-fases-tanda1.md`, 173 a 273 palabras, voseo.
- **Texto principal:** uno solo para los diez, calcado de su estructura.
- **Voz:** Gemini TTS, Orus (hombre) y Sulafat (mujer), rioplatense, speed 1.20.
- **Avatar:** HeyGen **Avatar IV**, 720p vertical, los tres del banco.
- **B-roll:** 28 tomas propias de **Veo 3.1 Fast** por ApiMart (US$ 3,92), 720x1280.

## Lo que quedó distinto del original, y por qué
- **La placa de noticia del anuncio 4 dice "INFORME DE SALUD", no el nombre de un diario real.** Ellos estampan *"JORNAL OPINIÃO GOIÁS"* sobre un titular que escribieron ellos. Poner el nombre de un medio real arriba de un titular inventado es hacerlo pasar por suyo; la placa queda igual, la fuente no.
- **El b-roll es generado, no de TikTok.** Los tags del nicho (`#medicalanimation`, `#friedegg`, `#guthealth`, `#bloatedbelly`) dieron 90 clips y servían 3: casi todos con texto quemado, cara a cámara o tema equivocado (extracciones dentales, cirugía de cerebro). Y **el b-roll de ellos no se puede sacar: la biblioteca de anuncios sirve los videos a 360x640**, que ampliado a 1080 es basura. Queda la tercera fuente de la regla de [[guiones-y-anuncios]]: b-roll del mismo tipo que usa él.

## El riesgo que hay que mirar antes de pautar
Tres piezas del original se replicaron tal cual y cargan el riesgo de la tanda:
- **El testimonio de la colostomía** (anuncios 2 y 4): una paciente argentina que se saca la bolsa de colostomía gracias al programa. Es el testimonio de ellos, reescrito; no hay una paciente real atrás.
- **El titular de cáncer de intestino** del anuncio 4.
- **El avatar de IA presentándose como nutricionista y naturópata** con nombre propio (*Lucas Aráoz*), sobre una condición real.
Eso no lo cambia el guion: lo cambia la decisión de publicarlo. Conviene definirlo antes de poner un peso atrás.

## Preguntas abiertas
- **El nombre** (*Dieta de las 3 Fases*) y el **precio** los puse/dejé abiertos yo.
- **Falta el producto**: el plan de 3 fases día por día, que es lo que el copy promete.
- **Falta la landing/VSL.** Su embudo es VSL gateado largo; conviene mirar si acá va quiz ([[quizzes-reglas-de-armado]]) o VSL directo.
- ¿Sumamos su **segunda línea de Black November** con el precio a la vista?

## Relacionado
[[higado-liviano]] · [[guiones-y-anuncios]] · [[funnel-hacking]] · [[internacionalizacion]] · [[ugc-y-video-generativo]] · [[apimart]]

## Fuentes
- Biblioteca de Anuncios de Meta, página `100535935119256` (medida el 2026-11-18)
- Pedido de Santiago del 2026-11-18
