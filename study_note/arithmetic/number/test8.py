# 实现斐波那契数列
# n=1时f(n)=1；n=2时f(n)=1;n>2时f(n)=f(n-1)+f(n-2)

# 递归法：
def fab1(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        a1 = 1
        a2 = 1
        a3 = 1
        for i in range(n - 2):
            a3 = a2 + a1
            a1 = a2
            a2 = a3
        return a3

# 生成器法：
def fab2(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        a = 1
        b = 1
        c = 1
        for i in range(n - 2):
            a = b
            b = c
            c = a + b
        yield c

for i in fab2(7):
    print(i)

# 迭代法：
def fab3(n):
    if n == 1:
        result = 1
    elif n == 2:
        result = 1
    else:
        result = fab2(n - 1) + fab2(n - 2)
    return result

# print(fab1(8),fab2(8))

for i in range(1, 10):
    print(i, fab1(i))