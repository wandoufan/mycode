# 关于集合的各种方法

s1 = set('bbaaac')
s2 = frozenset('aaaxxxzzzyyy')
s3 = frozenset('aaacbb')
s4 = set('bbaaa')
s5 = set('abcdefg')

# 使用于所有类型的集合方法:
print('子集', s4.issubset(s1))
print('超集', s4.issuperset(s1))
print('并集', s1.union(s2))
print('交集', s1.intersection(s2))
print('差集', s1.difference(s2))
print('异或', s1.symmetric_difference(s2))

# 仅适用于可变集合类型方法，注意不可变集合不可以添加删除成员，否则会报错
s1.add('d')
print('添加单个集合成员', s1)
s1.update('efgh')
print('添加多个集合成员', s1)
s1.remove('a')  # 如果对象不在集合内，会报错
print('删除单个集合成员', s1)
s1 = s1 - set('bcd')
print('删除多个集合成员', s1)
s1.discard('w')  # 如果对象不在集合内，不会报错
print('删除集合指定的成员', s1)
print('删除并返回集合中任意一个对象', s1.pop(), s1)

s4.intersection_update(s5)
print('s4变为s4,s5的交集',s4)
s5.difference_update(s4)
print('s5变为s5,s4的差集',s5)
s5.symmetric_difference_update(s4)
print('s5变为s4,s5的异或集',sorted(s5))

# ----------------------------------------------------------------------------------------
# 例子1：在for循环中对集合set进行添加修改
# 错误方法：在for循环中把集合处理后又赋值给集合本身
def func(set1, i):
    set1.add(i)
    return set1

set1 = set('abcde') 
for i in range(5):
    set1 = func(set1, i)# 可能会造成隐藏bug
print(set1)

# 正确的方法：
# 集合类型的数据会在内部直接修改，不需要把集合赋值给本身，函数也不需要有返回值
def func(set1, i):
    set1.add(i)

set1 = set('abcde')    
for i in range(5):
    func(set1, i)
print(set1)
