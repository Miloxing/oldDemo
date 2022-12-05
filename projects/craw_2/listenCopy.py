# coding=utf-8
import time

import pyperclip as pyperclip

originCode = ''
while True:
    # print('正在监听')
    data = pyperclip.paste()
    if str(data) == originCode:
        # time.sleep(2)
        continue
    else:
        with open(r'C:\Users\Miii\Desktop\CrawDemo\CrawDemo\downDics\down.txt', 'a', encoding='utf-8') as f:
            f.write(str(data) + "\n")
            print('写入完成 {}'.format(str(data)))
            originCode = str(data)
