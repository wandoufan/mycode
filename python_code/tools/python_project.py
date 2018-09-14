# 关于一个标准的python的工程项目代码规范

# python中的模块、包、库的区别：
# 模块module:一般是单个的.py文件,里边定义了一些函数和变量
# 包package:包是一个有层次的文件目录结构，包目录下的第一个文件就是__init__.py,另外还包含一些模块文件和子目录
# 如果子目录中也有__init__.py文件，那它就是这个包的子包
# 库library:具有相关功能模块的集合，包括标准库/内置库和第三方库


# 工程项目目录中一般包含：
# 备注：工程项目上传到git上应该直接就上传项目目录的内容，项目目录一层就不需要再传了

# 1.README.md
# 整个项目的说明，包括....

# 2.requirements.txt
# 程序运行需要的库及版本号，例如：
# nltk==3.3
# lxml==4.2.3
# jieba==0.39
# PyYAML==3.12

# 3.__init__.py
# __init__.py是包package的标识，文件内容可以为空，目录中没有这个文件，该目录就不会被认为是package
# __init__.py文件的另一个作用是通过定义__all__来指定模糊导入,__all__ = ['class1', 'class2']
# 模糊导入就是import package from * 的方式
# 尽量保证__init__.py文件简单，不在文件内写有效的工程代码

# 4.tests目录
# 存放测试代码

# 5.LICENSE.txt
# 许可文件

# 6.setup.py
# setup.py脚本对整个项目进行打包，
# 它描述了模块的内容，并且列出了其他一些有用信息，例如，它列出了模块所依赖的所有依赖库

# ------------------------------------------------------------------------------------------------
#  项目结构：

# myproject
# |-- README.md
# |-- setup.py
# |-- LICENSE.txt
# |-- requirements.txt
# |-- discover_new_word
# |   |-- __init__.py
# |   |-- useful_1.py
# |   |-- useful_2.py
# |   |-- demo.py # 一个简单的测试文件
# |-- tests
# |   |-- __init__.py
# |   |-- test1.py
# |   |-- test2.py