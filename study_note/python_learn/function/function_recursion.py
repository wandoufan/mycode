#递归recursion就是函数调用自身的这样一种行为,并需要设置正确的返回条件
#递归利用了堆栈这一数据结果，每次调用函数都有压栈，弹栈，保存等栈操作，比较耗费时间和空间
#注意：递归不一定比循环迭代效率高，使用不当可能会耗费更多的资源
#python的默认最大递归深度是100层，在写网络爬虫时可能需要更多的深度，可以用下列语句自定义深度
import sys
sys.setrecursionlimit(500)

#求100的阶乘
def test1(n):
    result=1
    for i in range(1,n+1):
        result=i*result
    return result
print('迭代法求阶乘',test1(5))

#递归法求100的阶乘
def recursion1(n):
    if n==1:
        return 1
    else:
        return n*recursion1(n-1)
print('递归法求阶乘',recursion1(5))

#求100的叠加和
def test2(n):
    result=0
    for i in range(1,n+1):
        result=i+result
    return result
print('迭代法求叠加和',test2(100))

#递归法求100的叠加和
def recursion2(n):
    if n==1:
        return 1
    else:
        return n+recursion2(n-1)
print('递归法求叠加和',recursion2(100))

#迭代法求斐波那契数列：n=1时f(n)=1；n=2时f(n)=1;n>2时f(n)=f(n-1)+f(n-2)
def fab2(n):
    a1=1
    a2=1
    a3=1
    for i in range(n-2):
        a3=a2+a1
        a1=a2
        a2=a3
    return a3
print('迭代法求斐波那契数列',fab2(8))

#递归法求斐波那契数列：n=1时f(n)=1；n=2时f(n)=1;n>2时f(n)=f(n-1)+f(n-2)
def fab1(n):
    if n==1:
        result=1
    elif n==2:
        result=1
    else:
        result=fab1(n-1)+fab1(n-2)
    return result
print('递归法求斐波那契数列',fab1(8))

#递归法求n层汉诺塔问题
print('汉诺塔步骤：')
def hannuo(n,x,y,z):
    if n==1:
        print(x,'-->',z)
    else:
        hannuo(n-1,x,z,y)
        print(x,'-->',z)
        hannuo(n-1,y,x,z)

hannuo(3,'a','b','c')