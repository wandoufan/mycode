#coding:utf-8

#subprocess模块实现shell命令相关的函数和功能,在linux中有较多的应用

#早期的Python版本中，我们主要是通过os.system()、os.popen().read()等函数来执行命令行指令的
#commands模块在python3.x中已经被废除，由subprocess模块来代替
#在新版的python中，通过subprocess模块完成命令行指令的执行

#subprocess模块中的常用函数:

import subprocess

# subprocess.run()执行指定的命令，等待命令执行完成后返回一个包含执行结果的CompletedProcess类的实例。
# CompletedProcess类的实例表示的是一个已结束进程的状态信息
# subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, shell=False, timeout=None, check=False, universal_newlines=False)

# subprocess.call()	执行指定的命令，返回命令执行状态，其功能类似于os.system(cmd)。
# subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False, timeout=None)

# subprocess.check_call() 执行指定的命令，如果执行成功则返回状态码，否则抛出异常。其功能等价于subprocess.run(..., check=True)。
# subprocess.check_call(args, *, stdin=None, stdout=None, stderr=None, shell=False, timeout=None)

# subprocess.check_output() 执行指定的命令，如果执行状态码为0则返回命令执行结果，否则抛出异常。
# subprocess.check_output(args, *, stdin=None, stderr=None, shell=False, universal_newlines=False, timeout=None)

# subprocess.getstatusoutput()接收字符串格式的命令，执行命令并返回执行结果，其功能类似于os.popen(cmd).read()和commands.getoutput(cmd)。
# 返回结果是元组(status,result),status为int类型，result为string类型
# 例如subprocess.getstatusoutput('pwd')---返回结果为(0,'/home/user')

# subprocess.getoutput()执行cmd命令，返回一个元组(命令执行状态, 命令执行结果输出)，其功能类似于commands.getstatusoutput()。
# subprocess.getoutput(cmd)

# 函数中参数说明：

# args： 要执行的shell命令，默认应该是一个字符串序列，如['df', '-Th']或('df', '-Th')，也可以是一个字符串，如'df -Th'，但是此时需要把shell参数的值置为True。
# shell： 如果shell为True，那么指定的命令将通过shell执行。如果我们需要访问某些shell的特性，如管道、文件名通配符、环境变量扩展功能，这将是非常有用的。当然，python本身也提供了许多类似shell的特性的实现，如glob、fnmatch、os.walk()、os.path.expandvars()、os.expanduser()和shutil等。
# check： 如果check参数的值是True，且执行命令的进程以非0状态码退出，则会抛出一个CalledProcessError的异常，且该异常对象会包含 参数、退出状态码、以及stdout和stderr(如果它们有被捕获的话)。
# stdout, stderr：
# run()函数默认不会捕获命令执行结果的正常输出和错误输出，如果我们向获取这些内容需要传递subprocess.PIPE，然后可以通过返回的CompletedProcess类实例的stdout和stderr属性或捕获相应的内容；
# call()和check_call()函数返回的是命令执行的状态码，而不是CompletedProcess类实例，所以对于它们而言，stdout和stderr不适合赋值为subprocess.PIPE；
# check_output()函数默认就会返回命令执行结果，所以不用设置stdout的值，如果我们希望在结果中捕获错误信息，可以执行stderr=subprocess.STDOUT。
# input： 该参数是传递给Popen.communicate()，通常该参数的值必须是一个字节序列，如果universal_newlines=True，则其值应该是一个字符串。
# universal_newlines： 该参数影响的是输入与输出的数据格式，比如它的值默认为False，此时stdout和stderr的输出是字节序列；当该参数的值设置为True时，stdout和stderr的输出是字符串。