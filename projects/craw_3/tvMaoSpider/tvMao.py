# coding='utf-8'
import asyncio
from pyquery import PyQuery as pq
import requests
import json
from bs4 import BeautifulSoup
from pyppeteer import launch
import time

#
#

# headers = {
#     u'User-Agent': u'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
# #
PAGE = "Zy0qHDI"


async def crawTvmao(links):
    browser = await launch({
        # 'headless': False,
        # 'dumpio': True,
        'executablePath': r"C:\Users\Miii\AppData\Local\Google\Chrome\Application\chrome.exe",
    })
    # browser = await launch()
    page = await browser.newPage()
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36')
    for link in links:
        await page.goto(link)
        # await page.waitForSelector('.clear epi_c')
        soup = BeautifulSoup(await page.content(), 'lxml')
        article = soup.select('.clear .epi_c p')[0].get_text()
        print(article)
    # # soup = BeautifulSoup(response, 'lxml')
    # links = soup.select('.module-content')[0].find_all('a')
    # for link in links[:n]:
    #     print(f'{link.text} - {link.get("href")}')
    await browser.close()


#
# PAGE = "M2laVg"
#
#
async def getUrls():
    url = "https://www.tvmao.com/drama/{}=/episode".format(PAGE)
    browser = await launch({
        # 'headless': False,
        'executablePath': r"C:\Users\Miii\AppData\Local\Google\Chrome\Application\chrome.exe",
    })
    page = await browser.newPage()
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36')

    await page.goto(url)
    soup = BeautifulSoup(await page.content(), 'lxml')

    linkCount = soup.select('.epipage li a')
    resultLinks = ['https://www.tvmao.com' + link.get('href') for link in linkCount]
    await browser.close()
    return resultLinks


async def getDetail():
    url = "https://www.tvmao.com/drama/{}=".format(PAGE)
    browser = await launch({
        # 'headless': False,
        'executablePath': r"C:\Users\Miii\AppData\Local\Google\Chrome\Application\chrome.exe",
    })
    page = await browser.newPage()
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36')
    await page.goto(url)
    # await page.waitForSelector('.clear epi_c')
    soup = BeautifulSoup(await page.content(), 'lxml')

    vul = soup.select(".obj-info")[0].get_text()
    location = vul.split('|')[0]
    year = vul.split('|')[2]
    people = soup.select(".obj-actor-info")[0].get_text()
    director = people.split('|')[0]
    maker = people.split('|')[1]
    print(f'{location} {year} {director} {maker}')
    await browser.close()


async def getActor():
    url = "https://www.tvmao.com/drama/{}=/actors".format(PAGE)
    browser = await launch({
        # 'headless': False,
        'executablePath': r"C:\Users\Miii\AppData\Local\Google\Chrome\Application\chrome.exe",
    })
    page = await browser.newPage()
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36')
    await page.goto(url)
    # await page.waitForSelector('.clear epi_c')
    soup = BeautifulSoup(await page.content(), 'lxml')

    actors = soup.select('.ac_piclst img')
    actors = [actor.get('alt') for actor in actors]
    actorPics = soup.select('.ac_piclst img')
    actorPics = [pic.get('src') for pic in actorPics]
    for a, p in zip(actors, actorPics):
        print(f'{a} - {p}')
    await browser.close()


async def main():
    await getDetail()
    await getActor()
    urls = await getUrls()
    await crawTvmao(urls)


asyncio.get_event_loop().run_until_complete(main())

# MODEL
# browser = await launch({
#     # 'headless': False,
#     'executablePath': r"C:\Users\Miii\AppData\Local\Google\Chrome\Application\chrome.exe",
# })
# page = await browser.newPage()
# await page.setUserAgent(
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36')
#     await page.goto(link)
#     # await page.waitForSelector('.clear epi_c')
#     soup = BeautifulSoup(await page.content(), 'lxml')
#     await browser.close()
