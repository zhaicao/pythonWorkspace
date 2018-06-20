# -*- coding: utf-8 -*-

# 定义控件信号所有的槽函数

__author__='zhaicao'

from eventAction.DefinedActions import TraceActions
from eventAction.Utils import  Util
from eventAction.DefinedThread import TraceGetDBThread


class TraceSolot(object):
    def __init__(self):
        self._action = TraceActions()

    # 设置输入框不可读
    def cbSetEnabledSlot(self, objDict, group):
        obj = objDict.getWidgetObj()
        sender = obj.sender()
        state = sender.isChecked()
        if (group == 'his'):
            nameList = ('dep_input_7', 'dep_input_8', 'dep_input_9', 'dep_input_10', 'dep_input_11', 'getDBBtn_2')
        elif (group == 'pp'):
            nameList = (
                'dep_input_25', 'dep_input_26', 'dep_input_27', 'dep_input_28', 'dep_input_29', 'dep_input_30',
                'dep_input_31', 'dep_input_32',
                'dep_input_33', 'dep_input_34', 'dep_input_49')
        elif (group == 'login'):
            nameList = ('dep_input_46', 'dep_input_47', 'dep_input_48')
        elif (group == 'nifiLogin'):
            nameList = ('dep_input_54', 'dep_input_55')
        elif (group == 'ppNet'):
            nameList = ('dep_input_26', 'dep_input_27', 'dep_input_28', 'dep_input_29')
        elif (group == 'db_pp'):
            nameList = ('db_input_12', 'db_input_13', 'db_input_14', 'db_input_15', 'db_input_16')
        elif (group == 'nifi_history'):
            nameList = ('nifi_input_12', 'nifi_input_13', 'nifi_input_14', 'nifi_input_15', 'nifi_input_16', 'getDBBtn_5')
        elif (group == 'nifi_pp'):
            nameList = ('nifi_input_18', 'nifi_input_19', 'nifi_input_20', 'nifi_input_21', 'nifi_input_22', 'getDBBtn_6')
        elif (group == 'nifi_islogin'):
            nameList = ('nifi_input_26', 'nifi_input_27')
        else:
            nameList = ()
        for name in nameList:
            objDict.setObjEnabled(name, state)

    # 更改Next按钮显示的槽函数
    def buttonChange(self, tabWidgetObj, comfirmBtn, depBtn, manBtn):
        if (tabWidgetObj.currentIndex() > (tabWidgetObj.count() - 2)):
            depBtn.show()
            manBtn.show()
            comfirmBtn.setText('保存')
        else:
            depBtn.hide()
            manBtn.hide()
            comfirmBtn.setText('下一步')

    # 下一步切换tab的槽函数
    def nextClicked(self, mainWidgetObj, tabWidgetObj, btnObj, depBtn, manBtn, deployItems, manifestItems, objsDict):
        pos = tabWidgetObj.currentIndex()
        tabCount = tabWidgetObj.count()
        if (pos < (tabCount - 1)):
            # 数据库下一步Check
            if (pos == 0):
                if not self._action.saveConfStep_1(objsDict):
                    Util.mesInfomation(mainWidgetObj, '输入\选择项不能为空，请输入')
                    return
            # 工艺参数下一步Check
            elif (pos == 1):
                if not self._action.saveConfStep_2(objsDict):
                    Util.mesInfomation(mainWidgetObj, '输入项不能为空，请输入')
                    return
            elif (pos == 2):
                if not self._action.saveConfStep_3(objsDict):
                    Util.mesInfomation(mainWidgetObj, '输入项不能为空，请输入')
                    return
            elif (pos == 3):
                if not self._action.saveConfStep_4(objsDict):
                    Util.mesInfomation(mainWidgetObj, '输入项不能为空，请输入')
                    return
            else:
                print('配置完成')
            # 改变按钮显示
            self.buttonChange(tabWidgetObj, btnObj, depBtn, manBtn)
            # 切换下一个tab
            tabWidgetObj.setCurrentIndex(tabWidgetObj.currentIndex() + 1)
        else:
            # 保存检查部署配置文件并获得部署配置的List
            deployList = self._action.getDeployConfValue(deployItems, objsDict)
            if (not deployList):
                Util.mesInfomation(mainWidgetObj, '请完善配置项')
            else:
                # 获得工厂定制的配置List
                manifestList = self._action.getManifestConfValue(manifestItems, deployItems, objsDict)
                # 保存部署配置文件
                if not self._action.saveConfItemsFile(mainWidgetObj, deployList, '请选择部署配置文件保存路径', 'YML Files(*.yml)',
                                                      'EXTRA VARIABLES.yml'):
                    return
                Util.mesInfomation(mainWidgetObj, '部署配置文件保存成功，请选择工厂定制文件保存路径')
                # 保存工厂定制文件
                if not self._action.saveConfItemsFile(mainWidgetObj, manifestList, '请选择工厂定制文件保存路径',
                                                      'PROPERTIES Files(*.properties)', 'manifest.properties', '='):
                    return
                Util.mesInfomation(mainWidgetObj, '保存成功')


    # 复制到剪贴板
    def copyConfClipboard(self, mainWidgetObj, type, deployItems, manifestItems, objsDict):
        if type == 'deploy':
            deployItems = self._action.getDeployConfValue(deployItems, objsDict)
            if (not deployItems):
                Util.mesInfomation(mainWidgetObj, '请完善部署配置项')
                return
            else:
                Util.copyClipboardText(Util.listToStr(deployItems))
                Util.mesInfomation(mainWidgetObj, '复制成功')
        elif type == 'manifest':
            manifestItems = self._action.getManifestConfValue(manifestItems, deployItems, objsDict)
            # 获得配置写入到系统剪贴板中
            Util.copyClipboardText(Util.listToStr(manifestItems, '='))
            Util.mesInfomation(mainWidgetObj, '复制成功')
        else:
            print('复制类型不存在')


    # 设置下拉框数据库
    def setDBNameList(self, mainWidgetObj, dbInfo, cbObj):
        # 实例化线程
        self.getDbThread = TraceGetDBThread(WidgetObj=mainWidgetObj, dbInfo=dbInfo, cbObj=cbObj)
        # 线程执行完毕绑定信号槽
        self.getDbThread.trigger.connect(self._action.setComboBoxDB)
        # 开始线程
        self.getDbThread.start()

    # 切换菜单页面
    def changeMenuPage(self, sWidgetObj, index):
        sWidgetObj.setCurrentIndex(index)

    # 获取Nifi模板
    def getNifiTemplate(self, mainWidgetObj, objsDict):
        file = self._action.getFileFullPath(mainWidgetObj, 'Nifi抽取模板', 'Xml Files(*.xml)')
        if file:
            objsDict.setObjTextByName('nifi_input_28', file)

    # 建立完整的追溯库
    def createFullDB(self, mainWidgetObj):
        Util.mesInfomation(mainWidgetObj, 'DB')

    # 更新NIfi模板
    def updateNifiTemplate(self, mainWidgetObj, nifiConfItems, objsDict):
        nifiList = self._action.getNifiConfValue(nifiConfItems, objsDict)
        if not nifiList:
            Util.mesInfomation(mainWidgetObj, '请完善输入\选择项')
        else:
            if self._action.updateNifiTemplate(nifiList):
                Util.mesInfomation(mainWidgetObj, 'Nifi抽取模板更新成功')
            else:
                Util.mesInfomation(mainWidgetObj, '更新失败')


