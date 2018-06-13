#try语句可以捕获语句范围内的异常,包括try-except，try-except-finally

#对于所有的错误的类型都可以用Exception来代替
try:
    a=1/0
except Exception as reason:
    print(reason)

#try-except语句,检测范围内一旦出现异常，剩下的语句就不会执行
try:
    a=1+'b'
except TypeError:
    print('数据类型错误！')


#导致OSError的原因可以用as reason 具体列出来
try:
    f=open('not_exist.txt','r')
    for each_line in f:
        print('each_line')
except OSError as reason:
    print('打开文件出错，错误原因：'+str(reason))

#try和多个except组合，分别对异常进行检测处理
try:
    f=open('not_exist.txt','r')
    for each_line in f:
        print('each_line')

    a=1+'b'
except TypeError:
    print('数据类型错误！')
except OSError:
    print('打开文件出错！')

#当无法确定异常类型时，可以不写错误类型
try:
    int('abc')
except:
    print('出错了！')   


#try-finally语句中无论是否异常,都可以将finally语句块的内容实现,如重要的关闭保存工作
try:
    f=open('C:/Users/xyf/Documents/python 代码/test_10/test10.txt','r')
    a=1+'b'
except:
    print('出错了！')
finally:
    #f.close()
    pass

#raise语句可以主动返回一个指定的错误类型，并可以加上自定义的错误解释
#raise TypeError('数据类型错误！')

#对于文件的操作可以使用with语句，with语句可以自动帮助用户关闭文件
try:
    with open('C:/Users/xyf/Documents/python 代码/test_10/test10.txt','r') as f:
        for each_line in f:
            print(each_line)
except:
    print('出错了！')