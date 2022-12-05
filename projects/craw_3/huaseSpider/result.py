# coding=utf-8
import re

result = []
with open(r'C:\Users\M\Desktop\huase\huase.txt', "r", encoding='utf-8') as f:
  result.extend(f.readlines())

# print(result[0].rsplit(' ')[-1])
result = [i.rsplit(' ')[-1] for i in result]
# print(len(result))
with open(r'C:\Users\M\Desktop\huase\down.txt', 'a', encoding='utf-8') as f:
  f.writelines((l for l in result))

# for i in result:
#   print(i)
# print(*result, sep = '\n')
# print(result, len(result))
