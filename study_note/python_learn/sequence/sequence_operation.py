# 主要记录序列对象共有的方法、函数、属性
# 字符串、列表和元组均为序列类型的数据


# in,not in 判断成员关系
alist=[1,2,3,4,5,6,7,8,9]
blist=[7,8,'man']
clist=[1,2,3,4]
print('apple' in alist)
print(1 not in alist,'\n')

# 序列的切片操作 list[start:end:step]
print(alist[0]) #第一个元素
print(alist[-1]) #最后一个元素
print(alist[1:3]) #第二个元素到第三个元素,注意不包括list[3]
print(alist[2:]) #从第三个元素到最后一个元素
print(alist[-2:]) # 注意：输出后两位！！！
print(alist[1:-1]) #从第二个元素到最后一个元素
print(alist[-3]) #倒数第三个元素
print(alist[2-3]) #2-3为-1，即最后一个元素
print(alist[::-1]) #输出相反序列
print(alist[::2]) #以2为步长的正向序列，即隔一个取一个
print(alist[::-2]) #以2为步长的逆向序列

# 用alist.append后缀参数可以直接在列表后面添加内容
alist.append('lady')
alist.append(alist[0]+6)
print(alist,'\n')

# 将序列重复n次
print(blist*3)

# 连接操作符+
print(alist+blist)

# 输出序列长度
print('序列长度是',len(alist))


# 与序列有关的四个内建函数
# 1.sorted()函数按字典序排序输出
print(sorted(clist))

# 2.reversed()反转函数，逆序输出
for t in reversed(clist):
    print(t)

# 3.enumerate()列举函数，顺序输出
for i,t in enumerate(clist):
    print(i,t)

# 4.zip()组合函数
list1=['big','blue','apple']
list2=['small','yellow','banana']
for i,j in zip(list1,list2):
    print('%s,%s' % (i,j))