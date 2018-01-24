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
b1 = set ([1,2,3])
b2 =set ([3,4,5])
s =b1&b2
print (s) 
s =b1|b2
print (s) 


