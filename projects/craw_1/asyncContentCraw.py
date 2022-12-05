# coding=utf-8
import time
import asyncio
from pyppeteer import launch

from pyquery import PyQuery as pq

urls = ["https://v.huya.com/u/146501201/video.html?sort=news&p={}".format(i) for i in range(1, 6)]


async def main():
    down_list = []
    browser = await launch()
    page = await browser.newPage()
    with open("/Users/ming/projects/huyaPyDwon/huya_longzhujieshuo.txt", 'a') as f:
        for url in urls:
            await page.goto(url)
            await page.waitForSelector('.content-list .statpid')
            doc = pq(await page.content())
            pink_link = "https://v.huya.com"
            names = [pink_link + item.attr('href') for item in doc('.content-list .statpid').items()]
            for name in names:
                f.write(name + '\n')

            # print('Names:', names)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
