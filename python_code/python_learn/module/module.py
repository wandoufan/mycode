# 模块module是编写封装好的程序，自己编写的.py文件放在Python安装目录下就可以调用模块
# sys.path可以用来设置搜索模块时的目录路径
# 目录：C:\Users\xyf\AppData\Local\Programs\Python\Python36-32\Lib
# 命名空间(Namespace)表示标识符(identifier)的可见范围
# 每个模块都会独立维护一个命名空间，调用模块中函数时应将模块名加在前面


# 三种调用模块的方法，知悉~
# 1.import 模块名
import hello
hello.sayhello()
# 2.from 模块名 import 类名 （导入模块中的一个类，而不是导入整个模块，可以使代码更精简）
from hello import Hi
hi = Hi()
hi.sayhi()
# 3.import 模块名 as 新名字，可以给导入的命名空间替换一个新的名字,适用用原模块名字复杂
import hello as world
world.sayhello()

# 特别地，如果调用文件和被调用的模块不在同一目录下，调用时要加上路径
# 例如，当hello模块在当前目录中的a目录中的b目录下时，即./a/b/hello.py
from a.b.hello import Hi


# 表明当前模块是主模块，相当于void main(),由它来调用系统的其他模块;
# 如果模块是被直接执行的,'__name__'属性的值为'__main__';
# 如果模块是被其他模块导入的，'__name__'属性的值为模块的名字
def test():
    pass
if __name__ == '__main__':
    test()

# 模块想要被搜索到并调用，需要放在预定义好的路径中，路径可以通过sys.path方法查看
# 模块最好放在site_packages目录下，该目录用来存放模块的
import sys
# print(sys.path)

# reload(module)函数用于重新加载之前已经载入的模块
# reload()函数一般用于原模块有变化等特殊情况，且被reload的模块之前需要已经import过
# 常用情况：(注意在新版python中sys.setdefaultencoding()已经被废除)
reload(sys)
sys.setdefaultencoding('uft-8')
