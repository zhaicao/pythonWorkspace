
__author__='zhaicao '

import requests,json

def deleteImage(imageName, tag, registryUrl='10.202.228.30:5000'):
    '''
    删除Docker Registry中的镜像
    镜像名：如/maxnerva/alarm
    镜像的tag：如0.5
    '''
    headers = {"Accept": "application/vnd.docker.distribution.manifest.v2+json"}
    r = requests.get('http://'+ registryUrl +'/v2'+ imageName+ '/manifests/'+ tag, headers = headers)
    sha256Code= r.headers.get('Docker-Content-Digest')
    if sha256Code:
        result = requests.delete('http://'+ registryUrl +'/v2'+ imageName +'/manifests/'+sha256Code, headers = headers)
        if result.status_code == 202:
            print('删除成功')
        else:
            print('删除失败')
    else:
        print('找不到该镜像')

def getTagsByImage(imageName, registryUrl='10.202.228.30:5000'):
    headers = {"Accept": "application/vnd.docker.distribution.manifest.v2+json"}
    r = requests.get('http://' + registryUrl + '/v2' + imageName + '/tags/list', headers=headers)
    print(r.url)
    print(json.loads(r.text)['tags'])

if __name__ == "__main__":
    # 参数镜像名和tag
    deleteImage('/maxnerva/zookeeper', '1.0')
    #getTagsByImage('/maxnerva/alarm')