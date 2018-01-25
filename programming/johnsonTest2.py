# 打开文件
fo = open("johnson.txt","r+")
print("文件名：",fo.name)
str ="9: johnson.txt.hhh"
# 加入到最后一行
fo.seek(0,2)
line = fo.write(str)
# 读取所有文件内容
fo.seek(0,0)
for index in range(5):
    line = next(fo)
    print ("第%d行-这是：%s"%(index,line))
fo.close()