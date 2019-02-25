# 主要介绍python中函数的一些基本知识点


# 一、函数的基本知识

# 1.python函数注释的标准格式
def student_info(name, age):
    """
    首先介绍函数的基本功能
    :param name: 介绍name参数
    :param age: 介绍age参数
    :return: 介绍函数的返回值
    """
    return name + str(age)

# 2.用pass关键字来标记未写完的函数
# 在python中的函数中如果不写任何语句块，解释器会产生报错
# 用pass语句来标记暂时不写的代码块，pass语句不做任何事情
# 注意：pass关键字没有return的功能，即如果pass下有其他代码仍然会继续执行
def pass_test():
    """
    未完成待补充的函数
    """
    pass

# 3.函数内的注释称为函数文档字符串,通过'''来标识，可以用特殊属性function.__doc__来获取
def test():
    """
    这是函数的注释文档
    """
    pass
print(test.__doc__)

# 4.可以通过函数对象的.__name__属性来获取函数的名字
func = test
print(func.__name__)

# 5.不确定函数用法时用help(function)查看函数文档
help(test)

# 6.
# 函数可以接收函数作为参数
# 函数可以返回函数作为结果
# 函数可以作为一个元素被存入列表等数据类型中
# 函数可以赋值给一个变量


# 二、函数的返回值

# 1.python的函数都是有返回值的，即使返回值为None
def test():
    """
    没有return语句时返回值为None
    """
    a = 1 + 1
print(test())

# 2.关于函数返回值的数据类型
def test():
    """
    函数返回多个参数时，如果没有指定，默认是将参数组合为一个元组类型返回
    """
    return 1, 2, 'a', 'b'
print(test(), type(test()))
def test():
    """
    指定函数返回参数的类型
    """
    return [1, 2, 'a', 'b']
print(test(), type(test()))

# 3.func和func()的区别
# python中的函数加上括号之后就会直接执行，如果不加括号就可以像变量一样被传递
# 注意：python语言中函数可以像变量一样被当做参数传递给另一个函数，而C和Java语言中不能这么实现
def double(x):
    print(2 * x)

def test(x, func):
    """
    函数可以接受函数作为参数，同样的，函数可以作为参数被传递给另一个函数
    """
    func(x)

param = double
print(type(param))
test(1, param)