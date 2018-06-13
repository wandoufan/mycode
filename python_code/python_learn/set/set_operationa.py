# 集合(set)是python的一种基本数据类型，没有特别的语法格式，字典的数据是无序的
# 可变集合可以添加和删除元素，不可变集合不可以改变
# 可变集合不是可哈希的，只有不可变集合可以作为字典的键或集合的一个成员

# 集合的创建只能用集合的工厂方法可变集合set(),不可变集合frozenset()
s1 = set('bbaaac')
s2 = frozenset('aaaxxxzzzyyy')
s3 = frozenset('aaacbb')
s4 = set('bbaaa')
s5 = set('abcdefg')

print(sorted(s1))
print(s2)

# 计算集合长度
print('集合的长度是按集合中字符的种类计算，重复的不算', len(s1) == len(s2))

# 集合等价/不等价
print('仅字符顺序不同的两个集合是相同的', s1 == s3)
print('大的集合是小的集合的超集', s1 > s4)

# 集合类型操作符(包含可变和不可变)
# 注意：当两个集合的可变类型不一致时，最终操作结果以左边的集合为准
print('并集', s1 | s2)
print('交集', s2 & s1)
print('差集', s1 - s2)
print('异或', s2 ^ s1)  # 异或：只属于s1或s2的元素

# 集合类型操作符(仅适用于可变的类型)
# 实际测试时，用操作符不可变类型也可以改变？？？？？
s2 |= set(s1)
print('s2变为s1,s2的并集',s2)
s1 &= set(s4)
print('s1变为s1,s4的交集',s1)
s5 -= set(s4)
print('s5变为s5-s4的差集',s5)
s5 ^= set(s2)
print('s5变为s5,s2的异或集',s5)


# 访问集合成员(集合本身是无序的，既没有数字索引也没有键，只能通过for循环迭代访问)
for i in s1:
    print(i)

# 判断元素是否是集合成员
print('a' in s1)

# 集合会自动删除重复的元素，利用这一特性可以快速除去列表中重复的元素
alist=[1,2,3,4,1,2,3,1,2,1]
bset=set(alist)
alist=list(bset)
print('去重后的列表',alist)