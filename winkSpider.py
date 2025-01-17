# coding:utf-8
import os
import random
import re
import shutil
import sys

import requests
import json
import time
from threading import Thread
from multiprocessing import Process  # , Pool, Manager, Value

import streamlink
from config import *

headers = header_to_json(header_raw)

data = {
    'offset': '0',
    'limit': '20',
    'isLive': 'Y',
    'width': '280',
    'height': '158',
    'imageResize': 'crop'
}
rstr = r"[\/\\\:\*\?\"\<\>\|\- \n]"
recording = []
proxies = {}  # {'https': '81.70.13.235:3247'}
trytimes = 1  # input('重试次数')
threads = 1  # input('线程数')
wait = 0  # False
# wait = Value('i', 0)
keep = []
# manager = Manager()
# keep = manager.list()
free_size = 0
# free_size = Value('f', 0)


def get_free_size():
    info = os.statvfs('/')
    free_size = round(info.f_bsize * info.f_bavail / 1024 / 1024 / 1024, 2)  # GB
    # free_size = Value('f', round(free_size, 2))
    return free_size


# response = requests.post('https://api.winktv.co.kr/v1/live/bookmark', headers=headers, data=data)

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
    try:
        response = requests.post(
            'https://api.winktv.co.kr/v1/live/bookmark', headers=headers, data=data, proxies=proxies)
    except Exception as e:
        print(e)
        return

    onLineBjs = json.loads(response.text)['list']
    users = []

    for l in onLineBjs:
        info = {
            'user_id': l['userId'],
            'user_nick': re.sub(rstr, "_", l['userNick']),
            'title': re.sub(rstr, "_", l['channelTitle']),
        }
        users.append(info)

    return users


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
        'https://api.winktv.co.kr/v1/live/bookmark', headers=headers, data=data)
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
def get_hls(uid):
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

    # specialFavList = ['lilac0510', 'apirl01', 'lovesther01', 'ladys77', 'xltb7482',
    #                   'double101', 'sigee111', 'tomato100', 'srkcom', 'jinricrew1', '5721004', 'lululemon026', 'luv333',
    #                   'bongbong486', 'o111na', 'becomegodjuliet']

    # for onlineId in onlineList:
    #     if onlineId in specialFavList:
    #         data['userId'] = onlineId
    #         # print(data)
    #
    #         response = requests.post(
    #             'https://api.winktv.co.kr/v1/live/play', headers=headers, data=data)
    #
    #         hlsList = json.loads(response.text)['PlayList']['hls3'][0]['url']
    #
    #         print(f"{onlineId} 在线，hls 源为 {hlsList}\r\n")
    #
    #         time.sleep(3)
    #         # print(f"{onlineId} 不在线\r\n")

    data['userId'] = uid

    while True:
        response = requests.post(
            'https://api.winktv.co.kr/v1/live/play', headers=headers, data=data, proxies=proxies)
        _data = response.json()
        isget = _data['result']
        if not isget:
            if 'needUnlimitItem' in response.text:
                sys.stdout.write(f'\r\033[K{uid}人数满，重试')
                time.sleep(0.5)
            elif 'needPw' in response.text:
                print(f'\r\033[K{uid}需要密码')
                break
            elif 'needCoin' in response.text:
                sys.stdout.write(f'\r\033[K{uid}需要硬币')
            elif 'castEnd' in response.text:
                sys.stdout.write(f'\r\033[K{uid}已结束直播')
                break
            else:
                print(_data)
                time.sleep(5)
            continue
        break
    hls = ''
    try:
        hls = _data['PlayList']['hls3'][0]['url']
    except AttributeError as e:
        print(uid, e)
    return hls


# 检查登录状态
def check_login():
    while True:
        try:
            response = requests.post(
                'https://api.winktv.co.kr/v1/member/login_info', headers=headers, proxies=proxies, timeout=5
            )
            return response.json()['loginInfo']['userInfo']['isLogin']
        except Exception as e:
            print(e)
        time.sleep(random.randint(5, 8))


def start_process(uid, nick, text):
    if uid not in recording:
        recording.append(uid)
        ##取消子进程
        # process = Process(target=start_record, args=(uid, nick, text), daemon=True)
        # process.start()
        # process.join()
        start_record(uid,nick,text)
        recording.remove(uid)


def start_record(user_id, user_nick, title):
    global wait
    try:
        hls = get_hls(user_id)
    except Exception as e:
        print(e)
        hls = ''
    if not hls:
        return
    session = streamlink.Streamlink()
    if threads:
        session.set_option('stream-segment-threads', int(threads))
    if trytimes:
        session.set_option('stream-segment-attempts', int(trytimes))
    session.set_option('hls-live-edge', 9999)
    try:
        streams = session.streams('hlsvariant://' + hls)
        stream = streams['best']
    except Exception as e:
        print(e)
        if 'streams' in locals():
            print(user_id, streams)
        return
    filename = f"{user_id}-{time.strftime('%y%m%d_%H%M%S')}-{user_nick}-{title}.ts"
    opath = "/root/b/d/kr"
    path = os.path.join(opath, user_id)
    try:
        fd = stream.open()
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            files = os.listdir(path)
            for file in files:
                fp = os.path.join(path, file)
                shutil.move(fp, opath)
        filepath = os.path.join(path, filename)
        try:
            f = open(filepath, 'wb')
        except:
            title = '_'
            filename = f"{user_id}-{time.strftime('%y%m%d_%H%M%S')}-{user_nick}-{title}.ts"
            filepath = os.path.join(path, filename)
            f = open(filepath, 'wb')
        readsize = 1024 * 8
        limitsize = 1024 * 1024 * 1024
        fs = 0
        print(f"\r\033[K{user_id} {user_nick} start recording")
        while 1:
            data = fd.read(readsize)
            if data and (not wait or user_id in keep):
                fs += f.write(data)
                if fs >= limitsize:
                    f.close()
                    shutil.move(filepath, opath)
                    filename = f"{user_id}-{time.strftime('%y%m%d_%H%M%S')}-{user_nick}-{title}.ts"
                    filepath = os.path.join(path, filename)
                    f = open(filepath, 'wb')
                    fs = 0
            else:
                break
    except Exception as e:
        print(f"\r\033[K{e}")
    finally:
        print(f"\r\033[K{user_id} {user_nick} recording end")
        if 'f' in locals():
            f.close()
            try:
                shutil.move(filepath, opath)
            except:
                pass
        if 'fd' in locals():
            fd.close()
        try:
            print(f"\r\033[K{user_id} {user_nick} recording end")
            files = os.listdir(path)
            if not files:
                os.rmdir(path)
        except:
            pass


def run():
    global free_size
    global keep
    global wait
    free_size = get_free_size()
    keep = get_keep_list()
    # if free_size.value <= 30 or (wait.value and free_size.value <= 35):
    if free_size <= 10 or (wait and free_size <= 15):
        sys.stdout.write(f"\r\033[K剩余空间{free_size}G, 停止下载")
        wait = 1
    else:
        wait = 0


def get_keep_list():
    try:
        keeps = open('./keep.txt').read().splitlines()
        # for i in keeps:
        #     if i not in keep:
        #         keep.append(i)
        keep = keeps
    except Exception as e:
        print(e)
        pass  # keep = []
    return keep


if __name__ == '__main__':
    while True:
        run()
        is_login = check_login()
        print('当前登录状态: ', is_login)
        if is_login:
            onlineList = getOnlineRes()
            if onlineList:
                for online in onlineList:
                    user_id, user_nick, title = online['user_id'], online['user_nick'], online['title']
                    if user_id not in recording and (not wait or user_id in keep):
                        th = Thread(target=start_process, args=(user_id, user_nick, title,), name=user_id, daemon=True)
                        th.start()
            else:
                sys.stdout.write('\r\033[K没有在线关注')
            print("\r\033[K等待再次检测")
            print(time.strftime('%H:%M:%S', time.localtime(time.time())))
            print('\r\n' + '*' * 20 + '\033[F\033[F\033[F\033[F\033[F\r')
            time.sleep(30)
        else:
            print("登录状态失效，请更新")
            time.sleep(600)
