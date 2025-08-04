import requests
import json

url = "http://127.0.0.1:54345"
headers = {
    'Content-Type': 'application/json',
    'x-api-key':'f2a39b9ffc0d4d21a2b4f6a637e1e8ed'
}

def createBrowser():
    json_data = {
        'name': 'google',  # 窗口名称
        'remark': '',  # 备注
        'proxyMethod': 2,  # 代理方式 2自定义 3 提取IP
        # 代理类型  ['noproxy', 'http', 'https', 'socks5', 'ssh']
        'proxyType': 'noproxy',
        'host': '',  # 代理主机
        'port': '',  # 代理端口
        'proxyUserName': '',  # 代理账号
        "browserFingerPrint": {  # 指纹对象
            'coreVersion': '124'  # 内核版本，注意，win7/win8/winserver 2012 已经不支持112及以上内核了，无法打开
        }
    }

    res = requests.post(f"{url}/browser/update",
                        data=json.dumps(json_data), headers=headers).json()
    if res['success'] == True:
        browserId = res['data']['id']
        return browserId
    else:
        return ''

def openBrowser(id):
    json_data = {"id": f'{id}'}
    res = requests.post(f"{url}/browser/open",
                        data=json.dumps(json_data), headers=headers).json()
    # print(res)
    return res["data"]["driver"]