# Laboratorio Wow (clon de Laboratorium Wow)

> Infoproducto low ticket de **300 experimentos de cocina para chicos de 3 a 12 años**, en fichas PDF.
> El ganador es polaco (**Happy Kids Corner** / `laboratorium-wow.impultienda.ar`) y lo clonamos para
> **Argentina**. Tanda 1 entregada el 22/11/2026: 4 videos de voz en off + 3 estáticos.
> (fuente: Biblioteca de Anuncios de Meta y la landing del ganador, leídas el 21/11/2026)

## Ficha del ganador
| Campo | Valor |
|---|---|
| Anunciante | Happy Kids Corner (vendedor: Chino Online LLC, Delaware) |
| Mercado | 🇵🇱 Polonia |
| Landing | laboratorium-wow.impultienda.ar (misma plataforma que [[scented-stones]]) |
| Arsenal | **62 anuncios activos**: 51 estáticos y 11 videos |
| Antigüedad | el más viejo del **31/10/2026** (3 semanas corriendo) |
| Precio | **20,90 $** pago único, garantía de 30 días, sin suscripción |
| Ancla | 296 $ (el paquete sumado) · "menos de 0,20 $ por tarde" |

## La oferta, pieza por pieza
- **Plan de 30 tardes** (63 $): una ficha por tarde, de la más fácil a la más vistosa.
- **300 experimentos por edad** (42 $): 3–5, 6–8 y 9–12 años, con color de seguridad.
- **Fichas "¿Por qué?"** (30 $): 300 explicaciones en tres renglones.
- **7 regalos**: lo que tenés en la cocina (15 cosas = 8 de cada 10 experimentos) · Menos limpieza
  (40 experimentos que se limpian en 2 minutos) · Show de magia científica (40 trucos + guion y entradas) ·
  Diploma y mapa del Pequeño Científico · 3 planes por edad de 30 tardes · Aviones y cohetes de papel ·
  Inventos que salieron por error.
- **Mecanismo**: *Método Wow → ¿Por qué?* El "wow" en el primer minuto (el agua cambia de color, el volcán
  explota, el huevo flota) y recién después la explicación. El argumento central: **la tablet no es más
  interesante que vos, solo sorprende más seguido**.
- **Colores de seguridad**: 🟢 lo hace solo · 🟡 con un grande al lado · 🔴 lo hace el grande y el chico mira.
- **Garantía "¡un experimento más!"**: si después de la primera ficha el chico no pide otro, devuelven todo.

## Su comunicación (la DNA que clonamos)
1. **Abren nombrando los materiales de la cocina**, no el producto: *"Bicarbonato, vinagre, leche, colorante.
   ¿Lo tenés en la cocina?"*. Es su copy más usado: **36 de los 62 anuncios** lo llevan.
2. **Dos o tres experimentos en fila**, cada uno con su ingrediente y lo que pasa (la leche que baila con una
   gota de detergente, la pimienta que se escapa del dedo, la espuma roja que se desborda).
3. **El chico pregunta "¿por qué?" y la respuesta ya está escrita en la ficha**. Desactiva la objeción
   "yo de química no sé nada".
4. **Las cifras siempre son las mismas**: 300 experimentos · 15 cosas que ya tenés = 8 de cada 10 · 5 minutos
   de preparación · 3 pasos · de 3 a 12 años · 4 regalos (en la landing son 7).
5. **CTA suave**: *"Tocá «Más información» y elegí el de hoy"*. **Nunca dicen el precio en el anuncio.**
6. **Ángulos que rotan**: la cocina que ya tenés · la tablet · no saber química · por edad · la abuela y los
   nietos · el regalo que no llena la casa de juguetes · Adviento sin chocolate · el sábado de lluvia ·
   maestras de jardín · el quiz "¿A o B?".

## Su edición de video (medida sobre los 11 videos activos)
- 21 a 33 s, 9:16, voz en off de mujer, **sin SFX** y con la música muy por debajo.
- **Caja de hook blanca redondeada arriba**: renglón 1 negro, renglón 2 en rojo y más grande
  ("Soda, ocet, mleko: / **300 eksperymentów**"). Dura los primeros segundos.
- **Subtítulos en mayúscula, cada palabra en su propia caja**: negro sobre blanco, y la palabra que suena
  **blanca sobre negro**. Tres palabras por grupo, en el tercio inferior.
- **B-roll real de experimentos** mezclado con **insertos del producto** (la ficha del día, los colores de
  seguridad, el plan de 30 tardes), anclados a la palabra que los nombra.

## Sus estáticos
- El #1 por impresiones es una **grilla de 6 experimentos** con etiqueta crema sobre cada foto, el título
  "LABORATORIUM WOW" arriba en azul y una **barra azul abajo**: "300 EKSPERYMENTÓW + 4 PREZENTY".
- El resto rota: titular + foto grande, el antes/después de la tablet, el quiz "¿en qué vaso flota el huevo?",
  mockups de las fichas y de las páginas del producto.
- Las fotos son **generadas con IA** (cocina clara, mesa de madera, albahaca al fondo), siempre con el mismo set.

## Lo que entregamos (tanda 1, 22/11/2026)
- **4 videos** de ~30 s: `OUTPUTS/2026-11-22-guiones-laboratorio-wow-AR-tanda1.md`. Ángulos: lo que ya tenés
  en la cocina · la tablet · no hace falta saber química · la abuela y los nietos.
- **3 estáticos** réplica de los suyos, en argentino: la grilla de 6, "A cada «¿por qué?» tenés la respuesta"
  y el quiz "¿A o B?" del huevo.
- Visual: **100 % clips reales de TikTok** (36 ventanas limpias de 112 clips bajados) + los 3 insertos de
  producto dibujados por código (`gfx_wow.py`), porque el producto en español todavía no existe.
- Voz **Sulafat** por API, acento rioplatense verificado, `speed 1.20`.

## Preguntas abiertas
- ¿Ya existe la landing argentina? Los guiones y los insertos se escribieron con la landing polaca traducida.
- ¿El precio en pesos? En el anuncio no va, pero hace falta para la landing y para los OTOs.
- Backend: clonar los 4 OTOs del molde de [[scented-stones]] ([[embudo-post-compra]] / [[embudo-vsl-post-pago]]).

## Relacionado
[[guiones-y-anuncios]] · [[scented-stones]] · [[caza-de-ofertas]] · [[internacionalizacion]] · [[estilo-de-video-ia]]

## Fuentes
- Biblioteca de Anuncios de Meta, búsqueda `laboratorium-wow.impultienda.ar` (21/11/2026)
- laboratorium-wow.impultienda.ar (landing completa, 21/11/2026)
