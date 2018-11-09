# 关于list函数的各种方法

alist = [1, 2, 3, 4, 'a', 'b', 'c', 'd']
blist = ['x', 'y', 'z']

# 查看返回对象在列表中的索引,如果对象没有在列表中则会报错
print(alist.index('b'))
# 查找列表指定范围中是否有指定的对象，若有返回索引值，若没有报错
print(alist.index('a', 1, 9))

# 在列表末尾添加一个对象
alist.append('e')
print(alist)

# 在列表尾部追加一个列表
# 注意extend()函数没有返回值，即不能赋值clist = alist.extend(blist)
alist.extend(blist)
print(alist)

# 在列表指定索引位置添加一个对象
alist.insert(0, 'first')

# 返回某个对象在列表的出现次数
print(alist.count(1))

# 删除列表某个元素,如果要删除的元素不在列表中会直接报错
alist.remove('e')
print(alist)

# 删除指定索引位置的对象，并返回该对象，当不填入参数时，默认值W为-1，即删除最后一个元素，
print(alist.pop(3))
print(alist)

# 反转列表
alist.reverse()
print(alist)

# 把对象按字典序排序
blist = [3, 6, 1, 2, 4, 5]
clist = ['d', 'a', 'A', 'c']
blist.sort()
clist.sort()
print(blist, clist)

# 列表转化为字符串
# 用一个字符串当分隔符，将另外一个字符串的元素分隔开
list1 = ['a', 'b', 'c']
s1 = ''.join(list1)
# 把list中的元素按行输出
s2 = '\n'.join(list1)
print(s1, '\n', s2)
print(','.join(list1))

# 把列表的内容清空
alist.clear()
print(alist)

# ---------------------------------------------------------------------------------------------

# 例子1：删除列表中所有的4
# 注意：在for循环中可以对列表中的元素进行修改，但不能在循环中增删列表中的元素!!!
# 对列表增删元素的本质是改变了列表的长度
# python在执行"for i in list:"时会固定的获得一个可迭代对象，整个迭代的次数就已经确定下来了
# 因此在循环中增删元素就会有越界/漏值的危险
# 参考资料：https://www.zhihu.com/question/49098374

# 错误方法1
a = [1, 2, 4, 4, 5]
for i in a:
    if i == 4:
        a.remove(4)
print(a)
# [1, 2, 4, 5]
# 错误方法2 for循环中使用del删除元素会超出索引长度而报错
b = [1, 2, 4, 4, 5]
for i in range(len(b)):
    if b[i] == 4:
        # del b[i]
        pass
print(b)
# IndexError: list index out of range

# 解决方法1 使用while循环
c = [1, 2, 4, 4, 5]
i = 0
while i < len(c):
    if c[i] == 4:
        del c[i]
    else:
        i += 1
print(c)
# [1, 2, 5]
# 解决方法2 推荐使用标准写法
d = [1, 2, 4, 4, 5]
d = [i for i in d if i != 4]
print(d)
# [1, 2, 5]


# 例子2：在for循环中删除列表的后几个元素
# 注意：不能在for循环中把一个列表不断的赋值给本身

# 错误的方法：在for循环中把列表处理后又赋值给了列表本身
def func(list1):
    list1.pop()
    return list1
list1 = [1, 2, 3, 4, 5, 6, 7]
for i in range(5):
    list1 = func(list1)# 可能会造成隐藏bug
print(list1)

# 正确的方法：
# 列表类型的数据会在内部直接修改，不需要把列表赋值给本身，函数也不需要有返回值
def func(list1):
    list1.pop()
list1 = [1, 2, 3, 4, 5, 6, 7]
for i in range(5):
    func(list1)
print(list1)


