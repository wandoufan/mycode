# coding:utf-8

# 关于python的内置函数locals()和globals()：
# 两个函数都返回一个键为变量，值为变量值的字典，分别代表局部和全局变量

# 每个函数都有着自已的名字空间，叫做局部名字空间，它记录了函数的变量，包括函数的参数和局部定义的变量。
# 每个模块拥有它自已的名字空间，叫做全局名字空间，它记录了模块的变量，包括函数、类、其它导入的模块、模块级的变量和常量。
# 还有就是内置名字空间， 任何模块均可访问它，它存放着内置的函数和异常。

# 当一行代码要使用变量 x 的值时，Python 会到所有可用的名字空间去查找变量，按照如下顺序:
# 局部名字空间 - 特指当前函数或类的方法。如果函数定义了一个局部变量 x, 或一个参数 x，Python 将使用它，然后停止搜索。
# 全局名字空间 - 特指当前的模块。如果模块定义了一个名为 x 的变量，函数或类，Python 将使用它然后停止搜索。
# 内置名字空间 - 对每个模块都是全局的。作为最后的尝试，Python 将假设 x 是内置函数或变量。


class Test:
	x = 6
	y = 'hello'

	def test1(self,a,b):
		d = 1
		c = a+b
		for i in range(5):
			j = 1
			k = i
		print(locals())
		print(globals())
		self.test2(locals())

	def test2(self,args):
		for k,v in args.items():
			print(k,v)


t = Test()
t.test1(1,2)
