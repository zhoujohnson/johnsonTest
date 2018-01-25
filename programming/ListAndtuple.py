'''a = ord("A")
print(a)
a = ord("中")
print(a)
b = chr(666666)
print (b)
c = '中文'.encode('utf-8')
# e = '中文'.encode('ascii')  ascii长度不够
print(c)
classmates = ["johnson","周泽强","爸爸"]
print(classmates)
a=len(classmates)
print(a)
print(classmates[2])
classmates.append("老公") #增加到list后面
print(classmates)
classmates.insert(2,"Iris")   #增加到指定位置
print(classmates)
classmates.pop()      #删除最后一位
"老公"
print(classmates)
classmates.pop(0)      #删除任意一位
"johnson"
print(classmates)
classmates[0]="johnson=周泽强"    #修改任意一位
print(classmates)'''
t=(1,2,["a","b"])
t[2][0]="johnson"
t[2][1]="Iris"
print (t)