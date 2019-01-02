# 函数中定义的参数及变量都称为局部变量local variable，仅在函数内有效
# python运行函数使用栈存储，当执行完函数后，函数的所有数据都会被自动删除
# 如果在函数内部修改去全局变量global variable,那么python会创建一个名称相同的局部变量代替，真正的全部变量不会变化
# 注意：尽量避免局部变量与全局变量名字相同,在函数内仅能访问全局变量，不能修改全局变量的值
# 注意：全局变量很容易造成代码BUG，在使用过程中要尽量避免使用到全局变量！


def discounts(price, rate):
    final_price = price * rate
    old_price = 50
    print('函数内修改的全局变量old_price', old_price)
    return final_price

old_price = 80
rate = 0.75
new_price = discounts(old_price, rate)
print('真正的全局变量old_price', old_price)
print(new_price)

#如果坚持要在函数中修改全局变量，使用关键字global可以达到目的
count=10
def change_count():
    global count
    count=5
    print('函数内部',count)

change_count()
print('函数外部',count)

#内嵌函数/内部函数：允许在函数内部定义另一个函数，内部函数的作用域都在外部函数之内
#注意：在只有在test2()内可以随意调用test3(),test2()外调用都会报错未定义test3()

def test1():
    test2()

def test2():
    def test3():
        print('hello,world')
    test3()

test1()
test2()
