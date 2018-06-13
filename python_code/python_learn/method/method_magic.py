#魔法方法__magic__总能够在适当的时候被调用,例如之前的__init__和__name__


#构造方法 __init__(self,[...]),用在类定义中，是类在实例化对象的时候首先会调用的一个方法
#__init__()的返回值一定是None，不能是其他,默认不写返回
class Rectangle:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def get_area(self):
        return self.x*self.y

    def get_perimeter(self):
        return (self.x+self.y)*2

ractangle1=Rectangle(3,4)
print(ractangle1.get_perimeter())
print(ractangle1.get_area())

