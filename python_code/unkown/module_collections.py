# coding:utf-8

# python自带了dict、set、list、tuple等常用容器类型
# collections库额外提供了一些容器类型，包含：
# OrderedDict类：排序字典，是字典的子类
# namedtuple()函数：命名元组，是一个工厂函数
# Counter类：为hashable对象计数，是字典的子类
# deque：双向队列
# defaultdict：使用工厂函数创建字典，使不用考虑缺失的字典键


from collections import Counter

# 以列表中的元素为key,出现次数为value写入一个字典中：

# 方法1：
list1 = ['a', 'b', 'd', 'a', 'c', 'd', 'a']
c = Counter(list1)
print(c['a'])
print(dict(c))

# 方法2:
list1 = ['a', 'b', 'd', 'a', 'c', 'd', 'a']
dict1 = {}
set1 = set(list1)
list2 = list(set1)
dict1 = {}.fromkeys(list2, 0)
for word in list1:
    dict1[word] = dict1[word] + 1
print(dict1)

# 方法3:
list1 = ['a', 'b', 'd', 'a', 'c', 'd', 'a']
dict1 = {}
for word in list1:
    dict1[word] = dict1.get(word, 0) + 1
print(dict1)