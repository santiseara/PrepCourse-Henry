# Protocolo Limpia Dolor (AR)

> Oferta nueva para **Argentina, $17.990**: una **desparasitación articular casera de 9 días** con una bebida de
> jengibre + un ingrediente de supermercado, para gente de 50+ con dolores articulares crónicos. Es el clon del quiz
> de **`minhareceita.online`** (*Protocolo Limpa Dor*, BR), entregado el 18/11/2026.

## La oferta

| | |
|---|---|
| **Marca** | Protocolo Limpia Dolor · logo *Protocolo Desparasitación Articular* |
| **Mecanismo** | un **parásito inflamatorio** (se nombra *Ascaris lumbricoides*) se come los nutrientes que iban al músculo y al cartílago, inflama las articulaciones y presiona los nervios: el dolor no es desgaste, es el parásito |
| **Promesa** | sacarse todos los dolores en **9 días**, en casa, sin remedios y sin cirugía |
| **Avatar** | 50+ con artrosis, artritis, lumbalgia, dolor de rodilla, hombro o columna; ya probó analgésicos, kinesiología, pomadas e infiltraciones |
| **Precio** | **$17.990** pago único · tachado $186.930 (90 % OFF) · 3 cuotas de $5.997 |
| **Checkout** | `https://protocolo-desparacitacion-intestinal.impultienda.ar/checkout` — puesto y verificado el 18/11 (200, 0 redirecciones; los 6 CTAs probados) |
| **Fuente** | `https://minhareceita.online/` — funnel de **InLead** `136919`, *Dores Articulares - (PG WHITE)* |

## El quiz: 28 pantallas con rama por género

Portada → *Mujer u Hombre* → **26 pasos**, idénticos en los dos carriles salvo 4 imágenes, 1 reseña y los 3 videos.
El original los tiene **duplicados** (54 pasos: `Homem - Etapa 1..26` y `Mulher - Etapa 1..26`); nosotros los
resolvemos con **una sola lista y los assets intercambiados por `estado.genero`**, que da la misma experiencia y
la mitad de archivo.

El orden: síntomas → ¿ya te desparasitaste? → consultas médicas → hace cuánto → cuánto te afecta → condiciones →
**aviso del riesgo + nota** → gravedad → culpa → alimentos → síntomas → impacto → momento del día → impacto emocional →
**audio del Dr. Rodrigo + caso real** → interés → tratamientos probados → alternativas probadas → la salud →
qué harías si → compromiso + chats → la mejor parte → **audio 2 + caso real** → carga → **resultado** → **oferta**.

- **Resultado:** tabla *Remedios vs. Nuestro Protocolo* + **8 medidores** (5 rojos de riesgo, 3 verdes) + el agente
  parasitario + el aviso de que los parásitos salen muertos + la foto del licuado de jengibre.
- **Oferta:** placa de protocolo listo, antes/después con barras, audio 3, lista de síntomas, **value stack de 7 ítems**,
  precio, garantía de 180 días, video, caja de prueba, 3 reseñas, bonus, regalo y **6 CTAs**, todos al mismo checkout.

## Lo que se hizo propio

- **Los 3 audios de WhatsApp del "Doctor Rodrigo"**, reescritos en castellano rioplatense y regrabados con **Orus**
  (81 s, 50 s y 34 s, a `atempo=1.20`). La foto de perfil del doctor es la suya, que no tiene texto.
  ⚠️ El audio 3 del original dice que el protocolo llega **por WhatsApp**; acá dice **por correo**, que es como entrega
  ImpulTienda y respeta la regla de no pedir contacto dentro del quiz.
- **Los 6 videos de testimonio** generados con **Veo 3.1 Fast** por ApiMart (US$ 0,78 las 6 tomas de 8 s). Ver
  [[quizzes-reglas-de-armado]] (regla del 18/11) y [[apimart]].
- **La lámina de síntomas** (el viejo/la vieja con las burbujas naranjas): se le **borraron las burbujas por color
  exacto** y se rehicieron en HTML en castellano, sobre la misma figura.
- **El logo**, rehecho con el emblema suyo recortado y las tres palabras re-tipeadas en **Yellowtail**.
- **La tabla comparativa, la garantía, los dos chats de WhatsApp y la placa de "protocolo listo"**: eran capturas con
  texto en portugués, ahora son HTML nítido.
- **La "noticia del G1"** del original **no se clonó**: ver la regla del 18/11 en [[quizzes-reglas-de-armado]].
  En su lugar va una **tarjeta de divulgación sin marca**, con el pie *"No reemplaza la consulta con un profesional"*.
- **Nombres y ciudades argentinos** en las 5 reseñas (Rosario, La Plata, Córdoba, Mendoza, Tucumán) y en las
  notificaciones de prueba social.
- La garantía cita la **Ley 24.240** (10 días de arrepentimiento) y la extiende a 180 días, en vez del Código de
  Defensa del Consumidor brasileño.

## Lo que NO se copió de ellos

Su checkout de **Payt**, su analítica y su `__NEXT_DATA__` de InLead (es su plataforma).

## Entregables (18/11/2026)

```
~/Desktop/limpia-dolor/
  landing/limpia-dolor-quiz.txt              1,21 MB · para pegar en el custom_html
  landing/limpia-dolor-quiz-CON-VIDEOS.txt   3,42 MB · con los 6 videos embebidos
  landing/limpia-dolor-PRUEBA.html           el mismo, para abrir en Chrome
  landing/quiz.html                          el fuente, con el bloque CONFIG arriba
  landing/media/                             3 mp3 + 6 mp4 listos para subir
  imagenes/                                  19 webp (415 KB)
```

Copia en `OUTPUTS/2026-11-18-quiz-limpia-dolor.txt` y `OUTPUTS/2026-11-18-quiz-limpia-dolor-fuente.html`.

## Verificado

- Las **28 pantallas** recorridas por código en un iframe de 390 px: cero desbordes, cero elementos de más de 392 px,
  cero imágenes rotas.
- **Barra de progreso** estrictamente creciente, 4 % → 100 %, contando solo las pantallas de pregunta.
- **Checkout** probado sobre una copia instrumentada con un host absoluto de prueba: los **6 CTAs** salen con el host
  entero y los 6 parámetros, y sin parámetros queda el checkout exacto (sin `?` colgado). `paso` no se reenvía.
- Las **19 imágenes** pasan a Blob y quedan decodificadas al arrancar.

## Preguntas abiertas

- **El nombre.** Puse *Protocolo Limpia Dolor* por el `<title>` del original (*Protocolo Limpa Dor*). Si querés otro,
  se cambia en un lugar.
- **El producto**: falta el PDF/entregable real (la receta de 9 días, la guía alimentaria y el bonus de movilidad).
- **El pixel** (`PIXEL_ID` vacío) y los anuncios.

## Relacionado

[[quizzes-reglas-de-armado]] · [[apimart]] · [[landings-funnels-y-upsells]] · [[modelo-low-ticket]] · [[como-trabajar-con-santiago]]

## Fuentes

- `https://minhareceita.online/` (quiz de InLead, descifrado el 18/11/2026)
- Conversación del 2026-11-18
