# The 3D Method — tanda 1 (mercado inglés): producción

Clon de **Método 3D - Juan Avalos** (`metodo3d.shop`), despiezado el 26/11/2026 sobre sus **99 ads
activos**. Guiones en `OUTPUTS/2026-11-26-guiones-the-3d-method.md`.

## Los 6 videos

| # | Hook (suyo) | Largo | Planos |
|---|---|---|---|
| 1 | Want to print something everyone asks you for? (su ad nº1 por impresiones + su cuerpo validado) | 42,4 s | 20 |
| 2 | The math behind one 3D printed ornament (su ad nº2, estacional) | 34,4 s | 16 |
| 3 | 3 mistakes every beginner makes (su formato de lista numerada) | 28,6 s | 13 |
| 4 | One piece. Nothing to glue. (los flexis) | 26,0 s | 12 |
| 5 | What would you pay for 90,000 designs? (el value stack) | 39,1 s | 18 |
| 6 | You don't have to print the hardest thing (lo de todos los días) | 26,7 s | 12 |

## Montaje (clon del suyo, medido cuadro a cuadro)

- Banner fijo de dos pastillas arriba todo el video: roja **#D81C1B** con texto blanco +
  amarilla **#FDD400** con texto negro.
- Titular de arranque: renglón 1 blanco con borde negro, renglón 2 en pastilla roja.
- Pastillas rojas numeradas (MISTAKE #1/#2/#3) y pastilla verde **#1FA14A** para el número de plata.
- Subtítulos de 3 palabras, Montserrat ExtraBold, la que suena en amarillo #FDD400.
- Barra de progreso amarilla pegada abajo. Cierre: pastilla roja INSTANT ACCESS + "Tap Learn more".
- Cortes de 1,8 a 2,5 s (promedio 2,1-2,2 s).

## Voz

Orus (hombre), estilo de tipo del Medio Oeste con tres impresoras corriendo atrás.
`gemini-2.5-flash-preview-tts`. Las 6 verificadas con Whisper: arrancan en la primera palabra del
guion y dan 190-213 ppm en crudo. V1 y V4 se rehicieron con `TTS_TEMP=0.55` porque salían a 168 y
163 Hz contra los 133-140 del resto; quedaron en 139 y 147.
El ritmo final apunta a **188 ppm** (tope de la banda del 24/11), así que el speed de cada video sale
de dividir: 0,89 / 0,90 / 1,00 / 0,99 / 0,94 / 0,97. El ganador lee a 205-213 ppm.

## Música y efectos

- **La pista que mandó Santiago**: `atlasaudio-advertising-marketing-617541.mp3`, la misma cama ya
  balanceada de The Laser Profit Vault (16/30/25/24/6 % de energía por banda), `music_db −6` con
  `duck 6`.
- Efectos de `~/SFX/alias`: pop en las pastillas, chaching en los números, ding en el cierre.

## Pool de TikTok

- 8 tags: `3dprinting`, `3dprinted`, `3dprintingbusiness`, `3dprintingbusinessideas`, `bambulab`,
  `articulateddragon`, `3dprintedchristmas`, `3dprintfarm`.
- 875 ids raspados, 817 clips bajados con tikwm, 224 pasados por el filtro denso (1 cuadro/s:
  texto, caras sobre el clip entero y bandas negras) → **88 con ventana limpia**.
- Segunda pasada a 3 cuadros/s sobre la ventana ya aprobada → 81.
- Pase a ojo (hoja de contactos de las ventanas) → 62. Se cayeron por personaje con derechos o
  marca ajena: Spider-Man (×2), Majin Buu, Mr. Krabs, Garfield, Pokémon, LEGO; más bandas negras,
  personas de cuerpo entero y planos donde no se ve el producto.
- **Lo que solo apareció en la hoja del RENDER** (regla del 23/11): un primer plano de piel, una
  figura **KAWS** y unos muñecos de **Naruto**. Pool final: **59 clips de 55 cuentas distintas**.

## Dos cosas medidas que valen para cualquier tanda

1. ⛔ **El `concat` de los cortes deja timestamps irregulares y el `overlay` DESCARTA la placa en esos
   cuadros.** Medido en V4: **21 de 780 cuadros sin banner**, en tramos de 0,2 a 0,4 s. No se arregla
   metiendo el banner como entrada propia con `-loop 1`: sigue faltando. Se arregla normalizando
   **todo a CFR antes de superponer** (`fps=fps=30:round=near,setpts=N/30/TB` en la base y
   `setpts=N/30/TB` en cada overlay, más `-fps_mode cfr -r 30` a la salida). Con eso: 0 de 1.271.
2. **Cambiar solo la capa de placas cuesta minutos.** Con `SOLO_AUDIO=1` y borrando únicamente
   `video.mp4`, `ov.mov` y `mix.wav` se reusan los cortes y el `cat.mp4`: los 6 salieron en 5 minutos
   en vez de 12. Hay que borrar `usage.json` y correr los 6 en orden para que el reparto de planos
   se reproduzca igual que en la corrida de los cortes.

## Entrega

- Drive: `Ebook Dami / Ebook The 3D Method (EN) / Videos terminados`, cada uno nombrado por el arranque
  de su hook (corrección de Santiago del 26/11: *"Poneles el nombre con los hooks"*; se habían subido
  como `26-11 - N`):
  `Want to print something everyone asks you for` · `Let me show you the math on printing Christmas
  ornaments` · `Three mistakes youre making if you just started 3D printing` · `You know those dragons
  that move like theyre alive` · `What would you pay for ninety thousand designs to print in 3D` ·
  `You dont have to print the hardest thing out there`.
- Másters sin comprimir en `~/Desktop/the-3d-method/anuncios/` como `26-11 - 1.mp4` a `26-11 - 6.mp4`
  (ahí el nombre de tanda sí va, es el que se carga en Meta).
- 🐞 El conector corta en **~5,43 MB** de archivo: el V5 a 5.447.131 bytes dio `EPROTO` cuatro veces
  seguidas y entró recién a 5.036.943. El `EPROTO` también aparece de forma intermitente en archivos
  que sí entran; se reintenta y al segundo o tercer intento pasa.
- Scripts: `scripts-vsl/edit_m3d.py`, `gen_m3d_plans.py`, `ventanas_m3d.py`, `afinar_m3d.py`,
  `vent_a_py.py`.
