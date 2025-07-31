from DrissionPage import Chromium

browser = Chromium() 

tab = browser.latest_tab
tab.get('https://www.iploong.com')