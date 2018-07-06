# 主要记录在Liunx系统下运行python程序的相关内容：


# ubuntu中运行python程序的方法：
# 1. 运行方式一
# touch test.py
# 然后vim test.py打开并编辑：
# print 'Hello World'
# 打开终端，输入命令：python test.py
# 2. 运行方式二
# 这部分内容只对Linux/Unix用户适用，首先我们需要通过chmod命令
# 给程序可执行的许可，然后运行程序
# chmod a+x helloworld.py
# ./helloworld.py(在ubuntu系统下测试有问题)
# 3. 运行方式三
# 把python程序添加到环境变量路径下
# cp helloworld.py /home/swaroop/bin/helloworld
# helloworld.py


# 查看安装的python程序路径：
# 'which /usr/bin/python*'
# 'ls-al /usr/bin/python*'


# 查看python的版本：
# 'python --version'


# 修改默认的python版本为3.6
# 'sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 200'

