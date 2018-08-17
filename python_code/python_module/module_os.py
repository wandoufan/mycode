# coding:utf-8

# OS即operating system，主要实现对文件相关的操作
# OS模块会根据操作系统自动选择对应的正确模块,使程序运行与操作系统实现无关

# OS模块中关于文件/目录常用的函数方法
import os

# getcwd()函数用来获得应用程序当前的工作目录的路径(current work directory)
print(os.getcwd())

# chdir(path)函数用来改变当前工作目录
os.chdir('C:/Users/xyf/Documents/python 代码/test_9')
print(os.getcwd())
os.chdir('C:/Users/xyf/Documents/python 代码/test_10')
# 特别地，os.chdir(..)返回上一层目录

# listdir(path='.')函数返回包含指定目录中所有文件和子目录的列表
# path参数可以指定列举目录，默认值为'.'，代表当前目录，也可以用'..'代表上一层目录
print(os.listdir())
print(os.listdir('C:/Users/xyf/Documents/python 代码'))
print(os.listdir('.'))
print(os.listdir('..'))

#mkdir(path)函数用来创建文件夹，如果文件夹存在，则返回FileExistError异常
os.mkdir('C:/Users/xyf/Documents/python 代码/file_old')
os.mkdir('file_new')
print(os.listdir())

#makedirs(path)函数可以用于创建多层文件夹,如果文件夹存在，则返回FileExistError异常
os.makedirs('./a/b/c')

#remove(path)函数删除指定的文件(非文件夹)，rmdir(path)删除空文件夹，removedirs(path)删除空的多层文件夹
#删除函数删除时遇到目录非空就会返回异常
#注意：删除非空文件夹使用shutil模块的shutil.rmtree(path)方法
os.remove('C:/Users/xyf/Documents/python 代码/test_10/file_new/a.txt')
os.rmdir('C:/Users/xyf/Documents/python 代码/test_10/a/b/c')
os.removedirs('C:/Users/xyf/Documents/python 代码/test_10/a/b/c')


#rename(old,new)函数重命名文件或文件夹
os.rename('file_old','file_new')

#system()函数用于执行脚本，以及调用操作系统自带的各种小工具,如计算器
os.system(shell_cmd)
os.system('calc')

#walk(top_path)函数遍历top参数指定路径下的所有子目录，并返回三元组(路径，包含目录，包含文件)
for i in os.walk('C:/Users/xyf/Documents/python 代码/test_10'):
    print(i)

#以下是os.path模块中路径相关的函数
#dirname()函数获取文件目录，即去掉路径中的文件名
print(os.path.dirname('C:/Users/xyf/Documents/python 代码/test_10/test10.txt'))

#basename()函数获取文件名，即去掉路径中的文件目录部分
print(os.path.basename('C:/Users/xyf/Documents/python 代码/test_10/test10.txt'))

#join(path1[,path2[,...]])函数将两个路径组合成完整的路径
print(os.path.join('C:/Users/xyf/Documents/python 代码/test_10/','a/b/test10.txt'))

#split(path)函数分割路径和文件名，但是无法区分文件是否存在，默认将最后一个分开
print(os.path.split('C:/Users/xyf/Documents/python 代码/test_10/test10.txt'))

#splitext(path)函数分割文件名和扩展名
print(os.path.splitext('C:/Users/xyf/Documents/python 代码/test_10/test10.txt'))

#getsize(file)函数返回文件的大写，单位字节
print(os.path.getsize('C:/Users/xyf/Documents/python 代码/test_10/test10.txt'))

#abspath(path)函数返回文件的绝对路径
print(os.path.abspath('C:/Users/xyf/Documents/python 代码/test_10/test10.txt'))

#realpath(__file__)函数获取当前执行脚本的路径，且路径名中包含脚本程序的名字，其中__file__为内置属性
print(os.path.realpath(__file__))
#os.path.dirname(os.path.realpath(__file__))和os.getcwd()的功能类似，一般都是获取脚本程序所在的目录，即当前工作目录
#区别在于：realpath获取的是该方法所在脚本的路径；getcwd()获得的是当前执行脚本所在的路径，无论从哪里调用该方法


#getatime(),getctime(),getmtime()函数用来获取文件的最近访问时间，创建时间，修改时间
#默认返回值是浮点型秒数，需要用time模块的localtime()函数换算
import time
print(time.localtime(os.path.getatime('test10.txt')))
print(time.localtime(os.path.getctime('test10.txt')))
print(time.localtime(os.path.getmtime('test10.txt')))



#以下是os.path模块中函数返回值为Ture或False的
#exists()函数判断路径是否存在
print(os.path.exists('C:/Users/xyf/Documents/python 代码/test_10/test10.txt'))

#isabs()函数判断路径是否为绝对路径
print(os.path.isabs('C:/Users/xyf/Documents/python 代码/test_10/test10.txt'))

#isdir()函数判断路径是否存在且是一个目录
print(os.path.isdir('C:/Users/xyf/Documents/python 代码/test_10'))

#isfile()函数判断路径是否存在且是一个文件
print(os.path.isfile('C:/Users/xyf/Documents/python 代码/test_10/test10.txt'))

#getenv()函数读取环境变量,putenv()函数设置环境变量
print(os.getenv('PATH'))



#以下是支持路径操作中常用到的一些定义
print(os.curdir)#代表当前目录，相当于'.'
print(os.listdir(os.curdir))
print(os.pardir)#代表上级目录，相当于'..'
print(os.listdir(os.pardir))
print(os.sep)#代表当前操作系统的路径分隔符
print(os.name)#代表当前操作系统的名字


#os._exit()会直接退出程序，并不产生异常
#sys.exit(n)表示退出程序，因此前面的部分执行，后边的部分就跳过了
#参数n为0时表示正常退出，不为0时表示有问题，会产生一个SystemExit异常,异常可以被捕获并反映退出原因
#一般来说os._exit()用于在子线程中退出，sys.exit(n)用于在主线程中退出
#sys.exit(1)
os._exit(0)

