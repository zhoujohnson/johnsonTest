
'''from collections import Iterable
f=isinstance([],Iterable)
print (f)
f = isinstance({},Iterable)
print (f)
f = isinstance((),Iterable)
print (f)
f = isinstance(set(),Iterable)
print (f)
f = isinstance("ABC",Iterable)
print (f)
f = isinstance(234,Iterable)
print (f)
f = isinstance((x for x in range(5)),Iterable)
print (f)'''
it = iter([1,2,3,4,5,9,10])
# 循环
while True:
    try:
        # 获得下一个值
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就调出循环
        break
print (x)