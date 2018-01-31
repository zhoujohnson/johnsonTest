'''def power(x,n=3):
    s= 1
    while n>0:
        n=n-1
        s=s*x
    return s 
print (power(2,3) )'''
'''def enroll (name,gender,age=18,city="shenzhen"):
    print ("name:",name)
    print ("gender:",gender)
    print ("age:",age)
    print ("city:",city)

enroll("johnson",12,city="xiangtan")  '''    

'''def end_End(L=[]):
    L.append("END")
    return L
# print (end_End([1,2,3,4]))
print(end_End())
print (end_End())'''
'''def End(l=None):
    if l is None:
        l = []
    l.append("END")
    return l
print (End())
print (End())
Python函数在定义的时候，默认参数L的值就被计算出来了
，即[]，因为默认参数L也是一个变量，它指向对象[]，每
次调用该函数，如果改变了L的内容，则下次调用时，默认
参数的内容就变了，不再是函数定义时的[]了。'''

'''def john(*numbers):
    sum = 0
    for i in numbers:
        sum = sum +i*i
    return sum
#print (john([1,2,3]))
#print (john((1,2,3,4)))
print (john(1,2,3))'''

'''def person(name,age,**kw):
    print ("name:",name,"age:",age,"other:",kw)

person("Mike",36)

extra = {"city":"China","who":"who ever"}
person ("johnson",22,**extra)'''

'''def person (name,age,*,city="guangzhou",job ):
    print (name,age,city,job)
person ("john",11,job="engneer")
'''

'''def product(x,*y):
    s=1
    for x in t:
        for y in t:
            s = s+x*y
    return s  
print (product())'''


'''def product(x=1,*nums):
    result = x
    for num in nums:
        result *= num
    return result
b=product()
print (b)'''

'''def f(n):
    if n==1:
        return 1
    else :
        return n*f(n-1)

print (f(1))
print (f(10))'''

def f(n):
    return f1(n,1)
def f1(n1,m1):
    if n1 ==1:
        return m1 
    return f1(n1-1,n1*m1)
print (f(100))