# -*- coding: utf-8 -*-
"""Dance Go · novela 4 «La foto del cumple» — cuarto ad del mismo molde copiado a Coach Ana Belen.
Vineta nueva en la cocina de la oficina (la foto grupal donde siempre se pone atras), con el mismo molde.
Las escenas I, J y K reusan los clips de la novela 1.
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
    "companiera": "An Argentine woman aged 38, curly dark hair, average build, wearing a light blue office shirt, holding a phone in one hand.",
    "sandra_antes": "An Argentine woman aged 45, dark brown hair tied back in a low ponytail, overweight with a round belly and heavy arms, tired ordinary face, wearing a loose grey t-shirt and black leggings.",
    "sandra_despues": ("sandra_antes", "now clearly slimmer with a flat stomach and slimmer arms, upright confident posture, brighter rested face, same low ponytail, wearing the same loose grey t-shirt, which now hangs loose on her, and the same black leggings"),
    "lucia": "An Argentine teenage girl aged 17, long straight dark hair, slim, wearing an oversized green t-shirt and jeans, holding a phone in one hand.",
    "camarera": "An Argentine woman aged 30, dark hair in a bun, slim and fit, wearing a white t-shirt under a black apron, behind a cafe counter.",
    "clienta_cafe": "An Argentine woman aged 50, wavy blonde-dyed hair to the shoulders, overweight, wearing a cream t-shirt, sitting at a cafe counter.",
}

ESCENAS = {
    "Y": ("Morning in an ordinary Argentine office kitchen with a kettle and mugs. On the left the overweight woman in the grey t-shirt "
          "(ref 1) holds a mug with both hands; on the right, an arm\'s length away, the curly-haired woman in the light blue shirt (ref 2) "
          "holds up her phone showing a photo, the phone clearly held in her hand.",
          ["sandra_antes", "companiera"]),
    "Z": ("Morning in the same ordinary Argentine office kitchen, same kettle and mugs. On the left the now slimmer woman in the grey "
          "t-shirt (ref 1) stands relaxed holding her mug; on the right, an arm\'s length away, the curly-haired woman in the light blue "
          "shirt (ref 2) holds up her phone to take a photo of her, the phone clearly held in her hand.",
          ["sandra_despues", "companiera"]),
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
    "F": ("F", "the workmate, a 38-year-old Argentine woman with a medium-pitched, chatty, warm voice"),
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
    "Y": {"S": "the overweight woman holding the mug", "F": "the curly-haired woman holding up the phone"},
    "Z": {"S": "the slimmer woman holding the mug", "F": "the curly-haired woman holding up the phone"},
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
    # Y · la foto del cumple del trabajo
    ("Y1", "Y", "The curly-haired woman holds her phone up and turns the screen toward the other woman, excited.",
     [("F", "chatty, warm", "Mirá la foto del cumple de Marcela, salimos todas divinas.")]),
    ("Y2", "prev", "The other woman leans in to look at the screen and then pulls back, holding her mug tighter.",
     [("S", "quiet, uncomfortable", "Yo estoy atrás de todas, casi no se me ve.")]),
    ("Y3", "Y", "The curly-haired woman lowers the phone and looks at her, not understanding.",
     [("F", "innocent", "Bueno, es que siempre te ponés atrás, nena.")]),
    ("Y4", "prev", "The woman with the mug looks at the phone one more time and then straight ahead.",
     [("S", "firm, quiet", "Ya sé. En la próxima me pongo adelante. Dame tres semanas.")]),
    # Z · la foto, tres semanas despues
    ("Z1", "Z", "The curly-haired woman holds up her phone to take a photo and stops, looking over the screen.",
     [("F", "surprised, happy", "Pará, esta foto me la guardo. Estás otra persona, nena.")]),
    ("Z2", "prev", "The slimmer woman poses with the mug in one hand, laughing.",
     [("S", "laughing", "Diez minutos por día en el living, con la tele. Nada más.")]),
    ("Z3", "Z", "The curly-haired woman lowers the phone and steps a little closer, interested.",
     [("F", "interested", "¿Y vos cuándo lo hacés? Porque yo salgo de acá a las seis.")]),
    ("Z4", "prev", "The slimmer woman shrugs and points at the clock on the wall.",
     [("S", "easy, convincing", "Cuando puedo. El test te arma el plan según el tiempo que tengas.")]),
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

PLACAS = {"Z1": "3 SEMANAS DESPUÉS"}
ETIQUETAS = {}
CTA = ("Tocá en", "Más información")
