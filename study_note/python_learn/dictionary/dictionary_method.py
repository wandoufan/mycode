# 关于dict的各种方法

dict1 = {'a': 1, 'b': 2, 'c': 3}

# 复制字典
dict3 = dict1.copy()
# print(dict3)

# 清空字典内容
dict3.clear()
# print(dict3)

# 创建新字典,第一个参数为键，第二个参数为值
dict2 = dict.fromkeys(('x', 'y', 'z'), 1)
# print(dict2)

# 返回字典键-值对的数目
print('字典长度:', len(dict1))

# 返回对象的哈希值(仅当对象可以作为字典键时才不报错，可以用来判读对象是否可哈希)
print('对象hash值：', hash('a'))
print('值相等的数字hash值相同：', hash(1) == hash(1.0))
# hash()函数返回一个整数值作为对象的hash值，其中相同数值的浮点型和整型数的hash值一样

# 返回字典中所有的键,注意返回类型不是列表,还需要用list方法转换为列表
print(dict1.keys())

# 将键按字典序排序在输出
dict4 = dict.fromkeys(('r', 'a', 'z', 'k'), -1)
print('按字典序的键', sorted(dict4.keys()))

# 返回字典中所有的值,注意返回类型不是列表,还需要用list方法转换为列表
print(dict1.values())

# 返回字典中所有的键值元组
print(dict1.items())
# 常用写法：
for key ,value in dict1.items():
	print(key, value)

# 查询并返回指定键的对象，如果字典中不含给定键，则返回自定义的值,default返回参数为None
print('查询的值为：', dict1.get('e', 'not exist this key'))

# 查询并返回指定键的值，如果字典中不含给定键，则添加该键-值
print('查询的值为：', dict1.setdefault('b'))
print('添加的值为：', dict1.setdefault('d', 4))
# print(dict1)

# 删除指定的键-值，并返回对应的值;如果给定的键不存在，则返回自定义的值
print('删除的值为：', dict1.pop('a', 'not exist this key'))
# print(dict1)

# 将dict1的内容添加到dict2中；如果两个字典的键有重复，以新添加的值为准
dict2.update(dict1)
print(dict2)

# ----------------------------------------------------------------------------------

# 例子1：给字典中的键和值后边都加上test字段
dict1 = {'a': 'A', 'b': 'B', 'c': 'C'}
def func1(a):
    return a + 'test'
def func2():
    return {func1(k): func1(v) for k, v in dict1.items()}
print(func2())

# 例子2：以列表中的元素为key,出现次数为value写入一个字典中
# 方法1
list1 = ['a', 'b', 'd', 'a', 'c', 'd', 'a']
dict1 = {}
set1 = set(list1)
list2 = list(set1)
dict1 = {}.fromkeys(list2, 0)
for word in list1:
	dict1[word] = dict1[word] + 1
print(dict1)
# 方法2
list1 = ['a', 'b', 'd', 'a', 'c', 'd', 'a']
dict1 = {}
for word in list1:
	dict1[word] = dict1.get(word, 0) + 1
print(dict1)
# 方法3
from collections import Counter
list1 = ['a', 'b', 'd', 'a', 'c', 'd', 'a']
c = Counter(list1)
print(dict(c))

# 例子3： 需要在循环遍历过程中对字典的某些不符合条件的键值对进行删除或者修改
# 错误的写法:
# 字典类型不支持在迭代中直接删除键值对(可以修改值)，否则会报错：dictionary changed size during iteration
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for word in dict1:
    if dict1[word] < 3:
        # del dict1[word]
        dict1[word] = 5
print(dict1)
# 正确的写法：
# 方法1：把字典转换为列表类型就可以在循环过程中直接删除
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for word in list(dict1):
    if dict1[word] < 3:
        del dict1[word]
print(dict1)
# 方法2：在列表中循环
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
keys = list(dict1.keys())
for key in keys:
    if dict1[key] < 3:
        del dict1[key]
print(dict1)

# 例子4：计算字典中所有值的和
dict1 = {'a':1,'b':2,'c':3,'d':4}
# 不推荐的写法，比较麻烦
num1 = 0
for v in dict1.values():
    num1 = num1 + v
print(num1)
# 推荐的写法(灵活运用sum函数)
num2 = sum(v for v in dict1.values())
print(num2)

# 例子5：将两个字典按键进行合并
stop_word_dict1 = {'a':3,'b':2,'c':1,'d':4}
stop_word_dict2 = {'b':3, 'c':2, 'e':2}
for k2 in stop_word_dict2.keys():
    stop_word_dict1[k2] = stop_word_dict2[k2] + stop_word_dict1.get(k2, 0)
print(stop_word_dict1)

# 例子5：将字典按照value大小进行排序输出
dict1 = {'a':3,'b':2,'c':1,'d':4}
sort_list = sorted(dict1.items(), key=lambda x:x[1], reverse=True)
# 备注：sorted函数的输出结果是以元组为元素的列表，可以直接再转换回字典结构
dict2 = dict(sort_list)
print(dict2)
