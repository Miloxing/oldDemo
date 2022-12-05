# coding=utf-8
# import contextlib
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
from http import cookies
import random, requests, time
from fake_useragent import UserAgent
from http.cookies import SimpleCookie
import json

# 自动 userAgent
ua = UserAgent()

with open(r'C:\Users\M\Desktop\projects\craw_2\util\mobile_user_agents.txt') as f:
    mobile_user_agents = [i.strip() for i in f.readlines()]


def get_ua(is_mobile=False):
    return random.choice(mobile_user_agents) if is_mobile else ua.random


def get_headers():
    return {
        "User-Agent": str(get_ua())
    }


# 自动代理
# proxy_pool
def get_proxy():
    pass


# 自动 cookies
def get_cookie():
    ck = SimpleCookie()
    with open("cookies.txt") as f:
        ck.load((f.read()))

    cookies = {}
    for key, morsel in ck.items():
        cookies[key] = morsel.value
    return cookies
