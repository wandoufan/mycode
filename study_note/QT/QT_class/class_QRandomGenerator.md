# QRandomGenerator

## 基本功能
使用这个类就可以从高质量的随机数字产生器中获得一个随机值  
备注：在Qt5.10版本中新增了这个类，用来替代qrand()和qsrand()函数  


## 用法示例
1. 获得一个[10, 100)的随机数
```
int num = QRandomGenerator::global() -> bounded(10, 100);
```


## 常用公共函数
备注：所有函数产生随机值的范围都是左闭右开区间 [low, high)
1. double QRandomGenerator::bounded(double highest)
从0到highest中间产生一个double类型的随机数  
参数可以为负数，此时产生的随机数也是负的随机数  
备注：负的参数必须不能是整数，否则运行时会报错  
函数效果等同于执行：  
```
return generateDouble() * highest;
```

2. quint32 QRandomGenerator::bounded(quint32 highest)
这是一个重载函数，从0到highest中间产生一个quint32类型的随机数  
实际测试，参数不能为负数  

3. quint32 QRandomGenerator::bounded(quint32 lowest, quint32 highest)
这是一个重载函数，从lowest到highest中间产生一个quint32类型的随机数  

4. int QRandomGenerator::bounded(int highest)
这是一个重载函数，从0到highest中间产生一个int类型的随机数  
参数必须为正数  

5. int QRandomGenerator::bounded(int lowest, int highest)
这是一个重载函数，从lowest到highest中间产生一个int类型的随机数  
参数可以为负数，但highest参数必须比lowest参数值更大  

6. double QRandomGenerator::generateDouble()
从[0, 1)范围内产生一个double型的随机数  
实际使用时可以用如下的写法，虽然没有看太明白  
```
return generateDouble() * highest;
```


## 静态公共函数
1. [static] QRandomGenerator \*QRandomGenerator::global()
返回一个指针，指向一个QRandomGenerator对象  
global()和system()的区别没有搞太明白，一般先使用global()函数  
备注：这个函数是线程安全的  

2. [static] QRandomGenerator QRandomGenerator::securelySeeded()
返回一个QRandomGenerator对象  

3. [static] QRandomGenerator \*QRandomGenerator::system()
返回一个指针，指向一个QRandomGenerator对象  
备注：这个函数是线程安全的  




