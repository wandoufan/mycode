2018.6.19
在用Python创建压缩包文件（把abc目录中的所有数据都变为zip压缩包）时，
最开始使用python的zipfile模块，结果发现该模块需要自己手动去遍历abc目录中的每一个文件和子目录，
然后逐个向压缩包中添加，使用起来非常麻烦。
但是如果在代码中调用shell命令'zip -r abc.zip abc'就可以一步完成。
python是胶水语言，要灵活运用python和其他语言，自由组合，取其中好用的部分来用。

2018.6.20
python代码中的tab和空格键不能混着用，否则会报错：缩进错误
尤其是代码放到Vim编辑器中时会有很多缩进问题。
要么都用空格，要么都用tab。
建议用空格，因为不是所有编辑器都会帮你把tab自动转换为四个空格。
另外在sublime编辑器中，如果用ctrl+shift+R来自动调整格式，
系统也是默认把所有的tab替换为空格

2018.6.21
python的函数参数中，有默认值的参数要放在没有默认值的参数的后边，否则会报错。
例如：def test(a,b,c=1,d=2)

2018.6.22
假设现在有两个函数：其中test2函数可以被单独调用，也可以被test1函数调用
class A:
	def test2(self, b):
		print('test2',b)
	def test1(self,a):
		print('test1',a)
		self.test2(a)
a = A()
a.test1('abc')
如果现在要求test2在被单独调用和被test1函数调用两种情况下执行不同的操作
有一个巧妙的方法可以快速修改，并且不影响函数接口(即其他地方调用test2函数时不需要修改参数)
给test2函数增加一个带default值的参数来做标志位
class A:
	def test2(self, b, is_from_test1=False):
		if is_from_test1 == False:
			print('test2', b)
		else:
			print('test1', b)
	def test1(self, a):
		print('test1', a)
		self.test2(a, is_from_test1=True)
a = A()
a.test2('abc')
2018.6.22
关于ftp方式上传和wget方式下载时的覆盖问题：
如果要下载/上传的文件在目标路径已经存在，则会进行自动覆盖；
即多次重复执行上传下载操作，也不会产生任何报错，新的数据会自动覆盖旧的数据；
注意：如果要传输的不是文件而是目录，那么ftp上新增和修改的文件会增加到本地，
但ftp上删除的文件在覆盖后本地的对应文件依然会存在；
遇到重复数据时覆盖方式和先删除再下载方式的区别：
覆盖方式一般由系统自动完成，更加安全；
先删除再下载时可能删除完后下载又失败，就造成没有任何数据了；
如果不能使用覆盖方式就采取原数据先改名，确定新数据下载成功后再删除原数据的方式；
思考：wget,scp等传输方式指定的目标路径如果不存在的话，系统一般都会帮助自动建立起来

2018.6.25
使用pycharm编辑器编辑被git初始化过的代码，文件颜色可以直接反映出来代码是否被修改过
在pycharm编辑器的Edit-Find-Find in Path中可以对整个目录中的所有文件进行关键字的全局搜索
在sublime编辑器的Find-Find in Files中也可以进行全局搜索

2018.6.28
dict1 = {'port': 80, 'color': 'yellow', 'number': 3.14}
注意，获取字典值两种方法的区别：
当要取的键值在字典中不存在时，get(key)方法会返回None,而[key]会报错
print(dict1.get('abc'))
print(dict1['abc'])

2018.7.4
代码规范：
在定义函数时要在函数开头先注明函数功能，输入参数，输出结果等信息
"""
执行分词接口的请求
:param one_sentence: 待分词的句子
:return:
"""

2018.7.10
关于python的缺陷：
1.python是一种解释型语言，运行速度要比Java和C等编译型语言慢得多，大部分时候
程序员的时间比CPU的时间值钱，但对于延迟要求很小的程序还是需要用C++语言来写。
一般来说，代码中只有少部分代码需要占用大量的处理时间，而大部分的代码不经常执行
或者执行非常快，就可以把少部分代码用C来写，其他部分用Python来写。
2.Python不适合于多线程、高并发的应用程序。因为Python中存在全局解释器锁/GIL，
会限制解释器同时执行多条python指令，目前看GIL机制短期内不会取消。目前python
要执行多线程并行代码，不能在单个Python进程中执行。

2018.7.18
1.注意：文件很大时不能用句柄的readlines()方法，否则打开文件会占用巨量内存
f = open('test.txt', 'r')
for line in f.readlines():
	print(line)
尽量直接使用迭代读取数据:
for line in f:
	print(line)
2.在向文本中读数据和写数据时，尽量经常使用string.strip()方法来保证数据纯净可靠

2018.7.19
用linux命令实现功能经常会比用python代码实现方便很多。
例如，需要从一个很大的test1.txt文件中取出一小部分来做测试。
用python代码实现需要用open函数从文件中逐行读取，并逐行写入另一份文件，比较麻烦。
用linux可以直接运行命令:'head 100 test1.txt > test2.txt'