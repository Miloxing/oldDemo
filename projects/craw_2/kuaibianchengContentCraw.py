# coding=utf-8
from CrawDemo.util.util import *
import requests
from bs4 import BeautifulSoup


# 遍历（方便遍历网址）
def lst(ul, nm):
    noun_list = [ul.format(i) for i in range(1, nm)]
    return noun_list


# 拼接 （方便拼接网址）
def add(li, lis):
    add_list = [li + str(l) for l in lis]
    return add_list


# 自动 headers
# headers = get_headers()

# data
# data = {'username':'asd',
#         'pwd':'123456$'}

# 手动 headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    "Cookie": "session=eyJfcGVybWFuZW50Ijp0cnVlLCJpZCI6IjM4NSJ9.Ygdd0g.eSE0RF0i6Sge7i2rznPIjvTxTmg"
}


# 请求
# 读取文件
def readLink():
    with open(r"C:\Users\Miii\Desktop\CrawDemo\CrawDemo\down.txt", 'r') as f:
        urls = f.readlines()
        links = [url.strip() for url in urls]
    return links


def main():
    links = readLink()
    # links = ['https://www.kuaibiancheng.com/topics/a844db3a-7d5a-4dcd-9ecc-b373413af665']
    with open(r"C:\Users\Miii\Desktop\CrawDemo\CrawDemo\面试.txt", "a", encoding='utf-8') as f:
        for url in links:
            r = requests.get(url, headers=headers)
            soup = BeautifulSoup(r.text, 'lxml')
            dic = soup.find("title")
            print("正在爬取{}".format(dic.text))
            f.write(dic.text + "\r\n")
            f.write("**************************************************" + "\r\n")
            lis = soup.select(".markdown-body")
            for l in lis:
                f.write(l.text)
            f.write('\r\n')
            time.sleep(3)


if __name__ == '__main__':
    main()
