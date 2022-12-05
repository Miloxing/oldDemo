#encoding=utf-8
import json

with open('水浒传第1集-电视剧 - 1.json', 'r', encoding='utf-8') as f:
    resList = str(f.readlines())
    # print(type(resList))
    downList= list(resList[2:-2])
    print(downList[100])
    # print(str(resList)[:500])
    # for l in resList[1:9]:
    #     print(l)
    #     # res = json.loads(l)
    #     # print(res['content'])
    
    # data = json.loads(f.readlines()[0])
    # # print(data)
    # print(data['content'])
    # print(data['ctime'] + '\n')
