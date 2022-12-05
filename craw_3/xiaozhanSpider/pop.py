list = []
with open(r'C:\Users\M\Desktop\alixiaozhan\other.txt', 'r') as f:
    list.extend(f.readlines())

for l in list:
    if l.endswith('.html\n'):
        pass
    else:
        print(l)