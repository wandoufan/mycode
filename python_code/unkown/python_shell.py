# 关于python中如何调用shell命令：
https://blog.csdn.net/qinglu000/article/details/52302560


# # Python经常被称作“胶水语言”，因为它能够轻易地操作其他程序，轻易地包装使用其他语言编写的库。
# 今天我们就讲解其中的一个方面，用Python调用Shell命令。用Python调用Shell命令有如下几种方式:


# # os.system("The command you want"). 这个调用相当直接，且是同步进行的，
# 程序需要阻塞并等待返回。返回值是依赖于系统的，直接返回系统的调用返回值，
# 所以windows和linux是不一样的

# # os.popen(command[,mode[,bufsize]]),图中是一个例子. 可以看出，
# popen方法通过p.read()获取终端输出，而且popen需要关闭close().当执行成功时，
# close()不返回任何值，失败时，close()返回系统返回值. 可见它获取返回值的方式和os.system不同。


# # 使用commands模块，图中是一组例子。根据你需要的不同，commands模块有三个方法可供选择。
# getstatusoutput, getoutput, getstatus。


# # 但是，如上三个方法都不是Python推荐的方法，而且在Python3中其中两个已经消失。
# Python文档中目前全力推荐第四个方法，subprocess! subprocess使用起来同样简单：


# # 直接调用命令，返回值即是系统返回。shell=True表示命令最终在shell中运行。
# Python文档中出于安全考虑，不建议使用shell=True。建议使用Python库来代替shell命令，
# 或使用pipe的一些功能做一些转义。官方的出发点是好的，不过真心麻烦了很多， so....   
# 如果你更关注命令的终端输出，可以如下图这样操作, 同样很简单.

