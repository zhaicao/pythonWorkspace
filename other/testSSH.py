
__author__='zhaicao '

import paramiko

private_key = paramiko.RSAKey.from_private_key_file('/Users/Ricky/Downloads/id_rsa_root')

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='10.202.228.31', port=22, username='root', pkey=private_key)

# 执行命令
stdin, stdout, stderr = ssh.exec_command('ls')
# 获取命令结果
res, err = stdout.read(), stderr.read()
result = res if res else err

print(result.decode('utf-8'))

# 关闭连接
ssh.close()

