# coding=utf-8

from util.util import *
import json
from bs4 import BeautifulSoup


# 遍历（方便遍历网址）
def lst(ul, nm):
    noun_list = [ul.format(i) for i in range(1, nm)]
    return noun_list


# 拼接 （方便拼接网址）
def add(li, lis):
    add_list = [li + str(l) for l in lis]
    return add_list


# testUrl
bID = '517625673'

# 自动 headers
headers = get_headers()


# 手动 headers
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}

# 获取总页数
def parsePn(url):
    r = requests.get(url, headers=headers)
    jsontext = json.loads(r.text)

    pn = jsontext['data']['video']
    pn = pn // 30 + 2
    # print(f'视频数量：{pn}')
    return pn


# 解析页面列表
def parseJsonData(jsondata):
    jsontext = json.loads(jsondata)

    # biliTest demo
    li = jsontext['data']['list']['vlist']
    link_list = [l['bvid'] for l in li]
    st = "https://www.bilibili.com/video/"

    parseList = add(st, link_list)
    return parseList


def main():
    # req_list = lst(kbjApiUrl,8)
    # req_list = lst(biliApiUrl, 2)
    testApiUrl = "https://s3.music.126.net/web/s/core_f0925e41d0679aa7e93fd3fd981d8b1e.js?f0925e41d0679aa7e93fd3fd981d8b1e"
    soU = requests.get(testApiUrl, headers=headers)
    print(soU.text)
    # 获取用户信息
    # pageUrl = f"https://space.bilibili.com/{bID}/video"
    # r = requests.get(pageUrl, headers=headers)
    # soup = BeautifulSoup(r.text, 'lxml')
    # pageTitle = (soup.title.string).split("的")[0]
    #
    # # 获取总页数
    # biliPnApiUrl = f'https://api.bilibili.com/x/space/navnum?mid={bID}'
    # pn = parsePn(biliPnApiUrl)
    # # print(f'总页数：{pn}')
    #
    # # 构建请求列表
    # pNlink = f'https://api.bilibili.com/x/space/arc/search?mid={bID}&ps=30&tid=0'
    # req_list = [pNlink + "&pn={}".format(i) for i in range(1, pn)]
    # # print(req_list)
    #
    # # 解析页面列表
    # with open(r'{}.txt'.format(pageTitle), 'a+', encoding='utf-8') as f:
    #     for l in req_list:
    #         r = requests.get(l, headers=headers)
    #         down_list = parseJsonData(r.text)
    #         for link in down_list:
    #             f.write(link + '\n')
    #     time.sleep(3)
    #

if __name__ == '__main__':
    main()
