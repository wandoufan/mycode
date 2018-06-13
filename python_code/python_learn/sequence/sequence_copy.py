
#浅拷贝和深拷贝只有在多层数据中才有区别
#备注：浅拷贝是只拷贝一层，深拷贝是拷贝多层
#对于元组、列表、字典等可能多层结构，如果改动外面一层，则浅拷贝和深拷贝一致
#对于数字、字符串等，浅拷贝和深拷贝一致且不会因原数据改动而变动
#赋值相当于添加指针，两个变量实际指向同一个数据，且内存ID是相同的


#修改多层数据：
import copy
A=('a','b',['c','d'])
print('原列表：',A)
#浅拷贝函数copy.copy()
B=copy.copy(A)
#深拷贝函数copy.deepcopy()
C=copy.deepcopy(A)
A[-1].append('e')
print('新列表：',A)
print('浅拷贝：',B)
print('深拷贝：',C)
print('\n')

#修改一层数据：
a=[1,2,3]
print('原列表: ',a)
b=a
c=copy.copy(a)
d=copy.deepcopy(a)
#a[1]=4
a.append(5)
print('新列表：',a)
print('赋值：',b)
print('浅拷贝：',c)
print('深拷贝：',d)
print('\n')


#修改多层数据：
alist=[1,2,[3,4]]
print('原列表：',alist)
blist=copy.copy(alist)
clist=copy.deepcopy(alist)
alist[-1].append(5)
print('新列表：',alist)
print('深拷贝：',blist)
print('浅拷贝：',clist)


#字符串
str1='abcd'
s2=copy.copy(str1)
s3=copy.deepcopy(str1)

str1='abc'

print(str1,s2,s3)

#数字
a=1
b=copy.copy(a)
c=copy.deepcopy(a)

a=2

print(a,b,c)
