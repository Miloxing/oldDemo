# coding=utf-8

from CrawDemo.util.util import *
from pyquery import PyQuery as pq


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


# 手动 headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}


# 读取文件链接
def readLink():
    with open(r"C:\Users\Miii\Desktop\CrawDemo\CrawDemo\down.txt", 'r') as f:
        urls = f.readlines()
        links = [url.strip() for url in urls]
    return links


# 保存 html 网页
def saveHtml(file_name, file_content):
    file_title = file_name
    character = '\/:*?"<>|'
    for s in character:
        if s in file_title:
            file_title = file_title.replace(s, '-')
        # print(html_title)
    with open(r'C:\Users\Miii\Desktop\CrawDemo\CrawDemo\xiami\{}.html'.format(file_title), "w", encoding='utf-8') as f:
        f.write(file_content)


def main():
    links = readLink()
    # links = ["https://wjinlei.github.io/posts/exp-ccna/"]

    # with open(r"C:\Users\Miii\Desktop\CrawDemo\CrawDemo\down2.txt", "a", encoding='utf-8') as f:
    # 保存解析后的文本
    # for url in links:
    #     r = requests.get(url, headers=headers)
    #     doc = pq(r.text)
    #     parseTitle = doc('title')
    #     parseContent = doc('#article-content')
    #     title = html2text.html2text(parseTitle.html())
    #     content = html2text.html2text(parseContent.html())
    #     f.write(title + "\r\n" + "**************************************************" + "\r\n")
    #     f.write(content)
    #     print("{}已经保存".format(title))
    #     time.sleep(2)

    # 保存 html 文件
    for url in links:
        r = requests.get(url, headers=headers)
        doc = pq(r.text)
        file_name = doc('title').text()
        saveHtml(file_name, r.text)
        print("{}已经保存".format(file_name))
        time.sleep(2)


if __name__ == '__main__':
    main()
