
# ------ 根据图片url下载图片 ------
# folderPath 定义图片存放的目录 imgUrl 一个图片的链接地址 index 索引，表示第几个图片
def downloadImg(folderPath, imgUrl, index):
    # ------ 异常处理 ------
    try:
        imgContent = (urllib.request.urlopen(imgUrl)).read()
    except urllib.error.URLError as e:
        if printLogEnabled : print  ('【错误】当前图片无法下载')
        return False
    except urllib.error.HTTPError as e:
        if printLogEnabled : print  ('【错误】当前图片下载异常')
        return False
    else:
        imgeNameFromUrl = os.path.basename(imgUrl)
        if printLogEnabled : print ('正在下载第'+str(index+1)+'张图片，图片地址:'+str(imgUrl))
        # ------ IO处理 ------
        isExists=os.path.exists(folderPath)
        if not isExists:  # 目录不存在，则创建
             os.makedirs( folderPath )
             #print  ('创建目录')
        # 图片名命名规则，随机字符串
        imgName = imgeNameFromUrl
        if len(imgeNameFromUrl) < 8:
            imgName = random_str(4) + random_str(1,'123456789') + random_str(2,'0123456789')+"_" + imgeNameFromUrl
        filename= folderPath + "\\"+str(imgName)+".jpg"
        try:
             with  open(filename, 'wb') as f:
                 f.write(imgContent)  # 写入本地磁盘
             # if printLogEnabled : print ('下载完成第'+str(index+1)+'张图片')
        except :
            return False
        return True
