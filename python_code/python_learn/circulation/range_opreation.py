#内建函数range()一般和for搭配，在一定数字范围内进行循环
#range()有三种不同方法来调用：range(start,end,step),range(start,end),range(end)
#至少要提供end参数，step默认值为1,start默认值0
#注意：i的循环范围是不包括最后一个值end的！
for i in range(5):
    print(i)

for i in range(0,5):
    print(i)

for i in range(1,9,2):
    print(i)