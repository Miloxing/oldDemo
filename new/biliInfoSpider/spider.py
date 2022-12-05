#coding='utf-8'

import requests
import time
import json
import csv
import random
import datetime

headers = {
    'authority': 'api.bilibili.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,zh-RU;q=0.8,en-RU;q=0.7,en;q=0.6',
    'cache-control': 'no-cache',
    '$cookie': 'buvid3=A125AAB5-AE50-9E16-CE12-41F667C6652841755infoc; b_nut=1669173741; i-wanna-go-back=-1; nostalgia_conf=-1; CURRENT_FNVAL=4048; rpdid=|(J~R~ku)JmR0J\'uYYmu~J)J~; fingerprint=ea52ad4a71ad72489841ac3ed1b28309; buvid_fp=A125AAB5-AE50-9E16-CE12-41F667C6652841755infoc; buvid_fp_plain=undefined; DedeUserID=24881199; DedeUserID__ckMd5=109f2e111882ae9f; hit-new-style-dyn=0; hit-dyn-v2=1; b_ut=5; LIVE_BUVID=AUTO4316694654335598; CURRENT_QUALITY=80; SESSDATA=6cf81a4d%2C1685587897%2C80172%2Ac2; bili_jct=95f85f0bfe0e2b1b668654a3b9425f38; bp_video_offset_24881199=735282088966619100; innersign=1; sid=8pefz20f',
    'origin': 'https://space.bilibili.com',
    'pragma': 'no-cache',
    'referer': 'https://space.bilibili.com/60509716/video?tid=0&page=1&keyword=&order=pubdate',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

params = (
    # 控制要下载的视频页面
    ('mid', '267776898'),
    ('ps', '30'),
    ('tid', '0'),
    ('pn', ''),
    ('keyword', ''),
    ('order', 'pubdate'),
    ('order_avoided', 'true'),
    ('w_rid', '8d37ebf9602f6e85256a5d199445776f'),
    ('wts', '1670042073'),
)

fileName = str(params[0][1])

def get_mid_list(newList):
    response = requests.get('https://api.bilibili.com/x/space/wbi/arc/search', headers=headers, params=newList)

    result = json.loads(response.text)
    rec = result['data']['list']['vlist']


    with open(f"{fileName}.csv","a",encoding="utf-8") as csvfile: 
        writer = csv.writer(csvfile)

        #先写入columns_name
        # writer.writerow(["play","comment","title","description","pic"])
        #写入多行用writerows
        # writer.writerows([[0,1,3],[1,2,3],[2,3,4]])
        for r in rec:
            currentTime = datetime.datetime.fromtimestamp(r['created'])
            bvTag = 'https://www.bilibili.com/video/' + r['bvid']
            resList=[r['play'],r['comment'],r['title'],currentTime,r['description'],bvTag,r['pic']]
            writer.writerow(resList)

def main():
    newList = [list(p) for p in params]

    # 控制页数
    pageNum = [str(i) for i in range(1,16)]

    for page in pageNum:
        newList[3][1] = page
        # print(newList)
        get_mid_list(newList)
        print(f"{page} is done")
        #控制休眠时间
        time.sleep(random.randint(1, 7))

if __name__ == "__main__":
    main()
