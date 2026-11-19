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

## Entregables (18/11/2026)

```
~/Desktop/limpia-dolor/
  landing/limpia-dolor-quiz.txt    662 KB · lo que está pegado en la tienda
  landing/limpia-dolor-PRUEBA.html el mismo, para abrir en Chrome
  landing/quiz.html                el fuente, con el bloque CONFIG arriba
  landing/media/                   3 mp3 + 6 mp4 (los mp4 ya subidos a Recursos)
  imagenes/                        19 webp (los 19 ya subidos a Recursos)
```

**Está en vivo** en `protocolo-desparacitacion-intestinal.impultienda.ar` desde el 18/11, pegado en
*Diseño de tienda → Contenido → HTML propio*. Las **19 imágenes y los 6 videos viven en Diseño → Recursos**
(`sb.impultienda.ar/storage/…/store-resources/43d7fdfe-…/`); **los 3 audios van embebidos**, porque Recursos no
acepta mp3. Detalle en [[quizzes-reglas-de-armado]] (regla del 18/11).

Copia en `OUTPUTS/2026-11-18-quiz-limpia-dolor.txt` y `OUTPUTS/2026-11-18-quiz-limpia-dolor-fuente.html`.

## Verificado

- Las **28 pantallas** recorridas por código en un iframe de 390 px: cero desbordes, cero elementos de más de 392 px,
  cero imágenes rotas.
- **Barra de progreso** estrictamente creciente, 4 % → 100 %, contando solo las pantallas de pregunta.
- **Checkout** probado sobre una copia instrumentada con un host absoluto de prueba: los **6 CTAs** salen con el host
  entero y los 6 parámetros, y sin parámetros queda el checkout exacto (sin `?` colgado). `paso` no se reenvía.
- Las **19 imágenes** pasan a Blob y quedan decodificadas al arrancar.

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
