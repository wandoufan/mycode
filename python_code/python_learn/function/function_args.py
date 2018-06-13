#*args和**args都是可变参数，适用于函数的参数不确定的时候
#*args可以看做是多个变量组成的list,**args可以看做是个字典

def funargs(*args): #可以传入任意数量个参数（包括零个）
    for i in args:
        print(i)

funargs(1,2,3,4,5)  #传入5个参数


#关于**kwargs与位置参数、*args、默认参数混着用的问题：（注意顺序）
#顺序必须是位置参数、*args、**kwargs，不然就会报错

#三者顺序是:位置参数、默认参数、*args
def foo_1(x,y=1,*args):
     pass
foo_1(1,2,3,4,5) # 其中的x为1，y=1的值被2替换，3,4,5都给args，即args=(3,4,5)


#三者顺序是:位置参数、*args、默认参数
def foo_2(x,*args,y=1):
     pass
foo_2(1,2,3,4,5) # 其中的x为1，2,3,4,5都给args，即args=(2,3,4,5),y始终为1


