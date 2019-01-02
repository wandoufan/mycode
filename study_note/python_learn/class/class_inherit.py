# 继承(inherit)机制可以让相似的类之间相同的属性方法自动传递，而不必每次都完整的去定义一个类
# 被继承的类称为基类、父类或超类，继承者称为子类；


class Dog:
    color = 'white'

    def __init__(self, sex):
        self.sex = sex

    def say(self):
        print('汪汪汪！')


class Taidi(Dog):

    def __init__(self, sex):
        pass#个性化内容
        Dog.__init__(self, sex)

    def say(self):
        print('喵喵喵！')


wangcai = Dog('boy')
laifu = Taidi('girl')
# 子类可以继承父类的所有属性方法
print(wangcai.color)
print(laifu.color)
# 如果子类中定义与父类相同的方法或属性，子类定义会覆盖父类定义
wangcai.say()
laifu.say()

# 调用未绑定的父类方法：对于构造方法__init__(),如果子类中也写了该方法，则需在子类的方法中调用父类的方法
print(wangcai.sex)
print(laifu.sex)


#多重继承：子类可以同时继承多个父类的属性和方法,但容易引起混乱，尽量避免使用
class Cat():
    age = 10

class Both(Dog,Cat):
    pass

wangcai = Both('boy')
print(wangcai.age)
