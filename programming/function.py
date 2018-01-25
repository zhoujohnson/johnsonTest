import sys
sys.path.append("..") #根据 sys.path环境变量的值，找到具体模块路径
from package.my_abs import my_abs
'''n1 = 255
n2 = 1000
n1 = hex(n1)
n2 = hex(n2)
print (n1)
print (n2)

# def定义一个函数，依次写出函数名、括号、括号中的参数和冒号
# 缩进块中编写函数体，函数的返回值用return语句返回。
def my_abs(x):
    if x>0:
        return x
    else :
        return -x'''


print (my_abs(2)) # 如何从package中导入函数求值

# pass语句作为占位符
def If ():
    pass

# print(my_abs("a"))  #修改抛出异常方式 isinstance()

import math
def action (x,y,step,z=0):
    nx = x + step*math.cos(z)
    ny = y + step*math.sin(z)
    return nx,ny
x,y = action(1,2,3,math.pi/2)
print (x,y)