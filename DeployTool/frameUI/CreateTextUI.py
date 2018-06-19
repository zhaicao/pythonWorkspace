# -*- coding: utf-8 -*-

# 窗口的所有控件的中文名、帮助提示及默认值生成的模块

__author__='zhaicao'

from PyQt5 import QtCore, QtGui, QtWidgets

class TraceCreateTextUI(object):

    #统一生成控件显示文字
    def initControlTexts(self):
        self.retranslateUi()
        self.helpToolTip()
        self.defaultVal()

    #显示Lable控件文字
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.dep_group_1.setTitle(_translate("MainWindow", "业务库"))
        self.labelText_3.setText(_translate("MainWindow", "账号"))
        self.labelText_5.setText(_translate("MainWindow", "数据库"))
        self.labelText_2.setText(_translate("MainWindow", "端口"))
        self.labelText_4.setText(_translate("MainWindow", "密码"))
        self.labelText_1.setText(_translate("MainWindow", "地址"))
        self.dep_input_5.setItemText(0, _translate("MainWindow", "请选择业务库"))

        self.getDBBtn_1.setText(_translate("MainWindow", "测试"))
        self.dep_group_2.setTitle(_translate("MainWindow", "历史库"))
        self.labelText_10.setText(_translate("MainWindow", "数据库"))

        self.dep_input_11.setItemText(0, _translate("MainWindow", "请选择历史库"))
        self.dep_input_6.setText(_translate("MainWindow", "是否抽取历史库"))
        self.getDBBtn_2.setText(_translate("MainWindow", "测试"))
        self.labelText_6.setText(_translate("MainWindow", "地址"))
        self.labelText_8.setText(_translate("MainWindow", "账号"))
        self.labelText_7.setText(_translate("MainWindow", "端口"))
        self.labelText_9.setText(_translate("MainWindow", "密码"))
        self.dep_group_3.setTitle(_translate("MainWindow", "BI库"))

        self.labelText_14.setText(_translate("MainWindow", "密码"))
        self.labelText_12.setText(_translate("MainWindow", "端口"))
        self.labelText_13.setText(_translate("MainWindow", "账号"))
        self.labelText_15.setText(_translate("MainWindow", "数据库"))
        self.labelText_11.setText(_translate("MainWindow", "地址"))
        self.labelText_16.setText(_translate("MainWindow", "数据源编号"))
        self.labelText_17.setText(_translate("MainWindow", "数据源名称"))
        self.dep_group_4.setTitle(_translate("MainWindow", "系统库"))
        self.labelText_19.setText(_translate("MainWindow", "端口"))
        self.labelText_21.setText(_translate("MainWindow", "密码"))
        self.labelText_20.setText(_translate("MainWindow", "账号"))
        self.labelText_22.setText(_translate("MainWindow", "数据库"))
        self.labelText_18.setText(_translate("MainWindow", "地址"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabStep_1), _translate("MainWindow", "Step1.数据库"))
        self.dep_group_5.setTitle(_translate("MainWindow", "工艺参数"))
        self.dep_input_24.setText(_translate("MainWindow", "是否启用工艺参数"))
        self.dep_group_6.setTitle(_translate("MainWindow", "工艺参数网络访问"))
        self.labelText_26.setText(_translate("MainWindow", "密码"))
        self.labelText_25.setText(_translate("MainWindow", "账号"))
        self.labelText_24.setText(_translate("MainWindow", "映射目录"))
        self.labelText_23.setText(_translate("MainWindow", "映射地址"))
        self.dep_input_25.setText(_translate("MainWindow", "是否工艺参数网络访问"))
        self.dep_group_7.setTitle(_translate("MainWindow", "工艺参数库"))
        self.labelText_29.setText(_translate("MainWindow", "账号"))
        self.labelText_30.setText(_translate("MainWindow", "密码"))

        self.labelText_31.setText(_translate("MainWindow", "数据库"))
        self.labelText_28.setText(_translate("MainWindow", "端口"))
        self.labelText_27.setText(_translate("MainWindow", "地址"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabStep_2), _translate("MainWindow", "Step2.工艺参数"))
        self.dep_group_8.setTitle(_translate("MainWindow", "基础配置"))
        self.labelText_32.setText(_translate("MainWindow", "系统版本"))
        self.labelText_33.setText(_translate("MainWindow", "业务端服务地址"))
        self.labelText_34.setText(_translate("MainWindow", "业务端服务端口"))
        self.dep_group_9.setTitle(_translate("MainWindow", "部署程序"))
        self.labelText_35.setText(_translate("MainWindow", "网络共享地址"))
        self.labelText_37.setText(_translate("MainWindow", "共享密码"))
        self.labelText_36.setText(_translate("MainWindow", "共享账号"))
        self.dep_group_10.setTitle(_translate("MainWindow", "部署地址"))
        self.labelText_38.setText(_translate("MainWindow", "拷贝目录"))
        self.labelText_40.setText(_translate("MainWindow", "PowerShell目录"))
        self.labelText_39.setText(_translate("MainWindow", "安装目录"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabStep_3), _translate("MainWindow", "Step3.部署配置"))
        self.dep_group_11.setTitle(_translate("MainWindow", "基础配置"))
        self.labelText_41.setText(_translate("MainWindow", "服务端口"))

        self.dep_group_12.setTitle(_translate("MainWindow", "单点登录"))
        self.labelText_42.setText(_translate("MainWindow", "服务地址(MI)"))
        self.labelText_43.setText(_translate("MainWindow", "页面端口"))

        self.labelText_44.setText(_translate("MainWindow", "接口端口"))

        self.dep_input_45.setText(_translate("MainWindow", "是否启用单点登录"))
        self.dep_group_13.setTitle(_translate("MainWindow", "ETL配置"))
        self.labelText_49.setText(_translate("MainWindow", "账号"))
        self.dep_input_53.setText(_translate("MainWindow", "是否启用登录"))

        self.labelText_45.setText(_translate("MainWindow", "工艺参数抽取目录"))
        self.labelText_48.setText(_translate("MainWindow", "抽取抽取频率(分钟)"))

        self.labelText_47.setText(_translate("MainWindow", "JVM(MB)"))
        self.labelText_46.setText(_translate("MainWindow", "ETL端口"))

        self.labelText_50.setText(_translate("MainWindow", "密码"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabStep_4), _translate("MainWindow", "Step4.系统配置"))
        self.dep_group_14.setTitle(_translate("MainWindow", "定制配置"))
        self.labelText_51.setText(_translate("MainWindow", "重构版本"))
        self.dep_input_59.setItemText(0, _translate("MainWindow", "停用"))
        self.dep_input_59.setItemText(1, _translate("MainWindow", "启用"))
        self.dep_input_60.setItemText(0, _translate("MainWindow", "停用"))
        self.dep_input_60.setItemText(1, _translate("MainWindow", "启用"))
        self.dep_input_58.setItemText(0, _translate("MainWindow", "停用"))
        self.dep_input_58.setItemText(1, _translate("MainWindow", "启用"))
        self.dep_input_57.setItemText(0, _translate("MainWindow", "停用"))
        self.dep_input_57.setItemText(1, _translate("MainWindow", "启用"))
        self.dep_input_62.setItemText(0, _translate("MainWindow", "停用"))
        self.dep_input_62.setItemText(1, _translate("MainWindow", "启用"))
        self.labelText_57.setText(_translate("MainWindow", "断链"))
        self.dep_input_61.setItemText(0, _translate("MainWindow", "停用"))
        self.dep_input_61.setItemText(1, _translate("MainWindow", "启用"))
        self.labelText_58.setText(_translate("MainWindow", "过滤万能工单"))
        self.labelText_55.setText(_translate("MainWindow", "FGB"))
        self.labelText_52.setText(_translate("MainWindow", "遏制"))
        self.labelText_54.setText(_translate("MainWindow", "工具管理"))
        self.dep_input_56.setItemText(0, _translate("MainWindow", "重构后"))
        self.dep_input_56.setItemText(1, _translate("MainWindow", "重构前"))
        self.labelText_53.setText(_translate("MainWindow", "设备维护"))
        self.labelText_56.setText(_translate("MainWindow", "视频监控"))
        self.dep_input_63.setItemText(0, _translate("MainWindow", "过滤"))
        self.dep_input_63.setItemText(1, _translate("MainWindow", "不过滤"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabStep_5), _translate("MainWindow", "Step5.工厂定制"))
        self.dep_copyDepBtn.setText(_translate("MainWindow", "复制配置"))
        self.dep_copyManBtn.setText(_translate("MainWindow", "复制定制"))
        self.dep_confirmBtn.setText(_translate("MainWindow", "下一步"))
        self.dep_cancelBtn.setText(_translate("MainWindow", "退出"))
        self.db_group_1.setTitle(_translate("MainWindow", "系统库"))
        self.labelText_59.setText(_translate("MainWindow", "地址"))
        self.labelText_61.setText(_translate("MainWindow", "账号"))
        self.labelText_60.setText(_translate("MainWindow", "端口"))
        self.labelText_62.setText(_translate("MainWindow", "密码"))

        self.labelText_63.setText(_translate("MainWindow", "数据库"))
        self.db_group_2.setTitle(_translate("MainWindow", "BI库"))
        self.labelText_64.setText(_translate("MainWindow", "地址"))
        self.labelText_66.setText(_translate("MainWindow", "账号"))
        self.labelText_65.setText(_translate("MainWindow", "端口"))
        self.labelText_67.setText(_translate("MainWindow", "密码"))

        self.labelText_68.setText(_translate("MainWindow", "数据库"))
        self.db_group_3.setTitle(_translate("MainWindow", "工艺参数库"))

        self.labelText_73.setText(_translate("MainWindow", "数据库"))
        self.labelText_69.setText(_translate("MainWindow", "地址"))
        self.labelText_72.setText(_translate("MainWindow", "密码"))
        self.labelText_70.setText(_translate("MainWindow", "端口"))
        self.labelText_71.setText(_translate("MainWindow", "账号"))
        self.db_input_11.setText(_translate("MainWindow", "是否抽取工艺参数"))
        self.db_comfirmBtn.setText(_translate("MainWindow", "更新数据库"))
        self.nifi_group_1.setTitle(_translate("MainWindow", "业务库"))
        self.labelText_74.setText(_translate("MainWindow", "地址"))
        self.labelText_76.setText(_translate("MainWindow", "账号"))
        self.labelText_75.setText(_translate("MainWindow", "端口"))
        self.labelText_77.setText(_translate("MainWindow", "密码"))

        self.labelText_78.setText(_translate("MainWindow", "数据库"))
        self.nifi_input_5.setItemText(0, _translate("MainWindow", "请选择业务库"))
        self.getDBBtn_3.setText(_translate("MainWindow", "测试"))
        self.nifi_group_2.setTitle(_translate("MainWindow", "BI库"))
        self.labelText_79.setText(_translate("MainWindow", "地址"))
        self.labelText_81.setText(_translate("MainWindow", "账号"))
        self.labelText_80.setText(_translate("MainWindow", "端口"))
        self.labelText_82.setText(_translate("MainWindow", "密码"))

        self.labelText_83.setText(_translate("MainWindow", "数据库"))
        self.nifi_input_10.setItemText(0, _translate("MainWindow", "请选择BI库"))
        self.getDBBtn_4.setText(_translate("MainWindow", "测试"))
        self.nifi_group_3.setTitle(_translate("MainWindow", "历史库"))
        self.labelText_88.setText(_translate("MainWindow", "数据库"))
        self.nifi_input_16.setItemText(0, _translate("MainWindow", "请选择历史库"))
        self.getDBBtn_5.setText(_translate("MainWindow", "测试"))
        self.labelText_85.setText(_translate("MainWindow", "端口"))
        self.labelText_86.setText(_translate("MainWindow", "账号"))
        self.labelText_87.setText(_translate("MainWindow", "密码"))

        self.labelText_84.setText(_translate("MainWindow", "地址"))
        self.nifi_input_11.setText(_translate("MainWindow", "是否抽取历史库"))
        self.nifi_group_4.setTitle(_translate("MainWindow", "工艺参数库"))
        self.nifi_input_22.setItemText(0, _translate("MainWindow", "请选择工艺参数库"))
        self.labelText_93.setText(_translate("MainWindow", "数据库"))

        self.getDBBtn_6.setText(_translate("MainWindow", "测试"))
        self.labelText_92.setText(_translate("MainWindow", "密码"))
        self.labelText_91.setText(_translate("MainWindow", "账号"))
        self.labelText_89.setText(_translate("MainWindow", "地址"))
        self.labelText_90.setText(_translate("MainWindow", "端口"))
        self.nifi_input_17.setText(_translate("MainWindow", "是否抽取工艺参数"))
        self.nifi_group_5.setTitle(_translate("MainWindow", "Nifi配置"))
        self.labelText_98.setText(_translate("MainWindow", "抽取模板"))

        self.labelText_97.setText(_translate("MainWindow", "密码"))
        self.labelText_96.setText(_translate("MainWindow", "账号"))
        self.labelText_94.setText(_translate("MainWindow", "地址"))
        self.labelText_95.setText(_translate("MainWindow", "端口"))
        self.nifi_input_23.setText(_translate("MainWindow", "是否启用登录权限"))
        self.nifi_confirmBtn.setText(_translate("MainWindow", "更新抽取模板"))
        self.menuDeploy.setTitle(_translate("MainWindow", "部署"))
        self.menuUpdate.setTitle(_translate("MainWindow", "升级"))
        self.firstDeploy.setText(_translate("MainWindow", "首次部署"))
        self.updateDB.setText(_translate("MainWindow", "数据库"))
        self.updateNifi.setText(_translate("MainWindow", "Nifi"))
        self.getFile.setText(_translate("MainWindow", "..."))


    #控件默认值
    def defaultVal(self):
        _translate = QtCore.QCoreApplication.translate
        self.dep_input_2.setText(_translate("MainWindow", "1433"))
        self.dep_input_8.setText(_translate("MainWindow", "1433"))
        self.dep_input_13.setText(_translate("MainWindow", "1433"))
        self.dep_input_20.setText(_translate("MainWindow", "1433"))
        self.dep_input_31.setText(_translate("MainWindow", "1433"))
        self.dep_input_44.setText(_translate("MainWindow", "8080"))
        self.dep_input_47.setText(_translate("MainWindow", "801"))
        self.dep_input_48.setText(_translate("MainWindow", "808"))
        self.dep_input_50.setText(_translate("MainWindow", "9001"))
        self.dep_input_51.setText(_translate("MainWindow", "2048"))
        self.dep_input_52.setText(_translate("MainWindow", "60"))
        self.db_input_2.setText(_translate("MainWindow", "1433"))
        self.db_input_7.setText(_translate("MainWindow", "1433"))
        self.db_input_13.setText(_translate("MainWindow", "1433"))
        self.nifi_input_2.setText(_translate("MainWindow", "1433"))
        self.nifi_input_7.setText(_translate("MainWindow", "1433"))
        self.nifi_input_13.setText(_translate("MainWindow", "1433"))
        self.nifi_input_19.setText(_translate("MainWindow", "1433"))
        self.nifi_input_25.setText(_translate("MainWindow", "1433"))


    #帮助显示
    def helpToolTip(self):
        QtWidgets.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        # 业务库Group
        self.help_1.setToolTip('<b>业务数据库</b>的IP地址及端口，端口默认1433')
        self.help_2.setToolTip('<b>业务数据库</b>的登录账号和密码')
        self.help_3.setToolTip('点击<b>测试</b>可自动获得数据库列表，若网络不稳定或其他问题，将有一定的延迟响应。在列表中选择需要抽取的业务库名')
        # 历史库Group
        self.help_4.setToolTip('<b>历史数据库</b>一般指mes_history，存放历史设备事件、状态等数据。'
                               '新上线的环境一般无历史数据，若开启抽取，则需进行配置')
        self.help_5.setToolTip('<b>历史数据库</b>的IP地址及端口，端口默认1433')
        self.help_6.setToolTip('<b>历史数据库</b>的登录账号和密码')
        self.help_7.setToolTip('点击<b>测试</b>可自动获得数据库列表，若网络不稳定或其他问题，将有一定的延迟响应。在列表中选择需要抽取的历史库名')
        # BI库Group
        self.help_8.setToolTip('<b>BI数据库</b>的IP地址及端口，端口默认1433')
        self.help_9.setToolTip('<b>BI数据库</b>的登录账号和密码')
        self.help_10.setToolTip('请输入BI库的库名，系统将<br>'
                                '会自动建立BI库')
        self.help_11.setToolTip('数据源一般指某个车间或分<br>'
                                '厂的数据，目前一个系统仅<br>'
                                '支持一个数据源。<br>'
                                '例如,数据源编号:KSSP;<br>'
                                '数据源名称:科尔本')
        # 系统库Group
        self.help_12.setToolTip('<b>系统数据库</b>为追溯分析系统运行的数据库，此处为IP地址及端口，端口默认1433')
        self.help_13.setToolTip('<b>系统数据库</b>的登录账号和密码')
        self.help_14.setToolTip('请输入系统的库名，系统将<br>'
                                '会自动建立BI库。默认名DAS')
        # 工艺参数
        self.help_15.setToolTip('<b>工艺参数</b>一般指生产过程中的设备监控数据。根据现场不同，有的不需要使用工艺参数。')
        self.help_16.setToolTip('<b>工艺参数</b>一般以文件形式存放在Imes服务器上,需要将该目录共享,后通过抽取配置映射成本地驱动器；若工艺参数文件在本地，则取消该选项')
        self.help_17.setToolTip('<b>工艺参数</b>该处输入工艺参数目录共享的IP地址。如：192.168.227.169')
        self.help_18.setToolTip('<b>映射目录</b>指共享后的目录。如网络地址为//192.168.227.169/KSSP_PPDATA，则KSSP_PPDATA是映射的目录')
        self.help_19.setToolTip('<b>账号和密码</b>分别是访问共享目录时的账号和密码')

        # 工艺参数库
        self.help_19.setToolTip('<b>工艺参数库</b>即抽取工艺参数后所存储的数据库，此处为IP地址及端口，端口默认1433')
        self.help_20.setToolTip('<b>工艺参数库</b>的登录账号和密码')
        self.help_21.setToolTip('请输入工艺参数库的库名,<BR>系统将会自动建立工艺参数库')
        self.help_22.setToolTip('<b>工艺参数库</b>采用分区建库，所以只需指定数据库物理文件放在的路径。一般默认为数据库的Data目录即可，如：D:\SqlServer\MSSQL11.MSSQLSERVER\MSSQL\DATA')

        # 基础配置
        self.help_23.setToolTip('<b>系统版本</b>为需要部署的追溯分析系统的版本，如:2.1.0')
        self.help_24.setToolTip('<b>业务端服务地址</b>为追溯业务端系统的IP地址')
        self.help_25.setToolTip('<b>业务端服务端口</b>为追溯业务端系统的端口号')
        # 部署程序
        self.help_26.setToolTip('<b>网络共享地址</b>为存放追溯分析系统发布件的网络地址。由于使用Ansible远程部署系统，会自动拷贝发布件至目标机，故发布件需要网络共享')
        self.help_27.setToolTip('<b>共享账号</b>为访问发布件网络地址所需要的账号')
        self.help_28.setToolTip('<b>共享密码</b>为访问发布件网络地址所需要的密码')
        # 部署地址
        self.help_29.setToolTip('<b>拷贝目录</b>为目标机上存放发布件的目录。Ansible将自动拷贝到目标机上指定的目录')
        self.help_30.setToolTip('<b>安装目录</b>为目标机上安装系统所在的目录')
        self.help_31.setToolTip('<b>PowerShell目录</b>为目标机上存放PowerShell脚本的目录。目标机上需要做一些操作，故需要powershell脚本支持')
        # 基础配置
        self.help_32.setToolTip('<b>服务端口</b>为追溯分析系统访问的端口，默认8080')
        # 单点登录
        self.help_33.setToolTip('<b>单点登录</b>单点登录需要MI系统支持，启用单点登录请确保MI运行正常')
        self.help_34.setToolTip('<b>服务地址</b>一般指MI访问的IP地址')
        self.help_35.setToolTip('<b>页面端口</b>是MI登录的页面访问端口，默认801')
        self.help_36.setToolTip('<b>接口端口</b>是MI登录的后端接口访问端口，默认808')
        # ETL配置
        self.help_37.setToolTip('<b>工艺参数抽取目录</b>是Nifi(ETL工具)抽取工艺参数的目录，若工艺参数在目标机本地上，则直接输入该目录且不用配置工艺参数网络访问；若工艺参数远程访问，则此处输入目标机上不存在的驱动器(盘符)，部署工具会通过PowerShell自动创建映射到目标机上的驱动器')
        self.help_38.setToolTip('<b>ETL端口</b>是NIfi页面访问的端口，默认9001')
        self.help_39.setToolTip('<b>JVM</b>是Nifi服务启动的内存，默认2048(2G)。推荐不要超过目标机上物理内存的1/2，如目标机上有其他服务，则内存需设置更小，但最好不要低于2G')
        self.help_40.setToolTip('<b>抽取频率</b>是Nifi抽取数据的时间间隔，默认1个小时(60分钟)抽取一次')
        self.help_41.setToolTip('<b>是否启用登录</b>是Nifi页面访问时权限的控制，启用该功能需要搭建LDAP服务，默认关闭')
        self.help_42.setToolTip('<b>账号</b>是登录访问Nifi页面的账号')
        self.help_43.setToolTip('<b>密码</b>是登录访问Nifi页面的密码')
        # 工厂定制
        self.help_44.setToolTip('<b>重构版本</b>主要针对业务端服务而言，业务端服务有重构前后之分，默认重构后版本')
        self.help_45.setToolTip('<b>遏制</b>指追溯分析系统是否需要遏制功能')
        self.help_46.setToolTip('<b>设备维护</b>指追溯分析系统是否需要设备维护类的功能')
        self.help_47.setToolTip('<b>工具管理</b>指追溯分析系统是否需要工具类的功能')
        self.help_48.setToolTip('<b>FGB</b>指追溯分析系统是否需要FGB功能')
        self.help_49.setToolTip('<b>视频监控</b>指追溯分析系统是否需要视频监控的功能')
        self.help_50.setToolTip('<b>断链</b>指追溯分析系统是否需要断链的功能')
        self.help_51.setToolTip('<b>过滤万能工单</b>指追溯分析系统对测试用的万能功能数据进行过滤')

        self.dep_copyDepBtn.setToolTip('复制部署配置(Step1~4)内容到系统剪贴板')
        self.dep_copyManBtn.setToolTip('复制工厂定制(Step5)内容到系统剪贴板')


