# -*- coding: utf-8 -*-
"""Arma el plan de los 10 anuncios de Dieta de las 3 Fases, calcados de Eduardo Claas."""
import json, os, re, subprocess

BASE = os.path.expanduser('~/Desktop/dieta-3-fases/work')
FF = os.path.expanduser('~/bin/ffmpeg')
SAL = os.path.expanduser('~/Desktop/dieta-3-fases/work/prod')
os.makedirs(SAL, exist_ok=True)


def dur(f):
    r = subprocess.run([FF, '-i', f], capture_output=True, text=True).stderr
    m = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r)
    h, mi, s = m.groups()
    return int(h)*3600 + int(mi)*60 + float(s)


# g -> (hook, visuales del cuerpo en orden, estilo de subtitulo, color)
ADS = {
 'g01': dict(
   nombre='1 · barra amarilla CAFÉ + intestino 3D',
   hook=dict(vis='intestino_inflamado', dura=3.0,
             amarilla=['MIRÁ LO QUE EL CAFÉ LE HACE', 'A UN INTESTINO INFLAMADO']),
   vis=['cafe_colando*', 'ensalada_cruda', 'avena', 'pan_integral', 'intestino_fermenta*',
        'gases_panza', 'panza_hinchada', 'bacterias_malas', 'microbiota', 'bacterias_buenas',
        'semillas_quemada', 'platos_sanos'],
   sub='grande', color='amarillo',
   clave=['café','intestino','inflamado','fibras','fermentan','silenciar','expurgar','recolonizar','orden','bacterias']),
 'g02': dict(
   nombre='2 · placa amarilla QUÉ COMER + podcast',
   hook=dict(vis='microbiota', dura=3.2,
             amarilla=['QUÉ COMER CUANDO EL', 'INTESTINO ESTÁ INFLAMADO']),
   vis=['colonoscopia*', 'pastillas', 'intestino_inflamado', 'bacterias_malas', 'bacterias_buenas',
        'higado_sano', 'platos_sanos', 'balanza', 'cuerpo_grasa'],
   sub='grande', color='amarillo',
   clave=['argentina','colostomía','inflamada','noventa','método','bacterias','semana','SER','gratuita']),
 'g03': dict(
   nombre='3 · barra roja HUEVOS/HÍGADO',
   hook=dict(vis='huevo_roto_madera', dura=3.0,
             roja=['MIRÁ LO QUE LOS HUEVOS', 'LE HACEN A TU HÍGADO']),
   vis=['higado_graso*', 'te_boldo', 'pastillas', 'zonulina', 'pared_abre', 'sangre_sucia',
        'higado_shock', 'grasa_velcro', 'eco_higado', 'cuerpo_grasa', 'intestino_inflamado', 'higado_sano'],
   sub='grande', color='amarillo',
   clave=['hígado','grasa','zonulina','proteína','intestino','toxinas','velcro','shock','SER']),
 'g04': dict(
   nombre='4 · placa de informe + colonoscopía',
   hook=dict(vis='colonoscopia', dura=4.2,
             diario=['INFORME DE SALUD',
                     ['EL CÁNCER DE INTESTINO ESTÁ', 'CRECIENDO, INCLUSO ENTRE LOS',
                      'JÓVENES. ¿SABÉS RECONOCER', 'LAS SEÑALES?'],
                     'de la Argentina']),
   vis=['microbiota*', 'bacterias_malas', 'bacterias_buenas', 'intestino_inflamado',
        'cuerpo_grasa', 'higado_sano', 'balanza', 'platos_sanos', 'gases_panza'],
   sub='grande', color='amarillo',
   clave=['argentina','colostomía','inflamada','método','bacterias','ochenta','gas','gratuita']),
 'g05': dict(
   nombre='5 · doctor LES RUEGO + subtítulo chico',
   hook=dict(vis='eco_higado', dura=3.4,
             titular=['LES RUEGO A TODOS LOS QUE', 'TIENEN HÍGADO GRASO', 'QUE MIREN ESTO']),
   vis=['higado_graso*', 'zonulina', 'pared_abre', 'sangre_sucia', 'higado_shock',
        'grasa_velcro', 'te_boldo', 'intestino_fermenta', 'bacterias_buenas', 'higado_sano'],
   sub='chico', color='amarillo',
   clave=['hígado','graso','zonulina','proteína','toxinas','sangre','inflamación','SER']),
 'g06': dict(
   nombre='6 · doctor + barra CON EL INTESTINO INFLAMADO',
   hook=dict(vis='cafe_colando', dura=3.0,
             barra=['MIRÁ LO QUE EL CAFÉ HACE', 'CON EL INTESTINO INFLAMADO']),
   vis=['intestino_inflamado*', 'ensalada_cruda', 'avena', 'pan_integral', 'gases_panza',
        'intestino_fermenta', 'bacterias_malas', 'microbiota', 'bacterias_buenas',
        'semillas_quemada', 'panza_hinchada', 'platos_sanos', 'balanza'],
   sub='grande', color='celeste',
   clave=['café','intestino','inflamado','fermentar','silenciar','expurgar','recolonizar','orden']),
 'g07': dict(
   nombre='7 · placa 12 ALIMENTOS QUE INFLAMAN',
   hook=dict(vis='platos_sanos', dura=3.0,
             titular=['12 ALIMENTOS QUE', 'INFLAMAN EL CUERPO!']),
   vis=['intestino_inflamado*', 'microbiota', 'bacterias_malas', 'huevo_sarten', 'pan_integral',
        'ensalada_cruda', 'balanza', 'zonulina', 'pared_abre', 'sangre_sucia', 'cuerpo_grasa',
        'bacterias_buenas', 'higado_sano'],
   sub='grande', color='amarillo',
   clave=['intestino','disbiosis','inflamado','zonulina','toxinas','cortisol','insulina','SER']),
 'g08': dict(
   nombre='8 · placa blanca PRESTÁ ATENCIÓN + huevo',
   hook=dict(vis='huevo_sarten', dura=2.8,
             blanca=['PRESTÁ ATENCIÓN A ESTO!']),
   vis=['avena*', 'pan_integral', 'cafe_colando', 'intestino_inflamado', 'cuerpo_grasa',
        'bacterias_buenas', 'balanza', 'platos_sanos'],
   sub='grande', color='amarillo',
   clave=['huevos','desayuno','metabolismo','grasa','bacterias','semana','gas','gratuita']),
 'g09': dict(
   nombre='9 · barra roja HÍGADO GRASO + hígado 3D',
   hook=dict(vis='higado_graso', dura=3.0,
             roja=['EL HÍGADO GRASO', 'NO EMPIEZA EN EL HÍGADO']),
   vis=['eco_higado*', 'zonulina', 'pared_abre', 'sangre_sucia', 'higado_shock', 'grasa_velcro',
        'te_boldo', 'intestino_inflamado', 'higado_sano', 'microbiota'],
   sub='grande', color='celeste',
   clave=['hígado','graso','zonulina','intestino','toxinas','sangre','shock','SER']),
 'g10': dict(
   nombre='10 · ecografía + día 1 a día 30 (doctora)',
   hook=dict(vis='balanza', dura=3.2,
             titular=['COMÉS POCO, HACÉS EJERCICIO', 'Y LA BALANZA NO SE MUEVE']),
   vis=['panza_hinchada*', 'intestino_inflamado', 'zonulina', 'pared_abre', 'bacterias_malas',
        'bacterias_buenas', 'microbiota', 'cuerpo_grasa', 'gases_panza', 'platos_sanos',
        'higado_sano', 'eco_higado'],
   sub='chico', color='celeste',
   clave=['intestino','metabolismo','zonulina','inflamación','microbiota','SER','día']),
}

planes = []
for g, a in ADS.items():
    av = f'{BASE}/heygen/hey_{g}.mp4'
    if not os.path.exists(av):
        print('FALTA el render de HeyGen:', g); continue
    D = dur(av) / 1.20                     # el cuerpo ya acelerado
    n = len(a['vis'])
    paso = max(4.6, (D - 6.0) / n)
    inserts, partidas = [], []
    for i, v in enumerate(a['vis']):
        t = 4.0 + i * paso
        if t > D - 3.0:
            break
        item = dict(t=round(t, 2), dura=2.2, vis=v.rstrip('*'))
        if v.endswith('*'):
            item['modo'] = 'partida'; item['dura'] = 3.2
            partidas.append(item)
        else:
            inserts.append(item)
    planes.append(dict(
        nombre=a['nombre'], salida=f'{SAL}/{g}.mp4', avatar=av, speed=1.20,
        hook=a['hook'], inserts=inserts, partidas=partidas, guion=f'{BASE}/guion/{g}.txt',
        sub=a['sub'], por_vez=3, clave=a['clave'], color=a['color'], cierre_seg=2.6))

json.dump(planes, open(f'{BASE}/planes.json', 'w'), ensure_ascii=False, indent=1)
print(f'{len(planes)} planes en {BASE}/planes.json')
for p in planes:
    print(' ', p['nombre'], '·', len(p['inserts']) + len(p['partidas']), 'visuales')
