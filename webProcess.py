import random
import time

def timePause():
    time.sleep(random.uniform(2.0, 10.0))
def timeLongPause():
    time.sleep(random.uniform(10.0, 60.0))
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
    tab.get('https://www.google.com')

    timePause()
    search_box = tab.ele('@name=q')
    search_box.input('iploong.com')
    timePause()
    tab.actions.key_down('ENTER')
    timePause()
    try:
        links = tab.eles('@class=zReHs')
        links[0].click()
        timePause()
    except:
        print('iploong在谷歌中未找到')

def randomMoveMouse(tab):
    timeLongPause()
    offsetX = random.randint(5, 500)
    offsetY = random.randint(5, 500)
    tab.actions.move(offset_x=offsetX, offset_y=offsetY)
    timePause()
    scrollDis = random.randint(5, 800)
    tab.actions.scroll(delta_y=scrollDis)
    timePause()
    menus = tab.eles('tag:a')
    if len(menus) == 3:
        menus[1].click()
        timePause()
        menus = tab.eles('tag:a')
        menus[2].click()
        timePause()
    
