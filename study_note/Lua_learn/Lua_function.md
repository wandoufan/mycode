# Lua函数

## 定义格式
```
optional_function_scope function function_name( argument1, argument2, argument3..., argumentn)
    function_body
    return result_params_comma_separated
end
```
1. optional_function_scope
该参数是可选参数，用来指定函数是全局函数还是局部函数，如果未设置该参数则默认为全局函数  
如果要设置函数为局部函数，则需要使用关键字local  
2. function
用来标识函数的关键字  
3. function_name
函数名称  
4. argument
函数参数，函数可以不带任何参数，可以带固定个数的参数，也可以带可变个数的参数  
其中，用三个点```...```来表示函数是可变个数的参数  
如果既有可变参数，又有固定参数，则固定参数放在前面  
5. function_body
函数体  
6. result_params_comma_separated
函数的返回值，函数可以有多个返回值，每个值之间逗号隔开  


## 代码示例
1. 函数可以存在变量里，因此可以像变量一样直接相互赋值  
```
function factorial1(n)
    if n == 0 then
        return 1
    else
        return n * factorial1(n - 1)
    end
end
print(factorial1(5))
> 120
factorial2 = factorial1
print(factorial2(5))
> 120
```
2. 将函数作为参数传递给另一个函数
```
function myprint(param)
	print("result is "..param)
end

function add(num1, num2, myprint)
	result = num1 + num2
	myprint(result)
end

add(1, 2, myprint)
```
3. 函数可以有多个返回值
```
function test(num1, num2, num3)
	return num3, num2, num1
end

print(test(1, 2, 3))
```
4. 函数的参数个数可以不固定
```
function add(...)
	sum = 0
	for k, v in ipairs{...}
	do
		sum = sum + v
	end
	return sum
end

print(add(1, 2, 3))
print(add(1, 2, 3, 4, 5))
```