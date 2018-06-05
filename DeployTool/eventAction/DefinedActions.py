# -*- coding: utf-8 -*-

# 定义窗口/槽函数中所有动作的实现

__author__='zhaicao'

from PyQt5 import QtWidgets
from eventAction.Utils import Util, MSSQL
import copy

class TraceActions(object):

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
                ms = MSSQL(host=ip, port=port, user=username, password=pwd, login_timeout=3, timeout=3)
                reslist = ms.ExecQuery(
                    "SELECT name FROM  master..sysdatabases WHERE name NOT IN ( 'master', 'model', 'msdb', 'tempdb', 'northwind','pubs','ReportServer','ReportServerTempDB')")
            except:
                Util.mesRemine(objDict.getWidgetObj(), '数据库连接信息不正确')
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
            nameList = ('input_24', 'input_25', 'input_26', 'input_27', 'input_28', 'input_29', 'input_30', 'input_31', 'input_32',
                        'input_33', 'input_34', 'input_35', 'input_36', 'input_37', 'input_38', 'input_53')
        elif( group == 'login' ):
            nameList = ('input_50', 'input_51', 'input_52')
        elif (group == 'nifiLogin'):
            nameList = ('input_58', 'input_59')
        elif (group == 'ppNet'):
            nameList = ('input_25', 'input_26', 'input_27', 'input_28')
        else:
            nameList = ()
        for name in nameList:
            objDict.setObjEnabled(name, state)

    # 检查数据库配置
    def saveConfStep_1(self, objDict):
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
        return True

    # 检查工艺参数
    def saveConfStep_2(self, objDict):
        ppEnable, ppNetEnable = objDict.getObjTextByName('input_72'), objDict.getObjTextByName('input_24')
        item = []
        if ( ppNetEnable and ppEnable):
            item.extend(['input_25', 'input_26', 'input_27', 'input_28'])
        if ( ppEnable ):
            item.extend(['input_29', 'input_30', 'input_31', 'input_32', 'input_33', 'input_34', 'input_35',
                    'input_36', 'input_37', 'input_38'])
        for i in item:
            text = objDict.getObjTextByName(i)
            if text.strip() == '':
                return False
        return True

    # 检查部署配置
    def saveConfStep_3(self, objDict):
        item = ['input_39', 'input_40', 'input_41',
                'input_42', 'input_43', 'input_44',
                'input_45', 'input_46', 'input_47']
        for i in item:
            text = objDict.getObjTextByName(i)
            if text.strip() == '':
                return False
        return True

    # 检查系统配置
    def saveConfStep_4(self, objDict):
        item = ['input_48', 'input_54','input_55', 'input_56']
        loginItem = ['input_50', 'input_51', 'input_52']
        nifiLoginItem = ['input_59', 'input_58']
        ppItem = ['input_53']
        # 判断单点登录是否启用
        if (objDict.getObjTextByName('input_49')):
            item.extend(loginItem)
        # 判断nifi登录是否启用
        if (objDict.getObjTextByName('input_57')):
            item.extend(nifiLoginItem)
        # 判断工艺参数是否启用
        if (objDict.getObjTextByName('input_72')):
            item.extend(ppItem)

        for i in item:
            text = objDict.getObjTextByName(i)
            if text.strip() == '':
                return False
        return True


    # 保存部署配置文件
    def saveConfItemsFile(self, widgetObj, configItem, title, fileType, defaultFilename, defaultPath = Util.getWinDesktop()):
        deployFile = QtWidgets.QFileDialog.getSaveFileName(widgetObj,
                                                           title,
                                                           defaultPath + '\\' + defaultFilename,
                                                           fileType)

        if (deployFile[0]):
            if( not Util.writeFile(deployFile[0], configItem) ):
                Util.mesRemine(widgetObj, '配置文件写入异常')
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
        hisEnable, ppEnable, ppNetEnable, loginEnable, EtlLoginEnable = objDict.getObjTextByName('input_6'), \
                                                                        objDict.getObjTextByName('input_72'),\
                                                                        objDict.getObjTextByName('input_24'),\
                                                                        objDict.getObjTextByName('input_49'),\
                                                                        objDict.getObjTextByName('input_57')
        # 判断是否存在不需要的项，统计加到exceptControls中
        if (not hisEnable):
            exceptItems.extend(['input_7', 'input_8', 'input_9', 'input_10', 'input_11'])
        if (not ppEnable):
            exceptItems.extend(['input_24', 'input_25', 'input_26', 'input_27', 'input_28', 'input_29', 'input_30', 'input_31',
                                   'input_32', 'input_33', 'input_34', 'input_35', 'input_36', 'input_37', 'input_38', 'input_53'])
        if (not loginEnable):
            exceptItems.extend(['input_50', 'input_51', 'input_52'])
        if (not EtlLoginEnable):
            exceptItems.extend(['input_58', 'input_59'])
        if (not ppNetEnable and ppEnable):
            exceptItems.extend(['input_25', 'input_26','input_27','input_28'])
        for i, k in controls.items():
            obj = objDict.getObjByName(i)
            if (i not in exceptItems):
                text = objDict.getTextByObj(obj)
                # 判断是输入项or选择项
                if (not isinstance(text, bool)):
                    if text.strip() == '' or text == '请选择业务库' or text == '请选择历史库':
                        return False
                    else:
                        # 为工艺参数、抽取频率加单位
                        if( i == 'input_37' or i == 'input_38'):
                            text +='MB'
                        if( i == 'input_56' ):
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
        controls['input_72'] = depConfDict['input_72']
        controls['input_49'] = depConfDict['input_49']
        for i in controls:
            if i == 'input_72' or i == 'input_49':
                controls[i]['value'] = str.lower(str(objDict.getObjTextByName(i)))
            else:
                controls[i]['value'] = str.lower(str(objDict.getObjBoolByName(i)))

        return list(controls.values())