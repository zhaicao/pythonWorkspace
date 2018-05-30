

from PyQt5 import QtCore, QtGui, QtWidgets

class TextUI(object):
    def __init__(self):
        pass

    #显示Lable控件文字
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.group_1.setTitle(_translate("mainWidget", "业务库"))
        self.label_72.setText(_translate("mainWidget", "端口"))
        self.label_73.setText(_translate("mainWidget", "密码"))
        self.label_76.setText(_translate("mainWidget", "账号"))
        self.label_77.setText(_translate("mainWidget", "数据库"))
        self.label_78.setText(_translate("mainWidget", "地址"))

        self.input_5.setItemText(0, _translate("mainWidget", "请选择业务库"))
        self.group_2.setTitle(_translate("mainWidget", "历史库"))
        self.label_85.setText(_translate("mainWidget", "数据库"))

        self.label_81.setText(_translate("mainWidget", "密码"))
        self.label_86.setText(_translate("mainWidget", "地址"))

        self.label_84.setText(_translate("mainWidget", "账号"))
        self.label_80.setText(_translate("mainWidget", "端口"))
        self.input_6.setText(_translate("mainWidget", "是否抽取历史库"))
        self.input_11.setItemText(0, _translate("mainWidget", "请选择历史库"))
        self.group_8.setTitle(_translate("mainWidget", "BI库"))

        self.label_116.setText(_translate("mainWidget", "密码"))
        self.label_117.setText(_translate("mainWidget", "端口"))

        self.label_120.setText(_translate("mainWidget", "账号"))
        self.label_121.setText(_translate("mainWidget", "数据库"))
        self.label_122.setText(_translate("mainWidget", "地址"))
        self.label_123.setText(_translate("mainWidget", "数据源编号"))
        self.label_124.setText(_translate("mainWidget", "数据源名称"))
        self.group_3.setTitle(_translate("mainWidget", "系统库"))
        self.label_64.setText(_translate("mainWidget", "端口"))
        self.label_65.setText(_translate("mainWidget", "密码"))

        self.label_68.setText(_translate("mainWidget", "账号"))
        self.label_69.setText(_translate("mainWidget", "数据库"))
        self.label_70.setText(_translate("mainWidget", "地址"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabStep_1), _translate("mainWidget", "Step1.数据库"))
        self.group_14.setTitle(_translate("mainWidget", "工艺参数"))
        self.label_126.setText(_translate("mainWidget", "密码"))
        self.label_38.setText(_translate("mainWidget", "账号"))
        self.label_41.setText(_translate("mainWidget", "映射目录"))
        self.label_43.setText(_translate("mainWidget", "映射地址"))
        self.input_24.setText(_translate("mainWidget", "是否启用工艺参数"))
        self.group_5.setTitle(_translate("mainWidget", "工艺参数库"))
        self.label_55.setText(_translate("mainWidget", "文件路径"))
        self.label_51.setText(_translate("mainWidget", "账号"))
        self.label_48.setText(_translate("mainWidget", "密码"))
        self.label_47.setText(_translate("mainWidget", "端口"))
        self.label_53.setText(_translate("mainWidget", "地址"))

        self.label_52.setText(_translate("mainWidget", "数据库"))
        self.label_56.setText(_translate("mainWidget", "开始年月"))
        self.label_57.setText(_translate("mainWidget", "初始值(MB)"))
        self.label_58.setText(_translate("mainWidget", "结束年月"))
        self.label_59.setText(_translate("mainWidget", "增长值(MB)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabStep_2), _translate("mainWidget", "Step2.工艺参数"))
        self.group_6.setTitle(_translate("mainWidget", "基础配置"))
        self.label_15.setText(_translate("mainWidget", "系统版本"))
        self.label_18.setText(_translate("mainWidget", "业务端服务地址"))
        self.label_16.setText(_translate("mainWidget", "业务端服务端口"))
        self.group_7.setTitle(_translate("mainWidget", "部署程序"))
        self.label_3.setText(_translate("mainWidget", "网络共享地址"))
        self.label_5.setText(_translate("mainWidget", "共享密码"))
        self.label_4.setText(_translate("mainWidget", "共享账号"))
        self.group8.setTitle(_translate("mainWidget", "部署地址"))
        self.label_9.setText(_translate("mainWidget", "拷贝目录"))
        self.label_10.setText(_translate("mainWidget", "PowerShell目录"))
        self.label_12.setText(_translate("mainWidget", "安装目录"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabStep_3), _translate("mainWidget", "Step3.部署配置"))
        self.group_9.setTitle(_translate("mainWidget", "基础配置"))
        self.label_95.setText(_translate("mainWidget", "服务端口"))
        self.group_11.setTitle(_translate("mainWidget", "单点登录"))
        self.label_29.setText(_translate("mainWidget", "服务地址(MI)"))
        self.label_31.setText(_translate("mainWidget", "页面端口"))
        self.label_32.setText(_translate("mainWidget", "接口端口"))
        self.input_49.setText(_translate("mainWidget", "是否启用单点登录"))
        self.group_12.setTitle(_translate("mainWidget", "ETL配置"))
        self.label_93.setText(_translate("mainWidget", "账号"))
        self.input_57.setText(_translate("mainWidget", "是否启用登录"))
        self.label_30.setText(_translate("mainWidget", "工艺参数抽取目录"))
        self.label_92.setText(_translate("mainWidget", "抽取抽取频率(分钟)"))
        self.label_39.setText(_translate("mainWidget", "JVM(MB)"))
        self.label_37.setText(_translate("mainWidget", "ETL端口"))
        self.label_94.setText(_translate("mainWidget", "密码"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabStep_4), _translate("mainWidget", "Step4.系统配置"))
        self.group_13.setTitle(_translate("mainWidget", "定制配置"))
        self.input_66.setItemText(0, _translate("mainWidget", "停用"))
        self.input_66.setItemText(1, _translate("mainWidget", "启用"))
        self.input_67.setItemText(0, _translate("mainWidget", "停用"))
        self.input_67.setItemText(1, _translate("mainWidget", "启用"))
        self.input_62.setItemText(0, _translate("mainWidget", "停用"))
        self.input_62.setItemText(1, _translate("mainWidget", "启用"))
        self.input_61.setItemText(0, _translate("mainWidget", "停用"))
        self.input_61.setItemText(1, _translate("mainWidget", "启用"))
        self.label_104.setText(_translate("mainWidget", "断链"))
        self.input_63.setItemText(0, _translate("mainWidget", "停用"))
        self.input_63.setItemText(1, _translate("mainWidget", "启用"))
        self.input_65.setItemText(0, _translate("mainWidget", "停用"))
        self.input_65.setItemText(1, _translate("mainWidget", "启用"))
        self.input_64.setItemText(0, _translate("mainWidget", "停用"))
        self.input_64.setItemText(1, _translate("mainWidget", "启用"))
        self.label_105.setText(_translate("mainWidget", "过滤万能工单"))
        self.label_97.setText(_translate("mainWidget", "重构版本"))
        self.label_102.setText(_translate("mainWidget", "FGB"))
        self.label_99.setText(_translate("mainWidget", "设备维护"))
        self.label_100.setText(_translate("mainWidget", "工具管理"))
        self.label_98.setText(_translate("mainWidget", "遏制"))
        self.label_103.setText(_translate("mainWidget", "视频监控"))
        self.label_101.setText(_translate("mainWidget", "工艺参数"))
        self.input_60.setItemText(0, _translate("mainWidget", "重构后"))
        self.input_60.setItemText(1, _translate("mainWidget", "重构前"))
        self.input_68.setItemText(0, _translate("mainWidget", "过滤"))
        self.input_68.setItemText(1, _translate("mainWidget", "不过滤"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabStep_5), _translate("mainWidget", "Step5.工厂定制"))
        self.confirmBtn.setText(_translate("mainWidget", "Next"))
        self.cancelBtn.setText(_translate("mainWidget", "Cancel"))

    #控件默认值
    def defaultVal(self):
        _translate = QtCore.QCoreApplication.translate
        self.input_2.setText(_translate("mainWidget", "1433"))
        self.input_8.setText(_translate("mainWidget", "1433"))
        self.input_13.setText(_translate("mainWidget", "1433"))
        self.input_20.setText(_translate("mainWidget", "1433"))
        self.input_30.setText(_translate("mainWidget", "1433"))
        self.input_23.setText(_translate("mainWidget", "DAS"))

    #帮助显示
    def helpToolTip(self):
        QtWidgets.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        # 业务库Group
        self.help_1.setToolTip('<b>业务数据库</b>的IP地址及端口，端口默认1433')
        self.help_2.setToolTip('<b>业务数据库</b>的登录账号和密码')
        self.help_3.setToolTip('选择抽取的业务库名')
        # 历史库Group
        self.help_4.setToolTip('<b>历史数据库</b>一般指mes_history，存放历史设备事件、状态等数据。'
                               '新上线的环境一般无历史数据，若开启抽取，则需进行配置')
        self.help_5.setToolTip('<b>历史数据库</b>的IP地址及端口，端口默认1433')
        self.help_6.setToolTip('<b>历史数据库</b>的登录账号和密码')
        self.help_7.setToolTip('选择抽取的历史库名')
        # BI库Group
        self.help_8.setToolTip('<b>BI数据库</b>的IP地址及端口，端口默认1433')
        self.help_9.setToolTip('<b>历史数据库</b>的登录账号和密码')
        self.help_10.setToolTip('请输入BI库的库名，系统将会自动建立BI库')
        self.help_11.setToolTip('数据源一般指某个车间或分厂的数据，目前一个系统仅支持一个数据源。'
                                '例如,数据源编号:KSSP;数据源名称:科尔本')
        # 系统库Group
        self.help_12.setToolTip('<b>系统数据库</b>为追溯分析系统运行的数据库，此处为IP地址及端口，端口默认1433')
        self.help_13.setToolTip('<b>系统数据库</b>的登录账号和密码')
        self.help_14.setToolTip('请输入系统的库名，系统将会自动建立BI库。默认为DAS')