# -*- coding: utf-8 -*-

# 窗体主函数

__author__='zhaicao'

from PyQt5 import QtCore, QtGui, QtWidgets
from CreateControls import ControlsUI
from CreateTextUI import CreateTextUI
from definedActions import defindeActions
from eventAction.Utils import *


class Ui_mainWidget(ControlsUI, CreateTextUI):
    def __init__(self):
        # 定义空间类型和名称对应的字典
        self.controlsDict = {
            # 业务库Group
            'input_1': QtWidgets.QLineEdit,
            'input_2': QtWidgets.QLineEdit,
            'input_3': QtWidgets.QLineEdit,
            'input_4': QtWidgets.QLineEdit,
            'input_5': QtWidgets.QComboBox,
            'getDBBtn_1': QtWidgets.QPushButton,
            # 历史库Group
            'input_6': QtWidgets.QCheckBox,
            'input_7': QtWidgets.QLineEdit,
            'input_8': QtWidgets.QLineEdit,
            'input_9': QtWidgets.QLineEdit,
            'input_10': QtWidgets.QLineEdit,
            'input_11': QtWidgets.QComboBox,
            'getDBBtn_2': QtWidgets.QPushButton,
            # BI库Group
            'input_12': QtWidgets.QLineEdit,
            'input_13': QtWidgets.QLineEdit,
            'input_14': QtWidgets.QLineEdit,
            'input_15': QtWidgets.QLineEdit,
            'input_16': QtWidgets.QLineEdit,
            'input_17': QtWidgets.QLineEdit,
            'input_18': QtWidgets.QLineEdit,
            # 系统库Group
            'input_19': QtWidgets.QLineEdit,
            'input_20': QtWidgets.QLineEdit,
            'input_21': QtWidgets.QLineEdit,
            'input_22': QtWidgets.QLineEdit,
            'input_23': QtWidgets.QLineEdit,
            # 工艺参数Group
            'input_24': QtWidgets.QCheckBox,
            'input_25': QtWidgets.QLineEdit,
            'input_26': QtWidgets.QLineEdit,
            'input_27': QtWidgets.QLineEdit,
            'input_28': QtWidgets.QLineEdit,
            # 工艺参数库
            'input_29': QtWidgets.QLineEdit,
            'input_30': QtWidgets.QLineEdit,
            'input_31': QtWidgets.QLineEdit,
            'input_32': QtWidgets.QLineEdit,
            'input_33': QtWidgets.QLineEdit,
            'input_34': QtWidgets.QLineEdit,
            'input_35': QtWidgets.QLineEdit,
            'input_36': QtWidgets.QLineEdit,
            'input_37': QtWidgets.QLineEdit,
            'input_38': QtWidgets.QLineEdit,
            # 基础配置
            'input_39': QtWidgets.QLineEdit,
            'input_40': QtWidgets.QLineEdit,
            'input_41': QtWidgets.QLineEdit,
            # 部署程序
            'input_42': QtWidgets.QLineEdit,
            'input_43': QtWidgets.QLineEdit,
            'input_44': QtWidgets.QLineEdit,
            # 部署地址
            'input_45': QtWidgets.QLineEdit,
            'input_46': QtWidgets.QLineEdit,
            'input_47': QtWidgets.QLineEdit,
            # 基础配置
            'input_48': QtWidgets.QLineEdit,
            # 单点登录
            'input_49': QtWidgets.QCheckBox,
            'input_50': QtWidgets.QLineEdit,
            'input_51': QtWidgets.QLineEdit,
            'input_52': QtWidgets.QLineEdit,
            # ETL配置
            'input_53': QtWidgets.QLineEdit,
            'input_54': QtWidgets.QLineEdit,
            'input_55': QtWidgets.QLineEdit,
            'input_56': QtWidgets.QLineEdit,
            'input_57': QtWidgets.QCheckBox,
            'input_58': QtWidgets.QLineEdit,
            'input_59': QtWidgets.QLineEdit,
            # 工厂定制
            'input_60': QtWidgets.QComboBox,
            'input_61': QtWidgets.QComboBox,
            'input_62': QtWidgets.QComboBox,
            'input_63': QtWidgets.QComboBox,
            'input_64': QtWidgets.QComboBox,
            'input_65': QtWidgets.QComboBox,
            'input_66': QtWidgets.QComboBox,
            'input_67': QtWidgets.QComboBox,
            'input_68': QtWidgets.QComboBox,
        }

        self.configs = dict()

    # 初始化UI
    def setupUi(self, mainWidget):
        #相关图标
        logoIcon = QtGui.QIcon()
        logoIcon.addPixmap(QtGui.QPixmap("icon/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.objsDict = GetObject(mainWidget, self.controlsDict)

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
            self.confirmBtn.setText('完成')
        else:
            self.confirmBtn.setText('Next')

    # 下一步切换tab的槽函数
    def nextClicked(self, pos, tabObj, widgetObj):
        # 改变按钮显示
        self.buttonChange(pos)
        if (pos < (tabObj.count() - 1)):
            if (pos == 0):
                print('1')
                self._action.saveDBConf(self.objsDict, self.configs)
            elif (pos == 1):
                print('系统数据库完成')
            elif (pos == 2):
                print('Nifi配置完成')
            elif (pos == 3):
                print('Nifi配置完成')
            else:
                print('工厂定制配置完成')
            tabObj.setCurrentIndex(pos + 1)
            print(self.configs)
        else:
            print('完成')