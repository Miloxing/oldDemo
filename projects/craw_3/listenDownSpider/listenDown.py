import time
import os
# import expression as expression
import pyperclip as pyperclip
# import yt_dlp


def ytDown(data):
    val = os.system(
        "yt-dlp -ciw -f bestvideo[height=1080]+bestaudio/bestvideo+bestaudio --merge-output-format mp4 --no-playlist -o './%(title)s.%(ext)s' {}".format(
            data))


def biliDown(data):
    val = os.system("lux {}".format(data))


def pageDown(data):
    val = os.system(
        """single-file  --browser-executable-path "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" {}""".format(
            data))


parseData = {
    'https://www.youtube.com': ytDown,
    'https://www.bilibili.com': biliDown,
    'https://www.zhihu.com/question': pageDown
}


def parseDownData(data, parseData):
    for key in parseData:
        if data.startswith(key):
            try:
                print('down', data)
                parseData[key](data)
            except:
                print("down error", data)
                with open("./error.txt", "a", encoding='utf-8') as f:
                    f.write(data + "\n")
                continue
        else:
            print('No downLink Pass')
            time.sleep(3)
            continue


def main():
    recent_data = ""
    while True:
        data = pyperclip.paste()
        data = str(data)
        if data == recent_data:
            print('文本相同, 3s后重新开始监听')
            time.sleep(3)
            continue
        else:
            parseDownData(data, parseData)
            recent_data = data


if __name__ == '__main__':
    main()
