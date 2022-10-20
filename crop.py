from PyQt5.QtWidgets import QRubberBand, QLabel
from PyQt5.QtGui import QPixmap,QPainter
from PyQt5.QtCore import QRect, Qt
from templates.menu import *

class LabelCrop(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent().setCursor(Qt.CrossCursor)
        self.x = self.parent().geometry().x()
        self.y = self.parent().geometry().y()
        self.width = self.parent().geometry().width()
        self.height = self.parent().geometry().height()
        print(self.width)
        print(self.height)

    def imagem(self, imagem):
        self.nome_imagem = imagem
        self.imagem = QPixmap(imagem)
        self.imagem_escala = self.imagem.scaled(self.width,self.height)
        SQUARE_SIDE = 40
        COLS, ROWS = int(self.width / SQUARE_SIDE +1), int(self.height / SQUARE_SIDE +1)
        painter = QPainter(self.imagem_escala)
        painter.setPen(Qt.darkGreen)
        for r in range(ROWS):
            painter.drawLine(0, SQUARE_SIDE * r, self.width, SQUARE_SIDE * r)
        for c in range(COLS):
            painter.drawLine(SQUARE_SIDE * c, self.height, SQUARE_SIDE * c, 0)
        self.setPixmap(self.imagem_escala)

    def mousePressEvent (self, eventQMouseEvent):
        self.originQPoint = eventQMouseEvent.pos()
        self.currentQRubberBand = QRubberBand(QRubberBand.Rectangle, self)
        self.currentQRubberBand.setGeometry(QRect(self.originQPoint, QtCore.QSize()))
        self.currentQRubberBand.show()

    def mouseMoveEvent (self, eventQMouseEvent):
        self.currentQRubberBand.setGeometry(QRect(self.originQPoint, eventQMouseEvent.pos()).normalized())

    def mouseReleaseEvent (self, eventQMouseEvent):
        self.currentQRubberBand.hide()
        currentQRect_escala = self.currentQRubberBand.geometry()
        print(currentQRect_escala)
        self.currentQRubberBand.deleteLater()
        # Pega o tamanho da proporção da imagem
        # Separa os valores
        x_escala = ((self.imagem.width()/self.width)*currentQRect_escala.x())
        y_escala = ((self.imagem.height()/self.height)*currentQRect_escala.y())
        width_escala = currentQRect_escala.width()
        width_escala_porc = ((100 * width_escala) / self.width)
        width_corte_original = (self.imagem.width() * (width_escala_porc / 100))
        height_escala = currentQRect_escala.height()
        height_escala_porc = ((100 * height_escala) / self.height)
        height_corte_original = (self.imagem.height() * (height_escala_porc / 100))
        # Corta a imagem direto da original para não perder a qualidade
        currentQRect = QRect(x_escala,y_escala,width_corte_original,height_corte_original)
        print('Qrect 2 aqui',currentQRect)
        # Salva e mostra a imagem novamente
        cropQPixmap = self.imagem.copy(currentQRect)
        cropQPixmap.save(self.nome_imagem)
        imagemCrop = QPixmap(self.nome_imagem)
        imagemCrop = imagemCrop.scaled(self.width, self.height)
        self.setPixmap(QPixmap(imagemCrop))