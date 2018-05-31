# -*- coding: utf-8 -*-

# 定义窗口中所有事件的实现
from PyQt5 import QtCore, QtGui, QtWidgets
from eventAction.Utils import *

__author__='zhaicao'

class defindeActions(object):
    def __init__(self):
        pass

    # 获得数据库的类方法,可使用@classmethod修饰
    def getComboBoxDB(self, objDict, group):

        ip = objDict.getObjTextByName('input_1') if group == 'bus' else objDict.getObjTextByName('input_7')
        port = objDict.getObjTextByName('input_2') if group == 'bus' else objDict.getObjTextByName('input_8')
        username = objDict.getObjTextByName('input_3') if group == 'bus' else objDict.getObjTextByName('input_9')
        pwd = objDict.getObjTextByName('input_4') if group == 'bus' else objDict.getObjTextByName('input_10')
        dbCb = objDict.getObjByName('input_5') if group == 'bus' else objDict.getObjByName('input_11')
        if (ip and port and username and pwd):
            reslist = ()
            try:
                ms = MSSQL(host=ip, port=port, user=username, password=pwd, login_timeout=3, timeout=3)
                reslist = ms.ExecQuery(
                    "SELECT name FROM  master..sysdatabases WHERE name NOT IN ( 'master', 'model', 'msdb', 'tempdb', 'northwind','pubs','ReportServer','ReportServerTempDB')")
            except:
                QtWidgets.QMessageBox.information(objDict.getWidgetObj(),
                                                "提示",
                                                "数据库连接信息不正确",
                                                QtWidgets.QMessageBox.Yes)
            if (reslist):
                dbCb.clear()
                for i in reslist:
                    dbCb.addItem(i[0])

    # 清空下拉框选择
    # 通过group判断业务库、历史库
    def initComboBoxDB(self, objDict, group):
        dbCb = objDict.getObjByName('input_5') if group == 'bus' else objDict.getObjByName('input_11')
        item = '请选择业务库' if group == 'bus' else '请选择历史库'
        dbCb.clear()
        dbCb.addItem(item)

    # 设置输入框不可读
    def cbSetEnabledSlot(self, objDict, group):
        obj = objDict.getWidgetObj()
        sender = obj.sender()
        state = sender.isChecked()
        if(group == 'his' ):
            nameList = ('input_7', 'input_8', 'input_9', 'input_10', 'input_11', 'getDBBtn_2')
        elif( group == 'pp' ):
            nameList = ('input_25', 'input_26', 'input_27', 'input_28', 'input_29', 'input_30', 'input_31', 'input_32',
                        'input_33', 'input_34', 'input_35', 'input_36', 'input_37', 'input_38')
        elif( group == 'login' ):
            nameList = ('input_50', 'input_51', 'input_52')
        else:
            nameList = ()

        for name in nameList:
            objDict.setObjEnabled(name, state)