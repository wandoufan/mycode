# 字典是python语言中唯一的映射类型，映射类型对象里hash值(键，key)和指向的对象(值，value)是一对多的关系。
# 区别：序列类型容器(列表、元组)只能用数字类型的键进行(如数值顺序的索引)访问，字典可以用字符串或数字作为键
# 字典的键必须是可哈希的，列表或其他字典都不能作为字典的键；但字典的值可以时任意数据类型
# 仅当元组中只包含数字/字符串等不可变数据时，元组才能作为字典的键
 

# 创建字典和给字典赋值,使用大括号{}来定义，字典可以为空，常见创建方法如下：
# 1.直接创建
dict1 = {'port': 80, 'color': 'yellow', 'number': 3.14}
# 2.使用dict()方法创建，方法对象内部是列表-元组或元组-列表  
dict2 = dict((['x', 1], ['y', 2], ['z', 3]))
dict2 = dict([('x', 1), ('y', 2), ('z', 3)])
# 3.使用{}.fromkeys方法创建，字典元素具有相同的值
dict3 = {}.fromkeys(('x', 'y'), -1)  

# 注意，获取字典值两种方法的区别：
# 当要取的键值在字典中不存在时，get方法会返回None或自己设定的值,而[key]会报错
# print(dict1.get('abc'))
# print(dict1['abc'])

# 更新字典
dict2['z'] = 3
print('添加：', dict2)
dict2['y'] = 0
print('修改：', dict2)
del dict2['x']
print('删除：', dict2)

# 访问字典中的值，字典的数据是无序的，不能用有序的数字索引
for key in dict1.keys():
    print('''使用dict1.keys()方法循环查看''', 'key=%s,value=%s' % (key, dict1[key]))

print('已知key,直接查看value:', dict1['port'])

for key in dict2:  # 注意：字典名后面的方法可以省略, 默认就是Key的值
    print('只需要字典名就可以循环查看', 'key=%s,value=%s' % (key, dict2[key]))

# 判断对象是否是字典的成员，返回True或False
print('port' in dict1)

# 每个键只能对应一个值，当有键发生冲突时，取最后的赋值
dict4 = {'port': 80, 'port': 8080}
print('端口号', dict4['port'])
