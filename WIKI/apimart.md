# APIMart

> Pasarela única de APIs de IA (190+ modelos de video, imagen, LLM y audio) con ~20 % de descuento sobre el precio oficial. Es la ruta de video del Manual de Edición IA ([[skills-launch-expert]]): wan2.7-r2v con voz fija, Omni Flash y Grok Imagine. Instalada en el segundo cerebro el 4/11/2026.

## Cómo quedó instalada

- **Cuenta:** la de Santiago, entrando con Google (creada el 4/11/2026, 10:36).
- **Clave:** la clave por defecto del sitio (`google_132885's initial token`), cuota ilimitada y acceso a todos los modelos. Guardada en `~/.config/apimart/env` con permisos 600. **No está en el repo ni se imprime nunca.**
- **Cliente:** `scripts/apimart.sh` en este repo. Para llamarlo corto, agregá a `~/.zshrc`:
  `alias apimart='~/PrepCourse-Henry/scripts/apimart.sh'`
- **Saldo al instalar: US$0,00.** Sin créditos la API devuelve 402 y no genera nada. Hay que cargar en https://apimart.ai/es/pricing (eso lo hace Santiago, no Claude).

## Comandos

```
apimart saldo                                            créditos disponibles
apimart avatar <foto_url> <voz_url|-> "<texto>" [seg] [out.mp4]   wan2.7-r2v, cara y voz fijas
apimart broll "<prompt>" [seg] [out.mp4]                 grok-imagine-video, el más barato
apimart video body.json                                  body crudo a /v1/videos/generations
apimart tarea <task_id>                                  estado de una tarea
apimart esperar <task_id> [out.mp4]                      espera y baja con curl -C -
```

## La API

- **Base:** `https://api.apimart.ai/v1` · auth `Authorization: Bearer <clave>` · RPM 500.
- **Video (asíncrono):** `POST /v1/videos/generations` → el id sale en `data[0].task_id`; después `GET /v1/tasks/{task_id}` hasta `status: completed` y el video en `data.result.videos[0].url[0]`.
- **Los links de video caducan** (72 h en Omni, 24 h en otros): bajar siempre el mp4 al disco apenas termina.
- **Las tareas que fallan no se cobran.** Las que salen bien se cobran por segundo de salida.
- Ejemplo real de wan2.7-r2v:

```bash
curl -X POST https://api.apimart.ai/v1/videos/generations \
  -H "Authorization: Bearer $APIMART_API_KEY" -H "Content-Type: application/json" \
  -d '{"model":"wan2.7-r2v",
       "prompt":"El personaje de image 1 habla a cámara, plano selfie, cámara en mano",
       "image_with_roles":[{"url":"https://.../cara.jpg","role":"reference_image","reference_voice":"https://.../voz.mp3"}],
       "duration":5,"resolution":"720P","size":"9:16"}'
```

## Modelos y precios (4/11/2026, precio oro con el 20 % ya aplicado)

| Modelo | Para qué | Precio |
|---|---|---|
| `wan2.7-r2v` | avatar que habla con **cara y voz fijas** (`reference_voice`), 2-15 s, 9:16 | **US$0,0664/s** en 720P · US$0,1096/s en 1080P |
| `grok-imagine-video` | **B-roll mudo**, lo más barato | US$0,04/s |
| `gemini-omni-1.1-flash` | avatar/video multimodal, primer y último cuadro, edición y extensión | US$0,0296/s en 360P · US$0,088/s en 720P · US$0,132/s en 1080P |
| `wan2.7-videoedit` | limpiar subtítulos o personas de un clip | máx. 10 s |
| `kling-v4` | B-roll de calidad (nunca con texto en pantalla) | US$0,14/s |
| `wan3.0-video` | clips largos, 2-30 s, referencias de imagen/video/audio | US$0,1315/s |
| `seedance-2.5` | audio + video, hasta 30 s | US$0,216/s |

Niveles Platino y Diamante bajan ~5 % y ~10 % más. El catálogo completo está en https://apimart.ai/es/model

## Qué cambió respecto al manual

- **wan2.7-r2v sigue vivo** y es la ruta de avatar con voz fija, pero ahora cuesta **US$0,066/s** (el manual decía ~US$0,06).
- **Omni Flash subió**: el manual anotaba ~US$0,036/s y hoy 720P son US$0,088/s. En **360P son US$0,0296/s**, que es el precio que el manual recordaba; para storyboard conviene 360P y recién después subir.
- Aparecieron **Wan 3.0 / 3.0 Prime** (hasta 30 s) y **Seedance 2.5**, que no estaban cuando se escribió el manual.

## Las skills de video la usan por variable de entorno (8/11)

Las tres skills de [[skills-de-video-ia]] (`antes-despues-ia`, `mini-novela`, `fruti-novela`) generan todo por ApiMart y la buscan en la variable **`APIMART_API_KEY`** — que es exactamente el nombre que ya tiene `~/.config/apimart/env`. Solo falta que la shell la exporte:

```bash
echo 'set -a; . ~/.config/apimart/env; set +a' >> ~/.zshrc && source ~/.zshrc
```

También aceptan `KIE_API_KEY` como hosting público de imágenes y voces; sin ella usan catbox.moe, que es gratis. Esas skills usan **Veo 3.1 Fast** (US$0,13 la toma de 8 s) y **Hailuo 2.3**, dos modelos que no están en la tabla de arriba.

## ApiMart hostea los archivos: no hace falta KIE ni catbox (11/11)

Los modelos piden la foto y la voz por **URL pública**, y la skill `antes-despues-ia` las sube con `KIE_API_KEY`. No hace falta: **ApiMart tiene su propio almacenamiento**, que es además el proveedor que después procesa el archivo.

```
POST https://api.apimart.ai/v1/uploads/images?retention_days=3   (JPEG/PNG/GIF/WebP, 30 MB)
POST https://api.apimart.ai/v1/uploads/audios?retention_days=3   (MP3/WAV/M4A, 15 MB)
POST https://api.apimart.ai/v1/uploads/videos?retention_days=3   (MP4/MOV/WebM, 50 MB)
-F file=@archivo    ·    la URL pública vuelve en el campo `url` de la raíz
```
- **Gratis hasta 2000 archivos cada 72 h** con la retención de 3 días (la cuota se ve en el panel).
- El cliente está en `~/Desktop/dancego/anuncios/ia/subir.py`: deja la URL cargada en `subidas.json`, que es de donde lee `comun.subir()` de la skill. Con eso, **las skills de video corren sin KIE y sin hosting de terceros**.
- **El saldo real se lee en `GET /v1/user/balance`** (`remain_balance` en dólares). El panel muestra *credits*, que son **dólares × 10**: 213,75 credits = US$21,38.
- **wan2.7-r2v: la muestra de `reference_voice` no puede pasar de 10 s.** Con 11 s la tarea falla con `duration should be at most 10s` — se devuelve el dinero (`billing_status: refunded`), pero se pierden los minutos.

## Preguntas abiertas

- **Costo real medido el 11/11:** 3 ads de 22-26 s con 4-5 escenas cada uno (8 imágenes con gpt-image-2 + 18 tomas de wan2.7-r2v en 720P, con 3 regeneraciones) = **US$8,63**. O sea ~US$2,90 por ad.
- ¿La voz sigue saliendo de Google AI Studio (Sulafat/Orus) y se pasa como `reference_voice`, o se prueba la voz propia de Omni?
- Falta probar el flujo de punta a punta: sin créditos ni `GET /v1/models` responde.

## Relacionado

[[ugc-y-video-generativo]] · [[skills-launch-expert]] · [[skills-de-video-ia]] · [[vsl-reglas-de-armado]] · [[ia-en-el-flujo-de-trabajo]]

## Fuentes

- https://apimart.ai/es/keys · https://apimart.ai/es/model/wan-2-7-r2v · https://apimart.ai/es/model/gemini-omni-1-1-flash · https://docs.apimart.ai
- RAW/2026-11-03-skills-launch-expert/01-edicion-ia.md
