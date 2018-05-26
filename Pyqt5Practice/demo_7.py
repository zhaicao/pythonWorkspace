
__author__ = 'zhaicao'

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLCDNumber, QSlider, QPushButton, QMainWindow
from PyQt5.QtCore import Qt, QObject, pyqtSignal


class simple(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    #信号槽
    def initUI(self):
        lcd = QLCDNumber()
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)

        #QSlider的valueChanged信号，槽函数dispaly
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal & slot')
        self.show()


class simple_2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event Handler')
        self.show()
    #重写keyPressEvent函数
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Escape:
            self.close()


class simple_3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('Button 1', self)
        btn1.move(30, 50)

        btn2 = QPushButton('Button 2', self)
        btn2.move(150, 50)

        #绑定信号槽
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Event Handler')
        self.show()

    def buttonClicked(self):
        #获得信号源本身对象
        sender = self.sender()
        print(sender.width())
        self.statusBar().showMessage(sender.text() + ' was pressed')


#自定义信号
class Communicate(QObject):
    #定义不带参数的信号
    closeApp = pyqtSignal()


class simple_4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.c = Communicate()
        #绑定信号和槽函数
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Event Handler')
        self.show()

    #定义鼠标点击事件
    def mousePressEvent(self, event):
        #发射自定义的信号，通过emit发射信号
        self.c.closeApp.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = simple_4()
    sys.exit(app.exec_())