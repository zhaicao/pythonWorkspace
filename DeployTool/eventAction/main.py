#encoding=utf-8

__author__='zhaicao'

import urllib.request
import urllib.error
import Conf
from Nifi import NifiApi
import ssl
import time
from Util import *

#返回Nifi状态
#参数：无
#返回值：Run:运行中，Stop：停止
def nifiStatus(url):
    try:
        ssl._create_default_https_context = ssl._create_unverified_context
        response = urllib.request.urlopen(url + "/nifi")
        if response.read():
            return 'Run'
    except urllib.error.URLError:
        return 'Stop'

#启动Nifi，轮询判断是否启动成功
#参数: nifiHome:Nifi版本，timeout(可选)：超时时间，单位s
#返回值，True：成功，False，启动失败或超时
def startNifi(url, timeout=60):
    #启动nifi程序
    timer = 0
    while True:
        if nifiStatus(url)== 'Run':
            break
        else:
            if timer >= timeout:
                return False
            time.sleep(1)
            timer+= 1
    return True

#重新部署模板
def reDeploymTemplate():
    print(getAbsPath('dbconfig.conf'))
    nifiConf = Conf.getNifiConf(getAbsPath('dbconfig.conf'))
    dbConf = Conf.getDBConf(getAbsPath('dbconfig.conf'))
    templates = Conf.getUploadTemNames('templates')
    if not nifiConf or not dbConf  or not templates :
        print('请检查配置、模板文件是否存在，再重试')
        return False
    # 判断Nifi是否启动
    if not startNifi(nifiConf['host'], 600):
        print('NIfi未启动')
        return False

    print('Template重新部署中...')
    # 初始化nifi，获得基础信息
    nifi = NifiApi(nifiConf['host'], nifiConf['username'], nifiConf['password'])
    groupInfo = nifi.getProcessGroups('root')
    uuid = groupInfo['processGroupFlow']['breadcrumb']['breadcrumb']['id']

    try:
        #遍历groups并依次停止删除groups
        for group in groupInfo['processGroupFlow']['flow']['processGroups']:
            nifi.updateProcessGroupState(group['status']['aggregateSnapshot']['id'], 'STOPPED')
            nifi.delProcessGroup(group['status']['aggregateSnapshot']['id'], group['revision']['version'])
    except:
        print('删除Groups异常')
        return False

    try:
        #获得所有模板，遍历并删除
        for template in nifi.getTemplates():
            nifi.deleteTemplates(template['id'])
    except:
        print('删除Templates异常')
        return False

    #遍历待上传的模板路径，上传模板
    for template in templates:
        if not nifi.uploadTemplate(template, uuid):
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
    #更新全部连接池控制器并启用
        for conServers in nifi.getAllConServices(uuid)['controllerServices']:
            if dbConf.has_key(conServers['component']['name']):
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
            nifi.updateConService(conserviceId=conServers['component']['id'],
                                 version=conServers['revision']['version'],
                                 state='ENABLED'
                                 )
    except:
        print('启用Controller Service异常')
        return False

    return True


if __name__ == '__main__':
    if reDeploymTemplate():
        print('Template重新部署成功')
    else:
        print('Template重新部署失败')