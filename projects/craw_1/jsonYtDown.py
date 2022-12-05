import time
import requests
import json

from CrawDemo.util.youtube_dl import down

API_URL = "https://liveapi.huya.com/moment/getMomentContent?&videoId={}"
# @retry(stop_max_attempt_number=7, wait_fixed=5000)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}



with open("/Users/ming/projects/huyaPyDwon/huya_longzhujieshuo.txt" , 'r') as f:
    list = f.readlines()
    # print(list)
    list = [i.strip()[24:33] for i in list]
    list = [API_URL.format(i) for i in list]
    for l in list:
        data = json.loads(requests.get(l, headers=headers).text)

        m3u8Link = data['data']['moment']['videoInfo']['definitions'][0]['m3u8']
        name  = data['data']['moment']['videoInfo']['videoTitle']

        down(m3u8Link,name)
        
        time.sleep(5)
    
