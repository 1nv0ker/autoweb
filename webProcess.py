import random
import time

urls = ["baidu.com", "google.com", "bitip.com",
         "youtube.com", "twitch.tv", "discord.com"]
def timePause():
    time.sleep(random.uniform(2.0, 10.0))
def timeLongPause():
    time.sleep(random.uniform(60.0, 180.0))

def pageFromBaidu(tab):
    tab.get('https://www.baidu.com')
    # tab.wait(random.uniform(10.0,20.0))
    search_input = tab.ele('#kw')

    search_input.input('iploong.com')

    search_button = tab.ele('#su')

    search_button.click()
    # tab.wait(random.uniform(10.0,20.0))
    try:
        content = tab.eles('@id=1')
        link = content[1].ele('tag:a')
        link.click()
        # tab.wait(random.uniform(10.0,20.0))
    except:
        print('iploong在百度中未找到')

def pageFromGoogle(browser):
    tab = browser.new_tab()
    tab.get('https://google.com/')
    timeLongPause()
    search_box = tab.eles('@name=q')
    if len(search_box)>0:
        search_box[0].input('iploong.com')
    timePause()
    tab.actions.key_down('ENTER')
    timePause()
    try:
        links = tab.eles('@class=zReHs')
        if len(links)>0:
            links[0].click()
        timePause()
    except:
        print('iploong在谷歌中未找到')
#ip检测
def ipTest(browser):
    try:
        tab = browser.new_tab()
        tab.get("https://httpbin.org/ip")
        dom = tab.eles('tag:pre')
        if len(dom)>0:
            ipHtml = dom[0].inner_html
            print(ipHtml)
            timePause()
    except:
        print('iptest 超时')
    
    
    
#iploong.com用户模拟
def randomMoveMouse(tab):
    timeLongPause()
    menus = tab.eles('tag:a')
    for _ in range(5):
        if len(menus) == 0:
            tab.refresh()
            timeLongPause()
            menus = tab.eles('tag:a')
            # print('menus', menus)
        else:
            break
    offsetX = random.randint(5, 500)
    offsetY = random.randint(5, 500)
    tab.actions.move(offset_x=offsetX, offset_y=offsetY)
    timePause()
    scrollDis = random.randint(5, 800)
    tab.actions.scroll(delta_y=scrollDis)
    timePause()
    if len(menus) == 3:
        menus[1].click()
        timePause()
        menus = tab.eles('tag:a')
        menus[2].click()
        timePause()
    random.choice(urls)

#miyaip.com用户模拟
def webActions(tab):
    timeLongPause()
    # menus = tab.eles('@class=item')
    # if len(menus)>2:
    #     menus[0].click()
    #     timePause()
    #     menus[1].click()
    # timePause()
    #随机产生一个动作
    randomValue = random.choices([0,2])
    #随机移动鼠标
    for _ in range(randomValue+1):
        offsetX = random.randint(50, 1500)
        offsetY = random.randint(100, 800)
        tab.actions.move(offset_x=offsetX, offset_y=offsetY)
        timePause()

    if randomValue == 0:
        print('跳转到登陆页')
        login = tab.eles('@class=btn login')
        # print('login', login)
        if len(login)>0:
            timePause()
            login[0].click()
            timeLongPause()
            tab.back()
    elif randomValue==1:
        print('跳转到注册页')
        register = tab.eles('@class=btn signup')
        if len(register)>0:
            timePause()
            register[0].click()
            timeLongPause()
            tab.back()
    else:
        print('随机滚轮')
        scrollDis = random.randint(50, 3000)
        tab.actions.scroll(delta_y=scrollDis)
    timeLongPause()
    #随机访问网页的链接
    links = tab.eles("@class=link-list")
    if len(links)>0:
        #随机访问次数
        randomValue = random.choices([1,9])
        for _ in range(randomValue):
            child = random.choice(links[0].children())
            if child != None:
                child.click()
                timePause()
    

    
