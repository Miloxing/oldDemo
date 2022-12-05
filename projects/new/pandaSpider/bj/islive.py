import requests
import json

headers = {
    'authority': 'www.winktv.co.kr',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-RU,zh;q=0.9,en-RU;q=0.8,en;q=0.7,zh-CN;q=0.6',
    'cache-control': 'no-cache',
    'cookie': 'adultPopupYN=Y; partner=winktv; mainEventLayerYN=Y; sessKey=90431bb23e9c79aa8b54b4a94dbed4824aa25688b3781ad5a1449346b03c3290; userLoginIdx=10045242; userLoginSaveID=WkdGamIyMXJZbXM9; userLoginSaveYN=N; userLoginYN=Y; 3be3f8e358abbf54cec643229de77fc9e4f3f0bbc9b171580d45d13aaa374c16=5MJLhn1IACCAL8ZDm2yTzDfWOuoZNWQvzIM8DrMg0K%2FgCJtTe6MCj2FxCYpzV7IJIv0onN7ZghuJuBVaOTQR7CgP%2FjzBb8TGP3KW5TT7qwNNnVTptEL97itfduUSOgUF97E2Zaoul%2F6Nq%2Fv1dBUTmEoxnxg8yZFqASRQRHCPVwZUFddShsk1aJL2qDL%2BLa%2FS',
    'pragma': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
}

data = {
  'action': 'watch',
#   'userIdx': '20091169',
  'password': '',
  'width': '48',
  'height': '48',
  'imageResize': 'crop',
  'fanIconWidth': '44',
  'fanIconHeight': '44',
  'fanIconImageResize': 'crop'
}

liveList = ['19645187', '19743076', '20091169' ,'20498122', '18567504', '17261053', '10529317', '20118491', '19955158', '18690900', '20118491', '19095629', '15979700', '14064292', '11051552']
banList = ['xltb7482', 'lovesther01', 'ladys77', 'becomegodjuliet', 'housegirl', 'sys27033', '5721004', 'lovejk8',  'jjuyeon2', 'april01', 'ayoung99', 'goldrain', 'joy0000', 'aooragi1', 'iusuzy']

for l in liveList:
    data['userIdx'] = l
    # print(data)
    response = requests.post('https://api.winktv.co.kr/v1/live/play', headers=headers, data=data)
    print(response.text)
    if islive := response.json()['result']:
        print(f'https://www.winktv.co.kr/live/play/{l}' + '\r\n')
