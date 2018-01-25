'''list = [1,2,'Iris',4,'Johnson','周泽强']
it = iter(list)
for x in it:
    print (x,end='\t')'''

'''#encoding:utf-8
# filename:argv_test.py
import sys
# 获取脚本参数
print ('The name of this program is: %s'%(sys.argv[0]))
# 获取参数列表
print ('The command line arguments are:')
for i in sys.argv:
    print (i)
# 统计参数个数
print ('There are %s arguments.'%(len(sys.argv)-1))'''

#打开文件
'''fo = open("johnson.txt","wb")
print ("文件名：",fo.name)
#刷新文件
fo.flush()
#返回文件描述
fid = fo.fileno()
print ("文件描述：",fid)
#检查是否为终端设备，如果是返回 True，否则返回 False。 
ret = fo.isatty()
print ("返回值",ret)

# 在循环中，next()方法会在每次循环中调用，
# 该方法返回文件的下一行，如果到达结尾(EOF),则触发 StopIteration
#关闭文件
fo.close()'''
'''fo = open("johnson.txt","r")
print ("文件为：",fo.name)
for index in range(5):
    line = next(fo)
    print ("第%d行-%s"%(index,line))
fo.close()
'''
'''# read()方法用于从文件中读取指定的字节数
fo = open("johnson.txt","r+")
line = fo.read(14)
print ("这个有%s字节"%line)
fo.close()
'''
# readline()方法用于从文中读取整行
'''fo = open("johnson.txt","r+")
print ("文件名：",fo.name)
line = fo.readline()
print("这一行有：%s" %line)
line = fo.readline(3)
print("读取的字符串为：%s"%line)
fo.close()
'''
'''# readlines()方法用于读取所有行（直到遇到结束符EOF）并返回列表，
# 可用for...in...

##打开文件
fo = open("johnson.txt","r+")
print ("文件名为：",fo.name)
for line in fo.readlines():
    line = line.strip()
    print ("读取的数据为：%s"%(line))
fo.close()'''
'''
# seek() 方法用于移动文件读取指针到指定位置。
# 打开文件
fo = open("johnson.txt","r+")
print("文件名为：",fo.name)
line = fo.readline()
print("读取的字符串为：%s"%(line))
fo.seek(2,0)
line = fo.readline()
print("读取的字符串为：%s"%(line))'''

'''# tell() 方法返回文件的当前位置，即文件指针当前位置。
fo = open("johnson.txt","r+")
print ("文件名为：",fo.name)
line = fo.readline()
# 获取当前位置
pos = fo.tell()
print("当前位置为：%d"%(pos))
fo.close()'''

#truncate() 方法用于从文件的首行首字符开始截断，截断文件为 
# size 个字符，无 size 表示从当前位置截断；截断之后 V 后面的
# 所有字符被删除，其中 Widnows 系统下的换行代表2个字符大小。 。
# 打开文件
'''fo = open("johnson.txt","r+")
print("文件名为：",fo.name)
line = fo.readline()
print("读取行：%s"%(line))
#截取文件
fo.truncate()
line = fo.readlines()
print("截取长度为：%s"%(line))
fo.close()'''

fo = open("johnson.txt","r+")
print("打开文件：",fo.name)
fo.truncate(19)
line = fo.read()
print("读取数据：%s"%(line))
fo.close()