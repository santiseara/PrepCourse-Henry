# -*- coding: utf-8 -*-
"""Ventanas limpias del pool de Crochet Painting (2026-11-20).
Pool: 193 clips de #crochetportrait, #graphgan, #c2ccrochet, #pixelcrochet,
#tapestrycrochet y #crochetwallhanging. El OCR de Vision (1 cuadro cada 1,5 s)
dejo 57 con ventana limpia; la revision visual del mosaico bajo 10 mas
(macrame, telar, tufting, texto en chino, texto en espanol sobre la pieza,
clip apaisado, clip oscuro). Quedan 47, y la hoja de contactos del render bajo 2 mas (c18 con texto quemado
ROTADO que el OCR no lee, c10 plano lejano sin pieza). A los 17 que habian quedado
recortados se les paso un OCR fino de 0,5 s (el de 1,5 s se come carteles que entran
y salen) y se les fijo la ventana por el tramo limpio corrido mas largo: 4 se cayeron.
Pool final: 41 clips.
"""

VENT = {
    'c00': ('6956295630348258565', 0.3, 30.3),   # limpio  @retroflowershop
    'c01': ('7363043717885840683', 0.3, 30.3),   # limpio  @macrame.masters
    'c02': ('7650629394628709653', 0.3, 20.0),   # limpio  @miriane.santana
    'c03': ('7657246454360067359', 0.3, 30.3),   # limpio  @ty_bailie
    'c04': ('7657368238627491103', 0.3, 30.3),   # limpio  @babykhiii
    'c05': ('7665609448483720479', 0.3, 27.3),   # limpio  @siewaa_e
    'c06': ('7440969708624481582', 5.0, 30.3),   # recorte fino  @magicallydee_
    'c07': ('7632968900187114759', 5.0, 30.3),   # recorte fino  @luisaroldannn
    'c08': ('7229746173144272155', 3.5, 29.4),   # recorte fino  @pelinsliving
    'c09': ('7238423179645996315', 4.0, 22.4),   # recorte fino  @xinecrochets
#    'c10': ('7280324077837880618', 4.9, 30.3),   # recorte  @ty_bailie   <- fuera: texto quemado rotado / plano lejano sin pieza
    'c11': ('7193084874503277830', 0.3, 21.3),   # limpio  @cosybearcrochet
    'c12': ('7678041266503945504', 3.5, 23.4),   # recorte fino  @knotty.app
    'c13': ('7617228468257950990', 9.0, 30.3),   # recorte fino  @needy.cat.crafts
    'c14': ('7615813497267473685', 0.3, 19.8),   # limpio  @alloagua
    'c15': ('7683689171239701781', 3.0, 21.9),   # recorte fino  @entrelazados.peru_
    'c16': ('7667046122132622613', 0.3, 18.3),   # limpio  @life_sphereee
    'c17': ('7599034489259527446', 3.5, 19.4),   # recorte fino  @rociarro
#    'c18': ('7001207193332665606', 0.3, 18.0),   # recorte  @sistertrashleigh   <- fuera: texto quemado rotado / plano lejano sin pieza
    'c19': ('7441318463999593761', 1.5, 16.4),   # recorte fino  @rociarro
    'c20': ('7708657680692301087', 0.3, 16.8),   # limpio  @he.huang367
    'c21': ('7387904340620610822', 0.3, 15.3),   # limpio  @anakarina.zs
    'c22': ('7510516248577428758', 0.3, 15.3),   # limpio  @cornwallcrochet
    'c23': ('7554140671850892556', 0.3, 15.3),   # limpio  @clochecleo
    'c24': ('7591700229200629022', 0.3, 15.3),   # limpio  @fuggler_luv_mlp
    'c25': ('7592415760090287390', 0.3, 15.3),   # limpio  @shakeniaceazer
    'c26': ('7652824711348489486', 0.3, 15.3),   # limpio  @kindredloop
    'c27': ('7438748588840078635', 0.3, 13.8),   # limpio  @kajuuuuul
    'c28': ('7601586614866906390', 0.3, 13.8),   # limpio  @bloomnbeth
    'c29': ('7678347482262146324', 0.3, 13.8),   # limpio  @aliciamtts
    'c30': ('7526594113748208909', 0.8, 12.9),   # recorte fino  @wrenycrochet
    'c31': ('7433561877663272222', 0.3, 12.3),   # limpio  @leilaniandstitch0
    'c32': ('7709268257227705631', 0.3, 12.3),   # limpio  @katkweensmith
    'c33': ('7200372726928821510', 1.5, 12.9),   # recorte fino  @mjsoffthehook
#    'c34': ('7578240755664211221', 3.4, 15.3),   # recorte  @lilecroche   <- fuera: ventana limpia de solo 3,4 s
#    'c35': ('7663533526234483999', 0.3, 12.0),   # recorte  @issa_fit_   <- fuera: ventana limpia de solo 6,6 s
    'c36': ('7454334730087992622', 0.3, 10.8),   # limpio  @sunnyside_storeco
    'c37': ('7682864230055365919', 0.3, 10.8),   # limpio  @josie.crochets
    'c38': ('7225029475262647594', 4.0, 13.9),   # recorte fino  @spunkyspiritshop
    'c39': ('7288691193939168558', 0.3, 9.3),   # limpio  @wasatchhandmade
#    'c40': ('7407528334348881182', 3.4, 12.3),   # recorte  @crochetbykiante   <- fuera: ventana limpia de solo 4,4 s
    'c41': ('7454291729663921413', 0.8, 8.4),   # recorte fino  @laurenvanseveren
#    'c42': ('7495350772939361558', 0.3, 9.0),   # recorte  @maybe.art.uk   <- fuera: cartel del creador que nombra ETSY
    'c43': ('7532611941135666445', 0.3, 7.8),   # limpio  @shev.crochets
    'c44': ('7633530954161704193', 0.3, 7.8),   # limpio  @ya.knits_
    'c45': ('7677211204779019553', 0.3, 7.8),   # limpio  @itsbciyawned
    'c46': ('7471450140964818222', 0.3, 6.3),   # limpio  @pipers.poison
}

FAM = {"7001207193332665606": "sistertrashleigh", "6919607755758210309": "heartsprinkle", "7134389655851552043": "destinymakes", "6956295630348258565": "retroflowershop", "7172980318889119022": "mommypants3", "7191314508646780203": "chaotichookercrochet", "7179634964093504814": "mommypants3", "7193775189786627334": "luxurybeautylogos", "7193084874503277830": "cosybearcrochet", "7203369250784890155": "ck.crochets", "7200372726928821510": "mjsoffthehook", "7225029475262647594": "spunkyspiritshop", "7213357909915290885": "delphenesstudio", "7229746173144272155": "pelinsliving", "7233602682395626758": "laagujamagica_", "7236440843656219946": "_ry444_", "7238423179645996315": "xinecrochets", "7277230830374702369": "atainya", "7277621755601063210": "lunamaeartistry", "7288691193939168558": "wasatchhandmade", "7280324077837880618": "ty_bailie", "7311815185159736608": "moonwoolcrafts", "7257286131929156870": "andreaacolor_", "7343764356032695594": "thefreckledfern", "7346246244311895329": "slaying_crocheting", "7348572243292884229": "hebrascrochet", "7315188703545216261": "entrelanascolombia", "7354412500349144362": "shujun_crochet", "7354231086806830344": "muncut_crochet", "7360125082540231942": "hebrascrochet", "7363023972608412974": "sysycrochets", "7364031205668359466": "wasatchhandmade", "7380508399244479790": "bekialexi", "7363043717885840683": "macrame.masters", "7364558689782566150": "hebrascrochet", "7384153907729009962": "lyshiamangu", "7395257938383867169": "taylormadebyclara", "7387904340620610822": "anakarina.zs", "7399070703703559454": "cocotriesitall_", "7407528334348881182": "crochetbykiante", "7399316203962928414": "cocotriesitall_", "7418994679259090218": "xseatherny", "7413489031847234848": "rociarro", "7415425451801300230": "hebrascrochet", "7422301112213998878": "diydivaa_", "7424991380327517472": "rociarro", "7433561877663272222": "leilaniandstitch0", "7426869670856117509": "ladykatrinacraft", "7440969708624481582": "magicallydee_", "7435033511616122167": "toffy.brand", "7438748588840078635": "kajuuuuul", "7441318463999593761": "rociarro", "7441412847738866986": "mamahouston4", "7443552773867638062": "yarnbender1", "7453839383708454174": "yarnth3ory", "7454334730087992622": "sunnyside_storeco", "7454291729663921413": "laurenvanseveren", "7471450140964818222": "pipers.poison", "7482163154844273926": "thali_colors", "7434637258206088504": "maghilando", "7459802064743369990": "entreovillos", "7484366562888142126": "aprilsbasementcrafting", "7488855225596398890": "ganxxet", "7491356050172448022": ".12amvibe", "7455705506246593798": "endlessknotzcanada", "7495350772939361558": "maybe.art.uk", "7495512885330726175": "jade.crochet.studios", "7500031277446319390": "w3akwrists", "7501901292764138782": "cottons.dream", "7503356671616453918": "threadlyattraction", "7510516248577428758": "cornwallcrochet", "7504732550703697174": "ilewandowskaaa", "7485156165559536901": "julia.okano", "7511444221140847894": "cosybearcrochet", "7510656874245623062": "crojo_creations", "7511638179582119170": "love.indy_", "7523436735057972511": "withlovedaniee", "7504107185811557638": "idalina_correa", "7525083874678820152": "miniworldlover", "7512198716296596792": "linhas.passadas", "7526594113748208909": "wrenycrochet", "7528553908927466774": "rociarro", "7531302974681812255": "subwayjointsart", "7532611941135666445": "shev.crochets", "7535880922328042807": "paytans.creations", "7533296001839336710": "miniworldlover", "7535157416825113912": "miniworldlover", "7546666364019166471": "lulietaart", "7536993393910631686": "miniworldlover", "7537319364048030998": "cyneesugar", "7552921870555745553": "miniworldlover", "7554140671850892556": "clochecleo", "7554784042369961246": "loveandstitch", "7555461404426390802": "philancer", "7558124632658824456": "i.m.hyu", "7554915186549820683": "venusdesaturno", "7559003560302644494": "4threadsco", "7567335144294550800": "crocuteau", "7578240755664211221": "lilecroche", "7582379881145699615": "brookelinn02", "7583183179691986196": "crochet.desde.cer5", "7585476344952311047": "inspiration.empire", "7570875343905492236": "majo.crochet0", "7583807638576647454": "breann253", "7588950963088526613": "bateecrochet201", "7591700229200629022": "fuggler_luv_mlp", "7590468560397438231": "viggo258", "7589365439885577485": "mossycrochets", "7596709683214306582": "shi.visuals", "7591915801075010836": "miniworldlover", "7592415760090287390": "shakeniaceazer", "7592914770315971870": "user2453618113930", "7597408903260818710": "fatimatirado_", "7599034489259527446": "rociarro", "7601586614866906390": "bloomnbeth", "7614161155656846622": "olga.levinski", "7615813497267473685": "alloagua", "7607204370341563669": "laizask", "7615261121490062613": "miniworldlover", "7621144138926394644": "daisycrochetcompany", "7618657753485085973": "theworldcrochets", "7621610280040058126": "pipers.poison", "7617228468257950990": "needy.cat.crafts", "7629028947392531720": "wumieecrochet__", "7633530954161704193": "ya.knits_", "7623106309210033415": "fluffybeavers", "7643080097880132896": "rucnaenni", "7645071421407857941": "lachinix03", "7632968900187114759": "luisaroldannn", "7652824711348489486": "kindredloop", "7653879144719174925": "hxuanshan", "7657246454360067359": "ty_bailie", "7649943579321847047": "caja_de_hobbies", "7650629394628709653": "miriane.santana", "7657368238627491103": "babykhiii", "7659821751945170183": "isa_yassuda", "7663533526234483999": "issa_fit_", "7665452728595811604": "miriane.santana", "7665609448483720479": "siewaa_e", "7665717828489678100": "bestchoicecrochet_", "7666963748791389471": "kristataliaferro", "7668072930294648085": "catelie___", "7667046122132622613": "life_sphereee", "7669115855212481814": "hookedbyjulian__", "7668814344565706015": "yarnpalsbynina", "7669601628328103182": "sel.linette_", "7670465774686850325": "inspiration.empire", "7671283373784026386": "delicadeza_pontoaponto", "7672798756869311765": "lemijecrochet", "7657972369293659414": "purlnhook", "7677211204779019553": "itsbciyawned", "7674711624510344466": "lethiciasaleso", "7678041266503945504": "knotty.app", "7678069290938944790": "eldaisycrochet", "7682864230055365919": "josie.crochets", "7678347482262146324": "aliciamtts", "7683689171239701781": "entrelazados.peru_", "7681659678975085846": "zanwi.de.nata", "7683897188589800725": "jiooncrochet", "7684741624777297182": "ty_bailie", "7679839587434319136": "sabcroch", "7686147354721848606": "kristataliaferro", "7689494780908260641": "cozyfaeriecraft", "7697669317495704846": "itslauryns", "7695925138323279118": "okiegirlblingnthings", "7687001138499013920": "crojo_creations", "7699904404828310815": "emloops_", "7700031832049454366": "weathersworldcreative", "7705900231354764575": "thisandthatbyellen", "7701354531736554760": "eucamila0706", "7706907475555093783": "coser.y.cantar.me", "7707020296510868766": "thisandthatbyellen", "7707274493139799310": "awesomewonder4u", "7707513404126252301": "thisandthatbyellen", "7699226741545487647": "the.humble.croche", "7708554340356672782": "graphganstudio", "7707953321134378271": "thisandthatbyellen", "7708288884995640607": "thisandthatbyellen", "7708657680692301087": "he.huang367", "7708973602904837390": "crochetpatterns.us", "7708661400024960286": "thisandthatbyellen", "7709042489801444639": "thisandthatbyellen", "7708688760979934471": "tillyreescrochet", "7709188178128817439": "thisandthatbyellen", "7709190507636755743": "thisandthatbyellen", "7709268257227705631": "katkweensmith", "7709496781515607326": "alicias_hobbies", "7709367652937944351": "ariee778", "7709548544289541406": "thisandthatbyellen", "7709766339052735758": "thisandthatbyellen", "7709620619347889439": "thisandthatbyellen", "7710085190961401102": "thehandmadenook", "7710107179587620116": "jami_creations"}
