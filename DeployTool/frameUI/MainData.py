# -*- coding: utf-8 -*-

# 定义配置输入项和控件对应关系字典

__author__ = 'zhaicao'

from PyQt5 import QtWidgets

class TraceObjItems(object):

    def initObjItems(self):
        self.TraceConfItems()

    def TraceConfItems(self):
        # 定义部署配置控件类型和名称对应的字典
        self.deployConfItem = {
            # 业务库Group
            'dep_input_1': {'objType': QtWidgets.QLineEdit, 'confItem': 'MIOT_Database_Host'},
            'dep_input_2': {'objType': QtWidgets.QLineEdit, 'confItem': 'MIOT_Database_Port'},
            'dep_input_3': {'objType': QtWidgets.QLineEdit, 'confItem': 'MIOT_Database_Username'},
            'dep_input_4': {'objType': QtWidgets.QLineEdit, 'confItem': 'MIOT_Database_Password'},
            'dep_input_5': {'objType': QtWidgets.QComboBox, 'confItem': 'MIOT_Database_Name'},
            'getDBBtn_1': {'objType': QtWidgets.QPushButton},
            # 历史库Group
            'dep_input_6': {'objType': QtWidgets.QCheckBox, 'confItem': 'isExtractHis'},
            'dep_input_7': {'objType': QtWidgets.QLineEdit, 'confItem': 'HIS_Database_Host'},
            'dep_input_8': {'objType': QtWidgets.QLineEdit, 'confItem': 'HIS_Database_Port'},
            'dep_input_9': {'objType': QtWidgets.QLineEdit, 'confItem': 'HIS_Database_Username'},
            'dep_input_10': {'objType': QtWidgets.QLineEdit, 'confItem': 'HIS_Database_Password'},
            'dep_input_11': {'objType': QtWidgets.QComboBox, 'confItem': 'HIS_Database_Name'},
            'getDBBtn_2': {'objType': QtWidgets.QPushButton},
            # BI库Group
            'dep_input_12': {'objType': QtWidgets.QLineEdit, 'confItem': 'BI_Database_Host'},
            'dep_input_13': {'objType': QtWidgets.QLineEdit, 'confItem': 'BI_Database_Port'},
            'dep_input_14': {'objType': QtWidgets.QLineEdit, 'confItem': 'BI_Database_Username'},
            'dep_input_15': {'objType': QtWidgets.QLineEdit, 'confItem': 'BI_Database_Password'},
            'dep_input_16': {'objType': QtWidgets.QLineEdit, 'confItem': 'BI_Database_Name'},
            'dep_input_17': {'objType': QtWidgets.QLineEdit, 'confItem': 'extractSourceId'},
            'dep_input_18': {'objType': QtWidgets.QLineEdit, 'confItem': 'extractSourceName'},
            # 系统库Group
            'dep_input_19': {'objType': QtWidgets.QLineEdit, 'confItem': 'DAS_Database_Host'},
            'dep_input_20': {'objType': QtWidgets.QLineEdit, 'confItem': 'DAS_Database_Port'},
            'dep_input_21': {'objType': QtWidgets.QLineEdit, 'confItem': 'DAS_Database_Username'},
            'dep_input_22': {'objType': QtWidgets.QLineEdit, 'confItem': 'DAS_Database_Password'},
            'dep_input_23': {'objType': QtWidgets.QLineEdit, 'confItem': 'DAS_Database_Name'},
            # 工艺参数Group
            'dep_input_24': {'objType': QtWidgets.QCheckBox, 'confItem': 'das.custom.processParameter'},
            'dep_input_25': {'objType': QtWidgets.QCheckBox, 'confItem': 'processParameterNetDir'},
            'dep_input_26': {'objType': QtWidgets.QLineEdit, 'confItem': 'PPDBFile_path'},
            'dep_input_27': {'objType': QtWidgets.QLineEdit, 'confItem': 'PPDBFile_dir'},
            'dep_input_28': {'objType': QtWidgets.QLineEdit, 'confItem': 'PPDBFile_username'},
            'dep_input_29': {'objType': QtWidgets.QLineEdit, 'confItem': 'PPDBFile_password'},
            # 工艺参数库
            'dep_input_30': {'objType': QtWidgets.QLineEdit, 'confItem': 'PP_Database_Host'},
            'dep_input_31': {'objType': QtWidgets.QLineEdit, 'confItem': 'PP_Database_Port'},
            'dep_input_32': {'objType': QtWidgets.QLineEdit, 'confItem': 'PP_Database_Username'},
            'dep_input_33': {'objType': QtWidgets.QLineEdit, 'confItem': 'PP_Database_Password'},
            'dep_input_34': {'objType': QtWidgets.QLineEdit, 'confItem': 'PP_Database_Name'},
            # 基础配置
            'dep_input_35': {'objType': QtWidgets.QLineEdit, 'confItem': 'release_ver'},
            'dep_input_36': {'objType': QtWidgets.QLineEdit, 'confItem': 'operation_host'},
            'dep_input_37': {'objType': QtWidgets.QLineEdit, 'confItem': 'operation_portal'},
            # 部署程序
            'dep_input_38': {'objType': QtWidgets.QLineEdit, 'confItem': 'deliverable_dir_path'},
            'dep_input_39': {'objType': QtWidgets.QLineEdit, 'confItem': 'deliverable_username'},
            'dep_input_40': {'objType': QtWidgets.QLineEdit, 'confItem': 'deliverable_password'},
            # 部署地址
            'dep_input_41': {'objType': QtWidgets.QLineEdit, 'confItem': 'dest_path'},
            'dep_input_42': {'objType': QtWidgets.QLineEdit, 'confItem': 'tools_path'},
            'dep_input_43': {'objType': QtWidgets.QLineEdit, 'confItem': 'script_path'},
            # 基础配置
            'dep_input_44': {'objType': QtWidgets.QLineEdit, 'confItem': 'tomcat_port'},
            # 单点登录
            'dep_input_45': {'objType': QtWidgets.QCheckBox, 'confItem': 'das.custom.ssoLogin'},
            'dep_input_46': {'objType': QtWidgets.QLineEdit, 'confItem': 'system_auth_login_host_default'},
            'dep_input_47': {'objType': QtWidgets.QLineEdit, 'confItem': 'system_auth_login_portal'},
            'dep_input_48': {'objType': QtWidgets.QLineEdit, 'confItem': 'system_auth_login_api_portal'},
            # ETL配置
            'dep_input_49': {'objType': QtWidgets.QLineEdit, 'confItem': 'ppDir'},
            'dep_input_50': {'objType': QtWidgets.QLineEdit, 'confItem': 'nifi_port'},
            'dep_input_51': {'objType': QtWidgets.QLineEdit, 'confItem': 'nifi_JVM'},
            'dep_input_52': {'objType': QtWidgets.QLineEdit, 'confItem': 'biIncrementSchedule'},
            'dep_input_53': {'objType': QtWidgets.QCheckBox, 'confItem': 'nifi_auth_enable'},
            'dep_input_54': {'objType': QtWidgets.QLineEdit, 'confItem': 'nifi_username'},
            'dep_input_55': {'objType': QtWidgets.QLineEdit, 'confItem': 'nifi_password'}
        }
        # 定义工厂定制控件类型和名称对应的字典
        self.manifestConfItem = {
            'dep_input_56': {'objType': QtWidgets.QComboBox, 'confItem': 'das.custom.isOpDbBeforeRefact'},
            'dep_input_57': {'objType': QtWidgets.QComboBox, 'confItem': 'das.custom.supression'},
            'dep_input_58': {'objType': QtWidgets.QComboBox, 'confItem': 'das.custom.equipmentMaintenance'},
            'dep_input_59': {'objType': QtWidgets.QComboBox, 'confItem': 'das.custom.toolManagement'},
            'dep_input_60': {'objType': QtWidgets.QComboBox, 'confItem': 'das.custom.fgb'},
            'dep_input_61': {'objType': QtWidgets.QComboBox, 'confItem': 'das.custom.isVideoMonitorEnabled'},
            'dep_input_62': {'objType': QtWidgets.QComboBox, 'confItem': 'das.custom.linkRepair'},
            'dep_input_63': {'objType': QtWidgets.QComboBox, 'confItem': 'das.custom.isAutoOrderFiltered'}
        }