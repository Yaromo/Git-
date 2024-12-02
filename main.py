import sys
from random import randint
from PyQt6.QtGui import QPainter, QColor, QBrush
from PyQt6.QtCore import Qt, QPoint
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.drawf)
    
    def paintEvent(self, a0):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()
        self.flag = False

    def drawf(self):
        self.flag = True
        self.update()

    def draw(self):
        num = randint(20, 100)
        self.qp.setBrush(QColor(255, 255, 0))
        self.qp.drawEllipse(QPoint(200, 210), num, num)
        
                
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Window()
    form.show()
    sys.exit(app.exec())