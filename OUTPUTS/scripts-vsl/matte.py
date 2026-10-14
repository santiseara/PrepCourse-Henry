"""Saca el fondo de la avatar (máscara de video) con Robust Video Matting en ONNX.
Uso: python3 matte.py <video.mp4> <rvm_mobilenetv3_fp32.onnx> <mascara.mp4> [ancho=540]
Devuelve un video en grises (blanco = persona) del mismo largo y fps, a <ancho> px, para usar con alphamerge.
Modelo: https://github.com/PeterL1n/RobustVideoMatting/releases (v1.0.0, rvm_mobilenetv3_fp32.onnx)."""
import sys, os, subprocess, numpy as np, onnxruntime as ort

FF = os.path.expanduser('~/bin/ffmpeg')
src, model, out = sys.argv[1:4]
W = int(sys.argv[4]) if len(sys.argv) > 4 else 540
H = W * 16 // 9
fps = subprocess.run([FF, '-i', src], capture_output=True, text=True).stderr.split(' fps')[0].split(', ')[-1]

sess = ort.InferenceSession(model, providers=['CPUExecutionProvider'])
rec = [np.zeros((1, 1, 1, 1), np.float32)] * 4
ds = np.array([0.4], np.float32)
rd = subprocess.Popen([FF, '-v', 'error', '-i', src, '-vf', f'scale={W}:{H}', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'],
                      stdout=subprocess.PIPE)
wr = subprocess.Popen([FF, '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'gray', '-s', f'{W}x{H}', '-r', fps, '-i', '-',
                       '-c:v', 'libx264', '-crf', '12', '-pix_fmt', 'yuv420p', out], stdin=subprocess.PIPE)
n = 0
while True:
    buf = rd.stdout.read(W * H * 3)
    if len(buf) < W * H * 3: break
    x = np.frombuffer(buf, np.uint8).reshape(H, W, 3).transpose(2, 0, 1)[None].astype(np.float32) / 255
    fgr, pha, *rec = sess.run(None, {'src': x, 'r1i': rec[0], 'r2i': rec[1], 'r3i': rec[2], 'r4i': rec[3], 'downsample_ratio': ds})
    wr.stdin.write((np.clip(pha[0, 0], 0, 1) * 255).astype(np.uint8).tobytes())
    n += 1
wr.stdin.close(); wr.wait()
print('máscara lista:', out, n, 'cuadros')
