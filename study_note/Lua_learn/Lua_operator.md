# Lua运算符

## 算术运算符
```
+	加法
-	减法
*	乘法
/	除法
%	取余
^	乘幂
-	负号
```


## 关系运算符
```
==	等于
~=	不等于 注意不是!=
>	大于
<	小于
>=	大于等于
<=	小于等于
```


## 逻辑运算符
1. and	逻辑与操作符
x and y: if x is true,then y,else x   返回x或y的值
注意：当x为ture时返回的是y，当x为false时返回的才是x
2. or	逻辑或操作符
x or y: if x is true,then x,else y   返回x或y的值
当x为true时返回x，当x为false时返回y
注意：返回的是x或y的值，不是True或False
3. not	逻辑非操作符
not x    返回True或False


## 其他运算符
1. .. 连接两个字符串
```
print("a".."b")
```
2. # 一元运算符，返回字符串或表的长度
```
print(#"654321")
```

## 运算符优先级
从高到低
```
^
not    - (unary)
*      /       %
+      -
..
<      >      <=     >=     ~=     ==
and
or
```