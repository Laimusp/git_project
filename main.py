import random
import sys
import math

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor, QPainterPath
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtWidgets import QApplication, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.is_on = False
        uic.loadUi('circle.ui', self)
        self.initUI()

    def initUI(self):
        self.btn.clicked.connect(self.update_window)

    def update_window(self):
        self.is_on = True
        self.repaint()

    def paintEvent(self, event):
        if self.is_on:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(250, 210, 1))
            for _ in range(25):
                self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        side = random.randint(10, 150)
        x, y = random.randint(1, 500), random.randint(1, 300)
        qp.drawEllipse(x - (side // 2), y - (side // 2), side, side)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    program = Example()
    program.show()
    sys.exit(app.exec())
