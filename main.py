from DrissionPage import ChromiumOptions,Chromium
from plugins import generate_random_string
from webProxy import create_proxy_auth_extension
from webProcess import timePause,randomMoveMouse,timeLongPause,webActions,ipTest
import shutil 
from urllib.parse import parse_qs
import random
# domain = 'www.iploong.com'
domain = 'www.miyaip.com'
# target_url = 'https://www.iploong.com'
target_url = 'https://www.miyaip.com'
step = 200
port = 9221

def main():
    with open('sg.txt', 'a', encoding='utf-8') as f_append:
        for _ in range(step):
            sg_str = progressProcess()
            if sg_str != False:
                f_append.write(sg_str+'\n')
        f_append.close()
    
def acceptExtension(browser):
    #打开新标签页
    tab = browser.new_tab()
    popup_url = 'chrome-extension://hoklmmgfnpapgjgcpechhaamimifchmp/panel/panel.html?domain='+domain
    try:
        tab.listen.start('matomo.similarweb.io')
        tab.get(popup_url, timeout=timeLongPause())
    except:
        print('插件页面超时')
        return False
    dom = tab.eles('I Accept')
    try:
        if len(dom) == 2:
            dom[1].click()
        packet = tab.listen.wait(timeout=60)
        # print('packetstart', packet)
        #重试5次
        for _ in range(5):
            if packet == False:
                packet = refreshExtension(tab)
            else:
                break
        # print('packetend', packet)
        if packet == False:
            return packet
        url = packet.url
        print('url', url)
        parsed_params = parse_qs(url)
        dimension11_value = parsed_params.get('dimension11', [None])[0]
        print("dimension11的值是:", dimension11_value)
        return dimension11_value
    except:
        print('找不到插件里的I Accept按钮')
        return False

def refreshExtension(tab):
    tab.listen.start('matomo.similarweb.io')
    tab.refresh()
    packet = tab.listen.wait(timeout=60)
    return packet

def progressProcess():
    filename = generate_random_string(8)
    # filename = 'data2'
    #edge浏览器路劲
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    co = ChromiumOptions()
    co.set_browser_path(edge_path)
    co.incognito(True)
    co.set_local_port(port)
    co.set_user_data_path('webData/'+filename)
    proxy_auth_plugin_path = create_proxy_auth_extension(
        plugin_path="./proxy",
    )
    co.add_extension(proxy_auth_plugin_path)
    
    timePause()
    co.add_extension('./extension')
    browser = Chromium(co)
    # tab = browser.new_tab()
    ipTest(browser)
    # tab.get("https://httpbin.org/ip")
    # ipHtml = tab.ele('tag:pre').inner_html
    # print(ipHtml)
    #查看ip
    # browser.new_tab('https://iplocation.com')
    
    timePause()
    tab = browser.new_tab()
    try:
        tab.get(target_url, timeout=timeLongPause())
    except:
        print('target_url加载 失败')
    
    timeLongPause()
    #同意插件获取数据
    randomValue = random.choices([0,1])
    if randomValue == 0:
        dimension11_value = acceptExtension(browser)
    else:
        dimension11_value = False
    # timePause()
    #iploong模拟动作
    # randomMoveMouse(tab)
    #miyaip模拟动作
    webActions(tab)
    # timeLongPause()
    # randomScroll(tab)
    browser.quit()
    timePause()
    # #删除浏览器配置数据
    shutil.rmtree('webData/'+filename)

    return dimension11_value
    
    
if __name__ == '__main__':
    main()