'''def now():
    print ("2018-2,4")
f =now
f()'''


'''def log(func):
    def wrapper(*args,**kw):
        print ('call %s():'% func.__name__)
        return func(*args,**kw)
    return wrapper
@log
def now():
    print ('2018.2.4')
now()
print (now.__name__)
'''
import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print ("%s%s()"%(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
@log("execute")
def now():
    print ("2018.2.5")

# 偏函数 Partial function
import functools
def int2(x,base=2):
    return int(x,base)

print (int2("100101000101010"))