# C++中的数据类型转换


## C语言中的数据类型转换格式
除了数据混合运算时系统自动进行类型转换外，用户可以自己进行强制类型转换
一般形式为 (类型名)(表示式)
```
(double)a
(int)(x + y)
(float)(5%3)
```
注意：强制类型转换会得到一个中间数据，并不改变原来变量的数据类型
注意：表达式应该都用括号括起来，例如(int)x + y表示先把x转换为整型，再与y相加
当表达式只有一个变量时，可以省略表达式括号，例如(int)x
类型名的括号一定不能省略，int(x)是错误写法


## warning: use of old-style cast
一般写法：实际测试，在Qt框架中按照C语言的类型转换方法会有警告提示
备注：好像只有在Qt 5.2.1等老版本中有警告提示，在Qt 5.11等新版本中正常
```
double d = 3.14;
float f = (float)d;
```
推荐写法：使用C++的强制类型转换
```
double d = 3.14;
float f = static_cast<float>(d);
```

--------------C++提供了4种强制类型转换--------------
备注：<>中填写要转换的数据类型，()中填写要转换的数据对象

## 概念
1. 上行转换
将子类指针转换为父类指针
2. 下行转换
将父类指针转换为子类指针


## 1. static_cast<data_type>(data) 编译时进行类型检查
static_cast属于最常用的
应用场景：
1. 基本数据类型之间的转换，如把int转换为char，把int转换成enum
2. 把空指针转换成目标类型的空指针
3. 把任何类型的表达式类型转换成void类型
4. 用于类层次结构中父类和子类之间指针和引用的转换


## 2. dynamic_cast<data_type>(data) 运行时进行类型检查
用法说明：
1. 不能用于内置的基本数据类型的强制转换
2. dynamic_cast转换如果成功的话返回的是指向类的指针或引用，转换失败的话则会返回NULL
3. 使用dynamic_cast进行转换，父类中一定要有虚函数，否则编译不通过
4. 在类层次间进行上行转换时，dynamic_cast和static_cast的效果是一样的
在进行下行转换时，dynamic_cast具有类型检查的功能，比static_cast更安全


## 3. const_cast<data_type>(data) 编译时进行类型检查
const_cast主要用来从const变量中删除const/volatile属性


## 4. reinterpret_cast<data_type>(data) 编译时进行类型检查
reinterpret_cast有着和C风格的强制转换同样的能力，尽量避免使用
它可以转化任何内置的数据类型为其他任何的数据类型，也可以转化任何指针类型为其他的类型
它甚至可以转化内置的数据类型为指针，无须考虑类型安全或者常量的情形


## static_cast和dynamic_cast区别
1. 上行转换
static_cast和dynamic_cast效果一样，都安全
2. 下行转换
需要注意要转换的父类类型指针是否真的指向子类对象
如果是，static_cast和dynamic_cast都能成功
如果不是，static_cast能返回，但是不安全，可能会出现访问越界错误；而dynamic_cast在运行时类型检查过程中，判定该过程不能转换，返回NULL
