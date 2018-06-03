# -*- coding: utf-8 -*-

# 窗体主函数

__author__='zhaicao'

from PyQt5 import QtCore, QtGui, QtWidgets
from DeployTool.frameUI.CreateControls import TraceControlsUI
from DeployTool.frameUI.CreateTextUI import TraceCreateTextUI
from DeployTool.eventAction.DefinedActions import TraceActions
from DeployTool.eventAction.DefinedSolot import TraceSolot
from DeployTool.eventAction.Utils import ObjRepository
# 引入图标资源文件
from DeployTool.frameUI import resoure_rc

class TraceMainWidget(TraceControlsUI, TraceCreateTextUI):
    # 初始化窗口
    def setupUi(self, mainWidget):
        #定义Logo和帮助图标
        logoIcon = QtGui.QIcon()
        logoIcon.addPixmap(QtGui.QPixmap(":/icon/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.helpIcon = QtGui.QPixmap(":/icon/help.png")

        mainWidget.setWindowTitle("追溯分析系统部署工具")
        mainWidget.setObjectName("mainWidget")
        mainWidget.resize(500, 640)
        mainWidget.setWindowIcon(logoIcon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(mainWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

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
        self._objsDict = ObjRepository(mainWidget, self.deployConfItem, self.manifestConfItem)
        # 初始化事件
        self._action = TraceActions()
        # 初始化槽函数
        self._solot = TraceSolot()


    # 控件信号
    def connectSignal(self, mainWidget):
        # 绑定切换页签的信号槽
        self.tabWidget.currentChanged.connect(lambda: self._solot.buttonChange(self.tabWidget, self.confirmBtn))
        # 定义Next按钮信号槽
        self.confirmBtn.clicked.connect(lambda: self._solot.nextClicked(mainWidget, self.tabWidget, self.confirmBtn, self.deployConfItem, self.manifestConfItem, self._objsDict))
        # Cancel按钮信号绑定退出槽函数
        self.cancelBtn.clicked.connect(mainWidget.close)
        # 是否抽历史库checkbox绑定信号槽
        self.input_6.stateChanged.connect(lambda: self._action.cbSetEnabledSlot(self._objsDict, 'his'))
        # 是否抽工艺参数checkbox绑定信号槽
        self.input_24.stateChanged.connect(lambda: self._action.cbSetEnabledSlot(self._objsDict, 'pp'))
        # 是否启用单点登录绑定信号槽
        self.input_49.stateChanged.connect(lambda: self._action.cbSetEnabledSlot(self._objsDict, 'login'))
        # 是否启用Nifi登录绑定信号槽
        self.input_57.stateChanged.connect(lambda: self._action.cbSetEnabledSlot(self._objsDict, 'nifiLogin'))

        # 获取业务库，联动
        # 业务库测试按钮绑定信号槽
        self.getDBBtn_1.clicked.connect(lambda: self._action.getComboBoxDB(self._objsDict, 'bus'))

        # 输入框修改初始化下拉框数据
        self.input_1.textChanged.connect(lambda: self._action.initComboBoxDB(self._objsDict, 'bus'))
        self.input_2.textChanged.connect(lambda: self._action.initComboBoxDB(self._objsDict, 'bus'))
        self.input_3.textChanged.connect(lambda: self._action.initComboBoxDB(self._objsDict, 'bus'))
        self.input_4.textChanged.connect(lambda: self._action.initComboBoxDB(self._objsDict, 'bus'))

        # 获取历史库，联动
        # 历史库测试绑定信号槽
        self.getDBBtn_2.clicked.connect(lambda: self._action.getComboBoxDB(self._objsDict, 'his'))

        # 输入框修改初始化下拉框数据
        self.input_7.textChanged.connect(lambda: self._action.initComboBoxDB(self._objsDict, 'his'))
        self.input_8.textChanged.connect(lambda: self._action.initComboBoxDB(self._objsDict, 'his'))
        self.input_9.textChanged.connect(lambda: self._action.initComboBoxDB(self._objsDict, 'his'))
        self.input_10.textChanged.connect(lambda: self._action.initComboBoxDB(self._objsDict, 'his'))