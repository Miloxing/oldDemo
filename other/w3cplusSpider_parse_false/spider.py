import requests
from bs4 import BeautifulSoup
from pyppeteer import launch
from pyquery import PyQuery as pq
import asyncio
import time

# headers = {
#     'authority': 'www.w3cplus.com',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'accept-language': 'zh-RU,zh;q=0.9,en-RU;q=0.8,en;q=0.7,zh-CN;q=0.6',
#     'cache-control': 'no-cache',
#     'cookie': 'Hm_lvt_177319b798978621f83845b12c86fa29=1650084903,1650106062; has_js=1',
#     'pragma': 'no-cache',
#     'referer': 'https://www.w3cplus.com/blog/tags/686.html',
#     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
# }

# params = (
#     ('page', '8'),
# )



    
async def crawWifi():
    browser = await launch({
            'headless': False,
            'dumpio': True,
            'executablePath': r"C:\Users\M\AppData\Local\Google\Chrome\Application\chrome.exe",
            "ignoreDefaultArgs": ['--enable-automation'],
            "userdataDir": r"C:\Users\M\Desktop\w3c\data",
            # 'args': [
            #     '--no-sandbox',
            #     '--load-extension={}'.format(chrome_extension),
            #     '--disable-extensions-except={}'.format(chrome_extension), ]
        })
    urls = [f"https://www.w3cplus.com/blog/tags/686.html?page={i}" for i in range(60)]
    
    
    for url in urls:
        print(f'scraping {url}')
        page = await browser.newPage()
        await page.goto(url)
        await page.waitForSelector('.node-teaser')
        # print(await page.content())
        soup = BeautifulSoup(await page.content(), 'html.parser')
        # print(soup)
        resultTitles = soup.select('.node-teaser h1')
        resultLinks = soup.select('.node-teaser h1 a')
        pageTimes = soup.select('.node-teaser .submitted')
        pageClickNum = soup.select('.node-teaser .submitted')
        pageTags = soup.select(".tags .field-items")
        
        titles = [link.getText().strip() for link in resultTitles]
        links = ["https://www.w3cplus.com" + link.get('href') for link in resultLinks]
        upTimes = [l.getText()[29:39] for l in pageTimes]
        clickNum = [l.getText()[52:].strip() for l in pageClickNum]
        tags = [l.text for l in pageTags]
        
        # # print(*list(zip(titles, links, upTimes, clickNum)), sep='\n')
        resDict = list(zip(titles, links, upTimes, clickNum, tags))
        # # print(resDict)
        
        with open('w3cPlusFinal.txt', 'a', encoding='utf-8') as f:
            for res in resDict:
                f.write(str(res) + '\n')
        print(f'scraping {url} done')
        time.sleep(5)
        await page.close()
    await browser.close()
    
async def main():
    await crawWifi()



asyncio.get_event_loop().run_until_complete(main())

