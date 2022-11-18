import random
import sys
import random

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(200, 330, 100, 40))
        self.btn.setObjectName("btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn.setText(_translate("MainWindow", "Кнопка"))


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.is_on = False
        self.setupUi(self)
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
            for _ in range(25):
                qp.setPen(QColor(*[random.randint(1, 255) for _ in range(3)]))
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
