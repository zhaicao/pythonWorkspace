# -*- coding: utf-8 -*-

# 定义控件信号所有的槽函数

__author__='zhaicao'

from eventAction.DefinedActions import TraceActions
from eventAction.Utils import  Util

class TraceSolot(object):
    def __init__(self):
        self._action = TraceActions()

    # 更改Next按钮显示的槽函数
    def buttonChange(self, tabWidgetObj, btnObj):
        if (tabWidgetObj.currentIndex() > (tabWidgetObj.count() - 2)):
            btnObj.setText('保存')
        else:
            btnObj.setText('下一步')

    # 下一步切换tab的槽函数
    def nextClicked(self, mainWidgetObj, tabWidgetObj, btnObj, deployItems, manifestItems, objsDict):
        # 改变按钮显示
        self.buttonChange(tabWidgetObj, btnObj)
        pos = tabWidgetObj.currentIndex()
        tabCount = tabWidgetObj.count()
        if (pos < (tabCount - 1)):
            # 数据库下一步Check
            if (pos == 0):
                if not self._action.saveConfStep_1(objsDict):
                    Util.mesRemine(mainWidgetObj, '输入\选择项不能为空，请输入')
                    return
            # 工艺参数下一步Check
            elif (pos == 1):
                if not self._action.saveConfStep_2(objsDict):
                    Util.mesRemine(mainWidgetObj, '输入项不能为空，请输入')
                    return
            elif (pos == 2):
                if not self._action.saveConfStep_3(objsDict):
                    Util.mesRemine(mainWidgetObj, '输入项不能为空，请输入')
                    return
            elif (pos == 3):
                if not self._action.saveConfStep_4(objsDict):
                    Util.mesRemine(mainWidgetObj, '输入项不能为空，请输入')
                    return
            else:
                print('配置完成')
            # 切换下一个tab
            tabWidgetObj.setCurrentIndex(tabWidgetObj.currentIndex() + 1)
        else:
            # 保存检查部署配置文件
            deployItems = self._action.getDeployConfValue(deployItems, objsDict)
            if (not deployItems):
                Util.mesRemine(mainWidgetObj, '请完善配置项')
            else:
                manifestItems = self._action.getManifestConfValue(manifestItems, objsDict)
                # 保存部署配置文件
                if not self._action.saveConfItemsFile(mainWidgetObj, deployItems, '请选择部署配置文件保存路径', 'YML Files(*.yml)',
                                                      'EXTRA VARIABLES.yml'):
                    return
                Util.mesRemine(mainWidgetObj, '部署配置文件保存成功，请选择工厂定制文件保存路径')
                # 保存工厂定制文件
                if not self._action.saveConfItemsFile(mainWidgetObj, manifestItems, '请选择工厂定制文件保存路径',
                                                      'PROPERTIES Files(*.properties)', 'manifest.properties'):
                    return
                Util.mesRemine(mainWidgetObj, '保存成功')