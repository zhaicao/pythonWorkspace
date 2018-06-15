# -*- coding: utf-8 -*-

# 程序入口

__author__='zhaicao'

import sys
from PyQt5 import QtWidgets
from frameUI.mainUI import TraceMainWidget
from eventAction.Utils import Util
# 主函数导入pymssql相关模块，否则pyinstaller打包报错
import _mssql
import uuid
import decimal


#对QWidget重写方法
class QMainWindow(QtWidgets.QMainWindow):
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
        #实例化重写后的QWidget
        m = QMainWindow()
        ui = TraceMainWidget()
        ui.setupUi(m)
        m.show()
        sys.exit(app.exec_())
