# try语句可以捕获语句范围内的异常,包括try-except，try-except-finally，raise


# 对于所有的错误的类型都可以用Exception来代替
try:
    a = 1 / 0
except Exception as reason:
    print(reason)

# try-except语句,检测范围内一旦出现异常，try剩下的语句就不会执行，转而执行except部分预先定义的操作
try:
    a = 1 + 'b'
except TypeError:
    print('数据类型错误！')


# 导致OSError的原因可以用as reason 具体列出来
try:
    f = open('not_exist.txt', 'r')
    for each_line in f:
        print('each_line')
except OSError as reason:
    print('打开文件出错，错误原因：' + str(reason))

# try和多个except组合，分别对异常进行检测处理
try:
    f = open('not_exist.txt', 'r')
    for each_line in f:
        print('each_line')

    a = 1 + 'b'
except TypeError:
    print('数据类型错误！')
except OSError:
    print('打开文件出错！')

# 当无法确定异常类型时，可以不写错误类型
try:
    int('abc')
except:
    print('出错了！')


# try-finally语句中无论是否异常,都可以将finally语句块的内容实现,如重要的关闭保存工作
try:
    f = open('C:/Users/xyf/Documents/python 代码/test_10/test10.txt', 'r')
    a = 1 + 'b'
except:
    print('出错了！')
finally:
    # f.close()
    pass

# raise语句可以主动返回一个指定的错误类型，并可以加上自定义的错误解释
if True:
    # raise IndexError('超出列表长度范围了')
    pass

# 对于文件的操作可以使用with语句，with语句可以自动帮助用户关闭文件
try:
    with open('C:/Users/xyf/Documents/python 代码/test_10/test10.txt', 'r') as f:
        for each_line in f:
            print(each_line)
except:
    print('出错了！')

# 例子1：try-except经常和循环搭配使用，即使循环中某次出现问题还可以继续执行完循环操作
for i in range(10):
    try:
        print(i)
        if i == 5:
            a = i + 'b' # 设置错误
    except:
        print('i=%s时出错了' %i)