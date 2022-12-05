# coding=utf-8

from util.util import *
import json


# 遍历（方便遍历网址）
def lst(ul, nm):
    noun_list = [ul.format(i) for i in range(1,nm)]
    return noun_list


# 拼接 （方便拼接网址）
def add(li, lis):
    add_list = [li + str(l) for l in lis]
    return add_list

# testUrl
bID = ''
biliApiUrl = f'https://api.bilibili.com/x/space/arc/search?mid={bID}&ps=30&tid=0&pn={}'

kbjApiUrl = 'https://bjapi.afreecatv.com/api/secretx/vods/all?page={}&per_page=60'

# 自动 headers
headers = get_headers()

# 手动 headers
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}


# 请求为动态网页 api
def parseJsonData(jsondata):
    jsontext = json.loads(jsondata)
    
    # kbjTest code
    # li = jsontext['data']
    # link_list = [l['title_no'] for l in li]
    # st = "https://vod.afreecatv.com/PLAYER/STATION/"
    
    # biliTest demo
    li = jsontext['data']['list']['vlist']
    link_list = [l['bvid'] for l in li]
    st = "https://www.bilibili.com/video/"
    
    parseList = add(st,link_list)   
    return parseList



def main():
    # req_list = lst(kbjApiUrl,8)
    req_list = lst(biliApiUrl,2)
    # print(req_list)
    for l in req_list:
        r = requests.get(l, headers=headers)
        down_list = parseJsonData(r.text)
        for link in down_list:
            print(link)
            # print('\r\n')
        time.sleep(3)


if __name__ == '__main__':
    main()



