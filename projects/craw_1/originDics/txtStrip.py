# with open(r'C:\Users\Miii\Desktop\CrawDemo\CrawDemo\originDics\kuaibiancheng.txt', 'r', encoding='utf-8') as f:
#     for l in f.readlines():
#         l.strip("\r\n")
#
#

# def delblankline(infile, outfile):
#     infopen = open(infile, 'r', encoding="utf-8")
#     outfopen = open(outfile, 'w', encoding="utf-8")
#
#     lines = infopen.readlines()
#     for line in lines:
#         if line.split():
#             outfopen.writelines(line)
#         else:
#             outfopen.writelines("")
#
#     infopen.close()
#     outfopen.close()
#
#
# delblankline("sss.txt", "o.txt")