# 与return相关的用法

# 程序执行时如果遇到第一个return即立即跳出整个程序返回，不会再往下执行,程序可以有多个return语句
def func1(a,b):
	if a>b:
		return a
	elif a==b:
		return 'ok'
	else:
		return b


# 特别的在try-except-finally中,即使前面有return语句了,finally中的语句依然会执行后再开始return 
def func3():  
    try:  
        print('return test1')
        return 'ok'
    except Exception as e:
    	print(e)
    finally:
        print('return test2') 
print(func3()) 


# 注意：在递归调用中
def recursion2(n):
    if n==1:
        return 1
    else:
        return n+recursion2(n-1)
print('递归法求叠加和',recursion2(100))


# 对于函数有返回值，可以用变量来函数返回值，也可以忽略返回值
def test(a,b,c):
	print('test')
	return a+b,b+c
# 用x,y来接收返回值
x,y=test(1,2,3)
print(x,y)
# 也可以直接调用函数，忽略返回值
test(1,2,3)


# 函数没有return语句时，默认return 一个None对象
def func2():
	pass
print(func2())