d ={"johnson":175,"Iris":160,"周泽强":"帅气"}
s = d["johnson"]
print (s)
d["May"]=123
print (d)
if "May"in d:
    print (True)
else :
    print (False)
if d.get("李倩"):  #通过dict提供的get()方法，如果key不存在，
#可以返回None，或者自己指定的value
    print (123)
else:
    print (345)
a = [1,2,3]
#d[a]= "john"   # list是可变的，就不能作为key：

# set和dict类似，也是一组key的集合，但不存储value。没有重复的key
b1 = set ([1,2,3])
b2 =set ([3,4,5])
s =b1&b2
print (s) 
s =b1|b2
print (s) 

# 添加元素
s=set([1,2,4])
s.add(3)
print (s)
# 删除元素
s.remove(2)
print (s)
'''a = [1,2]
s.add(a)
print (s)'''#set 为不可变对象

# 可变对象和不可变对象区别
#exp1: 可变对象
s = ["b","c","a"]
s.sort()
print (s)

#不可变对象
c = "abc"
b =c.replace("a","A")
print (c)
print (b)
a = (1,2,3)
b = (1,[2,3])
c = {"a1":1,"b1":1}
c["a1"]=a
c["b1"]=b
print (c)
c2 = {(1,2,3):"中国",(1,[2,3]):"小日本"}
print (c2)