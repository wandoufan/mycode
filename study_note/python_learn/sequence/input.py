#input输入函数，在cmd命令提示符下运行

#特别的，一次输入多个数据，中间用空格隔开
#m,n = map(int,input().split())

#例1：计算圆的面积
print('请输入半径r')

r=int(input('r='))#将输入的数据类型由字符转化为整型数字

print('面积为',3.14*(r**2),'\n')

#例2：判断输入的数据类型
print('请任意输入数据')

a=input()

print('数据类型是',type(a).__name__)

#例3：判断输入用户名字的长度
user_input=input('enter your name:')

print('the length of your name is :',len(user_input))

#例4：判断输入的对象是否是列表的元素，若是输出索引位置
alist=[1,2,3,4,'a','b','c']

b=input('输入任意对象')
if b in alist:
	print('索引位置是：',alist.index(b))
else:
	print('不是列表元素')


