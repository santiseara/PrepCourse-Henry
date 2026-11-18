# -*- coding: utf-8 -*-
"""B-roll 3D medico para Dieta de las 3 Fases, calcado del look de Eduardo Claas.
Veo 3.1 Fast por ApiMart, 8 s, 9:16, sin texto y sin voces.
Uso: python3 gen_broll_claas.py [ids...]   (sin ids = todos los que falten)"""
import os, sys, threading
sys.path.insert(0, '/Users/santiagoseara/.claude/skills/mini-novela/scripts')
import comun as C

D = os.path.expanduser('~/Desktop/dieta-3-fases/work/broll/veo')
os.makedirs(D, exist_ok=True)
LOG = os.path.join(D, 'costos.jsonl')
MODEL = os.environ.get('VEO', 'veo3.1-fast')

EST = ("Hyper-realistic 3D medical animation, photoreal CGI, macro detail, wet glossy organic surfaces, "
       "deep black background, cinematic volumetric lighting, shallow depth of field, slow steady camera move. "
       "No text, no subtitles, no captions, no watermark, no people, no hands. "
       "Audio: silence, no music, no voice, no narration.")

TOMAS = {
 'intestino_inflamado': "A human large intestine, anatomically accurate, swollen and inflamed, angry red and purple, "
    "glowing red hot spots pulsing under the surface, floating and slowly rotating in empty black space.",
 'intestino_fermenta': "Macro view inside a human intestine: half-digested food fermenting against the pink intestinal wall, "
    "gas bubbles swelling and rising, the wall stretching outward.",
 'bacterias_malas': "Macro view of a human intestinal wall being colonized by dark grey-green rod-shaped bacteria, "
    "spreading like mould over the pink tissue, the tissue reddening underneath.",
 'bacterias_buenas': "Macro view of a healthy pink intestinal wall being repopulated by glowing blue-white beneficial bacteria "
    "settling into the villi, the tissue turning healthy and bright.",
 'pared_abre': "Macro 3D cross-section of an intestinal wall: the tight junctions between the cells pull apart and open, "
    "dark toxins and food fragments leak through the gap into the red bloodstream below.",
 'zonulina': "Extreme macro 3D of a glowing protein molecule wedging itself between two intestinal cells and prying the junction open, "
    "golden molecule against pink tissue.",
 'higado_graso': "A human liver covered in thick yellow fat globules, dull and swollen, slowly rotating in empty black space.",
 'higado_sano': "A healthy human liver, deep clean red, glossy and smooth, glowing softly, slowly rotating in empty black space.",
 'higado_shock': "A human liver with inflammation spreading across its surface, red glow pulsing from inside, "
    "heat shimmer around it, floating in black space.",
 'sangre_sucia': "Macro view inside a blood vessel: dark murky toxic blood with floating debris and bacteria flowing fast "
    "toward a liver silhouette at the end of the tunnel.",
 'grasa_velcro': "Extreme macro of yellow fat globules sticking and clinging like velcro onto the dark red glossy surface of a liver.",
 'cuerpo_grasa': "A semi-transparent anatomical 3D figure of a human body seen from the front, thick yellow fat layer "
    "wrapped around the abdomen and waist, the rest of the body in red muscle, rotating slowly in black space.",
 'gases_panza': "3D anatomical cutaway of a human abdomen, the intestines filling with gas bubbles and expanding, "
    "the belly wall visibly swelling outward, dark clinical background.",
 'microbiota': "Dense microscopic landscape of a gut microbiome, thousands of bacteria of many shapes and colours "
    "covering the intestinal villi, camera drifting slowly through them.",
 'eco_higado': "A medical ultrasound monitor in a dark exam room showing a grainy black and white liver scan, "
    "the image shifting as the probe moves, clinical blue light.",
 'semillas_quemada': "Seeds falling in slow motion onto cracked burnt black scorched soil, smoke still rising, "
    "nothing growing, cinematic macro.",
 'cafe_colando': "Macro close-up of dark coffee dripping from a pour-over filter into a black ceramic mug on a kitchen counter, "
    "steam rising, warm morning light through a window, shallow depth of field.",
 'huevo_sarten': "Macro close-up of a raw egg cracked into a hot black frying pan, the white setting and bubbling around the yolk, "
    "steam rising, warm kitchen light.",
 'huevo_roto_madera': "Macro close-up of a raw egg cracked open on a rustic wooden board, the yolk glossy and intact, "
    "broken shell beside it, warm side light, dark background.",
 'pan_integral': "Macro close-up of a serrated knife slicing a dense wholegrain seeded bread loaf on a wooden board, "
    "crumbs falling, warm kitchen light.",
 'ensalada_cruda': "Close-up of a large bowl of raw green salad with lettuce, rocket and tomato being tossed with wooden tongs, "
    "bright daylight kitchen.",
 'avena': "Macro close-up of a bowl of oatmeal porridge with oats and berries, a spoon stirring slowly, steam rising, morning light.",
 'platos_sanos': "Top-down view of several healthy plates on a black table: grilled salmon with vegetables, a salad bowl, "
    "a grain bowl and chicken with broccoli, arranged in a circle on pure black background, slow rotation.",
 'panza_hinchada': "Close-up side view of a woman's bloated abdomen in a dark t-shirt and leggings, standing in a bedroom, "
    "her hand resting on the swollen belly, face not visible, soft home lighting.",
 'pastillas': "Close-up of a hand pouring white capsules and probiotic pills from a bottle into the palm, on a kitchen counter, "
    "several supplement bottles blurred behind.",
 'te_boldo': "Macro close-up of hot herbal tea being poured into a glass cup with dried leaves floating, steam rising, dark background.",
 'balanza': "Close-up of bare feet stepping onto a white bathroom scale on a tiled floor, the digital display out of focus, soft daylight.",
 'colonoscopia': "Endoscopic camera view travelling slowly through the inside of a human colon, pink wet mucosal walls with "
    "inflamed red patches, clinical bright light from the scope.",
}


def una(tid):
    out = f'{D}/{tid}.mp4'
    if os.path.exists(out) and os.path.getsize(out) > 100000:
        print('ya esta', tid, flush=True); return
    body = {'model': MODEL, 'prompt': TOMAS[tid] + ' ' + EST, 'duration': 8, 'aspect_ratio': '9:16'}
    try:
        C.video(body, out, LOG)
    except BaseException as e:
        print('FALLO', tid, str(e)[:240], flush=True)


ids = sys.argv[1:] or list(TOMAS)
th = []
for t in ids:
    h = threading.Thread(target=una, args=(t,)); h.start(); th.append(h)
    import time; time.sleep(1.5)
[h.join() for h in th]
print('FIN · saldo', C.saldo())
