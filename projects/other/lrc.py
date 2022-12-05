# -*- coding: UTF-8 -*-

import os
import re
from collections import Counter
 

def find_chinese (file):
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    chinese_txt = re.sub(pattern,'',file)
    return chinese_txt


def find_chinese_two(file):
    pattern = re.compile(r'[^\x00-\x7f]')
    unchinese = re.sub(pattern,"",file)


list = []
with open("/Users/ming/damuDown/node_modules/huya-danmu/LRC_DIR/lrc/parse.LRC", 'rb') as f:   
    data = f.read().decode('utf-8', errors='ignore')
    # data = bytes.decode(data)
    # print(type(data))
    array = data.split('\n')
    # print(array)
    for x in array:
        x = x[12:]
        if "房管" in x:
            find_chinese(x)
            x = x.replace('/{zj', '').replace('[送花]', '').replace('/{fsj2','').replace('[偷笑]', '').replace('[大哭]', '').replace('[大笑]','').replace('[疑问]','').replace('[感动]','').replace('/{hj', '').replace('/{dhl','').replace('/{wg','').replace('\u3000','').replace(',','').replace('，','').replace('', '')
            list.append(x)
        # print(list)

# 计数
def list_counter(list):
    counter_list = dict(Counter(list))
    
    #只展示重复元素
    # print ([key for key,value in counter_list.items() if value > 1]) 
    
    #展现重复元素和重复次数
    origin_dict = {key:value for key,value in counter_list.items() if value > 1}
    order_dict = sorted(origin_dict.items(), key =lambda x:x[1], reverse=True) 
    for l in order_dict:
        print(l)
        
list_counter(list) 

# 去重1
def new_list_two(list):
    new_list = []
    # 列表生成去重失败
    # new_list = [x for x in list if x not in new_list]
    for i in list:
        if i not in new_list:
            print(i)
            new_list.append(i)
    # print(len(list), len(new_list), new_list)
    


# 去重2

def new_list(list):
    print(len(list))
    only_list = set(list)
    print(len(only_list))
    print('\r\n' + '**************************************' + '\r\n')
    for l in only_list:
        print(l)
        
