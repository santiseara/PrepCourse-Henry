from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H=1080,1920
F='fonts/'
def font(name,size,wt=None):
    f=ImageFont.truetype(F+name,size)
    if wt: f.set_variation_by_axes([wt])
    return f
def emoji(ch,size):
    try:
        f=ImageFont.truetype('/System/Library/Fonts/Apple Color Emoji.ttc',160)
        im=Image.new('RGBA',(200,200),(0,0,0,0)); ImageDraw.Draw(im).text((10,10),ch,font=f,embedded_color=True)
        im=im.crop(im.getbbox()); return im.resize((size,int(im.height*size/im.width)),Image.LANCZOS)
    except Exception as e:
        print('emoji fail',e); return None
def shadow_text(d,xy,t,f,fill,anchor='mm',sw=6):
    d.text(xy,t,font=f,fill=fill,anchor=anchor,stroke_width=sw,stroke_fill=(0,0,0,255))
out='vsl/gfx/'
# 1 tilde verde
im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
cx,cy,r=540,560,190
d.ellipse((cx-r,cy-r,cx+r,cy+r),outline=(34,197,94,255),width=34)
d.line([(cx-95,cy+5),(cx-20,cy+85),(cx+120,cy-90)],fill=(34,197,94,255),width=44,joint='curve')
im.save(out+'check.png')
# 2 bonos
g=emoji('🎁',230)
for i,(t1,t2) in enumerate([('BONO 1','PROTOCOLO\nANTI-FLACIDEZ'),('BONO 2','REVELACIÓN\nLUMBAR CERVICAL'),('BONO 3','DRENAJE LINFÁTICO\nEXPRESS')],1):
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
    if g: im.alpha_composite(g,(540-g.width//2,520))
    shadow_text(d,(540,860),t1,font('Anton.ttf',120),(250,204,21,255))
    d.multiline_text((540,1060),t2,font=font('Anton.ttf',110),fill=(255,255,255,255),anchor='mm',align='center',spacing=10,stroke_width=7,stroke_fill=(0,0,0,255))
    im.save(out+f'bono{i}.png')
# 3 precio
im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
fo=font('Anton.ttf',110); shadow_text(d,(540,560),'$49.990',fo,(255,255,255,255))
bb=d.textbbox((540,560),'$49.990',font=fo,anchor='mm'); d.line([(bb[0]-10,560),(bb[2]+10,560)],fill=(239,68,68,255),width=14)
shadow_text(d,(540,780),'$14.990',font('Anton.ttf',230),(34,197,94,255),sw=9)
# flecha roja
ax=540; d.rectangle((ax-28,930,ax+28,1080),fill=(239,68,68,255)); d.polygon([(ax-90,1070),(ax+90,1070),(ax,1190)],fill=(239,68,68,255))
im.save(out+'precio.png')
# 4 anclaje 50 mil
im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
shadow_text(d,(540,620),'+$50.000',font('Anton.ttf',200),(239,68,68,255),sw=8)
shadow_text(d,(540,790),'POR MES',font('Anton.ttf',110),(255,255,255,255))
im.save(out+'anclaje.png')
# 5 testimonio card
im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
card=(90,420,990,1330)
sh=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(sh).rounded_rectangle((card[0],card[1]+20,card[2],card[3]+20),48,fill=(0,0,0,140)); sh=sh.filter(ImageFilter.GaussianBlur(24)); im.alpha_composite(sh)
d.rounded_rectangle(card,48,fill=(255,255,255,250))
d.ellipse((150,490,270,610),fill=(243,217,220,255)); d.text((210,550),'MG',font=font('Montserrat.ttf',48,800),fill=(180,86,106,255),anchor='mm')
d.text((300,515),'Mariela G.',font=font('Montserrat.ttf',52,800),fill=(15,23,42,255))
d.line([(302,600),(314,612),(336,588)],fill=(22,163,74,255),width=6)
d.text((346,580),'Alumna verificada · CABA',font=font('Montserrat.ttf',34,600),fill=(22,163,74,255))
d.text((150,660),'★★★★★',font=font('Montserrat.ttf',60,700),fill=(245,179,1,255)) if False else None
st=emoji('⭐',60)
if st:
    for k in range(5): im.alpha_composite(st,(150+k*70,650))
q=('"Tenía 47 años y me sentía invisible. Después de 3 embarazos y la premenopausia, evitaba los espejos. '
   'Con el pilates no solo recuperé mi figura... recuperé mi esencia. Por primera vez en años, me siento mujer otra vez."')
fq=font('Montserrat.ttf',42,500); words=q.split(); lines=[]; cur=''
for w_ in words:
    t=(cur+' '+w_).strip()
    if d.textlength(t,font=fq)>760: lines.append(cur); cur=w_
    else: cur=t
lines.append(cur)
y=760
for l in lines: d.text((150,y),l,font=fq,fill=(51,65,85,255)); y+=62
im.save(out+'testimonio.png')
# 6 garantia
im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
cx,cy=540,680
pts=[]
import math
for k in range(48):
    a=k*math.pi/24; rr=250 if k%2==0 else 222
    pts.append((cx+rr*math.cos(a),cy+rr*math.sin(a)))
d.polygon(pts,fill=(212,160,23,255)); d.ellipse((cx-185,cy-185,cx+185,cy+185),fill=(255,251,235,255),outline=(168,122,8,255),width=8)
d.text((cx,cy-30),'30',font=font('Anton.ttf',190),fill=(168,122,8,255),anchor='mm')
d.text((cx,cy+105),'DÍAS',font=font('Anton.ttf',70),fill=(168,122,8,255),anchor='mm')
shadow_text(d,(540,1010),'GARANTÍA TOTAL',font('Anton.ttf',120),(255,255,255,255),sw=8)
shadow_text(d,(540,1135),'O TE DEVUELVO LA PLATA',font('Anton.ttf',70),(250,204,21,255))
im.save(out+'garantia.png')
print('ok', 'emoji' if g else 'noemoji')
