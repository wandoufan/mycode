# 主要介绍python中浅拷贝、深拷贝、赋值的区别

# 浅拷贝是只拷贝外层数据(如有内层数据不拷贝数据只添加指针)，深拷贝是拷贝多层数据(对象的所有数据)
# 浅拷贝和深拷贝只有在多层数据中才有区别
# 原数据只有一层时，深浅拷贝一致且都不会随原数据的变化而变化
# 当修改多层数据的内层时，深拷贝不变，浅拷贝的内层部分会随之变化
# 对于元组、列表、字典等可能存在多层结构的类型，如果只改动外面一层，则浅拷贝和深拷贝一致
# 对于数字、字符串等单层结构的类型，浅拷贝和深拷贝一致且不会因原数据改动而变动

# 赋值相当于添加指针，两个变量实际指向同一个数据，且内存ID是相同的，因此赋值对象的值永远和原对象一致

import copy


# 1.修改多层结构的内层数据：
A = ('a', 'b', ['c', 'd'])
b = A
print('原列表：', A)
# 浅拷贝函数copy.copy()
B = copy.copy(A)
# 深拷贝函数copy.deepcopy()
C = copy.deepcopy(A)
A[-1].append('e')
print('新列表：', A)
print('赋值：', b)
print('浅拷贝：', B)
print('深拷贝：', C)
print('\n')

# 2.修改多层结构的外层数据：
alist = [1, 2, [3, 4]]
print('原列表：', alist)
blist = copy.copy(alist)
clist = copy.deepcopy(alist)
alist.append(5)
print('新列表：', alist)
print('深拷贝：', blist)
print('浅拷贝：', clist)
print('\n')

# 3.修改单层列表结构的数据：
a = [1, 2, 3]
print('原列表: ', a)
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
a.append(5)
print('新列表：', a)
print('赋值：', b)
print('浅拷贝：', c)
print('深拷贝：', d)
print('\n')

# 4.修改字符串/数字等单层结构的数据：
str1 = 'abcd'
print('原字符串：', str1)
s2 = copy.copy(str1)
s3 = copy.deepcopy(str1)
str1 = 'abc'
print('新字符串：', str1)
print('浅拷贝：', s2)
print('深拷贝：', s3)
