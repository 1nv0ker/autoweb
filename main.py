from DrissionPage import ChromiumOptions,Chromium
from plugins import generate_random_string
from webProxy import getProxy
import random
import time
domain = 'www.iploong.com'
target_url = 'https://www.iploong.com'
port = 9222
def main():
    progressProcess()
    
def acceptExtension(browser):
    #打开新标签页
    tab = browser.new_tab()
    popup_url = 'chrome-extension://hoklmmgfnpapgjgcpechhaamimifchmp/panel/panel.html?domain=www.iploong.com'
    tab.get(popup_url)
    tab.wait()
    dom = tab.eles('I Accept')
    try:
        dom[1].click()
    except:
        print('找不到插件里的I Accept按钮')

def pageFromBaidu(browser):
    tab = browser.new_tab()
    tab.get('https://www.baidu.com')
    tab.wait(random.uniform(1.0, 5.0))
    search_input = tab.ele('#kw')

    search_input.input('iploong.com')

    search_button = tab.ele('#su')

    search_button.click()
    time.sleep(2)
    try:
        content = tab.eles('@id=1')
        link = content[1].ele('tag:a')
        link.click()
    except:
        print('iploong在百度中未找到')
def progressProcess():
    filename = generate_random_string(8)
    filename = 'data3'
    co = ChromiumOptions().set_local_port(port).set_user_data_path('webData/'+filename)
    proxy = getProxy()
    # print(proxy)
    co.set_proxy('http://'+proxy)
    # co.add_extension('./proxy')
    # co.add_extension('./extension')
    browser = Chromium(co)

    #同意插件获取数据
    # acceptExtension(browser)

    #从百度进入网站
    pageFromBaidu(browser)
    # browser.wait(random.uniform(1.0, 5.0))
    
    

if __name__ == '__main__':
    main()