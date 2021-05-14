# Lua逻辑语句
备注：语句后面


## if
备注：布尔表达式可以用括号括起来，也可以不用括号  
1. if语句
```
if(a > b)
then
	print(a)
end
```
2. if-elseif语句
```
if a > b
then
	print(a)
elseif a < b
then
	print(b)
end
```
3. if-elseif-else语句
```
if a > b
then
	print(a)
elseif a < b
then
	print(b)
else
	print("equal")
end
```

## while
```
while(condition)
do
   statements
end
```

## for
1. 数值for循环
第一个参数是起始值，第二个参数是终止值  
第三个参数是步长，可选值，如果不指定，默认为1  
```
for a = 1, 30, 2
do
	print(a)
end
```
2. 泛型for循环
通过一个迭代器来遍历表中的数据，pairs和ipairs都是Lua提供的迭代器函数  
```
table1 = {}
table1["1"] = "value_1"
table1["2"] = "value_2"
table1["3"] = "value_3"
for k, v in pairs(table1)
do
	print(k..":"..v)
end

table2 = {"a", "b", "c"}
for k, v in ipairs(table2)
do
	print(k, v)
end
```

## repeat-until
类似与do-while语句
```
repeat
   statements
until( condition )
```

## break
```
a = 10
while( a < 20 )
do
   a = a + 1
   if(a > 15)
   then
      break
   end
end
```

## goto
语法格式```goto label```  
label格式```::label::```  
```
local a = 1
::label:: print("--- goto label ---")

a = a+1
if a < 3 then
    goto label
end
```
