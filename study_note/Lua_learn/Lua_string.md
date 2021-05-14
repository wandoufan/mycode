# Lua字符串

## 表示方式
字符串由一对双引号或单引号来表示  
也可以用[[]]来表示一段字符串  
```
html = [[
line1
line2
line3
]]
print(html)
```


## 字符串函数
1. string.upper(argument)
字符串全部转为大写字母后返回其副本，原字符串不变  

2. string.lower(argument)
字符串全部转为小写字母后返回其副本，原字符串不变  

3. string.gsub(mainString,findString,replaceString,num)
对字符串指定部分进行替换后返回其副本，原字符串不变  
mainString为要操作的字符串，findString为被替换的字符，replaceString要替换的字符，num为替换次数（可以忽略，则全部替换  

4. string.find (str, substr, [init, [end]])
在一个指定的目标字符串中搜索指定的内容(第三个参数为索引)，返回其具体位置，如果不存在则返回nil  
```
> string.find("Hello Lua user", "Lua", 1) 
7    9
```

5. string.reverse(arg)
字符串反转后返回其副本，原字符串不变  

6. string.format(...)
返回一个类似printf的格式化字符串  
```
> string.format("the value is:%d",4)
the value is:4
```

7. string.char(arg)
将整型数字转成字符并连接，返回一个字符串  
```
> string.char(97,98,99,100)
abcd
```

8. string.len(arg)
计算字符串长度

9. string.rep(string, n)
返回字符串string的n个拷贝
```
> string.rep("abcd",2)
abcdabcd
```

10. string.byte(arg[,int])
转换字符为整数值，可以用int参数指定某个字符，默认第一个字符  
```
> string.byte("ABCD",4)
68
> string.byte("ABCD")
65
```

11. string.gmatch(str, pattern)
返回一个迭代器函数，每一次调用这个函数，返回一个在字符串 str 找到的下一个符合 pattern 描述的子串  
如果参数 pattern 描述的字符串没有找到，迭代函数返回nil  
```
> for word in string.gmatch("Hello Lua user", "%a+") do print(word) end
Hello
Lua
user
```

12. string.match(str, pattern, init)
string.match()只寻找源字串str中的第一个配对，参数init可选，指定搜寻过程的起点，默认为1  
在成功配对时, 函数将返回配对表达式中的所有捕获结果；当没有成功的配对时, 返回nil  
```
> string.match("Hello Lua user", "%a+")
Hello
```

13. string.sub(s, i [, j])
截取字符串中的一部分，返回截取下来的字符串，原字符串不变  
三个参数分别是要原字符串，截取起始位置，截取结束位置(可选参数)  
```
a = "123456789"
b = string.sub(a, 3, 5)
print(a)
print(b)
> 123456789
> 345
```


## 字符串的格式化及正则匹配
https://www.runoob.com/lua/lua-strings.html