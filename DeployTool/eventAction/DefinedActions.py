# -*- coding: utf-8 -*-

# 定义窗口/槽函数中所有动作的实现

__author__='zhaicao'

from PyQt5 import QtWidgets
from eventAction.Utils import Util, MSSQL
import copy

class TraceActions(object):

    # 获得数据库的类方法,可使用@classmethod修饰
    def getDBList(self, dbInfo):

        if (dbInfo['ip'] and dbInfo['port'] and dbInfo['user'] and dbInfo['pwd']):
            try:
                ms = MSSQL(host=dbInfo['ip'], port=dbInfo['port'], user=dbInfo['user'], password=dbInfo['pwd'], login_timeout=10, timeout=5)
                resList = ms.ExecQuery(
                    "SELECT name FROM  master..sysdatabases WHERE name NOT IN ( 'master', 'model', 'msdb', 'tempdb', 'northwind','pubs','ReportServer','ReportServerTempDB')")
            except:
                return ['Error']
            return resList
        else:
            return ['None']

    # 设置数据库下拉框数据
    def setComboBoxDB(self, dataList, cbObj, WidgetObj):

        if dataList[0] == 'Error':
            Util.mesInfomation(WidgetObj, '数据库信息不正确')
        elif dataList[0] == 'None':
            Util.mesInfomation(WidgetObj, '请完善数据库连接信息')
        else:
            cbObj.clear()
            for i in dataList:
                cbObj.addItem(i[0])


    # 清空下拉框选择
    # 通过group判断业务库、历史库
    def initComboBoxDB(self, cbObj, cbitem):
        cbObj.clear()
        cbObj.addItem(cbitem)

    # 设置输入框不可读
    def cbSetEnabledSlot(self, objDict, group):
        obj = objDict.getWidgetObj()
        sender = obj.sender()
        state = sender.isChecked()
        if(group == 'his' ):
            nameList = ('dep_input_7', 'dep_input_8', 'dep_input_9', 'dep_input_10', 'dep_input_11', 'getDBBtn_2')
        elif( group == 'pp' ):
            nameList = ('dep_input_25', 'dep_input_26', 'dep_input_27', 'dep_input_28', 'dep_input_29', 'dep_input_30', 'dep_input_31', 'dep_input_32',
                        'dep_input_33', 'dep_input_34', 'dep_input_49')
        elif( group == 'login' ):
            nameList = ('dep_input_46', 'dep_input_47', 'dep_input_48')
        elif (group == 'nifiLogin'):
            nameList = ('dep_input_54', 'dep_input_55')
        elif (group == 'ppNet'):
            nameList = ('dep_input_26', 'dep_input_27', 'dep_input_28', 'dep_input_29')
        else:
            nameList = ()
        for name in nameList:
            objDict.setObjEnabled(name, state)

    # 检查数据库配置
    def saveConfStep_1(self, objDict):
        item = ['dep_input_1', 'dep_input_2', 'dep_input_3', 'dep_input_4', 'dep_input_5',
                'dep_input_12', 'dep_input_13', 'dep_input_14', 'dep_input_15', 'dep_input_16', 'dep_input_17', 'dep_input_18',
                'dep_input_19', 'dep_input_20', 'dep_input_21', 'dep_input_22', 'dep_input_23']
        hisItem = ['dep_input_7', 'dep_input_8', 'dep_input_9', 'dep_input_10', 'dep_input_11']
        # 判断历史库是否启用
        if (objDict.getObjTextByName('dep_input_6')):
            item.extend(hisItem)

        for i in item:
            text = objDict.getObjTextByName(i)
            if text.strip() == '' or text == '请选择业务库' or text == '请选择历史库':
                return False
        return True

    # 检查工艺参数
    def saveConfStep_2(self, objDict):
        ppEnable, ppNetEnable = objDict.getObjTextByName('dep_input_24'), objDict.getObjTextByName('dep_input_25')
        item = []
        if ( ppNetEnable and ppEnable):
            item.extend(['dep_input_26', 'dep_input_27', 'dep_input_28', 'dep_input_29'])
        if ( ppEnable ):
            item.extend(['dep_input_30', 'dep_input_31', 'dep_input_32', 'dep_input_33', 'dep_input_34'])
        for i in item:
            text = objDict.getObjTextByName(i)
            if text.strip() == '':
                return False
        return True

    # 检查部署配置
    def saveConfStep_3(self, objDict):
        item = ['dep_input_35', 'dep_input_36', 'dep_input_37',
                'dep_input_38', 'dep_input_39', 'dep_input_40',
                'dep_input_41', 'dep_input_42', 'dep_input_43']
        for i in item:
            text = objDict.getObjTextByName(i)
            if text.strip() == '':
                return False
        return True

    # 检查系统配置
    def saveConfStep_4(self, objDict):
        item = ['dep_input_44', 'dep_input_50','dep_input_51', 'dep_input_52']
        loginItem = ['dep_input_46', 'dep_input_47', 'dep_input_48']
        nifiLoginItem = ['dep_input_54', 'dep_input_55']
        ppItem = ['dep_input_49']
        # 判断单点登录是否启用
        if (objDict.getObjTextByName('dep_input_45')):
            item.extend(loginItem)
        # 判断nifi登录是否启用
        if (objDict.getObjTextByName('dep_input_53')):
            item.extend(nifiLoginItem)
        # 判断工艺参数是否启用
        if (objDict.getObjTextByName('dep_input_24')):
            item.extend(ppItem)

        for i in item:
            text = objDict.getObjTextByName(i)
            if text.strip() == '':
                return False
        return True


    # 保存部署配置文件
    def saveConfItemsFile(self, widgetObj, configItem, title, fileType, defaultFilename, connector = ":", defaultPath = Util.getWinDesktop()):
        deployFile = QtWidgets.QFileDialog.getSaveFileName(widgetObj,
                                                           title,
                                                           defaultPath + '\\' + defaultFilename,
                                                           fileType)

        if (deployFile[0]):
            if( not Util.writeFile(deployFile[0], configItem, connector) ):
                Util.mesInfomation(widgetObj, '配置文件写入异常')
                return False
            return True
        else:
            return False

    # 保存并检查所有的部署配置项到dict中
    def getDeployConfValue(self, confDict, objDict):
        controls = copy.copy(confDict)
        controls.pop('getDBBtn_1')
        controls.pop('getDBBtn_2')
        exceptItems = []
        hisEnable, ppEnable, ppNetEnable, loginEnable, EtlLoginEnable = objDict.getObjTextByName('dep_input_6'), \
                                                                        objDict.getObjTextByName('dep_input_24'),\
                                                                        objDict.getObjTextByName('dep_input_25'),\
                                                                        objDict.getObjTextByName('dep_input_45'),\
                                                                        objDict.getObjTextByName('dep_input_53')
        # 判断是否存在不需要的项，统计加到exceptControls中
        if (not hisEnable):
            exceptItems.extend(['dep_input_7', 'dep_input_8', 'dep_input_9', 'dep_input_10', 'dep_input_11'])
        if (not ppEnable):
            exceptItems.extend(['dep_input_25', 'dep_input_26', 'dep_input_27', 'dep_input_28', 'dep_input_29', 'dep_input_30', 'dep_input_31', 'dep_input_32',
                                   'dep_input_33', 'dep_input_34', 'dep_input_49'])
        if (not loginEnable):
            exceptItems.extend(['dep_input_46', 'dep_input_47', 'dep_input_48'])
        if (not EtlLoginEnable):
            exceptItems.extend(['dep_input_54', 'dep_input_55'])
        if (not ppNetEnable and ppEnable):
            exceptItems.extend(['dep_input_26', 'dep_input_27','dep_input_28','dep_input_29'])
        for i, k in controls.items():
            obj = objDict.getObjByName(i)
            if (i not in exceptItems):
                text = objDict.getTextByObj(obj)
                # 判断是输入项or选择项
                if (not isinstance(text, bool)):
                    if text.strip() == '' or text == '请选择业务库' or text == '请选择历史库':
                        return False
                    else:
                        # 抽取频率加单位
                        if( i == 'dep_input_56' ):
                            text +=' min'
                        controls[i]['value'] = text
                else:
                    # True 和 False转小写
                    controls[i]['value'] = str.lower(str(text))
            else:
                controls[i]['value'] = ''
        return list(controls.values())


    # 获得所有工厂定制配置项
    def getManifestConfValue(self, maniConfDict, depConfDict, objDict):
        controls = copy.deepcopy(maniConfDict)
        controls['dep_input_24'] = depConfDict['dep_input_24']
        controls['dep_input_45'] = depConfDict['dep_input_45']
        for i in controls:
            if i == 'dep_input_24' or i == 'dep_input_45':
                controls[i]['value'] = str.lower(str(objDict.getObjTextByName(i)))
            else:
                controls[i]['value'] = str.lower(str(objDict.getObjBoolByName(i)))

        return list(controls.values())