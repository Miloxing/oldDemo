import jieba
file=open(r'C:\Users\M\Desktop\fangguan_res.txt',encoding="utf-8")
file_context=file.read()
words1=jieba.__lcut(file_context)#全模式
words2=jieba.__lcut_for_search(file_context)#搜索引擎模式
 
#统计词频
 
data1={}
for chara in words1:
    if len(chara)<4:
        continue
    if chara in data1:
        data1[chara]+=1
    else:
        data1[chara]=1
        
data1=sorted(data1.items(),key = lambda x:x[1],reverse = True) #排序

with open(r'C:\Users\M\Desktop\danmu_data_4.txt','w',encoding="utf-8") as f:
    # f.write('\n'.join(str(i)[2:].split("'")[0] for i in data1))
    i = 1
    for l in data1:
        if not i % 5 == 0:
            f.write(str(l))
            i += 1
        else:
            f.write(str(l) + '\n')
            i += 1
        
    # f.write('\n'.join(str(i) for i in data1))

 
data2={}
for chara in words2:
    if len(chara)<2:
        continue
    if chara in data2:
        data2[chara]+=1
    else:
        data2[chara]=1
        
data2=sorted(data2.items(),key = lambda x:x[1],reverse = True) #排序

# print(*data2,sep='\n')
