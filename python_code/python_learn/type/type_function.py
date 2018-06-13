
#type()以一个对象作为参数，并返回该对象的类型

print(type(4).__name__)

print(type(4.0))

print(type('$*!'))

a=type('hello,world!')
print(a)

b=type(type(4))
print(b)

print('\n')

#str()函数将对象的内容转化为字符串，相当于引号''
a=str(True)
print(a[1])

b=str(3.1415)
print(b[1])

c=str([1,2,'b',3,'c',4])
print(c[0])
print(c[1])
print(c[2])

d=str(0xff)
print(d)

print('\n')

#repr()函数与str()函数大致相同
d=repr(3.1415)
print(d[1])


#用来转换对象类型
print(int(3.6))
print(float(4))
print(complex(3))
print(list('abcd'))
print(tuple('abcd'))
print(bool(0))
print(bool([]))
print(bool(-2))
print(bool(1))
print(bool(3))
print(bool('hello'))

print(type(int(3.2)).__name__)






