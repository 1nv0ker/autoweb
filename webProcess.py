import random
import time
def randomScroll(tab, steps=10):

    directions = ['up', 'down', 'left', 'right']
    for _ in range(steps):
        try:
            # 随机选择滚动方向
            direction = random.choice(directions)
            
            # 随机生成滚动距离(50-500像素)
            distance = random.randint(50, 500)
            
            # 随机生成等待时间(0.5-2秒)，模拟人类思考时间
            wait_time = random.uniform(0.5, 2)
            time.sleep(wait_time)
            
            # 执行滚动操作
            if direction == 'up':
                tab.scroll.up(distance)
            elif direction == 'down':
                tab.scroll.down(distance)
            elif direction == 'left':
                tab.scroll.left(distance)
            elif direction == 'right':
                tab.scroll.right(distance)
                
            print(f"滚动方向: {direction}, 距离: {distance}px, 等待时间: {wait_time:.2f}s")
            
        except Exception as e:
            print(f"滚动过程中发生错误: {e}")
            continue