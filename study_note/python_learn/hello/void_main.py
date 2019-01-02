def foo():
	print("hello,world")

# 表明当前模块是主模块，相当于void main(),由它来调用系统的其他模块;
# 如果模块是被直接执行的,__name__值为'__main__';
# 如果模块是被其他模块导入的，__name__值为模块的名字
if __name__ == '__main__':
	foo()


