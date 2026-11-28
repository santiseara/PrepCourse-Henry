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
- ⏳ Ads: analizar los ~58 de ellos (situación y guion más repetidos), hacer **uno** con Veo 3 en ApiMart (cuenta de Juan Pineiro) y esperar su corrección.

## Preguntas abiertas
- ¿Qué precio va? ¿Se mantienen los 148.223 clientas y los "8 a 11 minutos"?
- ¿Las fotos de las edades y de los "¿Te gusta o no?" (ropa de Tai Chi) quedan, o se pasan a algo más japonés?

## Relacionado
[[tai-chi-fit]] · [[quizzes-reglas-de-armado]] · [[apimart]] · [[guiones-y-anuncios]]

## Fuentes
- Conversación del 2026-11-28 · Biblioteca de anuncios, página `321291277727767`
- `https://test.caminata-oriental.com/` (`app.js`, `app.css`, `img/`)
