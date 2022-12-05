# coding: utf-8
downLinks = []

with open('down.txt', 'r', encoding='utf-8') as f:
    downLinks.extend(f.readlines())

print([l.strip() for l in downLinks])
