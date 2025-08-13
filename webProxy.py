import random
import os
import string
def getProxy():
    proxystring = '''proxy.bitip.com:10001:1b7g3stpcswvnbitip_g-DE_f-129029g9h9g1:127939ghg92g2f28'''
    proxytemp = proxystring.split('\n')
    proxy = random.choice(proxytemp)
    proxies = proxy.split(':')
    return {
        "host":proxies[0],
        "port":proxies[1],
        "username":proxies[2],
        "password":proxies[3]
    }

def create_proxy_auth_extension(scheme='http', plugin_path=None):
    proxies = getProxy()
    proxy_host = proxies["host"]
    proxy_port = proxies["port"]
    proxy_username = proxies["username"]
    proxy_password = proxies["password"]
    # 创建Chrome插件的manifest.json文件内容
    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 3,
        "name": "Proxy auth",
        "permissions": [
            "proxy",
            "webRequest",
            "webRequestAuthProvider"
        ],
        "host_permissions": ["<all_urls>"],
        "background": {
            "service_worker": "background.js"
        },
        "minimum_chrome_version":"88"
    }
    """

    # 创建Chrome插件的background.js文件内容
    background_js = string.Template(
        """
        var config = {
            mode: "fixed_servers",
            rules: {
                singleProxy: {
                    scheme: "${scheme}",
                    host: "${host}",
                    port: parseInt(${port})
                },
                bypassList: ["localhost", "127.0.0.1"]
            }
        };

        chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

        function callbackFn(details) {
            return {
                authCredentials: {
                    username: "${username}",
                    password: "${password}"
                }
            };
        }

        chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
        );
        """
    ).substitute(
        host=proxy_host,
        port=proxy_port,
        username=proxy_username,
        password=proxy_password,
        scheme=scheme,
    )

    # 创建插件目录并写入manifest.json和background.js文件
    os.makedirs(plugin_path, exist_ok=True)
    with open(os.path.join(plugin_path, "manifest.json"), "w+") as f:
        f.write(manifest_json)
    with open(os.path.join(plugin_path, "background.js"), "w+") as f:
        f.write(background_js)
    
    return os.path.join(plugin_path)