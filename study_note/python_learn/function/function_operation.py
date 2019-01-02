#python的函数都是有返回值的，即使返回值为None
#函数参数分为形式参数和实际参数；形参指函数括号中定义的变量名，实参指函数调用实际传递进来的值


#关键字参数是在定义时通过参数名指定要赋值的参数，避免搞错参数的顺序而导致函数调用出错
def add(num1,num2):
    '''注释：add()函数用于参数相加'''
    return num1+num2
print('关键字参数',add(num1=1,num2=2))

#默认参数是在定义时赋予了默认值的参数，从而可以不带参数的调用函数
def output(name='port:',number='80'):
    return name+number
print('默认参数',output())

#收集参数/可变参数，即不确定函数有多少个参数时在参数前加*表示打包,函数的其他参数不加*标识
def test1(*list1,extra):
    print('收集参数',list1)
    print('位置参数',extra)
test1(1,2,3,4,extra='abc')
#星号*既可以打包也可以解包，将一个列表list2传入test函数中作为收集参数时需要在list2前加*表示实参需解包后使用
def test2(*list2):
    print('有%d个收集参数'%(len(list2)))
list2=['a','b','c']
test2(list2)
test2(*list2)

#函数内的注释称为函数文档字符串,通过'''来标识，可以用特殊属性function.__doc__来获取
print('查看函数文档',add.__doc__)

#不确定函数用法时用help(function)查看函数文档
help(add)

#函数返回值的数据类型可以动态变化，并且各不相同
def test3():
    return 1,2,'a','b'
print('返回元组',test3())
def test4():
    return [1,2,'a','b']
print('返回列表',test4())