# -*- coding: utf-8 -*-

# 窗口的所有控件的中文名、帮助提示及默认值生成的模块

__author__='zhaicao'

from PyQt5 import QtCore, QtGui, QtWidgets
from frameUI.MainData import TraceItems

class TraceCreateTextUI(TraceItems):
    def __init__(self):
        # 继承对应的配置字典
        super().TraceConfItems()

    #统一生成控件显示文字
    def createTabTexts(self):
        self.retranslateUi()
        self.helpToolTip()
        self.defaultVal()

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
        self.getDBBtn_1.setText(_translate("mainWidget", "测试"))
        self.group_2.setTitle(_translate("mainWidget", "历史库"))
        self.label_85.setText(_translate("mainWidget", "数据库"))

        self.label_81.setText(_translate("mainWidget", "密码"))
        self.label_86.setText(_translate("mainWidget", "地址"))

        self.label_84.setText(_translate("mainWidget", "账号"))
        self.label_80.setText(_translate("mainWidget", "端口"))
        self.input_6.setText(_translate("mainWidget", "是否抽取历史库"))
        self.input_11.setItemText(0, _translate("mainWidget", "请选择历史库"))
        self.getDBBtn_2.setText(_translate("mainWidget", "测试"))
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
        self.input_72.setText(_translate("mainWidget", "是否启用工艺参数"))
        self.group_14.setTitle(_translate("mainWidget", "工艺参数网络访问"))
        self.groupBox.setTitle(_translate("mainWidget", "工艺参数"))
        self.group_14.setTitle(_translate("mainWidget", "工艺参数"))
        self.label_126.setText(_translate("mainWidget", "密码"))
        self.label_38.setText(_translate("mainWidget", "账号"))
        self.label_41.setText(_translate("mainWidget", "映射目录"))
        self.label_43.setText(_translate("mainWidget", "映射地址"))
        self.input_24.setText(_translate("mainWidget", "工艺参数是否网络访问"))
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
        self.input_65.setItemText(0, _translate("mainWidget", "停用"))
        self.input_65.setItemText(1, _translate("mainWidget", "启用"))
        self.input_66.setItemText(0, _translate("mainWidget", "停用"))
        self.input_66.setItemText(1, _translate("mainWidget", "启用"))
        self.input_62.setItemText(0, _translate("mainWidget", "停用"))
        self.input_62.setItemText(1, _translate("mainWidget", "启用"))
        self.input_61.setItemText(0, _translate("mainWidget", "停用"))
        self.input_61.setItemText(1, _translate("mainWidget", "启用"))
        self.label_104.setText(_translate("mainWidget", "断链"))
        self.input_63.setItemText(0, _translate("mainWidget", "停用"))
        self.input_63.setItemText(1, _translate("mainWidget", "启用"))
        self.input_64.setItemText(0, _translate("mainWidget", "停用"))
        self.input_64.setItemText(1, _translate("mainWidget", "启用"))
        self.label_105.setText(_translate("mainWidget", "过滤万能工单"))
        self.label_97.setText(_translate("mainWidget", "重构版本"))
        self.label_102.setText(_translate("mainWidget", "FGB"))
        self.label_99.setText(_translate("mainWidget", "设备维护"))
        self.label_100.setText(_translate("mainWidget", "工具管理"))
        self.label_98.setText(_translate("mainWidget", "遏制"))
        self.label_103.setText(_translate("mainWidget", "视频监控"))
        self.input_60.setItemText(0, _translate("mainWidget", "重构后"))
        self.input_60.setItemText(1, _translate("mainWidget", "重构前"))
        self.input_67.setItemText(1, _translate("mainWidget", "过滤"))
        self.input_67.setItemText(0, _translate("mainWidget", "不过滤"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabStep_5), _translate("mainWidget", "Step5.工厂定制"))
        self.confirmBtn.setText(_translate("mainWidget", "下一步"))
        self.cancelBtn.setText(_translate("mainWidget", "退出"))


    #控件默认值
    def defaultVal(self):
        _translate = QtCore.QCoreApplication.translate
        self.input_2.setText(_translate("mainWidget", "1433"))
        self.input_8.setText(_translate("mainWidget", "1433"))
        self.input_13.setText(_translate("mainWidget", "1433"))
        self.input_20.setText(_translate("mainWidget", "1433"))
        self.input_30.setText(_translate("mainWidget", "1433"))
        self.input_23.setText(_translate("mainWidget", "DAS"))
        self.input_35.setText(_translate("mainWidget", "201001"))
        self.input_36.setText(_translate("mainWidget", "202912"))
        self.input_37.setText(_translate("mainWidget", "10"))
        self.input_38.setText(_translate("mainWidget", "100"))
        self.input_48.setText(_translate("mainWidget", "8080"))
        self.input_51.setText(_translate("mainWidget", "801"))
        self.input_52.setText(_translate("mainWidget", "808"))
        self.input_54.setText(_translate("mainWidget", "9001"))
        self.input_55.setText(_translate("mainWidget", "2048"))
        self.input_56.setText(_translate("mainWidget", "60"))


    #帮助显示
    def helpToolTip(self):
        QtWidgets.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        # 业务库Group
        self.help_1.setToolTip('<b>业务数据库</b>的IP地址及端口，端口默认1433')
        self.help_2.setToolTip('<b>业务数据库</b>的登录账号和密码')
        self.help_3.setToolTip('点击<b>测试</b>可自动获得数据库列表，若网络不稳定或其他问题，将有3秒左右延迟响应。在列表中选择需要抽取的业务库名')
        # 历史库Group
        self.help_4.setToolTip('<b>历史数据库</b>一般指mes_history，存放历史设备事件、状态等数据。'
                               '新上线的环境一般无历史数据，若开启抽取，则需进行配置')
        self.help_5.setToolTip('<b>历史数据库</b>的IP地址及端口，端口默认1433')
        self.help_6.setToolTip('<b>历史数据库</b>的登录账号和密码')
        self.help_7.setToolTip('点击<b>测试</b>可自动获得数据库列表，若网络不稳定或其他问题，将有3秒左右延迟响应。在列表中选择需要抽取的历史库名')
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
        self.help_57.setToolTip('<b>工艺参数</b>一般指生产过程中的设备监控数据。根据现场不同，有的不需要使用工艺参数。')
        self.help_15.setToolTip('<b>工艺参数</b>一般以文件形式存放在Imes服务器上,需要将该目录共享,后通过抽取配置映射成本地驱动器；若工艺参数文件在本地，则取消该选项')
        self.help_16.setToolTip('<b>工艺参数</b>该处输入工艺参数目录共享的IP地址。如：192.168.227.169')
        self.help_17.setToolTip('<b>映射目录</b>指共享后的目录。如网络地址为//192.168.227.169/KSSP_PPDATA，则KSSP_PPDATA是映射的目录')
        self.help_18.setToolTip('<b>账号和密码</b>分别是访问共享目录时的账号和密码')

        # 工艺参数库
        self.help_19.setToolTip('<b>工艺参数库</b>即抽取工艺参数后所存储的数据库，此处为IP地址及端口，端口默认1433')
        self.help_20.setToolTip('<b>工艺参数库</b>的登录账号和密码')
        self.help_21.setToolTip('请输入工艺参数库的库名,<BR>系统将会自动建立工艺参数库')
        self.help_22.setToolTip('<b>工艺参数库</b>采用分区建库，所以只需指定数据库物理文件放在的路径。一般默认为数据库的Data目录即可，如：D:\SqlServer\MSSQL11.MSSQLSERVER\MSSQL\DATA')
        self.help_23.setToolTip('<b>工艺参数库</b>按照月份分区建库，故需要提前指定月份文件，默认201001-202912')
        self.help_24.setToolTip('<b>初始值</b>为数据库物理文件初始大小，默认为10MB;<b>增长值</b>为数据库物理文件每次增长大小，默认为100MB；')
        # 基础配置
        self.help_25.setToolTip('<b>系统版本</b>为需要部署的追溯分析系统的版本，如:2.1.0')
        self.help_26.setToolTip('<b>业务端服务地址</b>为追溯业务端系统的IP地址')
        self.help_27.setToolTip('<b>业务端服务端口</b>为追溯业务端系统的端口号')
        # 部署程序
        self.help_28.setToolTip('<b>网络共享地址</b>为存放追溯分析系统发布件的网络地址。由于使用Ansible远程部署系统，会自动拷贝发布件至目标机，故发布件需要网络共享')
        self.help_29.setToolTip('<b>共享账号</b>为访问发布件网络地址所需要的账号')
        self.help_30.setToolTip('<b>共享密码</b>为访问发布件网络地址所需要的密码')
        # 部署地址
        self.help_31.setToolTip('<b>拷贝目录</b>为目标机上存放发布件的目录。Ansible将自动拷贝到目标机上指定的目录')
        self.help_32.setToolTip('<b>安装目录</b>为目标机上安装系统所在的目录')
        self.help_33.setToolTip('<b>PowerShell目录</b>为目标机上存放PowerShell脚本的目录。目标机上需要做一些操作，故需要powershell脚本支持')
        # 基础配置
        self.help_34.setToolTip('<b>服务端口</b>为追溯分析系统访问的端口，默认8080')
        # 单点登录
        self.help_35.setToolTip('<b>单点登录</b>单点登录需要MI系统支持，启用单点登录请确保MI运行正常')
        self.help_36.setToolTip('<b>服务地址</b>一般指MI访问的IP地址')
        self.help_37.setToolTip('<b>页面端口</b>是MI登录的页面访问端口，默认801')
        self.help_38.setToolTip('<b>接口端口</b>是MI登录的后端接口访问端口，默认808')
        # ETL配置
        self.help_39.setToolTip('<b>工艺参数抽取目录</b>是Nifi(ETL工具)抽取工艺参数的目录，若工艺参数在目标机本地上，则直接输入该目录且不用配置工艺参数网络访问；若工艺参数远程访问，则此处输入目标机上不存在的驱动器(盘符)，部署工具会通过PowerShell自动创建映射到目标机上的驱动器')
        self.help_40.setToolTip('<b>ETL端口</b>是NIfi页面访问的端口，默认9001')
        self.help_41.setToolTip('<b>JVM</b>是Nifi服务启动的内存，默认2048(2G)。推荐不要超过目标机上物理内存的1/2，如目标机上有其他服务，则内存需设置更小，但最好不要低于2G')
        self.help_42.setToolTip('<b>抽取频率</b>是Nifi抽取数据的时间间隔，默认1个小时(60分钟)抽取一次')
        self.help_43.setToolTip('<b>是否启用登录</b>是Nifi页面访问时权限的控制，启用该功能需要搭建LDAP服务，默认关闭')
        self.help_44.setToolTip('<b>账号</b>是登录访问Nifi页面的账号')
        self.help_45.setToolTip('<b>密码</b>是登录访问Nifi页面的密码')
        # 工厂定制
        self.help_46.setToolTip('<b>重构版本</b>主要针对业务端服务而言，业务端服务有重构前后之分，默认重构后版本')
        self.help_47.setToolTip('<b>遏制</b>指追溯分析系统是否需要遏制功能')
        self.help_48.setToolTip('<b>设备维护</b>指追溯分析系统是否需要设备维护类的功能')
        self.help_49.setToolTip('<b>工具管理</b>指追溯分析系统是否需要工具类的功能')
        self.help_50.setToolTip('<b>FGB</b>指追溯分析系统是否需要FGB功能')
        self.help_51.setToolTip('<b>视频监控</b>指追溯分析系统是否需要视频监控的功能')
        self.help_52.setToolTip('<b>断链</b>指追溯分析系统是否需要断链的功能')
        self.help_53.setToolTip('<b>过滤万能工单</b>指追溯分析系统对测试用的万能功能数据进行过滤')


