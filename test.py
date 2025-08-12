from DrissionPage import ChromiumOptions,Chromium,ChromiumPage
from plugins import generate_random_string
from webProxy import create_proxy_auth_extension
from webProcess import timePause, pageFromGoogle,randomMoveMouse,timeLongPause
import shutil 
from urllib.parse import parse_qs
domain = 'www.iploong.com'
target_url = 'https://www.iploong.com'
step = 1
port = 9222

def main():
   for _ in range(step):
        progressProcess()
    
def acceptExtension(browser):
    #打开新标签页
    tab = browser.new_tab()
    popup_url = 'chrome-extension://hoklmmgfnpapgjgcpechhaamimifchmp/panel/panel.html?domain='+domain
    tab.listen.start('matomo.similarweb.io') 
    #matomo.similarweb.io
    tab.get(popup_url)
    
    dom = tab.eles('I Accept')
    print('dom', dom)
    # dom[1].click()
    # for packet in tab.listen.steps():
    #     url = packet.url
    #     print('url', url)
    #     parsed_params = parse_qs(url)
    #     dimension11_value = parsed_params.get('dimension11', [None])[0]
    #     print("dimension11的值是:", dimension11_value)
    #     return dimension11_value
    # try:
    #     # res = tab.listen.wait()
    #     123
    #     # tab.refresh()
    
    #     # print(res)
    # except:
    #     print('找不到插件里的I Accept按钮')
 
    

def progressProcess():
    filename = generate_random_string(8)
    # filename = 'data2'
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    co = ChromiumOptions()
    co.set_browser_path(edge_path)
    co.set_local_port(port)
    co.set_user_data_path('webData/'+filename)
    proxy_auth_plugin_path = create_proxy_auth_extension(
        plugin_path="./proxy",
    )
    # print(proxy)
    # co.set_proxy('http://'+proxy)
    # co.add_extension(proxy_auth_plugin_path)
    timePause()
    # co.add_extension('./extension')
    browser = Chromium(co)
    
    #查看ip
    # browser.new_tab('https://iplocation.com')
    #同意插件获取数据
    
    timePause()
    #从百度进入网站
    # pageFromBaidu(tab)
    
    #从google进入网站
    # pageFromGoogle(browser)
    tab = browser.new_tab()
    # tab.listen.steps()
    # tab.clear_cache(session_storage=True, local_storage=True, cache=True)
    tab.get(target_url)
    # tab.li
    
    # timePause()
   
    
    # tab = browser.latest_tab
    # sg_str = acceptExtension(browser)
    # print('acceptExtension')
    # timePause()
    randomMoveMouse(tab)
    timePause()

    # timeLongPause()
    # # randomScroll(tab)
    # browser.quit()

    # #删除浏览器配置数据
    # shutil.rmtree('webData/'+filename)
    # return sg_str

main()
    