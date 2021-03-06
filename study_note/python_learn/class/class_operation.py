# 主要记录python中类的概念和一些基本操作

# 容器如列表，元组，字符串，字典等是对数据的封装
# 函数是对常用代码语句的封装
# 类是对方法和属性的封装，即函数+数据
# 模块是对完整程序的封装

# 类(class)=属性+方法
# 用类来创建一个真正的对象(object)，对象称为类的一个实例(Instance),也叫实例对象


# 一、创建类及类的示例化
# 默认类名大写字母开头，函数名小写字母开头
# 每个方法都有一个self参数，相当于C++的this指针，一个类可以生成无数对象，self就是每个对象的标识
# 类内的每个函数都加上self参数，方便类内函数相互调用
class Dog:
    # 类中的属性
    color = 'white'
    age = 5
    # 类中的方法
    def run(self):
        print('dog running!')

    def eat(self):
        print('dog eating!')

    def set_sex(self, sex):
        self.sex = sex

# 创建对象，即类的实例化
wangcai = Dog()
wangcai.run()
wangcai.eat()
wangcai.color = 'black'
print(wangcai.color)
print(wangcai.age)
wangcai.set_sex('boy')
print(wangcai.sex)


# 二、特殊的构造方法：__init__()
# 只要实例化一个对象，该方法就会在实例化成对象时第一个被调用
# 通过该方法，实例化对象时可以传入参数，参数会自动传入__init__()方法中
class Cat:

    def __init__(self, sex):
        # self.change_sex()
        self.sex = sex
        self.change_sex()

    def change_sex(self):
        print('!!', self.sex)
        self.sex = 'boy'
        print('!!', self.sex)
        print('change sex to boy')

laifu = Cat('girl')
# 注意：change_sex的位置前后决定了执行的先后顺序，内部的self.sex和外部传入的sex二者之间不一定相等
print(laifu.sex)
print('\n')


# 三、类中的私有属性
# C++和Java中用public和private关键字来区分数据的公有和私有
# Python默认对象的属性和方法都是公开的，但在变量名或函数名前加上'__'就会变私有(伪私有)
# 私有变量在外部是隐藏无法访问的，如果要访问就从内部进行
class Student:
    __sex = 'boy'
    def __init__(self, age):
        self.age = age

    def get_sex(self):
        return self.__sex

tom = Student(10)
print(tom.get_sex())
# 实际在外部可以通过'_类名__变量名'的方式直接访问，即python对象没有真正意义的私有权限控制机制
print(tom._Student__sex)


# 四、类和类的实例化对象的属性
# 使用__dict__查看对象拥有的属性，仅显示实例对象的属性，不显示类属性和特殊属性
# __dict__属性结果是一个字典格式，其中键表示属性名，值表示对应的数据值
class Test(object):
    subject = 'math'
    gender = 'boy'
    def __init__(self, age):
        self.age = age

test = Test(10)
# 实例化对象可以直接添加类中没有的属性，对实例化对象添加新属性不会影响类的属性
test.name = 'abc'
test.color = 'red'
# 注意：类的__dict__属性和类的实例化对象的__dict__属性不相同
# 实例化对象的属性包括name、color、age，但不包括类中的subject、gender
print(test.__dict__)
# 类的属性包括subject、gender及其他自带属性，但不包括name、color、age
print(Test.__dict__)


# 五、类中属性的值
# 如果对实例对象的属性进行赋值，就覆盖了类对象的属性；
# 如果没有对实例对象的属性进行单独赋值，则实例对象引用的还是类对象的属性；
# 尽量避免在一个类中写很多的属性方法，尽量利用继承机制来简化
class D:
    count = 0

a = D()
b = D()
c = D()
b.count += 10
D.count += 100
c.count += 10
print(a.count, b.count, c.count)
