#利用列表的容器性和可更改性来构建一个堆栈,用存储和取回输入的字符串

#定义一个空列表
stack=[]

#定义输入函数
def push():
	a=str(input('enter new string:'))
	stack.append(a)

#定义输出函数
def pop_it():
	if len(stack)==0:
		print('cannot pop from a empty stack')
	else:
		print(stack.pop(-1))
#定义展示函数
def viewstack():
	print(stack)

#定义控制菜单主函数
def showmenu():
	user_input=input('please input your command:')
	if user_input=='push':
		push()
	elif user_input=='pop':
		pop_it()
	elif user_input=='show':
		viewstack()
	else:
		print('illegal command!')


#定义循环函数，让用户可以一直输入命令
while True:
	showmenu()
