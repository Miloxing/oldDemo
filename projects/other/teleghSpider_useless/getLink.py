# import re 
  
# def Find(string): 
# 	# findall() 查找匹配正则表达式的字符串
# 	url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', string)
# 	return url 
  
  
# with open('./down.txt', 'r', encoding='utf-8') as f:
# 	for l in f.readlines():
# 		# print(l)
# 		if l.endswith(')\n'):
# 			print((l.rsplit('(')[-1])[:-2])

# coding=utf-8
import os
import time
import random
from func_timeout import func_set_timeout


# url = """single-file  --browser-executable-path "C:\Program Files\Google\Chrome\Application\chrome.exe"  --browser-cookies-file ./realpython.com_cookies.txt --browser-wait-until domcontentloaded --output-directory ./result --urls-file={}.txt"""
# osLink = """single-file  --browser-executable-path "C:\Program Files\Google\Chrome\Application\chrome.exe"  --browser-cookies-file "./realpython.com_cookies.txt" --browser-wait-delay 5000 --browser-wait-until domcontentloaded --output-directory "./result" --urls-file={}.txt"""

# osLink = """single-file  --browser-executable-path "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"   --browser-wait-until networkidle2 --output-directory "./result" --browser-headless false --urls-file={}"""


osLink = """single-file  --browser-executable-path "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"   --output-directory "./result"  {}"""

@func_set_timeout(60)
def craw(l):
    val = os.system(osLink.format(l))
    

with open('./down.txt', 'r', encoding='utf-8') as f:
    for l in f.readlines():
            # print(osLink.format(l))
        l = l.strip()
        print(f'正在爬取 - {l}')
        try:       
            craw(l)        
        except:
            print('error', l)
            continue
        




# for l in urls:
#     # os.system(osLink.format(l))
#     print("正在爬取", osLink.format(l))
#     # print(osLink.format(l))
#     # print('正在爬取 - {}'.format(l))
#     try:       
#         craw(l)        
#     except:
#         print('error', l)
#         continue
#     # print(l, 'done sleep')
#     # time.sleep(random.randrange(1, 10))

