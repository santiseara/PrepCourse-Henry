# -*- coding: utf-8 -*-
"""Dance Go · novela 2 «Agarrate del tuyo» — copia del control de 2:18 (47 dias corriendo) de Coach Ana Belen (Metodo 21-7).
Mismo molde: cadena de contagio (super, timbre, hija que se rie, bici, kiosco), la animada 3D,
la cafeteria (nucleo de venta) y el cierre. Las escenas G,H,I,J,K reusan los clips de la novela 1,
igual que hace el competidor, que repite los mismos modulos en todos sus ads.
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
    "sonia": "An Argentine woman aged 52, short dyed reddish hair, slim and energetic, wearing a flowery blouse and jeans, pushing a supermarket trolley.",
    "joven_super": "An Argentine woman aged 34, dark hair in a bun, slightly overweight, wearing a mustard t-shirt and jeans, pushing a supermarket trolley.",
    "vecina": "An Argentine woman aged 49, curly grey-streaked hair, overweight, wearing a flowered house dress and slippers, holding a tupper with both hands.",
    "sandra_antes": "An Argentine woman aged 45, dark brown hair tied back in a low ponytail, overweight with a round belly and heavy arms, tired ordinary face, wearing a loose grey t-shirt and black leggings.",
    "sandra_despues": ("sandra_antes", "now clearly slimmer with a flat stomach and slimmer arms, upright confident posture, brighter rested face, same low ponytail, wearing the same loose grey t-shirt, which now hangs loose on her, and the same black leggings"),
    "lucia": "An Argentine teenage girl aged 17, long straight dark hair, slim, wearing an oversized green t-shirt and jeans, holding a phone in one hand.",
    "ciclista": ("sandra_despues", "same woman now wearing a black sleeveless cycling top, black shorts and a dark cap, riding a bicycle"),
    "amiga_bici": "An Argentine woman aged 47, blonde hair in a messy bun, overweight, wearing a pink t-shirt and grey leggings, riding an old bicycle, out of breath.",
    "kiosquera": "An Argentine woman aged 40, dark hair tied back, wearing a black work apron over a t-shirt, standing behind a small neighbourhood kiosk counter.",
    "clienta_kiosco": "An Argentine woman aged 44, curly brown hair, slightly overweight, wearing a black t-shirt and jeans, a small backpack on one shoulder.",
    # cafeteria
    "camarera": "An Argentine woman aged 30, dark hair in a bun, slim and fit, wearing a white t-shirt under a black apron, behind a cafe counter.",
    "clienta_cafe": "An Argentine woman aged 50, wavy blonde-dyed hair to the shoulders, overweight, wearing a cream t-shirt, sitting at a cafe counter.",
}

ESCENAS = {
    "S": ("Daytime in the checkout queue of an ordinary Argentine supermarket, shelves and a conveyor belt behind. On the left the slim "
          "52-year-old woman with short reddish hair (ref 1) stands behind her trolley moving her feet in small dance steps; on the "
          "right, one trolley away, the younger woman in the mustard t-shirt (ref 2) watches her, both hands on her own trolley.",
          ["sonia", "joven_super"]),
    "T": ("Evening at the front door of an ordinary Argentine house, a corridor and a living room with a TV on behind. In the doorway on "
          "the right the slimmer woman in the grey t-shirt (ref 1) holds the door open, slightly out of breath; outside on the left the "
          "overweight neighbour in the house dress (ref 2) holds a tupper with both hands.",
          ["sandra_despues", "vecina"]),
    "U": ("Evening in a real ordinary Argentine living room, a TV on showing a dance class, a sofa on the right. In the middle of the room "
          "the overweight woman in the grey t-shirt (ref 1) dances facing the TV; on the sofa on the right, well apart from her, the "
          "teenage girl (ref 2) sits with her phone in one hand, laughing at her.",
          ["sandra_antes", "lucia"]),
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
    "O": ("F", "Sonia, a 52-year-old Argentine woman with a medium-pitched, energetic, cheerful voice"),
    "J": ("F", "the younger woman at the supermarket, a 34-year-old Argentine woman with a soft, shy voice"),
    "V": ("F", "the neighbour, a 49-year-old Argentine woman with a high-pitched, nosy, friendly voice"),
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
    "S": {"O": "the slim woman with short reddish hair behind her trolley", "J": "the younger woman in the mustard t-shirt"},
    "T": {"S": "the woman holding the door open", "V": "the neighbour in the house dress holding the tupper"},
    "U": {"S": "the woman dancing in front of the TV", "L": "the teenage girl sitting on the sofa"},
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
    # S · el super (contagio en la cola)
    ("S1", "S", "The 52-year-old woman keeps her hands on the trolley and marks a small dance step with her feet while she talks sideways.",
     [("O", "cheerful, confident", "Así, mientras hacés la cola. Ni gimnasio ni ropa especial.")]),
    ("S2", "prev", "The younger woman looks around, embarrassed, then back at her.",
     [("J", "embarrassed, low", "¿Acá, en el súper?")]),
    ("S3", "S", "The 52-year-old woman shrugs and smiles, still marking the step.",
     [("O", "warm", "Yo tengo cincuenta y dos y arranqué peor que vos.")]),
    ("S4", "prev", "She taps the handle of her trolley twice while she talks.",
     [("O", "convincing", "Dance Go. Diez minutos por día y hoy el test es gratis.")]),
    ("S5", "prev", "She nods at the other woman's trolley, inviting her.",
     [("O", "playful", "Agarrate del tuyo y seguime.")]),
    # T · la vecina que toca el timbre
    ("T1", "T", "The neighbour holds the tupper with both hands and leans to look past her into the living room.",
     [("V", "nosy, friendly", "Te escucho la música desde mi cocina, nena. ¿Tenés gente?")]),
    ("T2", "prev", "The woman in the doorway laughs, out of breath, and wipes her forehead with the back of her hand.",
     [("S", "laughing, out of breath", "No. Soy yo sola, con la tele del living.")]),
    ("T3", "T", "The neighbour looks her up and down, surprised, still holding the tupper.",
     [("V", "surprised", "¿Y eso es lo que te está cambiando el cuerpo?")]),
    ("T4", "prev", "The woman in the doorway nods and points inside with her thumb.",
     [("S", "simple, proud", "Diez minutos por día. Dance Go. Hoy el test es gratis, hacelo vos también.")]),
    # U · la hija que se rie
    ("U1", "U", "The teenage girl on the sofa films her mother with her phone and laughs out loud.",
     [("L", "teasing, laughing", "Má, parecés un pollo mojado.")]),
    ("U2", "prev", "The mother keeps dancing facing the TV without turning around.",
     [("S", "unbothered, cheerful", "Y sí. Y en tres semanas voy a ser un pollo mojado que entra en el jean.")]),
    ("U3", "U", "The teenage girl lowers the phone, watches for a second and stands up from the sofa.",
     [("L", "curious", "¿Me enseñás ese paso que estás haciendo?")]),
    ("U4", "prev", "The mother waves her over with one hand, both of them now facing the TV, apart from each other.",
     [("S", "warm", "Vení. Te van diciendo qué pie mover, no hay forma de hacerlo mal.")]),
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

PLACAS = {"T1": "3 SEMANAS DESPUÉS"}
ETIQUETAS = {}
CTA = ("Tocá en", "Más información")
