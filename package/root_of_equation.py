import math

'''def quadratic(a,b,c):
    if not isinstance(a,(int,float)):
        raise TypeError("Bad operrand type ")
    if not isinstance(b,(int,float)):
        raise TypeError("Bad operrand type ")
    if not isinstance(c,(int,float)):
        raise TypeError("Bad operrand type ")
        if (b**2-4*a*c) < 0:
            print ("此方程无解")            

        else :
            x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
            x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
            return x1,x2 

print (quadratic(1,2,1))'''

import math
def quadratic(a,b,c):
    if not isinstance(a,(int,float)):
        raise TypeError('a is not a number')
    if not isinstance(b,(int,float)):
        raise TypeError('b is not a number')
    if not isinstance(c,(int,float)):
        raise TypeError('c is not a number')
    d=b*b-4*a*c
    if a==0:
        if b==0:
            if c==0:
                return '方程根为全体实数'
            else:
                return '方程无根'
        else:
            x1=-c/b
            x2=x1
            return x1,x2
    else:
        if d<0:
            return '方程无根'
        else:
            x1 = (-b + math.sqrt(d))/2/a 
            x2 = (-b - math.sqrt(d))/2/a
            return x1,x2        
#print(quadratic(2,3,1))

def qual(x,n=3):
    s = 1
    while n > 0:
        n = n-1
        s = s*x
    return s
print(qual(4,2))

#定义默认参数要牢记一点：默认参数必须指向不变对象！ 


'''def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print (add_end())
print (add_end())'''

def add_end (b = []):
    b.append("End")
    return b
print (add_end([1,2,3]))
print (add_end())
print (add_end())