import random
import string

def generate_random_string(length: int) -> str:
    """
    生成指定长度的随机字母数字混合字符串
    
    参数:
        length: 生成的字符串长度
        
    返回:
        随机字母数字混合字符串
    """
    # 定义字符集：包含大小写字母和数字
    characters = string.ascii_letters + string.digits
    
    # 从字符集中随机选择字符，组成指定长度的字符串
    random_string = ''.join(random.choice(characters) for _ in range(length))
    
    return random_string

