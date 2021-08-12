# Lua语法

## 基本语法
1. 输出字符串时，print后面可以有括号，也可以没有括号
```
print"hello, world";
print("hello, world");
```
2. 每个语句后面可以有分号，也可以没有分号
```
print"hello, world";
print"hello, world"
```


## print的写法
1. 逗号隔开，中间会多出一个tab的空格长度
```
print("a 的值为:", a)
> a 的值为:	1
```
2. 用两个点隔开，中间没有间隔，两边只能是字符串型的数据
注意：这种方式不能用来输出nil型的变量，否则会报错  
```
print("a 的值为:"..a)
> a 的值为:1
```


## 注释
1. 单行注释用两个以上的减号
```--这是注释```
```--这是注释--```
2. 多行注释
```
--[[
这是注释
--]]
```
```
--[[
这是注释
]]--
```


## 标识符
1. 标识符只能由字母、数字、下划线组成，且首个字符必须是字母或下划线
2. 标识符区分字母大小写
3. 最好不要使用下划线加大写字母的标示符，因为这样的变量名一般保留用于Lua的内部全局变量


## 保留关键词
保留关键字不能作为常量或变量或其他用户自定义标示符  
```
and	break	do	else
elseif	end	false	for
function	if	in	local
nil	not	or	repeat
return	then	true	until
while	goto
```


## 赋值语句
1. Lua可以对多个变量同时赋值
当变量个数 > 值的个数时，多余变量设置为nil
当变量个数 < 值的个数时，多余的值会被忽略
```
a, b = 1, 2
print(a, b)
```
2. Lua可以通过赋值语句交换两个变量的值
```
a, b = 1, 2
a, b = b, a
print(a, b)
```