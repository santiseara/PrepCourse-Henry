# Protocolo Limpia Dolor (AR)

> Oferta nueva para **Argentina, $17.990**: una **desparasitación articular casera de 9 días** con una bebida de
> jengibre + un ingrediente de supermercado, para gente de 50+ con dolores articulares crónicos. Es el clon del quiz
> de **`minhareceita.online`** (*Protocolo Limpa Dor*, BR), entregado el 18/11/2026.

## La oferta

| | |
|---|---|
| **Marca** | Protocolo Limpia Dolor · logo *Protocolo Desparasitación Articular* |
| **Mecanismo** | un **parásito inflamatorio** (se nombra *Ascaris lumbricoides*) se come los nutrientes que iban al músculo y al cartílago, inflama las articulaciones y presiona los nervios: el dolor no es desgaste, es el parásito |
| **Promesa** | sacarse todos los dolores en **9 días**, en casa, sin remedios y sin cirugía |
| **Avatar** | 50+ con artrosis, artritis, lumbalgia, dolor de rodilla, hombro o columna; ya probó analgésicos, kinesiología, pomadas e infiltraciones |
| **Precio** | **$17.990** pago único · tachado $186.930 (90 % OFF) · 3 cuotas de $5.997 |
| **Checkout** | `https://protocolo-desparacitacion-intestinal.impultienda.ar/checkout` — puesto y verificado el 18/11 (200, 0 redirecciones; los 6 CTAs probados) |
| **Fuente** | `https://minhareceita.online/` — funnel de **InLead** `136919`, *Dores Articulares - (PG WHITE)* |

## El quiz: 28 pantallas con rama por género

Portada → *Mujer u Hombre* → **26 pasos**, idénticos en los dos carriles salvo 4 imágenes, 1 reseña y los 3 videos.
El original los tiene **duplicados** (54 pasos: `Homem - Etapa 1..26` y `Mulher - Etapa 1..26`); nosotros los
resolvemos con **una sola lista y los assets intercambiados por `estado.genero`**, que da la misma experiencia y
la mitad de archivo.

El orden: síntomas → ¿ya te desparasitaste? → consultas médicas → hace cuánto → cuánto te afecta → condiciones →
**aviso del riesgo + nota** → gravedad → culpa → alimentos → síntomas → impacto → momento del día → impacto emocional →
**audio del Dr. Rodrigo + caso real** → interés → tratamientos probados → alternativas probadas → la salud →
qué harías si → compromiso + chats → la mejor parte → **audio 2 + caso real** → carga → **resultado** → **oferta**.

- **Resultado:** tabla *Remedios vs. Nuestro Protocolo* + **8 medidores** (5 rojos de riesgo, 3 verdes) + el agente
  parasitario + el aviso de que los parásitos salen muertos + la foto del licuado de jengibre.
- **Oferta:** placa de protocolo listo, antes/después con barras, audio 3, lista de síntomas, **value stack de 7 ítems**,
  precio, garantía de 180 días, video, caja de prueba, 3 reseñas, bonus, regalo y **6 CTAs**, todos al mismo checkout.

## Lo que se hizo propio

- **Los 3 audios de WhatsApp del "Doctor Rodrigo"**, reescritos en castellano rioplatense y regrabados con **Orus**
  (75 s, 46 s y 31 s, a `atempo=1.30`). La foto de perfil del doctor es la suya, que no tiene texto.
  ⚠️ El audio 3 del original dice que el protocolo llega **por WhatsApp**; acá dice **por correo**, que es como entrega
  ImpulTienda y respeta la regla de no pedir contacto dentro del quiz.
- **Los 6 videos de testimonio** generados con **Veo 3.1 Fast** por ApiMart (US$ 0,78 las 6 tomas de 8 s). Ver
  [[quizzes-reglas-de-armado]] (regla del 18/11) y [[apimart]].
- **La lámina de síntomas** (el viejo/la vieja con las burbujas naranjas): se le **borraron las burbujas por color
  exacto** y se rehicieron en HTML en castellano, sobre la misma figura.
- **El logo**, rehecho con el emblema suyo recortado y las tres palabras re-tipeadas en **Yellowtail**.
- **La tabla comparativa, la garantía, los dos chats de WhatsApp y la placa de "protocolo listo"**: eran capturas con
  texto en portugués, ahora son HTML nítido.
- **La "noticia del G1"** del original **no se clonó**: ver la regla del 18/11 en [[quizzes-reglas-de-armado]].
  En su lugar va una **tarjeta de divulgación sin marca**, con el pie *"No reemplaza la consulta con un profesional"*.
- **Nombres y ciudades argentinos** en las 5 reseñas (Rosario, La Plata, Córdoba, Mendoza, Tucumán) y en las
  notificaciones de prueba social.
- La garantía cita la **Ley 24.240** (10 días de arrepentimiento) y la extiende a 180 días, en vez del Código de
  Defensa del Consumidor brasileño.

## Lo que NO se copió de ellos

Su checkout de **Payt**, su analítica y su `__NEXT_DATA__` de InLead (es su plataforma).

## Entregables (18/11/2026, recortado el 19/11)

```
~/Desktop/limpia-dolor/
  landing/limpia-dolor-quiz.txt    473 KB · lo que va pegado en la tienda
  landing/limpia-dolor-PRUEBA.html el mismo, para abrir en Chrome
  landing/quiz.html                el fuente, con el bloque CONFIG arriba
  landing/media/                   3 mp3 + 6 mp4 (a2.mp3, v3 y v4 ya no se usan)
  imagenes/                        19 webp (los 19 ya subidos a Recursos)
```

### El recorte del 19/11: 28 pantallas → 25

Santiago pidió sacar tres pasos del tramo final, y el quiz quedó **de la última pregunta derecho a la carga y a la
oferta**:

| iba | se sacó |
|---|---|
| 22 · *¿Te comprometés a seguir el Protocolo de 9 Días?* | el paso entero, con los dos botones y el carrusel de chats |
| 24 · el **segundo audio** + el caso de 1 semana + *Generar mi Protocolo Personalizado* | el paso entero (queda un solo audio en el medio del quiz y el de la oferta) |
| 26 · el **resumen** entre la carga y la oferta (tabla comparativa, medidores, *Ascaris lumbricoides*, la bebida) | el paso entero |

Quedaron **25 pantallas (0–24)**, la barra de progreso llega a 100 % en la última pregunta y la carga encadena
directo a la oferta. Barrido de huérfanos y la regla general en [[quizzes-reglas-de-armado]] (regla del 19/11).
Lo que ya no se usa: `media/a2.mp3`, `media/v3_hombre_columna.mp4` y `media/v4_mujer_manos.mp4` (los dos mp4 siguen
subidos a Recursos, no molestan).

**Está en vivo** en `protocolo-desparacitacion-intestinal.impultienda.ar` desde el 18/11, pegado en
*Diseño de tienda → Contenido → HTML propio*. ⚠️ **Lo que está pegado es la versión de 28 pantallas: el recorte del
19/11 todavía no se subió.** Las **19 imágenes y los 6 videos viven en Diseño → Recursos**
(`sb.impultienda.ar/storage/…/store-resources/43d7fdfe-…/`); **los audios van embebidos**, porque Recursos no
acepta mp3. Detalle en [[quizzes-reglas-de-armado]] (regla del 18/11).

Copia en `OUTPUTS/2026-11-18-quiz-limpia-dolor.txt` y `OUTPUTS/2026-11-18-quiz-limpia-dolor-fuente.html`.

## Verificado

- Las **28 pantallas** recorridas por código en un iframe de 390 px: cero desbordes, cero elementos de más de 392 px,
  cero imágenes rotas.
- Tras el recorte del 19/11, las **25 pantallas** recorridas de nuevo en Chrome, clickeando paso por paso: cero
  desbordes, cero imágenes rotas, cero errores de consola, los **6 CTAs** ligados y la carga saltando a la oferta.
- **Barra de progreso** estrictamente creciente, 4 % → 100 %, contando solo las pantallas de pregunta.
- **Checkout** probado sobre una copia instrumentada con un host absoluto de prueba: los **6 CTAs** salen con el host
  entero y los 6 parámetros, y sin parámetros queda el checkout exacto (sin `?` colgado). `paso` no se reenvía.
- Las **19 imágenes** pasan a Blob y quedan decodificadas al arrancar.

## El VSL post-quiz (2026-11-22)

Clon 1:1 del VSL ganador de **Protocolo Chía 4S** (11:44, post-quiz), con la comunicación atada a los ads que ya
corren. Guion, tabla de equivalencias y mapa de b-rolls en
`OUTPUTS/2026-11-22-bcl-desparasitacion-articular-guion.md` y `…-plan.md`.

| | |
|---|---|
| **Duración** | **12:28** · 1080x1920 · 30 fps (crudo 16:23 → 15:35 recortado → `SPEED=1.25` a pedido de Santiago) |
| **Avatar** | el doctor asiático de los ads (`ARTROSIS V*`), **Avatar IV**, voz `damian` |
| **HeyGen** | 6 bloques de 667, 428, 526, 455, 346 y 524 palabras — **526 créditos** |
| **Montaje** | 34 b-rolls de los 51 clips propios + **11 placas** + cama de suspenso con ducking |
| **Entrega** | `~/Desktop/limpia-dolor/vsl/` — master y versión web de 720 para Panda Video |

- El nombre **"Limpia Dolor" no se dice nunca**: el producto es *Protocolo de Desparasitación Articular de 9 días*,
  que es lo que dice el logo del quiz.
- Las **4 fases de 4 semanas** del ganador pasaron a **3 etapas de 3 días** (Soltar · Limpiar · Reconstruir), para
  no contradecir los 9 días que promete el quiz.
- El quiz **no nombra los ingredientes** (dice "se consiguen en cualquier supermercado"), así que el VSL puede decir
  **carozo de palta y cúrcuma** como los ads, sin contradecirlo. La visual del jengibre quedó afuera por eso.
- Dos zonas **venden con la cara, sin un solo corte**: el value stack con el precio, y el cierre desde
  *"Yo ya hice mi parte"* hasta *"Te espero adentro"*.
- Las reglas técnicas que salieron de este montaje están en [[vsl-reglas-de-armado]] (bloque del 22/11).

## Preguntas abiertas

- **El nombre.** Puse *Protocolo Limpia Dolor* por el `<title>` del original (*Protocolo Limpa Dor*). Si querés otro,
  se cambia en un lugar.
- **El producto**: falta el PDF/entregable real (la receta de 9 días, la guía alimentaria y el bonus de movilidad).
- **El pixel** (`PIXEL_ID` vacío) y los anuncios.

## Relacionado

[[quizzes-reglas-de-armado]] · [[apimart]] · [[landings-funnels-y-upsells]] · [[modelo-low-ticket]] · [[como-trabajar-con-santiago]]

## Fuentes

- `https://minhareceita.online/` (quiz de InLead, descifrado el 18/11/2026)
- Conversación del 2026-11-18

## El original: Emma Miller (BR) y cómo se clonan sus ads (19/11/2026)

**La página fuente** es **`Emma Miller`** (`view_all_page_id=508084695729778`), con **~490 anuncios activos**
y **un solo texto** para todos (*"Dor nas juntas ao acordar? Rigidez depois de ficar muito tempo parado?…"*):
testean creativo, no copy, igual que [[higado-liviano]] y [[dieta-3-fases]].
En Argentina corre además `view_all_page_id=1172801672593830`, que vende el mismo **"Protocolo Limpia Dolor
9 Días" a $19.999** y un "Protocolo Diabetes 14 días", casi todo con **imágenes estáticas** (solo 2 videos).

### El molde de sus ads (medido)
- **~80 s de anuncio + una cola de reloj girando** hasta los 5 o 10 minutos. El corte es exacto: el audio
  muere a los 79,6 s y de ahí al final solo hay un reloj. Nuestros clones repiten eso con **~30 s de reloj**
  (total ~110 s).
- Placa de titular arriba (roja con texto blanco bold itálico, o blanca con texto negro, según el ad),
  subtítulo quemado de 2-4 palabras en blanco con la palabra clave en **amarillo**, b-rolls y **renders 3D
  médicos**, y cierre con placa + **tres flechas rojas**.

### Cómo se baja su material
El `<video>` de la Ads Library sirve **360x640**, que no alcanza. La buena está en el HTML de la página:
el campo **`video_hd_url`** (hay uno por tarjeta, en el mismo orden que los `<video>`) da **720x1280**.
Se baja desde la propia página con `fetch` + `blob` + `<a download>`, sin que la URL salga de Chrome.
⚠️ El `fetch` a blob corta cerca de **16 MiB**; los ads completos entran porque pesan 8-40 MB.

### El clon NO se genera de cero: se dobla
Comparando nuestro **v6** contra su original (#14 *Artrose no joelho*), son **el mismo video cuadro por
cuadro**. Lo único que cambia es la voz, la placa y los subtítulos. El flujo real, que está armado en la
cuenta de HeyGen de Santiago (`searasantiago58@gmail.com`, plan Pro):
1. Por cada ad se crea un **avatar de foto** del presentador, tomado de un cuadro limpio de su propio video,
   con el nombre `ARTROSIS V<n> AV<n> <plano>` (ya hay 17, de V1 a V9; el V6 no tiene porque es 100 % animado).
2. Se genera el **Vídeo de Avatar** con el guion en castellano, voz **`damian`** (el único clon masculino de
   la cuenta) y **Avatar IV a 1080p** (nunca Avatar 6, que viene por defecto y es el caro).
3. Se **monta localmente**: el avatar como base, encima los b-rolls y renders recortados del original en sus
   tiempos, la placa y los subtítulos propios.

### Borrar sus subtítulos en portugués (regla del 19/11)
Los b-rolls traen el subtítulo portugués quemado y **hay que sacarlo bien**.
- ⛔ **`delogo` no sirve**: deja rayas verticales muy visibles.
- ⛔ **Blur solo tampoco**: queda el fantasma del texto.
- ✅ Lo que funciona, y es lo que tiene el v6 aprobado: **recortar la banda, pasarle `gblur=sigma=50` +
  `eq=brightness=-0.34:contrast=0.45`, superponerla y rematar los bordes con dos `drawbox` de alpha 0,10 y
  0,16**. Queda una banda oscura difuminada que además hace de fondo al subtítulo nuevo.
- La banda va **a medida de cada clip**: la mayoría lleva `y 1040→1270`, pero los que tienen el subtítulo en
  dos líneas o más arriba necesitan arrancar en `y 920`. Hay que **mirar clip por clip**: el del viejito en
  la cama se escapó en la primera pasada.
- **La banda NO va sobre los planos del avatar**: ahí no hay nada que tapar y se ve como una franja negra
  pegada. Nuestros subtítulos se leen solos con su contorno.

### Las placas se calcan midiendo los píxeles rojos
En vez de estimar a ojo, se mide la caja del original (detectando los píxeles rojos por fila) y se dibuja la
nuestra con esas coordenadas exactas, **un poco más grande**, para que no asome el portugués por los costados.
Medidas del #25 en 1080x1920: titular `x166 y867 746x114`, bajada `x6 y985 1068x53`, placa final `y866 h196`.
Fuente: **Arial Bold Italic** con `borderw` del mismo blanco para engrosarla.

### Los subtítulos nuestros, medidos del v3
**y 1194–1246** (63,5 % del alto), letras de **53 px** (fuente ~72), **Rubik**, blanco con la palabra clave en
**amarillo**, 2-3 palabras por bloque. Se queman con un **.ass** y el filtro `subtitles` (ffmpeg tiene libass),
que es la única forma cómoda de pintar una sola palabra de otro color.

### Los tiempos salen del audio, no se estiman
Para calzar subtítulos y b-rolls hay que transcribir el audio **con marcas de tiempo**. La API de Gemini
(`gemini-3.8-flash`) lo hace, pero **tarda muchos minutos con audio largo y devuelve 503 seguido**: conviene
lanzarla temprano y en paralelo con el resto del trabajo. Como respaldo, el audio del avatar es voz limpia sin
música, así que **`silencedetect` da los cortes de frase reales** y se puede repartir el guion sobre ellos.
⚠️ Nunca estimar los tiempos escalando los del portugués: el ritmo no coincide frase a frase.

### Cuidado al matar procesos
`pkill` sobre un `ffmpeg` que está escribiendo deja el MP4 **corrupto aunque el header diga la duración
correcta**. Si se interrumpe un render, se borra el archivo y se rehace.

### Dos trampas del tramo final (19/11/2026)
- **El original tiene ~16 s de NEGRO entre el ad y el reloj.** Si se corta el reloj "desde donde termina el
  ad" sale un video con 16 s en negro. En el `hd-25` el ad muere a los 79,6 s y **el reloj recién arranca a
  los 96,6 s**. Nuestros videos aprobados (v6) van **del cierre directo al reloj, sin negro**, así que el
  reloj hay que buscarlo con `blackdetect` antes de recortarlo.
- **Cortar con `-c copy` no cae en keyframe** y mete esos mismos cuadros negros al principio del clip:
  el reloj se recorta **recodificando**.

### En los tramos de pantalla partida va NUESTRO avatar arriba (regla del 19/11)
Santiago, al ver el primer corte: *"cuando el avatar está dividido, de pantalla dividida, se ve que dejaste
el mismo, entonces claramente no coordina los labios… poner el avatar que hiciste con HeyGen arriba y
dejando el b-roll abajo"*.
- El original **alterna pantalla completa con pantalla partida** (presentador arriba, b-roll abajo). En el
  #25 hay **cinco tramos partidos**, no solo la apertura: 0-5,5 s, 6,6-8,4 s, 8,4-11,6 s, 25-27,6 s y
  38,9-45,5 s.
- Si de esos tramos se superpone el recorte **entero** del original, arriba queda el presentador de ellos
  hablando en portugués y **los labios no cierran**. Hay que superponer **solo la mitad de abajo** del
  b-roll, a partir de la línea de division, y dejar que arriba se vea nuestro avatar.
- **La línea se mide, no se estima**: se busca la fila con mayor discontinuidad vertical entre `y=700` y
  `y=1300`. En el #25 dio **930 a 986 segun el clip**. Un `div: 0` en `broll_tiempos.json` significa que ese
  b-roll va a pantalla completa (en el #25, las moleculas de la palta y el parasito).
- El encuadre del avatar a pantalla completa **coincide** con el del original, asi que el recorte superior
  calza sin reescalar. Lo unico que cambia es que nuestro plano es algo mas cerrado que el de la apertura
  de ellos, que usa una toma mas abierta.

### La musica de fondo
La **musica de suspenso de Santiago** (la misma de [[higado-liviano]], `musica-de-suspense-335486`), a
**0,15 con ducking** (`sidechaincompress` contra la voz): baja sola cuando habla y sube en los silencios y
en la cola de reloj. Santiago: *"que no tape tanto el sonido, o sea, en un volumen mediano"*.
En higado-liviano se habia usado fija al 0,20.

### ⛔ El Escritorio esta en iCloud: renderizar en disco local
Un `ffmpeg` largo que lee de `~/Desktop/` falla con **`Error opening input: Operation timed out`** en medio
del render, aunque el archivo exista y tenga el tamaño correcto. Paso obligatorio: **copiar todos los
insumos a una carpeta local** (el scratchpad de la sesion) y renderizar desde ahi; recien el entregable
final se copia al Escritorio.

### El cuadro base del avatar se BUSCA sin subtitulo, no se limpia (regla del 19/11)
Para el avatar del #09 limpie el subtitulo del cuadro base con `delogo` y **HeyGen le quemo la marca gris en
el pecho en todo el video**: inservible, hubo que rehacerlo y pagar el render dos veces.
- Antes de crear un avatar, **barrer el video buscando un cuadro realmente limpio**: contar pixeles blancos
  y amarillos en la banda del subtitulo (`y 880-1060`) cada medio segundo y quedarse con los que den **cero**.
  En el #09 habia dos, a los **76,0 s y 77,5 s**; en un ad de 80 s siempre hay alguno entre frase y frase.
- Solo si no aparece ninguno se limpia, y entonces la zona borrada tiene que quedar **tapada despues por el
  subtitulo nuestro**; si queda por encima, se ve.

### No todos los ads son "presentador a camara"
El **#09** (*Acaba com dor na coluna… com menos de R$8*) es **voz en off sobre escena**: el doctor aparece a
camara solo en los primeros 5 s y en los ultimos 15, y el resto son dos pacientes —doña Maria y don Antonio—
haciendo pruebas de movilidad. Ademas **tiene tres voces**: el doctor y las cuatro lineas de los pacientes.
- El doctor va con avatar y la voz `damian`; **las lineas de los pacientes se generan aparte** con las voces
  de la casa (mujer **Sulafat**, hombre **Orus**) y se insertan en sus huecos.
- Conviene medir el hueco de cada linea en el original antes de generarla, porque el castellano se estira:
  la linea larga de Antonio entraba en 6,1 s y salio de 8,9 a 11,4 s segun el modelo y el estilo.

### La franja del subtitulo se MIDE en cada video (19/11)
Buscando el cuadro limpio del entrevistador del **#21** mire la franja `y 880-1120`, que es donde caen los
subtitulos del #09 — pero los del #21 van en **`y 1100-1350`**. Resultado: el cuadro elegido tenia
*"faz doutor"* y HeyGen lo quemo en el pecho del avatar en todo el video. Render perdido.
- Antes de barrer en busca del cuadro limpio, **extraer un cuadro cualquiera y mirar a que altura esta el
  subtitulo de ESE video**. Varia entre ads de la misma pagina.
- Vale tambien para el color: el #21 subtitula en **verde**, no en amarillo, asi que el detector tiene que
  buscar el color de ese video.

### El #21 es un podcast de dos personas: dos avatares y dos voces
El **#21** (*Dor forte no ciatico e nas costas?*) alterna al **doctor mayor** con un **entrevistador joven**.
- Van **dos avatares** (`ARTROSIS V12 AV1 mayor` y `AV3 joven limpio`) y **dos videos de avatar** que se
  cortan en bloques y se intercalan, igual que en el #09.
- Como en la cuenta hay **una sola voz masculina** (`damian`), el joven se resuelve asi: se genera su texto
  con **Orus** por API y se le **sube el wav a HeyGen** (pestaña *Audio* del paso del guion, en vez de
  escribir el guion). HeyGen le hace el lip sync igual y los dos personajes suenan distinto, sin estrenar
  una voz nueva.
- ⚠️ Sus subtitulos van en **verde**, no en amarillo, y **mas abajo** (`y ~1100-1300`) que los del #09.
  El cierre no lleva texto: es **pantalla negra con tres flechas rojas**.

### Los subtitulos no se pisan con la placa
En el #09 la placa roja va de `y 1052` a `1363` y el subtitulo cae en `y 1190`: se superponen. En el
original **no hay subtitulo mientras esta la placa**. Regla: al generar el .ass, **descartar los eventos que
arrancan antes de que termine la placa**. En el #25 no hacia falta porque su placa esta mas arriba
(`y 867-1038`) y no llega al subtitulo.

## ⛔ Dos errores que Santiago encontró en la primera entrega (19/11, tarde)

Santiago: *"El v11 está totalmente mal, el audio está totalmente trabado… Ni lo miraste"* y *"el v12 tiene el
audio discoordinado con los labios… ya me cansé de decirte que tenés que usar siempre el avatar que vos
hacés"*. Las dos cosas se escuchaban/veían al primer play y yo había verificado **solo cuadros y numeros**.

### 1. Mezclar mono y estereo en el concat rompe el audio
Las voces de los pacientes salian de `tts_gemini` en **mono** y los bloques del avatar en **estereo**. Al
concatenarlas con el demuxer `concat`, el audio sale **trabado** y por tramos solo se oye una de las voces.
- **Regla: toda pieza que entra a un concat se normaliza a `-ac 2 -ar 48000` antes.** No alcanza con que el
  concat reencodee al final.
- Si ya esta armado, no hace falta rehacer el video: se extrae el audio de cada pieza a wav estereo, se
  concatenan los wav y se pega la pista al MP4 que ya tiene el video bien.

### 2. Casi ningun "b-roll" de ellos es un b-roll: es el presentador hablando
En el **#21**, de los 9 tramos que recorte como b-roll, **8 eran el presentador de ellos hablando** con un
grafico encima (la licuadora, el reloj, la taza, la pierna, la caja de remedios). Superpuestos enteros,
arriba queda **su boca moviendose en portugues** y los labios no cierran.
- **Regla: el avatar nuestro es la base de TODO el video.** De los tramos de ellos se superpone **solo el
  grafico**, recortando de su linea para abajo (`div` en el plan). El clip que no tenga un grafico
  aprovechable **se descarta** y queda nuestro avatar hablando.
- Es la misma causa que la correccion de pantalla partida del #25, pero ahi eran 5 tramos y acá son 8 de 9:
  **hay que mirar clip por clip si aparece una cara hablando**, no asumir que un recorte es b-roll.

### Y la regla de fondo: no se entrega sin mirar y escuchar
Una hoja de cuadros y `volumedetect` **no detectan** ni un audio trabado ni unos labios desfasados.
Antes de entregar: **transcribir el audio final** (si sale entrecortado o se pierde texto, hay un problema)
y **mirar los tramos donde hay una cara hablando**.

### Transcribir el audio final detecta lo que los cuadros no
Verificando el v12 por transcripcion aparecio un error que no se ve en ninguna hoja de cuadros: el doctor
contestaba **"Lo puede hacer" ANTES de que el joven le preguntara** "¿y lo puede hacer en casa?". Causa: al
cortar el audio del avatar en bloques, el corte M2/M3 cayo **despues** de esa frase en vez de antes.
- En un dialogo, el corte entre bloques va **en el silencio que separa las intervenciones**, y hay que
  confirmar **con que palabra termina y con cual arranca** cada bloque, no solo que el corte caiga en una pausa.
- El prompt que lo detecta: pedirle a Gemini que transcriba y que **avise en una linea `PROBLEMA:` si el
  audio esta cortado, trabado, se superponen voces o cambia de voz de golpe**.

### La banda no debe tapar el grafico
Primera version del v12 arreglado: puse la banda de `y 1030` a `1630` y **tapo la licuadora, el jengibre y
la taza**, que son justo lo que se quiere mostrar. Los subtitulos de ellos en el #21 estan en **y 1206-1246**
—medido clip por clip—, o sea **exactamente donde va el nuestro**. Con una banda de `y 1165` a `1315`
alcanza: tapa el de ellos, hace de fondo al nuestro y deja ver el grafico.
