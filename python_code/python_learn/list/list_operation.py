#列表属于可变数据类型，包含任意数目的各种python对象，使用方括号[]来定义

#列表创建赋值
alist=[123,'abc',3.14,[456,'def'],3-4j]
blist=[1,2,3,4,5,6,7,8,9]
clist=['a','b','c','B']

print(alist,blist)
print(list('foo'))#将foo转换为列表型并输出

#判断对象是否列表成员
print('abc' in alist)
print('abc' not in alist)

#切片操作访问列表中的值
#注意：切片的内容是不包含最后一个值的!
print(alist[:])
print(alist[0])
print(alist[-1])
print(alist[2:4])
print('输出子列表中的子元素',alist[3][1])
print('输出相反序列',alist[::-1])
print('隔一个取一个',alist[::2])

#更新列表元素,用list.append()方法可以直接在列表后面添加内容
blist[1]='a'
blist[3:5]='b','c'
blist.append(['d','e','f'])
print(blist)

#删除列表元素，使用索引标记或者list.remove()方法
del alist[0]
alist.remove('abc') 
print(alist)

#将序列重复n次，也可以直接blist*=3
print(blist*3)

#连接操作符+,注意只能用来相同类型的数据连接，不能列表+字符串，也不能列表+单个列表元素
print(alist+blist)

#输出序列长度
print('序列长度是',len(alist))

#in,not in 判断成员关系
print('apple' in alist)
print(1 not in alist,'\n')

#sorted()函数按字典序排序输出
print(sorted(clist))

#reversed()反转函数，逆序输出
for t in reversed(clist):
	print(t)

#enumerate()列举函数，顺序输出
for i,t in enumerate(clist):
	print(i,t)

#zip()组合函数
list1=['big','blue','apple']
list2=['small','yellow','banana']
for i,j in zip(list1,list2):
	print('%s,%s' % (i,j))

#sum()求和函数,仅当列表元素都是数字;sum()中有一个可选参数，表示从该数字加起
list3=[1,2,3]
print(sum(list3,10))
print(str(sum(list3)))

#list()和tuple()函数用于类型转换（例如元组类型转换为列表类型后就可以修改内容了）
atuple=tuple(alist)
print(atuple,'is a type of',type(atuple).__name__)
print(atuple==alist)#虽然元素相同，但id不同,仅当元素和类型相同时才为ture

