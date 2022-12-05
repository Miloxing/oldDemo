#coding='utf-8'
import json, time, re

import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-RU,zh;q=0.9,en-RU;q=0.8,en;q=0.7,zh-CN;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Origin': 'https://www.qingting.fm',
    'Pragma': 'no-cache',
    'Referer': 'https://www.qingting.fm/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = (
    ('user_id', 'null'),
)

response = requests.get('https://i.qingting.fm/capi/v3/channel/387255', headers=headers, params=params)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://i.qingting.fm/capi/v3/channel/387255?user_id=null', headers=headers)

vid = json.loads(response.text)['data']['v']

url = f"https://i.qingting.fm/capi/channel/387255/programs/{vid}?curpage=1&pagesize=30&order=asc"

resultJson = json.loads(requests.get(url, headers=headers).text)

print(*{"https://www.qingting.fm/channels/387255/programs/" + str(l['id']):l['title'] for l in resultJson['data']['programs']}.items(), sep='\n')
