# coding:utf-8

# Cython是一个快速生成Python扩展模块的编译器，语法层面上属于是Python语法和C语言语法的混合，
# 当Python性能遇到瓶颈时，Cython直接将C的原生速度植入Python程序，这样使Python程序无需使用C重写，
# 能快速整合原有的Python程序，这样使得开发效率和执行效率都有很大的提高

# 和python代码不同，Cython代码必须被编译，通常存在两种情况：
# 1.一个.pyx文件被Cython编译成了一个.c文件，其中.pyx文件包含python本身的代码
# 2.一个.c文件被C编译器编译成了一个.so文件(windows平台上是.pyd文件)，编译后的文件可以
# 直接被导入python会话中，这部分功能由distutils或setuptools来实现

# 构建Cython代码的几种常用方法：
# 1.写一个distutils或setuptools,即setup.py(最常用且推荐的方式)
# 2.使用Pyximport,像导入.py文件一样导入Cython的.pyx文件(在后台使用distutils来编译和构建)
# 这个方法比写一个setup.py要简单，但是不够灵活
# 3.运行Cython命令行，手动的从.pyx文件中产生.c文件，然后手动将.c文件编译为共享对象库或
# 适合导入Python的动态链接库(手动操作常用于调试和测试)
# 4.使用jupyter-notebook，可以在线快速创建Cython代码 

# 参考文档：
# https://www.cnblogs.com/freeweb/p/6548208.html
# http://cython.org/
# http://docs.cython.org/en/latest/src/quickstart/build.html

# ------------------------------------------------------------------------

# cython编译步骤：
# 1.目标python代码hello.pyx(.pyx是cython格式的文件)
def test(num):
    k = 100
    for i in range(num):
        k = k * i
    return k

# 2.同目录下写一个setup.py脚本(一或二都可以)来对目标python代码hello.pyx进行编译
# 脚本中各个参数的含义？？？
# 脚本一
from distutils.core import setup
from Cython.Build import cythonize
setup(name='Hello world app',
      ext_modules=cythonize("hello.pyx"))
# 脚本二
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
ext_modules = [Extension('hello', [
        'hello.pyx', 'hello.pxd',
            ])]
setup(
    name = 'Hello world app',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules)

# 3.如果是脚本一：运行命令'python setup.py build'来进行编译
# 如果是脚本二：运行命令'python setup.py build_ext --inplace'来进行编译
# 然后会在当前目录下会生成hello.c文件(hello.pyx转换过来的C代码)和一个build目录
# build目录中有hello.cpython-36m-x86_64-linux-gnu.so文件(python经过cython编译之后的模块)
# 注意：.so文件就是经过cython编译后的用来替代原来.pyx文件的，即编译产生.so文件后实际就不再需要.pyx文件了
# 一定要把.so文件从build目录移动到和.pyx文件同一目录下，否则其他调用它的代码会找不到它

# 4.在其他python代码或会话中直接调用hello.pyx中的函数
from hello import test
from datetime import datetime
if __name__ == '__main__':
    time_1 = datetime.now()
    for num in range(30000):
        test(num)
    time_2 = datetime.now()
    print('run time:', time_2 - time_1)

# 纯python代码直接运行的效果：
# run time: 0:00:17.871023
# 用cython编译后运行的效果：
# run time: 0:00:09.096707

# ------------------------------------------------------------------

# 进一步提升性能：
# 简单的用cython对代码进行编码可以提高35%的性能，但如果在代码中声明变量类型可以提升更大的性能
# 注意：尤其是在for循环中被多次调用的变量在声明变量类型后对性能的提升更大
# 加入静态变量类型后的hello.pyx代码
def test(int num):
    cdef int i# 用cdef关键字来声明C语言中变量类型和函数
    cdef double k
    k = 100
    for i in range(num):
        k = k * i
    return k
# 加入变量类型后的效果：
# run time: 0:00:00.374669

# 附：C语言中的数值变量类型及其表示范围
# 短整型short： -32768 ~ + 32767 (2 Bytes)
# 无符号短整型unsigned short： 0 ~ 65536 (2 Bytes)
# 整型int： -2147483648 ~ +2147483647 (4 Bytes)
# 无符号整型unsigned int： 0 ~ 4294967295 (4 Bytes)
# 单精度浮点型float：3.4 x 10^（-38）~ 3.4 x 10^（+38） 
# 双精度浮点型double：1.7 x 10^（-308）~ 1.7 x 10^（+308） 
