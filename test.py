from fake_useragent import UserAgent
from user_agents import parse
from deviceFinger import getRandom
useragent = UserAgent().random
user_agent = parse(useragent)
getRandom()