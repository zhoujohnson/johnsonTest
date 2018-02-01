'''l = []
n=1 
while n<=99:
    l.append(n)
    n=n+2

print (l)

l=["Smith","Noah","China","johnson","Iris","Lucas"]

i = []
n = 4 
for t in range (4):
    i.append(l[t])
print (i)

i=l[:3]
print (i)
j = l[-2:]
print (j)'''

'''l = list(range(1,100))
a = l[22:88]
print (a)
b = l[:10:2]
print (b)
c = l[::5]
print (c)
d = l[:]
print (d)

a = "johnsonzhou"
b = a[:5]
print (b)
k = (1,2,3,4,5,6,7)
q = k[:3]
print (q)'''

'''d = {"a":1,"b":2,"c":3,"d":4}
for value in d.values():   #求值方法
    print (value)

from collections import Iterable
print(isinstance("abc",Iterable))
for i,value in enumerate(["A","B","C"]):
    #enumerate函数可以把一个list变成索引-元素对
    # ，这样就可以在for循环中同时迭代索引和元素本身：
    print (i,value)'''

a = list(range(1,11))
print (a)
b = []
for i in range(1,11):
    b.append(i*i)
print (b)

b = [x*x for x in range(1,11)]
print (b)
b = [x*x for x in range(1,11) if x % 2 !=0]
print (b)
c = [m+y for m in "abc" for y in "egf"]
print (c)
d = {"a":"d","b":"ds","c":"dd","d":"dss"}
a = [b+ "="+ c for b,c in d.items()]
print (a)
L = ['Hello', 'World', 18, 'Apple', None]
l2 = [s.lower() if isinstance(s, str) else s for s in L]
print (l2)