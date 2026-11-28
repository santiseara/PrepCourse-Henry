# Caminata Japonesa

> Oferta nueva AR: clon de **Caminata Oriental** (página "Silvia Fitness", ~58 ads activos en AR), que vende Tai Chi presentado como **"Caminata Tai Chi"** para mujeres +40 que quieren bajar de peso. Nosotros lo presentamos como **Caminata Japonesa**: mismo quiz, mismos ads hechos con IA, otro nombre. (fuente: conversación del 2026-11-28)

## Ideas clave
- **La idea de Santiago:** el Tai Chi ya vendió (ver [[tai-chi-fit]]). Caminata Oriental lo vende **sin decir "clase de Tai Chi"**: lo vende como *caminata*, comparándolo con el Tai Chi. Nosotros hacemos lo mismo con otro nombre.
- **El quiz se copia exacto** (regla del 14/11 de [[quizzes-reglas-de-armado]]: *su HTML, no nuestra plantilla*).
- **Los ads se copian en situación y guion**, pero **máximo 1:10 de habla**. Si se quiere llegar a 2 minutos como ellos, el resto es un **contador de 1 minuto** con *"Aprovechá la oferta, hacé clic abajo"*.
- **Producción:** ApiMart con **Veo 3** desde la cuenta de **Juan Pineiro**. Si no aparece esa cuenta, se abre desde Google (sesión ya iniciada); **con otra cuenta no se genera nada**.
- **Primero UN video para que Santiago lo corrija.** Hasta que no lo corrige no se sigue. Después, 6 de testeo.

## El original: Caminata Oriental
| | |
|---|---|
| Página | Silvia Fitness · id `321291277727767` · ~58 ads activos en AR |
| Quiz | `test.caminata-oriental.com`: HTML propio (`index.html` + `app.js` + `app.css`), sin plataforma |
| Checkout | `pago.caminata-oriental.com` |
| Precio | **$8.799**, tachado $39.799, 3 cuotas de $2.933 |
| Promesa | Caminata Tai Chi para bajar de peso, **8 a 11 minutos por día**, desde casa, sin impacto · 148.223 clientas |
| Producto | Reto de 28 días en 4 semanas, una clase por día, app con video y temporizador, 64 movimientos, asistencia 24/7 por Facebook |
| Bonos | Dormí mejor ($7.999) · 7 minutos para la espalda ($12.999) · Guía antiinflamatoria ($4.999), **elegidos según las respuestas** |
| Embudo | **33 pantallas → oferta directo, sin VSL** |

**Stack que NO se copia:** su pixel `27539384562427720`, su `api/track.php` (analítica propia), su `quiz_session` en el checkout y el `sessionStorage` que retomaba el paso.

## Cómo se armó el quiz (28/11)
- `curl` al `index.html` → `app.js` con el array de pasos en texto plano (escapes `\xE9` y `\u{1F381}`, que se decodifican antes de reemplazar) → 55 imágenes en `img/<clave>.webp`.
- **Script:** `OUTPUTS/scripts-quiz/build_caminata_japonesa.py <work/orig> <imagenes> <salida.txt>`: 18 pares que fallan si no matchean, barrido de rastros (`Tai Chi`, `Oriental`, su dominio, su pixel), imágenes embebidas como blob (regla del 16/11), sin `loading="lazy"`, arranque siempre en la portada.
- **Checkout relativo (`/checkout`)** hasta que Santiago pase el real. El motor hacía `new URL(v.checkoutUrl)`, que **revienta con una URL relativa**: se parchea a `new URL(v.checkoutUrl, location.href)`. Se pone por env: `CHECKOUT=https://… PIXEL_ID=… python3 build_caminata_japonesa.py …`.
- **7 imágenes con la marca vieja, rehechas con Pillow y sin un crédito:** el logo (su ícono + "Caminata / Japonesa" en Fraunces con sus dos colores), el *Tu plan incluye*, la firma de la pantalla de carga (Dancing Script), las **citas de los 3 testimonios** y **5 textos de la maqueta de la app** (girados 4° y −3° como los teléfonos).
- 🐞 **En una cita, no se retipea una línea sola: se retipea el bloque entero.** La línea nueva con Inter salía más finita que las otras dos, que eran de otra tipografía. Rehecho el bloque completo con la misma fuente, queda parejo.
- **Verificado en un iframe de 390 px:** las 33 pantallas hasta la oferta, 0 errores, 0 imágenes rotas, 0 desborde (salvo 3 px en el paso del peso objetivo, que es del original), 55/55 imágenes decodificadas al cargar, y los **3 CTAs** aterrizan en `/checkout` con `utm_*` y `fbclid`.
- **Peso: 949 KB** (el tope de ImpulTienda es 1,5 MB).

## Estado
- ✅ Quiz: `~/Desktop/caminata-japonesa/landing/caminata-japonesa-quiz.txt` (+ `PRUEBA.html`) y `OUTPUTS/2026-11-28-quiz-caminata-japonesa.html`.
- ⏳ Checkout y precio: los pasa Santiago. **Hoy queda el precio de ellos ($8.799).**
- ✅ **Ad 1 «La pileta» (28/11), esperando la corrección de Santiago:** `~/Desktop/caminata-japonesa/anuncios/28-11 - 1 La pileta.mp4` (72 s de habla + 60 s de contador = 2:12, 1080x1920). Guion: `OUTPUTS/2026-11-28-caminata-japonesa-guion-1-la-pileta.md`. Proyecto: `~/Desktop/caminata-japonesa/work/v1/`.
- ⏳ Los otros 5 de la tanda, **recién después de su corrección**.

## Los ads del original (despiece del 28/11)
- **53 ads activos levantados, 43 con video, todos creativos distintos** (ninguno duplicado), casi todos de **80 a 250 s**. Se bajó y transcribió una muestra de 10 (los de más impresiones).
- **La fórmula, en 4 de los 5 largos:** escena de **humillación con fecha** (la mamá de una amiga dice que mejor no vaya a la pileta · el ex va a estar en la fiesta · el ex va a la graduación de la hija con la novia nueva · "ese vestido no es para tu cuerpo") → **"Dame 28 días. El lunes arranco el reto de Caminata Tai Chi"** → **diario frente al espejo** Día 1 / 7 / 14 / 21 / 28 con placa **"DÍA N de 28" + barra de progreso** arriba y la misma mujer adelgazando → "Tocá el enlace de abajo" → (a veces) la llegada al evento → **contador rojo de 1 minuto** "APROVECHÁ AHORA MISMO · HACÉ CLICK EN MÁS INFORMACIÓN".
- **El diario es un cuerpo fijo que repiten casi palabra por palabra** en todos ("Tengo 52 años, dos rodillas que se quejan y cero ganas de gimnasio… Día 7: subí la escalera del tren… Día 14: me entró la calza… Día 21: me vi en una vidriera… Día 28: lo terminé"). **Lo que rota es la escena de humillación.** Igual que [[the-3d-method]]: cuerpo validado, hook nuevo.
- Otros formatos que corren: chica en la playa con la amiga, señora en la cocina con planilla de altura y peso, "la app de Caminata Oriental es gratis" con cartel, y placas de "último día gratis".
- Prometen **"bajé 14 kilos"**: nosotros **sin número de kilos** (políticas de Meta, regla de la skill `mini-novela`).

## Cómo se hizo el ad 1 (28/11)
- **ApiMart con la cuenta de Juan Piñeiro**: clave guardada en `~/.config/apimart/juan.env` (600, fuera del repo), sacada del panel con su sesión de Chrome. ⚠️ **La clave vieja de `~/.config/apimart/env` es de OTRA cuenta** (google_132885, US$ 3,81): no se usa para esta oferta.
- Skill `mini-novela`: 5 retratos (Marta antes / mitad / después, Sofi, Graciela) + 7 escenas. **El truco de que el living no cambie entre días:** el cuadro del Día 1 se copia como "personaje" `espejo` y entra de **referencia 2** en las escenas C-F ("exactly the same living room, mirror and framing as reference 2"). Salió el mismo living en los cinco días.
- **16 tomas de `veo3.1-fast` a US$ 0,60 cada una** (no 0,13: el precio subió). Total del ad: **~US$ 10,40** (saldo de Juan: 50 → 39,63).
- 🐞 **El filtro de Veo bloqueó 4 veces** (sin cobrar): "se pone de costado para mostrar la calza", "la mira de arriba abajo" y la escena de la pileta con gente de fondo. Se destrabó con un gesto neutro, la escena **solo con las dos mujeres adultas vestidas** y la frase más suave.
- 🐞 **`verif.py` alucinó "no no no no…" sobre una toma buena** (G1): se escuchó con Whisper sin VAD, la frase estaba perfecta, y se cargó el borde a mano en `bordes.json` en vez de pagar otra.
- 🐞 **Veo dijo la última frase dos veces** (G2) y el corte del aligner cayó a mitad de la palabra ("…nata japonesa"): se transcribió cada tramo por separado y se quedó el limpio.
- Montaje: `montar_cj.py` (copia de `montar.py` con la placa **DÍA N de 28 + barra amarilla** centrada arriba), `SUBS=ad PPP=2 VEL=1.18 PAUSA=0.35`, 1080x1920. Guion contra audio **0,997**. Contador: `contador.py` (Pillow, 60 cuadros de 1 s).

## Preguntas abiertas
- ¿Qué precio va? ¿Se mantienen los 148.223 clientas y los "8 a 11 minutos"?
- ¿Las fotos de las edades y de los "¿Te gusta o no?" (ropa de Tai Chi) quedan, o se pasan a algo más japonés?

## Relacionado
[[tai-chi-fit]] · [[quizzes-reglas-de-armado]] · [[apimart]] · [[guiones-y-anuncios]]

## Fuentes
- Conversación del 2026-11-28 · Biblioteca de anuncios, página `321291277727767`
- `https://test.caminata-oriental.com/` (`app.js`, `app.css`, `img/`)
