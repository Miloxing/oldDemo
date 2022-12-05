import requests
import json
import time
from biliUtil import headers


# 测试结果用
def testResponse(url):
    response = requests.get(url, headers=headers)
    jsonResult = response.text[41:-1]
    # print(len('jQuery172013836417122193168_1649395493305('))
    print(jsonResult)


# 解析函数
# def parseComment(txtName, pageNum):
#     NEXT = range(1, pageNum)
#     with open('{}.txt'.format(txtName), 'a', encoding='utf-8') as f:

#         for n in NEXT:
#             print('scraping page {}'.format(n))
#             params['next'] = str(n)


class Model(object):
    """
    打定类信息
    """

    def __repr__(self):
        name = self.__class__.__name__
        properties = ('{}=({})'.format(k, v) for k, v in self.__dict__.items())
        s = '\n<{} \n  {}>'.format(name, '\n  '.join(properties))
        return s


class Comment(Model):
    """
    存储评论信息
    """

    def __init__(self):
        self.name = ''
        self.comment = ''
        self.re_rep = ''


def cached_url(url):
    """
    请求网页，并将结果缓存
    """
    response = requests.get(url, headers=headers)
    jsonLspResult = response.text.split('(', 1)[1]
    jsonResult = jsonLspResult[:-1]
    # print(jsonResult)
    return jsonResult


def result_from_url(url):
    # 获取json数据
    jsonResult = cached_url(url)

    # 解析json数据
    replies = json.loads(jsonResult)['data']['replies']

    # 调用结果函数，从json数据中提取信息
    comments = [result_from_json(rep) for rep in replies]

    return comments


def result_from_json(rep):
    """
    构造结果函数
    """
    m = Comment()

    m.name = rep['member']['uname']
    m.comment = rep['content']['message']
    # m.re_rep = [l['content']['message'] for l in rep['replies']]

    if rep['replies']:
        for l in rep['replies']:
            m.re_rep = l['content']['message']
    else:
        m.re_rep = ''

    return m


def main():
    URL = 'https://api.bilibili.com/x/v2/reply/main?callback=jQuery1720036247953782141185_1649474920069&jsonp=jsonp&next={}&type=1&oid=595377300&mode=3&plat=1'
    NEXT = range(0, 3)
    for n in NEXT:
        if not n == 1:
            print('scraping page {}'.format(n))
            # testResponse(URL.format(n))
            comments = result_from_url(URL.format(n))
            print(*comments, sep='\n')
            print("\n" + "*" * 50 + "\n")
            time.sleep(3)
        else:
            continue


if __name__ == "__main__":
    main()
