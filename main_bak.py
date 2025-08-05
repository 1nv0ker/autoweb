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