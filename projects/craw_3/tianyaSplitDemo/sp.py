# sourcery skip: avoid-builtin-shadow
list = [f'http://bbs.tianya.cn/post-funinfo-5390415-{l}.shtml' for l in range(1, 640)] 

n =5
m = 1
for i in range(0, len(list), n):
    # print(i)
    # print(list[i:i+n])
    with open(f'{m}.txt', 'w') as f:
        for j in list[i:i+n]:
            f.write(j + '\n')
    m += 1
