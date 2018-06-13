
def displayNumType(num):#定义一个新函数来判断并输出数值对象的类型
	print(num,'is')
	if isinstance(num,(int,float,complex)):
		print('a number of type:',type(num).__name__)#type()后面的__name__参数可以将结果显示更简洁
	else:
		print('not a number at all !')

displayNumType(-69)
displayNumType(999999999999999999999999999)
displayNumType(98.6)
displayNumType(-5.2+1.9j)
displayNumType('xxx')


#isinstance用来判断对象是否是某种类型，第一个参数是对象，第二个参数是指定的数据类型，
#如果是返回True,如果不是返回False
num='hello'
print(isinstance(num,(str,list)))