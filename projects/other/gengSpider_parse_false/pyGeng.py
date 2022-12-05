import requests
from bs4 import BeautifulSoup
import string
from time import sleep

cookies = {
    'PHPSESSID': 'pnviv265gscub1h8kbe76469b2',
    'hd_sid': 'd7fbcQ',
    'Hm_lvt_369fd2cc978993a5cd323cb2bb490db3': '1652865978',
    'Hm_lpvt_369fd2cc978993a5cd323cb2bb490db3': '1652874896',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-RU,zh;q=0.9,en-RU;q=0.8,en;q=0.7,zh-CN;q=0.6',
    'Connection': 'keep-alive',
    'Referer': 'https://gengbaike.cn/list-letter-V.html',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


charList = list(string.ascii_uppercase)


def getPageList(char):
    url = f'https://gengbaike.cn/list-letter-{char}.html'

    response = requests.get(url, headers=headers, cookies=cookies)

    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        pageNum = int(soup.select('.a-c a')[-2].text)
        return [url] + [f'https://gengbaike.cn/list-letter-{char}-{i}.html' for i in range(2, pageNum + 1)]
    except Exception:
        return [url]

for i in charList[:1]:
    resLink = getPageList(i)
    for res in resLink:
        # print(res)
        response = requests.get(res, headers=headers, cookies=cookies)
        soup = BeautifulSoup(response.text, 'html.parser')

        contentLink = ['https://gengbaike.cn/' + i.get('href') for i in soup.select('.col-dl dd a')]

        ttContent = [i.text for i in soup.select('.col-dl dd')]

        resContent = []

        for l in contentLink:
            # print(l)
            response = requests.get(l, headers=headers, cookies=cookies)
            soup = BeautifulSoup(response.text, 'html.parser')

            content = soup.select('.content_1 .content_topp')[1].text

            resContent.append(content)
            sleep(3)

        for l , k in zip(ttContent, resContent):
            print(l, k)
