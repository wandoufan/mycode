def displayNumType(num):#定义一个新函数判断数字的类型并输出结果
	print(num,'is')
	if type(num)==type(2):
		print('an integer')
	elif type(num).__name__==type(3.14).__name__:
		print('an float')
	elif type(num)==type(2-3j):
		print('an complex')
	else:
		print('not a number at all!')


displayNumType(-64)
displayNumType(3.76)
displayNumType(2-3j)
displayNumType('xxfj')