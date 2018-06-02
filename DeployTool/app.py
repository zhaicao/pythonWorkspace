
# 程序入口

__author__='zhaicao'

import sys
from PyQt5 import QtWidgets
from mainUI import TraceMainWidget

#对QWidget重写方法
class QWidget(QtWidgets.QWidget):
    def __init__(self):
            super().__init__()

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, '提示', '确定要退出吗？', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
        app = QtWidgets.QApplication(sys.argv)
        #定义为重写后的QWidget
        w = QWidget()
        ui = TraceMainWidget()
        ui.setupUi(w)
        w.show()
        sys.exit(app.exec_())