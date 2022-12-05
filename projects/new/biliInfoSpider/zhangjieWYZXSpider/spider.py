import requests
from time import sleep
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq


cookies = {
    'Hm_lvt_c37474bc3ea598fec912e4dbded5d6c2': '1656114786',
    'RSTestCookie': '1',
    'kvdkkecookieinforecord': '%2C21-447411%2C17-400745%2C16-407140%2C28-414607%2C28-424541%2C28-458038%2C',
    'Hm_lpvt_c37474bc3ea598fec912e4dbded5d6c2': '1656116633',
}

headers = {
    'Accept': 'text/html
,application/xhtml
+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-RU,zh;q=0.9,en-RU;q=0.8,en;q=0.7,zh-CN;q=0.6',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://www.wyzxwk.com/e/action/ListInfo.php?page=2&mid=9&line=15&tempid=27&ph=1&andor=and&author=%E5%BC%A0%E6%8D%B7&orderby=newstime&myorder=0&totalnum=160',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (Khtml
, like Gecko) Chrome/102.0.0.0 Safari/537.36',
}

# params = (
#     ('page', '3'),
#     ('mid', '9'),
#     ('line', '15'),
#     ('tempid', '27'),
#     ('ph', '1'),
#     ('andor', 'and'),
#     ('author', '\u5F20\u6377'),
#     ('orderby', 'newstime'),
#     ('myorder', '0'),
#     ('totalnum', '160'),
# )

# linkNums = list(range(11))
# Printing the list of numbers from 0 to 10.
# print(linkNums)

urls = [f"http://www.wyzxwk.com/e/action/ListInfo.php?page={i}&mid=9&line=15&tempid=27&ph=1&andor=and&author=%E5%BC%A0%E6%8D%B7&orderby=newstime&myorder=0&totalnum=160" for i in list(range(11))]

# response = requests.get('http://www.wyzxwk.com/e/action/ListInfo.php', headers=headers, params=params, cookies=cookies, verify=False)

# print(*urls, sep='\n')

downLinks = []

for url in urls:
    response = requests.get(url, headers=headers, cookies=cookies, verify=False)

    soup = BeautifulSoup(response.text, 'lxml')

    pageLinks = soup.select('.m-pt a')

    downLinks.extend(l.get('href') for l in pageLinks)
    
    print(f'scrawler {url} successfully downloaded')
    sleep(5)

with open('down.txt', 'a', encoding='utf-8') as f:
    f.write(''.join(downLinks) + '\n')

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('http://www.wyzxwk.com/e/action/ListInfo.php?page=3&mid=9&line=15&tempid=27&ph=1&andor=and&author=%E5%BC%A0%E6%8D%B7&orderby=newstime&myorder=0&totalnum=160', headers=headers, cookies=cookies, verify=False)
