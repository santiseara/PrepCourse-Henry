# Prompt para la sesión nueva — replicar 12 anuncios de Fausto Almeida

Estamos en el segundo cerebro de Santiago: `/Users/santiagoseara/PrepCourse-Henry`.
Respondé siempre en español argentino con voseo.

## Antes de tocar nada, leé

- `CLAUDE.md`
- `WIKI/como-trabajar-con-santiago.md`
- `WIKI/guiones-y-anuncios.md`
- `WIKI/vsl-reglas-de-armado.md` — **sobre todo las secciones 10 y 11**, que son los errores
  que ya se cometieron en esta misma oferta. No los repitas.
- `WIKI/higado-liviano.md`

## La tarea

Entrá a esta página de la Biblioteca de Anuncios de Meta:

https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=AR&id=1031228289991869&is_targeted_country=false&media_type=all&search_type=page&sort_data[mode]=total_impressions&sort_data[direction]=desc&view_all_page_id=1397189743483324

Es **Fausto Almeida**, page id `1397189743483324`, Argentina, ordenada por impresiones.

Tenés que entrar con **Claude in Chrome** (la extensión emparejada con "MacBook Air de Santiago").
No sirve `curl` ni `WebFetch`: Facebook devuelve 403 a todo lo que no sea un navegador real con
sesión iniciada. Ya se probó desde la Mac y desde un servidor remoto, y las dos dan 403.

### Paso 1 — elegir los 12
Mirá todos los anuncios activos y elegí **los 12 mejores vos**, sin preguntarle a Santiago.
Los criterios que delatan al ganador, en orden:

1. **Cuánto tiempo lleva al aire** (fecha de inicio más vieja = lo están pagando porque vende).
2. **Cuántas variantes del mismo creativo** están corriendo a la vez.
3. Que sean **formatos distintos entre sí**, no 12 versiones del mismo.

### Paso 2 — bajarlos y desarmarlos
Bajá los 12 y hacé una **planilla plano por plano** de cada uno:

- segundo exacto de cada corte
- qué se ve en cada plano (encuadre, quién/qué aparece, movimiento de cámara)
- texto en pantalla: qué dice, tipografía, color, posición, cuándo entra y sale
- transiciones, efectos, zooms
- música y efectos de sonido
- en qué segundo aparece el CTA y qué dice
- la transcripción completa del audio

### Paso 3 — mostrársela a Santiago ANTES de producir
Pasale la planilla y esperá que te diga que está bien. **No produzcas nada antes de eso.**

### Paso 4 — replicar
Replicá los 12 **exactamente**: mismos planos, mismos tiempos, mismos encuadres, mismos textos
en pantalla con el mismo estilo, mismas transiciones, misma música, el CTA en el mismo lugar.

**Lo único que cambia es el guion**, adaptado a nuestra oferta. Todo lo demás se copia.

Si falta una imagen o un plano para que coincida, se genera con ApiMart o HeyGen hasta que
coincida. No se tapa el hueco con lo que haya a mano.

## Nuestra oferta

**Hígado Liviano**, para Argentina. Es un **método digital de 21 días** (qué comer, a qué hora,
qué activa la bilis). **No es el suplemento físico** que vende el competidor. Precio todavía sin
confirmar. Falta la landing y falta el producto.

## Reglas que Santiago ya marcó a los gritos. No las rompas

- **Replicá, no inventes.** Textual: *"No hagas lo que se te cante el orto. Replicalos."*
- **Ninguna visual repetida dentro de un mismo anuncio.** Nunca uses `lista[k % len(lista)]`
  para elegir b-roll: garantiza que se repita. Antes de repetir, espaciá los cortes o alargá
  los planos; si aun así no alcanza, frená y generá las visuales que faltan.
- **Cada plano tiene que tener que ver con lo que se dice en ese segundo.** En la tanda anterior
  se coló una mujer estirando los brazos en un living en un anuncio sobre el hígado. Se nota y
  arruina el video.
- **Nada de antes/después falsos.** En el kit hay `F12-espejo-antes` y `F13-espejo-despues` que
  son **dos personas distintas**. Nunca las pongas juntas en pantalla partida.
- **Nada de testimonios inventados.** No uses las fotos `17`, `18`, `19`, `23`, `24`, `38` del kit:
  serían clientas falsas con resultados. Tampoco inventes estudios médicos ni análisis de una
  persona real, ni le pongas título de médico a un avatar.
- **Máximo lo que pidió:** esta vez pidió **12** (la regla habitual es 6 por tanda, pero acá pidió 12).

## Trampas técnicas de esta máquina. Te van a morder si no las sabés

1. **🔴 `ffprobe` es un shim falso.** `~/bin/ffprobe` es un script de 4 líneas que devuelve la
   duración y nada más, sin importar qué `-show_entries` le pidas. Por eso los controles daban
   "OK" siempre. **Usá `~/bin/ffmpeg -i archivo`** y leé la línea `Stream #`.

2. **🔴 `loudnorm` deja el audio en 192 kHz** y el AAC lo guarda a **96 kHz**. Cualquier
   reproductor que asuma 48 kHz lo reproduce al doble de lento: **se escucha la primera mitad y
   el resto nunca suena**. Santiago lo reportó como *"se corta el audio a la mitad"*.
   Después de `loudnorm` va **siempre** `aresample=48000`, y el muxeo final lleva `-ar 48000 -ac 2`.
   Control obligatorio: `~/bin/ffmpeg -i salida.mp4` tiene que decir `48000 Hz`.

3. **El demuxer `concat` resuelve las rutas de la lista relativas AL ARCHIVO DE LISTA**, no al
   directorio actual. Si no van absolutas (`os.path.abspath`), falla con código 254.

4. **Verificá que el mp4 existe y pesa lo que tiene que pesar antes de decir que está listo.**
   Ya pasó una vez que se dio una tanda por terminada y no se había generado ni un archivo.

5. `zoompan` tiene un bug conocido con `d=`. Para el push-in usá
   `scale=w='W*(1.0+0.09*t/L)':eval=frame`.

## Herramientas y credenciales

- **HeyGen**: siempre **Avatar IV** ("motor 4"), 720p vertical, el modelo más barato. Avatares del
  banco, no estrenes ninguno. Avisá los créditos antes de una tanda larga.
- **Voz**: Gemini TTS, voces fijas **Sulafat** (mujer) y **Orus** (hombre). Nunca una voz nueva.
- **ApiMart** para video con IA: `https://api.apimart.ai/v1`, clave en `~/.config/apimart/env`
  (cargala con `set -a && . ~/.config/apimart/env && set +a`). Modelo `kling-v2-6`,
  US$ 0,184 por toma de 5 s. Cliente de ejemplo en
  `~/.claude/skills/mini-novela/scripts/comun.py`.
- **faster-whisper** está instalado para el `python3` del sistema. **Ojo: no lo corras con
  `python3 -I`**, porque esa bandera ignora el site-packages del usuario y no lo encuentra.

## Dónde está todo

```
~/Desktop/higado-liviano/
  anuncios/          los 6 videos viejos (están mal, son la referencia de qué NO hacer)
  work/visuales/     el kit que mandó Santiago: 20 clips + 42 fotos 9:16
  work/guion/        g1..g6.txt    guiones viejos
  work/guion_ext/    e1..e6.txt    extensiones viejas
  work/clips/        los renders de avatar de HeyGen
~/Downloads/u_6niyix0m9h-musica-de-suspense-335486.mp3.mpeg   la música que mandó
OUTPUTS/scripts-vsl/edit_higado3.py    el editor, ya con los arreglos de audio y repetición
```

Los videos viejos y sus guiones **son referencia de lo que salió mal**. Santiago dijo
*"olvidate absolutamente de todo lo que hiciste"*. Se arranca de cero desde los anuncios de él.

## Entrega

Cuando estén aprobados y renderizados, suben solos al Drive, carpeta
*Ebook Dami / Ebook Hígado Liviano (AR) / Videos terminados* (id `13WgRrtqJnXFiRxIonF0D11OykzisFqHk`),
reemplazando lo que haya. El conector corta en **10.000.000 bytes de payload base64**, o sea
**~7,4 MB de archivo**: comprimí a **6,6 MiB** con 2 pasadas y `preset slower`.

Después actualizá `WIKI/higado-liviano.md`, `changelog.md`, y hacé commit y push.

## Lo último

Santiago está podrido de que le entreguen videos mal hechos. Antes de decirle que algo está
listo, **abrilo y miralo**: sacá una tira de fotogramas cada 2 segundos y revisala con tus
propios ojos, y comprobá que el audio diga `48000 Hz`. Un control que no puede fallar no es
un control.
