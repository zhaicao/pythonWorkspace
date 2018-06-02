# -*- coding: utf-8 -*-

# 基础工具方法

__author__='zhaicao'


import pymssql
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
import copy, winreg

class MSSQL:
    def __init__(self,**kwargs):
        self.dbInfo = kwargs

    def __GetConnect(self):
        self.conn = pymssql.connect(**self.dbInfo,charset = "utf8")
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur

    #返回查询结果
    def ExecQuery(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()
        self.conn.close()
        return resList

    # 执行sql
    def ExecNonQuery(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()



# 通过对象名找对象
class GetObject(object):
    def __init__(self, widgetObj, *objDict):
        self.__widgetObj = widgetObj
        self.__objDict = dict()
        # dict取并集
        for i in objDict:
            self.__objDict = dict(self.__objDict,**i)


    def getObjByName(self, objName):
        return self.__widgetObj.findChild(self.__objDict[objName]['objType'], objName)


    def getObjTextByName(self, objName):
        obj = self.__widgetObj.findChild(self.__objDict[objName]['objType'], objName)
        if isinstance(obj, QtWidgets.QComboBox):
            return obj.currentText()
        elif isinstance(obj, QtWidgets.QLineEdit):
            return obj.text()
        elif isinstance(obj, QtWidgets.QCheckBox):
            return obj.checkState() == Qt.Checked
        else:
            return None

    def getObjBoolByName(self, objName):
        obj = self.__widgetObj.findChild(self.__objDict[objName]['objType'], objName)
        return bool(obj.currentIndex())

    def getWidgetObj(self):
        return self.__widgetObj

    def setObjEnabled(self, objName, state):
        self.__widgetObj.findChild(self.__objDict[objName]['objType'], objName).setEnabled(state)

    def getTextByObj(self, obj):
        if isinstance(obj, QtWidgets.QComboBox):
            return obj.currentText()
        elif isinstance(obj, QtWidgets.QLineEdit):
            return obj.text()
        elif isinstance(obj, QtWidgets.QCheckBox):
            return obj.checkState() == Qt.Checked
        else:
            return None

# 提示消息
def mesRemine(widgetObj, message, title = '提示'):
    QtWidgets.QMessageBox.information(widgetObj,
                                      title,
                                      message,
                                      QtWidgets.QMessageBox.Yes)

# dict写文件
def writeFile(filepath, fileData):
    f = open(filepath, 'w')
    try:
        for i in fileData:
            f.write('%s=%s' % (i['confItem'], i['value']) + '\n')
    except Exception as e:
        print(e)
        return False
    finally:
        f.close()
    return True

# 获得Win桌面路径
def getWinDesktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, \
                          r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders', )
    return winreg.QueryValueEx(key, "Desktop")[0]







if __name__=='__main__':
    print(getWinDesktop())
    pass
    # reslist = ()
    # try:
    #     ms = MSSQL(host = "1",user = "1", password = "1", login_timeout=3)
    #     reslist = ms.ExecQuery(
    #         "SELECT name FROM  master..sysdatabases WHERE name NOT IN ( 'master', 'model', 'msdb', 'tempdb', 'northwind','pubs' )")
    # except pymssql.InterfaceError:
    #     print('数据库连接信息不正确')
    # except pymssql.OperationalError:
    #     print('数据库操作异常')
    # #reslist = ms.ExecQuery("SELECT Name FROM SysObjects Where XType='U' ORDER BY Name")
