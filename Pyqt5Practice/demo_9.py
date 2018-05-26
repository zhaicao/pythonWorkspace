
__author__='zhaicao'

import sys
from PyQt5.QtWidgets import (QWidget, QCheckBox, QApplication, QPushButton, QFrame, QSlider, QLabel, QProgressBar, QCalendarWidget,
                             QHBoxLayout, QLineEdit, QSplitter, QComboBox)
from PyQt5.QtCore import Qt, QBasicTimer, QDate
from PyQt5.QtGui import QColor,QPixmap

#复选框
class simple_1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cb = QCheckBox('Show Title', self)
        cb.move(20,20)
        #复选框选择
        cb.toggle()

        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Checkbox')
        self.show()

    #槽函数接受信号状态
    #Qt.Checked选择
    #Qt.PartiallyChecked半选
    #QT.Unchecked未选
    def changeTitle(self, state):
        print(state)
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('')


#按钮控件
class simple_2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.col = QColor(0, 0, 0)

        redb = QPushButton('Red', self)
        #将button设置为可选。
        redb.setCheckable(True)
        redb.move(10, 10)
        #将button点击信号的布尔值传给槽函数setColor
        redb.clicked[bool].connect(self.setColor)

        greenb = QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(10, 60)

        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(10, 110)

        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" %
                                  self.col.name())

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Toggle button')
        self.show()

    #设置颜色槽函数
    def setColor(self, pressed):
        #获得信号源对象，按钮
        source = self.sender()
        #判断是否选中
        if pressed:
            val = 255
        else:
            val = 0
        #若是红色按钮，则QColor对象setRed
        if source.text() == "Red":
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)
        self.square.setStyleSheet("QFrame { background-color: %s }" %
                                      self.col.name())

#声音调节
class simple_3(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        sld = QSlider(Qt.Horizontal, self)
        #设置无焦距
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)

        self.lable = QLabel(self)
        self.lable.setPixmap(QPixmap('web.png'))
        self.lable.setGeometry(160, 40, 80, 30)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QSlider')
        self.show()

    def changeValue(self, value):
        if value == 0:
            self.lable.setPixmap(QPixmap('web.png'))
        elif value > 0 and value <= 30:
            self.lable.setPixmap(QPixmap('web.png'))
        elif value > 30 and value < 80:
            self.lable.setPixmap(QPixmap(''))
        else:
            self.lable.setPixmap(QPixmap('web.png'))


#进度条
class simple_4(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn =QPushButton('start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QSlider')
        self.show()

    #重载定时器
    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
        self.step += 1
        self.pbar.setValue(self.step)


    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            #设置时间间隔，每隔多少毫秒调用timerEvent一次
            self.timer.start(100, self)
            self.btn.setText('Stop')

#日历控件
class simple_5(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20, 20)
        cal.clicked[QDate].connect(self.showDate)

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(130, 260)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()


    def showDate(self, date):
        self.lbl.setText(date.toString())


#QPixmap优化图像
class simple_6(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap('web.png')

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)


        self.move(300, 200)
        self.setWindowTitle('Red Rock')
        self.show()


#文本框
class simple_7(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        qle = QLineEdit(self)

        qle.move(60, 100)
        self.lbl.move(60, 40)

        qle.textChanged[str].connect(self.onChanged)


        self.move(300, 200)
        self.setWindowTitle('Red Rock')
        self.show()

    def onChanged(self, value):
        self.lbl.setText(value)
        self.lbl.adjustSize()


#QSplitter
class simple_8(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)

        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        splitter2 = QSplitter(Qt.Horizontal)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()

#下拉框
class simple_9(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel("Ubuntu", self)
        combo = QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Arch")
        combo.addItem("Gentoo")

        combo.move(50, 50)
        self.lbl.move(50, 150)

        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QComboBox')
        self.show()

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    s = simple_9()
    sys.exit(app.exec_())

