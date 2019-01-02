#coding:utf-8

#python 中的traceback模块用来追踪显示系统运行中出现的错误的具体位置

import traceback


#用try-except语句只能知道错误类型，却不知道具体哪一行报错
try:
	a=1/0
except Exception as reason:
	print(reason)


#用traceback.print_exc()直接把错误打印出来
list1=[1,2,3]

try:
	print(list1[4])
except Exception as e:
	traceback.print_exc()


#用traceback.format_exc()返回错误的字符串

def test():
	list1=[1,2,3]
	try:
		print(list1[4])
	except Exception as e:
		return traceback.format_exc()

print(test())

