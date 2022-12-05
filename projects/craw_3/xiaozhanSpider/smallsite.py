from pyppeteer import launch
from bs4 import BeautifulSoup
import asyncio
from urllib.parse import unquote
import time

list = []
with open(r'C:\Users\M\Desktop\alixiaozhan\down.txt', 'r') as f:
    list.extend(f.readlines())

# print(list)
resultList = [l.strip() for l in list]
# print(resultList)
async def ruanyifeng():
    # print('\n' + '******** 阮一峰博客 ********' + '\n')
    # n = 1
    # url = "https://xiaozhan.pan666.cn/%E5%BD%B1%E8%A7%86/%20[%E7%A5%9E%E5%81%B7%E5%86%9B%E5%9B%A2%202021]%E5%BE%B7%E5%9B%BD%20%20%E7%BE%8E%E5%9B%BD%20%20%E5%8A%A8%E4%BD%9C%20%20%E7%8A%AF%E7%BD%AA%20%20%E6%B4%BB%E6%AD%BB%E4%BA%BA%E5%86%9B%E5%9B%A2%E5%89%8D%E4%BC%A0%20%20%E8%A1%8C%E7%9B%97%E4%B9%8B%E5%B8%88%20.html"
    # browser = await launch()


    browser = await launch({
            'headless': False,
            'dumpio': True,
            'executablePath': r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
            "ignoreDefaultArgs": ['--enable-automation'],
            "userdataDir": r"C:\Users\M\Desktop\alixiaozhan\data",
            # 'args': [
            #     '--no-sandbox',
            #     '--load-extension={}'.format(chrome_extension),
            #     '--disable-extensions-except={}'.format(chrome_extension), ]
        })
    for url in resultList:
        print('fetch {}'.format(url))
        page = await browser.newPage()
        await page.goto(url)
        # await page.waitFor(10000)
        file_content = await page.content()

        file_name = unquote(url[27:-5].split("/")[1])
        character = '\/:*?"<>|'
        for s in character:
            if s in file_name:
                file_name = file_name.replace(s, 'Y')
        # print()
        with open(file_name + ".html", "wb") as f:
                #   写文件用bytes而不是str，所以要转码
            f.write(file_content.encode('utf-8'))
        await page.close()
        # time.sleep(2)
        # print(content)
        # soup = BeautifulSoup(await page.content(), 'html.parser')
        # # soup = BeautifulSoup(response, 'lxml')
        # links = soup.select('.module-content')[0].find_all('a')
        # for link in links[:n]:
        #     print(f'{link.text} - {link.get("href")}')
    await browser.close()


async def main():
    await ruanyifeng()

asyncio.get_event_loop().run_until_complete(main())