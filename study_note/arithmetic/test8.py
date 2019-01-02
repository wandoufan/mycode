#实现斐波那契数列
#递归法：
def fab1(n):
    a1=1
    a2=1
    a3=1
    for i in range(n-2):
        a3=a2+a1
        a1=a2
        a2=a3
    return a3

#生成器法：
def fab3(n):
    a=1
    b=1
    c=1
    for i in range(n-2):
        
        a=b
        b=c
        c=a+b
    yield c

for i in fab3(7):
    print(i)




#迭代法：
def fab2(n):
    if n==1:
        result=1
    elif n==2:
        result=1
    else:
        result=fab2(n-1)+fab2(n-2)
    return result

#print(fab1(8),fab2(8))