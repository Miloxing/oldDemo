# coding=utf-8
import logging

import requests
import json
from bs4 import BeautifulSoup
from pyppeteer import launch
import asyncio
from pyquery import PyQuery as pq

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}


# zxf
async def parseWeekListen():
    print('\n' + '******** zzz的网易云 ********' + '\n')
    headers = {
        'authority': 'music.163.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98"',
        'content-type': 'application/x-www-form-urlencoded',
        'nm-gcore-status': '1',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56',
        'sec-ch-ua-platform': '"Windows"',
        'accept': '*/*',
        'origin': 'https://music.163.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://music.163.com/user/home?id=5171201758',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': '_iuqxldmzr_=32; _ntes_nuid=422e4d34cb83604d95eb1b793ec4e036; _ntes_nnid=422e4d34cb83604d95eb1b793ec4e036,1641474878753; NMTID=00OWCZTHwWYA8jsCU2UusDh4ODxBMAAAAF-L4bt_A; WEVNSM=1.0.0; WNMCID=gqfjym.1641474879319.01.0; WM_TID=DyQUsLPkWetAEEVQQUJvqUzqlW3uGNV0; timing_user_id=time_RN8k4wz3u9; NTES_P_UTID=P2fDFE5RWZMua0EbKsr5FswxvRVveFTp|1644573567; P_INFO=dadiaomin@126.com|1644573567|1|study|00&99|CN&1631596404&study#CN&null#10#0#0|&0||dadiaomin@126.com; ntes_kaola_ad=1; WM_NI=EGZ%2B%2BfN9NVsGiYmFx%2BSPY4Z1pAXogFunQipir%2BCpMEGrEYKTYxJ6%2FZYAW1fgSTWUDXM%2FoWpCJgaO4vaTDztnCG2Q6jY6tX2pQyxQhzIH%2F7Hhx2HiVDqUVN6UYwWVY5f6UzY%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee87ed4f8cb1aabbf254acac8ab2c44a968b8b85f821a9be84d0ce6292bcb989e52af0fea7c3b92a879996ccaa6e8ee782b7f24dab87a3a7fb21919097d5d93bb49f9890e64eb7b29f8af363b2f58d91d04f85ae8bbaca609ba886d7ae529b9f99d2e56d918c99b6c7548ff1a1b8f3498ab9afb0b77ea38c8c9bf7668199feb2b5629beabcb9b17c93a7b8b2eb728b98e1d8cb64bcee888ad550b38b9aafb55f9ba999b7dc3fa6ea9b9bdc37e2a3; JSESSIONID-WYYY=%5CxUGZ2E%2FkOKJy09HxXly%2FTjeC4sE%5C%2BoWvUtk62TNFeeaNa6rv9F499B1%5CDZdI5%5C5fTT0Asm%2F2qBQqK0DWWbRaJNzloBMTWvWo6t%2FwO8uq31mq7%2Bf5hlNZC41o3GPgCzgECpsMj7oF1kBv8CVSxnoS2MoC7w47ugQo7qslREp746S13SB%3A1645444624405',
        'dnt': '1',
        'sec-gpc': '1',
    }

    params = (
        ('csrf_token', ''),
    )

    data = {
        'params': 'yLBq95Kj7KcTGIqd7fJENU4rNghmBGu4cxCUFdUmwECCkmH/LOoIoe46pKkjSD4ovUXu90DpDv7wOv7dt2VYWRn2No4ll3st0VCOVnDItKxSPM+YnRaTfeG5lxSZEDkjamLAo5JWPuNecQJNNvHbz9tIHNot4KLkzh1XNIwbxnC918w2+IwBuOvDoy3xJARn',
        'encSecKey': 'b926e969b2c5efe4de105c270d91a2aa8da1aa1b9bbace43a8ca9b35962dc7c13612a8a17f97ca5b5db8b22a389e0a388cd67c27cfec7865a49c2a7fbe14d0d64fb37e33b46e69ec64ae8d82541a6fa440d624e95638328e426d4a8adca8be1b96f165c419fa388ccff792418390f0ddb1b8452bda710714c4e2ddce1335101a'
    }
    response = requests.post('https://music.163.com/weapi/v1/play/record', headers=headers, params=params, data=data)
    micList = json.loads(response.text)['weekData']
    nonList = []
    if micList != nonList:
        resultList = [micList[0]['song']]
        for i in resultList:
            print(i['name'], "https://music.163.com/#/song?id={}".format(i['id']) + '\r\n')
    else:
        print('没有查询到结果')


# zym

async def parseTrue():
    print('\n' + '******** yyy的网易云 ********' + '\n')
    headers = {
        'authority': 'music.163.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98"',
        'content-type': 'application/x-www-form-urlencoded',
        'nm-gcore-status': '1',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56',
        'sec-ch-ua-platform': '"Windows"',
        'accept': '*/*',
        'origin': 'https://music.163.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://music.163.com/user/songs/rank?id=3504124',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': '_iuqxldmzr_=32; _ntes_nuid=422e4d34cb83604d95eb1b793ec4e036; _ntes_nnid=422e4d34cb83604d95eb1b793ec4e036,1641474878753; NMTID=00OWCZTHwWYA8jsCU2UusDh4ODxBMAAAAF-L4bt_A; WEVNSM=1.0.0; WNMCID=gqfjym.1641474879319.01.0; WM_TID=DyQUsLPkWetAEEVQQUJvqUzqlW3uGNV0; timing_user_id=time_RN8k4wz3u9; NTES_P_UTID=P2fDFE5RWZMua0EbKsr5FswxvRVveFTp|1644573567; P_INFO=dadiaomin@126.com|1644573567|1|study|00&99|CN&1631596404&study#CN&null#10#0#0|&0||dadiaomin@126.com; ntes_kaola_ad=1; WM_NI=EGZ%2B%2BfN9NVsGiYmFx%2BSPY4Z1pAXogFunQipir%2BCpMEGrEYKTYxJ6%2FZYAW1fgSTWUDXM%2FoWpCJgaO4vaTDztnCG2Q6jY6tX2pQyxQhzIH%2F7Hhx2HiVDqUVN6UYwWVY5f6UzY%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee87ed4f8cb1aabbf254acac8ab2c44a968b8b85f821a9be84d0ce6292bcb989e52af0fea7c3b92a879996ccaa6e8ee782b7f24dab87a3a7fb21919097d5d93bb49f9890e64eb7b29f8af363b2f58d91d04f85ae8bbaca609ba886d7ae529b9f99d2e56d918c99b6c7548ff1a1b8f3498ab9afb0b77ea38c8c9bf7668199feb2b5629beabcb9b17c93a7b8b2eb728b98e1d8cb64bcee888ad550b38b9aafb55f9ba999b7dc3fa6ea9b9bdc37e2a3; JSESSIONID-WYYY=%5CxUGZ2E%2FkOKJy09HxXly%2FTjeC4sE%5C%2BoWvUtk62TNFeeaNa6rv9F499B1%5CDZdI5%5C5fTT0Asm%2F2qBQqK0DWWbRaJNzloBMTWvWo6t%2FwO8uq31mq7%2Bf5hlNZC41o3GPgCzgECpsMj7oF1kBv8CVSxnoS2MoC7w47ugQo7qslREp746S13SB%3A1645444624405',
        'dnt': '1',
        'sec-gpc': '1',
    }

    params = (
        ('csrf_token', ''),
    )

    data = {
        'params': 'KYEBpcUkF1EBqYoyCzFcp9mFwk7Z7dB+E5p/uUHj+fU0egt95P6VUPLImnaCTbwNivx52aIWEMpn42xm9PdQJtUxVRLbZMzvYhI76+KXcHnCDjphKL6QJ99QEUFJ03C+1tZlWRuQearYkwLa9tz9afhbeEWnFFDMyHO7JCoOImMsetZWUf2QchPtSjyZr3ug',
        'encSecKey': '7daf375b1a0b7f9e8c544c705e82bf5ee663102172e245a08dd78fd68341fa26a6636635e7bb848d0a1d4a11a4832301589518d52da1f935a6800f6155875aeea8849613985a0c4d9565eee2b0745e33ed6d969319c1984cb06ea0f72091b472243659b73b6b453417f1f137f46c7cf3010a77a393bdf9e726afaf484b0ac35b'
    }

    response = requests.post('https://music.163.com/weapi/v1/play/record', headers=headers, params=params, data=data)
    micList = json.loads(response.text)['weekData']
    nonList = []
    if micList != nonList:
        resultList = [micList[0]['song']]
        for i in resultList:
            print(i['name'], "https://music.163.com/#/song?id={}".format(i['id']) + '\r\n')
    else:
        print('没有查询到结果')


# isoft
async def parseIsoft():
    print('\n' + '******** 异次元软件 ********' + '\n')
    headers = {
        'authority': 'www.iplaysoft.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.iplaysoft.com/',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': 'comment_author_1a6752d3542a91d0ef18b67da891dabf=yukminney; comment_author_email_1a6752d3542a91d0ef18b67da891dabf=dadiaomin1991%40gmail.com; Hm_lvt_7ea7fde02e53834cf198b5ff640e0d18=1645329787,1645357487,1645440834,1645447956; Hm_lpvt_7ea7fde02e53834cf198b5ff640e0d18=1645447956',
        'dnt': '1',
        'sec-gpc': '1',
    }

    n = 1
    response = requests.get('https://www.iplaysoft.com/', headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    resultLinks = soup.select('.entry-banner')
    resulttitles = soup.select('.entry-head')
    for l, k in zip(resulttitles[:n], resultLinks[:n]):
        resultUrl = k.find('a')['href']
        resultName = l.find('a').getText()
        print(f'{resultName},  {resultUrl}')
    # resultUrl = resultLinks[0].find('a')['href']
    # resultName = resulttitles[0].find('a').getText()
    # print(f'{resultName},  {resultUrl}')


# zhangjie
async def parseZj():
    print('\n' + '******** 张捷财经观察 ********' + '\n')
    n = 1
    r = requests.get('https://api.bilibili.com/x/space/arc/search?mid=1955809864&ps=30&tid=0&pn=1', headers=headers)
    jsonText = json.loads(r.text)['data']['list']['vlist']
    for j in jsonText[:n]:
        print(j['title'], "https://www.bilibili.com/video/" + j['bvid'])


# acwifi
async def crawWifi():
    print('\n' + '******** 路由器评测 ********' + '\n')
    n = 1
    url = "https://www.acwifi.net/category/wifi"
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)
    await page.waitForSelector('.excerpt ')
    soup = BeautifulSoup(await page.content(), 'html.parser')
    # print(soup)
    resultLinks = soup.select('header h2 a')
    for l in resultLinks[0:n]:
        link = l.get('href')
        word = l.getText()
        print(f'{word} - {link}')
    await browser.close()

# ruanyifeng
async def ruanyifeng():
    print('\n' + '******** 阮一峰博客 ********' + '\n')
    n = 1
    url = "https://www.ruanyifeng.com/blog/archives.html"
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)
    # await page.waitForSelector('#homepage')
    soup = BeautifulSoup(await page.content(), 'html.parser')
    # soup = BeautifulSoup(response, 'lxml')
    links = soup.select('.module-content')[0].find_all('a')
    for link in links[:n]:
        print(f'{link.text} - {link.get("href")}')
    await browser.close()


# qignting
async def CrawQt():
    print('\n' + '******** 观棋有语 ********' + '\n')
    n = 1
    cookies = {
        'HWWAFSESID': '51ed9a3be338adda75',
        'HWWAFSESTIME': '1646552113744',
        'Hm_lvt_bbe853b61e20780bcb59a7ea2d051559': '1646458395,1646463004,1646552116',
        'Hm_lpvt_bbe853b61e20780bcb59a7ea2d051559': '1646552116',
    }

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.30',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Microsoft Edge";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    }

    response = requests.get('https://www.qingting.fm/channels/387255/', headers=headers, cookies=cookies)
    soup = BeautifulSoup(response.text, 'lxml')
    link = soup.select('.pTitle')
    title = soup.select('.pTitle p')
    for l, k in zip(link[0:n], title[0:n]):
        l = l.get('href')
        k = k.getText()
        print(f'{k} - https://www.qingting.fm{l}')


async def main():
    await parseWeekListen()
    await parseTrue()
    await parseIsoft()
    await parseZj()
    await CrawQt()
    await ruanyifeng()
    await crawWifi()


asyncio.get_event_loop().run_until_complete(main())
# def main():
#     # # zz的网易云
#     # print('\n' + '******** zzz的网易云 ********' + '\n')
#     # parseWeekListen()
#     #
#     # # z的网易云
#     # print('\n' + '******** yyy的网易云 ********' + '\n')
#     # parseTrue()
#     #
#     # # 异次元软件世界
#     # print('\n' + '******** 异次元软件世界 ********' + '\n')
#     # parseIsoft()
#     #
#     # # 张捷财经观察
#     # print('\n' + '******** 张捷财经观察 ********' + '\n')
#     # parseZj()
#     #
#     # # acwifi
#     # print('\n' + '******** 路由器评测 ********' + '\n')
#     # crawWifi()
#
#     # crawRuanyifeng
#     crawRuanyifeng()
#     # asyncio.get_event_loop().run_until_complete(crawRuanyifeng())
#
#
# if __name__ == '__main__':
#     main()
