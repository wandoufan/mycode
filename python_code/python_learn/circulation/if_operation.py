# 用if-elif可以代替实现switch-case功能
command = str('other')
if command == 'open':
    print('open success')
elif command == 'save':
    print('save success')
elif command == 'delete':
    print('delete success')
else:
    print('illegal command!')


# 用序列和成员关系符可以简化上面的的操作
if command in ('open', 'save', 'delete'):
    print('%s success' % (command))
else:
    print('illegal command!')

# 使用映射对象如字典同样可以实现上面的操作，而且它的搜索类操作比if-else语句或者for循环速度快的多
dict1 = {'open': 'open success',
         'save': 'save success', 'delete': 'delete success'}
default = 'illegal command!'
print(dict1.get(command, default))

# 条件表达式（即三元操作符C?X:Y）
x, y = 3, 4
smaller = x if x < y else y
# 相当于
#if x < y:
#    smaller = x
#else:
#    smaller = y
