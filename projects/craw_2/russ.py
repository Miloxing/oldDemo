# coding=utf-8
import logging

import requests
import json
from bs4 import BeautifulSoup
from pyppeteer import launch
import asyncio
from pyquery import PyQuery as pq


# headers = {
#     u'User-Agent': u'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}


# # acwifi
async def crawSteam():
    chrome_extension = r'C:\Users\M\AppData\Local\Google\Chrome\User Data\Default\Extensions\lfhjgihpknekohffabeddfkmoiklonhm\0.1.0_0'
    url = "https://s1.byrutor.com/page/125"
    # url = "https://zhuanlan.zhihu.com/p/82245551"
    browser = await launch({
        'headless': False,
        # 'dumpio': True,
        'executablePath': r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        'args': [
            '--no-sandbox',
            '--load-extension={}'.format(chrome_extension),
            '--disable-extensions-except={}'.format(chrome_extension), ]
    })
    page = await browser.newPage()
    page.setDefaultNavigationTimeout(1200 * 1000)
    await page.goto(url)
    await page.waitForSelector('#dle-content')

    soup = BeautifulSoup(await page.content(), 'lxml')
    # print(soup)
    resultLinks = soup.select('.shortn-img a')
    # print(resultLinks[0].get('href'))
    resultRanks = soup.select('.short-item .meta')
    # print(resultRanks[1].get_text().split('\n')[2])
    for l, k in zip(resultLinks, resultRanks):
        l = l.get('href')
    k = k.get_text().split('\n')[2]
    print(f'{l} - {k}')
    await browser.close()


async def main():
    await crawSteam()


asyncio.get_event_loop().run_until_complete(main())

# headers = {
#     'authority': 's1.byrutor.com',
#     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-user': '?1',
#     'sec-fetch-dest': 'document',
#     'referer': 'https://s1.byrutor.com/page/9/',
#     'accept-language': 'zh-RU,zh;q=0.9',
#     'cookie': '__ddgid=MRvbIz9OZCLw1AgR; __ddgmark=ma0M5fBD77d1J3rV; __ddg5=HcuNQtbpvmbll61L; __ddg2=YPkO9PuoyLxnwa8B; __ddg1=iL0MCC49wgY0YHj8iAzF; PHPSESSID=74099c91d88a841d38163ec2754dd0e3',
# }
#
# # proxies = {
# #   "http": "127.0.0.1:8080",
# # }
# response = requests.get('https://s1.byrutor.com/page/12/', headers=headers, timeout=30)
# soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)
