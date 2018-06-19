#encoding=utf-8

__author__='zhaicao'

import ConfigParser
import os
import sys

_dbConf = {'SqlConnectionPool' : None, 'BIConnectionPool' : None, 'PPConnectionPool' : None, 'HistoryConnectionPool' : None}

#获取Nifi基础信息
def getNifiConf(confPath):
    cp = ConfigParser.SafeConfigParser()
    cp.read(confPath)
    try:
        return {
            'host' : cp.get('NIFI', 'host'),
            'username' : cp.get('NIFI', 'username'),
            'password' : cp.get('NIFI', 'password')
        }
    except:
        print('Nifi配置文件读取异常')
        return None

#获得数据库基础配置
#参数：confPath - 配置文件路径
def getDBConf(confPath):
    cp = ConfigParser.SafeConfigParser()
    cp.read(confPath)
    try:
        for index in _dbConf:
            _dbConf[index] = {
                    'Database Connection URL': 'jdbc:sqlserver://' + cp.get(index, 'host') + ':' + cp.get(index,'port') + ';database=' + cp.get(index, 'db'),
                    'database-driver-locations': cp.get(index, 'driver'),
                    'Database User': cp.get(index, 'user'),
                    'Password': cp.get(index, 'pwd'),
                    'Validation-query': 'SELECT 1'
            }
    except:
        print('数据库配置文件读取异常')
    return _dbConf

#获得上传文件的路径
#参数：directory - 文件所在目录
def getUploadTemNames(directory):
    #脚本和exe运行目录会不一致，需判断
    if getattr(sys, 'frozen', False):
        dir = os.path.dirname(sys.executable)
    elif __file__:
        dir = os.path.dirname(__file__)
    templates = []
    try:
        for file in os.listdir(os.path.join(dir, directory)):
            templates.append(os.path.join(dir, directory, file))
        if len(templates) == 0:
            print('templates does not exist')
            return None
        else:
            return templates
    except:
        print(directory + ' 目录不存在')
        return None

if __name__ == '__main__':
    print(getDBConf('dbconfig.conf'))

