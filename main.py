from DrissionPage import ChromiumPage, ChromiumOptions, SessionPage,WebPage
from fake_useragent import UserAgent
from user_agents import parse
import random
import requests
import json

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
    proxies = getProxy()
    co = ChromiumOptions()
    print(deviceinfo)
    # driverPath  = create_bit_browser()
    co.set_argument('--disable-blink-features=AutomationControlled')
    # co.set_argument('--no-sandbox')
    # co.set_argument('--headless')
    co.set_user_agent(deviceinfo['userAgent'])
    # co.set_browser_path(driverPath)
    # co.set_argument('--disable-blink-features=AutomationControlled')
    # co.set_argument('--window-size', str(deviceinfo["width"])+','+str(deviceinfo["height"]))
    # co.add_extension('./extension')
    # proxy = random.choice(proxies)
    # print(proxy)
    # co.set_proxy(proxy)
    
    page = ChromiumPage(co)
    print(page.run_js('return [screen.width, screen.height]'))  # 输出：[1366, 768]
    # page.set.window_size(deviceinfo["width"], deviceinfo["height"])
    # page.set(deviceinfo.width, deviceinfo.height)
    # page.run_js('Object.defineProperty(navigator, "language", {value: "en-US"});')
    # page.run_js("""
    #     // 修改 Canvas 绘制行为，添加随机噪声
    #     const oldToDataURL = HTMLCanvasElement.prototype.toDataURL;
    #     HTMLCanvasElement.prototype.toDataURL = function() {
    #         const ctx = this.getContext('2d');
    #         ctx.fillStyle = 'rgba(128,128,128,0.5)';
    #         ctx.fillRect(0, 0, this.width, this.height); // 添加基础图形
    #         ctx.fillStyle = 'rgba(' + Math.random()*255 + ',' + Math.random()*255 + ',' + Math.random()*255 + ', 0.3)';
    #         ctx.fillText(Date.now().toString(), 10, 20); // 添加动态文本干扰
    #         return oldToDataURL.apply(this, arguments);
    #     };
    # """)
    # print(WebPage)
    
    # page = WebPage(chromium_options=co)
    page.get('https://www.iploong.com')
    # page.

main()