# -*- coding: utf-8 -*-

__author__='zhaicao'

from PyQt5 import QtCore, QtGui, QtWidgets
from frameUI.CreateControls import TraceControlsUI
from frameUI.CreateTextUI import TraceCreateTextUI
from frameUI.MainData import TraceObjItems
from eventAction.DefinedActions import TraceActions
from eventAction.DefinedSolot import TraceSolot
from eventAction.Utils import ObjRepository
from frameUI import resoure_rc

class TraceMainWidget(TraceControlsUI, TraceCreateTextUI, TraceObjItems):
    def setupUi(self, MainWindow):
        # 主窗口设置
        MainWindow.setWindowTitle("追溯分析部署配置工具 V2.0.6(Bate)")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 660)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(".QGroupBox {border-radius: 3px;border: 1px solid #BFBFBF;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        # 设置菜单
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 23))
        self.menubar.setObjectName("menubar")
        # 部署菜单
        self.menuDeploy = QtWidgets.QMenu(self.menubar)
        self.menuDeploy.setObjectName("menuDeploy")
        # 更新菜单
        self.menuUpdate = QtWidgets.QMenu(self.menubar)
        self.menuUpdate.setObjectName("menuUpdate")
        MainWindow.setMenuBar(self.menubar)
        # 部署菜单子菜单
        self.firstDeploy = QtWidgets.QAction(MainWindow)
        self.firstDeploy.setObjectName("firstDeploy")
        self.menuDeploy.addAction(self.firstDeploy)
        # 升级菜单子菜单
        self.updateDB = QtWidgets.QAction(MainWindow)
        self.updateDB.setObjectName("updateDB")
        self.menuUpdate.addAction(self.updateDB)

        self.updateNifi = QtWidgets.QAction(MainWindow)
        self.updateNifi.setObjectName("updateNifi")
        self.menuUpdate.addAction(self.updateNifi)

        self.menubar.addAction(self.menuDeploy.menuAction())
        self.menubar.addAction(self.menuUpdate.menuAction())
        # 生成控件
        super().initControls(self.stackedWidget)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 生成控件文字显示
        super().initControlTexts()
        # 生成控件名和对象关联dict
        super().initObjItems()
        # 初始化菜单切换信号槽
        self.connSignalMenu()
        # 初始化第一个页面控件信号槽
        self.connSignalPage_1(MainWindow)
        # 初始化第两个页面控件信号槽
        self.connSignalPage_2(MainWindow)
        # 初始化第三个页面控件信号槽
        self.connSignalPage_3(MainWindow)
        # 初始化控件库
        self._objsDict = ObjRepository(MainWindow, self.deployConfItem, self.manifestConfItem, self.dbConfItem, self.nifiConfItem)
        # 初始化事件
        self._action = TraceActions()
        # 初始化槽函数
        self._solot = TraceSolot()


    # 公共信号
    def connSignalMenu(self):
        self.firstDeploy.triggered.connect(lambda: self._solot.changeMenuPage(self.stackedWidget, 0))
        self.updateDB.triggered.connect(lambda: self._solot.changeMenuPage(self.stackedWidget, 1))
        self.updateNifi.triggered.connect(lambda: self._solot.changeMenuPage(self.stackedWidget, 2))

    # 控件信号
    def connSignalPage_1(self, mainWidget):
        # 绑定切换页签的信号槽
        self.tabWidget.currentChanged.connect(
            lambda: self._solot.buttonChange(self.tabWidget, self.dep_confirmBtn, self.dep_copyDepBtn, self.dep_copyManBtn))
        # 定义Next按钮信号槽
        self.dep_confirmBtn.clicked.connect(
            lambda: self._solot.nextClicked(mainWidget, self.tabWidget, self.dep_confirmBtn, self.dep_copyDepBtn,
                                            self.dep_copyManBtn, self.deployConfItem, self.manifestConfItem,
                                            self._objsDict))
        # 定义复制部署按钮信号槽
        self.dep_copyDepBtn.clicked.connect(
            lambda: self._solot.copyConfClipboard(mainWidget, 'deploy', self.deployConfItem, self.manifestConfItem,
                                                  self._objsDict))
        # 定义复制定制按钮信号槽
        self.dep_copyManBtn.clicked.connect(
            lambda: self._solot.copyConfClipboard(mainWidget, 'manifest', self.deployConfItem, self.manifestConfItem,
                                                  self._objsDict))
        # Cancel按钮信号绑定退出槽函数
        self.dep_cancelBtn.clicked.connect(mainWidget.close)
        # 是否抽历史库checkbox绑定信号槽
        self.dep_input_6.stateChanged.connect(lambda: self._solot.cbSetEnabledSlot(self._objsDict, 'his'))
        # 是否抽工艺参数checkbox绑定信号槽
        self.dep_input_24.stateChanged.connect(lambda: self._solot.cbSetEnabledSlot(self._objsDict, 'pp'))
        # 工艺参数是否支持网络访问checkbox绑定信号槽
        self.dep_input_25.stateChanged.connect(lambda: self._solot.cbSetEnabledSlot(self._objsDict, 'ppNet'))
        # 是否启用单点登录绑定信号槽
        self.dep_input_45.stateChanged.connect(lambda: self._solot.cbSetEnabledSlot(self._objsDict, 'login'))
        # 是否启用Nifi登录绑定信号槽
        self.dep_input_53.stateChanged.connect(lambda: self._solot.cbSetEnabledSlot(self._objsDict, 'nifiLogin'))

        # 获取业务库，联动
        # 业务库测试按钮绑定信号槽
        self.getDBBtn_1.clicked.connect(lambda: self._solot.setDBNameList(mainWidget,
                                                                          {
                                                                              'ip': self.dep_input_1.text(),
                                                                              'port': self.dep_input_2.text(),
                                                                              'user': self.dep_input_3.text(),
                                                                              'pwd': self.dep_input_4.text(),
                                                                          },
                                                                          self.dep_input_5))
        # 输入框修改初始化下拉框数据
        self.dep_input_1.textChanged.connect(lambda: self._action.initComboBoxDB(self.dep_input_5, '请选择业务库'))
        self.dep_input_2.textChanged.connect(lambda: self._action.initComboBoxDB(self.dep_input_5, '请选择业务库'))
        self.dep_input_3.textChanged.connect(lambda: self._action.initComboBoxDB(self.dep_input_5, '请选择业务库'))
        self.dep_input_4.textChanged.connect(lambda: self._action.initComboBoxDB(self.dep_input_5, '请选择业务库'))
        # 获取历史库，联动
        # 历史库测试绑定信号槽
        self.getDBBtn_2.clicked.connect(lambda: self._solot.setDBNameList(mainWidget,
                                                                          {
                                                                              'ip': self.dep_input_7.text(),
                                                                              'port': self.dep_input_8.text(),
                                                                              'user': self.dep_input_9.text(),
                                                                              'pwd': self.dep_input_10.text(),
                                                                          },
                                                                          self.dep_input_11))
        # 输入框修改初始化下拉框数据
        self.dep_input_7.textChanged.connect(lambda: self._action.initComboBoxDB(self.dep_input_11, '请选择历史库'))
        self.dep_input_8.textChanged.connect(lambda: self._action.initComboBoxDB(self.dep_input_11, '请选择历史库'))
        self.dep_input_9.textChanged.connect(lambda: self._action.initComboBoxDB(self.dep_input_11, '请选择历史库'))
        self.dep_input_10.textChanged.connect(lambda: self._action.initComboBoxDB(self.dep_input_11, '请选择历史库'))

    # page_2控件信号
    def connSignalPage_2(self, mainWidget):
        # 是否更新系统库
        self.db_input_1.stateChanged.connect(lambda: self._solot.cbSetEnabledSlot(self._objsDict, 'db_das'))
        # 是否更新BI库
        self.db_input_7.stateChanged.connect(lambda: self._solot.cbSetEnabledSlot(self._objsDict, 'db_bi'))
        # 是否更新工艺参数
        self.db_input_13.stateChanged.connect(lambda: self._solot.cbSetEnabledSlot(self._objsDict, 'db_pp'))
        # 升级DB的信号
        self.db_comfirmBtn.clicked.connect(lambda: self._solot.createFullDB(mainWidget))

    # page_3控件信号
    def connSignalPage_3(self, mainWidget):
        # 是否抽取历史库
        self.nifi_input_11.stateChanged.connect(lambda: self._solot.cbSetEnabledSlot(self._objsDict, 'nifi_history'))
        # 是否抽取工艺参数
        self.nifi_input_17.stateChanged.connect(lambda: self._solot.cbSetEnabledSlot(self._objsDict, 'nifi_pp'))
        # 是否启用登录
        self.nifi_input_23.stateChanged.connect(lambda: self._solot.cbSetEnabledSlot(self._objsDict, 'nifi_islogin'))
        # 业务库试绑定信号槽
        self.getDBBtn_3.clicked.connect(lambda: self._solot.setDBNameList(mainWidget,
                                                                          {
                                                                              'ip': self.nifi_input_1.text(),
                                                                              'port': self.nifi_input_2.text(),
                                                                              'user': self.nifi_input_3.text(),
                                                                              'pwd': self.nifi_input_4.text(),
                                                                          },
                                                                          self.nifi_input_5))
        # 业务库输入框修改初始化下拉框数据
        self.nifi_input_1.textChanged.connect(lambda: self._action.initComboBoxDB(self.nifi_input_5, '请选择业务库'))
        self.nifi_input_2.textChanged.connect(lambda: self._action.initComboBoxDB(self.nifi_input_5, '请选择业务库'))
        self.nifi_input_3.textChanged.connect(lambda: self._action.initComboBoxDB(self.nifi_input_5, '请选择业务库'))
        self.nifi_input_4.textChanged.connect(lambda: self._action.initComboBoxDB(self.nifi_input_5, '请选择业务库'))

        # BI库试绑定信号槽
        self.getDBBtn_4.clicked.connect(lambda: self._solot.setDBNameList(mainWidget,
                                                                          {
                                                                              'ip': self.nifi_input_6.text(),
                                                                              'port': self.nifi_input_7.text(),
                                                                              'user': self.nifi_input_8.text(),
                                                                              'pwd': self.nifi_input_9.text(),
                                                                          },
                                                                          self.nifi_input_10))
        # BI库输入框修改初始化下拉框数据
        self.nifi_input_6.textChanged.connect(lambda: self._action.initComboBoxDB(self.nifi_input_10, '请选择BI库'))
        self.nifi_input_7.textChanged.connect(lambda: self._action.initComboBoxDB(self.nifi_input_10, '请选择BI库'))
        self.nifi_input_8.textChanged.connect(lambda: self._action.initComboBoxDB(self.nifi_input_10, '请选择BI库'))
        self.nifi_input_9.textChanged.connect(lambda: self._action.initComboBoxDB(self.nifi_input_10, '请选择BI库'))

        # 历史库试绑定信号槽
        self.getDBBtn_5.clicked.connect(lambda: self._solot.setDBNameList(mainWidget,
                                                                          {
                                                                              'ip': self.nifi_input_12.text(),
                                                                              'port': self.nifi_input_13.text(),
                                                                              'user': self.nifi_input_14.text(),
                                                                              'pwd': self.nifi_input_15.text(),
                                                                          },
                                                                          self.nifi_input_16))
        # 历史库输入框修改初始化下拉框数据
        self.nifi_input_12.textChanged.connect(lambda: self._action.initComboBoxDB(self.nifi_input_16, '请选择历史库'))
        self.nifi_input_13.textChanged.connect(lambda: self._action.initComboBoxDB(self.nifi_input_16, '请选择历史库'))
        self.nifi_input_14.textChanged.connect(lambda: self._action.initComboBoxDB(self.nifi_input_16, '请选择历史库'))
        self.nifi_input_15.textChanged.connect(lambda: self._action.initComboBoxDB(self.nifi_input_16, '请选择历史库'))

        # 工艺参数试绑定信号槽
        self.getDBBtn_6.clicked.connect(lambda: self._solot.setDBNameList(mainWidget,
                                                                          {
                                                                              'ip': self.nifi_input_18.text(),
                                                                              'port': self.nifi_input_19.text(),
                                                                              'user': self.nifi_input_20.text(),
                                                                              'pwd': self.nifi_input_21.text(),
                                                                          },
                                                                          self.nifi_input_22))
        # 工艺参数输入框修改初始化下拉框数据
        self.nifi_input_18.textChanged.connect(lambda: self._action.initComboBoxDB(self.nifi_input_22, '请选择工艺参数库'))
        self.nifi_input_19.textChanged.connect(lambda: self._action.initComboBoxDB(self.nifi_input_22, '请选择工艺参数库'))
        self.nifi_input_20.textChanged.connect(lambda: self._action.initComboBoxDB(self.nifi_input_22, '请选择工艺参数库'))
        self.nifi_input_21.textChanged.connect(lambda: self._action.initComboBoxDB(self.nifi_input_22, '请选择工艺参数库'))
        # 选择Nifi模板地址
        self.getFile.clicked.connect(lambda: self._solot.getNifiTemplate(mainWidget, self._objsDict))
        # 升级Nifi更新按钮信号
        self.nifi_confirmBtn.clicked.connect(lambda: self._solot.updateNifiTemplate(mainWidget, self.nifiConfItem, self._objsDict))