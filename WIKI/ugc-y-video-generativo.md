# UGC y video generativo

> Reglas fijas de UGC (9:16, handheld, sin subtítulos ni música), avatares recurrentes, el pack de testimonios para Sora 2, prompts para Flow/VEO 3 y cómo armar un avatar de VSL en HeyGen. (fuente: RAW/2026-10-10-wiki-previa/ugc-y-video-generativo.md)

El UGC es una pata central de la estrategia creativa. La mayoría se produce con IA generativa, no con creadores reales.

## Reglas fijas de UGC

Aplican salvo instrucción contraria. Cuando no se respetan, son fuente recurrente de fricción:

- **9:16 vertical**
- Cámara **handheld**, natural, documental, realista
- Voz natural, sin sonar producido
- **Sin subtítulos** — Santiago los añade después en CapCut
- **Sin texto sobreimpreso** ni elementos gráficos innecesarios
- **Sin música** salvo que la pida
- Producto visible cuando corresponde
- Español latino o argentino según mercado ([[internacionalizacion]])
- Si pidió que el personaje **sostenga** el producto o el libro, lo sostiene **mientras habla** — no lo deja sobre una mesa

## Avatares

Personajes recurrentes de creativos. **No son personas del equipo.**

| Avatar | Perfil |
|---|---|
| Diego | Hombre |
| Cami | 29 años, runner, fitness |
| Mateo | 28 años |
| Delfi | 30 años |
| Susana | 56 años, maestra jubilada |

También se han pedido: mujeres de 35–40, madres, pastores, profesionales, personas en cocinas, personas mostrando productos.

**Contenido cristiano:** avatar pastor masculino de 50–60 años con apariencia real, contexto de iglesia. Detalle práctico registrado — ciertos nombres provocaban rechazo en los modelos y hubo que usar «Padre Fío» / «Padre Bio» como alternativa.

## El pack de producción

El prompt de testimonios en Sora 2 define el entregable estándar: **guion de voz (ElevenLabs) + prompt visual (Sora 2 / Runway)**, en tres estilos psicológicos distintos:

| Estilo | Psicología | Entorno |
|---|---|---|
| **El escéptico convertido** | «No creía, ahora estoy sorprendido» | Casa del avatar, selfie vertical |
| **El profesional satisfecho** | Serio, habla de ROI y resultados | Oficina o estudio bien iluminado |
| **El resultado tangible** | Alivio y felicidad | Usando el producto, lifestyle |

Regla de oro: **14 segundos máximo, 35–40 palabras**. Hook (0–3s) / Beneficio (4–10s) / Cierre + CTA (11–14s). Coherencia obligatoria entre avatar, entorno y guion.

## Prompts para video generativo

Regla crítica con **Flow / VEO 3** cuando se da una imagen de referencia:

> **«Guiate de esta imagen sin cambiar ni agregar nada.»**

Se preservan composición, personaje, entorno, vestimenta, posición, elementos, producto y escena. Solo cambia la acción o el diálogo pedido. Nada de elementos nuevos, nada de modificaciones arbitrarias.

Y cuando pide **«PROMPT NO UNA IMAGEN»**: se entrega solo el prompt, en bloque de código.

## Green screen

Para ciertos UGC se pide **fondo verde / chroma**, con el objetivo explícito de poder editar después en CapCut.

## Audio

- Voz natural, sin efectos innecesarios
- Persona hablando directamente a cámara
- Con ElevenLabs, **la duración del guion debe coincidir con la del creativo de referencia** del competidor
- **Ritmo de la voz en off (24/10/2026).** En los editores (`edit_*.py`) la voz pasa siempre por `silenceremove` + `atempo` antes de alinear subtítulos. Valores que pidió Santiago: `speed` ≥ **1.20** y `silence: [0.26, 0.12]` (umbral de pausa / silencio que se deja). Con 0.6/0.35 el ad "queda lento". Si el audio ya viene de un avatar que habla a cámara, no se tocan los silencios ([[atlas-de-cortes]]).

## Herramientas

**Video:** VEO 3 · Flow · Seedance 2.0 · Sora 2 · Runway · HeyGen (para VSL, hay lección dedicada)
**Voz:** ElevenLabs
**Edición y subtítulos:** CapCut

Ver [[stack-de-herramientas]].

## Complementos prácticos

### Cómo se pide la foto de un avatar (regla, 2026-10-28)
Santiago rechazó un prompt que pedía **estudio, fondo gris liso, cuerpo entero, pose rígida y boca cerrada**: *"me hizo cualquier cosa, la idea es hacer uno que sea casual, algo más normal, me hizo a un hombre parado nomás"*. La referencia que sí sirve son las dos tomas del Coach Santi de [[calistenia-rusa]].

- **Casual y en entorno real**, nunca estudio: el lugar donde ese personaje estaría de verdad (el jardín de su casa, la puerta de su taller), con desorden propio del lugar y profundidad de fondo.
- **En plena frase**: boca abierta hablando, mirada a la cámara y **las manos arriba en pleno gesto**. Una foto de alguien parado, quieto y callado no sirve.
- **Luz natural** de la tarde, nada de softbox ni fondo liso. Que parezca un cuadro sacado de un video de celular.
- **Plano medio**, de la cabeza a medio muslo, con aire arriba y a los costados para el recorte a 9:16.
- **Dos tomas del mismo personaje** (parado y sentado), que después se intercalan por bloque sin pagar render extra.
- Cara despejada: sin gorra, sin anteojos, sin nada tapándola. Ropa sin marcas ni estampas.
- Costo: la foto no cuesta créditos y el video sí. Si la primera sale con piel plástica o manos raras, se tira otra antes de subirla a HeyGen.

### Avatar de VSL en HeyGen
- Imagen base: pedirle a ChatGPT **varias poses o variantes de la misma persona**, que mejoran la consistencia del personaje. **Prueba de autoridad en la imagen:** diplomas, fotos familiares de fondo, vestuario y joyas acordes al personaje, e instrucciones anti-IA explícitas.
- En HeyGen: personaje virtual con **3–5 fotos en 9:16**.
- **Voz:** clonada (ElevenLabs u otra) desde un audio grabado con el guion completo, dividido en tramos si hace falta, e importada como **«voz de terceros»**. No se deja que HeyGen genere el guion.
- **Un audio por escena**, en 9:16.
- **Edición de un VSL de front:** recortar los silencios entre frases, que mejora la retención, y **B-roll cada 3–5 segundos, sobre todo al inicio**. El VSL post-pago, en cambio, va sin B-roll.
- Alternativa más barata a HeyGen: **DreamFace**.
- El mismo avatar sirve como **«personaje de autoridad» reutilizable** para tandas de anuncios, no solo para el VSL.

### B-roll generado
- **Flow / Veo 3:** clips de 8 s **acelerados ~1,5×** para ganar ritmo.
- **Seedance** también está disponible por API (KIE, Apimart) o en planes «ilimitados» de terceros. Conviene desconfiar de lo «ilimitado»: hay reportes de límites reales y bugs.

Relacionado: [[guiones-de-video-ads]] · [[imagenes-y-mockups]] · [[biblioteca-de-prompts]]

## Conexiones con tu operación actual
- **Cuando te escriba prompts de video**, aplico las reglas fijas por defecto: 9:16, handheld, sin subtítulos, sin texto sobreimpreso, sin música y el producto en la mano mientras habla.
- **Susana (56, maestra jubilada)** es el avatar ideal para la variable "anti-hustle jubilada" de [[scented-stones]] ("I'm 58 and I didn't want a side hustle…").
- **El "escéptico convertido"** del pack de testimonios es la estructura de la contadora del guión 3. Da para una versión de testimonio de 14 segundos.
- **Decisión pendiente sobre Emma Carter:** hoy es una persona **sin cara** (natives con manos, [[guiones-y-anuncios]]). Convertirla en avatar de HeyGen con cara le daría un "personaje de autoridad" reutilizable, pero cambia la estética. Te toca decidir.

## La skill `edicion-ia` (3/11/2026)

Desde el 3/11 está instalado el Manual de Edición IA de Launch Expert como skill **`edicion-ia`** ([[skills-launch-expert]]). Es el manual de producción completo: rutas de modelo con costo, generación sin tirar plata, detección de defectos y control final.

**Lo que suma a esta página:**
- **Rutas por tipo de video, con costo:** wan2.7-r2v por ApiMart con `reference_voice` (~US$0,06/s) para avatar con voz fija · Omni Flash 1.1 ext (~US$0,036/s) si se acepta que la voz varíe · Veo 3.1 Lite para diálogo corto con buena boca · Grok Imagine (US$0,05-0,11 por toma de 6 s) para B-roll · Kling 2.5/2.6 i2v (~US$0,17) para B-roll de calidad, **nunca con texto en pantalla porque deforma letras** · HeyGen Video Translation para doblar dejando la edición idéntica.
- **Lo que no funciona:** Kling con audio, Seedance con audio (~US$1 por 8 s), Veo 3.1 completo (~32 créditos/clip), Veo por Kie con fotos de personas, Omni completo.
- **Del guion a los clips:** una frase por clip (ads ~18-20 palabras, VSL hasta ~22), cortar **solo en coma o punto**, nada de clips de menos de 6 palabras, cifras en letras, y pedir en el prompt que termine la última palabra y se quede callada.
- **Ritmos medidos:** wan2.7 español = palabras/4,1 + 0,6 s · ElevenLabs ~161 ppm · HeyGen a speed 1,05 ~175 ppm.
- **Filtro de seguridad:** los modelos bloquean frases de presión de venta, y los bloqueos **no se cobran**. Tabla de reemplazos: "a un precio que no vas a volver a ver" → "solo en esta página"; "por un único pago de X" → "por X, en un solo pago". Si un clip falla 4 veces, cambiar el gesto o el prompt.
- **Nunca regenerar porque falló la descarga:** re-bajar con `curl -C -`. Regenerar cobra dos veces. Guardar el ID de cada tarea apenas se manda.
- **Defectos que hay que buscar siempre**, con su detección: ignora la foto de referencia (hasta ~45 % en Omni; correlación del primer cuadro, corte en 0,93), corte o zoom interno (diferencia entre cuadros > 6× la mediana), subtítulos quemados (OCR sobre la mitad inferior; detectar bordes no sirve), sílabas sueltas (alineación forzada + transcribir el clip **ya recortado y aislado**), tartamudeos (Whisper **medium**, el small no los oye), voz que cambia de tono (medir F0, regenerar lo que se sale ±8 %).
- **Falsos positivos de Whisper:** confunde siglas y marcas y alucina "subtítulos de Amara.org" o "suscribite" en los silencios. Revisar a mano antes de "arreglar".
- **Montaje:** bordes por alineación forzada (0,10 s de aire antes de la primera palabra, 0,16 s después de la última) y pausas internas **por energía del audio**, no por los tiempos de Whisper. Ads → SP 1,0-1,15 · GAP 0,60 s · KEEP 0,20 s. VSL → SP 1,12-1,15 · GAP 0,30 s · KEEP 0,14 s. Acelerar voz y video juntos. Audio final a **−14 LUFS**, música 0,05-0,08 con ducking.
- **Control final en orden**, y el paso que se suele saltear: el MP4 entero **no** ve las sílabas sueltas de los bordes, por eso hay que transcribir cada clip recortado por separado. Y mirar el video completo con auriculares: ningún script reemplaza escucharlo.

⚠️ **Dónde choca con lo tuyo y manda lo tuyo:** el manual elige la voz **por país** y la toma de una muestra de referencia; vos tenés voces fijas por género (**Sulafat** mujer, **Orus** hombre) generadas en **Google AI Studio por API**. El manual arma el visual con clips generados; vos usás **clip de TikTok, ni una foto fija**. Y tus ads de voz en off van a **speed 1.30**. Lo del manual que sí entra sin discusión es el control de calidad: los defectos, la detección y el orden del control final.

## Fuentes
- RAW/2026-10-10-wiki-previa/ugc-y-video-generativo.md (página de la wiki previa, actualizada el 2026-08-10)
- Fuentes originales citadas (todavía no están en este cerebro): RAW/contexto-chatgpt.md, RAW/prompts/prompt-testimonios-sora-2.md, RAW/formacion/lecciones/vsl-con-heygen.md
