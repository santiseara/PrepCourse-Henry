---
name: antes-despues-ia
description: Hace de punta a punta un video vertical 100 % con IA en el formato «antes y después» que escala en Meta (alguien hace una selfie con su pareja atrás el día 1 y el día N, después una coach a cámara, un testimonio con foto del antes y del después y la coach recortada adelante, y un botón final), con voz fija por personaje, subtítulos dinámicos, stickers sobrios y SOLO VOZ. ACTIVAR con "video antes y después con IA", "formato marido día 1 día 21", "hacé este guion en video con avatar", "réplica del formato pilates/baile", "video de transformación con IA", "testimonio con IA", o cuando pasen un guion clip por clip con personajes y una referencia de este formato.
---

# Video «antes y después» 100 % IA

Del guion al MP4 final en un solo proyecto. Las imágenes, los avatares que hablan y las tomas mudas salen de **ApiMart**. La alineación, el recorte de la persona y el montaje corren **local**.

**Lo que sale:** MP4 1080x1920 de ~60-90 s, solo voz, −14 LUFS.
- **Gancho:** selfie del marido con la esposa bailando atrás, «día 01», corte seco a «día 21». El cambio de cuerpo se ve a primera vista.
- **Coach a cámara:** jump cuts y stickers chicos.
- **Testimonio:** pantalla completa con la foto animada del antes y del después, y la coach recortada abajo a la derecha, sin recuadro.
- **Cierre:** botón azul «MÁS INFORMACIÓN».

Costo de referencia: **~US$9 por video** (14 clips con voz ~US$8, 2 tomas mudas ~US$0,50, 5 fotos).

## 0. Reglas que no se negocian
1. **Cero música y cero efectos de sonido.** Los videos que escalan en este formato son solo voz. Ni whoosh, ni pop, ni riser.
2. **Una sola voz fija por personaje.** Cada personaje habla con UNA muestra de referencia (`voces/*.mp3`, 8-10 s), nunca con una voz descrita en el prompt: si no, la tonada cambia entre clips.
3. **Primero 1 clip de prueba**, se muestra y se espera el OK. Recién después va el lote.
4. **Regenerar SOLO los clips malos**, con la lista exacta. Una descarga fallida no se regenera: se baja de nuevo (`descargas_pendientes.jsonl`). Regenerar cobra dos veces.
5. **Los bordes de cada clip salen de la alineación forzada**, nunca de Whisper. Whisper pone la 1ª palabra en 0,00 s y deja sílabas sueltas en los empalmes.
6. **Las fotos del «después» se hacen editando la del «antes»** (mismo lugar, misma cara, misma cámara). Así el cambio se nota y es creíble.
7. **Testimonio honesto.** Si la persona del testimonio no existe, el video lleva el rótulo `"rotulo": "Caso ilustrativo · imágenes con IA"`. Sirve para mostrar el formato o para YouTube. **No lo pautes como si fuera una clienta real**: es un testimonio falso, y Meta rechaza los antes/después en «Salud y bienestar». Para pautar, usá una clienta real con su permiso y sus fotos.
8. Las claves van en variables de entorno (`~/.zshrc`). Nunca se pegan en el chat ni en `proyecto.json`.
9. Antes de entregar se corre el **control de la sección 5**. Si algo no se verificó, se dice.

## 1. Instalación (una vez)
```bash
# macOS con chip M recomendado (el recorte usa la GPU 'mps'). También corre en Linux/Windows con CPU o CUDA.
brew install ffmpeg                       # o tu gestor de paquetes
pip3 install torch torchaudio faster-whisper transformers opencv-python pillow numpy soundfile librosa
echo 'export APIMART_API_KEY="tu_clave"' >> ~/.zshrc      # https://apimart.ai → API keys
echo 'export KIE_API_KEY="tu_clave"' >> ~/.zshrc          # opcional: hosting gratis para subir fotos y voces (kie.ai)
source ~/.zshrc
```
Los modelos piden la foto y la voz por **URL pública**. `comun.subir()` las sube al hosting gratis de Kie. Si no usás Kie, subilas donde quieras y cargá las URLs en `subidas.json` (el formato está en el mensaje de error).

`<skill>` = la carpeta de esta skill (por ejemplo `~/.claude/skills/antes-despues-ia`). Las fuentes Poppins (licencia OFL) vienen en `fuentes/`. Los emojis de los stickers usan la fuente de Apple: en otro sistema, los stickers salen sin emoji.

## 2. Armar el proyecto
1. Creá una carpeta para el video y copiá `<skill>/ejemplo/proyecto.json` adentro.
2. Poné las **voces de referencia** en `voces/`: un mp3 de 8-10 s por personaje, con el acento exacto del país, hablando suelto y sin música. Pueden ser grabaciones tuyas o de un locutor (con su permiso), o el audio de un clip de avatar que ya te guste. Esa muestra define la voz de TODO el video.
3. Completá `proyecto.json` con el guion. Cada clip es 1-2 oraciones (≤ ~8 s de habla):
   - `escena`: `gancho` (selfie con alguien atrás), `presentador` (a cámara) o `testimonio` (con `fondo_video` = la toma muda del antes o del después).
   - `texto`: lo que dice, exacto, con los números en letras («cuarenta y dos»). En `numeros` decís cómo mostrarlos en el subtítulo («42»).
   - `gesto`: qué hace el que habla. En los clips del gancho, `fondo`: qué hace la persona de atrás. Va en inglés y es lo que le da vida a la escena.
   - `etiquetas` («día 01» / «día 21»), `stickers` (aparecen cuando se dice `palabra`), `boton`, `palabras_clave` (en caja amarilla), `golpes` (zoom corto en esa palabra).
   - `zoom_fondo.centro`: dónde está la persona de atrás en el cuadro 1080x1920. `entradas`: el zoom de apertura hacia ella en los clips que querés.
4. **Voseo:** wan2.7 dice el imperativo en forma de tú («toca», «completa», «asegura») aunque escribas «tocá». Escribilo sin imperativo: «tenés que tocar el botón…».

Todos los comandos se corren **desde la carpeta del proyecto**.

## 3. Producción (con OK en cada compuerta)
```bash
python3 <skill>/scripts/imagenes.py          # fotos base y después las «después» editando las «antes»
```
**Compuerta 1:** mostrá las fotos lado a lado y esperá el OK. Revisá que el cambio de cuerpo se vea al primer vistazo y que el resto (cara, ropa del que habla, lugar, encuadre) sea idéntico. Para rehacer una: borrala y volvé a correr con su nombre.

```bash
python3 <skill>/scripts/clips.py h1a         # 1 clip de prueba (~US$0,42)
python3 <skill>/scripts/alinear.py h1a       # ¿dice el guion exacto?
```
**Compuerta 2:** pasá el clip de prueba y esperá el OK de la voz, la cara y lo que pasa atrás.

```bash
python3 <skill>/scripts/clips.py             # el lote (solo genera los que faltan)
python3 <skill>/scripts/animar.py            # tomas mudas del testimonio (Hailuo 2.3)
python3 <skill>/scripts/alinear.py           # control de guion + bordes → words.json
python3 <skill>/scripts/hoja.py h1a h1b h2 h3 i1 ...   # build/hoja.jpg para mirar cuadro por cuadro
```
- Para cada `MAL`: movelo a `clips/viejos/` y regeneralo **solo a él** con `clips.py <clave>`.
- En la hoja, buscá: otra cara, ropa que cambia, saltos de plano y una persona de atrás que no hace lo pedido.

## 4. Voz pareja y montaje
```bash
python3 <skill>/scripts/voz.py               # tono por clip contra la mediana del personaje
```
wan2.7 varía el tono entre clips aunque use la misma referencia (en las pruebas, hasta +20 %). Si un clip se sale más de ±6 %, unificalo con **seed-vc**, local y gratis:
```bash
git clone https://github.com/Plachtaa/seed-vc ~/tools/seed-vc && cd ~/tools/seed-vc && python3.10 -m venv .venv && .venv/bin/pip install -r requirements.txt
# por clip: modelo f0, 30 pasos, cfg 0.7; referencia = 10-15 s de 2-3 clips cercanos a la mediana del personaje
.venv/bin/python inference.py --source <proyecto>/clips_audio/<k>.wav --target <proyecto>/ref_<personaje>.wav --output <proyecto>/vc_tmp \
   --diffusion-steps 30 --inference-cfg-rate 0.7 --f0-condition True --auto-f0-adjust True --semi-tone-shift 0
```
- Sacá el audio de cada clip entero (`ffmpeg -i clips/<k>.mp4 -ac 1 -ar 44100 clips_audio/<k>.wav`) y guardá cada resultado como `voz_vc/<k>.wav`, normalizado a −18 LUFS y con el mismo largo que el clip.
- Después de convertir, **transcribí cada clip de nuevo**. seed-vc a veces cambia una palabra (en las pruebas: «Hoy»→«Voy», «Tenés»→«Tienes»). Probá 60 pasos con cfg 0,5, o bajá el tempo a 0,9 antes de convertir y volvé a la velocidad original después.
- Si el clip que se rompe es uno de los que usaste de referencia, dejalo con su audio original: ya es esa voz.

```bash
python3 <skill>/scripts/recorte.py t1 t2     # recorta a la coach para ponerla delante del testimonio
python3 <skill>/scripts/montar.py --clave    # build/prev_*.jpg: 2 cuadros por clip, revisar ANTES del render
python3 <skill>/scripts/montar.py            # render final (o AUDIO_DIR=voz_vc python3 … si pasaste por seed-vc)
python3 <skill>/scripts/montar.py --audio    # si solo cambiaste voces: rearma el audio sin re-renderizar el video
```

## 5. Control antes de entregar
```bash
python3 <skill>/scripts/control.py           # volumen, negros/congelados, guion entero con Whisper medium, build/hoja_final.jpg
```
- **Aparece «bueno listo» o «mirá» de más:** un borde dejó pasar el relleno. Mirá el `b` de ese clip en `words.json`.
- **Una palabra distinta:** escuchá ese tramo aislado antes de regenerar. Whisper confunde en contexto: «Mirala ahora» lo oye «Mirá la hora», y «para hacer» lo oye «para ser».
- **Siempre sobre el render más nuevo.** Nunca analices un MP4 de antes del último cambio.
- Reportá qué encontraste y qué corregiste.

## 6. Problemas conocidos (y su arreglo)
| Síntoma | Causa | Arreglo |
|---|---|---|
| Se come la 1ª palabra | wan arranca a hablar en 0 s | ya va el relleno «Mirá,» adelante, que se recorta solo |
| Se come «Mirá» en «Mirá el caso…» | el relleno se funde con la frase | `relleno_inicio_alt` («Bueno,») se usa solo |
| La última palabra queda cortada o inventa palabras al final | wan estira el habla hasta el último cuadro | ya va «Bueno, listo.» al final; la duración sale de las sílabas |
| «toca / completa» en vez de «tocá» | wan pierde el voseo en el imperativo | reescribir: «tenés que tocar…» |
| La persona de atrás cambia de cuerpo | el prompt no lo fija | ya va «body shape, size and clothes stay exactly as in the first frame»; regenerar ese clip |
| Hailuo: «did not pass content safety review» (no cobra) | el prompt nombra la panza o el cuerpo | describí solo el movimiento («breathes, shifts her weight, looks at herself») |
| Zoom interno o cambio de plano en un clip | wan, ~1 de cada 15 | se ve en la hoja; regenerar si salta a mitad de frase |
| La coach recortada tiene bordes raros | la máscara toma un objeto | revisar `--clave`; tomá un fondo liso en `coach.png` |

## 7. Archivos
- `scripts/comun.py`: config, cliente de ApiMart (espera hasta 1 h y descarga con reintento), subida, rellenos y duración.
- `imagenes.py`, `clips.py` (wan2.7-r2v con `reference_voice`), `animar.py` (Hailuo 2.3).
- `alinear.py` (MMS + Whisper medium), `voz.py`, `hoja.py`, `recorte.py` (Mask2Former), `montar.py`, `control.py`.
- `norm_es.py`: normaliza el guion contra Whisper (números, tildes).
- `ejemplo/proyecto.json`: proyecto completo de ejemplo («Reto de baile 21 días») para copiar y adaptar.
