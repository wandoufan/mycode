# coding:utf-8

# super函数用于调用父类(超类)的一个方法，可以用来解决多重继承的问题；
# 只有在新式类中才可以使用super函数；
# 注意：当类中本身没有父类或继承object时，就不需要使用super函数

# 直接用类名调用父类方法在使用单继承时没问题，但如果使用多重继承；
# 就会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。

# super(type[, object-or-type])
# 参数type代表类，参数object-or-type一般代表self类

# 继承中存在的问题：
# 1.在类的继承中如果重定义了某个方法，该方法就会覆盖父类的同名方法，但有时候我们又希望实现父类的功能
# 这时候我们就需要调用父类的方法，可以通过super语句实现
# 在python3中使用super().function来代替super(class,self).function


class Dog:
    color = 'white'

    def __init__(self, sex):
        self.sex = sex

    def say(self):
        print('汪汪汪！')


class Taidi(Dog):

    def __init__(self, sex):
        pass  # 个性化内容
        # super语句最常见用法就是在子类中调用父类的初始化方法
        # super语句可以自动找到父类的方法，并传入self参数
        # 用super语句来代替Dog.__init__(self, sex)，可以在修改Dog类名时减少修改工作量
        super().__init__(sex)

    def say(self):
        print('喵喵喵！')
        # 注意：python3中使用super(Dog,self).say()会报错
        super().say()

taidi = Taidi('boy')
taidi.say()
