#python 中with open as 
#有一些任务，可能需要事先设置，事后做清理工作，常用于打开文件的部分

#文件处理中可能会读文件时出错，或者事后忘记关闭文件句柄

f=open('a.txt','r')
try:
	data=f.read()
finally:
	f.close()

#但是用try-except处理代码会冗长，with语法可以更简洁的处理
with open('a.txt','r') as f:
	data=f.read()

print(data)

