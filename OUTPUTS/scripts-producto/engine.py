# -*- coding: utf-8 -*-
"""
Motor de planos de herreria - Herrero de Finde.
Geometria 3D simple (vigas/chapas/canos) -> vistas ortogonales, isometrico,
lista de cortes, aprovechamiento en barras de 6 m, costo de material y precio sugerido.
Salida: paginas A4 vectoriales con reportlab.
"""
import math, os, re
from math import gcd, sqrt, cos, sin, radians
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.lib.colors import Color, HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

A4W, A4H = 595.28, 841.89
HERE = os.path.dirname(os.path.abspath(__file__))

# ----------------------------------------------------------------------------- fuentes
def registrar_fuentes():
    f = os.path.join(HERE, 'fonts')
    pares = [('B', 'Barlow-Regular'), ('BM', 'Barlow-Medium'), ('BS', 'Barlow-SemiBold'),
             ('BB', 'Barlow-Bold'), ('BCR', 'BarlowCondensed-Regular'),
             ('BCM', 'BarlowCondensed-Medium'), ('BC', 'BarlowCondensed-Bold'),
             ('MB', 'Montserrat-ExtraBold')]
    for alias, arch in pares:
        pdfmetrics.registerFont(TTFont(alias, os.path.join(f, arch + '.ttf')))

# ----------------------------------------------------------------------------- paleta
TINTA   = HexColor('#15181C')
TINTA2  = HexColor('#3C434C')
GRIS    = HexColor('#8A9099')
GRIS_CL = HexColor('#C9CED4')
PAPEL   = HexColor('#FFFFFF')
CREMA   = HexColor('#F4F2EE')
NARANJA = HexColor('#F26B21')
NAR_CL  = HexColor('#FDE6D6')
VERDE   = HexColor('#1C8C4C')
VERDE_CL= HexColor('#E3F2E8')
ACERO   = HexColor('#9AA2AB')
AZUL    = HexColor('#2B5F86')

# ============================================================================= MATERIALES
# precio = por barra de 6 m (perfiles) o por m2 (chapas y mallas), en pesos, oct-2026
M = {}
def _m(k, nom, corto, fam, precio, **kw):
    d = dict(nom=nom, corto=corto, fam=fam, precio=precio, barra=6000)
    d.update(kw); M[k] = d

# canos estructurales cuadrados
_m('TC20', 'Caño estructural cuadrado 20 x 20 x 1,2 mm', '20x20x1,2', 'tubo', 14000, w=20, h=20, kgm=0.68)
_m('TC25', 'Caño estructural cuadrado 25 x 25 x 1,6 mm', '25x25x1,6', 'tubo', 18000, w=25, h=25, kgm=1.12)
_m('TC30', 'Caño estructural cuadrado 30 x 30 x 1,6 mm', '30x30x1,6', 'tubo', 22000, w=30, h=30, kgm=1.37)
_m('TC40', 'Caño estructural cuadrado 40 x 40 x 2 mm', '40x40x2', 'tubo', 32000, w=40, h=40, kgm=2.27)
_m('TC50', 'Caño estructural cuadrado 50 x 50 x 2 mm', '50x50x2', 'tubo', 40000, w=50, h=50, kgm=2.90)
_m('TC50G','Caño estructural cuadrado 50 x 50 x 3 mm', '50x50x3', 'tubo', 56000, w=50, h=50, kgm=4.23)
_m('TC60', 'Caño estructural cuadrado 60 x 60 x 2 mm', '60x60x2', 'tubo', 50000, w=60, h=60, kgm=3.53)
_m('TC80', 'Caño estructural cuadrado 80 x 80 x 3 mm', '80x80x3', 'tubo', 94000, w=80, h=80, kgm=6.95)
_m('TC100','Caño estructural cuadrado 100 x 100 x 3 mm', '100x100x3', 'tubo', 122000, w=100, h=100, kgm=8.83)
# rectangulares
_m('TR4020', 'Caño estructural rectangular 40 x 20 x 1,6 mm', '40x20x1,6', 'tubo', 19000, w=40, h=20, kgm=1.37)
_m('TR5030', 'Caño estructural rectangular 50 x 30 x 2 mm', '50x30x2', 'tubo', 29000, w=50, h=30, kgm=2.27)
_m('TR6040', 'Caño estructural rectangular 60 x 40 x 2 mm', '60x40x2', 'tubo', 38000, w=60, h=40, kgm=2.90)
_m('TR8040', 'Caño estructural rectangular 80 x 40 x 2 mm', '80x40x2', 'tubo', 46000, w=80, h=40, kgm=3.53)
_m('TR10050','Caño estructural rectangular 100 x 50 x 3 mm', '100x50x3', 'tubo', 86000, w=100, h=50, kgm=6.47)
_m('TR12060','Caño estructural rectangular 120 x 60 x 3 mm', '120x60x3', 'tubo', 104000, w=120, h=60, kgm=7.88)
# angulos
_m('AN25', 'Ángulo de alas iguales 25 x 25 x 3 mm', 'ángulo 25x3', 'angulo', 16000, w=25, h=25, kgm=1.11)
_m('AN30', 'Ángulo de alas iguales 30 x 30 x 3 mm', 'ángulo 30x3', 'angulo', 19000, w=30, h=30, kgm=1.36)
_m('AN40', 'Ángulo de alas iguales 40 x 40 x 4 mm', 'ángulo 40x4', 'angulo', 34000, w=40, h=40, kgm=2.42)
_m('AN50', 'Ángulo de alas iguales 50 x 50 x 5 mm', 'ángulo 50x5', 'angulo', 52000, w=50, h=50, kgm=3.77)
_m('AN63', 'Ángulo de alas iguales 63 x 63 x 6 mm', 'ángulo 63x6', 'angulo', 78000, w=63, h=63, kgm=5.72)
# planchuelas
_m('PL25', 'Planchuela 25 x 3 mm (1" x 1/8")', 'planchuela 25x3', 'planchuela', 12000, w=25, h=3, kgm=0.59)
_m('PL38', 'Planchuela 38 x 6 mm (1 1/2" x 1/4")', 'planchuela 38x6', 'planchuela', 26000, w=38, h=6, kgm=1.79)
_m('PL50', 'Planchuela 50 x 6 mm (2" x 1/4")', 'planchuela 50x6', 'planchuela', 34000, w=50, h=6, kgm=2.36)
_m('PL76', 'Planchuela 76 x 6 mm (3" x 1/4")', 'planchuela 76x6', 'planchuela', 52000, w=76, h=6, kgm=3.58)
_m('PL100','Planchuela 100 x 8 mm (4" x 5/16")', 'planchuela 100x8', 'planchuela', 86000, w=100, h=8, kgm=6.28)
# redondos y canos redondos
_m('RD8',  'Hierro redondo liso 8 mm', 'redondo 8', 'redondo', 7000, w=8, h=8, kgm=0.39)
_m('RD10', 'Hierro redondo liso 10 mm', 'redondo 10', 'redondo', 10000, w=10, h=10, kgm=0.62)
_m('RD12', 'Hierro redondo liso 12 mm', 'redondo 12', 'redondo', 14000, w=12, h=12, kgm=0.89)
_m('RD16', 'Hierro redondo liso 16 mm', 'redondo 16', 'redondo', 24000, w=16, h=16, kgm=1.58)
_m('RD20', 'Hierro redondo liso 20 mm', 'redondo 20', 'redondo', 36000, w=20, h=20, kgm=2.47)
_m('CR25', 'Caño redondo 1" x 1,6 mm', 'caño 1"', 'redondo', 26000, w=25, h=25, kgm=0.94)
_m('CR38', 'Caño redondo 1 1/2" x 2 mm', 'caño 1 1/2"', 'redondo', 44000, w=38, h=38, kgm=1.83)
_m('CR50', 'Caño redondo 2" x 2 mm', 'caño 2"', 'redondo', 58000, w=50, h=50, kgm=2.44)
_m('CR60', 'Caño redondo 2 1/2" x 2 mm', 'caño 2 1/2"', 'redondo', 72000, w=60, h=60, kgm=3.05)
# perfiles C
_m('C100', 'Perfil C 100 x 50 x 2 mm', 'perfil C 100', 'perfil', 80000, w=100, h=50, kgm=4.70)
_m('C120', 'Perfil C 120 x 50 x 3 mm', 'perfil C 120', 'perfil', 118000, w=120, h=50, kgm=7.30)
_m('UPN100', 'Perfil U normal 100 x 50 (UPN 100)', 'UPN 100', 'perfil', 150000, w=100, h=50, kgm=10.60)
# chapas y planos (precio por m2)
_m('CH16', 'Chapa lisa 1,6 mm (BWG 16)', 'chapa 1,6 mm', 'chapa', 38000, t=1.6, por='m2')
_m('CH2',  'Chapa lisa 2 mm', 'chapa 2 mm', 'chapa', 46000, t=2.0, por='m2')
_m('CH3',  'Chapa lisa 3 mm', 'chapa 3 mm', 'chapa', 66000, t=3.0, por='m2')
_m('CH47', 'Chapa lisa 4,75 mm (3/16")', 'chapa 4,75 mm', 'chapa', 98000, t=4.75, por='m2')
_m('CH6',  'Chapa lisa 6 mm (1/4")', 'chapa 6 mm', 'chapa', 108000, t=6.0, por='m2')
_m('CHA3', 'Chapa antideslizante 3 mm', 'antideslizante 3 mm', 'chapa', 86000, t=3.0, por='m2')
_m('CHEX', 'Chapa expandida (metal desplegado) 1,6 mm', 'expandida', 'chapa', 42000, t=1.6, por='m2')
_m('MALLA','Malla de hierro 10 x 10 cm, 4,2 mm', 'malla', 'chapa', 24000, t=4.2, por='m2')
_m('FEN18','Fenólico 18 mm', 'fenólico 18 mm', 'chapa', 52000, t=18.0, por='m2')
_m('MAD25','Tabla de madera dura 25 mm', 'tabla 25 mm', 'chapa', 44000, t=25.0, por='m2')
_m('CHGR', 'Rejilla de hierro (grating) 25 mm', 'rejilla', 'chapa', 94000, t=25.0, por='m2')

VALOR_HORA = 48000       # tu hora de taller, pesos
INSUMOS = 0.12           # discos, gas, alambre, antioxido y pintura sobre el material
FACTOR_ALTO = 1.30       # techo del rango de venta

# ============================================================================= PIEZAS
class Pz(object):
    """Una pieza. Viga/cano: eje p1->p2 con perfil. Chapa: caja por sus 3 extensiones."""
    __slots__ = ('tag','rol','mat','p1','p2','kind','w','h','corte','paso','marca','extra')
    def __init__(self, tag, rol, mat, p1, p2, kind='viga', w=None, h=None, corte='recto', marca=True, extra=None):
        self.tag, self.rol, self.mat = tag, rol, mat
        self.p1, self.p2 = tuple(float(v) for v in p1), tuple(float(v) for v in p2)
        self.kind, self.corte, self.marca, self.extra = kind, corte, marca, extra or {}
        d = M[mat]
        self.w = w if w is not None else d.get('w', 10)
        self.h = h if h is not None else d.get('h', 10)
    @property
    def largo(self):
        return dist(self.p1, self.p2)
    def ejes(self):
        """(dir, u, v) del perfil."""
        d = norm(sub(self.p2, self.p1))
        ref = (0.0, 0.0, 1.0)
        if abs(d[2]) > 0.92: ref = (0.0, 1.0, 0.0)
        u = norm(cross(d, ref)); v = norm(cross(u, d))
        return d, u, v
    def caja(self):
        """Vertices del prisma de la pieza."""
        if self.kind == 'cil':
            d, u, v = self.ejes()
            r = self.w/2.0
            pts = []
            for i in range(16):
                a = 2*math.pi*i/16.0
                off = add(mul(u, r*math.cos(a)), mul(v, r*math.sin(a)))
                pts.append(add(self.p1, off)); pts.append(add(self.p2, off))
            return pts
        if self.kind == 'chapa':
            (x1,y1,z1), (x2,y2,z2) = self.p1, self.p2
            xs=[x1,x2]; ys=[y1,y2]; zs=[z1,z2]
            return [(x,y,z) for x in xs for y in ys for z in zs]
        d,u,v = self.ejes()
        pts=[]
        for p in (self.p1, self.p2):
            for su in (-0.5, 0.5):
                for sv in (-0.5, 0.5):
                    pts.append(add(p, add(mul(u, su*self.w), mul(v, sv*self.h))))
        return pts
    def caras(self):
        """Lista de (4 vertices, normal) del prisma."""
        if self.kind == 'cil':
            d, u, v = self.ejes()
            r = self.w/2.0; n = 16
            aro_a = []; aro_b = []
            for i in range(n):
                ang = 2*math.pi*i/n
                off = add(mul(u, r*math.cos(ang)), mul(v, r*math.sin(ang)))
                aro_a.append(add(self.p1, off)); aro_b.append(add(self.p2, off))
            out = []
            for i in range(n):
                j = (i+1) % n
                ang = 2*math.pi*(i+0.5)/n
                nor = add(mul(u, math.cos(ang)), mul(v, math.sin(ang)))
                out.append(([aro_a[i], aro_a[j], aro_b[j], aro_b[i]], nor))
            out.append((aro_a[::-1], mul(d, -1)))
            out.append((aro_b, d))
            return out
        if self.kind == 'chapa':
            (x1,y1,z1),(x2,y2,z2) = self.p1, self.p2
            x1,x2 = min(x1,x2),max(x1,x2); y1,y2 = min(y1,y2),max(y1,y2); z1,z2 = min(z1,z2),max(z1,z2)
            v = {}
            for i,(x,y,z) in enumerate([(x1,y1,z1),(x2,y1,z1),(x2,y2,z1),(x1,y2,z1),
                                        (x1,y1,z2),(x2,y1,z2),(x2,y2,z2),(x1,y2,z2)]): v[i]=(x,y,z)
            idx = [((0,1,2,3),(0,0,-1)),((4,5,6,7),(0,0,1)),((0,1,5,4),(0,-1,0)),
                   ((3,2,6,7),(0,1,0)),((0,3,7,4),(-1,0,0)),((1,2,6,5),(1,0,0))]
            return [([v[i] for i in q], n) for q,n in idx]
        d,u,v = self.ejes()
        a,b = self.p1, self.p2
        hw, hh = self.w/2.0, self.h/2.0
        c = lambda p,su,sv: add(p, add(mul(u, su*hw), mul(v, sv*hh)))
        A=[c(a,-1,-1), c(a,1,-1), c(a,1,1), c(a,-1,1)]
        B=[c(b,-1,-1), c(b,1,-1), c(b,1,1), c(b,-1,1)]
        caras=[(A[::-1], mul(d,-1)), (B, d),
               ([A[0],A[1],B[1],B[0]], mul(v,-1)),
               ([A[3],A[2],B[2],B[3]], v),
               ([A[0],A[3],B[3],B[0]], mul(u,-1)),
               ([A[1],A[2],B[2],B[1]], u)]
        return caras

# helpers vectoriales
def sub(a,b): return (a[0]-b[0], a[1]-b[1], a[2]-b[2])
def add(a,b): return (a[0]+b[0], a[1]+b[1], a[2]+b[2])
def mul(a,k): return (a[0]*k, a[1]*k, a[2]*k)
def dot(a,b): return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
def cross(a,b): return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def largo3(a): return sqrt(dot(a,a))
def norm(a):
    n = largo3(a)
    return (a[0]/n, a[1]/n, a[2]/n) if n else (1.0,0.0,0.0)
def dist(a,b): return largo3(sub(a,b))

# constructores comodos -------------------------------------------------------
def vx(tag, rol, mat, x1, x2, y, z, **kw):   # viga en el eje X
    return Pz(tag, rol, mat, (x1,y,z), (x2,y,z), **kw)
def vy(tag, rol, mat, y1, y2, x, z, **kw):   # viga en el eje Y
    return Pz(tag, rol, mat, (x,y1,z), (x,y2,z), **kw)
def vz(tag, rol, mat, z1, z2, x, y, **kw):   # viga vertical
    return Pz(tag, rol, mat, (x,y,z1), (x,y,z2), **kw)
def chapa(tag, rol, mat, x1, x2, y1, y2, z1, z2, **kw):
    return Pz(tag, rol, mat, (x1,y1,z1), (x2,y2,z2), kind='chapa', **kw)
def chapa_h(tag, rol, mat, x1, x2, y1, y2, z, **kw):   # chapa horizontal
    t = M[mat].get('t', 3.0)
    return chapa(tag, rol, mat, x1, x2, y1, y2, z, z+t, **kw)
def chapa_v(tag, rol, mat, x1, x2, y, z1, z2, **kw):   # chapa vertical (plano XZ)
    t = M[mat].get('t', 3.0)
    return chapa(tag, rol, mat, x1, x2, y, y+t, z1, z2, **kw)
def chapa_vy(tag, rol, mat, y1, y2, x, z1, z2, **kw):  # chapa vertical (plano YZ)
    t = M[mat].get('t', 3.0)
    return chapa(tag, rol, mat, x, x+t, y1, y2, z1, z2, **kw)

def marco_xy(tagbase, rol, mat, x1, x2, y1, y2, z, corte='45 grados', **kw):
    """Marco rectangular horizontal a 45. x1..x2 e y1..y2 son las medidas de afuera."""
    w = M[mat].get('w', 10)
    return [vx(tagbase, rol, mat, x1, x2, y1+w/2.0, z, corte=corte, **kw),
            vx(tagbase, rol, mat, x1, x2, y2-w/2.0, z, corte=corte, **kw),
            vy(tagbase+'b', rol, mat, y1, y2, x1+w/2.0, z, corte=corte, **kw),
            vy(tagbase+'b', rol, mat, y1, y2, x2-w/2.0, z, corte=corte, **kw)]

def marco_xz(tagbase, rol, mat, x1, x2, z1, z2, y, corte='45 grados', **kw):
    """Marco rectangular vertical en el plano XZ, medidas de afuera."""
    d = M[mat]; w = d.get('w', 10); h = d.get('h', 10)
    return [vx(tagbase, rol, mat, x1, x2, y, z1+h/2.0, corte=corte, **kw),
            vx(tagbase, rol, mat, x1, x2, y, z2-h/2.0, corte=corte, **kw),
            vz(tagbase+'b', rol, mat, z1, z2, x1+w/2.0, y, corte=corte, **kw),
            vz(tagbase+'b', rol, mat, z1, z2, x2-w/2.0, y, corte=corte, **kw)]

def marco_yz(tagbase, rol, mat, y1, y2, z1, z2, x, corte='45 grados', **kw):
    """Marco rectangular vertical en el plano YZ, medidas de afuera."""
    d = M[mat]; w = d.get('w', 10); h = d.get('h', 10)
    return [vy(tagbase, rol, mat, y1, y2, x, z1+h/2.0, corte=corte, **kw),
            vy(tagbase, rol, mat, y1, y2, x, z2-h/2.0, corte=corte, **kw),
            vz(tagbase+'b', rol, mat, z1, z2, x, y1+w/2.0, corte=corte, **kw),
            vz(tagbase+'b', rol, mat, z1, z2, x, y2-w/2.0, corte=corte, **kw)]

def reparto(a, b, n):
    """n puntos repartidos entre a y b (incluidos los extremos)."""
    if n <= 1: return [(a+b)/2.0]
    paso = (b-a)/float(n-1)
    return [a + paso*i for i in range(n)]

def interiores(a, b, n):
    """n puntos interiores equiespaciados entre a y b."""
    if n <= 0: return []
    paso = (b-a)/float(n+1)
    return [a + paso*(i+1) for i in range(n)]

# ============================================================================= PLANO
CATS = [
    ('TR', 'Trailers y carros', 'Trailers, carros de arrastre y zorras'),
    ('BQ', 'Parrillas, ahumadores y fogoneros', 'Todo lo que lleva fuego'),
    ('GY', 'Gimnasio en casa y racks', 'Jaulas, bancos y soportes'),
    ('FM', 'Portones de campo, comederos y corrales', 'Lo que piden en el campo y en la quinta'),
    ('SH', 'Herramientas, plantillas y mesas de taller', 'Lo que usas para fabricar el resto'),
    ('TK', 'Racks y bandejas para camioneta', 'Arriba de la caja y arriba del techo'),
    ('FN', 'Muebles industriales', 'Hierro y madera para vender a la semana'),
    ('ST', 'Cocheras, estructuras y techos', 'Lo grande, lo que se cotiza mas caro'),
]
CAT_NOM = dict((c[0], c[1]) for c in CATS)

class Plano(object):
    def __init__(self, cat, nombre, piezas, pasos, horas, nivel, resumen, quien,
                 herramientas, avisos, dims=None, detalle=None, extras=None, variante=''):
        self.cat, self.nombre = cat, nombre
        self.piezas = [p for p in piezas if p is not None]
        self.pasos, self.horas, self.nivel = pasos, horas, nivel
        self.resumen, self.quien = resumen, quien
        self.herramientas, self.avisos = herramientas, avisos
        self.dims = dims or []
        self.detalle = detalle
        self.extras = extras or []      # [(descripcion, cantidad_texto, precio)]
        self.variante = variante
        self.codigo = None
        self.pagina = None
        self._cl = None

    # --- geometria ---------------------------------------------------------
    def bbox(self):
        xs=[]; ys=[]; zs=[]
        for p in self.piezas:
            for (x,y,z) in p.caja(): xs.append(x); ys.append(y); zs.append(z)
        return (min(xs),max(xs),min(ys),max(ys),min(zs),max(zs))
    def medidas(self):
        x1,x2,y1,y2,z1,z2 = self.bbox()
        return (x2-x1, y2-y1, z2-z1)

    # --- lista de cortes ---------------------------------------------------
    def cortes(self):
        if self._cl is not None: return self._cl
        grupos = {}
        for p in self.piezas:
            if p.kind == 'chapa':
                (x1,y1,z1),(x2,y2,z2) = p.p1, p.p2
                lados = sorted([abs(x2-x1), abs(y2-y1), abs(z2-z1)], reverse=True)
                k = (p.mat, round(lados[0]), round(lados[1]), 'chapa')
            else:
                k = (p.mat, round(p.largo), 0, p.corte)
            grupos.setdefault(k, []).append(p)
        orden = sorted(grupos.items(), key=lambda kv: (-kv[0][1], kv[0][0]))
        letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        out = []
        for i, (k, ps) in enumerate(orden):
            mat, l1, l2, corte = k
            roles = []
            for p in ps:
                if p.rol not in roles: roles.append(p.rol)
            rol = ' / '.join(roles[:2]) + (' ...' if len(roles) > 2 else '')
            letra = letras[i] if i < 26 else letras[i//26-1] + letras[i%26]
            out.append(dict(letra=letra, mat=mat, largo=l1, ancho=l2, corte=corte,
                            rol=rol, cant=len(ps), piezas=ps))
            for p in ps: p.extra['letra'] = letra
        self._cl = out
        return out

    # --- compra ------------------------------------------------------------
    def compra(self):
        """[(material, texto_cantidad, precio)] + nesting por material."""
        porbarra = {}; porm2 = {}
        for it in self.cortes():
            d = M[it['mat']]
            if d.get('por') == 'm2':
                area = (it['largo']/1000.0) * (it['ancho']/1000.0) * it['cant']
                porm2[it['mat']] = porm2.get(it['mat'], 0.0) + area
            else:
                porbarra.setdefault(it['mat'], []).extend([it['largo']]*it['cant'])
        filas = []; nest = []
        for mat, largos in sorted(porbarra.items(), key=lambda kv: -M[kv[0]]['precio']):
            barras = acomodar(largos, M[mat]['barra'])
            n = len(barras)
            precio = n * M[mat]['precio']
            metros = sum(largos)/1000.0
            filas.append(dict(mat=mat, cant='%d barra%s de 6 m' % (n, '' if n==1 else 's'),
                              detalle=('%.1f m netos' % metros).replace('.', ','), precio=precio, n=n))
            nest.append((mat, barras))
        for mat, area in sorted(porm2.items(), key=lambda kv: -kv[1]*M[kv[0]]['precio']):
            a = max(area, 0.01)
            bruto = a * 1.12
            precio = bruto * M[mat]['precio']
            filas.append(dict(mat=mat, cant=('%.2f m²' % bruto).replace('.', ','),
                              detalle=('%.2f m² netos' % a).replace('.', ','), precio=precio, n=0))
        return filas, nest

    def costo_compra(self):
        filas, _ = self.compra()
        return redondear(sum(f['precio'] for f in filas) + sum(e[2] for e in self.extras), 1000)

    def costo_material(self):
        """Lo que consume este trabajo: metros usados + 8 % de desperdicio."""
        total = 0.0
        for it in self.cortes():
            d = M[it['mat']]
            if d.get('por') == 'm2':
                total += (it['largo']/1000.0)*(it['ancho']/1000.0)*it['cant']*d['precio']*1.12
            else:
                total += (it['largo']/1000.0)*it['cant']*(d['precio']/(d['barra']/1000.0))*1.08
        total += sum(e[2] for e in self.extras)
        return redondear(total, 1000)

    def precio_venta(self):
        mat = self.costo_material()
        bajo = mat * (1 + INSUMOS) + self.horas[0] * VALOR_HORA
        bajo = redondear(bajo, 5000)
        alto = redondear(bajo * FACTOR_ALTO, 5000)
        return bajo, alto

    def insumos(self):
        return redondear(self.costo_material() * INSUMOS, 1000)

def acomodar(largos, barra=6000, sierra=3):
    """First-fit decreasing: reparte los cortes en barras comerciales."""
    res = []
    for L in sorted(largos, reverse=True):
        L = min(L, barra)
        puesto = False
        for b in res:
            if b['libre'] >= L + sierra:
                b['cortes'].append(L); b['libre'] -= (L + sierra); puesto = True; break
        if not puesto:
            res.append(dict(cortes=[L], libre=barra - L - sierra))
    return res

def redondear(v, paso):
    return int(round(v/float(paso)) * paso)

# ============================================================================= FORMATO
def pesos(v):
    s = '{:,.0f}'.format(float(v)).replace(',', '.')
    return '$' + s

def pulg(mm):
    if mm <= 0: return '0"'
    v = mm/25.4
    s = int(round(v*16))
    ent, rem = s//16, s%16
    if rem == 0: return '%d"' % ent
    g = gcd(rem, 16)
    fr = '%d/%d' % (rem//g, 16//g)
    return ('%d %s"' % (ent, fr)) if ent else ('%s"' % fr)

def mm_y_pulg(mm):
    return '%d mm  ·  %s' % (int(round(mm)), pulg(mm))

def med2(L, A):
    return ('%.2f x %.2f m' % (L/1000.0, A/1000.0)).replace('.', ',')

def metros(mm):
    return ('%.2f m' % (mm/1000.0)).replace('.', ',')

# ============================================================================= DIBUJO
ISO_SX = 0.70711
ISO_SY = 0.40825
ISO_CAM = (1.0, 1.0, 1.0)

def proy(p, vista):
    x,y,z = p
    if vista == 'frente':  return ( x, z)
    if vista == 'lateral': return (-y, z)
    if vista == 'planta':  return ( x,-y)
    return ((x-y)*ISO_SX, (2*z-x-y)*ISO_SY)

def hull(pts):
    pts = sorted(set((round(a,3), round(b,3)) for a,b in pts))
    if len(pts) <= 2: return pts
    def cr(o,a,b): return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
    lo=[]
    for p in pts:
        while len(lo)>=2 and cr(lo[-2],lo[-1],p) <= 0: lo.pop()
        lo.append(p)
    up=[]
    for p in reversed(pts):
        while len(up)>=2 and cr(up[-2],up[-1],p) <= 0: up.pop()
        up.append(p)
    return lo[:-1] + up[:-1]

class Marco(object):
    """Transformacion de mm de la pieza a puntos de la hoja."""
    def __init__(self, x, y, w, h, b1, b2, b3, b4, pad=0.0, k=None):
        ancho = max(b2-b1, 1.0); alto = max(b4-b3, 1.0)
        if k is None:
            k = min((w-2*pad)/ancho, (h-2*pad)/alto)
        self.k = k
        self.ox = x + (w - ancho*k)/2.0 - b1*k
        self.oy = y + (h - alto*k)/2.0 - b3*k
    def __call__(self, pt):
        return (self.ox + pt[0]*self.k, self.oy + pt[1]*self.k)

def caja_vista(piezas, vista):
    pts = []
    for p in piezas:
        for v in p.caja(): pts.append(proy(v, vista))
    xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
    return min(xs), max(xs), min(ys), max(ys)

def marco_para(piezas, vista, box, pad=0.0, k=None):
    b1,b2,b3,b4 = caja_vista(piezas, vista)
    return Marco(box[0], box[1], box[2], box[3], b1, b2, b3, b4, pad, k)

def escala_comun(piezas, pares, pad=0.0):
    """pares: [(vista, box)]. Devuelve {vista: Marco} con la misma escala."""
    k = None
    for vista, box in pares:
        b1,b2,b3,b4 = caja_vista(piezas, vista)
        kk = min((box[2]-2*pad)/max(b2-b1,1.0), (box[3]-2*pad)/max(b4-b3,1.0))
        k = kk if k is None else min(k, kk)
    return dict((v, marco_para(piezas, v, b, pad, k)) for v, b in pares), k

def dibujar_vista(c, piezas, vista, box, pad=6.0, lw=0.55, relleno=PAPEL, borde=TINTA, mk=None):
    """Vista ortogonal: silueta de cada pieza, de atras hacia adelante."""
    mk = mk or marco_para(piezas, vista, box, pad)
    prof = {'frente': (0,-1,0), 'lateral': (1,0,0), 'planta': (0,0,1)}[vista]
    visibles = [p for p in piezas if vista not in p.extra.get('sin_vista', ())]
    punteadas = [p for p in piezas if vista in p.extra.get('sin_vista', ())]
    ordenadas = sorted(visibles, key=lambda p: dot(mul(add(p.p1,p.p2),0.5), prof))
    for p in ordenadas:
        hp = hull([proy(v, vista) for v in p.caja()])
        if len(hp) < 3: continue
        path = c.beginPath()
        a = mk(hp[0]); path.moveTo(a[0], a[1])
        for q in hp[1:]:
            b = mk(q); path.lineTo(b[0], b[1])
        path.close()
        c.setFillColor(relleno); c.setStrokeColor(borde); c.setLineWidth(lw)
        c.drawPath(path, stroke=1, fill=1)
    for p in punteadas:
        hp = hull([proy(v, vista) for v in p.caja()])
        if len(hp) < 3: continue
        path = c.beginPath()
        a = mk(hp[0]); path.moveTo(a[0], a[1])
        for q in hp[1:]:
            b = mk(q); path.lineTo(b[0], b[1])
        path.close()
        c.setStrokeColor(GRIS); c.setLineWidth(0.45); c.setDash(2, 2)
        c.drawPath(path, stroke=1, fill=0); c.setDash()
    return mk

def dibujar_iso(c, piezas, box, pad=6.0, mk=None, resaltar=None, grises=None, lw=0.3,
                base=ACERO, luz=(0.35,-0.55,0.76)):
    """Isometrico sombreado. resaltar: tags en naranja. grises: tags en gris claro."""
    resaltar = set(resaltar or []); grises = set(grises or [])
    mk = mk or marco_para(piezas, 'iso', box, pad)
    luz = norm(luz); cam = norm(ISO_CAM)
    caras = []
    for p in piezas:
        if p.tag in grises:   col = HexColor('#D9DDE1')
        elif resaltar and p.tag in resaltar: col = NARANJA
        elif resaltar:        col = HexColor('#D9DDE1')
        else:                 col = base
        for quad, n in p.caras():
            n = norm(n)
            if dot(n, cam) <= 0.02: continue
            sh = 0.60 + 0.40*max(0.0, dot(n, luz))
            trozos = trocear(quad)
            for sq in trozos:
                cen = mul(reduce_add(sq), 1.0/len(sq))
                caras.append((dot(cen, cam), sq, col, sh, 'f'))
            caras.append((max(dot(v, cam) for v in quad), quad, col, sh, 'l'))
    caras.sort(key=lambda t: t[0])
    for _, quad, col, sh, modo in caras:
        path = c.beginPath()
        a = mk(proy(quad[0], 'iso')); path.moveTo(a[0], a[1])
        for v in quad[1:]:
            b = mk(proy(v, 'iso')); path.lineTo(b[0], b[1])
        path.close()
        if modo == 'f':
            c.setFillColor(Color(min(1, col.red*sh), min(1, col.green*sh), min(1, col.blue*sh)))
            c.drawPath(path, stroke=0, fill=1)
        else:
            c.setStrokeColor(Color(col.red*sh*0.45, col.green*sh*0.45, col.blue*sh*0.45))
            c.setLineWidth(lw); c.drawPath(path, stroke=1, fill=0)
    return mk

def trocear(quad, maxlado=140.0):
    """Parte una cara grande en sub-cuadros para ordenar bien por profundidad."""
    a, b, c_, d = quad
    l1 = max(dist(a,b), dist(d,c_)); l2 = max(dist(b,c_), dist(a,d))
    nu = max(1, min(8, int(math.ceil(l1/maxlado))))
    nv = max(1, min(8, int(math.ceil(l2/maxlado))))
    if nu == 1 and nv == 1: return [quad]
    out = []
    for i in range(nu):
        for j in range(nv):
            u0, u1 = i/float(nu), (i+1)/float(nu)
            v0, v1 = j/float(nv), (j+1)/float(nv)
            def P(u, v):
                top = add(mul(a, 1-u), mul(b, u))
                bot = add(mul(d, 1-u), mul(c_, u))
                return add(mul(top, 1-v), mul(bot, v))
            e = 0.02
            u0e, u1e = u0 - e/float(nu), u1 + e/float(nu)
            v0e, v1e = v0 - e/float(nv), v1 + e/float(nv)
            out.append([P(u0e,v0e), P(u1e,v0e), P(u1e,v1e), P(u0e,v1e)])
    return out

def reduce_add(pts):
    s = (0.0,0.0,0.0)
    for p in pts: s = add(s, p)
    return s

# --- cotas -------------------------------------------------------------------
def _flecha(c, x, y, dx, dy, s=3.2):
    d = norm((dx, dy, 0))
    px, py = -d[1]*s*0.33, d[0]*s*0.33
    p = c.beginPath(); p.moveTo(x, y)
    p.lineTo(x - d[0]*s + px, y - d[1]*s + py)
    p.lineTo(x - d[0]*s - px, y - d[1]*s - py)
    p.close(); c.setFillColor(TINTA); c.drawPath(p, stroke=0, fill=1)

def cota_h(c, mk, x1, x2, yref, texto, off=12, lado=1, size=6.1, color=TINTA):
    a = mk((x1, yref)); b = mk((x2, yref))
    y = a[1] + off*lado
    c.setStrokeColor(GRIS); c.setLineWidth(0.35); c.setDash(1, 1.6)
    c.line(a[0], a[1], a[0], y); c.line(b[0], b[1], b[0], y); c.setDash()
    c.setStrokeColor(color); c.setLineWidth(0.5)
    c.line(a[0], y, b[0], y)
    _flecha(c, a[0], y, -1, 0); _flecha(c, b[0], y, 1, 0)
    c.setFont('BCM', size); tw = c.stringWidth(texto, 'BCM', size)
    c.setFillColor(PAPEL); c.rect((a[0]+b[0])/2 - tw/2 - 1.6, y - size*0.38, tw + 3.2, size*1.08, stroke=0, fill=1)
    c.setFillColor(color); c.drawCentredString((a[0]+b[0])/2, y - size*0.3, texto)

def cota_v(c, mk, y1, y2, xref, texto, off=12, lado=1, size=6.1, color=TINTA):
    a = mk((xref, y1)); b = mk((xref, y2))
    x = a[0] + off*lado
    c.setStrokeColor(GRIS); c.setLineWidth(0.35); c.setDash(1, 1.6)
    c.line(a[0], a[1], x, a[1]); c.line(b[0], b[1], x, b[1]); c.setDash()
    c.setStrokeColor(color); c.setLineWidth(0.5)
    c.line(x, a[1], x, b[1])
    _flecha(c, x, a[1], 0, -1); _flecha(c, x, b[1], 0, 1)
    c.saveState(); c.translate(x, (a[1]+b[1])/2); c.rotate(90)
    c.setFont('BCM', size); tw = c.stringWidth(texto, 'BCM', size)
    c.setFillColor(PAPEL); c.rect(-tw/2 - 1.6, -size*0.38, tw + 3.2, size*1.08, stroke=0, fill=1)
    c.setFillColor(color); c.drawCentredString(0, -size*0.3, texto)
    c.restoreState()

# ============================================================================= TEXTO
def envolver(c, texto, fuente, size, ancho):
    palabras = texto.split()
    lineas = []; actual = ''
    for w in palabras:
        probe = (actual + ' ' + w).strip()
        if c.stringWidth(probe, fuente, size) <= ancho or not actual:
            actual = probe
        else:
            lineas.append(actual); actual = w
    if actual: lineas.append(actual)
    return lineas

def parrafo(c, texto, x, y, ancho, fuente='B', size=8.2, lead=10.2, color=TINTA2, max_lineas=None):
    c.setFillColor(color); c.setFont(fuente, size)
    ls = envolver(c, texto, fuente, size, ancho)
    if max_lineas: ls = ls[:max_lineas]
    for i, l in enumerate(ls):
        c.drawString(x, y - i*lead, l)
    return y - (len(ls)-1)*lead

def chip(c, x, y, texto, bg=NAR_CL, fg=NARANJA, size=6.2, pad=4.0, alto=11.0, fuente='BC'):
    c.setFont(fuente, size)
    w = c.stringWidth(texto, fuente, size) + pad*2
    c.setFillColor(bg); c.roundRect(x, y, w, alto, 2.0, stroke=0, fill=1)
    c.setFillColor(fg); c.drawString(x + pad, y + alto/2 - size*0.36, texto)
    return w

def linea(c, x1, y, x2, color=GRIS_CL, lw=0.5, dash=None):
    c.setStrokeColor(color); c.setLineWidth(lw)
    if dash: c.setDash(*dash)
    c.line(x1, y, x2, y); c.setDash()


def letras_iso(c, pl, box, mk=None, pad=6.0):
    """Marca con un circulito donde va cada letra de la lista de cortes."""
    mk = mk or marco_para(pl.piezas, 'iso', box, pad)
    dibujar_iso(c, pl.piezas, box, mk=mk)
    puestos = []
    for it in pl.cortes():
        p = max(it['piezas'], key=lambda q: dot(mul(add(q.p1, q.p2), 0.5), ISO_CAM))
        cen = mul(add(p.p1, p.p2), 0.5)
        x, y = mk(proy(cen, 'iso'))
        if any((x-a)**2 + (y-b)**2 < 90 for a, b in puestos): continue
        puestos.append((x, y))
        c.setFillColor(NARANJA); c.circle(x, y, 5.4, stroke=0, fill=1)
        c.setFont('BC', 7); c.setFillColor(PAPEL)
        c.drawCentredString(x, y-2.4, it['letra'])
    return mk
