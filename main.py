from DrissionPage import ChromiumOptions,Chromium
from plugins import generate_random_string
from webProxy import create_proxy_auth_extension
from webProcess import timePause, pageFromGoogle,randomMoveMouse
import shutil 
domain = 'www.iploong.com'
target_url = 'https://www.iploong.com'
step = 100
port = 9222
def main():
    for _ in range(100):
        progressProcess()
    
def acceptExtension(browser):
    #打开新标签页
    tab = browser.new_tab()
    popup_url = 'chrome-extension://hoklmmgfnpapgjgcpechhaamimifchmp/panel/panel.html?domain='+domain
    tab.get(popup_url)
    dom = tab.eles('I Accept')
    try:
        dom[1].click()
    except:
        print('找不到插件里的I Accept按钮')

def progressProcess():
    filename = generate_random_string(8)
    # filename = 'data2'
    co = ChromiumOptions().set_local_port(port).set_user_data_path('webData/'+filename)
    proxy_auth_plugin_path = create_proxy_auth_extension(
        plugin_path="./proxy",
    )
    # print(proxy)
    # co.set_proxy('http://'+proxy)
    co.add_extension(proxy_auth_plugin_path)
    timePause()
    co.add_extension('./extension')
    browser = Chromium(co)

    #同意插件获取数据
    
    timePause()
    #从百度进入网站
    # pageFromBaidu(tab)
    
    #从google进入网站
    # pageFromGoogle(browser)
    tab = browser.new_tab(target_url)
    # tab = browser.latest_tab
    timePause()
    acceptExtension(browser)
    timePause()
    randomMoveMouse(tab)
    
    timePause()
    # randomScroll(tab)
    browser.quit()

    # #删除浏览器配置数据
    shutil.rmtree('webData/'+filename)
    
    

if __name__ == '__main__':
    main()