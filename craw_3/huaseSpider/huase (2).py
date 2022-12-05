import requests
from bs4 import BeautifulSoup
import time
import random

cookies = {
    'cPNj_2132_saltkey': 'xEia9z7G',
    'cPNj_2132_lastvisit': '1649049854',
    'cPNj_2132_sendmail': '1',
    'cPNj_2132_lastfp': '31b9dd6e2579614c0c94fdb1475e72fb',
    'cPNj_2132_st_t': '0%7C1649053460%7Ca37215d881a9e4b611e2300ab79d7f24',
    'cPNj_2132_atarget': '1',
    'cPNj_2132_forum_lastvisit': 'D_2_1649053460',
    'cPNj_2132_visitedfid': '2',
    'cPNj_2132_lastact': '1649053472%09forum.php%09viewthread',
    'cPNj_2132_viewid': 'tid_815546',
}

headers = {
    'authority': 'sehuatang.net',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://sehuatang.net/',
    'accept-language': 'zh-RU,zh;q=0.9,en-RU;q=0.8,en;q=0.7,zh-CN;q=0.6',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'cPNj_2132_saltkey=xEia9z7G; cPNj_2132_lastvisit=1649049854; cPNj_2132_sendmail=1; cPNj_2132_lastfp=31b9dd6e2579614c0c94fdb1475e72fb; cPNj_2132_st_t=0%7C1649053460%7Ca37215d881a9e4b611e2300ab79d7f24; cPNj_2132_atarget=1; cPNj_2132_forum_lastvisit=D_2_1649053460; cPNj_2132_visitedfid=2; cPNj_2132_lastact=1649053472%09forum.php%09viewthread; cPNj_2132_viewid=tid_815546',
}

urls = ["https://sehuatang.net/forum-2-{}.html".format(i) for i in range(265, 301)]

with open ("huase.txt", "a", encoding='utf-8') as f:


  for index,url in enumerate(urls):
    if index % 10 == 0 and index != 0:
      print('wait for 20 seconds')
      time.sleep(random.randrange(20, 25))
    else:
      print("scraping {} ", url)
      session = requests.Session()
      session.keep_alive = False
      response = session.get(url, headers=headers, cookies=cookies)

      soup = BeautifulSoup(response.text, 'lxml')
      links = soup.find_all('a', class_='s xst')
      for l in links:      
        f.writelines(l.text + ' https://sehuatang.net/' + l.get('href') + '\n')
      time.sleep(random.randrange(10, 15))

    # time.sleep(2)
