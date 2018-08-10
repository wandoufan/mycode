# coding:utf-8

# 总结setuptools和distutils.core的使用

# 参考资料
# http://www.sohu.com/a/113563836_218897

# 例子1：
from distutils.core import setup
from Cython.Build import cythonize

setup(name='Hello world app',
      ext_modules=cythonize("hello.pyx"))

# 'python setup.py build'命令执行后产生包含.so文件的build目录和hello.c文件

# 例子2：
from setuptools import setup, find_packages
# find_packages([director])方法可以自动搜索引入python包
# 部分参数仅提供详细的描述信息，不影响具体的打包安装过程 

setup(
    name = "discoverword",# 应用名
    version = "1.0",# 版本号
    keywords = "discover new word",# 关键字(描述信息)
    description = "discover new word",# 描述(描述信息)
    long_description = "discover new word which not exist in local dictionary from input text",# 详细描述(描述信息)
    license = "MIT Licence",# 授权许可(描述信息)
    url = "https://gitlab.yunfutech.com/nlp_projects/oov_detection",# 项目主页(描述信息)
    author = "xingyifan",# 作者(描述信息)
    author_email = "xingyifan@yunfutech.com",# 邮箱(描述信息)
    packages = find_packages(),# 包括安装包在内的pyhon包
    include_package_data = True,# 自动打包文件夹内的所有数据
    platforms = "any",
    install_requires = ["Cython==0.28.4 ",],# 程序运行依赖列表
    scripts = [],
    entry_points = {'console_scripts': ['discoverword = discover.start:begin']}# 设置程序入口为discoverword
    # 安装后执行命令discoverword相当于调用start.py中的begin()方法
)

# 'python setup.py install'命令执行后产生