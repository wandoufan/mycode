#输入三个整数x,y,z，请把这三个数由小到大输出。

x=input('x=')
y=input('y=')
z=input('z=')

#方法一
list1=[]
list1.append(x)
list1.append(y)
list1.append(z)
list1.sort()
print('方法一',list1)

#方法二
a=0
if x>y:
    a=x
    x=y
    y=a
if y>z:
    a=y
    y=z
    z=a
if x>y:
    a=x
    x=y
    y=a

print(x,y,z)
#输入为8，3，5和8，5，3时结果不对？？

