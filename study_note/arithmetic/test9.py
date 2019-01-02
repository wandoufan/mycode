#求n的阶乘

def f1(n):
    if n==1:
        return 1
    else:
       return n*f1(n-1)

def f2(n):
    if n==1:
        result=1
    else:
        result=n*f2(n-1)
    return result

def f3(n):
    result=1
    for i in range(1,n+1):
        result=result*i
    return result


print(f1(6),f2(6),f3(6))

#求n的叠加和

def f1(n):
    if n==1:
        return 1
    else:
        return f1(n-1)+n

def f2(n):
    result=0
    for i in range(1,n+1):
        result=result+i
    return result


print(f1(100),f2(100))




