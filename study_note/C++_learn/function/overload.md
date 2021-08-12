# 函数重载overload

## 基本概念
函数重载是指在满足一定条件的前提下，C++允许同一个作用域内多个函数同名，包括：  
1. 函数形参的个数不同（注意有默认参数的情况）  
2. 函数形参的个数相同，但类型不同或顺序不同  
注意：重载函数的返回类型可以相同也可以不同，但函数之间只有返回类型不同，不能成为合法的重载函数  
当调用了重载函数时，编译器会根据函数参数情况自动去匹配到正确的函数  
函数重载是一种静态多态  
注意：overload不是关键字，进行函数重载时不需要用overload进行任何声明  
备注：C++支持函数重载，但C语言不支持函数重载  


## 函数重载的作用
重载函数常用在同一个作用域内，用同一个函数名来命名一组功能相近的函数  
使用重载函数可以减少函数名数量，避免了命名空间污染，一定程度上解决命名冲突的问题  


## 在子类中对函数进行重写
在子类中，经常对基类中的纯虚函数进行重写，这也是函数重载最常用的地方  
在函数定义时，在后面加上override关键字，即表示这个函数需要被重写  
如果后面的代码中没有进行函数重写，则编译器会报错  
注意：函数类型一般都是protected  
头文件示例：  
```
class SkyplotWidget : public QWidget
{
protected:
    void mousePressEvent(QMouseEvent *event) override;
}
```
源文件示例：  
```
void SkyplotWidget::mousePressEvent(QMouseEvent *event)
{
    if(event -> button() ==  Qt::RightButton)//鼠标点击右键
    {
        mouse_pos = event -> pos();
        mouse_global_pos = event -> globalPos();
        menu -> exec(mouse_global_pos);
    }
}
```


## 运算符重载
和函数重载一样，运算符也可以进行重载，即同一个运算符代表多个含义  
重载的运算符是带有特殊名称的函数，函数名是由关键字operator和其后要重载的运算符符号构成的  
```
// 对+进行重载，可以改造成任何想要的含义
// 注意这个函数的参数和返回值都必须是类
class operator+(class_1, class_2)
{
	...
}
```
