# coding:utf-8

# IPython可以看做一个增强版的python shell,可以提高python的编写、测试、调试的速度
# IPython主要用于交互式数据处理和数据的可视化处理。
# 另外还提供Jupyter notebook使用的一个Jupyter内核（IPython notebook）
# IPython是python的解释器之一，另外的其他解释器还有CPython、PyPy、Jython、IronPython等
# 参考文档：https://blog.csdn.net/gavin_john/article/details/53086766
# https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001407375700558864523211a5049c4983176de304549c8000

# Jupyter Notebook/IPython notebook本质是一个Web应用程序，可以支持40多种编程语言
# 使用浏览器作为界面，向后台的IPython服务器发送请求，并显示结果，
# 主要优点是可以在线编辑代码，不需要本地环境,还可以进行实时交互；
# 另外还可以将代码及运行过程完整的记录下来并保存起来。

# 使用前需要先安装：'pip install ipython','pip install jupyter'
# 'pip install -i https://pypi.douban.com/simple/ jupyter notebook'
# ipython启动命令：
# 'ipython',打开ipython.exe命令行窗口
# 'ipython qtconsole',打开ipython的图形交互界面

# ipython提供的功能：
# 1.Tab键自动补全:在shell中输入表达式时，只要按下Tab键，当前命名空间中任何
# 与输入的字符串相匹配的变量(对象或者函数等)就会被找出来,这时可以通过键盘的向下翻页键找到自己需要的对象。
# 2.内省：在变量的前面或者后面加上一个问号?，就可以将有关该对象的一些通用信息显示出来
# 如果对象是一个函数或者实例方法，则它的docstring也会被显示出来
# 如果使用两个问号??，那么还可以显示出该方法的源代码
# 3.使用历史命令：使用上下翻页键可以找到历史使用命令，
# 使用'hist'或'history'或'hist%'命令查看所有的历史输入,加上'-n'参数可以加上序号。
# 4.运行脚本：在ipython会话环境中，所有类型文件都可以通过%run命令当做Python程序来运行
# 使用'%run file_path'即可
# 5.快速测量代码运行时间：使用%timeit魔法命令可以快速测量代码运行时间。
# -n选项可以控制命令在单词循环中执行的次数，-r选项控制执行循环的次数。
# 例如'%timeit [x*x for x in range(100)]'
# 6.快速debug:可以使用%debug魔法命令在异常点启动调试器。
# 使用u和d向上和向下访问栈，使用q退出调试器。
# 7.进行交互式计算：%pylab魔法命令可以使Numpy和matplotlib中的科学计算功能生效。

# ----------------------------------------------------------------------------------

# Jupyter notebook的使用：
# 参考文档：https://www.cnblogs.com/nxld/p/6566380.html
# 设置jupyter notebook的远程访问
# https://blog.csdn.net/simple_the_best/article/details/77005400
# 设置jupyter notebook的工作路径
# https://note.youdao.com/share/?id=b0dad7bc188a474aede5795218d52377&type=note#/
# jupyter notebook中的一些快捷键和命令模式
# https://www.jianshu.com/p/e862c9f19c1a

# 输入命令'jupyter notebook'，会打开web页面和一个jupyter.exe命令行窗口
# 其中jupyter.exe命令行窗口就相当于本地的notebook server,因此使用过程中窗口不能关闭
# 否则就会报错：A connection to the notebook server could not be established.
# 打开的本地web页面为http://localhost:8888/tree，页面中会显示工作目录中的文件

# 其中web页面的工作目录可以自行设置：
# 在本地C:\Users\Administrator\.jupyter目录下，找到配置文件jupyter_notebook_config.py
# 如果目标文件不存在，则先运行命令'jupyter notebook --generate-config'就会生成文件
# 在配置文件中找到'c.NotebookApp.notebook_dir=',在后面写入指定的本地工作目录，并去掉#注释

# web页面的操作：
# 可以对页面中列出来的工作目录中的文件进行操作，选择文件后可以进行删除，移动，重命名等操作
# 也可以上传本地文件或新建文件
# 选择new中常用python3来编写代码等文件，另外也可以选择Folder来新建目录
# 选择Terminal可以打开连接Linux的命令行窗口

# 编写文件时还可以选择code或markdown等模式，在线编辑时也支持ipython中的所有功能
# 编辑页面上方有保存，插入新输入框，复制剪切，运行等简单功能；页面下方为输入框
# 在上方的Edit中可以实现对输入框的删除，插入，移动等操作；
# 输入框可以通过上方的Insert在任意位置插入；
# 可以在整个notebook最上面插入Heading格式的输入框作为标题；
# 在一个输入框中输入代码后可以通过'Enter'键换行继续输入
# 'Shift+Enter'  运行输入框内的代码并显示运行结果，且一个新的输入框会出现。
# 'Ctrl+Enter' 只会显示运行结果而不会创建新的输入框
# 'Z' 恢复删除的最后一个单元
# 'DD'	删除选中的单元(连续两个大写D)
# 注意:在输入框开头感叹号!，空格后边就可以直接跟上linux命令

# 有一个很方便的功能是，可以选择任意一个之前已经运行过的输入框，对其中的
# 代码或参数修改后再单独运行这个输入框(而不是运行整个notebook)；
# 当然也可以通过上方的Cell-Run all来运行整个notebook的所有输入框；
# 在交互式数据处理场景中经常需要增加或修改代码，如果每次改动都要重新运行一次会耗费很多时间
# notebook可以方便的实现只运行修改的部分，而那些未修改的或是需要很多运行时间的数据处理部分的代码就可以跳过

# 代码及执行过程保存：
# 代码创建过程中会自动在本地工作目录下创建出.ipynb格式的文件，只能在jupyter的web页面上打开
# 建议在页面上方File中以html格式保存到本地

# 通过jupyter notebook访问远程服务器：
# 地址为http://192.168.2.250:8888 密码为123456
# 密码hash值'sha1:df2eaba5234c:8bcef5028cdaacbc35aaf17f87545111d92b62db'
# 'jupyter notebook'命令可以在Linux中启动服务，需要提前'source activate python36'进入环境
# 需要注意的是不能在隐藏目录下启动 jupyter notebook, 否则无法正常访问文件。
# 关闭窗口后服务会停止，可以通过守护进程'nohup jupyter notebook &'
# 或者通过tmux的新窗口中启动服务来保护进程。
# 'netstat -apn | grep 8888' 查看进程是否在运行
