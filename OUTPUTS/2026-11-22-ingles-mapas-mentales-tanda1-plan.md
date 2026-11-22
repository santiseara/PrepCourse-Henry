# Inglés con Mapas Mentales — cómo se armó la tanda 1 (2026-11-22)

Clon argentino de **Fluente com Legenda** (`mapa.fluentecomlegenda.com`). Los 6 guiones están en
`OUTPUTS/2026-11-22-ingles-mapas-mentales-6-guiones.md` y la descripción en
`OUTPUTS/2026-11-22-ingles-mapas-mentales-descripcion.md`.

## El problema que resolvió esta tanda

El producto que modelamos es **brasileño**: el cuerpo de sus mapas está en portugués. Medido sobre 24 de
sus creativos (~1.300 segundos, OCR de Vision cuadro por segundo), quedaban **~85 segundos usables** para un
ad argentino. No alcanza para seis videos y, encima, lo que se ve es material de otro idioma.

**Decisión:** el material que se muestra en el ad es **el producto en español, dibujado por código**
(`OUTPUTS/scripts-vsl/gfx_ingles.py`), con la misma DNA que ellos muestran en sus creativos. Es la misma
salida que [[laboratorio-wow]]: cuando el producto en el idioma destino todavía no existe, el inserto se
dibuja, no se saca prestado.

## Las 15 páginas del producto (43 planos)

Cada una sale a 2160x3840 y en tres encuadres (hoja entera, mitad de arriba, mitad de abajo):

| Página | Qué muestra |
|---|---|
| `mapa_much_many` | MUCH Y MANY (A2): significado, estructura, dato rápido, error común ✗/✓, mini ejercicio |
| `mapa_was_were` | WAS Y WERE (A2): estructura, afirmativa/negativa, pregunta y respuesta corta, dato rápido, error, ejercicio |
| `mapa_have_has` | HAVE Y HAS (A1): estructura, afirmativa, negativa y pregunta, las que más se usan, error, ejercicio |
| `mapa_aeropuerto` | EN EL AEROPUERTO (A2): palabras clave, frases, **mini diálogo**, tip, error, ejercicio |
| `mapa_cuerpo` | PARTES DEL CUERPO (A1) |
| `mapa_there_is` | THERE IS Y THERE ARE (A1) |
| `bonus_frases_1` | 500 frases: tabla frase en inglés · cómo se pronuncia · traducción |
| `bonus_frases_2` | La misma tabla, tema "trabajo y estudio" |
| `bonus_ruta` | Ruta de la Fluidez: plan diario con checklist tildado |
| `bonus_phrasal` | 100 phrasal verbs |
| `bonus_expresiones` | 150 expresiones y modismos |
| `bonus_ebooks` | 82 ebooks y audiolibros (grilla de tapas) |
| `bonus_los_cinco` | Los 5 bonus juntos |
| `niveles` | A1 → C2 con la cantidad de mapas de cada nivel |
| `grilla_mapas` | La vista de volumen: 30 hojas en miniatura ("más de 300") |

**La hoja termina en y=1500 de 1920 a propósito:** los últimos 420 px quedan de fondo oscuro para que el
subtítulo quemado no tape ni una línea del material.

## El b-roll

14 clips de TikTok (`#mapasmentales`, `#apuntes`, `#impresora`, `#papeleria`, `#estudiaringles`), elegidos
**a ojo** sobre hojas de contactos: impresora escupiendo la hoja, anillados de apuntes, post-it de mapa
mental, mano escribiendo, pilas de hojas de colores. En dos se recorta el borde de arriba con `zoom`/`ybias`
para sacar la marca de agua del creador.

## Edición

- Voz **Sulafat** por API, estilo rioplatense (personaje + "no estás leyendo: estás hablando"), `speed 1.20`.
- Corte cada **~2,5 s** (más lento que un ad de b-roll puro: la hoja hay que poder leerla).
- Subtítulos Montserrat ExtraBold, 3 palabras, blancos con borde negro y la palabra que suena en amarillo,
  en la banda oscura de abajo.
- Cada página entra **anclada a la palabra que la nombra** (`aeropuerto`, `was`, `ruta`, `bonus`, `300`…).
- Primer plano fijo por video, elegido por el hook (impresora para "mirá lo que acabo de imprimir",
  anillado para "se te desparraman los apuntes").
