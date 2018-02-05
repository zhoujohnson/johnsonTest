'''l = [x*x for x in range(10)]
print (l)
m =(x*x for x in range(10))
for n in m :
    print (n)'''


'''def fib (max):
    n,a,b = 0,0,1
    while n<max:
        print (b)
        a,b=b,a+b
        n = n+1
    return "do it"
print (fib(6))'''

def fix(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b=b,a+b
    return "我就是程序员，哼哼哈"

'''def odd():
    print ("step 1")
    yield 1
    print ("step 2")
    yield 3
    print ("step 3")
    yield 5
o=odd()
next(o)
next(o)'''
g = fix(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
