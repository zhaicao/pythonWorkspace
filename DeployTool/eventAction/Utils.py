# -*- coding: utf-8 -*-

# 基础工具方法

__author__='zhaicao'


import sys, pymssql
from PyQt5.QtWidgets import QLineEdit, QComboBox

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
    def __init__(self, widgetObj, objDict):
        self.__widgetObj = widgetObj
        self.__objDict = objDict


    def getObjByName(self, objName):
        return self.__widgetObj.findChild(self.__objDict[objName], objName)


    def getObjTextByName(self, objName):
        obj = self.__widgetObj.findChild(self.__objDict[objName], objName)
        if isinstance(obj, QComboBox):
            return obj.currentText()
        elif isinstance(obj, QLineEdit):
            return obj.text()
        else:
            return None


    def getWidgetObj(self):
        return self.__widgetObj


    def setObjEnabled(self, objName, state):
        self.__widgetObj.findChild(self.__objDict[objName], objName).setEnabled(state)



if __name__=='__main__':
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
