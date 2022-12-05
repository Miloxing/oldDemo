import os
import re
import sys
 
 
path = r'C:\Users\M\Desktop\新建文件夹 (3)\新建文件夹\bgm\result'
fileList = os.listdir(path)                 # 待修改文件夹
print("修改前："+str(fileList))         # 输出文件夹中包含的文件
 
currentpath = os.getcwd()                   # 得到进程当前工作目录
os.chdir(path)                              # 将当前工作目录修改为待修改文件夹的位置
n = 1                                       # 名称变量
for fileName in fileList:                   # 遍历文件夹中所有文件
    pat=".+\.(mp3|m4a)"                # 匹配文件名正则表达式
    pattern = re.findall(pat,fileName)      # 进行匹配
    # os.rename(fileName,(str(n)+ "-" + fileName + '.'+pattern[0]))     #文件重新命名
    os.rename(fileName,(str(n)+ "-" + fileName))     #文件重新命名
    n += 1                                  # 改变编号，继续下一项
 
os.chdir(currentpath)                       # 改回程序运行前的工作目录
sys.stdin.flush()                           # 刷新
print("修改后："+str(os.listdir(path)))     #输出修改后文件夹中包含的文件
