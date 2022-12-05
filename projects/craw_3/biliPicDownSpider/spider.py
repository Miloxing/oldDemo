import requests
import json, time, re

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
    'blackside_state': '0',
    'CURRENT_BLACKGAP': '0',
    'i-wanna-go-back': '-1',
    'b_ut': '5',
    'nostalgia_conf': '-1',
    'bp_article_offset_24881199': '646561804127830000',
    'LIVE_BUVID': 'AUTO9416494762768235',
    'CURRENT_FNVAL': '4048',
    'b_lsid': 'E2E1010C38_180220522B8',
    'PVID': '1',
    'innersign': '1',
    'bp_t_offset_24881199': '648553419272880130',
    'bp_video_offset_24881199': '648553419272880100',
}

headers = {
    'authority': 'api.bilibili.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-RU,zh;q=0.9,en-RU;q=0.8,en;q=0.7,zh-CN;q=0.6',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'buvid3=0ED77564-9EFA-47F0-695D-E24B002D220E85128infoc; _uuid=B10768DC1-449B-CD79-A649-311010AC56C54B81636infoc; buvid_fp=94ef16c344049a332785e5aa76628a40; buvid4=96A3D46A-FB97-5301-66E1-0081875F4B0586617-022040614-hsRhWxGcTqFye7Wz8MsmEQ%3D%3D; rpdid=|(YYR|l)J)R0J\'uYRmkk~))m; fingerprint=28d2c46b48fa7980a5dca7614d80fa9f; SESSDATA=f943b1ba%2C1664779900%2Ce56ca%2A41; bili_jct=19f021c0fa44b1805792af83c060ecec; DedeUserID=24881199; DedeUserID__ckMd5=109f2e111882ae9f; sid=jxcod4pb; blackside_state=0; CURRENT_BLACKGAP=0; i-wanna-go-back=-1; b_ut=5; nostalgia_conf=-1; bp_article_offset_24881199=646561804127830000; LIVE_BUVID=AUTO9416494762768235; CURRENT_FNVAL=4048; b_lsid=E2E1010C38_180220522B8; PVID=1; innersign=1; bp_t_offset_24881199=648553419272880130; bp_video_offset_24881199=648553419272880100',
    'origin': 'https://space.bilibili.com',
    'referer': 'https://space.bilibili.com/24881199/favlist',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
}

# params = {
#     'media_id': '82633499',
#     'pn': '10',
#     'ps': '20',
#     'keyword': '',
#     'order': 'mtime',
#     'type': '0',
#     'tid': '0',
#     'platform': 'web',
#     'jsonp': 'jsonp',
# }

# 20220414
urls = [f"""https://api.bilibili.com/x/v3/fav/resource/list?media_id=82633499&pn={str(n)}&ps=20&keyword=&order=mtime&type=0&tid=0&platform=web&jsonp=jsonp""" for n in range(1, 70)]

# 过滤除中英文及数字以外的其他字符
def filter_str(desstr, restr='_'):
    res = re.compile("[^\\u4e00-\\u9fa5^a-z^A-Z^0-9^.]")
    return res.sub(restr, desstr)

for l in urls:
    print(f"正在爬取 {l}")
    response = requests.get(l, headers=headers, cookies=cookies)

    # print(response.text)

    jsonResult = json.loads(response.text)

    # print(jsonResult["data"]["medias"][0])


    # print(*{r['cover'] : r["title"] for r in jsonResult["data"]["medias"]}.items(), sep="\n")
    picResult = {r['cover'] : r["title"] for r in jsonResult["data"]["medias"]}
    
    
    filePath = r"C:\Users\M\Desktop\pics"
    for k, v in picResult.items():
        picContent = requests.get(k, headers=headers, cookies=cookies).content
        picName = filePath + "\\" + filter_str(v) + ".jpg"
        
        try:
            with open (f"{picName}", "wb") as f:
                f.write(picContent)
            print(f"{picName} 下载成功")
            time.sleep(1)
        except:
            print(f"{picName} - {k} 写入失败")
            continue
    time.sleep(5)
