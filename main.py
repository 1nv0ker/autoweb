from DrissionPage import ChromiumPage, ChromiumOptions, SessionPage,WebPage
from fake_useragent import UserAgent
from user_agents import parse
import random
import requests
import json
from deviceFinger import set_custom

headers = {'Content-Type': 'application/json'}
# browser = Chromium() 
# tab = browser.latest_tab
# tab.get('https://www.iploong.com')

# browser.get('chrome-extension://hoklmmgfnpapgjgcpechhaamimifchmp/panel/panel.html?domain=www.iploong.com')

def getRandom():
    userAgent = UserAgent().random
    user_agent = parse(userAgent)#随机useragent

    if user_agent.is_mobile:
        width = random.randint(320, 430)
        height = random.randint(568, 930)
        return {
            "userAgent":userAgent,
            "width":width,
            "height":height
        }
    elif user_agent.is_tablet:
        screens = [[834,1194],[820,1180],[810,1080],[1200, 1920], [1024,768]]
        screen = random.choice(screens)
        return {
            "userAgent":userAgent,
            "width":screen[0],
            "height":screen[1]
        }
    else:
        screens = [[1920,1080], [1024, 720],[2560,1440],[3840,2160]]
        screen = random.choice(screens)
        return {
            "userAgent":userAgent,
            "width":screen[0],
            "height":screen[1]
        }
def getProxy():
    proxystring = '''proxy.bitip.com:10001:1c7t3eykxutgrbitip_g-US_f-129029g9h9g1:127939ghg92g2f28
proxy.bitip.com:10003:1c7t3eykxutgrbitip_g-US_f-129029g9h9g1:127939ghg92g2f28
proxy.bitip.com:10004:1c7t3eykxutgrbitip_g-US_f-129029g9h9g1:127939ghg92g2f28
proxy.bitip.com:10004:1c7t3eykxutgrbitip_g-US_f-129029g9h9g1:127939ghg92g2f28
proxy.bitip.com:10004:1c7t3eykxutgrbitip_g-US_f-129029g9h9g1:127939ghg92g2f28
proxy.bitip.com:10004:1c7t3eykxutgrbitip_g-US_f-129029g9h9g1:127939ghg92g2f28
proxy.bitip.com:10004:1c7t3eykxutgrbitip_g-US_f-129029g9h9g1:127939ghg92g2f28
proxy.bitip.com:10002:1c7t3eykxutgrbitip_g-US_f-129029g9h9g1:127939ghg92g2f28
proxy.bitip.com:10002:1c7t3eykxutgrbitip_g-US_f-129029g9h9g1:127939ghg92g2f28
proxy.bitip.com:10004:1c7t3eykxutgrbitip_g-US_f-129029g9h9g1:127939ghg92g2f28'''
    proxytemp = proxystring.split('\n')
    proxies = []
    for item in proxytemp:
        data = item.split(':')
        proxies.append('https://'+data[2]+':'+data[3]+'@'+data[0]+':'+data[1])
    return proxies

def create_bit_browser():
    # browser_id = createBrowser()
    url = "http://127.0.0.1:54345/browser/open"
    headers = {'X-API-KEY': 'f2a39b9ffc0d4d21a2b4f6a637e1e8ed'}
    json_data = {'id': 'f657877d57e145d6b6408720adb2dfa6'}
    res = requests.post(url, json=json_data, headers=headers).json()
    print(res)
    return res['data']['driver']

def main():
    deviceinfo = getRandom()
    # proxies = getProxy()
    co = ChromiumOptions()
    # print(deviceinfo)
    # driverPath  = create_bit_browser()
    co.set_argument('--disable-blink-features=AutomationControlled')
    
    co.add_extension('./extension')
    # proxy = random.choice(proxies)
    # print(proxy)
    # co.set_proxy(proxy)
    
    page = ChromiumPage(co)
    # page.set.window.screen(1024)
    set_custom(page)
    # page.run_js('localStorage.clear()')
    # set_custom_useragent(page)

    page.get('https://www.iploong.com')


main()