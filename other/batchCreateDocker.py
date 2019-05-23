
__author__='zhaicao '

import docker
import requests,json
import sys

# client = docker.DockerClient(base_url="tcp://10.202.228.32:2375")
#
# print(client.images.list())
#
# print(client.containers.list()[0].attrs.get('Name'))
#
# print(client.containers.list(all=True))

def runAgentContainer(hostName, zabbixServer='zabbix-server', remoteUrl= '10.202.228.30:2375'):
    '''
    新建zabbix-agent容器
    :param hostName: 容器名及ZBX_HOSTNAME
    :param port: 宿主机端口
    :param ZBX_SERVER_HOST: ZBX_SERVER_HOST
    :param remoteUrl: 远程docker守护进程地址
    :return: 返回container对象
    '''
    client = docker.DockerClient(base_url="tcp://" + remoteUrl)
    container = client.containers.run('zabbix/zabbix-agent:alpine-4.0.6',
                                      name=hostName,
                                      #links={zabbixServer:'zabbix-server'},
                                      #network='network_1',
                                      environment=["ZBX_HOSTNAME=" + hostName, "ZBX_SERVER_HOST=" + zabbixServer],
                                      detach=True)
    return container


def loginZabbix(username, pwd, registryUrl='10.202.228.30:8082'):
    '''
    登录zabbix，返回token
    :param username: 用户名
    :param pwd: 密码
    :param registryUrl: zabbix的URL
    :return: 返回登录的token
    '''
    postParam = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": username,
            "password": pwd
        },
        "id": 1
    }
    headers = {"Content-Type": "application/json"}
    r = requests.post('http://' + registryUrl + '/api_jsonrpc.php', data=json.dumps(postParam), headers=headers)
    return r.json().get('result')

def createZabbixHost(hostName, ip, token, port=10050, groupid='15', templateid='10001', registryUrl='10.202.228.30:8082'):
    '''
    新建zabbix主机
    :param hostName: 主机名
    :param ip: 主机IP
    :param port:  主机端口
    :param token:  登录Token
    :param groupid: 群组
    :param templateid: 模板
    :param registryUrl: zabbix的URL
    :return: 返回主机HostId
    '''
    postParam = {
       "jsonrpc": "2.0",
       "method": "host.create",
       "params": {
           "host": hostName,
           "interfaces": [
               {
                    "type": 1,
                    "main": 1,
                    "useip": 1,
                    "ip": ip,
                    "dns": "",
                    "port": port
                }
            ],
           "groups": [
                {
                    "groupid": groupid
                }
           ],
           "templates": [
                {
                    "templateid": templateid
                }
           ]
       },
       "auth": token,
       "id": 1
    }
    headers = {"Content-Type": "application/json"}
    r = requests.post('http://' + registryUrl + '/api_jsonrpc.php', data=json.dumps(postParam), headers=headers)
    return r.json()['result']['hostids'][0]



if __name__ == "__main__":
    # Docker 设置
    dockerHost = '10.202.228.32'
    defaultNetId = '552b2459ca58'
    customNetId = '85b83cb9395f'
    # ZabbixWeb访问的URL地址
    zabbixWebHost = '10.202.228.32:80'
    # ZabbixServer容器内的IP
    zabbixServerHost = '172.18.0.2'
    # Docker宿主机IP
    dockerHost = '10.202.228.32'
    # 基础设置
    baseName = 'zabbix-agent-32'
    startIp = '172.18.3.1'
    count = 100

    # ==========================
    ipList = startIp.split('.')
    _startIp = int(ipList[3])
    if _startIp + count > 255:
        print('超出地址范围')
        sys.exit(1)
    for i in range(_startIp, _startIp + count):
        ip = '%s.%s.%s.%s' % (ipList[0], ipList[1], ipList[2], i)
        hostName = baseName + '_%s.%s' % (ipList[2], i)
        print('正在创建%s容器' % ip)
        runAgentContainer(hostName, zabbixServer=zabbixServerHost, remoteUrl=dockerHost + ':2375')
        client = docker.DockerClient(base_url="tcp://" + dockerHost + ':2375')
        # 删除默认的网络
        client.networks.get(defaultNetId).disconnect(hostName)
        # 增加新自定义网络
        network = client.networks.get(customNetId)
        network.connect(hostName, ipv4_address= ip, links={'zabbix-server':'zabbix-server'})
        # 获取zabbix登录token
        zabbixToken = loginZabbix('Admin', 'zabbix', registryUrl = zabbixWebHost)
        # 新建主机
        hostId = createZabbixHost(hostName, ip, zabbixToken, registryUrl = zabbixWebHost)


