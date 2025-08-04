from DrissionPage import ChromiumOptions,Chromium
from bitApi import createBrowser,openBrowser

def main():
    co1 = ChromiumOptions().set_local_port(9222).set_user_data_path('data3')
    # co2 = ChromiumOptions().set_local_port(9333).set_user_data_path('data2')
    co1.add_extension('./extension')
    # co2.add_extension('./extension')
    browser1 = Chromium(co1)
    # browser2 = Chromium(co2)
    browser1.new_tab('https://iploong.com')
    # browser2.new_tab('https://iploong.com')
    # browserId = createBrowser()
    # driverPath = openBrowser(browserId)
    
    # co = ChromiumOptions().set_browser_path(driverPath)
    # 用该配置创建页面对象
    # browser = Chromium(addr_or_opts=co)

    # browser.new_tab('https://iploong.com')
    # tab.get('https://iploong.com')

main()