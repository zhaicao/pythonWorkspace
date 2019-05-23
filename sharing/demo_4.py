
__author__='zhaicao '

import paramiko
import io
import os
import time
import math
import ruamel.yaml as yaml



def excuteCommand(command):
    '''
    执行命令
    :param command:
    :return: 返回结果(str)
    '''
    # 创建SSH对象
    ssh = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(hostname='10.202.228.31', port=22, username='maxnerva', password='maxnerva')
    # 执行命令
    stdin, stdout, stderr = ssh.exec_command(command)
    # 获取命令结果
    res, err = stdout.read(), stderr.read()
    result = res if res else err
    # 关闭连接
    ssh.close()
    return result.decode('utf-8')


def updateYml(source, node, content, ymlFile="docker-compose.yml"):
    '''
    更新yml中指定节点的内容
    :param source: 源yml内容
    :param node: 指定的节点(从根开始)
    :param content: 更新的内容
    :param ymlFile: yml文件
    :return: 返回修改后的yml字符串
    '''
    # 写入cat内容
    with io.open(ymlFile, 'w') as f:
        f.write(source)
    # 读取内容
    with io.open(ymlFile, 'r') as f:
        pre = yaml.load(f, Loader=yaml.RoundTripLoader)
        pre['services'][node] = content
    # 写入修改后内容
    with io.open(ymlFile, 'w') as f:
        yaml.dump(pre, f, default_flow_style=False, Dumper=yaml.RoundTripDumper)
    # 读取修改后内容
    with io.open(ymlFile, 'r') as f:
        resAfter = f.read()
    # 删除文件
    if (os.path.exists(ymlFile)):
        os.remove(ymlFile)
    return resAfter


if __name__ == "__main__":

    # ==================服务配置=====================
    # 文件路径
    service = "cmdb"
    content = {
        'image': '10.202.228.30:5000/maxnerva/cmdb:V1.2.6.4',
        'container_name': 'cmdb',
        'ports': ["8081:8081"],
        'environment': {
            'eurekaHost': '10.202.228.31',
            'serverHost': '10.202.228.31',
            'serverPort': '8081',
            'MIN_MEM': '1024M',
            'MAX_MEM': '1024M'
          },
        'depends_on': ['config'],
        'restart': 'always'
        }
    # ==================服务配置 over=====================

    pre = time.time()
    # 获取服务器上docker-compose.yml源内容
    res = excuteCommand('cat docker-compose/docker-compose.yml')
    # 对源yml内容进行更新
    resAfter = updateYml(res, service, content)
    # 将更新的内容写入新的yml中
    res = excuteCommand('cat > docker-compose/docker-compose.yml << EOF \n' +
                      resAfter +
                       '\nEOF')
    # 更新容器
    excuteCommand('docker-compose -f docker-compose/docker-compose.yml up -d')
    print('执行完成，耗时%s秒' % str(math.floor(time.time() - pre)))