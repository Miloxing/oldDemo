# coding:utf-8
import requests
from bs4 import BeautifulSoup
import time, random, json
from pyquery import PyQuery as pq

headers = {
    'authority': 'www.bilibili.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-RU,zh;q=0.9,en-RU;q=0.8,en;q=0.7,zh-CN;q=0.6',
    'cache-control': 'no-cache',
    '$cookie': 'buvid3=A94EEC9C-3A2C-1BF2-69E3-BBD12B6784CD99822infoc; i-wanna-go-back=-1; _uuid=5144C8B9-8211-A6C10-1673-6389A6D1B810300110infoc; buvid4=354578DC-86B0-C464-9545-016044BBAA6600474-022061315-hsRhWxGcTqFdRasngSrjvQ%3D%3D; fingerprint=afaa92a9b88c9484ad8a7090e38bc9de; buvid_fp_plain=undefined; DedeUserID=24881199; DedeUserID__ckMd5=109f2e111882ae9f; CURRENT_BLACKGAP=0; b_ut=5; buvid_fp=afaa92a9b88c9484ad8a7090e38bc9de; blackside_state=0; rpdid=|(YYR|l)l|m0J\'uYlluu)~um; nostalgia_conf=-1; hit-dyn-v2=1; LIVE_BUVID=AUTO3116552866324471; is-2022-channel=1; CURRENT_QUALITY=0; PVID=1; theme_style=light; SESSDATA=7a1dbfc7%2C1672070707%2C15cbf%2A61; bili_jct=2f5151f5ffdfdda22709be5a8f03a985; sid=6m09c8p3; bsource=search_baidu; innersign=1; CURRENT_FNVAL=4048; b_lsid=6278CE58_181B28F73B0; b_timer=%7B%22ffp%22%3A%7B%22444.41.fp.risk_A94EEC9C%22%3A%22181A5592326%22%2C%22333.1007.fp.risk_A94EEC9C%22%3A%22181B2563948%22%2C%22333.788.fp.risk_A94EEC9C%22%3A%22181B236F71A%22%2C%22333.999.fp.risk_A94EEC9C%22%3A%22181B03AD865%22%2C%22333.976.fp.risk_A94EEC9C%22%3A%22181B2922BDD%22%2C%22333.337.fp.risk_A94EEC9C%22%3A%22181B2564B3D%22%2C%22777.5.0.0.fp.risk_A94EEC9C%22%3A%22181AAA98B76%22%2C%22444.42.fp.risk_A94EEC9C%22%3A%22181AAF224B8%22%2C%22333.905.fp.risk_A94EEC9C%22%3A%22181AAF9EEDC%22%7D%7D; bp_video_offset_24881199=677400605704060900',
    'pragma': 'no-cache',
    'referer': 'https://www.bilibili.com/read/readlist/rl476106?spm_id_from=333.999.0.0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
}

params = (
    ('from', 'readlist'),
)

# urls = ['https://www.bilibili.com/read/cv14292068/']
urls = ['https://www.bilibili.com/read/cv13498920/?from=readlist', 'https://www.bilibili.com/read/cv13309667/?from=readlist', 'https://www.bilibili.com/read/cv13509990/?from=readlist', 'https://www.bilibili.com/read/cv13510344/?from=readlist', 'https://www.bilibili.com/read/cv13532966/?from=readlist', 'https://www.bilibili.com/read/cv13533577/?from=readlist', 'https://www.bilibili.com/read/cv13550417/?from=readlist', 'https://www.bilibili.com/read/cv13565220/?from=readlist', 'https://www.bilibili.com/read/cv13578002/?from=readlist', 'https://www.bilibili.com/read/cv13642296/?from=readlist', 'https://www.bilibili.com/read/cv13717467/?from=readlist', 'https://www.bilibili.com/read/cv13836981/?from=readlist', 'https://www.bilibili.com/read/cv14241601/?from=readlist', 'https://www.bilibili.com/read/cv14242085/?from=readlist', 'https://www.bilibili.com/read/cv14242301/?from=readlist', 'https://www.bilibili.com/read/cv14250169/?from=readlist', 'https://www.bilibili.com/read/cv14251193/?from=readlist', 'https://www.bilibili.com/read/cv14265393/?from=readlist', 'https://www.bilibili.com/read/cv14276664/?from=readlist', 'https://www.bilibili.com/read/cv14292068/?from=readlist', 'https://www.bilibili.com/read/cv14301995/?from=readlist', 'https://www.bilibili.com/read/cv14316628/?from=readlist', 'https://www.bilibili.com/read/cv14326585/?from=readlist', 'https://www.bilibili.com/read/cv14351322/?from=readlist', 'https://www.bilibili.com/read/cv14360185/?from=readlist', 'https://www.bilibili.com/read/cv14374904/?from=readlist', 'https://www.bilibili.com/read/cv14390522/?from=readlist', 'https://www.bilibili.com/read/cv14407459/?from=readlist', 'https://www.bilibili.com/read/cv14432759/?from=readlist', 'https://www.bilibili.com/read/cv14457670/?from=readlist', 'https://www.bilibili.com/read/cv14485172/?from=readlist', 'https://www.bilibili.com/read/cv14503976/?from=readlist', 'https://www.bilibili.com/read/cv14532861/?from=readlist', 'https://www.bilibili.com/read/cv14544514/?from=readlist', 'https://www.bilibili.com/read/cv14589966/?from=readlist', 'https://www.bilibili.com/read/cv14517149/?from=readlist', 'https://www.bilibili.com/read/cv14641176/?from=readlist', 'https://www.bilibili.com/read/cv14961752/?from=readlist', 'https://www.bilibili.com/read/cv14979093/?from=readlist', 'https://www.bilibili.com/read/cv14995698/?from=readlist', 'https://www.bilibili.com/read/cv15011897/?from=readlist', 'https://www.bilibili.com/read/cv15026893/?from=readlist']


def parseArticle(url):
    response = requests.get(url, headers=headers, params=params)

    #NB. Original query string below. It seems impossible to parse and
    #reproduce query strings 100% accurately so the one below is given
    #in case the reproduced version is not "correct".
    # response = requests.get('https://www.bilibili.com/read/cv14292068/?from=readlist', headers=headers)

    doc = pq(response.text)
    art = doc('.inner-title').text()
    cont = doc('.article-content').text()
    return art, cont

with open ('article.txt', 'a', encoding='utf-8') as f:
    print(len(urls))
    time.sleep(100)
    for url in urls:
        art, cont = parseArticle(url)
        f.writelines(f"# {art}")
        f.writelines('\n\n')
        f.writelines(cont)
        f.writelines('\n\n')
        print(f'write successfully {url}')
        time.sleep(5)


