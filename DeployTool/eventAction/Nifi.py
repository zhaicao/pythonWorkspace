#encoding=utf-8

__author__='zhaicao'

import urllib.request
import urllib.parse
import urllib.error
import json
import ssl
import lxml.etree as etree
from requests_toolbelt.multipart.encoder import MultipartEncoder
import os
import sys
import time
from Util import *

#NifiAPi调用类
class NifiApi(object):
    _url = ''
    _username = ''
    _password = ''
    _token = ''

    def __init__(self, url, username, password):
        self._url = url
        self._username = username
        self._password = password
        if 'https' in self._url.lower():
            self.getToken()

    #获取验证Token
    def getToken(self):
        # 忽略SSL不受信任
        ssl._create_default_https_context = ssl._create_unverified_context
        value = {"username": self._username, "password":self._password}
        getParams = urllib.parse.urlencode(value)
        request = urllib.request.Request(self._url + "/nifi-api/access/token", getParams)
        response = urllib.request.urlopen(request)
        self._token = "Bearer " + response.read()

    #获得Group基本信息
    def getProcessGroups(self, Group):
        content_type = "content_type = 'application/json'"
        headers = {'Authorization': self._token}
        request = urllib.request.Request(self._url + "/nifi-api/flow/process-groups/"+ Group, headers= headers)
        response = urllib.request.urlopen(request)
        return json.loads(response.read())

    #获得全部模板信息
    def getTemplates(self):
        content_type = "content_type = 'application/json'"
        headers = {'Authorization': self._token}
        request = urllib.request.Request(self._url + "/nifi-api/flow/templates", headers=headers)
        response = urllib.request.urlopen(request)
        data = json.loads(response.read())
        return data['templates']

    #根据id删除模板
    def deleteTemplates(self, templateId):
        headers = {'Authorization': self._token}
        request = urllib.request.Request(self._url + "/nifi-api/templates/" + templateId, headers=headers)
        request.get_method = lambda: 'DELETE'
        response = urllib.request.urlopen(request)
        return response.read()

    # 根据id下载模板
    def downloadTemplates(self, templateId):
        headers = {'Authorization': self._token}
        request = urllib.request.Request(self._url + "/nifi-api/templates/" + templateId + "/download", headers = headers)
        response = urllib.request.urlopen(request)
        data = response.read()
        tree = etree.HTML(data)
        xpathlist = tree.xpath("//templates/name")
        for item in xpathlist:
            filename = (item.xpath('string(.)'))
        file = open('D:/' + filename +'.xml','w')
        file.write(data)
        file.close()

    #上传模板
    def uploadTemplate(self, filePath, uuId):
        mData = MultipartEncoder(
            fields={'template': open(filePath, 'rb')}
        )
        headers = {
            'Authorization': self._token,
            'Content-Type': mData.content_type,
            'Content-Length': mData.len
        }
        request = urllib.request.Request(self._url + "/nifi-api/process-groups/" + uuId + "/templates/upload", mData, headers)
        try:
            response = urllib.request.urlopen(request).read()
        except urllib.error.HTTPError as e:
            print(e,'该模板已存在')
            return False
        except:
            print('其他异常，上传失败')
            return False
        else:
            return response

    #实例化模板
    def instantiateTemplate(self, groupId, templateId):
        headers = {'Authorization': self._token, 'Content-Type':'application/json'}
        postParams = {
            "originX": 200.0,
            "originY": 200.0,
            "templateId": templateId
        }
        request = urllib.request.Request(self._url + "/nifi-api/process-groups/" + groupId + "/template-instance", json.dumps(postParams), headers)
        response = urllib.request.urlopen(request)
        #return response.read()

    #获得全部控制器
    def getAllConServices(self, groupId):
        headers = {'Authorization': self._token}
        request = urllib.request.Request(self._url + "/nifi-api/flow/process-groups/" + groupId + "/controller-services", headers = headers)
        response = urllib.request.urlopen(request)
        return json.loads(response.read())

    #获得单个控制器信息
    def getConService(self, conServiceId):
        headers = {'Authorization': self._token}
        request = urllib.request.Request(self._url + "/nifi-api/controller-services/" + conServiceId,
                                  headers=headers)
        response = urllib.request.urlopen(request)
        return json.loads(response.read())


    #删除控制器
    def delConServices(self, ConServiceId, version):
        headers = {'Authorization': self._token}
        request = urllib.request.Request(self._url + "/nifi-api/controller-services/" + ConServiceId + "?version=" + str(version), headers=headers)
        request.get_method = lambda: 'DELETE'
        response = urllib.request.urlopen(request)
        return response.read()


    # 更新控制器配置参数
    def updateConService(self, conserviceId, version, conserviceName=None, data=None, state=None):
        headers = {'Authorization': self._token, 'Content-Type': 'application/json','User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36','X-Requested-With':'XMLHttpRequest'}
        postParams = {
            'component':{'id': conserviceId,
                         },
            'revision':{
                'clientId': self.getClientId(),
                'version' : version
                         }
        }
        if state == 'DISABLED':
            postParams['component']['state'] = state
        else :
            if conserviceName:
                postParams['component']['name'] = conserviceName
            if data:
                postParams['component']['properties'] = data
            if state:
                postParams['component']['state'] = state
        request = urllib.request.Request(self._url + "/nifi-api/controller-services/" + conserviceId, data = json.dumps(postParams), headers = headers)
        request.get_method = lambda: 'PUT'
        response = urllib.request.urlopen(request)
        return json.loads(response.read())

    #删除processgroup
    def delProcessGroup(self, id, version=0):
        headers = {'Authorization': self._token}
        request = urllib.request.Request(self._url + "/nifi-api/process-groups/" + id + '?version=' + str(version), headers=headers)
        request.get_method = lambda: 'DELETE'
        response = urllib.request.urlopen(request)
        return response.read()


    #更新processGroup运行状态
    def updateProcessGroupState(self, id, state):
        headers = {'Authorization': self._token, 'Content-Type': 'application/json'}
        postParams = {
            'id' : id,
            'state' : state
        }
        request = urllib.request.Request(self._url + "/nifi-api/flow/process-groups/" + id, data=json.dumps(postParams), headers=headers)
        request.get_method = lambda: 'PUT'
        response = urllib.request.urlopen(request)
        return json.loads(response.read())

    #获得clientId
    def getClientId(self):
        headers = {'Authorization': self._token}
        request = urllib.request.Request(self._url + "/nifi-api/flow/client-id",headers=headers)
        response = urllib.request.urlopen(request)
        return response.read()

    #更新控制服务器的引用
    def updateConServiceRefrence(self, conserviceId, referencs):
        headers = {'Authorization': self._token, 'Content-Type': 'application/json'}
        postParams = {
            'id' : conserviceId,
            'state' : 'STOPPED',
            'referencingComponentRevisions': referencs
        }
        request = urllib.request.Request(self._url + "/nifi-api/controller-services/" + conserviceId + '/references', data = json.dumps(postParams), headers = headers)
        request.get_method = lambda: 'PUT'
        response = urllib.request.urlopen(request)
        return json.loads(response.read())

    #获得单个proceeor的配置信息
    def getProcessorInfo(self, processorId):
        headers = {'Authorization': self._token}
        request = urllib.request.Request(self._url + "/nifi-api/processors/" + processorId,
                                  headers= headers)
        response = urllib.request.urlopen(request)
        return json.loads(response.read())

    #更新Processor的properties的配置
    def updateProcessorConf(self, processorId, processorName, confData, version):
        headers = {'Authorization': self._token, 'Content-Type': 'application/json'}
        postParams = {
            'component':{
                'id': processorId,
                'name': processorName,
                'state': "STOPPED",
                'config': {
                    'properties': confData
                }
        },
            'revision':{
                'clientId': self.getClientId(),
                'version': version
            }
        }
        request = urllib.request.Request(self._url + "/nifi-api/processors/" + processorId,
                                  data=json.dumps(postParams), headers= headers)
        request.get_method = lambda: 'PUT'
        response = urllib.request.urlopen(request)
        return json.loads(response.read())

    #根据路径返回Processor的Id
    def getProcessorId(self, path):
        index = 0
        uuid = 'root'
        while(index < len(path)):
            groups= self.getProcessGroups(uuid)['processGroupFlow']['flow']['processGroups']
            if groups:
                for i in groups:
                    if i['status']['aggregateSnapshot']['name'] == path[index]:
                        uuid = i['status']['aggregateSnapshot']['id']
            else:
                processors= self.getProcessGroups(uuid)['processGroupFlow']['flow']['processors']
                if processors:
                    for i in processors:
                        if i['status']['aggregateSnapshot']['name'] == path[index]:
                            uuid = i['status']['aggregateSnapshot']['id']
            index += 1
        return uuid

    # 获得Variables参数
    def getVariables(self, processGroupId):
        headers = {'Authorization': self._token}
        request = urllib.request.Request(self._url + "/nifi-api/process-groups/" + processGroupId+ '/variable-registry',
                                  headers=headers)
        response = urllib.request.urlopen(request)
        return json.loads(response.read())

    # 设置Variables参数
    def setVariables(self, processGroupId, Name, Value):
        headers = {'Authorization': self._token, 'Content-Type': 'application/json'}
        postParams = {
            'processGroupRevision': {
                'clientId': self.getClientId(),
                'version': self.getVariables(processGroupId)['processGroupRevision']['version'],
            },
            'variableRegistry': {
                'processGroupId': processGroupId,
                'variables': [{
                    'variable': {
                        'name': Name,
                        'value': Value
                                }
                    }
                ]
            }
        }
        request = urllib.request.Request(self._url + "/nifi-api/process-groups/" + processGroupId + '/variable-registry/update-requests',
                                  data= json.dumps(postParams), headers= headers)
        response = urllib.request.urlopen(request)
        return json.loads(response.read())

# 定义Nifi异常
class nifiError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)



#Nifi执行类
class Nifi(object):

    #初始化Nifi参数及数据库配置
    def __init__(self, confPath= 'config.properties'):
        # 获得基础配置
        properties= Properties(getAbsPath(confPath))
        self._host= properties.get('nifi_host')
        self._port= properties.get('nifi_port')
        self._auth = properties.get('nifi_auth_enable')
        self._IsExtractHis= properties.get('isExtractHis')
        self._ppDir= properties.get('ppDir')
        self._JAVA_HOME= properties.get('JAVA_HOME')
        self._NIFI_DIR= properties.get('NIFI_HOME')
        self._JVMmem= properties.get('nifi_JVM')
        self._username= None
        self._password= None

        # 获取是否启用登录
        if self._auth.lower() == 'true':
            self._url= 'https://'
            self._username= properties.get('nifi_username')
            self._password= properties.get('nifi_password')
        else:
            self._url= 'http://'
        # 组装URL
        self._url += properties.get('nifi_host') + ':' + properties.get('nifi_port')

        # 数据库配置
        self._dbConf = {'SqlConnectionPool': None, 'BIConnectionPool': None, 'PPConnectionPool': None,
                        'HistoryConnectionPool': None}
        for index in self._dbConf:
            if 'Sql' in index: item = 'MIOT'
            elif 'BI' in index: item = 'BI'
            elif 'History' in index: item = 'HIS'
            elif 'PP' in index: item = 'PP'
            else:
                raise ValueError
            self._dbConf[index] = {
                'Database Connection URL': 'jdbc:sqlserver://' + properties.get(
                item + '_Database_Host') + ';database=' + properties.get(item + '_Database_Name'),
                'database-driver-locations': '../conf/custom_lib/mssql-jdbc-6.2.2.jre8.jar',
                'Database User': properties.get(item + '_Database_Username'),
                'Password': properties.get(item + '_Database_Password'),
                'Validation-query': 'SELECT 1'
            }

    #返回Nifi状态
    #参数：无
    #返回值：Run:运行中，Stop：停止
    def nifiStatus(self):
        try:
            ssl._create_default_https_context = ssl._create_unverified_context
            response = urllib2.urlopen(self._url + "/nifi")
            if response.read():
                return 'Run'
        except urllib.error.URLError:
            return 'Stop'

    #启动Nifi，轮询判断是否启动成功
    #参数: nifiHome:Nifi版本，timeout(可选)：超时时间，单位s
    #返回值，True：成功，False，启动失败或超时
    def startNifi(self, nifiHome, timeout=60):
        #启动nifi程序
        os.startfile(self._NIFI_DIR+ 'Nifi/'+ nifiHome+ '/bin/start-nifi.bat')
        time.sleep(2)
        timer = 0
        while True:
            if self.nifiStatus()== 'Run':
                break
            else:
                if timer >= timeout:
                    return False
                time.sleep(1)
                timer+= 1
                #进度条
                if timer % 4 == 0: bar= '   '
                elif timer % 4 == 1: bar= '.  '
                elif timer % 4 == 2: bar = '.. '
                else: bar = '...'
                sys.stdout.write('\rNifi服务启动较慢，请不要关闭新窗口(默认10min超时)'+ bar)
                sys.stdout.flush()
        return True

    #实例化模板并修改连接池控制器
    #返回值：True:成功，False：失败
    def instanceTem(self):
        # 初始化NifiAppi对象,获得rootGroupsId
        api = NifiApi(self._url, self._username, self._password)
        groupInfo = api.getProcessGroups('root')
        rootGroupsId = groupInfo['processGroupFlow']['breadcrumb']['breadcrumb']['id']
        # 遍历groups并依次停止删除groups
        try:
            for group in groupInfo['processGroupFlow']['flow']['processGroups']:
                api.updateProcessGroupState(group['status']['aggregateSnapshot']['id'], 'STOPPED')
                api.delProcessGroup(group['status']['aggregateSnapshot']['id'], group['revision']['version'])
        except:
            print('删除Groups异常')
            return False
        # 停止全部连接池控制器
        try:
            for conServices in api.getAllConServices(rootGroupsId)['controllerServices']:
                api.updateConService(conserviceId=conServices['component']['id'],
                                      version=conServices['revision']['version'],
                                      state='DISABLED')
            # 删除控制器(停止和删除不能在同一循环下)
            for conServices in api.getAllConServices(rootGroupsId)['controllerServices']:
                api.delConServices(conServices['component']['id'], conServices['revision']['version'])
        except:
            print('删除Controller Service异常')
            return False

        try:
            # 实例化模板
            for template in api.getTemplates():
                api.instantiateTemplate(rootGroupsId, template['id'])
        except:
            print('实例化Template异常')
            return False

        try:
            # 更新全部连接池控制器
            for conServers in api.getAllConServices(rootGroupsId)['controllerServices']:
                if self._dbConf.has_key(conServers['component']['name']):
                    api.updateConService(conserviceId=conServers['component']['id'],
                                          version=conServers['revision']['version'],
                                          data=self._dbConf[conServers['component']['name']]
                                          )
        except:
            print('更新Controller Service异常')
            return False

        try:
            # 启用全部连接池控制器
            for conServers in api.getAllConServices(rootGroupsId)['controllerServices']:
                api.updateConService(conserviceId=conServers['component']['id'],
                                    version=conServers['revision']['version'],
                                    state='ENABLED'
                                    )
        except:
            print('启用Controller Service异常')
            return False

        return True

    #设置是否抽取历史库
    #返回值：True：成功，False：失败
    def setIsExtractHis(self):
        path = ['3.增量抽取流程', '通用ETL增量抽取流程', 'Ods Group', 'Extract Data']
        api = NifiApi(self._url, self._username, self._password)
        proId = api.getProcessorId(path)
        rootId = api.getProcessGroups('root')['processGroupFlow']['breadcrumb']['breadcrumb']['id']
        data = {'history-dbcp-service': None}

        if self._IsExtractHis:
            for i in api.getAllConServices(rootId)['controllerServices']:
                if i['component']['name'] == 'HistoryConnectionPool':
                    data['history-dbcp-service'] = i['component']['id']
        try:
            api.updateProcessorConf(proId, "Extract Data", data, api.getProcessorInfo(proId)['revision']['version'])
        except:
            return False
        return True

    # 设置Variables
    # 返回值：True成功，False失败
    def setVariables(self):
        api = NifiApi(self._url, self._username, self._password)
        rootGroupId= api.getProcessGroups('root')['processGroupFlow']['breadcrumb']['breadcrumb']['id']
        try:
            api.setVariables(rootGroupId, 'ppDir', self._ppDir)
        except:
            return False
        return True

    # 设置工厂定制配置
    # 参数Nifi_Home: Nifi目录
    # 返回值: True成功，False失败
    def setCustomPro(self, nifiHome):
        try:
            FileUtil().copy_file(getAbsPath('manifest.properties'), self._NIFI_DIR+ 'Nifi/'+ nifiHome+ '/conf/custom.properties')
        except:
            return False
        return True

    #设置Nifi基础配置
    #参数：Nifi_Home: Nifi根目录
    #返回值: True:成功，False：失败
    def setNifiPro(self, nifiHome):
        try:
            nifiPro= Properties(self._NIFI_DIR+ 'Nifi/'+ nifiHome+ '/conf/nifi.properties')
            #设置Nifi地址及端口
            if self._auth.lower() == 'true':
                nifiPro.put('nifi.web.https.host', self._host)
                nifiPro.put('nifi.web.https.port', self._port)
                nifiPro.put('nifi.web.http.host', '')
                nifiPro.put('nifi.web.http.port', '')
            else:
                nifiPro.put('nifi.web.http.host', self._host)
                nifiPro.put('nifi.web.http.port', self._port)
                nifiPro.put('nifi.web.https.host', '')
                nifiPro.put('nifi.web.https.port', '')
        except:
            print('nifi.properties Error')
            return False
        try:
            #设置Nifi启动JVM内存
            nifiBootstrap = Properties(self._NIFI_DIR+ 'Nifi/'+ nifiHome + '/conf/bootstrap.conf')
            nifiBootstrap.put('java.arg.2', '-Xms'+ self._JVMmem+ 'm')
            nifiBootstrap.put('java.arg.3', '-Xms'+ self._JVMmem+ 'm')
        except:
            print('bootstrap.conf Error')
            return False
        # 设置nifi-env.bat
        # with open('Nifi/nifi-1.4.0/bin/nifi-env.bat', 'a') \
        #         as  file:
        #     file.write('\n\nset JAVA_HOME=' + self._JAVA_HOME)
        return True


    #实例化Nifi，设置是否抽取历史库，设置Variables
    #返回值：全部成功返回True，失败返回False
    def setFullNifi(self):
        if not self.instanceTem(): return False
        if not self.setIsExtractHis(): return False
        if not self.setVariables(): return False
        return True

    # Nifi基础设置，未启动前
    def setBasicNifi(self, nifiHome):
        if not self.setCustomPro(nifiHome): return False
        if not self.setNifiPro(nifiHome): return False
        return True

    #解压Nifi文件夹
    def unZipNifi(self):
        try:
            zipFileNames = FileUtil().file_name(os.path.abspath('.'), 'zip')
            for file in zipFileNames:
                if file.find('ETL') >= 0:
                    # 解压Nifi
                    FileUtil().Decompression(os.path.abspath('.') + '/' + file, self._NIFI_DIR)
            return True
        except:
            print('发布件解压异常')
            return False

    # 完整部署ETL服务
    def completeDep(self, nifiHome):
        # 解压Nifi
        # windows CMD下需使用os.system('cls')清屏
        sys.stdout.write('\r正在解压Nifi')
        if self.unZipNifi():
            # 判断Nifi运行状态
            if self.nifiStatus() == 'Stop':
                # Nifi基础设置
                sys.stdout.write('\r                    ')
                sys.stdout.write('\r正在进行Nifi基础设置')
                if self.setBasicNifi(nifiHome):
                    # 启动Nifi，10min超时
                    if self.startNifi(nifiHome, 600):
                        # Nifi配置
                        sys.stdout.write('\r                                            ')
                        sys.stdout.write('\r正在配置Nifi')
                        if self.setFullNifi():
                            sys.stdout.write('\r                    ')
                            sys.stdout.write('\rETL安装完成')
                        else:
                            sys.stdout.write('\nNifi配置失败,请重试')
                            raise nifiError('配置错误')
                    else:
                        sys.stdout.write('\nNifi启动失败,请重试')
                        raise nifiError('启动错误')
                else:
                    sys.stdout.write('\nNifi基础设置失败,请重试')
                    raise nifiError('基础设置错误')
            else:
                sys.stdout.write('\nNifi正在运行，请关闭Nifi服务后，重试')
                raise nifiError('Nifi正在运行，无法进行基础设置')
        else:
            sys.stdout.write('\nNifi解压失败,请重试')
            raise nifiError('解压错误')

if __name__=="__main__":
    nifi = Nifi()
    Nifi_Home = 'nifi-1.4.0'
    nifi.completeDep(Nifi_Home)
