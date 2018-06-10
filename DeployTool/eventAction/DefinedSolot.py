# -*- coding: utf-8 -*-

# 定义控件信号所有的槽函数

__author__='zhaicao'

from eventAction.DefinedActions import TraceActions
from eventAction.Utils import  Util
from eventAction.DefinedThread import TraceGetDBThread


class TraceSolot(object):
    def __init__(self):
        self._action = TraceActions()

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
                                                      'PROPERTIES Files(*.properties)', 'manifest.properties'):
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
            Util.copyClipboardText(Util.listToStr(manifestItems))
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

