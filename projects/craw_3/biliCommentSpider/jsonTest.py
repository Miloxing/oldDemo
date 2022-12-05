import requests

cookies = {
    'buvid3': '0ED77564-9EFA-47F0-695D-E24B002D220E85128infoc',
    '_uuid': 'B10768DC1-449B-CD79-A649-311010AC56C54B81636infoc',
    'buvid_fp': '94ef16c344049a332785e5aa76628a40',
    'buvid4': '96A3D46A-FB97-5301-66E1-0081875F4B0586617-022040614-hsRhWxGcTqFye7Wz8MsmEQ%3D%3D',
    'rpdid': '|(YYR|l)J)R0J\'uYRmkk~))m',
    'fingerprint': '28d2c46b48fa7980a5dca7614d80fa9f',
    'SESSDATA': 'f943b1ba%2C1664779900%2Ce56ca%2A41',
    'bili_jct': '19f021c0fa44b1805792af83c060ecec',
    'DedeUserID': '24881199',
    'DedeUserID__ckMd5': '109f2e111882ae9f',
    'sid': 'jxcod4pb',
    'CURRENT_BLACKGAP': '0',
    'blackside_state': '0',
    'i-wanna-go-back': '-1',
    'b_ut': '5',
    'nostalgia_conf': '-1',
    'CURRENT_FNVAL': '4048',
    'bp_t_offset_24881199': '646299630739390486',
    'innersign': '1',
    'bsource': 'share_source_copy_link',
    'b_lsid': 'F75B38E4_18008E941F4',
    'PVID': '6',
    'bp_video_offset_24881199': '646744112620372000',
}

headers = {
    'authority': 'api.bilibili.com',
    'accept': '*/*',
    'accept-language': 'zh-RU,zh;q=0.9,en-RU;q=0.8,en;q=0.7,zh-CN;q=0.6',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'buvid3=0ED77564-9EFA-47F0-695D-E24B002D220E85128infoc; _uuid=B10768DC1-449B-CD79-A649-311010AC56C54B81636infoc; buvid_fp=94ef16c344049a332785e5aa76628a40; buvid4=96A3D46A-FB97-5301-66E1-0081875F4B0586617-022040614-hsRhWxGcTqFye7Wz8MsmEQ%3D%3D; rpdid=|(YYR|l)J)R0J\'uYRmkk~))m; fingerprint=28d2c46b48fa7980a5dca7614d80fa9f; SESSDATA=f943b1ba%2C1664779900%2Ce56ca%2A41; bili_jct=19f021c0fa44b1805792af83c060ecec; DedeUserID=24881199; DedeUserID__ckMd5=109f2e111882ae9f; sid=jxcod4pb; CURRENT_BLACKGAP=0; blackside_state=0; i-wanna-go-back=-1; b_ut=5; nostalgia_conf=-1; CURRENT_FNVAL=4048; bp_t_offset_24881199=646299630739390486; innersign=1; bsource=share_source_copy_link; b_lsid=F75B38E4_18008E941F4; PVID=6; bp_video_offset_24881199=646744112620372000',
    'referer': 'https://www.bilibili.com/video/BV1Mq4y1a73f',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
}

params = {
    'callback': 'jQuery172031913138470130087_1649420334685',
    'jsonp': 'jsonp',
    'next': '0',
    'type': '1',
    'oid': '595377300',
    'mode': '3',
    'plat': '1',
    '_': '1649420344437',
}

response = requests.get('https://api.bilibili.com/x/v2/reply/main', headers=headers, params=params, cookies=cookies)

print(response.text.split('(', 1)[1][:-1])
