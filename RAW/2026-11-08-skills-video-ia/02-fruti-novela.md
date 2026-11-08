---
name: fruti-novela
description: Crea anuncios en formato FRUTINOVELA (novela 3D estilo Pixar con personas con cabeza de fruta que actúan y dialogan, 3-4 min, vertical 9:16) para Meta Ads, desde el guion hasta el MP4 final con Veo 3.1 por ApiMart. ACTIVAR cuando el usuario diga "frutinovela", "fruti novela", "novela de frutas", "personajes fruta", "novela Pixar con frutas", o pase una frutinovela de ejemplo + su oferta para hacer otra, o pida cambiar el mecanismo de una frutinovela ya hecha.
---

# Frutinovela · novelas 3D con personajes fruta que venden

Una frutinovela es una mini novela de 3-4 minutos en 3D estilo Pixar: **personas con cabeza de fruta** que viven el problema,
discuten, apuestan, se transforman y al final cuentan cómo lo lograron. No parece un anuncio: parece una serie animada.
La fruta hace el trabajo visual: cada personaje se reconoce de un vistazo (la papaya, la cereza, la palta) y eso ayuda
a que la IA **no cruce las voces** entre ellos.

El ejemplo de esta skill es «La apuesta» (`plantillas/guion_ejemplo.py` + `ejemplo/`): 62 tomas, 3:42, unos US$12 en ApiMart.

---

## 0. Requisitos (una sola vez)
```bash
brew install ffmpeg                                   # Windows: winget install ffmpeg
pip install faster-whisper torch torchaudio numpy speechbrain librosa
export APIMART_API_KEY="tu_clave"                     # https://apimart.ai · en ~/.zshrc. NUNCA en archivos
```
- Las imágenes se suben a un link público para que Veo las lea: con `KIE_API_KEY` usa Kie; si no, catbox.moe (gratis).
- Scripts en `scripts/` de esta skill. Todos reciben la carpeta del proyecto (la que tiene `guion.py`):
  `S=~/.claude/skills/fruti-novela/scripts; P=<carpeta del proyecto>`
- Costos (ApiMart): toma de Veo 3.1 Fast 8 s ≈ **US$0,13**; imagen ≈ US$0,01. Novela de 3:30 ≈ 55-65 tomas + reintentos ≈ **US$8-12**.

## 1. Si el usuario pasa una frutinovela de EJEMPLO: estudiarla primero
1. Transcribir con tiempos (faster-whisper, `word_timestamps=True`).
2. Hoja de cuadros: `ffmpeg -i ej.mp4 -vf "fps=1/4,scale=270:-1,tile=8x7" hoja.jpg` y mirarla.
3. Anotar: qué fruta es cada personaje, su ropa y su lugar en cada escena; cuántas voces hay; la arquitectura (§2);
   el estilo de subtítulos y las placas («21 DÍAS DESPUÉS»).
4. Mantener la historia y el ritmo, y adaptar al país de la oferta: moneda, nombres, voseo/tuteo, la experta o marca.

## 2. Arquitectura (la que mejor funciona: «la apuesta»)
| # | Parte | Qué pasa | Duración |
|---|---|---|---|
| 1 | **Humillación pública** | En una comida familiar le tiran un comentario cruel delante de todos («para tu talle nadie te arregla nada») | 0-30 s |
| 2 | **La apuesta con plazo** | Alguien apuesta plata a que no cambia antes de un evento (cumpleaños, casamiento) en X días | 10 s |
| 3 | **El intento que no funciona** | Gimnasio, dieta, lechuga; la pareja se burla («faltan 14 días y estás igual») | 20 s |
| 4 | **La mentora revela el MECANISMO** | Una vecina/verdulera/amiga: «vas perdiendo porque lo hacés de la forma que no funciona…» + qué es, cuánto dura, qué hace | 50-60 s |
| 5 | **La transformación** | Ella cuenta a cámara mientras entrena: semana 1, semana 2, el jean que ahora cierra | 20-25 s |
| 6 | **La revancha** (placa «X DÍAS DESPUÉS») | Llega al evento, cobra la apuesta delante de todos, el que se burlaba se queda mudo | 25 s |
| 7 | **La amiga pregunta → CTA** | «¿Te operaste?» → explica el mecanismo otra vez → «Tocá en Más información y hacé el test gratis» | 30 s |

Lo que la hace funcionar: **villanos claros** (cuñada, marido burlón), **plata en juego** con fecha, **revancha visible**,
el mecanismo contado **dos veces** (mentora y protagonista) y un cierre con escasez suave («el grupo nuevo está por cerrar»).
Políticas de Meta: sin kilos exactos, sin «enfermedad/diagnóstico», sin la palabra «link»; al quiz se lo llama «test».

### Cambiar SOLO el mecanismo (para reutilizar una novela ya hecha)
Las tomas del mecanismo están en la parte 4 (mentora) y en la parte 7 (protagonista). En el ejemplo: C5-C7, C9-C14 y F4-F6.
Se reescriben esas líneas en `guion.py`, se mueven esos clips a `clips/malos/` y se regeneran solo esos (≈ US$2).
El resto de la novela (humillación, apuesta, revancha) queda igual.

## 3. Diseño de personajes fruta (lo que evita el 80 % de los problemas)
- **Una fruta distinta por personaje y de color distinto**: papaya (amarilla), cereza (roja), palta (verde), ananá, durazno (rosa).
  Nunca dos de la misma fruta ni de colores parecidos en la misma escena (dos frutillas = voces cruzadas).
- La fruta acompaña al personaje: protagonista con cuerpo grande = papaya; la cuñada filosa = cereza brillante; la sabia = palta con anteojos.
- **Antes y después = la misma imagen editada** (`("zulma_antes", "ahora más delgada…")`): misma cara, mismas hojas, otro cuerpo y otra ropa.
- Ropa fija por personaje y por escena: se usa en los `POS` para que Veo sepa quién habla.
- Estilo fijo en `FOTO`, `CUADRO` y `ESTILO` del guion (ver el ejemplo): «3D animated Pixar-style… human bodies with big expressive fruit heads».

## 4. El prompteo (cómo escribir `guion.py`)
Copiar `plantillas/guion_ejemplo.py` y reemplazar. Partes:
- `ACENTO`: el del país («Rioplatense Spanish… voseo, 'acá' never 'aquí'»).
- `PERSONAJES`: retrato nuevo = texto en inglés con FRUTA EN MAYÚSCULAS, edad, cuerpo, expresión y ropa.
- `ESCENAS[letra] = (descripción, [refs])`: el primer cuadro de cada escena, con cada personaje ubicado (izquierda/derecha/fondo).
  Escribir «Only these two women are in the yard, nobody else in the background» si hay riesgo de extras parecidos.
- `VOZ[clave] = ("F"/"M", descripción)`: **voces bien separadas por tono y edad**:
  grave y lenta (la mayor), aguda y filosa (la villana), media y cálida (la protagonista), rápida y aniñada (la amiga);
  hombres «MAN … very deep, low … male baritone voice». La misma descripción en todas las tomas.
- `POS[letra][clave]`: «the papaya-head woman in the grey t-shirt». Fruta + ropa = quién habla, sin dudas.
- `TOMAS`: `(id, imagen_de_arranque, acción_en_inglés, [(clave, emoción, "línea")])`
  - **Una línea y un solo personaje por toma.** Es la regla que más voces salva.
  - Máximo ~16 palabras por toma (8 s). Si es más larga, partirla en dos tomas.
  - La acción siempre es algo concreto (señala, cuenta billetes, se cruza de brazos). Nada de caras quietas.
  - `imagen_de_arranque`: la letra de la escena o de un primer plano (`"P"`), o `"prev"`.
- `PLACAS = {"E1": "21 DÍAS DESPUÉS"}` y `CTA = ("Tocá en", "Más información")`.

## 5. Piloto (obligatorio) y lote
```bash
python3 $S/imagenes.py $P --dry && python3 $S/imagenes.py $P personajes && python3 $S/imagenes.py $P escenas
python3 $S/gen.py $P A1 A2 A3 && python3 $S/verif.py $P A1 A2 A3 && python3 $S/voces.py $P
```
Mostrar al usuario la hoja de personajes, las escenas y las 3 tomas, y **esperar su OK** (caras, voces y acento). Después:
```bash
$S/paralelo.sh $P 15          # todas las tomas que faltan, 15 a la vez, cada una desde la imagen de su escena; reintenta el filtro
python3 $S/verif.py $P        # guion por toma
python3 $S/voces.py $P        # voces cruzadas (CRUCE / GENERO / MEZCLA)
python3 $S/tono.py $P         # tono de cada línea contra su personaje
```
`paralelo.sh` es ~10 veces más rápido que en cadena y las caras quedan más estables (cada toma arranca de la imagen limpia).

## 6. Control de imagen (mirar SIEMPRE la hoja de contacto)
`python3 $S/qc.py $P` arma `build/hoja.jpg`. Para una toma puntual: `ffmpeg -i clips/E7.mp4 -vf "fps=1,scale=200:-1,tile=8x1" tira.jpg`.
Buscar y regenerar solo esas tomas:
- **Una cabeza que cambia de fruta o de color** a mitad de la toma.
- **Alguien que camina a través de la mesa** o aparece un personaje nuevo → acción «Everyone stays in place, nobody walks».
- **Cuerpos imposibles** en ejercicios → describir una pose simple y anatómica (sentadilla contra la pared) en la escena.
- **Un personaje de fondo que se ríe falso todo el tiempo** → rehacer la imagen de la escena con él «eating calmly with his mouth closed».
- **Subtítulos inventados quemados** por Veo.

## 7. Problemas de Veo y cómo se arreglan
| Problema | Arreglo |
|---|---|
| El filtro frena la toma («content safety», no cobra) | Sacar de la ACCIÓN palabras sobre el cuerpo («le mira el cuerpo», «se tapa la panza») |
| Frena siempre las líneas muy cortas («Pasámelo.», «Tu apuesta.») | Alargarlas un poco («Pasámelo ya mismo, Rosa.») o arrancar desde un primer plano del personaje solo |
| Un hombre habla con voz de mujer | Primer plano con él SOLO en cuadro (escena `P`/`H`) + emoción calma («deep, smug, calm»), nunca «laughing» |
| La línea de la villana suena a la protagonista | Primer plano de la villana sola (escena `Q`) |
| En el primer plano la cámara se abre y aparecen personajes deformes | Acción: «Tight static close-up for the whole video: the camera never moves or zooms out and no other people ever appear» |
| La protagonista suena más aguda en algunas tomas | Si en la escena no hay otra mujer, es su voz con otra emoción: aceptarla o regenerar con emoción más calma |
| Inventa palabras antes o después | El montaje corta pegado a la primera y última palabra del guion |
| Se le escapa «aquí», «tú» | El ACENTO lo pide; si igual pasa, reescribir la línea |

Escuchar siempre las marcas de `voces.py` y `tono.py` antes de regenerar: una mujer que grita o un hombre que se ríe dan falsos avisos.

## 8. Montaje
```bash
MUDA_MAX=3 python3 $S/montar.py $P     # → <proyecto>/FINAL.mp4
python3 $S/qc.py $P                    # parecido guion/audio (≥ 0,97) + hoja de contacto
```
- Cada toma se corta **pegada a la primera y la última palabra** (0,08 s antes, 0,16 s después): así no entran los grititos,
  risas o palabras que Veo agrega en los bordes. Pausas internas largas se achican.
- **Subtítulos estilo captions**: una sola línea, 1-3 palabras en MAYÚSCULAS, amarillo con borde negro grueso, sincronizados palabra por palabra.
- Placas sobre negro («21 DÍAS DESPUÉS») y placa final con flecha + CTA. Sin música ni SFX, audio a -14 LUFS.
- Corte a mano: `ajustes.json` → `{"A3": {"a": 0.4, "b": 5.1}}`. Para sacar una toma del corte sin borrarla, montar una
  copia del proyecto con `TOMAS=[t for t in TOMAS if t[0] not in ("A2",)]` al final de su `guion.py`.
- **No se entrega** si el parecido da < 0,97, si una cara o una fruta cambia, si alguien atraviesa objetos o hay texto quemado.

## 9. Carpetas del proyecto
```
<proyecto>/
  guion.md   (versión para leer y aprobar)      guion.py   (la que leen los scripts)
  img/personajes/  img/escenas/                 clips/  ·  clips/malos/ (descartadas)
  bordes.json  ajustes.json  costos.jsonl  build/  FINAL.mp4
```

## 10. Uso honesto
Es una dramatización con personajes animados: no la presentes como un testimonio real, no prometas resultados exactos
y respetá las políticas de Meta del país donde la publiques.
