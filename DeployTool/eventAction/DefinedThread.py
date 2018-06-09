# -*- coding: utf-8 -*-

# 申明线程类

__author__ = 'zhaicao'

from PyQt5 import QtCore, QtWidgets
from eventAction.DefinedActions import TraceActions

# 定义追溯分析获得数据库线程
class TraceGetDBThread(QtCore.QThread):
    # 定义执行完的信号
    trigger = QtCore.pyqtSignal(list, QtWidgets.QComboBox, QtWidgets.QWidget)

    def __init__(self, WidgetObj, dbInfo, cbObj, parent=None):
        super().__init__()
        self.cbObj = cbObj
        self.dbInfo = dbInfo
        self.WidgetObj = WidgetObj

    # 执行线程
    def run(self):
        result = TraceActions().getComboBoxDB(self.dbInfo)
        # 执行完返回信号
        self.trigger.emit(result, self.cbObj, self.WidgetObj)
        self.quit()