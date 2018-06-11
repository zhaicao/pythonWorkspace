# -*- coding: utf-8 -*-

# 基础公共模块

__author__='zhaicao'

import pymssql
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
import winreg
import os

# SqlServer访问类
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



# 对象库，封装对象的基本操作
class ObjRepository(object):
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

# 基础公用类
class Util(object):
    # 提示确认消息，自定义消息框
    @classmethod
    def mesInfomation(self, widgetObj, message,title = '提示', *args):
        mesbox = QtWidgets.QMessageBox(widgetObj)
        mesbox.setWindowTitle(title)
        mesbox.setText(message)
        # 判断按钮，有则加入按钮
        if len(args) == 0:
            mesbox.addButton('好', QtWidgets.QMessageBox.ActionRole)
        else:
            for i in args:
                mesbox.addButton(i, QtWidgets.QMessageBox.ActionRole)
        mesbox.exec_()
        return mesbox

    # classmethod
    @classmethod
    def writeFile(cls, filepath, fileData):
        f = open(filepath, 'w')
        try:
            for i in fileData:
                f.write('%s: %s' % (str(i['confItem']), str(i['value'])) + '\n')
        except Exception as e:
            print(e)
            return False
        finally:
            f.close()
        return True

    # 配置dict转str
    @classmethod
    def listToStr(cls, confList):
        reStr = ''
        for i in confList:
            reStr += '%s: %s' % (str(i['confItem']), str(i['value'])) + '\n'
        return reStr
    # 获得Win桌面路径
    @classmethod
    def getWinDesktop(cls):
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, \
                          r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders', )
        return winreg.QueryValueEx(key, "Desktop")[0]

    # 复制文本至剪贴板
    @classmethod
    def copyClipboardText(self, Text):
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(str(Text))

    # 复制图像至剪贴板
    @classmethod
    def copyClipboardImage(self, image):
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setPixmap(QtGui.QPixmap(os.path.join(os.path.dirname(__file__), image)))

    # 复制HTML至剪贴板
    @classmethod
    def copyHtml(self, html):
        mimeData = QtCore.QMimeData()
        mimeData.setHtml(html)
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setMimeData(mimeData)


if __name__ == '__main__':
    a = "python"
    Util().setClipboardText(a)
    print(Util.getClipboardText())
