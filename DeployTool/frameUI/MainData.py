
# 定义配置输入项和控件对应关系字典

__author__ = 'zhaicao'

from PyQt5 import QtWidgets

class TraceItems(object):

    def TraceConfItems(self):
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
            'input_72': {'objType': QtWidgets.QCheckBox, 'confItem': 'processParameter'},
            'input_24': {'objType': QtWidgets.QCheckBox, 'confItem': 'processParameterNetDir'},
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
        self.manifestConfItem = {
            'input_60': {'objType': QtWidgets.QComboBox, 'confItem': 'isOpDbBeforeRefact'},
            'input_61': {'objType': QtWidgets.QComboBox, 'confItem': 'supression'},
            'input_62': {'objType': QtWidgets.QComboBox, 'confItem': 'equipmentMaintenance'},
            'input_63': {'objType': QtWidgets.QComboBox, 'confItem': 'toolManagement'},
            'input_64': {'objType': QtWidgets.QComboBox, 'confItem': 'fgb'},
            'input_65': {'objType': QtWidgets.QComboBox, 'confItem': 'isVideoMonitorEnabled'},
            'input_66': {'objType': QtWidgets.QComboBox, 'confItem': 'linkRepair'},
            'input_67': {'objType': QtWidgets.QComboBox, 'confItem': 'isAutoOrderFiltered'}
        }