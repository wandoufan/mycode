
# 迭代器是一个有next()方法的对象，而不是通过索引来计数;每次迭代的结果都会被当做下次迭代的初始值；
# 可以迭代非序列类型但表现出序列行为的对象，如字典的键，一个文件的行
# 循环中需要下一个项时，调用迭代器的next()方法就可以获得；条目全部取出时返回StopIteration异常表示迭代完成
# 迭代函数iter()用来创建迭代器，单参数iter(obj)：检查对象是否为序列并迭代所有元素
# 双参数iter(func,sentinel)，重复调用func函数，直到迭代器下个值等于sentinel


#注意：可变对象在迭代时不可以进行修改删除等操作，否则会报错

# 迭代类型：序列
alist = [1, 2, 3, 4, 5]
i = iter(alist)
while True:
    try:
        print(next(i))
    except StopIteration:
        break
# 或者用下面方法
btuple = ('abc', 123, 3.14)
j = iter(btuple)
print(j.__next__())
print(j.__next__())
print(j.__next__())

# 迭代类型：字典
dict1 = {'port': 80, 'color': 'yellow', 'number': 3.14}
for key in dict1.keys():
    print('key:%s,value:%s' % (key, dict1[key]))
for value in dict1.values():
    print(value)
for item in dict1.items():
    print(item)


# 迭代类型：文件
import sys
myfile = open('C:/Users/xyf/Documents/python 代码/test_8/test8.txt', 'r')
for each_line in myfile:
    print(each_line)
