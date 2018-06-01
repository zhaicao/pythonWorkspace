# -*- coding: utf-8 -*-

# 定义窗口中所有事件的实现
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from eventAction import Utils

__author__='zhaicao'

class defindeActions(object):
    def __init__(self):
        pass

    # 获得数据库的类方法,可使用@classmethod修饰
    def getComboBoxDB(self, objDict, group):

        ip = objDict.getObjTextByName('input_1') if (group == 'bus') else objDict.getObjTextByName('input_7')
        port = objDict.getObjTextByName('input_2') if (group == 'bus') else objDict.getObjTextByName('input_8')
        username = objDict.getObjTextByName('input_3') if (group == 'bus') else objDict.getObjTextByName('input_9')
        pwd = objDict.getObjTextByName('input_4') if (group == 'bus') else objDict.getObjTextByName('input_10')
        dbCb = objDict.getObjByName('input_5') if (group == 'bus') else objDict.getObjByName('input_11')

        if (ip and port and username and pwd):
            reslist = ()
            try:
                ms = Utils.MSSQL(host=ip, port=port, user=username, password=pwd, login_timeout=3, timeout=3)
                reslist = ms.ExecQuery(
                    "SELECT name FROM  master..sysdatabases WHERE name NOT IN ( 'master', 'model', 'msdb', 'tempdb', 'northwind','pubs','ReportServer','ReportServerTempDB')")
            except:
                Utils.mesRemine(objDict.getWidgetObj(), '数据库连接信息不正确')
            if (reslist):
                dbCb.clear()
                for i in reslist:
                    dbCb.addItem(i[0])

    # 清空下拉框选择
    # 通过group判断业务库、历史库
    def initComboBoxDB(self, objDict, group):
        dbCb = objDict.getObjByName('input_5') if (group == 'bus') else objDict.getObjByName('input_11')
        item = '请选择业务库' if (group == 'bus') else '请选择历史库'
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
        elif (group == 'nifiLogin'):
            nameList = ('input_58', 'input_59')
        else:
            nameList = ()
        for name in nameList:
            objDict.setObjEnabled(name, state)

    # 保存数据库配置
    def saveConfStep_1(self, controlsDict, objDict):
        item = ['input_1', 'input_2', 'input_3', 'input_4', 'input_5',
                'input_12', 'input_13', 'input_14', 'input_15', 'input_16', 'input_17', 'input_18',
                'input_19', 'input_20', 'input_21', 'input_22', 'input_23']
        hisItem = ['input_7', 'input_8', 'input_9', 'input_10', 'input_11']
        # 判断历史库是否启用
        if (objDict.getObjTextByName('input_6')):
            item.extend(hisItem)

        for i in item:
            text = objDict.getObjTextByName(i)
            if text.strip() == '' or text == '请选择业务库' or text == '请选择历史库':
                return False
            controlsDict[i]['value'] = text
        controlsDict['input_6']['value'] = objDict.getObjTextByName('input_6')
        return True

    # 保存工艺参数
    def saveConfStep_2(self, controlsDict, objDict):
        if ( objDict.getObjTextByName('input_24') ):
            item = ['input_25', 'input_26', 'input_27', 'input_28',
                    'input_29', 'input_30', 'input_31', 'input_32', 'input_33', 'input_34', 'input_35',
                    'input_36', 'input_37', 'input_38']
            for i in item:
                text = objDict.getObjTextByName(i)
                if text.strip() == '':
                    return False
                controlsDict[i]['value'] = text
        controlsDict['input_24']['value'] = objDict.getObjTextByName('input_24')
        return True

    # 保存部署配置
    def saveConfStep_3(self, controlsDict, objDict):
        item = ['input_39', 'input_40', 'input_41',
                'input_42', 'input_43', 'input_44',
                'input_45', 'input_46', 'input_47']
        for i in item:
            text = objDict.getObjTextByName(i)
            if text.strip() == '' or text == '请选择业务库' or text == '请选择历史库':
                return False
            controlsDict[i]['value'] = text
        return True

    # 保存系统配置
    def saveConfStep_4(self, controlsDict, objDict):
        item = ['input_48', 'input_53', 'input_54','input_55', 'input_56']
        loginItem = ['input_50', 'input_51', 'input_52']
        nifiLoginItem = ['input_59', 'input_58']
        # 判断单点登录是否启用
        if (objDict.getObjTextByName('input_49')):
            item.extend(loginItem)
        # 判断nifi登录是否启用
        if (objDict.getObjTextByName('input_57')):
            item.extend(nifiLoginItem)

        for i in item:
            text = objDict.getObjTextByName(i)
            if text.strip() == '' or text == '请选择业务库' or text == '请选择历史库':
                return False
            controlsDict[i]['value'] = text
        controlsDict['input_49']['value'] = objDict.getObjTextByName('input_49')
        controlsDict['input_57']['value'] = objDict.getObjTextByName('input_57')
        return True

    # 工厂定制配置
    def saveConfStep_5(self, controlsDict, objDict):
        item = ['input_60', 'input_61', 'input_62','input_63', 'input_64','input_65', 'input_66', 'input_67']
        for i in item:
            controlsDict[i]['value'] = objDict.getObjBoolByName(i)
        return True


    # 保存部署配置文件
    def saveConfigFile(self, widgetObj, controlsDict, configType, title, fileType, defaultPath = 'C:/Users/slave/Desktop'):
        itemList = Utils.getConfigByType(controlsDict, configType)
        # 检查配置项是否有空
        if (not Utils.checkIsNull(itemList)):
            Utils.mesRemine(widgetObj, '请完成配置项')
            return False
        deployFile = QtWidgets.QFileDialog.getSaveFileName(widgetObj,
                                                           title,
                                                           defaultPath,
                                                           fileType)

        if (deployFile[0]):
            if( not Utils.writeFile(deployFile[0], itemList) ):
                Utils.mesRemine(widgetObj, '配置文件写入异常')
                return False
            return True
        else:
            return False