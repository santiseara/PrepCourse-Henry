import os,subprocess,sys,glob,json
import numpy as np
from PIL import Image
sys.path.insert(0,'/Users/santiagoseara/PrepCourse-Henry/OUTPUTS/scripts-vsl')
from vent_macetas import VENT
FF=os.path.expanduser('~/bin/ffmpeg')
if not os.path.exists(FF): FF='ffmpeg'
res={}
for k,v in VENT.items():
    vid,a,b=v[0],v[1],v[2]
    src=f'tiktoks/{vid}.mp4'
    tops,bots=[],[]
    for i in range(10):
        t=a+(b-a)*i/9.0
        subprocess.run([FF,'-y','-v','error','-ss',f'{t:.2f}','-i',src,'-frames:v','1','-vf','scale=160:-1','/tmp/_b.png'],check=False)
        try: im=np.array(Image.open('/tmp/_b.png').convert('L'))
        except Exception: continue
        f=im.mean(axis=1); h=len(f)
        top=0
        while top<h//3 and f[top]<14: top+=1
        bot=0
        while bot<h//3 and f[h-1-bot]<14: bot+=1
        tops.append(top/h); bots.append(bot/h)
    if not tops: continue
    mt,mb=max(tops),max(bots)
    util=1-mt-mb
    z=round(min(2.2, 1/util+0.02),2) if util<0.995 else 1.0
    yb=0.5 if abs(mt-mb)<0.01 else (mt/(mt+mb) if (mt+mb)>0 else 0.5)
    res[k]=dict(top=round(mt,3),bot=round(mb,3),zoom=z,yb=round(yb,2))
    if z>1.0: print(f'{k} {vid}  top={mt:.3f} bot={mb:.3f} -> zoom {z} yb {yb:.2f}')
json.dump(res,open('/tmp/barras.json','w'),indent=1)
print('listo')
