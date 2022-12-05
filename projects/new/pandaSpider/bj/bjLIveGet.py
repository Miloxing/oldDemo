import requests
import json

headers = {
    'authority': 'api.winktv.co.kr',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-RU,zh;q=0.9,en-RU;q=0.8,en;q=0.7,zh-CN;q=0.6',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'partner=winktv; sessKey=90431bb23e9c79aa8b54b4a94dbed4824aa25688b3781ad5a1449346b03c3290; userLoginIdx=10045242;',
    'origin': 'https://www.winktv.co.kr',
    'referer': 'https://www.winktv.co.kr/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    'x-device-info': '{"t":"webPc","v":"1.0","ui":10045242}',
}

data = {
  'offset': '0',
  'limit': '30',
  'isLive': 'Y',
  'width': '280',
  'height': '158',
  'imageResize': 'crop'
}

response = requests.post('https://api.winktv.co.kr/v1/live/bookmark', headers=headers, data=data)

bjResult = json.loads(response.text)['list']

for l in bjResult:
    isLive = l['media']['isLive']
    userId = l['media']['userId']
    userIdx = "https://www.winktv.co.kr/live/play/" + str(l['media']['userIdx'])
    print(isLive, userId, userIdx)
