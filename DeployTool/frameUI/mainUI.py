# -*- coding: utf-8 -*-

# 窗体主函数

__author__='zhaicao'

from PyQt5 import QtCore, QtGui, QtWidgets
from CreateControls import ControlsUI
from CreateTextUI import CreateTextUI
from definedActions import defindeActions
from eventAction.Utils import *
import copy


class Ui_mainWidget(ControlsUI, CreateTextUI):
    def __init__(self):
        # 定义部署配置控件类型和名称对应的字典
        self.deployConfItem = {
            # 业务库Group
            'input_1': {'objType': QtWidgets.QLineEdit, 'confItem': 'MIOT_Database_Host'},
            'input_2': {'objType': QtWidgets.QLineEdit, 'confItem': 'MIOT_Database_Port'},
            'input_3': {'objType': QtWidgets.QLineEdit, 'confItem': 'MIOT_Database_Username'},
            'input_4': {'objType': QtWidgets.QLineEdit, 'confItem': 'MIOT_Database_Password'},
            'input_5': {'objType': QtWidgets.QComboBox, 'confItem': 'MIOT_Database_Name'},
            'getDBBtn_1': {'objType': QtWidgets.QPushButton},
            # 历史库Group
            'input_6': {'objType': QtWidgets.QCheckBox, 'confItem': 'isExtractHis'},
            'input_7': {'objType': QtWidgets.QLineEdit, 'confItem': 'HIS_Database_Host'},
            'input_8': {'objType': QtWidgets.QLineEdit, 'confItem': 'HIS_Database_Port'},
            'input_9': {'objType': QtWidgets.QLineEdit, 'confItem': 'HIS_Database_Username'},
            'input_10': {'objType': QtWidgets.QLineEdit, 'confItem': 'HIS_Database_Password'},
            'input_11': {'objType': QtWidgets.QComboBox, 'confItem': 'HIS_Database_Name'},
            'getDBBtn_2': {'objType': QtWidgets.QPushButton},
            # BI库Group
            'input_12': {'objType': QtWidgets.QLineEdit, 'confItem': 'BI_Database_Host'},
            'input_13': {'objType': QtWidgets.QLineEdit, 'confItem': 'BI_Database_Port'},
            'input_14': {'objType': QtWidgets.QLineEdit, 'confItem': 'BI_Database_Username'},
            'input_15': {'objType': QtWidgets.QLineEdit, 'confItem': 'BI_Database_Password'},
            'input_16': {'objType': QtWidgets.QLineEdit, 'confItem': 'BI_Database_Name'},
            'input_17': {'objType': QtWidgets.QLineEdit, 'confItem': 'extractSourceId'},
            'input_18': {'objType': QtWidgets.QLineEdit, 'confItem': 'extractSourceName'},
            # 系统库Group
            'input_19': {'objType': QtWidgets.QLineEdit, 'confItem': 'DAS_Database_Host'},
            'input_20': {'objType': QtWidgets.QLineEdit, 'confItem': 'DAS_Database_Port'},
            'input_21': {'objType': QtWidgets.QLineEdit, 'confItem': 'DAS_Database_Username'},
            'input_22': {'objType': QtWidgets.QLineEdit, 'confItem': 'DAS_Database_Password'},
            'input_23': {'objType': QtWidgets.QLineEdit, 'confItem': 'DAS_Database_Name'},
            # 工艺参数Group
            'input_24': {'objType': QtWidgets.QCheckBox, 'confItem': 'processParameter'},
            'input_25': {'objType': QtWidgets.QLineEdit, 'confItem': 'PPDBFile_path'},
            'input_26': {'objType': QtWidgets.QLineEdit, 'confItem': 'PPDBFile_dir'},
            'input_27': {'objType': QtWidgets.QLineEdit, 'confItem': 'PPDBFile_username'},
            'input_28': {'objType': QtWidgets.QLineEdit, 'confItem': 'PPDBFile_password'},
            # 工艺参数库
            'input_29': {'objType': QtWidgets.QLineEdit, 'confItem': 'PP_Database_Host'},
            'input_30': {'objType': QtWidgets.QLineEdit, 'confItem': 'PP_Database_Port'},
            'input_31': {'objType': QtWidgets.QLineEdit, 'confItem': 'PP_Database_Username'},
            'input_32': {'objType': QtWidgets.QLineEdit, 'confItem': 'PP_Database_Password'},
            'input_33': {'objType': QtWidgets.QLineEdit, 'confItem': 'PP_Database_Name'},
            'input_34': {'objType': QtWidgets.QLineEdit, 'confItem': 'REPLACE_DB_FILE_DIR'},
            'input_35': {'objType': QtWidgets.QLineEdit, 'confItem': 'REPLACE_START_MONTH'},
            'input_36': {'objType': QtWidgets.QLineEdit, 'confItem': 'REPLACE_END_MONTH'},
            'input_37': {'objType': QtWidgets.QLineEdit, 'confItem': 'REPLACE_DB_FILE_INIT_SIZE'},
            'input_38': {'objType': QtWidgets.QLineEdit, 'confItem': 'REPLACE_DB_FILE_GROWTH_SIZE'},
            # 基础配置
            'input_39': {'objType': QtWidgets.QLineEdit, 'confItem': 'release_ver'},
            'input_40': {'objType': QtWidgets.QLineEdit, 'confItem': 'operation_host'},
            'input_41': {'objType': QtWidgets.QLineEdit, 'confItem': 'operation_portal'},
            # 部署程序
            'input_42': {'objType': QtWidgets.QLineEdit, 'confItem': 'deliverable_dir_path'},
            'input_43': {'objType': QtWidgets.QLineEdit, 'confItem': 'deliverable_username'},
            'input_44': {'objType': QtWidgets.QLineEdit, 'confItem': 'deliverable_password'},
            # 部署地址
            'input_45': {'objType': QtWidgets.QLineEdit, 'confItem': 'dest_path'},
            'input_46': {'objType': QtWidgets.QLineEdit, 'confItem': 'tools_path'},
            'input_47': {'objType': QtWidgets.QLineEdit, 'confItem': 'script_path'},
            # 基础配置
            'input_48': {'objType': QtWidgets.QLineEdit, 'confItem': 'tomcat_port'},
            # 单点登录
            'input_49': {'objType': QtWidgets.QCheckBox, 'confItem': 'ssoLogin'},
            'input_50': {'objType': QtWidgets.QLineEdit, 'confItem': 'system_auth_login_host_default'},
            'input_51': {'objType': QtWidgets.QLineEdit, 'confItem': 'system_auth_login_portal'},
            'input_52': {'objType': QtWidgets.QLineEdit, 'confItem': 'system_auth_login_api_portal'},
            # ETL配置
            'input_53': {'objType': QtWidgets.QLineEdit, 'confItem': 'ppDir'},
            'input_54': {'objType': QtWidgets.QLineEdit, 'confItem': 'nifi_port'},
            'input_55': {'objType': QtWidgets.QLineEdit, 'confItem': 'nifi_JVM'},
            'input_56': {'objType': QtWidgets.QLineEdit, 'confItem': 'biIncrementSchedule'},
            'input_57': {'objType': QtWidgets.QCheckBox, 'confItem': 'nifi_auth_enable'},
            'input_58': {'objType': QtWidgets.QLineEdit, 'confItem': 'nifi_username'},
            'input_59': {'objType': QtWidgets.QLineEdit, 'confItem': 'nifi_password'}
        }
        # 定义工厂定制控件类型和名称对应的字典
        self.manifestConfItem =  {
            'input_60': {'objType': QtWidgets.QComboBox, 'confItem': 'isOpDbBeforeRefact'},
            'input_61': {'objType': QtWidgets.QComboBox, 'confItem': 'supression'},
            'input_62': {'objType': QtWidgets.QComboBox, 'confItem': 'equipmentMaintenance'},
            'input_63': {'objType': QtWidgets.QComboBox, 'confItem': 'toolManagement'},
            'input_64': {'objType': QtWidgets.QComboBox, 'confItem': 'fgb'},
            'input_65': {'objType': QtWidgets.QComboBox, 'confItem': 'isVideoMonitorEnabled'},
            'input_66': {'objType': QtWidgets.QComboBox, 'confItem': 'linkRepair'},
            'input_67': {'objType': QtWidgets.QComboBox, 'confItem': 'isAutoOrderFiltered'}
        }
    # 初始化UI
    def setupUi(self, mainWidget):
        #相关图标
        logoIcon = QtGui.QIcon()
        logoIcon.addPixmap(QtGui.QPixmap("icon/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.helpIcon = QtGui.QPixmap("icon/help.png")

        mainWidget.setWindowTitle("追溯分析系统部署工具")
        mainWidget.setObjectName("mainWidget")
        mainWidget.resize(500, 640)
        mainWidget.setWindowIcon(logoIcon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(mainWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.helpIcon = QtGui.QPixmap("icon/help.png")
        self.tabWidget = QtWidgets.QTabWidget(mainWidget)
        self.tabWidget.setObjectName("tabWidget")

        #调用父类生成tabWidget中的控件
        super().createTabControls(self.tabWidget)

        self.verticalLayout.addWidget(self.tabWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        # Next&finish按钮
        self.confirmBtn = QtWidgets.QPushButton(mainWidget)
        self.confirmBtn.setObjectName("confirmBtn")
        self.horizontalLayout.addWidget(self.confirmBtn)
        # 取消按钮
        self.cancelBtn = QtWidgets.QPushButton(mainWidget)
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout.addWidget(self.cancelBtn)

        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWidget)

        # 初始化控件文字、帮助提示和默认值
        super().createTabTexts()
        # 初始化控件信号槽
        self.connectSignal(mainWidget)

        # 初始化控件库
        self.objsDict = GetObject(mainWidget, self.deployConfItem, self.manifestConfItem)

        self._action = defindeActions()


    # 控件信号槽
    def connectSignal(self, mainWidget):
        # 定义事件类

        # 绑定切换页签的信号槽
        self.tabWidget.currentChanged[int].connect(self.buttonChange)
        # 定义Next按钮信号槽
        self.confirmBtn.clicked.connect(lambda: self.nextClicked(self.tabWidget.currentIndex(), self.tabWidget, mainWidget))
        # Cancel按钮信号绑定退出槽函数
        self.cancelBtn.clicked.connect(mainWidget.close)
        # 是否抽历史库checkbox绑定信号槽
        self.input_6.stateChanged.connect(lambda: self._action.cbSetEnabledSlot(self.objsDict, 'his'))
        # 是否抽工艺参数checkbox绑定信号槽
        self.input_24.stateChanged.connect(lambda: self._action.cbSetEnabledSlot(self.objsDict, 'pp'))
        # 是否启用单点登录绑定信号槽
        self.input_49.stateChanged.connect(lambda: self._action.cbSetEnabledSlot(self.objsDict, 'login'))
        # 是否启用Nifi登录绑定信号槽
        self.input_57.stateChanged.connect(lambda: self._action.cbSetEnabledSlot(self.objsDict, 'nifiLogin'))

        # 获取业务库，联动
        # 业务库测试绑定信号槽
        self.getDBBtn_1.clicked.connect(lambda: self._action.getComboBoxDB(self.objsDict, 'bus'))

        # 输入框修改初始化下拉框数据
        self.input_1.textChanged.connect(lambda: self._action.initComboBoxDB(self.objsDict, 'bus'))
        self.input_2.textChanged.connect(lambda: self._action.initComboBoxDB(self.objsDict, 'bus'))
        self.input_3.textChanged.connect(lambda: self._action.initComboBoxDB(self.objsDict, 'bus'))
        self.input_4.textChanged.connect(lambda: self._action.initComboBoxDB(self.objsDict, 'bus'))

        # 获取历史库，联动
        # 历史库测试绑定信号槽
        self.getDBBtn_2.clicked.connect(lambda: self._action.getComboBoxDB(self.objsDict, 'his'))

        # 输入框修改初始化下拉框数据
        self.input_7.textChanged.connect(lambda: self._action.initComboBoxDB(self.objsDict, 'his'))
        self.input_8.textChanged.connect(lambda: self._action.initComboBoxDB(self.objsDict, 'his'))
        self.input_9.textChanged.connect(lambda: self._action.initComboBoxDB(self.objsDict, 'his'))
        self.input_10.textChanged.connect(lambda: self._action.initComboBoxDB(self.objsDict, 'his'))



    # 更改Next按钮显示的槽函数
    def buttonChange(self, pos):
        if (pos > (self.tabWidget.count() - 2)):
            self.confirmBtn.setText('保存')
        else:
            self.confirmBtn.setText('下一步')

    # 下一步切换tab的槽函数
    def nextClicked(self, pos, tabObj, widgetObj):
        # 改变按钮显示
        self.buttonChange(pos)
        if (pos < (tabObj.count() - 1)):
            # 数据库下一步Check
            if (pos == 0):
                if not self._action.saveConfStep_1(self.deployConfItem, self.objsDict):
                    mesRemine(widgetObj, '输入\选择项不能为空，请输入')
                    return
            # 工艺参数下一步Check
            elif (pos == 1):
                if not self._action.saveConfStep_2(self.deployConfItem, self.objsDict):
                    mesRemine(widgetObj, '输入项不能为空，请输入')
                    return
            elif (pos == 2):
                if not self._action.saveConfStep_3(self.deployConfItem, self.objsDict):
                    mesRemine(widgetObj, '输入项不能为空，请输入')
                    return
            elif (pos == 3):
                if not self._action.saveConfStep_4(self.deployConfItem, self.objsDict):
                    mesRemine(widgetObj, '输入项不能为空，请输入')
                    return
            else:
                print('配置完成')
            # 切换下一个tab
            tabObj.setCurrentIndex(pos + 1)
        else:
            # 保存检查部署配置文件
            deployItems = self._action.getDeployConfValue(self.deployConfItem, self.objsDict)
            if( not deployItems ):
                mesRemine(widgetObj, '请完善配置项')
            else:
                manifestItems = self._action.getManifestConfValue(self.manifestConfItem, self.objsDict)
                # 保存部署配置文件
                if not self._action.saveConfItemsFile(widgetObj, deployItems, '请选择部署配置文件保存路径', 'YML Files(*.yml)', 'tracedeploy.yml'):
                    return
                mesRemine(widgetObj, '部署配置文件保存成功，请选择工厂定制文件保存路径')
                # 保存工厂定制文件
                if not self._action.saveConfItemsFile(widgetObj, manifestItems, '请选择工厂定制文件保存路径', 'PROPERTIES Files(*.properties)', 'manifest.properties'):
                    return
                mesRemine(widgetObj, '保存成功')
