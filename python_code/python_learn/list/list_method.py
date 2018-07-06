#关于list函数的各种方法

alist=[1,2,3,4,'a','b','c','d']
blist=['x','y','z']

#查看返回对象在列表中的索引,如果对象没有在列表中则会报错
print(alist.index('b'))

#在列表末尾添加一个对象
alist.append('e')
print(alist)

#在列表尾部追加一个列表
alist.extend(blist)
print(alist)

#在列表指定索引位置添加一个对象
alist.insert(0,'first')

#返回某个对象在列表的出现次数
print(alist.count(1))

#删除列表某个元素
alist.remove('e')
print(alist)

#查找列表指定范围中是否有指定的对象，若有返回索引值，若没有报错
print(alist.index('a',1,9))

#删除指定索引位置的对象，并返回该对象，当不填入参数时，默认值W为-1，即删除最后一个元素，
print(alist.pop(3))
print(alist)

#反转列表
alist.reverse()
print(alist)

#把对象按字典序排序
blist=[3,6,1,2,4,5]
clist=['d','a','A','c']
blist.sort()
clist.sort()
print(blist,clist)

#列表转化为字符串
#用一个字符串当分隔符，将另外一个字符串的元素分隔开
list1=['a','b','c']
s1=''.join(list1)
#把list中的元素按行输出
s2='\n'.join(list1)
print(s1,'\n',s2)
print(','.join(str4))
print(str4.join(str1))
