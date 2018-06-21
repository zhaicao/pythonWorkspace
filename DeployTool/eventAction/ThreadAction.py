# -*- coding: utf-8 -*-

# 申明使用线程的子类

__author__ = 'zhaicao'

from PyQt5 import QtCore, QtWidgets
from eventAction.DefinedActions import TraceActions

# 获得数据库列表的子类
class DBThread(QtCore.QObject):
    # 自定义信号
    finishDBListSignal = QtCore.pyqtSignal(list, QtWidgets.QComboBox, QtWidgets.QWidget)
    # 自定义停止线程信号
    stopThreadSignal = QtCore.pyqtSignal()
    # 构造函数
    def __init__(self, WidgetObj, dbInfo, cbObj, btnObj, parent=None):
        super().__init__()
        self.cbObj = cbObj
        self.dbInfo = dbInfo
        self.WidgetObj = WidgetObj
        self.btnObj = btnObj

    # 获得数据库List
    def getDBList(self):
        # 改变按钮禁用
        self.btnObj.setEnabled(False)
        self.btnObj.setText('连接中')
        # 获得数据库List
        result = TraceActions().getDBList(self.dbInfo)
        # 发送完成信号
        self.finishDBListSignal.emit(result, self.cbObj, self.WidgetObj)
        # 改变按钮可用
        self.btnObj.setEnabled(True)
        self.btnObj.setText('连接')
        # 停止线程信号
        self.stopThreadSignal.emit()

# Nifi异步操作的子类
class NifiThread(QtCore.QObject):
    # 自定义信号
    finishSignal = QtCore.pyqtSignal(QtWidgets.QWidget, bool)
    # 自定义停止线程信号
    stopThreadSignal = QtCore.pyqtSignal()
    # 构造函数
    def __init__(self, WidgetObj, nifiConfList, btnObj, parent=None):
        super().__init__()
        self.WidgetObj = WidgetObj
        self.nifiConfList = nifiConfList
        self.btnObj = btnObj

    def updateNifiTemplate(self):
        # 改变按钮禁用
        self.btnObj.setEnabled(False)
        self.btnObj.setText('更新中...')
        result = TraceActions().updateNifiTemplate(self.nifiConfList, self.WidgetObj)
        # 发送完成信号
        self.finishSignal.emit(self.WidgetObj, result)
        # 改变按钮禁用
        self.btnObj.setEnabled(True)
        self.btnObj.setText('更新抽取模板')
        self.stopThreadSignal.emit()