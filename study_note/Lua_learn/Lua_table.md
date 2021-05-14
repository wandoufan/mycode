# Lua中的表

## 基本概念
Lua中的表（table）其实是一个"关联数组"（associative arrays），数组的索引可以是数字、字符串或表类型  
在Lua里，table的创建是通过"构造表达式"来完成，最简单构造表达式是{}，用来创建一个空表  
注意：不同于其他语言的数组把0作为数组的初始索引，在Lua里表的默认初始索引一般以1开始  


## Table函数


## 代码示例
1. 可以使用[索引]来访问表中的元素，如果索引是字符串类型时，还可以使用.来进行访问操作  
```
site = {}
site["key"] = "value"
print(site["key"])
print(site.key)
```
2. table不能直接用print直接输出出来，只能用for循环进行输出
```
--创建空的table时不需要指明表的长度
table1 = {}
table1["0"] = "value_0"
table1["1"] = "value_1"
table1["2"] = "value_2"
table1["3"] = "value_3"
for k, v in pairs(table1) do
	print(k..":"..v)
end
```
3. 索引可以从0或负数开始，但当表中没有索引的对应值时，返回nil
```
table1 = {"a", "b", "c", "d", "e"}

for i = -3, #table1
do 
	print(table1[i])
end
```