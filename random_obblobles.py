import sys

from random import randint
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 500)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(500, 500))
        self.widget.setMaximumSize(QSize(500, 500))
        self.draw = QPushButton(self.widget)
        self.draw.setObjectName(u"draw")
        self.draw.setGeometry(QRect(144, 390, 181, 23))

        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"obbloble", None))
        self.draw.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0440\u0438\u0441\u043e\u0432\u0430\u0442\u044c \u043a\u0440\u0443\u0433\u043b\u0430\u043d \u0441\u043b\u0443\u0447\u0430\u0439\u043d\u044b\u0439", None))
    # retranslateUi


OBBLOBLES = 10


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.draw.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_obbloble(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_obbloble(self, qp):
        qp.setPen(QColor('black'))
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        for i in range(OBBLOBLES):
            diameter = randint(1, 100)
            qp.drawEllipse(QPoint(randint(0, 500), randint(0, 350)), diameter, diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
