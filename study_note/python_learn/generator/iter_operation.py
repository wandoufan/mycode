# 主要记录python中的迭代器

# 迭代器是遍历访问集合元素的一种方式，从第一个元素开始直到所有元素被访问结束，迭代只能向前不能后退
# 迭代的集合对象可以是序列类型的列表、元组、字符串等，也可以是非序列类型的集合、字典、文件句柄等
# 注意：可变对象在迭代时不可以进行修改删除等操作，否则会产生错误

# 生成器和迭代器的区别：
# 生成器可以看做特殊的迭代器，生成器函数的返回结果是一个迭代器对象
# 生成器函数中使用了yield关键字


# 迭代器有两个基本方法：iter()和next()
set1 = set('abcde')
# iter()方法用来创建迭代器对象，每次迭代的结果都会被当做下次迭代的初始值
it = iter(set1)
while True:
    try:
        # next()方法用来逐个遍历迭代器中的对象，循环中需要下一个项时，调用迭代器的next()方法就可以获得
        print(next(it))
    except:
        # 出现StopIteration异常表示迭代完成，防止出现无限循环的问题
        StopIteration
        break

# -----------------------------------------------------

# 示例1.迭代类型：序列
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

# 示例2.迭代类型：字典
dict1 = {'port': 80, 'color': 'yellow', 'number': 3.14}
for key in dict1.keys():
    print('key:%s,value:%s' % (key, dict1[key]))
for value in dict1.values():
    print(value)
for item in dict1.items():
    print(item)

# 示例3.迭代类型：文件
# import sys
# myfile = open('C:/Users/xyf/Documents/python 代码/test_8/test8.txt', 'r')
# for each_line in myfile:
#     print(each_line)
