#闭包closure:如果在一个内部函数里，对在外部作用域(非全局作用域)的变量进行引用，且外函数的返回值是内函数的引用
#则内部函数就被认为是闭包的
#test1中的变量x也是局部变量，但是在test1的内部函数test2中也只能对x进行访问，不能修改

def test1(x):
    def test2(y):
        return x*y
    return test2

i=test1(8)#此时i=8y
print(i(5))#此时i(5)=8*5=40

#如果坚持要在内部函数中修改外部函数的变量，使用关键字nonlocal可以达到目的

def test2():
    count=10
    def test3():
        nonlocal count
        count=5
        print('内部函数',count)
    test3()
    print('外部函数',count)

test2()