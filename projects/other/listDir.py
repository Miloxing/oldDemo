import os
import datetime
import schedule, functools, time
import re


# 过滤除中英文及数字以外的其他字符
def filter_str(desstr, restr=''):
    res = re.compile("[^\\u4e00-\\u9fa5^a-z^A-Z^0-9^.]")
    return res.sub(restr, desstr)

url = r"C:\Users\M\Desktop\honglou"
dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


# 非for循环打印
# links = [f"{ua}" for ua in os.listdir(url)]
# resLinks = [filter_str(ua) for ua in links]
# print(*resLinks, sep='\n')

# def run_every(freq=1, time_unit='minute'):
#     '''定时任务装饰器'''

#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             try:
#                 run_task(func, freq, time_unit)
#             except:
#                 pass

#         return wrapper

#     return decorator


# writelines可以接迭代器
def get_dir():
    with open('listDir.txt', 'a') as f:
        f.writelines("******* " + dt + " *****************************\n")
        f.writelines(filter_str( f"{ua}") + "\n" for ua in os.listdir(url))
        

# # @run_every(1, 'second')
# # def test():
# #     print('test')


# test()
while True:
    if datetime.datetime.now().hour == 17:
        print("午时一到，开始执行任务!")
        get_dir()
        print('任务执行完毕!')
        time.sleep(3600)
        continue
    else:
        print('时机未到！')
        time.sleep(3600)
        continue
