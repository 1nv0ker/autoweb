import random
import time

def pageFromBaidu(browser):
    tab = browser.new_tab()
    tab.get('https://www.baidu.com')
    tab.wait(random.uniform(10.0,20.0))
    search_input = tab.ele('#kw')

    search_input.input('iploong.com')

    search_button = tab.ele('#su')

    search_button.click()
    tab.wait(random.uniform(10.0,20.0))
    try:
        content = tab.eles('@id=1')
        link = content[1].ele('tag:a')
        link.click()
        tab.wait(random.uniform(10.0,20.0))
    except:
        print('iploong在百度中未找到')
    
    return tab

def pageFromGoogle(browser):
    tab = browser.new_tab()
    tab.get('https://www.google.com')
    time.sleep(2)
    search_box = tab.ele('@name=q')
    search_box.input('iploong.com')
    tab.actions.key_down('ENTER')
    time.sleep(5)
    try:
        links = tab.eles('@class=zReHs')
        links[0].click()
    except:
        print('iploong在谷歌中未找到')
    return tab

def randomScroll(tab, steps=10):

    directions = ['up', 'down', 'left', 'right']
    
