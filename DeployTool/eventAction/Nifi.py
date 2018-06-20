#encoding=utf-8

__author__='zhaicao'


import urllib.request
import urllib.parse
import urllib.error
import ssl
import json
import lxml.etree as etree
from requests_toolbelt.multipart.encoder import MultipartEncoder
import copy


# 封装Nifi常用的api
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
        getParams = urllib.parse.urlencode(value).encode('UTF-8')
        request = urllib.request.Request(self._url + "/nifi-api/access/token", getParams)
        response = urllib.request.urlopen(request)
        self._token = "Bearer " + response.read().decode('UTF-8')

    #获得Group基本信息
    def getProcessGroups(self, Group):
        headers = {'Authorization': self._token, 'Content-Type':'application/json'}
        request = urllib.request.Request(self._url + "/nifi-api/flow/process-groups/"+ Group, headers= headers)
        response = urllib.request.urlopen(request)
        return json.loads(response.read())

    #获得全部模板信息
    def getTemplates(self):
        headers = {'Authorization': self._token, 'Content-Type':'application/json'}
        request = urllib.request.Request(self._url + "/nifi-api/flow/templates", headers=headers)
        response = urllib.request.urlopen(request)
        data = json.loads(response.read())
        return data['templates']

    #根据id删除模板
    def deleteTemplates(self, templateId):
        headers = {'Authorization': self._token, 'Content-Type':'application/json'}
        request = urllib.request.Request(self._url + "/nifi-api/templates/" + templateId, headers=headers)
        request.get_method = lambda: 'DELETE'
        response = urllib.request.urlopen(request)
        return response.read().decode('UTF-8')

    # 根据id下载模板
    def downloadTemplates(self, templateId):
        headers = {'Authorization': self._token, 'Content-Type':'application/json'}
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
        request = urllib.request.Request(self._url + "/nifi-api/process-groups/" + groupId + "/template-instance", json.dumps(postParams).encode('utf-8'), headers)
        response = urllib.request.urlopen(request)

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
        return response.read().decode('UTF-8')


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
        request = urllib.request.Request(self._url + "/nifi-api/controller-services/" + conserviceId, data = json.dumps(postParams).encode('UTF-8'), headers = headers)
        request.get_method = lambda: 'PUT'
        response = urllib.request.urlopen(request)
        return json.loads(response.read())

    #删除processgroup
    def delProcessGroup(self, id, version=0):
        headers = {'Authorization': self._token, 'Content-Type':'application/json'}
        request = urllib.request.Request(self._url + "/nifi-api/process-groups/" + id + '?version=' + str(version), headers=headers)
        request.get_method = lambda: 'DELETE'
        response = urllib.request.urlopen(request)
        return response.read().decode('UTF-8')


    #更新processGroup运行状态
    def updateProcessGroupState(self, id, state):
        headers = {'Authorization': self._token, 'Content-Type': 'application/json'}
        postParams = {
            'id' : id,
            'state' : state
        }
        request = urllib.request.Request(self._url + "/nifi-api/flow/process-groups/" + id, data=json.dumps(postParams).encode('UTF-8'), headers=headers)
        request.get_method = lambda: 'PUT'
        response = urllib.request.urlopen(request)
        return json.loads(response.read())

    #获得clientId
    def getClientId(self):
        headers = {'Authorization': self._token, 'Content-Type':'application/json'}
        request = urllib.request.Request(self._url + "/nifi-api/flow/client-id",headers=headers)
        response = urllib.request.urlopen(request)
        return response.read().decode('UTF-8')

    #更新控制服务器的引用
    def updateConServiceRefrence(self, conserviceId, referencs):
        headers = {'Authorization': self._token, 'Content-Type': 'application/json'}
        postParams = {
            'id' : conserviceId,
            'state' : 'STOPPED',
            'referencingComponentRevisions': referencs
        }
        request = urllib.request.Request(self._url + "/nifi-api/controller-services/" + conserviceId + '/references', data = json.dumps(postParams).encode('UTF-8'), headers = headers)
        request.get_method = lambda: 'PUT'
        response = urllib.request.urlopen(request)
        return json.loads(response.read())

    #获得单个proceeor的配置信息
    def getProcessorInfo(self, processorId):
        headers = {'Authorization': self._token, 'Content-Type':'application/json'}
        request = urllib.request.Request(self._url + "/nifi-api/processors/" + processorId,
                                  headers= headers)
        response = urllib.request.urlopen(request)
        return json.loads(response.read())

    #更新Processor的config的配置项
    def updateProcessorConf(self, processorId, processorName, configItem, confData, version):
        headers = {'Authorization': self._token, 'Content-Type': 'application/json'}
        postParams = {
            'component':{
                'id': processorId,
                'name': processorName,
                'state': "STOPPED",
                'config': {
                    configItem: confData
                }
        },
            'revision':{
                'clientId': self.getClientId(),
                'version': version
            }
        }
        request = urllib.request.Request(self._url + "/nifi-api/processors/" + processorId,
                                  data=json.dumps(postParams).encode('UTF-8'), headers= headers)
        request.get_method = lambda: 'PUT'
        response = urllib.request.urlopen(request)
        return json.loads(response.read())

    #根据路径返回Processor的Id
    def getProcessorId(self, path):
        index = 0
        groupIds = ['root']
        isProcess = True
        while(index < len(path)):
            for uuid in groupIds:
                isFind = True
                if isProcess:
                    groups= self.getProcessGroups(uuid)['processGroupFlow']['flow']['processGroups']
                    for i in groups:
                        if path[index] == i['status']['aggregateSnapshot']['name']:
                            groupIds.append(i['status']['aggregateSnapshot']['id'])
                            isFind = False
                            break
                    if isFind:
                        processes= self.getProcessGroups(uuid)['processGroupFlow']['flow']['processors']
                        for p in processes:
                            if path[index] == p['status']['aggregateSnapshot']['name']:
                                groupIds.append(p['status']['aggregateSnapshot']['id'])
                                isProcess = False
                                break
            index += 1
        if groupIds[-1] == 'root':
            return None
        return groupIds[-1]

    #根据路径返回Processor的Id集合
    def getProcessorIdsByPath(self, path):
        proIds = []
        index = 0
        groupIds = [['root'], [], [], []]
        while(index < len(path)):
            for uuid in groupIds[index]:
                groups= self.getProcessGroups(uuid)['processGroupFlow']['flow']['processGroups']
                for i in groups:
                    if path[index] == '*' or path[index] == i['status']['aggregateSnapshot']['name']:
                        groupIds[index+1].append(i['status']['aggregateSnapshot']['id'])
                processes= self.getProcessGroups(uuid)['processGroupFlow']['flow']['processors']
                for p in processes:
                    if path[-1] in p['status']['aggregateSnapshot']['name']:
                        proIds.append(p['status']['aggregateSnapshot']['id'])
            index += 1
        return proIds

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
                                  data= json.dumps(postParams).encode('UTF-8'), headers= headers)
        response = urllib.request.urlopen(request)
        return json.loads(response.read())

    # 设置事务的登录账号密码
    # 参数：
    # processorId：事务Id的姓名
    def setTransactionAuth(self, processorId, processorName, version):
        headers = {'Authorization': self._token, 'Content-Type': 'application/json'}
        postParams = {
            'component': {
                'id': processorId,
                'name': processorName,
                'state': "STOPPED",
                'config': {
                    'properties': {
                        'nifi-user-name': self._username,
                        'nifi-user-password': self._password
                    }
                }
            },
            'revision': {
                'clientId': self.getClientId(),
                'version': version
            }
        }
        request = urllib.request.Request(self._url + "/nifi-api/processors/" + processorId,
                                  data=json.dumps(postParams).encode('UTF-8'), headers=headers)
        request.get_method = lambda: 'PUT'
        response = urllib.request.urlopen(request)
        return json.loads(response.read())


class Nifi(object):
    # 返回Nifi状态
    # 参数：无
    # 返回值：Run:运行中，Stop：停止
    def nifiStatus(self, url):
        try:
            ssl._create_default_https_context = ssl._create_unverified_context
            response = urllib.request.urlopen(url + "/nifi")
            if response.read():
                return 'Run'
        except urllib.error.URLError:
            return 'Stop'

    # 启动Nifi，轮询判断是否启动成功
    # 参数: nifiHome:Nifi版本，timeout(可选)：超时时间，单位s
    # 返回值，True：成功，False，启动失败或超时
    def startNifi(self, url, timeout=60):
        import time
        # 启动nifi程序
        timer = 0
        while True:
            if self.nifiStatus(url) == 'Run':
                break
            else:
                if timer >= timeout:
                    return False
                time.sleep(1)
                timer += 1
        return True

    # 重新部署模板
    def reDeploymTemplate(self, nifiConf):
        # 根据权限拼接URL
        if nifiConf['nifi.auth'] == 'false':
            nifiConf['nifi.host'] = 'http://' + nifiConf['nifi.host'] + ':' + nifiConf['nifi.port']
        else:
            nifiConf['nifi.host'] = 'https://' + nifiConf['nifi.host'] + ':' + nifiConf['nifi.port']

        dbConf = self.getDBConf(nifiConf)

        # 判断Nifi是否启动
        if not self.startNifi(nifiConf['nifi.host'], 600):
            print('NIfi未启动')
            return False

        # 初始化nifi，获得基础信息
        nifi = NifiApi(nifiConf['nifi.host'], nifiConf['nifi.user'], nifiConf['nifi.pwd'])
        groupInfo = nifi.getProcessGroups('root')
        uuid = groupInfo['processGroupFlow']['breadcrumb']['breadcrumb']['id']

        try:
            # 遍历groups并依次停止删除groups
            for group in groupInfo['processGroupFlow']['flow']['processGroups']:
                nifi.updateProcessGroupState(group['status']['aggregateSnapshot']['id'], 'STOPPED')
                nifi.delProcessGroup(group['status']['aggregateSnapshot']['id'], group['revision']['version'])
        except:
            print('删除Groups异常')
            return False

        try:
            # 获得所有模板，遍历并删除
            for template in nifi.getTemplates():
                nifi.deleteTemplates(template['id'])
        except:
            print('删除Templates异常')
            return False

        # 根据模板路径上传模板
        if not nifi.uploadTemplate(nifiConf['nifi.template'], uuid):
            return False

        try:
            # 停止全部连接池控制器
            for conServices in nifi.getAllConServices(uuid)['controllerServices']:
                nifi.updateConService(conserviceId=conServices['component']['id'],
                                      version=conServices['revision']['version'],
                                      state='DISABLED')
            # 删除控制器(停止和删除不能在同一循环下)
            for conServices in nifi.getAllConServices(uuid)['controllerServices']:
                nifi.delConServices(conServices['component']['id'], conServices['revision']['version'])
        except:
            print('删除Controller Service异常')
            return False

        try:
            # 实例化模板
            for template in nifi.getTemplates():
                nifi.instantiateTemplate(uuid, template['id'])
        except:
            print('实例化Template异常')
            return False

        try:
            # 更新全部连接池控制器并启用
            for conServers in nifi.getAllConServices(uuid)['controllerServices']:
                if conServers['component']['name'] in dbConf:
                    nifi.updateConService(conserviceId=conServers['component']['id'],
                                          version=conServers['revision']['version'],
                                          data=dbConf[conServers['component']['name']]
                                          )
        except:
            print('更新Controller Service异常')
            return False

        try:
            # 启用全部连接池控制器
            for conServers in nifi.getAllConServices(uuid)['controllerServices']:
                if conServers['component']['name'] == u'HistoryConnectionPool' and nifiConf['HistoryConnectionPool.enable'].lower() != 'true':
                    pass
                elif conServers['component']['name'] == u'PPConnectionPool' and nifiConf['PPConnectionPool.enable'].lower() != 'true':
                    pass
                else:
                    nifi.updateConService(conserviceId=conServers['component']['id'],
                                    version=conServers['revision']['version'],
                                    state='ENABLED'
                                    )
        except:
            print('启用Controller Service异常')
            return False
        return True


# 获得数据库基础配置
    # 参数：confPath - 配置文件路径
    def getDBConf(self, confPath):
        _dbConf = {'SqlConnectionPool': None, 'BIConnectionPool': None, 'PPConnectionPool': None,
                   'HistoryConnectionPool': None}
        try:
            for index in _dbConf:
                _dbConf[index] = {
                    'Database Connection URL': 'jdbc:sqlserver://' + confPath[index + '.host'] + ':' + confPath[index + '.port'] + ';database=' + confPath[index + '.db'],
                    'database-driver-locations': '../conf/custom_lib/mssql-jdbc-6.2.2.jre8.jar',
                    'Database User': confPath[index + '.user'],
                    'Password': confPath[index + '.pwd'],
                    'Validation-query': 'SELECT 1'
                }
        except:
            print('数据库配置文件读取异常')
        return _dbConf

if __name__=='__main__':
    pass