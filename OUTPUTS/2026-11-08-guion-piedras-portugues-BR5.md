# Piedras aromáticas — BR5, el ad «I never» pasado a portugués

> Quinto anuncio del mismo ganador, hecho igual que BR1–BR4: **misma imagen, misma cama de audio, mismos cortes, misma duración (20,67 s)**.
> Lo único nuevo es la voz (Sulafat, brasileña) y los subtítulos en portugués, con el **mismo estilo del original** (Courier Bold, blanco con contorno negro, palabra activa en amarillo, bloques de hasta 2 líneas de 24 caracteres).

Archivo: `~/Desktop/scented-stones-ad/anuncios/portugues/SS-PT-5-nunca-quis.mp4` · fuente: `~/Downloads/i never.mp4`

## El original en inglés (leído de sus subtítulos quemados)

```
I never wanted to have a business. I was never interested in this entrepreneur, invoice, scale-it thing. I just wanted a calm extra income to cover my little pleasures. I started making scented aroma stones by chance. A year later, I still don't want a business, but I have one that pulls in $3,500 a month from my kitchen. I bought a guide from a woman named Emma for $27 on an impulse. Inside is the exact formula
```

El video original termina así, cortado en «formula», sin CTA. **Se dejó igual**, porque se pidió tal cual.

## BR5 — «Eu nunca quis ter um negócio»

```
Eu nunca quis ter um negócio. Nunca me interessei por essa coisa de empreendedora, nota fiscal, escalar. Eu só queria uma renda extra tranquila para cobrir os meus pequenos prazeres. Comecei a fazer pedras aromáticas por acaso. Um ano depois, eu continuo sem querer um negócio, mas eu tenho um que rende dezoito mil reais por mês na minha cozinha. Comprei um guia de uma mulher chamada Emma por vinte e sete reais, por impulso. Dentro está a fórmula exata
```

**En español (para que sepas qué dice):** Yo nunca quise tener un negocio. Nunca me interesó esa cosa de emprendedora, factura, escalar. Yo solo quería un ingreso extra tranquilo para cubrir mis pequeños gustos. Empecé a hacer piedras aromáticas de casualidad. Un año después, sigo sin querer un negocio, pero tengo uno que deja dieciocho mil reales por mes en mi cocina. Me compré una guía de una mujer llamada Emma por veintisiete reales, por impulso. Adentro está la fórmula exacta.

## Lo que se localizó

- **$3.500/mes → dezoito mil reais** (misma conversión que BR1–BR4, ~5,4 R$/USD, redondeada a una cifra que un brasileño diría).
- **$27 → vinte e sete reais.** Se mantuvo la cifra 27 en reales: es un precio low ticket normal en Brasil. Si la oferta en Brasil va a otro precio, se cambia una palabra y se regenera.
- **Emma se queda.** Funciona igual como nombre en Brasil y es el único dato de la historia.
- «entrepreneur, invoice, scale-it thing» → **«empreendedora, nota fiscal, escalar»**: nota fiscal es la palabra exacta del miedo brasileño a formalizarse.
- En los subtítulos las cifras van **en número** (18 mil reais, 27 reais), como el original muestra $3,500 y $27, aunque la voz las diga con todas las letras.

## Cómo se hizo

- **Nada del video se rehízo.** Se separaron los stems del fuente con demucs (`_assets/stems/htdemucs/orig5/`), se tapó el subtítulo inglés por inpaint en la franja 1368–1512 y se quemó el portugués encima.
- **Estilo medido sobre el original, no inventado:** Courier New Bold 47 px (28 px de avance por carácter, igual que el fuente), interlineado 56, baseline 1457 para una línea y 1429/1485 para dos, blanco #FFFFFF con contorno negro de 3 px y palabra activa en amarillo #EBD414. Bloque alineado a la izquierda y centrado por su línea más larga.
- **Voz:** Sulafat por API, `gemini-3.1-flash-tts-preview`, style brasileño con pedido de ritmo de propaganda. **4 tomas**: 27,20 / 25,24 / 23,64 / 26,12 s. Se descartó la b (dijo «pra» y «tá» en vez de «para» y «está») y se usó la **c**, que es la más corta y lee el guion exacto → tempo final **1,152** (las otras pedían 1,25 a 1,35).
- Palabras alineadas con el guion: **80/80**. 12 bloques de subtítulo, los mismos 12 del original.
- Script: `~/Desktop/scented-stones-ad/anuncios/portugues/work/render_never_pt.py` (copia en `OUTPUTS/scripts-vsl/render_never_pt.py`)

## Relacionado
[[internacionalizacion]] · [[scented-stones]] · [[guiones-y-anuncios]]

## Fuentes
- ~/Downloads/i never.mp4
- OUTPUTS/2026-11-07-guiones-piedras-portugues-BR1-BR4.md
