# Despiece frame por frame — los ads de Sana Pilates (AR)

> 22 videos bajados de la Biblioteca de Anuncios (página `982998884899600`), transcriptos con Whisper,
> con detección de cortes, medición de audio y de ritmo. Hecho el 2026-11-09 para construir **Origen Pilates**.
> Material en `~/Desktop/origen-pilates/anuncios/competidor/`.

---

## 1. Ficha técnica común

| Dato | Valor |
|---|---|
| Resolución de las copias | **360 × 640 (9:16)**, 30 fps, H.264 (son las copias de la biblioteca, no los masters) |
| Audio | Pico entre **−0,1 y −6,4 dBFS**, media por segundo entre −20 y −28 dB → **voz bien al frente**, cama muy abajo |
| Duraciones | 0:25 · 0:43 ×3 · 0:44 · 0:53 · 0:57 · 1:08 · 1:09 · 1:15 ×2 · 1:16 · 1:25 · 1:46 · 1:47 · 1:55 · 1:58 · 2:04 · 2:08 · 2:46 · 3:19 · 3:58 · 4:03 |
| **Ritmo de habla** | **166 palabras por minuto de mediana** (rango 138 a 190) |

⚠️ **El dato del ritmo importa.** Nuestra regla interna dice 150 ppm y el molde brasileño iba a 185. El argentino que funciona acá está en **165-175**: ni la locución acelerada de Brasil ni la lectura lenta. Los guiones de Origen Pilates se calculan a **170 ppm**.

---

## 2. Corrección sobre el supuesto de partida

**No es cierto que sus anuncios sean "casi todos con IA".** Verificado cuadro a cuadro en resolución grande:

| Pieza | Veredicto | Cómo se prueba |
|---|---|---|
| Profesora en cocina luminosa (remera coral, pelo canoso recogido, plantas y un mate en la mesada) | **IA** | La mano izquierda sale con los dedos fusionados, la pose es rígida y la piel tiene el detalle hiperreal típico del modelo. Los planos de ese bloque duran **7,36 · 7,87 · 7,50 · 8,87 · 9,86 · 8,00 s** — la firma de clips de 8 segundos |
| Presentadora sentada en sillón de oficina con biblioteca detrás | **Real** | Gesto natural, manos correctas, fondo estable, micro-movimientos de cabello |
| "Marta, 63 años" en su habitación | **Real** | Persona real filmada con celular, piso de baldosa, cama con colcha |
| Entrevista en el shopping con micrófono | **Real** | Cámara en mano, gente de fondo caminando, profundidad real |
| Clips de pilates en el piso con ventanal al atardecer | **Real / stock** | Se repiten entre ads |

**Conclusión:** su material es **mayormente real**, con **un bloque de avatar IA** en la familia educativa larga. El que sí está 100 % en IA es el competidor brasileño ([[origen-pilates]], "Calistenia Japonesa 28 Dias"), con mini-novelas 3D.

Para nosotros no cambia la decisión — los videos van con IA porque es lo que podemos producir y es el carril que ellos tienen flojo — pero sí cambia **de dónde copiamos**: el molde de IA sale del ad brasileño ya despiezado (`OUTPUTS/2026-11-04-analisis-ad-pilates-brasil.md`), no de ellos. De ellos copiamos **el guion, el ritmo y la edición**.

---

## 3. Duración de plano, por familia

| Familia | Cortes medidos | Lectura |
|---|---|---|
| **Bloque de avatar IA** (educativo largo) | **7,4 a 9,9 s** | Clips de 8 s generados y apenas recortados |
| **Mosaico de píldoras** (UGC real) | **1,5 a 4,4 s** | Micro-clips encadenados, cada uno otra mujer |
| **Entrevista en la calle** | 4 a 11 s | Plano sostenido, corte sólo en la pregunta |
| **Historia de vida** | 2,4 a 9,2 s, con un plano de 25 s | Testimonio largo + b-roll corto |
| **Diario Día 1 → Día 28** | 4 a 9,7 s | Una placa de día por plano |

Para los nuestros con Veo: **clips de 8 s** en los videos de avatar, y **cortes de 1,9 a 2,9 s** en los de voz en off (la regla de siempre).

---

## 4. Los subtítulos (el estilo exacto a copiar)

- **MAYÚSCULAS**, sans serif **bold y condensada**.
- **Blancos, con contorno negro grueso y una sombra dura abajo a la derecha.** Sin caja de fondo.
- **Una sola línea, de 2 a 5 palabras.**
- **A la altura del pecho**, no al pie del cuadro. Es la diferencia más visible con el molde brasileño.
- **Sin palabra activa en amarillo** en los bloques de avatar. El amarillo aparece sólo en las placas rojas de hook.
- En los micro-clips del mosaico con voz original cambian a **minúsculas, dos líneas, abajo**: es el "subtítulo de testimonio", distinto a propósito del "subtítulo de locución".

### Otros elementos en pantalla
- **Caja roja de hook** arriba o abajo, texto blanco con una palabra en amarillo, en itálica. Aparece en los primeros 3 planos y se va.
- **Placas de serie** en los clips de ejercicio: `3 x 15`, `3 x 12`, `ABDOMEN PROFUNDO`, en blanco con sombra.
- **Picture-in-picture arriba a la derecha**: la presentadora hablando mientras abajo corre el clip de pilates. Nunca corta la voz.
- **Placa de cierre de marca** (la única del video), fondo crema: logo de loto · *Sana Pilates (Método Asiático)* · **ÚLTIMOS CUPOS DISPONIBLES** · *Pilates Asiático para Mujeres +40* · botón redondeado **"Hacé el Quiz y Empezá Hoy"**.

---

## 5. El guion, desarmado

### 5.1 El bloque de oferta es fijo y va siempre al final
Palabra por palabra, en 14 de los 22 videos:

```
Arrancó la promoción de Sana Pilates y va a estar disponible solo hasta este viernes.
Durante estos días podés conseguir todo el programa de Pilates Asiático por solo 7.999 pesos.
```

**La escasez es de calendario, no de stock.** No dicen "quedan X lugares" en el video (eso está en la landing).

### 5.2 El banco de píldoras
Micro-clips de 5 a 10 s que se recombinan. Las que más se repiten:

| Píldora | Texto |
|---|---|
| La profe | *"Esto es lo que hacen mis alumnos todos los días, 5 minutos desde casa. Es pilates asiático, lo pueden sostener y se nota."* |
| La de 50 | *"Tengo 50 y me siento más fuerte que a los 30."* |
| El living y el mat | *"No hay gym, no hay dietas raras, todo acá en mi living y en mi mat."* |
| La de 62 | *"¿Cuántos años tenés? — Mirá, estoy vieja, 62 años. — No, pero estás muy bien, parecés mucho más joven."* |
| La de 53 | *"¿Cómo se siente tener 53? — Mejor que antes. — Te ves increíble, ¿qué estás haciendo?"* |
| La mamá sin tiempo | *"Che, ¿vos entrenás o vas al gimnasio? — No, soy mamá, laburo todo el día, no tengo tiempo."* |
| La amiga | *"Le debo todo a mi amiga Sole, que me insistió con pilates asiático."* |

### 5.3 Las aperturas que usan
1. **Pregunta de calle:** *"¿Cuántos años tenés?"* · *"Che, ¿vos entrenás o vas al gimnasio?"*
2. **Instrucción con número:** *"Cinco movimientos, ocho minutos al día. Eso es todo lo que necesitás para callarles la boca a los que te dijeron que no podías."*
3. **Dato contraintuitivo:** *"No lo sabías, pero si hacés 60 repeticiones de este ejercicio, esto te va a ayudar a firmar todo tu abdomen. Ese es el truco de las asiáticas."*
4. **Escena de pareja:** *"¿Salís? ¿Así nomás?"* (la mini-novela del marido que se va a la fiesta)
5. **Diario en primera persona:** *"Día 1. Me sentí un poco ridícula haciendo pilates sola en mi habitación, pero lo hice igual."*
6. **Presentación con edad:** *"Me llamo Marta, tengo 63 años y hoy empiezo pilates asiático en casa."*
7. **Encuentro incómodo:** *"Me encontré a mi ex marido en la cola del súper. Estaba con su novia nueva."*

### 5.4 El mecanismo, en sus palabras
> *"Después de los 40 esos músculos profundos se apagan. Por eso entrenás y entrenás y no ves ninguna diferencia en el espejo. Pero cuando se vuelven a activar, la cintura vuelve a aparecer y el cuerpo vuelve a responder como antes."*

Y el remate contra el gimnasio: *"Una hora de cardio, gimnasio todos los días, 30 series de sentadillas. Error, error, error. La mayoría de las máquinas del gimnasio en las que sufriste años ni llegan a esos músculos."*

### 5.5 La escalera de resultados
> *"El primer día sentís más energía y más ganas. En tres días los dolores del cuerpo bajan. Y en 7 días adelgazás, se te va la panza y todo el mundo te empieza a hacer cumplidos."*

El beneficio social **va último**, igual que en el molde brasileño.

### 5.6 Los CTAs que rotan
- *"Tocá acá abajo en saber más, respondé el quiz y lo tenés por 7.999."*
- *"Entrá a sanaspilates.com y armá el tuyo."*
- *"Tocá en más información y empezá hoy."*
- *"¿Estás o seguís mirando?"*
- *"Y no lo pienses tanto, porque mientras vos lo dejás para después, otra ya está arrancando."*

---

## 6. Lo que NO copiamos

| Qué hacen | Por qué no |
|---|---|
| *"Bajé 12 kilos"*, *"6 kilos menos en 28 días"*, *"del talle XL al M"* | Política de pérdida de peso de Meta. Es lo que bloqueó las cuentas en Profesional Digital |
| *"En 7 días adelgazás"* | Plazo de resultado |
| *"Si tus brazos se ven así…"*, *"mirá esta panza"* | Atributos personales en segunda persona sobre el cuerpo de quien mira |
| Clips de TV con Valeria, Pampita, Araceli, Andrea nombradas | Derechos de imagen y riesgo de rechazo |
| *"Si no sentís la cintura más firme, me cambio el nombre"* | Garantía de resultado |
| El precio dicho en el video | Regla fija: en el ad no va el número |

**Lo que sí se queda:** el mecanismo de los músculos profundos, el error del gimnasio, la escalera por días **sin cifras de peso**, la escasez de calendario, el living y el mat, los 15 minutos, "sin impacto y sin aparatos", y la placa de marca final con el CTA al quiz.

---

## 7. La receta de producción para Origen Pilates

| Pieza | Decisión |
|---|---|
| Modelo | **Veo 3.1** en [[apimart]] (`veo3.1-fast`, y `veo3.1-quality` si un clip clave sale con defectos) |
| Clip | **8 segundos**, 9:16, audio nativo con diálogo |
| Video | **6 clips = ~48 s** · guion de **135 a 140 palabras** a 170 ppm |
| Continuidad | **Misma descripción de personaje palabra por palabra en los 6 prompts** (edad, pelo, ropa, ambiente, luz, encuadre) para que se lean como jump cuts del mismo video |
| Voz | La que genera Veo en el propio clip, con acento rioplatense pedido en el prompt |
| Subtítulos | Mayúsculas bold, blanco con contorno negro y sombra, 2-5 palabras, **a la altura del pecho** |
| Placa final | La nuestra, en la paleta de Origen Pilates, con "Hacé el test de 1 minuto" |
| Control | Hoja de contactos del render + revisión de **manos, dientes, lipsync y continuidad de fondo** clip por clip |

---

## Relacionado
[[origen-pilates]] · [[estilo-de-video-ia]] · [[apimart]] · [[guiones-y-anuncios]]
