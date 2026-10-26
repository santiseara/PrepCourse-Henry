# -*- coding: utf-8 -*-
"""Maquetador de documentos de texto (los bonus escritos)."""
from engine import *
from paginas import ML, MR, ANCHO, seccion

class Doc(object):
    def __init__(self, c, titulo, bajada, bonus='', pie_txt=''):
        self.c = c; self.titulo = titulo; self.bajada = bajada
        self.bonus = bonus; self.pie_txt = pie_txt or titulo
        self.n = 1; self.y = 0; self.abierta = False

    # ---------- portada
    def portada(self, intro, items=None, muestra=None):
        c = self.c
        c.setFillColor(TINTA); c.rect(0, 0, A4W, A4H, stroke=0, fill=1)
        c.setFillColor(NARANJA); c.rect(0, A4H-14, A4W, 14, stroke=0, fill=1)
        c.setFont('BC', 13); c.setFillColor(NARANJA)
        c.drawString(ML, A4H-62, 'HERRERO DE FINDE')
        c.setFont('BCM', 9.5); c.setFillColor(HexColor('#9AA2AB'))
        c.drawString(ML, A4H-78, self.bonus.upper())
        c.setFont('MB', 34); c.setFillColor(PAPEL)
        y = A4H - 150
        for l in envolver(c, self.titulo.upper(), 'MB', 34, ANCHO):
            c.drawString(ML, y, l); y -= 40
        c.setFillColor(NARANJA); c.rect(ML, y+10, 120, 5, stroke=0, fill=1)
        c.setFont('BCM', 14); c.setFillColor(HexColor('#D7DBDF'))
        y -= 16
        for l in envolver(c, self.bajada, 'BCM', 14, ANCHO):
            c.drawString(ML, y, l); y -= 19
        c.setFont('B', 10); c.setFillColor(HexColor('#AEB6BE'))
        y -= 16
        for l in envolver(c, intro, 'B', 10, ANCHO-60):
            c.drawString(ML, y, l); y -= 14
        if items:
            c.setFillColor(HexColor('#22262B'))
            alto = 26 + len(items)*16
            c.roundRect(ML, 110, ANCHO, alto, 4, stroke=0, fill=1)
            yy = 110 + alto - 22
            c.setFont('BC', 10); c.setFillColor(NARANJA)
            c.drawString(ML+16, yy, 'LO QUE VAS A ENCONTRAR ADENTRO')
            yy -= 18
            for it in items:
                c.setFillColor(NARANJA); c.circle(ML+22, yy+2.6, 2, stroke=0, fill=1)
                c.setFont('B', 8.6); c.setFillColor(PAPEL)
                c.drawString(ML+30, yy, it); yy -= 16
        c.setFillColor(NARANJA); c.rect(0, 0, A4W, 14, stroke=0, fill=1)
        c.showPage(); self.n += 1

    # ---------- paginas
    def _abrir(self):
        c = self.c
        c.setFillColor(TINTA); c.rect(0, A4H-44, A4W, 44, stroke=0, fill=1)
        c.setFillColor(NARANJA); c.rect(0, A4H-47, A4W, 3, stroke=0, fill=1)
        c.setFont('BC', 8.4); c.setFillColor(NARANJA)
        c.drawString(ML, A4H-22, 'HERRERO DE FINDE')
        c.setFont('BCM', 7); c.setFillColor(HexColor('#9AA2AB'))
        c.drawString(ML, A4H-33, self.bonus.upper())
        c.setFont('BC', 11); c.setFillColor(PAPEL)
        c.drawRightString(A4W-MR, A4H-26, self.titulo.upper())
        self.y = A4H - 76
        self.abierta = True

    def _cerrar(self):
        c = self.c
        linea(c, ML, 52, A4W-MR, GRIS_CL, 0.5)
        c.setFont('BCM', 7); c.setFillColor(GRIS)
        c.drawString(ML, 42, 'Herrero de Finde · ' + self.bonus)
        c.drawCentredString(A4W/2, 42, self.pie_txt)
        c.drawRightString(A4W-MR, 42, 'pág. %d' % self.n)
        c.showPage(); self.n += 1; self.abierta = False

    def espacio(self, alto):
        if not self.abierta: self._abrir()
        if self.y - alto < 80:
            self._cerrar(); self._abrir()

    def cerrar(self):
        if self.abierta: self._cerrar()

    # ---------- bloques
    def h1(self, t):
        self.espacio(76)
        if self.y < A4H - 90: self.y -= 18
        c = self.c
        c.setFont('BC', 19); c.setFillColor(TINTA)
        for l in envolver(c, t.upper(), 'BC', 19, ANCHO):
            c.drawString(ML, self.y, l); self.y -= 22
        c.setFillColor(NARANJA); c.rect(ML, self.y + 12, 46, 3, stroke=0, fill=1)
        self.y -= 14

    def h2(self, t):
        self.espacio(46)
        self.y -= 6
        c = self.c
        c.setFillColor(NARANJA); c.rect(ML, self.y-2, 3, 11, stroke=0, fill=1)
        c.setFont('BC', 11); c.setFillColor(TINTA)
        c.drawString(ML+10, self.y, t.upper())
        self.y -= 22

    def p(self, t, size=9.5, lead=13.6):
        c = self.c
        for l in envolver(c, t, 'B', size, ANCHO):
            self.espacio(lead)
            c.setFont('B', size); c.setFillColor(TINTA2)
            c.drawString(ML, self.y, l); self.y -= lead
        self.y -= 9

    def bullets(self, items, size=9.4, lead=13.0):
        c = self.c
        for it in items:
            negrita = ''
            if '**' in it:
                partes = it.split('**')
                negrita, it = partes[1], (partes[2] if len(partes) > 2 else '')
            self.espacio(lead+4)
            c.setFillColor(NARANJA); c.circle(ML+3, self.y+3, 2.2, stroke=0, fill=1)
            x = ML+11
            if negrita:
                c.setFont('BB', size); c.setFillColor(TINTA)
                c.drawString(x, self.y, negrita)
                x += c.stringWidth(negrita + ' ', 'BB', size)
            resto = it.strip()
            if resto:
                ancho1 = ANCHO - (x - ML)
                ls = envolver(c, resto, 'B', size, ancho1)
                c.setFont('B', size); c.setFillColor(TINTA2)
                c.drawString(x, self.y, ls[0]); self.y -= lead
                for l in ls[1:]:
                    self.espacio(lead)
                    c.setFont('B', size); c.setFillColor(TINTA2)
                    c.drawString(ML+11, self.y, l); self.y -= lead
            else:
                self.y -= lead
            self.y -= 4
        self.y -= 8

    def check(self, items, size=9.4, lead=13.2):
        c = self.c
        for it in items:
            ls = envolver(c, it, 'B', size, ANCHO-18)
            self.espacio(lead*len(ls)+4)
            c.setStrokeColor(GRIS); c.setLineWidth(0.7)
            c.rect(ML, self.y-1.5, 8, 8, stroke=1, fill=0)
            c.setFont('B', size); c.setFillColor(TINTA2)
            for i, l in enumerate(ls):
                c.drawString(ML+16, self.y, l); self.y -= lead
            self.y -= 6

    def caja(self, titulo, texto, color=CREMA, barra=NARANJA, size=8.8):
        c = self.c
        ls = envolver(c, texto, 'B', size, ANCHO-32)
        alto = 40 + len(ls)*12.4
        self.espacio(alto+8)
        c.setFillColor(color); c.roundRect(ML, self.y-alto+10, ANCHO, alto, 4, stroke=0, fill=1)
        c.setFillColor(barra); c.rect(ML, self.y-alto+10, 3.5, alto, stroke=0, fill=1)
        c.setFont('BC', 10); c.setFillColor(TINTA)
        c.drawString(ML+16, self.y-8, titulo.upper())
        yy = self.y - 26
        c.setFont('B', size); c.setFillColor(TINTA2)
        for l in ls:
            c.drawString(ML+16, yy, l); yy -= 12.4
        self.y -= alto + 12

    def caja_oscura(self, titulo, items):
        c = self.c
        alto = 34 + len(items)*15
        self.espacio(alto+8)
        c.setFillColor(TINTA); c.roundRect(ML, self.y-alto+10, ANCHO, alto, 4, stroke=0, fill=1)
        c.setFont('BC', 11); c.setFillColor(NARANJA)
        c.drawString(ML+16, self.y-8, titulo.upper())
        yy = self.y - 26
        for it in items:
            c.setFillColor(NARANJA); c.circle(ML+20, yy+2.6, 2, stroke=0, fill=1)
            c.setFont('B', 8.4); c.setFillColor(PAPEL)
            c.drawString(ML+28, yy, it); yy -= 15
        self.y -= alto + 12

    def tabla(self, cols, filas, anchos, size=8.5):
        c = self.c
        self.espacio(26 + len(filas)*13)
        x0 = ML
        c.setFont('BCM', 6.8); c.setFillColor(GRIS)
        x = x0
        for t, a in zip(cols, anchos):
            c.drawString(x, self.y, t.upper()); x += a
        self.y -= 4
        linea(c, ML, self.y, A4W-MR, GRIS_CL, 0.5); self.y -= 12
        for i, fila in enumerate(filas):
            self.espacio(14)
            if i % 2 == 0:
                c.setFillColor(HexColor('#F7F8F9')); c.rect(ML-4, self.y-4, ANCHO+8, 13.4, stroke=0, fill=1)
            x = x0
            for j, (t, a) in enumerate(zip(fila, anchos)):
                c.setFont('BM' if j == 0 else 'B', size)
                c.setFillColor(TINTA if j == 0 else TINTA2)
                txt = str(t)
                while c.stringWidth(txt, 'B', size) > a - 6 and len(txt) > 4: txt = txt[:-2]
                c.drawString(x, self.y, txt); x += a
            self.y -= 14.6
        self.y -= 12

    def frase(self, t):
        c = self.c
        ls = envolver(c, t, 'BC', 13, ANCHO-40)
        self.espacio(len(ls)*18 + 16)
        c.setFillColor(NARANJA); c.rect(ML, self.y-len(ls)*18+10, 4, len(ls)*18, stroke=0, fill=1)
        c.setFont('BC', 13); c.setFillColor(TINTA)
        for l in ls:
            c.drawString(ML+16, self.y, l); self.y -= 18
        self.y -= 10
