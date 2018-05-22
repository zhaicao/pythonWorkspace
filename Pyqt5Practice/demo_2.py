
__author__='zhaicao'

import sys
from PyQt5 import QtWidgets, QtGui

class Example(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口的位置和大小
        self.setGeometry(300, 300, 300, 220)
        # 设置窗口的标题
        self.setWindowTitle('Icon')
        # 设置窗口的图标，引用当前目录下的web.png图片
        self.setWindowIcon(QtGui.QIcon('web.png'))

        # 显示窗口
        self.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Example()
    sys.exit(app.exec_())