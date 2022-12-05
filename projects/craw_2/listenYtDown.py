import time

import expression as expression
import pyperclip as pyperclip
import yt_dlp

recent_data = ""
while True:
    data = pyperclip.paste()
    data = str(data)
    if (data == recent_data):
        print('文本相同, 3s后重新开始监听')
        time.sleep(3)
        continue
    else:
        print('文本不同, 尝试下载')
        if data.startswith("https://www.youtube.com"):

            print(data)
            #     @retry(stop_max_attempt_number=7)
            try:
                ydl_opts = {
                    "format": "bestvideo[height=1080]+bestaudio/bestvideo+bestaudio",
                    "merge_output_format": "mp4",
                    'nooverwrites': True,
                    'ignoreerrors': True,
                    "outtmpl": "/Users/minnie/Downloads/ytDown/%(title)s.%(ext)s",
                    "--no-playlist": True
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([data])
                    recent_data = data
                    continue
            except expression as identifier:
                pass
            # down(data)
            # recent_data = data
            # continue
        elif data.startswith("https://www.bilibili.com"):
            print(data)
            #     @retry(stop_max_attempt_number=7)
            try:
                ydl_opts = {
                    # "format": "bestvideo[height=1080]+bestaudio/bestvideo+bestaudio",
                    "merge_output_format": "mp4",
                    'nooverwrites': True,
                    'ignoreerrors': True,
                    "outtmpl": "/Users/minnie/Downloads/biliDown/%(title)s.mp4",
                    "--no-playlist": True,
                    "external_downloader": "aria2c"
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([data])
                    recent_data = data
                    continue
            except expression as identifier:
                pass
        else:
            print('文本非链接, 3s后重新开始监听')
            time.sleep(3)
            recent_data = data
            continue


# def onread():
#     data = pyperclip.paste()
#     while True:
#         with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([youtube_url])
#         continue

# onread()

# data = pyperclip.paste()
# url = 'https://www.youtube.com/watch?v=Flf_7bpuxJU&t=141s'

# while True:
#         data = pyperclip.paste()
#         data= str(data)
#         if (data.startswith("https")):
#                 # print(data)
#                 ydl_opts = {}
#                 with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#                         ydl.download([data])
#                         continue
#         else:
#                 print('no')
#                 continue
