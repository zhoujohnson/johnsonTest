'''sum = 0
a = range(101)
for a1 in a:
    sum = sum + a1
print(sum)

# 求100以内奇数之和
sum = 0
s = 99
while s>0:
    sum = sum + s
    s=s-2
print (sum)

# break语句用法
s=1 
while s<100:
    if s>10:
        break 
    print (s)
    s = s + 1
print ("end")'''

#continue 语句用法
n = 0
while n <10:
    n=n+1
    if n % 2 ==0:
        continue 
    print(n)
    
print ("end")