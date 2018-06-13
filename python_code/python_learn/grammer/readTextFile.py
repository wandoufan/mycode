#-*- coding: UTF-8 -*-
print('read and display text file!')

#get filename
fname = input('enter filename:')  #打开相对路径的文件
#fname = 'C:/Users/xyf/Desktop/'+input('enter filename:') #打开绝对路径的文件
#路径用/或者\\，不能用\
print('\n')

#attempt to open file for reading
try:
	 word=open(fname,'r')
except IOError as e:
	print('e') #e为系统的默认报错内容，也可以自定义报错
else:
	#display contents to the screen
	for eachline in word:
		print(eachline)
	word.close()	