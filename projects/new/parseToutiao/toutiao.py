import requests

cookies = {
    'tt_webid': '7110208013156517389',
    'WIN_WH': '1440_687',
    'PIXIEL_RATIO': '2',
    'FRM': 'new',
    'ttcid': '014da55983eb43eea00fc0a7621bc45c15',
    'tt_scid': 'LmvJzDJJZjLUSPsLwF.OBCT9C6e6xLNr4Uzj.rWtcYgO1AUcF9Q2-fugnKBvJHaBfd29',
    '_S_DPR': '2',
    '_S_IPAD': '0',
    '_S_UA': 'Mozilla%2F5.0%20(Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F103.0.0.0%20Safari%2F537.36',
    '_S_WIN_WH': '1280_579',
    'passport_csrf_token': 'c1a126a41a95416041d16df4a6e3c498',
    'passport_csrf_token_default': 'c1a126a41a95416041d16df4a6e3c498',
    'msToken': 'vcWPGrvEXpGmMjtjYPOJ-3d9CbW6F2qUjwxNK6T_llYrOjbG7BxRAaGriAMrz5EyoFSq4HeMlJnUBquZfLDUVdkup6l2tpqnAbLgSAB9-oA=',
    'x-jupiter-uuid': '16670966138104496',
    'W2atIF': '1',
    '_tea_utm_cache_1698': 'undefined',
    'gd_worker_v2_random_178365': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2Njc3MDE0MTcsImlhdCI6MTY2NzA5NjYxNywibWF0Y2giOnRydWUsIm5iZiI6MTY2NzA5NjYxNywicGVyY2VudCI6MC43MDAzNzEzMTU2MjMzOTZ9.Djd2m6ckjZIm64bZoblXwkHUk0W6bu-5LjyIq_rpSlQ',
    'ttwid': '1%7Ce03PVa6cOYE-Vj-1lLXBnd8Uuwp7skafAwm5qVUxkJ8%7C1667096617%7C8561cf621a460448c5d74d6f09e3cf93d538214fd2ca6b0ff27051bdb7518fda',
    'MONITOR_WEB_ID': '76504800-9109-4237-862b-5fd4345f7c79',
    'MONITOR_DEVICE_ID': '8393e36c-d311-41fc-9841-ee7ccbd416e5',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-RU;q=0.8,en-RU;q=0.7,en;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://m.toutiao.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    'authority': 'p3-sign.toutiaoimg.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'zh-CN,zh;q=0.9,zh-RU;q=0.8,en-RU;q=0.7,en;q=0.6',
    'cache-control': 'no-cache',
    'cookie': 'MONITOR_WEB_ID=76a1cdd3-45ab-46a8-aa78-80ae065275d9',
    'pragma': 'no-cache',
    'referer': 'https://m.toutiao.com/',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    'content-type': 'application/json',
    'origin': 'https://m.toutiao.com',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'access-control-request-headers': 'content-type',
    'access-control-request-method': 'GET',
    'Content-Type': 'application/json; charset=UTF-8',
    'Access-Control-Request-Headers': 'content-type',
    'Access-Control-Request-Method': 'POST',
    'Origin': 'https://m.toutiao.com',
}

params = (
    ('W2atIF', '1'),
)

data = []

response = requests.post('https://m.toutiao.com/', headers=headers, params=params, cookies=cookies, data=data)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://m.toutiao.com/?W2atIF=1', headers=headers, cookies=cookies, data=data)


print(response.text)
