#新式类是指继承object的类
class A(object):
      pass
      
#经典类是指没有继承object的类
class B:
     pass

#Python 2.x中默认都是经典类，只有显式继承了object才是新式类
#Python 3.x中默认都是新式类,经典类被移除，不必显式的继承object
#只有在新式类中才可以使用super函数

#关于新式类和经典类的区别：

class A:  
    pass  
class B:  
    pass  
class C(B):  
    pass  
class D(C,A):  
    pass  
#执行顺序为：D->C->B->A
class A(object):  
    pass  
class B(object):  
    pass  
class C(object):   
    pass  
class D(A,B,C):   
    pass  
#执行顺序为： D->A->B->C->Object

#新式类的MRO(method resolution order 基类搜索顺序)算法采用C3算法广度优先搜索
#而旧式类的MRO算法是采用深度优先搜索
#MRO就是类的方法解析顺序表，也就是继承父类方法时的顺序表