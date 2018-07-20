# coding:utf-8

# sys模块提供了一系列有关python运行环境的变量和函数

import sys

# sys模块常用的方法函数：

# sys.path是一个list列表，存储python搜索模块的路径集，可以通过方法动态的改变python搜索路径
# 如果python中导入的package或module不在环境变量path中，可以用sys.path添加
# 添加引用模块的地址，添加后即时生效，后面每次import操作都会检查这个目录
# 注意：向sys.path中添加路径只有在程序生命周期内有效，退出python环境后路径失效
sys.path.append(module_path)
sys.path.insert(0, module_path)

# 注意：sys.argv的使用方法是接收在shell环境中输入的命令参数!
# 例如在cmd中执行脚本test.py: python test.py hello world
# 其中hello和world都属于sys.argv获取到的参数，脚本便可以根据获取的不同参数执行不同操作
# sys.argv获取当前正在执行的命令行参数的参数列表
print(sys.argv[0])  # 0代表当前脚本的文件名
print(sys.argv[1:])  # 有效参数是从1开始

# sys.modules获取当前程序已经导入的模块列表
# print(sys.modules.keys())#模块名
# print(sys.modules.values())#模块

# sys.maxsize获取系统支持的最大值
print(sys.maxsize)

# sys.version获取python程序的版本
print(sys.version)

# sys.platform返回操作系统平台名称
print(sys.platform)

# sys.exec_prefix返回python程序的安装位置
print(sys.exec_prefix)

# 旧版本的python中用sys.setdefaultencoding()设置默认编码格式，
# 新版python中默认编码格式为utf-8，sys.setdefaultencoding()已经被废除

# sys.setdefaultencoding()设置默认编码格式
print(sys.getdefaultencoding())

# sys.setrecursionlimit()
sys.setrecursionlimit(500)

# sys.exit(n)表示退出程序，因此前面的部分执行，后边的部分就跳过了
# 参数n为0时表示正常退出，不为0时表示有问题，会产生一个SystemExit异常,异常可以被捕获并反映退出原因
print('123')
sys.exit(1)
print('abc')

# os._exit()会直接退出程序，并不产生异常
# 一般来说os._exit()用于在子线程中退出，sys.exit(n)用于在主线程中退出
