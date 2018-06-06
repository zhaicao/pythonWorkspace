
# 程序入口

__author__='zhaicao'

import sys
from PyQt5 import QtWidgets
from frameUI.mainUI import TraceMainWidget
from Utils import Util
# 主函数导入pymssql相关模块，否则pyinstaller打包报错
import _mssql
import uuid
import decimal


#对QWidget重写方法
class QWidget(QtWidgets.QWidget):
    def __init__(self):
            super().__init__()

    def closeEvent(self, event):
        reply = Util.mesInfomation(self, '确定要退出吗？', '提示', '是', '否')
        if reply.clickedButton().text() == '是':
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