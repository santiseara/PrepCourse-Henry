"""Silvia Fitness · Adiós Panza · tanda 1 (2026-11-16). Clon de la edición y los guiones de Belu Fitness.
Un video por escena: A=V1 déficit (cocina) · B=V2 a los 40 (living, cuerpo entero) · C=V3 espejo (parque)
D=V4 gimnasio (respuesta a comentario) · E=V5 principiantes (comentario + mate) · F+G=V6 mudo (sentadillas arriba, mate abajo).
Sin testimonios inventados ni cifras de kilos (Manual de Edición IA, sección 13)."""

ACENTO = ("Rioplatense Spanish from Buenos Aires with voseo (say 'acá' never 'aquí', 'vos' never 'tú', 'tenés' never 'tienes') "
          "and natural Argentine porteña intonation, fast and energetic like an Instagram reel")
ESTILO = ("Realistic candid vertical smartphone selfie video of a real fitness coach, first-person selfie POV, the phone is NOT visible, "
          "she looks straight into the lens")

PERSONAJES = {"silvia": "(foto propia)"}

SIL = ("Keep the exact face, freckles, honey-brown wavy hair in a messy high ponytail, gold hoop earrings and athletic body of the woman "
       "in reference 1.")
ESCENAS = {
    "A": ("Morning, a bright Argentine apartment kitchen with white curtains and a light marble counter with a plate of sliced fruit "
          "(banana, orange, strawberries) and a bowl of oatmeal. The woman (ref 1) wears a pink sports bra and taupe high-waisted leggings, "
          "stands behind the counter holding half a peeled banana, selfie framing from the waist up, looking into the lens, phone not visible. "
          + SIL, ["silvia"]),
    "B": ("A bright Argentine apartment living room with long white curtains, wooden floor, a light grey sofa and a dark yoga mat. "
          "The woman (ref 1) wears a black sports bra, black high-waisted leggings and white sneakers, stands on the yoga mat, full body "
          "visible from head to sneakers, filmed by a phone leaning on the floor a few meters away, smiling at the camera. " + SIL, ["silvia"]),
    "C": ("Late afternoon in a tree-lined park in Buenos Aires with tall plane trees and a dirt path. The woman (ref 1) wears a black sports "
          "bra and black high-waisted leggings, selfie framing from the waist up while walking toward the lens, natural daylight, phone not "
          "visible. " + SIL, ["silvia"]),
}

VOZ = {"S": ("F", "Silvia, a 40-year-old Argentine fitness coach with a warm, confident, energetic medium-pitched porteña voice")}
POS = {k: {"S": "the woman"} for k in "ABCDE"}

TOMAS = [
    # V1 · déficit (ad01 de Belu)
    ("A1", "A", "She holds half a banana and talks to the lens with a knowing look, gesturing with the banana.",
     [("S", "confident", "Si no estás en déficit calórico, nunca vas a bajar de peso, aunque entrenes dos horas por día.")]),
    ("A2", "A", "She points at the plate of fruit on the counter and shrugs, smiling.",
     [("S", "friendly", "Estos cambios no se logran con dietas extremas: se logran comiendo abundante, pero nutritivo.")]),
    ("A3", "A", "She counts three ideas on her fingers while talking, energetic.",
     [("S", "energetic", "Con mi método de entrenamiento, alimentación y mentalidad antiabandono, vas a lograrlo vos también.")]),
    ("A4", "A", "She leans a bit closer to the lens and gestures with her free hand, enthusiastic.",
     [("S", "enthusiastic", "Te llevás cinco rutinas distintas por semana, con planillas y videos de cada ejercicio, para tu nivel.")]),
    ("A5", "A", "She gestures toward the plate of fruit while talking, smiling.",
     [("S", "cheerful", "Y además tenés la grilla de comidas, la guía para aprender a comer, recetas ricas y muchísimo más.")]),
    ("A6", "A", "She raises her eyebrows with a challenging smile and points down with her finger.",
     [("S", "excited", "¿Estás lista para un cambio real? Sumate hoy, que está con la mitad de precio y bonos de regalo.")]),
    # V2 · a los 40 (ad06 de Belu)
    ("B1", "B", "She lifts the hem of her sports bra slightly and touches her toned abs proudly, then opens her arms, smiling.",
     [("S", "playful, challenging", "¿Quién te dijo que a los cuarenta no podés tener el abdomen así?")]),
    ("B2", "B", "She does two quick bodyweight squats on the mat and then talks, slightly out of breath, gesturing.",
     [("S", "energetic", "Veinte o treinta minutos, tres o cuatro veces por semana desde casa, alcanzan si el método es bueno.")]),
    ("B3", "B", "She walks two steps toward the camera, gesturing with both hands.",
     [("S", "convinced", "Con mi método, bajar la panza desde tu living en cuatro semanas es más que posible.")]),
    ("B4", "B", "She counts on her fingers while talking, standing on the mat.",
     [("S", "enthusiastic", "Cinco rutinas distintas por semana, con videos de cada ejercicio y adaptaciones para cada nivel.")]),
    ("B5", "B", "She mimes eating with her hand and smiles, relaxed.",
     [("S", "friendly", "Más la grilla de comidas repetible, la guía para aprender a comer y recetas saludables.")]),
    ("B6", "B", "She puts her hands on her hips, smiles and points at the camera.",
     [("S", "excited", "¿Estás lista para llegar al verano con el cuerpo que soñás? Sumate hoy y llevate nueve bonos de regalo.")]),
    # V3 · espejo (ad07 de Belu)
    ("C1", "C", "She walks along the park path talking to the lens, gesturing with her free hand.",
     [("S", "dreamy, warm", "Imaginate cómo serían tus días si te levantaras y realmente te gustara lo que ves en el espejo.")]),
    ("C2", "C", "She keeps walking and nods, convinced.",
     [("S", "convinced", "Con mi plan de cuatro semanas de entrenamiento y alimentación, es más que posible, y desde tu casa.")]),
    ("C3", "C", "She stops walking and counts on her fingers.",
     [("S", "enthusiastic", "Te llevás cinco rutinas por semana, con planilla y video de cada ejercicio, en nivel inicial, intermedio o avanzado.")]),
    ("C4", "C", "She gestures with her open hand as if listing things, smiling.",
     [("S", "cheerful", "La grilla de comidas, recetas saludables, rutinas de abdomen para diástasis y mucho más.")]),
    ("C5", "C", "She stops walking, smiles widely and nods at the lens.",
     [("S", "excited", "¿Estás lista para un cambio de verdad? Sumate hoy y llevate los bonos de regalo.")]),
    # V4 · gimnasio, respuesta a comentario (ad11 de Belu)
    ("D1", "D", "She tilts her head with an amused, slightly ironic smile, gesturing with her free hand.",
     [("S", "amused, ironic", "La gente dice: tengo que cambiar mi cuerpo, tengo que empezar el gimnasio. ¿Para qué, chicas?")]),
    ("D2", "D", "She puts her hand on her chest, proud and sincere.",
     [("S", "sincere", "Yo el mejor cuerpo lo tuve entrenando desde casa, sin máquinas y sin pesas enormes.")]),
    ("D3", "D", "She shakes her head, then nods firmly and points at the lens.",
     [("S", "firm, motivating", "El gimnasio no es ni el problema ni la solución. El método sí. Así que sumate y arrancá hoy.")]),
    # V5 · principiantes, respuesta a comentario
    ("E1", "E", "She holds the mate gourd and talks to the lens, nodding.",
     [("S", "warm", "Me preguntan si sirve para las que nunca entrenaron. Sí, y está pensado justo para eso.")]),
    ("E2", "E", "She gestures with her free hand while holding the mate.",
     [("S", "reassuring", "Cada rutina tiene nivel inicial, intermedio y avanzado. Arrancás tranqui, en tu living y sin elementos.")]),
    ("E3", "E", "She counts on the fingers of her free hand, smiling.",
     [("S", "friendly", "Y no es una dieta imposible: son catorce días de desayuno, almuerzo, merienda y cena, sin pasar hambre.")]),
    ("E4", "E", "She smiles and points down with her free hand.",
     [("S", "excited", "Para arrancar hoy mismo, tocá acá abajo, que todavía está con la mitad de precio.")]),
    # V6 · mudo (ad03/ad12 de Belu): sentadillas arriba, mate abajo
    ("F1", "F", "She does slow controlled bodyweight squats on the yoga mat, then speeds up into jump squats, breathing, focused.", []),
    ("G1", "E", "She takes a slow sip from the metal straw of the mate gourd and looks into the lens with a confident knowing smile, nodding slightly.", []),
]
