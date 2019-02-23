# 主要记录与类和对象相关的一些BIF


# 1.issubclass(class,classinfo),如果第一个参数是第二个参数的子类，则返回Ture,否则False
class A:
    pass

class B(A):
    pass

class C:
    color = 'white'
    age = 10

print(issubclass(B,A))
print(issubclass(A,B))
print(issubclass(B,(A,C)))  # classinfo可以是类对象组成的元组，只要class是元组中任一元素的子类，即为True
print(issubclass(A,A))  # 类可以是其自身的的子类
print(issubclass(A,object))  # object是所有类的父类


# 2.isinstance(object,classinfo),如果第一个参数是第二个参数或参数子类的实例对象，则返回Ture,否则False
# 第一个参数必须是对象，第二个参数必须是类或类组成的元组
b1 = B()
print(isinstance(b1,B))
print(isinstance(b1,A))
print(isinstance(b1,C))
print(isinstance(b1,(A,B,C)))  # classinfo可以是类对象组成的元组，只要class是元组中任一元素的子类，即为True

#特别的，用来检查数据类型
def num_check(num):
    if isinstance(num,(int,float,complex)):
        print(num,'is number')
    else:
        print('not number')
num_check(3.14)
num_check('abc')


# 以下函数都是访问对象属性的BIF
# 3.hasattr(object,name),attr是attribute的缩写，测试一个对象里是否有指定的属性，返回True或False
c1 = C()
print(hasattr(c1,'color'))  # 注意：属性名要用括号括起来！
print(hasattr(c1,'weight'))

# 4.getattr(object,name,default)返回指定对象的属性值，如果属性值不存在则返回自定义的default
# 如果没有设置default参数，则返回AttributeError异常
print(getattr(c1,'color'))
print(getattr(c1,'weight','attribute not exist'))

# 5.setattr(object,name,value)设置对象中指定属性的值，如果属性不存在就新建属性并赋值
setattr(c1,'age',5)
print(getattr(c1,'age'))
setattr(c1,'sex','boy')
print(getattr(c1,'sex'))

# 6.delattr(object,name)删除对象中指定的属性，如果属性不存在返回AttributeError异常
delattr(c1,'sex')
print(getattr(c1,'sex','attribute not exist'))

# property()可以设置属性的属性，便于大规模修改属性时只修改一个地方
# 过于复杂，暂时跳过
