
__author__='zhaicao'

import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication

class simple(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI_2()

    #按钮提示
    def initUI_1(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn = QPushButton('按钮', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')

        btn.resize(btn.sizeHint())

        btn.move(50, 50)

        self.setGeometry(500, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()

    #按钮事件
    def initUI_2(self):
        qBtn  = QPushButton('退出', self)
        qBtn.clicked.connect(QCoreApplication.instance().quit)
        qBtn.resize(qBtn.sizeHint())
        qBtn.move(50, 50)

        self.setGeometry(500, 300, 300, 200)
        self.setWindowTitle('按钮事件')
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = simple()
    sys.exit(app.exec_())