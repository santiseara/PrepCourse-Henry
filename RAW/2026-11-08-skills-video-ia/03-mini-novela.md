---
name: mini-novela
description: Crea anuncios en formato MINI NOVELA con IA (3-4 min, vertical, actores IA que actúan y dialogan con voces fijas, estilo novela) para Meta Ads, desde el guion hasta el MP4 final: arquitectura de la historia, personajes con antes/después, tomas con Veo 3.1 por ApiMart, verificación de cada toma, detector de voces cruzadas y montaje con subtítulos y placas. ACTIVAR cuando el usuario diga "mini novela", "novela con IA", "anuncio novela", "formato novela", "historia con actores IA", o pase una novela de referencia + un guion/oferta para generar otra.
---

# Mini novela IA · anuncios que se ven como una novela

Este formato escala en Brasil (ofertas con 70+ novelas activas a la vez). Funciona porque **no parece un anuncio**: es una historia
de 3-4 minutos con personajes que viven el problema, una amiga que revela el secreto y un final donde todo se resuelve. La venta
llega recién al final, cuando el espectador ya está enganchado con la historia.

Sale de novelas reales hechas 100 % con IA con estos mismos scripts.

---

## 0. Antes de arrancar

**Requisitos (una sola vez):**
```bash
# ffmpeg
brew install ffmpeg                       # Mac  (Windows: winget install ffmpeg)
# Python
pip install faster-whisper torch torchaudio numpy
pip install speechbrain librosa           # solo para el detector de voces (paso 6)
# Clave de ApiMart (https://apimart.ai): NUNCA escribirla en archivos
export APIMART_API_KEY="tu_clave"         # ponela en ~/.zshrc para no repetirla
```
Las imágenes se suben a un link público para que Veo las lea. Si tenés `KIE_API_KEY`, se usa Kie; si no, catbox.moe (es gratis).

**Scripts:** están en la carpeta `scripts/` de esta skill. Todos reciben la carpeta del proyecto (la que tiene `guion.py`).
Para correrlos: `python3 ~/.claude/skills/mini-novela/scripts/<script>.py <proyecto>`.

**Costos aproximados:**
- Toma de Veo 3.1 Fast (8 s): ~US$0,13. Una novela de 3:30 lleva ~45-55 tomas más reintentos, unos **US$8-10**.
- Imágenes: ~US$0,05-0,10 cada una.

---

## 1. Si el usuario pasa una novela de REFERENCIA: estudiarla primero

Antes de escribir, entendé el formato de la referencia:
1. **Transcribir con tiempos**, con faster-whisper y `word_timestamps`, para sacar quién habla y cuándo.
2. **Sacar cuadros** (`ffmpeg -vf fps=1/3`) y mirarlos: cuántas escenas hay, dónde transcurren, cuántos personajes y cómo cambian los cuerpos.
3. Anotar:
   - La arquitectura (sección 2).
   - Cuántas voces distintas hay y de quién es cada una.
   - El estilo de los subtítulos y de las placas.
   - Si lleva música (las que hicimos NO llevan).
4. **No confundir las voces:** cada personaje tiene UNA voz que no cambia en todo el video. La protagonista del antes y la del
   después son la misma persona y llevan la misma voz.

## 2. Arquitectura de la historia (no saltear ninguna parte)

| # | Parte | Para qué sirve | Duración |
|---|---|---|---|
| 1 | **HOY / hook** | El resultado ya logrado + una frase que no se entiende sola («Me apoyé en una pared») | 0-20 s |
| 2 | **ANTES** (placa «X MESES ANTES») | El dolor en escenas cotidianas y concretas: ropa que no entra, comer parado, no salir en las fotos | 20-60 s |
| 3 | **La amiga o el conocido que cambió** | Revela el **mecanismo** («no era falta de disciplina, era X») y dice que «hay un test que te dice cuál es la tuya» | ~60 s |
| 4 | **Tomas mudas** | La protagonista arranca: prepara, prueba, hace el test en el celular | 5-10 s |
| 5 | **El cambio** (placa «X MESES DESPUÉS») | **Se repiten las escenas del ANTES**, pero ahora salen bien: el jean entra, se agacha sin dolor | 30-45 s |
| 6 | **Un tercero pregunta** | Vecina, tía o compañera: «¿Qué hiciste?» → «Hacé el test. Hacelo hoy, no sé hasta cuándo está» | 15-20 s |
| 7 | **La experta a cámara** | «Tocá acá abajo, respondé unas preguntas y te armo X justo para vos» | 8-10 s |

**Lo que la hace brutal:**
- **Antes/después visible:** se ve a simple vista, con la misma cara, el mismo pelo y la misma voz. Solo cambian el cuerpo, la postura y la ropa.
- **Escenas espejo:** la misma situación aparece dos veces, primero con dolor y después resuelta. Es lo que más engancha.
- **Clímax emocional:** antes del CTA va un momento que emociona: la hija que llora, el marido que se suma.
- **Humor:** una escena de comedia en el medio (el marido se ríe de ella haciendo el ejercicio).
- **Personajes con oficio y barrio:** peluquera, albañil, costurera. Nada de gente genérica.
- **Políticas de Meta:** sin kilos exactos, sin promesas médicas, sin «enfermedad/diagnóstico», sin la palabra «link». Al quiz se lo llama «test».

## 3. Escribir el guion

Escribir **dos archivos** en la carpeta del proyecto:
1. `guion.md`: la versión para leer, con la oferta, los personajes y una tabla por escena (toma · acción · línea). Se le muestra al usuario y **se espera su OK**.
2. `guion.py`: la versión que leen los scripts. Copiar `plantillas/guion_ejemplo.py` (ahí están TODAS las reglas del formato) y completarlo.

Reglas del `guion.py`:
- **Una toma = máximo 8 s:** de 0 a 3 líneas que entren cómodas, más la ACCIÓN que hacen mientras hablan (en inglés).
- **Intercambios rápidos** («¿Ya?» / «Sí.» / «¿Y?»): una línea por toma. Si no, Veo repite, inventa o cruza las voces.
- **`POS` por escena:** describí a cada personaje por su lugar y su ropa en ESA escena («the woman on the left in the red dress»). Es lo que evita las voces cruzadas.
- **`VOZ`:** género + una descripción en inglés, la misma en todas las tomas.
- **`ACENTO`:** el del país de la oferta. Rioplatense: «acá», nunca «aquí»; «vos», nunca «tú».
- **Números escritos como se dicen** si son raros («cinco mil pesos»).

## 4. Piloto antes del lote (obligatorio)

Nunca generar la novela entera de una. Primero:
```bash
S=~/.claude/skills/mini-novela/scripts; P=<carpeta del proyecto>
python3 $S/imagenes.py $P --dry          # revisar los prompts
python3 $S/imagenes.py $P personajes     # retratos (antes y después de la misma cara)
python3 $S/imagenes.py $P escenas        # primer cuadro de cada escena
python3 $S/gen.py $P A1 A2 A3 --dry      # revisar los prompts de las tomas
python3 $S/gen.py $P A1 A2 A3            # SOLO la escena del hook
python3 $S/verif.py $P A1 A2 A3
```
Mostrarle al usuario los retratos, las escenas y las tres tomas, y **esperar su OK** (caras, voces y acento) antes de seguir.

## 5. Lote completo
```bash
python3 $S/gen.py $P                     # todas las que faltan (las escenas van en paralelo)
python3 $S/verif.py $P                   # al final imprime «PARA REGENERAR: ...»
$S/reintentar.sh $P A4 B2                # regenera esas tomas (hasta 5 intentos) y las verifica
```
- **Regenerar solo las tomas malas**, nunca todo.
- Si una toma falla por **descarga**, NO se regenera: el link queda en `clips/descargas_pendientes.jsonl` y se baja a mano.
- Si una toma tiene que salir de nuevo, primero se borra (o se mueve) `clips/<id>.mp4`.

## 6. Detector de voces cruzadas
```bash
python3 $S/voces.py $P
```
Marca las líneas donde Veo le dio la voz al personaje equivocado (CRUCE / GENERO) o mezcló dos voces (MEZCLA). Para arreglarlas:
```bash
python3 $S/partir.py $P G1 K3            # una línea por toma (mueve los clips viejos a clips/malos)
$S/reintentar.sh $P G1 G1b K3 K3b
python3 $S/voces.py $P                   # volver a pasarlo
```
Un hombre que se ríe o grita puede dar falso GENERO. Si no aparece CRUCE, escuchar la línea antes de regenerarla.

## 7. Montaje y control
```bash
python3 $S/montar.py $P                  # → <proyecto>/FINAL.mp4
python3 $S/qc.py $P                      # guion vs. audio + hoja de contacto build/hoja.jpg
```
- El montaje recorta cada toma a su tramo hablado (con bordes por alineación forzada, no por Whisper) y achica los huecos largos.
  Además agrega las placas, los subtítulos chicos en minúsculas y la placa final con la flecha y el CTA. Sin música ni SFX, a -14 LUFS.
- Si algún corte queda justo, se ajusta a mano en `ajustes.json` (`{"A3": {"a": 0.4, "b": 5.1}}`) y se vuelve a montar.
- **No se entrega** si el parecido entre guion y audio da menos de 0,97, si en la hoja de contacto una cara cambia entre tomas,
  si el antes/después no se nota o si hay texto quemado por Veo.

## 8. Lo que aprendimos (gotchas de Veo 3.1)

| Problema | Arreglo |
|---|---|
| Rellena los 8 s inventando frases | El prompt dice «ONLY these words… nothing before, between or after» y el montaje corta al final del guion |
| Le da la línea al personaje equivocado | `POS` claro por escena + «Speaker assignment is strict» (ya está en gen.py) → si igual pasa, `partir.py` |
| Encadenar muchas tomas desde el último cuadro deforma las caras (look plástico) | gen.py vuelve a la foto de la escena cada 2 tomas (`MAX_CADENA=2`) |
| Quema subtítulos inventados (~1 de cada 40 tomas) | Mirar la hoja de contacto y regenerar esa toma |
| Se le escapa «aquí», «tú», «compras» | El ACENTO lo dice explícito; si igual pasa, reescribir la línea («completá» en vez de «hacé») |
| El filtro bloquea líneas al azar (no cobra) | `reintentar.sh`; si se repite, alargar la frase o cambiar una palabra. «link» y frases de escasez muy agresivas se bloquean siempre |
| Caras quietas que solo mueven la boca (wan, Omni) | Por eso se usa Veo: los personajes ACTÚAN. Cada toma lleva una acción concreta |

## 9. Estructura de carpetas del proyecto
```
<proyecto>/
  guion.md              versión para leer (se aprueba)
  guion.py              versión para los scripts
  img/personajes/       retratos (antes, después y los demás)
  img/escenas/          primer cuadro de cada escena (A.png, B.png…)
  clips/                tomas de Veo (A1.mp4…)  ·  clips/malos/ las descartadas
  bordes.json           verificación de cada toma
  ajustes.json          (opcional) cortes a mano
  costos.jsonl          lo que costó cada generación
  build/                temporales del montaje y hoja de contacto
  FINAL.mp4             el anuncio
```
