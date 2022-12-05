# coding=utf-8
import os
import time
import random
from func_timeout import func_set_timeout


# url = """single-file  --browser-executable-path "C:\Program Files\Google\Chrome\Application\chrome.exe"  --browser-cookies-file ./realpython.com_cookies.txt --browser-wait-until domcontentloaded --output-directory ./result --urls-file={}.txt"""
# osLink = """single-file  --browser-executable-path "C:\Program Files\Google\Chrome\Application\chrome.exe"  --browser-cookies-file "./realpython.com_cookies.txt" --browser-wait-delay 5000 --browser-wait-until domcontentloaded --output-directory "./result" --urls-file=".\{}.txt""""

osLink = """single-file  --browser-executable-path "C:\\Users\M\AppData\Local\Google\Chrome\Application\chrome.exe"   --browser-wait-until networkidle2 --output-directory "./result" --browser-headless false --urls-file {}.txt"""

# urls = list(range(1, 129))

# def get_proxy():
#     rv = list(r.hkeys('use_proxy'))
#     if rv:
#         return random.choice(rv)

# proxyNum = get_proxy()
# os.environ["HTTPS_PROXY"] = proxyNum

@func_set_timeout(60)
def craw(l):
    val = os.system(osLink.format(str(l)))


for l in range(20,129):
    # os.system(osLink.format(l))
    print("正在爬取", l)
    # print(osLink.format(l))
    # print('正在爬取 - {}'.format(l))
    try:
        craw(l)
        # continue
    except:
        print('error', l)
        continue
    
    # print(l, 'done sleep')
    time.sleep(random.randrange(5, 10))
