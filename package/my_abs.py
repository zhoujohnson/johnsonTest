#封装一个求绝对值的函数
# 简单版本
'''def my_abs(x):
    if x>0:
        return x
    else :
        return -x'''

# 相对提升版本，涉及到引入报错
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError("bad operrand type")
    if x>=0:
        return x
    else :
        return -x