# coding:utf-8
import requests
import json
import time

headers = {
    'authority': 'api.pandalive.co.kr',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,zh-RU;q=0.8,en-RU;q=0.7,en;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'userLoginSaveYN=Y; userLoginSaveID=WTJocWFERTVPVEU9; _gcl_au=1.1.894357695.1667040572; _ga=GA1.3.1009708996.1657246450; _ga_W91XDLC3YE=GS1.1.1667284058.21.1.1667284137.0.0.0; _ga_NGSHFJTQS1=GS1.1.1667284059.21.1.1667284137.0.0.0; partner=pandatv; sessKey=0be0c7cda5b3fe04b2140f771867075f6a0244dada73d6176d5b4d9a942169b4; userLoginYN=Y; userLoginIdx=1783371; 3be3f8e358abbf54cec643229de77fc9e4f3f0bbc9b171580d45d13aaa374c16=Y1NeO0USeqjGfGooBn%2BROiC0heNY9sZHrGkeLQ9qCS5nMCnGjhtKsFSOMsFw0rYRZt98927Bw3uSpj1DbafIGmQcDJw14shk6fQ0bih1J6gGgwEJeLpTHPFnUhv72VbeuE5gGwIak539vDXm2rFenGCu6DjdUI60%2BKrZMN4yzCYe6U9BHBDR5vNieNaHc4uv',
    'origin': 'https://www.pandalive.co.kr',
    'pragma': 'no-cache',
    'referer': 'https://www.pandalive.co.kr/',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'x-device-info': '{"t":"webPc","v":"1.0","ui":1783371}',
}

data = {
  'offset': '0',
  'limit': '20',
  'isLive': 'Y',
  'width': '280',
  'height': '158',
  'imageResize': 'crop'
}

# response = requests.post('https://api.pandalive.co.kr/v1/live/bookmark', headers=headers, data=data)

# 得到在线订阅
def getOnlineRes():

    data = {
        'offset': '0',
        'limit': '120',
        'isLive': 'Y',
        'width': '280',
        'height': '158',
        'imageResize': 'crop'
    }

    response = requests.post(
        'https://api.pandalive.co.kr/v1/live/bookmark', headers=headers, data=data)

    onLineBjs = json.loads(response.text)['list']

    return [l['userId'] for l in onLineBjs]


# 得到所有订阅
def getAllRes():
    data = {
        'offset': '0',
        'limit': '200',
        'isLive': '',
        'width': '280',
        'height': '158',
        'imageResize': 'crop'
    }

    response = requests.post(
        'https://api.pandalive.co.kr/v1/live/bookmark', headers=headers, data=data)
    allMarkRes = json.loads(response.text)['list']
    print(len([l['userId'] for l in allMarkRes]))
    # l['media']['isLive'] == 'true'

# getAllRes()


# favList = ['lilac0510', 'apirl01', 'lovesther01', 'ladys77', 'xltb7482',
#            'double101', 'sigee111', 'tomato100', 'srkcom', 'jinricrew1', '5721004', 'lululemon026', 'luv333', 'bongbong486']

# 得到特别订阅提醒 

# while True:
#     onlineIds = getOnlineRes()
#     if onlineIds:
#         favOnlineUps = [l for l in favList if l in onlineIds]
#         print(f'在线主播为{onlineIds}\r\n特别关注主播在线为{favOnlineUps}\r\n即将开始休眠!' )
#         # print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#         print(time.strftime('%H:%M:%S',time.localtime(time.time())))
#         print('\r\n' + '*'*20 + '\r\n')
#         time.sleep(3600)
#     else:
#         print('net error')
#         break

# 得到特别订阅 hls 源
def getHlsRes(onlineList):

    # onlineId = ''

    data = {
        'action': 'watch',
        # 'userId': onlineId,
        'password': '',
        'width': '48',
        'height': '48',
        'imageResize': 'crop',
        'fanIconWidth': '44',
        'fanIconHeight': '44',
        'fanIconImageResize': 'crop'
    }

    specialFavList = ['lilac0510', 'apirl01', 'lovesther01', 'ladys77', 'xltb7482',
           'double101', 'sigee111', 'tomato100', 'srkcom', 'jinricrew1', '5721004', 'lululemon026', 'luv333', 'bongbong486', 'o111na', 'becomegodjuliet']


    for onlineId in onlineList:
        if onlineId in specialFavList:
            data['userId'] = onlineId
            # print(data)

            response = requests.post(
                'https://api.pandalive.co.kr/v1/live/play', headers=headers, data=data)

            hlsList = json.loads(response.text)['PlayList']['hls3'][0]['url']

            print(f"{onlineId} 在线，hls 源为 {hlsList}\r\n")

            time.sleep(3)
            # print(f"{onlineId} 不在线\r\n")


while True:
    onlineList = getOnlineRes()
    if onlineList:
        getHlsRes(onlineList)
        print("等待再次检测")
        print(time.strftime('%H:%M:%S',time.localtime(time.time())))
        print('\r\n' + '*'*20 + '\r\n')
        time.sleep(30)
    else:
        break
