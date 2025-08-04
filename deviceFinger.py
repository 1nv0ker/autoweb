from fake_useragent import UserAgent
from user_agents import parse
import random
vendors = [
    {
        "match":"Safari",
        "value":"Apple Computer, Inc."
    },
    {
        "match":"Chrome",
        "value":"Google Inc."
    }
]
def set_custom(page):
    deviceInfo = getRandom()
    print(deviceInfo, deviceInfo["width"])
    js = f"""
    const originalScreen = window.screen;
    Object.defineProperty(window, 'screen', {{
        get: function() {{
            return {{
                ...originalScreen,  // 继承原始属性
                width: {deviceInfo["width"]},    // 自定义宽度
                height: {deviceInfo["height"]},  // 自定义高度
                availWidth: {deviceInfo["width"]},
                availHeight: {deviceInfo["height"]},
            }};
        }}
    }});
    Object.defineProperty(navigator, 'userAgent', {{
        get: function() {{
            console.log('{deviceInfo["userAgent"]}')
            return '{deviceInfo["userAgent"]}';
        }}
    }});
    Object.defineProperty(navigator, 'vendor', {{
        get: function() {{
            return '{deviceInfo["vendor"]}';
        }}
    }});
    HTMLCanvasElement.prototype.toDataURL = function() {{
        return 'data:image/png;base64,test'; 
    }};
    """
    print(js)
    page.add_init_js(js)


def getRandom():
    userAgent = UserAgent().random
    user_agent = parse(userAgent)#随机useragent
    vendor = [s for s in vendors if s["match"] in userAgent]
    vendor = vendor[0]["value"] if len(vendor)>0 else ""
    print(vendor, userAgent)
    if user_agent.is_mobile:
        width = random.randint(320, 430)
        height = random.randint(568, 930)
        return {
            "userAgent":userAgent,
            "width":width,
            "height":height,
            "vendor":vendor
        }
    elif user_agent.is_tablet:
        screens = [[834,1194],[820,1180],[810,1080],[1200, 1920], [1024,768]]
        screen = random.choice(screens)
        return {
            "userAgent":userAgent,
            "width":screen[0],
            "height":screen[1],
            "vendor":vendor
        }
    else:
        screens = [[1920,1080], [1024, 720],[2560,1440],[3840,2160]]
        screen = random.choice(screens)
        return {
            "userAgent":userAgent,
            "width":screen[0],
            "height":screen[1],
            "vendor":vendor
        }