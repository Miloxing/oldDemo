import requests
from bs4 import BeautifulSoup

cookies = {
    '__u_a': 'v2.3.0',
    'time': 'ct=1650362184.658',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-RU,zh;q=0.9,en-RU;q=0.8,en;q=0.7,zh-CN;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'http://bbs.tianya.cn/post-funinfo-5390415-5.shtml',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
}

# response = requests.get('http://bbs.tianya.cn/post-funinfo-5390415-6.shtml', headers=headers, cookies=cookies, verify=False)

urls = [f"http://bbs.tianya.cn/post-funinfo-5390415-{i}.shtml" for i in range(1, 2)]



# print(*urls, sep='\n')
for url in urls:
    response = requests.get(url, headers=headers, cookies=cookies, verify=False)

    soup = BeautifulSoup(response.text, 'lxml')
    pageContent = soup.find('div', class_='atl-main')
    print(pageContent.text)
