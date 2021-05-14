# Lua变量

## 全局变量
1. 变量除非用local显式的声明为局部变量，否则在创建之后默认就是全局变量
2. 访问一个没有初始化赋值的全局变量也不会报错，只是得到的结果是nil
3. 如果需要删除一个全局变量，只需要将变量赋值为nil
4. Lua是动态型语言，变量在使用前不需要声明类型


## 基本数据类型
1. nil
这个最简单，只有值nil属于该类，表示一个无效值（在条件表达式中相当于false）  
如果用nil进行类型比较，则必须加上双引号，因为type(X)返回是一个"nil"字符串，属于string类型  
```
type(X)==nil
> false
type(X)=="nil"
> true
```
2. boolean
包含两个值：false和true  
Lua中只有false和nil为false，其他的都为true，数字0也是true  
```
if 0 then
    print("数字 0 是 true")
else
    print("数字 0 为 false")
end
> 数字 0 是 true
```
3. number
表示双精度类型的实浮点数  
Lua中默认只有一种number类型，即double（双精度）类型  
整数和浮点数的类型都属于number  
4. string
表示字符串
5. function
由C或Lua编写的函数，用function关键字来标识函数名  
6. userdata
userdata是一种用户自定义数据，用于表示一种由应用程序或C/C++语言库所创建的类型  
可以将任意C/C++的任意数据类型的数据（通常是struct和指针）存储到Lua变量中调用  
7. thread
表示执行的独立线路，用于执行协同程序  
8. table
Lua中的表结构


## 查看数据类型
```
print(type("Hello world"))      --> string
print(type(10.4*3))             --> number
print(type(print))              --> function
print(type(type))               --> function
print(type(true))               --> boolean
print(type(nil))                --> nil
print(type(type(X)))            --> string
```

