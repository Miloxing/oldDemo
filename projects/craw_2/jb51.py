import requests
from bs4 import BeautifulSoup
import time

cookies = {
    'Hm_lvt_5cf7ffaf53f2ae2c09200905ee32a7d5': '1646284229,1646310968,1647670085',
    'ASPSESSIONIDCGQCQCBD': 'APCFNLKCMJILLDFNCDIHHELB',
    'Hm_lvt_b88cfc1ccab788f0903cac38c894caa3': '1646310968,1646712950,1647670085,1648285994',
    'ASPSESSIONIDAETARCBD': 'LPHKFADDLFFENDJLJNALJAGA',
    'ASPSESSIONIDAETDTBDA': 'FKBHGKMCHCGHOLNJBMPKHLJI',
    'ASPSESSIONIDCGQCQDDD': 'HFPCOBIDCHPHHKLCGOABOECD',
    'Hm_lpvt_b88cfc1ccab788f0903cac38c894caa3': '1648300720',
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Microsoft Edge";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.52',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://www.jb51.net/article/153287.htm',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'Hm_lvt_5cf7ffaf53f2ae2c09200905ee32a7d5=1646284229,1646310968,1647670085; ASPSESSIONIDCGQCQCBD=APCFNLKCMJILLDFNCDIHHELB; Hm_lvt_b88cfc1ccab788f0903cac38c894caa3=1646310968,1646712950,1647670085,1648285994; ASPSESSIONIDAETARCBD=LPHKFADDLFFENDJLJNALJAGA; ASPSESSIONIDAETDTBDA=FKBHGKMCHCGHOLNJBMPKHLJI; ASPSESSIONIDCGQCQDDD=HFPCOBIDCHPHHKLCGOABOECD; Hm_lpvt_b88cfc1ccab788f0903cac38c894caa3=1648300720',
}

urls = ["https://www.jb51.net/list/list_3_{}.htm".format(i) for i in range(1, 101)]

with open('jb51_js.txt', 'w') as f:
    for url in urls:
        print("正在爬取：{}".format(url))
        response = requests.get(url, headers=headers, cookies=cookies)
        soup = BeautifulSoup(response.text, 'lxml')
        links = soup.select('dt > a')
        results = ["https://www.jb51.net/" + link.get('href') for link in links]
        for result in results:
            f.writelines(result + '\n')
        # time.sleep(5)