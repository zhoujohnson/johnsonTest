'''a=abs(-10)
print (a)
f = abs
print (f(-100))
x = -5
y = 6
f =abs
def add(x,y,f):
    
    return f(x)+f(y)
print (add(1,-3,abs))'''
'''def f(x):
    return x*x
r = map(f,[1,2,3,4,5,6])
a= list(r)
print (a)'''

'''from functools import reduce
def a(x,y):
    return x+y
print (reduce(a,[1,2,3,4,5,6,6,6]))'''

'''def odd(n):
    return n%2==1
a = list(filter(odd,[1,3,4,5,6,43,7,3,6,7,9]))
print (a)
b =sorted(a)
print (b)'''
'''def empty(a):
    return a and a.strip()
p=list(filter(empty,["fj","","  ","johnson","Iris"]))
print (p)'''
'''def add_f():
    n=1
    while True:
        n=n+2
        yield n
def not_di(n):
    return lambda x:x%n>0    #lambda匿名函数，起到简化函数的方式
def primes():
    yield 2
    it = add_f()#初始序列
    while True:
        n =next(it) #返回序列的第一个数
        yield n
        it = filter(not_di(n),it)#构造新序列
# 打印1000以内的素数
for n in primes():
    if n<1000:
        print (n)
    else:
        break'''

'''a = [1,3,4,1,5,-3,12,-43,1,33]
print (sorted(a,key=abs))
b = ["jjj","Jodf","周泽强","tdsa","Tsfdk"]
print (sorted(b))
print (sorted(b,key=str.lower))
print (sorted(a,key=abs,reverse=True))'''

# 返回函数
'''def calc_sum(*args):
    ax = 0
    for n in args:
        ax =ax +n
    retun ax'''
'''def count():
    fa = []
    for i in range(1,4):
        def f():
            return i*i
        fa.append(f)
    return fa
f1=count()'''

'''def count():
    def f(j):
        def g():
            return j*j
        return g
    fs =[]
    for i in range(1,4):
        fs.append(f(i)) #f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1,f2,f3 =count()
print (f1())
print (f2())'''

f = lambda x:x*x
print (f(5))