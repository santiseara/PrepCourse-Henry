import cv2, numpy as np, glob, os, json
BR='work/brolls'
def firmas(path, paso=0.1):
    cap=cv2.VideoCapture(path); fps=cap.get(cv2.CAP_PROP_FPS) or 30
    out=[]; i=0
    while True:
        ok,f=cap.read()
        if not ok: break
        if i % max(1,int(round(fps*paso)))==0:
            g=cv2.cvtColor(cv2.resize(f,(32,64)),cv2.COLOR_BGR2GRAY).astype(np.float32)
            out.append((i/fps,g))
        i+=1
    cap.release(); return out
# referencia: b0190 es presentadora casi entera
ref=[g for t,g in firmas(f'{BR}/b0190.mp4') if t<1.8]
R=np.mean(ref,axis=0)
res={}
for p in sorted(glob.glob(f'{BR}/*.mp4')):
    n=os.path.basename(p)[:-4]
    fs=firmas(p)
    d=[(round(t,2), float(np.abs(g-R).mean())) for t,g in fs]
    res[n]=d
json.dump(res, open('/private/tmp/claude-501/-Users-santiagoseara-PrepCourse-Henry/c08963b6-31c2-4caf-b289-ac7a26e0648e/scratchpad/firmas.json','w'))
UM=22
for n,d in res.items():
    malas=[t for t,x in d if x<UM]
    if malas: print(f'{n}: presentadora en {malas[0]:.1f}-{malas[-1]:.1f}s  ({len(malas)} muestras)  dur={d[-1][0]:.1f}')
