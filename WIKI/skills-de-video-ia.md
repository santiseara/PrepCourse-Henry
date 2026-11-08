# Skills de video con IA (ApiMart)

> Tres skills nuevas que Santiago pasó el 8/11/2026, instaladas en `~/.claude/skills/`: **`antes-despues-ia`**, **`mini-novela`** y **`fruti-novela`**. Las tres hacen un anuncio de punta a punta (guion → MP4 vertical) con **ApiMart** como pasarela de generación y montaje local con ffmpeg. Son hermanas de las 7 de [[skills-launch-expert]]: Claude las carga solo cuando la tarea las toca, no hay que pegarlas en el chat. (fuente: RAW/2026-11-08-skills-video-ia/)

**Lo que tienen en común, y es lo que las hace valer:** un piloto obligatorio antes del lote, regenerar **solo** lo que salió mal, los bordes de cada clip por **alineación forzada** y no por Whisper, **cero música y cero SFX**, audio a **−14 LUFS** y un control de calidad con hoja de contacto antes de entregar. Todo eso ya era regla en [[estilo-de-video-ia]] y en el Manual de Edición IA.

## Las 3, qué son y con qué se disparan

| Skill | Formato que produce | Largo | Modelo | Costo por video | Frase que la activa |
|---|---|---|---|---|---|
| `antes-despues-ia` | Selfie "día 01 / día 21" con alguien atrás + coach a cámara + testimonio con antes/después + botón final | 60-90 s | **wan2.7-r2v** (voz fija por referencia) + Hailuo 2.3 para tomas mudas | **~US$9** (14 clips ≈ US$8, 2 mudas ≈ US$0,50, 5 fotos) | "video antes y después con IA", "formato marido día 1 día 21", "video de transformación con IA" |
| `mini-novela` | Mini novela con actores IA que actúan y dialogan, estilo novela brasileña | 3-4 min | **Veo 3.1 Fast** | **US$8-10** (45-55 tomas a US$0,13) | "mini novela", "novela con IA", "anuncio novela", "formato novela" |
| `fruti-novela` | Lo mismo pero en **3D estilo Pixar con personas con cabeza de fruta** | 3-4 min | **Veo 3.1 Fast** | **US$8-12** (55-65 tomas) | "frutinovela", "novela de frutas", "personajes fruta" |

`mini-novela` y `fruti-novela` son la misma máquina (mismos scripts: `imagenes.py`, `gen.py`, `verif.py`, `voces.py`, `qc.py`, `montar.py`); la fruti agrega `tono.py`, `paralelo.sh` y el diseño de personajes-fruta. `antes-despues-ia` es otra máquina: trae recorte de persona con Mask2Former, unificación de tono de voz con seed-vc y stickers.

## Requisitos (una vez, y todavía no están)

```bash
brew install ffmpeg
pip3 install faster-whisper torch torchaudio numpy speechbrain librosa     # las tres novelas
pip3 install transformers opencv-python pillow soundfile                   # además, antes-despues-ia
export APIMART_API_KEY="..."    # en ~/.zshrc, nunca en archivos ni en el chat
export KIE_API_KEY="..."        # opcional: hosting gratis de imágenes/voces; si no, catbox.moe
```

⚠️ **La clave ya existe, solo no está exportada.** [[apimart]] la guarda en `~/.config/apimart/env` y con el mismo nombre que piden las skills (`APIMART_API_KEY`), pero ese archivo no se carga solo. Una línea en `~/.zshrc` lo arregla: `set -a; . ~/.config/apimart/env; set +a`. **Y el saldo de ApiMart al 4/11 era US$0,00**: sin créditos la API devuelve 402 y no genera nada.

## Lo que estas skills agregan y no estaba escrito

### La arquitectura de la novela que escala (esto es lo más valioso)

`mini-novela` trae la estructura de 7 partes de las novelas brasileñas (ofertas con 70+ novelas activas a la vez):

1. **HOY / hook** (0-20 s): el resultado ya logrado + una frase que no se entiende sola ("Me apoyé en una pared").
2. **ANTES**, con placa "X MESES ANTES" (20-60 s): el dolor en escenas cotidianas (la ropa que no entra, comer parado, no salir en las fotos).
3. **La amiga que cambió** (~60 s): revela el **mecanismo** ("no era falta de disciplina, era X") y nombra el **test**.
4. **Tomas mudas** (5-10 s): arranca, prueba, hace el test en el celular.
5. **El cambio**, placa "X MESES DESPUÉS" (30-45 s): **se repiten las escenas del ANTES, ahora bien**.
6. **Un tercero pregunta** (15-20 s): "¿Qué hiciste?" → "Hacé el test, no sé hasta cuándo está".
7. **La experta a cámara** (8-10 s): "Tocá acá abajo, respondé unas preguntas y te armo X para vos".

Lo que la hace funcionar: **escenas espejo** (la misma situación con dolor y después resuelta — es lo que más engancha), antes/después con la **misma cara, mismo pelo y misma voz**, un clímax emocional antes del CTA, una escena de comedia en el medio y personajes con oficio y barrio (peluquera, albañil, costurera), nunca gente genérica.

`fruti-novela` cambia la arquitectura por **"la apuesta"**, que es más dura y más corta de armar:

1. **Humillación pública** (0-30 s): un comentario cruel delante de toda la familia.
2. **La apuesta con plazo** (10 s): alguien apuesta plata a que no cambia antes de un evento.
3. **El intento que no funciona** (20 s) y la burla ("faltan 14 días y estás igual").
4. **La mentora revela el mecanismo** (50-60 s).
5. **La transformación** (20-25 s): ella cuenta a cámara mientras entrena.
6. **La revancha**, placa "X DÍAS DESPUÉS" (25 s): cobra la apuesta delante de todos.
7. **La amiga pregunta → CTA** (30 s): el mecanismo contado **por segunda vez** + escasez suave.

Las dos piden: **villanos claros**, plata en juego con fecha, revancha visible y el **mecanismo dicho dos veces**.

### Reutilizar una novela cambiando solo el mecanismo
Es la jugada más barata de las tres skills: las tomas del mecanismo viven en dos partes (la mentora y la protagonista). Se reescriben esas líneas en `guion.py`, se mueven esos clips a `clips/malos/` y se regeneran **solo esos**: **≈ US$2** por una novela nueva. El resto (humillación, apuesta, revancha) queda igual. Es el equivalente a la renovación por hook de [[renovacion-de-creativos]], pero de 3 minutos.

### El problema de las voces cruzadas y cómo se mata
Veo le da la línea al personaje equivocado. Las defensas, en orden:
- **Una línea y un solo personaje por toma.** Es la regla que más voces salva. Máximo ~16 palabras (8 s).
- **`POS` por escena:** describir a cada uno por su lugar y su ropa en **esa** escena ("the woman on the left in the red dress"). En la fruti, **fruta + ropa** ("the papaya-head woman in the grey t-shirt").
- **Voces bien separadas por tono y edad** en `VOZ`, con la **misma descripción en todas las tomas**: grave y lenta la mayor, aguda y filosa la villana, media y cálida la protagonista, hombres "very deep, low, male baritone".
- **`voces.py`** marca CRUCE / GENERO / MEZCLA con speechbrain; **`partir.py`** parte la toma en una línea por toma y se regenera.
- Un hombre que se ríe o una mujer que grita dan **falso positivo**: escuchar antes de regenerar.
- Si igual pasa: **primer plano del personaje solo en cuadro**, con emoción calma, nunca "laughing".

### Diseño de personajes fruta (lo que evita el 80 % de los problemas)
- **Una fruta distinta y de color distinto por personaje**: papaya amarilla, cereza roja, palta verde, ananá, durazno rosa. **Dos frutillas en la misma escena = voces cruzadas.**
- La fruta acompaña al personaje: protagonista con cuerpo grande = papaya; la cuñada filosa = cereza brillante; la sabia = palta con anteojos.
- Ropa fija por personaje y por escena, porque la ropa es lo que identifica a quién habla.
- **El "después" es la misma imagen editada**, nunca una imagen nueva: misma cara, mismas hojas, otro cuerpo y otra ropa.

### Lo que `antes-despues-ia` agrega aparte
- **Las fotos del "después" se hacen editando la del "antes"** (mismo lugar, misma cara, misma cámara). Así el cambio se nota y es creíble.
- **El tono de wan2.7 varía entre clips hasta +20 %** aunque uses la misma voz de referencia. `voz.py` mide cada clip contra la mediana del personaje; si se sale de **±6 %**, se unifica con **seed-vc** (local y gratis). Después de convertir hay que **transcribir de nuevo**: seed-vc cambia palabras ("Hoy"→"Voy", "Tenés"→"Tienes").
- **Rellenos automáticos en los bordes:** wan arranca a hablar en 0 s y estira el habla hasta el último cuadro, así que mete un "Mirá," adelante y un "Bueno, listo." atrás, y los recorta solos. Si aparece "bueno listo" en el control, un borde dejó pasar el relleno.
- **Recorte de la coach con Mask2Former** para ponerla delante del testimonio, sin recuadro, abajo a la derecha.
- Hailuo 2.3 para las tomas mudas: si el prompt nombra la panza o el cuerpo, el filtro frena (y no cobra) → describir solo el movimiento ("breathes, shifts her weight, looks at herself").

### El voseo y los filtros, ya resueltos
- **wan2.7 y Veo pierden el voseo en el imperativo** ("toca", "completa", "asegura") aunque escribas "tocá". El arreglo es reescribir sin imperativo: *"tenés que tocar el botón…"*.
- El `ACENTO` se declara explícito ("Rioplatense Spanish, voseo, 'acá' never 'aquí'"). Si igual se le escapa, se reescribe la línea.
- **Políticas de Meta ya metidas en la skill:** sin kilos exactos, sin "enfermedad/diagnóstico", **sin la palabra "link"** (al quiz se lo llama **"test"**), y las frases de escasez muy agresivas se bloquean siempre.
- **El filtro de contenido no cobra** cuando frena. Frena las líneas muy cortas ("Pasámelo.") → alargarlas. Frena las acciones que nombran el cuerpo → describir solo el movimiento.

### Lo que no se entrega
Las tres coinciden: **no se entrega** si el parecido guion/audio da **menos de 0,97**, si en la hoja de contacto una cara o una fruta cambia entre tomas, si alguien atraviesa un objeto, si el antes/después no se nota o si **Veo quemó subtítulos inventados** (~1 de cada 40 tomas).

## Dónde chocan con las reglas de Santiago

| Lo que dice la skill | Lo que manda | Qué hacer |
|---|---|---|
| Voz con **muestra de referencia** por personaje (wan2.7 / Veo generan la voz) | **Las voces van en Google AI Studio: mujer = Sulafat, hombre = Orus**, por API, a **speed 1.30** ([[estilo-de-video-ia]]) | En las novelas la voz **viene pegada al clip de Veo**, no se puede sustituir sin romper el labial: es la excepción. En `antes-despues-ia`, si hay que unificar tono, seed-vc contra una referencia de Sulafat/Orus. |
| Visual generado 100 % con IA | **Todo el visual es clip de TikTok**, ni una foto fija ni stock | Las tres son **otro formato**, no el de voz en off: acá el visual generado es el producto. No mezclar las dos recetas en el mismo video. |
| Modelos y parámetros propios | **Siempre lo más barato que sirva** | Ya cumplen: Veo 3.1 **Fast**, wan2.7 en vez de Veo completo. Nada de subir a Veo full. |
| Piloto de 3 tomas y después el lote entero | **Tanda de máximo 6 videos**, 3 si es una oferta que ya corre | Una novela es **un** creativo de 3-4 min, no una tanda. Para tandas sigue mandando la regla de 3/6. |
| Testimonio con personas que no existen | — | **Rótulo obligatorio "Caso ilustrativo · imágenes con IA"** y la skill avisa: Meta rechaza los antes/después en Salud y bienestar. **No pautarlo como testimonio real.** Para pautar, clienta real con permiso y sus fotos. |

## Preguntas abiertas

- **Falta cargar saldo en ApiMart** (y cargar `~/.config/apimart/env` en la shell). Hasta eso, ninguna de las tres puede generar un cuadro.
- Falta probar una novela entera de punta a punta con una oferta real. El candidato natural es una oferta de salud/estética con quiz ya armado ([[dancego]], [[pilates-hormonal]], [[monjaro-violeta]]): las tres tienen el "test" que pide el CTA del formato.
- Falta decidir si la novela de 3-4 min entra en la V3 como un creativo más o en una CBO aparte: es un formato de retención larga, el CPA y el hook rate no se leen igual que en un ad de 40 s ([[metricas-y-kpis]]).
- `antes-despues-ia` pide **chip M con GPU `mps`** para el recorte y los emojis de los stickers usan la fuente de Apple. En otro equipo salen sin emoji.
- Los ejemplos de referencia (los `.mp4` de las páginas de las skills) **no los tenemos**: las dos novelas rinden mucho más si se les pasa una novela de ejemplo para estudiar primero.

## Relacionado
[[skills-launch-expert]] · [[apimart]] · [[estilo-de-video-ia]] · [[ugc-y-video-generativo]] · [[guiones-y-anuncios]] · [[renovacion-de-creativos]] · [[quiz-funnel]] · [[vsl-reglas-de-armado]]

## Fuentes
- RAW/2026-11-08-skills-video-ia/01-antes-despues-ia.md
- RAW/2026-11-08-skills-video-ia/02-fruti-novela.md
- RAW/2026-11-08-skills-video-ia/03-mini-novela.md
- RAW/2026-11-08-skills-video-ia/skill-antes-despues-ia.zip · skill-fruti-novela.zip · skill-mini-novela-v2.zip
- Instaladas en `~/.claude/skills/antes-despues-ia/`, `~/.claude/skills/mini-novela/`, `~/.claude/skills/fruti-novela/`
