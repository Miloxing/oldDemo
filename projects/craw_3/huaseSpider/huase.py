import requests
from bs4 import BeautifulSoup
import time
import random

# coding=utf-8
import time
import asyncio
from pyppeteer import launch

from pyquery import PyQuery as pq

urls = ["https://sehuatang.net/forum-2-{}.html".format(i) for i in range(800, 807)]


async def main():
    down_list = []
    browser = await launch(
        {'headless': False}
    )
    page = await browser.newPage()
    with open(r"C:\Users\M\Desktop\huase\huase-2.txt", 'a', encoding='utf-8') as f:
        for url in urls:
            print(url)
            await page.goto(url)
            # await page.waitForSelector('.xst')
            response = await page.content()
            soup = BeautifulSoup(response, 'lxml')
            links = soup.find_all('a', class_='s xst')
            for l in links: 
              f.writelines(l.text + ' https://sehuatang.net/' + l.get('href') + '\n')
            # print('Names:', names)
            # time.sleep(60)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())



# urls = ["https://sehuatang.net/forum-2-{}.html".format(i) for i in range(301, 800)]

# with open ("huase-2.txt", "a", encoding='utf-8') as f:


#   for index,url in enumerate(urls):
#     if index % 10 == 0 and index != 0:
#       print('wait for 20 seconds')
#       time.sleep(random.randrange(5, 10))
#       session = requests.Session()
#       session.keep_alive = False
#       response = session.get(url, headers=headers, cookies=cookies)

#       soup = BeautifulSoup(response.text, 'lxml')
#       links = soup.find_all('a', class_='s xst')
#       for l in links:      
#         f.writelines(l.text + ' https://sehuatang.net/' + l.get('href') + '\n')
#     else:
#       print("scraping {} ", url)
#       session = requests.Session()
#       session.keep_alive = False
#       response = session.get(url, headers=headers, cookies=cookies)

#       soup = BeautifulSoup(response.text, 'lxml')
#       links = soup.find_all('a', class_='s xst')
#       for l in links:      
#         f.writelines(l.text + ' https://sehuatang.net/' + l.get('href') + '\n')
#       time.sleep(random.randrange(10, 15))

#     # time.sleep(2)
