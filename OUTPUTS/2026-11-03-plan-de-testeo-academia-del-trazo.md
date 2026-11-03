# Plan de testeo — Academia del Trazo (AR) — 2026-11-03

Modelado de Academia de Dibujo Creativo / Universo Creativo. Análisis completo en
`OUTPUTS/2026-11-03-analisis-academia-dibujo-creativo.md`.

## Lo que se copia y lo que no

| | Ellos | Nosotros |
|---|---|---|
| Formato de creativo | Voz en off femenina + b-roll de manos dibujando, 9:16, subtítulos, piano, 40–57 s | **Igual.** Regla de oro: no se cambia el formato que le funciona al que modelás |
| Mecanismo | "El talento no existe, existe el método" (4 de 9 ads) | **Método de las 3 Capas** (forma → volumen → piel). Propio, concreto y demostrable |
| Promesa | 21 días | 21 días (validada) |
| Ángulos | Talento, contrafáctico, miedo, edad | **Cuaderno abandonado, copiar vs. ver, regalo, 20 minutos sin pantalla, día 1 vs día 21** |
| Descuento en el video | "50% OFF" dicho en el audio | **Fuera.** Sin precio y sin porcentaje en el ad |
| Landing | Hero de características, sin dolores, sin bonus, 2 bundles, garantía 7 días | Promesa con número, dolores, mecanismo, bonus x4, un solo producto, garantía 30 días |
| Precio | $16.856 / $19.921 ARS en dos bundles | **$16.990 ARS**, uno solo |
| Ahorro | "50% de descuento" | "Te ahorrás $47.410" |

## Tanda 1 — 6 videos (3/11)

Formato idéntico para los seis: **voz en off mujer (Sulafat, speed 1.30) + clips de TikTok de manos dibujando** (nada de fotos fijas ni stock), subtítulos palabra por palabra, piano suave, 9:16, 60–70 s, placa final sin precio.

| Nombre en Meta | Archivo | Dur. | Ángulo | Qué testea |
|---|---|---|---|---|
| 3/11 - 1 | `ADT-V1-las-tres-capas-calma.mp4` | 42 s | Las 3 capas | El mecanismo propio. Es el que define si el diferencial se entiende |
| 3/11 - 2 | `ADT-V2-el-cuaderno-en-el-cajon-calma.mp4` | 45 s | El cuaderno en el cajón | Dolor de abandono + plan de 21 días como solución |
| 3/11 - 3 | `ADT-V3-copio-bien-de-la-nada-no-calma.mp4` | 46 s | Copio bien, de la nada no me sale | Objeción que ellos no tocan |
| 3/11 - 4 | `ADT-V4-el-retrato-como-regalo.mp4` | 44 s | El retrato como regalo | Ángulo de uso, no de aprendizaje. Es el hueco más grande que dejan |
| 3/11 - 5 | `ADT-V5-veinte-minutos-sin-pantalla.mp4` | 45 s | 20 minutos sin pantalla | Beneficio emocional, no técnico. Abre público más joven |
| 3/11 - 6 | `ADT-V6-dia-1-vs-dia-21.mp4` | 40 s | Día 1 vs día 21 | Prueba de progreso. El formato que más retiene en nichos de habilidad |

Los seis están renderizados en `~/Desktop/dibujo-creativo/anuncios/`. Guiones completos en
`OUTPUTS/2026-11-03-guiones-academia-del-trazo.md`.

**La música es la segunda variable de la tanda.** Los tres primeros van con la cama tranquila
(`music_calma.py`: piano de fieltro + pad, 64 BPM, Am–F–C–G, sin percusión) y los tres últimos con la
cama de Herrero (`music/bed.wav`), más brillante y con más ritmo. Es la única diferencia entre los dos
grupos además del ángulo, así que si uno de los dos tercios rinde parejo mejor, la cama es candidata a
quedar fija para la oferta. Excepción consciente a la regla de una sola cama por tanda
([[guiones-y-anuncios]]), pedida por Santiago el 3/11.

**Cómo se hicieron:** voz Sulafat por API (`gemini-2.5-flash-preview-tts`, Style en voseo), `speed 1.30`
con `silence [0.26, 0.12]`, cortes de 1,9–2,9 s, pool de 101 recortes de **15 clips de TikTok** de manos
dibujando (ni una foto fija, ni stock), dos camas musicales a -8 dB repartidas 3 y 3 (ver abajo), caja de hook ocre, chips con check
y placa final ACADEMIA DEL TRAZO. Scripts: `OUTPUTS/scripts-vsl/gen_trazo_plans.py` y `edit_trazo.py`.

## Estructura en Meta (V3)

```
Campaña   V3 · Academia del Trazo · <Cuenta>     CBO · Ventas · Compra · Volumen más alto
 └─ Conjunto  3-11   → 6 anuncios (3/11 - 1 … 3/11 - 6)
```

- País: **Argentina**. Edad 18–65. Advantage+ Audience activado. Ubicaciones automáticas.
- Atribución 7 días clic + 1 día visualización. Inicio 00:00 hora Argentina.
- Título con prueba social: ⭐️⭐️⭐️⭐️⭐️ 4.9/5. CTA: **Más información**.
- Las dos descripciones del archivo de guiones se reparten 3 y 3 entre los seis anuncios: es la variable que ellos nunca testearon (dos copies para 80 ads).
- Las renovaciones entran como conjunto nuevo en la misma campaña, nunca en campaña paralela.

## Orden de trabajo

1. **Primero la landing.** No se testea creativo sobre una landing que no llega a 2,5% de comprate. Está en `~/Desktop/dibujo-creativo/landing/`.
2. Tanda 1 de 6 videos.
3. Según lo que pegue: tanda 2 con 6 hooks nuevos sobre el cuerpo ganador (renovación, no guiones nuevos).
4. Tanda de **imágenes/natives** aparte: ellos corren 42 ads estáticos contra 38 de video. Si el video paga, la imagen es el volumen barato.

## Qué mirar

- Comprate (compras ÷ visitas a la landing) **≥ 2,5–3%**. Por debajo se arregla la landing, no se sube presupuesto.
- Visita → checkout ≥ 10%. Si está bien y checkout → compra < 25%, el problema es el checkout.
- Carga = visitas a la landing ÷ clics en el enlace, objetivo 60–90%.
- Mínimo 3 días de tráfico antes de juzgar cualquier cambio en la landing.
