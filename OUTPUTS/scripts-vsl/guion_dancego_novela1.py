# -*- coding: utf-8 -*-
"""Dance Go · novela 1 «Dame tres semanas» — copia del ad de 3:16 de Coach Ana Belen (Metodo 21-7).
Misma arquitectura: cadena de vinetas domesticas con humillacion + salto de tres semanas,
contagio en la calle, la animada 3D, la cafeteria (nucleo de venta) y el cierre con placa.
"""

ACENTO = ("Rioplatense Spanish from Buenos Aires with voseo (say 'acá' never 'aquí', 'vos' never 'tú', "
          "'tenés' never 'tienes') and natural Argentine porteño intonation, relaxed everyday speech")
ESTILO = ("Realistic candid vertical smartphone video, slightly shaky handheld, imperfect framing, real ordinary Argentine "
          "setting, natural light, no color grading, ordinary real-looking people, little or no makeup, no studio light")

FOTO = ("Full-body portrait, photorealistic, ordinary real-looking person, natural uneven skin texture, almost no makeup, "
        "candid snapshot taken with a phone, soft daylight, plain neutral background. No text, no logos, no watermark.")
CUADRO = ("Vertical 9:16 photorealistic still frame grabbed from a candid handheld smartphone video, real ordinary Argentine "
          "setting, slightly imperfect framing, natural light, mild phone-camera noise, no color grading. "
          "Keep the exact face, body, hair and clothes of the people in the reference images. "
          "Anatomy must be correct: two arms and two hands per person, hands fully visible or clearly out of frame, "
          "no extra limbs. Any phone that is recording must be clearly held by a hand or propped on a visible surface. "
          "No text, no subtitles, no logos, no watermark.")

PERSONAJES = {
    # vinetas A-F: Sandra
    "sandra_antes": "An Argentine woman aged 45, dark brown hair tied back in a low ponytail, overweight with a round belly and heavy arms, tired ordinary face, wearing a loose grey t-shirt and black leggings.",
    "sandra_despues": ("sandra_antes", "now clearly slimmer with a flat stomach and slimmer arms, upright confident posture, brighter rested face, same low ponytail, wearing the same loose grey t-shirt, which now hangs loose on her, and the same black leggings"),
    "lucia": "An Argentine teenage girl aged 17, long straight dark hair, slim, wearing an oversized green t-shirt and jeans, holding a phone in one hand.",
    "ex": "An Argentine man aged 50, grey short hair, slim build, wearing a grey zip-up jacket and jeans.",
    "novia": "An Argentine woman aged 35, very slim and athletic, long dark hair in a high ponytail, wearing a black sports bra and black leggings, expensive sneakers.",
    "marido": "An Argentine man aged 48, short dark hair, slightly overweight, wearing a plain navy t-shirt and shorts, holding a phone in one hand.",
    # vinetas G-H: otras mujeres
    "ciclista": ("sandra_despues", "same woman now wearing a black sleeveless cycling top, black shorts and a dark cap, riding a bicycle"),
    "amiga_bici": "An Argentine woman aged 47, blonde hair in a messy bun, overweight, wearing a pink t-shirt and grey leggings, riding an old bicycle, out of breath.",
    "kiosquera": "An Argentine woman aged 40, dark hair tied back, wearing a black work apron over a t-shirt, standing behind a small neighbourhood kiosk counter.",
    "clienta_kiosco": "An Argentine woman aged 44, curly brown hair, slightly overweight, wearing a black t-shirt and jeans, a small backpack on one shoulder.",
    # cafeteria
    "camarera": "An Argentine woman aged 30, dark hair in a bun, slim and fit, wearing a white t-shirt under a black apron, behind a cafe counter.",
    "clienta_cafe": "An Argentine woman aged 50, wavy blonde-dyed hair to the shoulders, overweight, wearing a cream t-shirt, sitting at a cafe counter.",
}

ESCENAS = {
    "A": ("Late afternoon on the pavement outside an Argentine sports club, parked cars and trees behind. On the left the overweight "
          "woman with the ponytail (ref 1) sits on a low wall; in the middle the teenage girl (ref 2) stands holding her phone; "
          "on the right the grey-haired man (ref 3) and the very slim athletic woman in the black sports bra (ref 4) walk in together, "
          "clearly separated from the others, each person with both hands visible.",
          ["sandra_antes", "lucia", "ex", "novia"]),
    "B": ("Late afternoon on the same pavement outside the same Argentine sports club, same parked cars and trees. On the left the "
          "now slimmer woman with the ponytail in the loose grey t-shirt (ref 1) stands relaxed; on the right, a step away from her, "
          "the very slim athletic woman in the black sports bra (ref 2) stares at her, both arms at her sides.",
          ["sandra_despues", "novia"]),
    "C": ("Evening in a real ordinary Argentine living room, a TV on showing a dance class, a rug on the floor. In the middle of the "
          "room the overweight woman in the grey t-shirt (ref 1) dances facing the TV, seen from behind and to the side; in the "
          "doorway on the left, several steps away, the slightly overweight man in the navy t-shirt (ref 2) stands holding his phone "
          "in one hand.",
          ["sandra_antes", "marido"]),
    "D": ("Morning in a real ordinary Argentine kitchen with a kettle on the stove and a window. On the right the slimmer woman in the "
          "grey t-shirt (ref 1) dances on her own next to the counter; on the left, separated by the counter, the teenage girl (ref 2) "
          "leans in the doorway holding a mug with both hands.",
          ["sandra_despues", "lucia"]),
    "E": ("Afternoon in a modest Argentine backyard with a small above-ground pool and plastic chairs. On the left the overweight woman "
          "(ref 1) stands holding folded towels; on the right, two steps away, the teenage girl (ref 2) stands with her arms crossed, "
          "looking down.",
          ["sandra_antes", "lucia"]),
    "F": ("Afternoon in the same modest Argentine backyard with the same small pool and plastic chairs. The now slimmer woman (ref 1) "
          "stands by the pool in a dark one-piece swimsuit, relaxed and smiling; on the right, a few steps away, the teenage girl (ref 2) "
          "holds up a phone with both hands, framing a photo of her.",
          ["sandra_despues", "lucia"]),
    "G": ("Morning on a quiet Argentine suburban street with low houses and trees. In the foreground on the left the fit woman in the "
          "black cycling top and cap (ref 1) rides a bicycle; behind her on the right, a few metres back, the overweight blonde woman "
          "in the pink t-shirt (ref 2) pedals an old bicycle, out of breath. Both women hold their own handlebars with both hands.",
          ["ciclista", "amiga_bici"]),
    "H": ("Night inside a small Argentine neighbourhood kiosk, shelves of sweets and cigarettes behind the counter. Behind the counter "
          "on the right the woman in the black apron (ref 1) looks at her phone resting on the counter; in front of the counter on the "
          "left, on the other side, the curly-haired woman with the backpack (ref 2) leans in to talk to her.",
          ["kiosquera", "clienta_kiosco"]),
    "I": ("A 3D animated Pixar-style young woman with big expressive eyes standing in a bright stylised kitchen, soft cartoon lighting, "
          "glossy render, full body, wearing a pink sports top and black shorts, round belly, looking at the camera.",
          []),
    "J": ("Daytime inside a small Argentine specialty coffee shop with a marble counter, espresso machine and chalkboard menus. Behind "
          "the counter on the right the slim woman in the white t-shirt and black apron (ref 1) faces the camera; in front of the "
          "counter on the left, seen from behind over her shoulder, the overweight blonde woman in the cream t-shirt (ref 2) sits on a "
          "stool.",
          ["camarera", "clienta_cafe"]),
    "K": ("Evening in a real ordinary Argentine living room with a TV on showing a dance class. The slimmer woman in the grey t-shirt "
          "(ref 1) dances facing the camera, smiling, both hands visible.",
          ["sandra_despues"]),
}

VOZ = {
    "S": ("F", "Sandra, a 45-year-old Argentine woman with a medium-pitched, warm, slightly tired porteña voice"),
    "L": ("F", "Lucía, a 17-year-old Argentine girl with a light, young, casual voice"),
    "N": ("F", "the girlfriend, a 35-year-old Argentine woman with a high-pitched, sweet but condescending voice"),
    "M": ("M", "the husband, a 48-year-old Argentine man with a low, flat, resigned voice"),
    "C": ("F", "the cyclist, a 45-year-old Argentine woman with a medium-pitched, cheerful, breathy voice"),
    "B": ("F", "the friend on the old bicycle, a 47-year-old Argentine woman, out of breath, higher-pitched"),
    "K": ("F", "the kiosk woman, a 40-year-old Argentine woman with a medium-low, dry, friendly voice"),
    "Q": ("F", "the customer at the kiosk, a 44-year-old Argentine woman with a medium-pitched, chatty voice"),
    "W": ("F", "the waitress, a 30-year-old Argentine woman with a clear, confident, friendly young voice"),
    "P": ("F", "the customer at the cafe, a 50-year-old Argentine woman with a medium-low, discouraged voice"),
    "T": ("F", "the 3D animated young woman, a soft, emotional, slightly childlike Argentine voice"),
}

POS = {
    "A": {"S": "the overweight woman sitting on the low wall", "L": "the teenage girl with the phone",
          "N": "the very slim woman in the black sports bra", "M": "the grey-haired man in the jacket"},
    "B": {"S": "the slimmer woman in the loose grey t-shirt", "N": "the very slim woman in the black sports bra"},
    "C": {"S": "the woman dancing in front of the TV", "M": "the man standing in the doorway"},
    "D": {"S": "the woman dancing next to the kitchen counter", "L": "the teenage girl in the doorway holding the mug"},
    "E": {"S": "the woman holding the towels", "L": "the teenage girl with her arms crossed"},
    "F": {"S": "the woman in the dark swimsuit by the pool", "L": "the teenage girl holding up the phone"},
    "G": {"C": "the woman in the black cycling top and cap in front", "B": "the blonde woman in the pink t-shirt behind"},
    "H": {"K": "the woman in the black apron behind the counter", "Q": "the curly-haired woman in front of the counter"},
    "I": {"T": "the 3D animated young woman"},
    "J": {"W": "the woman in the black apron behind the counter", "P": "the blonde woman sitting on the stool"},
    "K": {"S": "the woman dancing in front of the TV"},
}

TOMAS = [
    # A · la novia del padre (humillacion)
    ("A1", "A", "The teenage girl looks up from her phone and leans toward the seated woman, lowering her voice.",
     [("L", "warning, quiet", "Má, llegó papá. Y trajo a la novia.")]),
    ("A2", "prev", "The very slim woman in the sports bra smiles widely at the teenage girl, then turns her head to the seated woman.",
     [("N", "sweet, condescending", "¡Qué linda tu hija! ¿Y vos? ¿Seguís ocupada?")]),
    ("A3", "A", "The very slim woman puts one hand on her own waist and looks the seated woman up and down while she talks.",
     [("N", "smug, light", "Yo voy al gimnasio cuatro veces por semana. Hay que cuidarse, sobre todo a cierta edad.")]),
    ("A4", "prev", "The seated woman stands up slowly, holds the slim woman's gaze and answers calmly before walking off.",
     [("S", "calm, defiant", "Dame tres semanas.")]),
    # B · tres semanas despues
    ("B1", "B", "The very slim woman freezes mid-step, looks the other woman up and down, blinking.",
     [("N", "stunned", "Sandra, ¿qué te pasó? Estás irreconocible.")]),
    ("B2", "prev", "The slimmer woman shrugs with a small smile and walks past her.",
     [("S", "light, proud", "Dance Go. Diez minutos por día en el living."),
      ("S", "friendly", "El test es gratis. Pasáselo a Lucía.")]),
    # C · el marido que ya la da por perdida
    ("C1", "C", "The man in the doorway raises his phone and speaks without looking up, flat.",
     [("M", "resigned, flat", "Le aviso que no vas. Como siempre.")]),
    ("C2", "prev", "The woman keeps dancing facing the TV and answers over her shoulder without stopping.",
     [("S", "breathing hard, casual", "¿A dónde no voy, según vos?")]),
    ("C3", "C", "The man counts the occasions on his fingers, tired.",
     [("M", "tired, listing", "Al cumple de mi hermana. Como el bautismo, como año nuevo, como el de tu sobrina.")]),
    ("C4", "prev", "The woman turns to face him, still moving to the music, and points at his phone.",
     [("S", "firm, cheerful", "Poné dos. Voy por el día once. Para el sábado llego.")]),
    # D · la hija en la cocina
    ("D1", "D", "The teenage girl leans in the doorway holding the mug with both hands and rolls her eyes, amused.",
     [("L", "teasing", "¿Otra vez bailando en la cocina?")]),
    ("D2", "prev", "The woman keeps dancing next to the counter and glances at the kettle.",
     [("S", "cheerful", "Diez minutos más y te dejo la cocina libre.")]),
    ("D3", "D", "The teenage girl sips from the mug and watches her mother dance.",
     [("L", "curious", "Hace tres semanas que te encuentro igual.")]),
    ("D4", "prev", "The woman stops, pulls at the waist of her jeans to show how loose it is.",
     [("S", "proud, warm", "Tres semanas justas. ¿Ves este jean? Es el que no me entraba en marzo.")]),
    # E · el cumple de la pileta (la escena cruel)
    ("E1", "E", "The teenage girl looks down at the floor, uncomfortable, and speaks quietly.",
     [("L", "uncomfortable, quiet", "Má, escuchame. La mamá de Tomás dijo que mejor no vayas al cumple de la pileta.")]),
    ("E3", "E", "The teenage girl shrugs, still looking down, and then looks up at her mother.",
     [("L", "sad, honest", "Porque el año pasado se rieron de tus fotos en malla. Perdón, preferí decírtelo yo.")]),
    ("E4", "prev", "The woman puts the towels down on a chair, lifts her chin and smiles tightly.",
     [("S", "hurt but determined", "Que me vean llegar igual. Dame tres semanas.")]),
    # F · la pileta, despues
    ("F1", "F", "The slimmer woman in the swimsuit walks to the edge of the pool and turns to the camera, relaxed.",
     [("S", "light, happy", "Dance Go. Diez minutos por día, en el living de mi casa.")]),
    ("F2", "prev", "The teenage girl holds the phone up with both hands, framing her mother, and laughs.",
     [("L", "excited", "Má, esta vez las fotos las sacás vos.")]),
    # G · la bici (contagio)
    ("G1", "G", "The blonde woman behind pedals hard, waving one hand for a second before grabbing the handlebar again.",
     [("B", "shouting, out of breath", "¡Frená! ¡Frená que no te alcanzo!")]),
    ("G2", "prev", "The woman in front slows down, looks back over her shoulder and laughs.",
     [("C", "teasing", "Bajate y caminá, como hacía yo el año pasado.")]),
    ("G3", "G", "The blonde woman catches up, braking, staring at the other woman's body.",
     [("B", "panting, amazed", "¿Qué te hiciste?")]),
    ("G4", "prev", "The woman in front pats the handlebar and answers, still pedalling slowly.",
     [("C", "cheerful", "Dance Go. Diez minutos por día y hoy el test es gratis.")]),
    ("G5", "prev", "The blonde woman stretches one hand out toward her and immediately puts it back on the handlebar.",
     [("B", "eager", "Pasámelo."), ("C", "laughing", "Alcanzame primero.")]),
    # H · el kiosco
    ("H1", "H", "The woman with the backpack leans on the counter from the customer side, confidential.",
     [("Q", "confidential", "¿Sabés qué? Te lo digo porque me caés bien.")]),
    ("H2", "prev", "She taps the counter twice with one finger while she talks.",
     [("Q", "convincing", "Hoy está gratis el test de Dance Go. Ese de los diez minutos.")]),
    ("H3", "H", "The woman in the apron picks up her phone from the counter and shows the screen for a second.",
     [("K", "dry, honest", "Yo lo tengo guardado hace un mes en el celu.")]),
    ("H4", "prev", "The customer shakes her head, smiling, and points at the phone.",
     [("Q", "warm, pushy", "Y bueno, sacalo del guardado. Son diez minutos por día.")]),
    # I · la animada 3D (confesion)
    ("I1", "I", "The 3D animated woman looks down at her own belly, then at the camera, sad.",
     [("T", "sad, confessional", "Tres años mirando el número de la balanza y llorando.")]),
    ("I2", "prev", "She opens both hands in front of her, realising something.",
     [("T", "realising", "Dance Go me enseñó que el problema no era la fuerza de voluntad.")]),
    ("I3", "prev", "She shakes her head and smiles a small honest smile.",
     [("T", "honest", "Era que odiaba todo lo que estaba haciendo.")]),
    ("I4", "I", "She shakes her head slowly, remembering, both hands open in front of her. No text appears on screen.",
     [("T", "listing, tired", "Probé el gimnasio, probé las dietas y probé caminar sola a las seis de la mañana.")]),
    ("I5", "prev", "She shrugs happily and does a tiny dance step.",
     [("T", "bright", "Y lo único que me enganchó fue bailar.")]),
    # J · la cafeteria (nucleo de venta)
    ("J1", "J", "The waitress puts a cup of coffee down on the counter in front of the seated woman.",
     [("W", "friendly", "Acá está tu café. ¿Te traigo algo para comer?")]),
    ("J2", "prev", "The seated woman shakes her head and pushes the menu away.",
     [("P", "discouraged", "No. Estoy tratando de entrar en un vestido para el casamiento de mi hija.")]),
    ("J3", "J", "The waitress leans on the counter with both hands, interested.",
     [("W", "curious", "¿Y estás haciendo algo?")]),
    ("J4", "prev", "The seated woman turns her cup slowly on the counter.",
     [("P", "defeated", "Estoy tratando, pero no me da resultado.")]),
    ("J5", "J", "The waitress tilts her head and asks carefully.",
     [("W", "pointed", "¿El plan que seguís lo armaste para tu edad y para tu nivel?")]),
    ("J6", "prev", "The seated woman looks up, confused.",
     [("P", "confused", "No, nunca lo pensé así. ¿Eso importa tanto?")]),
    ("J7", "J", "The waitress straightens up and explains with her hands.",
     [("W", "explaining", "Todo importa. Si nunca bailaste, no podés arrancar con la misma clase que alguien que baila hace años.")]),
    ("J8", "prev", "The waitress opens both hands, simple.",
     [("W", "simple", "El cuerpo responde distinto.")]),
    ("J9", "J", "The seated woman leans forward on the counter.",
     [("P", "interested", "¿Y cómo sé cuál me toca a mí?")]),
    ("J10", "prev", "The waitress points at the customer's phone resting on the counter.",
     [("W", "clear", "Hacés el test que arma el plan."), ("P", "surprised", "¿Qué test? Nunca escuché nada de eso.")]),
    ("J11", "J", "The waitress mimes answering questions on a phone with one finger.",
     [("W", "explaining", "El de Dance Go. Es un minuto: ponés tu edad y te dice con qué clases arrancar.")]),
    ("J12", "prev", "The seated woman raises her eyebrows, doubtful.",
     [("P", "doubtful", "¿Y funciona?")]),
    ("J13", "J", "The waitress steps back from the counter and opens her arms to show herself.",
     [("W", "proud, warm", "Mirá cómo estoy yo. Dos talles menos y nunca pisé un gimnasio.")]),
    ("J14", "prev", "The waitress leans back in on the counter, honest.",
     [("W", "honest", "Me funcionó cuando dejé de copiar rutinas de internet y bailé las clases que eran para mí.")]),
    ("J15", "J", "The waitress shrugs and smiles, relaxed.",
     [("W", "relaxed", "Y sigo comiendo igual, porque yo no aguanto pasar hambre.")]),
    ("J16", "prev", "The waitress looks straight into the camera and points down with one finger.",
     [("W", "warm, direct", "Tranquila. El botón de Más información está acá abajo. Entrá y respondé las preguntas.")]),
    # K · cierre
    ("K1", "K", "The slimmer woman dances facing the camera in her living room, laughing, both hands up.",
     [("S", "happy, direct", "Diez minutos por día. En tu living, sin que te vea nadie.")]),
    ("K2", "prev", "She points down at the camera with one finger, still moving.",
     [("S", "encouraging", "Mirá, el botón de Más información lo tenés acá abajo. Son unas preguntas de un minuto.")]),
]

PLACAS = {"B1": "3 SEMANAS DESPUÉS", "D1": "3 SEMANAS DESPUÉS", "F1": "3 SEMANAS DESPUÉS"}
ETIQUETAS = {}
CTA = ("Tocá en", "Más información")
