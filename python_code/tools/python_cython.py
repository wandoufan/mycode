# coding:utf-8

# Cython是一个快速生成Python扩展模块的编译器，语法层面上属于是Python语法和C语言语法的混合，
# Cython可以将程序性能瓶颈部分的Python代码(.pyx文件)编译为一个.c文件，.c文件再被C编译器
# 编译成一个.so文件，这样程序的其他部分就可以直接调用.so文件来获得性能上的提升
# 除了提升性能之外，cython另一重要功能就是可以直接在python代码中调用C代码

# 注意：cython和cpython的区别：
# cython是提升性能的编译器，cpython是解释python代码的解释器，除了名字接近外之间没有关系
# 当我们从Python官方网站下载并安装好Python3.x后，我们就直接获得了一个官方版本的解释器CPython
# 这个解释器是用C语言开发的，所以叫CPython，在命令行下运行python就是启动CPython解释器
# CPython是python最常用也是默认的解释器，支持绝大多数的第三方库
# 另外的其他解释器还有IPython、PyPy、Jython、IronPython等

# 和python代码不同，Cython代码必须被编译，通常存在两种情况：
# 1.一个.pyx文件被Cython编译成了一个.c文件，其中.pyx文件包含python本身的代码
# 2.一个.c文件被C编译器编译成了一个.so文件(windows平台上是生成.pyd文件)，
# 编译后的文件可以直接被导入python会话中，这部分功能由distutils或setuptools来实现

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

# -----------------------------------------------------------------------------------------------

# cython编译步骤：
# 1.目标python代码hello.pyx(.pyx是cython格式的文件,也可以将现有的.py文件直接改名.pyx)
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

# ---------------------------------------------------------------------------------------------

# 进一步提升性能：
# 简单的用cython对代码进行编译可以提高10%-50%的性能，但如果在代码中声明函数和变量类型可以提升更大的性能
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

# 注意：使用cython优化只会减少程序运行的消耗时间，不会影响到程序的运行结果
# 即,使用cython优化和不使用cython优化的程序运行结果应该是一样的
# 在实际使用过程有声明了变量类型后计算结果改变的情况，声明的类型应该是对的，具体错误原因未知
# 因此使用cython优化后要注意检查结果的一致性

# ------------------------------------------------------------------------------------------

# 关于def、cdef、cpdef的区别：
# 1.def:
# 只能用来声明python中的函数；def函数可以被Python和cython调用；
# 备注：实际测试中发现，对于.pyx中被外部python调用的接口函数(单独的函数，并非类中的函数)
# 只能用def声明，用cdef和cpdef声明都会报错
# 2.cdef:
# 用来声明C语言中的变量类型；cdef声明的函数可以被cython和c调用；
# 备注：实际使用中，cdef常用于声明类和变量，很少用于声明函数
# cdef函数可以接受python中没有的变量类型，如指针
# cdef函数仅在以下情况下使用：
# *需要传递一个非Python类型的数据类型
# *需要传递一个函数给C语言作为一个函数指针
# *需要经常调用的一个函数且不需要从python中调用(仅在当前代码内部运行而不暴露给外部python代码调用的函数)
# 3.cpdef:
# 可以同时声明python和C中的函数，会通过cython产生一个def函数和cdef函数；
# 备注：实际使用中，cpdef极少用到
# cpdef函数仅在以下情况下使用：
# *需要经常调用的一个函数且需要从Python中调用(暴露给外部的python代码调用的函数接口)
# 参考文档：
# https://www.cnblogs.com/lidyan/p/7474244.html
# https://stackoverflow.com/questions/28362009/definition-of-def-cdef-and-cpdef-in-cython


# 4种声明复杂数据类型的方法：
# 1.class:标准的python类的关键字
# 2.cdef class:声明扩展的python类(最常用)
# 可以将类的属性声明为C中的变量类型，也可以对类中的函数进行声明
# 3.cdef struct:声明C语言中struct(struct是C语言中的结构体)
# 4.cdef cppclass:声明C++中的类可以用cppclass关键字
# 参考文档：
# https://spacy.io/api/cython#conventions


# 重要：使用中遇到的关键问题：
# * 不能对Python的类使用cppclass，否则会报错：
# Expected an identifier, found 'def'/'cdef'
# * 类只能用cdef声明，不能用cpdef声明，即不能cpdef class WordSegment(object)，否则报错：
# Extension types cannot be declared cpdef
# * 类中初始化函数__init__()只能用def来声明，不能用cdef或cpdef，否则会报错：
# Special methods must be declared with 'def', not 'cdef
# * set数据类型不支持被声明，即不能cdef set word_set，否则会报错：
# cdef statement not allowed here
# * 声明的字符串类型中cdef char*对应的是str，cdef unicode对应的是bytes，否则会报错：
# TypeError: expected bytes, str found
# * def声明的python函数中的变量仍然可以用cdef声明为C中的变量类型
# * cdef声明的函数不能嵌套在def函数内部，但cdef函数中可以包含def和cpdef声明
# * 类中初始化函数__init__()中的每一个未被声明过类型的self属性需要在类的开头(函数外部)进行声明，
# 例如对函数中的self.number = 0 ,要在上方声明cdef int number ，否则会报错：
# AttributeError: 'wordseg.wordseg.WordSegment' object has no attribute 'number'
# * 如果类中的任意函数的属性被类外部调用，要将属性在类的开头(函数外部)用Public声明，
# 例如 cdef public int number ，否则会报错
# AttributeError: 'wordseg.wordseg.WordInfo' object has no attribute 'number'
# * 对变量进行public声明时，一定要写在类开头，不能写在函数内部，否则会报错：
# Local variable cannot be declared public
# * 在整个pyx文件中被外部调用的接口函数(不在类中的单独的函数)声明不能用cpdef，否则报错：
# closures inside cpdef functions not yet supported
# * 在整个pyx文件中被外部调用的接口函数(不在类中的单独的函数)声明也不能用cdef，否则会找不函数并报错：
# cannot import name 'discover_new_word'


# 使用拓展:
# 1.cimport:
# cython除了可以实现高性能的python代码，另外一个重要功能就是直接在python代码中导入C库
# 可以使用cimport直接从cython代码中调用C库中的函数,例如调用C中math库的sin函数：
# from libc.math cimport sin
# cdef double f(double x):
#     return sin(x * x)
# 2.extern:
# cython已经预定义了很多支持直接用cimport导入的库，对于没有被cython提前支持的C代码
# 可以使用extern关键字来导入，例如导入C文件string.h:
# cdef extern from "string.h":
# 3.__cinit__():
# __cinit__()函数可以用来替代__init__()函数，但不能接受参数，例如：
# def __cinit__(self):
# 4.PreshMap
# PreshMap可以专门针对Python中的dict结构进行优化，python的字典中的键和值都是24个字节
# 经过优化后能占4或8个字节，其中initial_size参数代表字典中键值对的数量，例如：
# from preshed.maps cimport PreshMap
# 5.pxd文件
# ......


# python和cython中的变量和函数的对应关系：
# https://blog.csdn.net/wc781708249/article/details/80249166
# http://cython.readthedocs.io/en/latest/src/tutorial/external.html
# http://cython.readthedocs.io/en/latest/src/tutorial/clibraries.html

# 附：C语言中的数值变量类型及其表示范围
# 短整型short： -32768 ~ + 32767 (2 Bytes)
# 无符号短整型unsigned short： 0 ~ 65536 (2 Bytes)
# 整型int： -2147483648 ~ +2147483647 (4 Bytes)
# 无符号整型unsigned int： 0 ~ 4294967295 (4 Bytes)
# 单精度浮点型float：3.4 x 10^（-38）~ 3.4 x 10^（+38） 
# 双精度浮点型double：1.7 x 10^（-308）~ 1.7 x 10^（+308） 

# ----------------------------------------------------------------------------------------------
# 参考代码：
# https://github.com/explosion/spaCy/blob/master/spacy/tokenizer.pyx
# 代码示例1：新词发现代码
# 其中WordSegment类为对外的接口(外部python代码直接调用WordSegment类)

# coding=utf-8
import re
import codecs
import traceback


from datetime import datetime
import math


cdef indexOfSortedSuffix(line, max_word_len):
    """
    :param line:读取的语料中每一行文本内容
    :param line:max_word_len:限制的最大词长
    """
    cdef list indexes = []
    cdef int length = len(line)
    for i in range(0, length):
        for j in range(i + 1, min(i + 1 + max_word_len, length + 1)):
            indexes.append((i, j))
    # 返回一个排序后的以(i,j)元组为元素的indexes列表
    return indexes

cdef class WordInfo(object):

    cdef public unicode text
    cdef public float freq
    cdef public dict left_word
    cdef public dict right_word
    cdef public float left_entropy
    cdef public float right_entropy
    cdef public float aggregation
    cdef public int count
    cdef public float final_score
    cdef public float freq_score

    def __init__(self, text):
        super(WordInfo, self).__init__()
        self.text = text # 文本片段
        self.freq = 0.0 # 词出现的频率
        self.left_word = {} # 词的左邻字集合，字为key,字频为value
        self.right_word = {} # 词的右邻字集合，字为key,字频为value
        self.left_entropy = 0.0 # 词的左熵
        self.right_entropy = 0.0 # 词的右熵
        self.aggregation = 0 # 词的凝合程度/聚合程度
        self.count = 0 # 新增参数：词出现的次数
        self.final_score = 0 # 新增参数：词的最终分数，即（左熵+右熵）*aggregation
        self.freq_score = 0 # 新增参数：以freq_score为准进行排序,即freq*final_score

    def update(self, left, right):
        """
        更新文本片段出现的次数和左右邻字集合
        """
        self.count += 1
        if left:
            self.left_word[left] = self.left_word.get(left, 0) + 1
        if right: 
            self.right_word[right] = self.right_word.get(right, 0) + 1

    def compute(self, length):
        """
        计算文本片段的词频和左右熵
        """
        self.freq = self.count / length
        self.left_entropy = self.entropyOfList(self.left_word)
        self.right_entropy = self.entropyOfList(self.right_word)

    def computeAggregation(self, words_dict):
        """
        计算文本片段的聚合度
        """
        parts = self.genSubparts(self.text)
        if len(parts) > 0:
            self.aggregation = min(
                [self.freq / words_dict[p1_p2[0]].freq / words_dict[p1_p2[1]].freq for p1_p2 in parts])


    def compute_score(self):
        """
        计算文本片段的分数
        score = (left + right) * aggregation
        """
        self.final_score = (self.left_entropy + self.right_entropy) * self.aggregation

    def compute_freq_score(self):
        """
        计算文本片段分数和词频的乘积
        freq_score = freq*final_score
        """
        self.freq_score = self.freq * self.final_score

    cdef entropyOfList(self, neighbor_dict):
        """
        计算熵值
        """
        cdef int length = 0
        cdef int v
        for v in neighbor_dict.values():
            length = length + v
        return sum([-v / length * math.log(float(v) / length) for v in neighbor_dict.values()])
    
    cdef genSubparts(self, string):
        """
        将字符串切分为所有可能的两部分
        例如，输入 "abcd", 返回[("a", "bcd"), ("ab", "cd"), ("abc", "d")]
        如果输入字符串长度为1，返回空列表
        """
        cdef int length
        cdef list res
        length = len(string)
        res = []
        for i in range(1, length):
            res.append((string[0:i], string[i:]))
        return res


cdef class WordSegment(object):

    cdef public int max_word_len
    cdef public float min_freq
    cdef public float min_entropy
    cdef public float min_aggregation
    cdef public list word_infos
    cdef public list word_infos_with_freq
    cdef public list word_with_freq
    cdef public list words

    def __init__(self, fi, max_word_len=5, min_freq=0.00005, min_entropy=2.0, min_aggregation=50):
        super(WordSegment, self).__init__()
        self.max_word_len = max_word_len
        self.min_freq = min_freq
        self.min_entropy = min_entropy
        self.min_aggregation = min_aggregation
        time_1 = datetime.now()
        # 计算候选词的左右熵，聚合度等各种属性
        # self.word_infos是一个包含所有候选词的WordInfo对象的列表
        self.word_infos = self.genWords(fi)
        time_2 = datetime.now()

        # 按照config文件中设定的左右熵和聚合度的阈值对候选词进行过滤
        filter_func = lambda v: len(v.text) > 1 and v.aggregation > self.min_aggregation and \
                                v.freq > self.min_freq and v.left_entropy > self.min_entropy and v.right_entropy > self.min_entropy
        # self.word_infos_with_freq是过滤后的包含所有候选词的WordInfo对象的列表                         
        self.word_infos_with_freq = [w for w in list(filter(filter_func, self.word_infos))]
        time_3 = datetime.now()

        print('生成新词信息时间：{}s'.format((time_2 - time_1).seconds))
        print('对新词进行过滤时间：{}s'.format((time_3 - time_2).seconds))

    cdef genWords(self, fi):
        """
        计算文本片段的各种属性信息
        """
        # pattern = re.compile('[\\s\\d,.<>/?:;\'\"[\\]{}()\\|~!@#$%^&*\\-_=+a-zA-Z，。《》、？：；“”‘’｛｝【】（）…￥！—┄－]+')
        # 保留符号：中文，英文，数字，#&.+(为了发现新词C++、C#、R&B等)
        pattern = re.compile('[\\s,<>/?:;\'\"[\\]{}()\\|~!$%^*\\-_=，。《》、？：；“”‘’｛｝【】（）…￥！—┄－]+')

        # 先按行计算候选词的出现次数，左邻字集合，右邻字集合
        # word_cands是一个以候选词为key,候选词的WordInfo对象为value的字典结构
        cdef dict word_cands = {}
        # length是文本的长度
        cdef int length = 0
        cdef tuple suf

        with codecs.open(fi, mode='r', encoding='utf-8') as lines:
            for line in lines:
                # 将匹配的各种标点符号都替换为空格
                line = re.sub(pattern, ' ', line)
                length = length + len(line)
                suffix_indexes = indexOfSortedSuffix(line, self.max_word_len)
                for suf in suffix_indexes:
                    word = line[suf[0]:suf[1]]
                    if word not in word_cands:
                        word_cands[word] = WordInfo(word)
                    word_cands[word].update(line[suf[0] - 1:suf[0]], line[suf[1]:suf[1] + 1])

        # 总的计算候选词的出现次数，词频，左右熵等
        for word in word_cands:
            word_cands[word].compute(length)

        # 总的计算候选词的聚合度等(计算聚合度需要提前计算出候选词每个子部分的词频)
        for word in word_cands:
            # 对长度等于1或不符合正则标准的候选词，只需要它的词频信息，后期会过滤掉，因此不需要再计算聚合度等
            if len(word) == 1:
                continue
            if not self.is_word(word):
                continue
            word_cands[word].computeAggregation(word_cands)
            word_cands[word].compute_score()
            word_cands[word].compute_freq_score()

        # 计算完聚合度之后过滤掉长度为1或不符合正则标准的候选词
        for word in list(word_cands):
            if len(word) == 1:
                del word_cands[word]
                continue
            if not self.is_word(word):
                del word_cands[word]

        # 按照候选词的freq_score属性排序后返回一个包含所有候选词的WordInfo对象的列表
        cdef list word_infos
        word_infos = list(word_cands.values())
        return sorted(word_infos, key=lambda word_info: word_info.freq_score, reverse=True)

    def is_word(self, word):
        """判断是否是单词"""
        if re.search(r'\s', word):  # 含有空格、回车、换行、制表符不算作单词
            return False
        elif re.match(r'^[a-zA-Z]+$', word):  # 纯英文的字符串不算做单词
            return False
        elif re.search(r'[a-z]|[A-Z]|[\u4E00-\u9FA5]', word):  # 单词但含有英文或汉字才记作单词
            return True
        else:
            return False

    def load_word_list(self, file_name):
        """
        自定义词表加载，加载后对新词执行过滤
        :param file_name: 词表文件名
        :return:
        """
        try:
            # 加载词表
            word_set = set()
            with codecs.open(file_name, mode='r', encoding='utf-8') as fi:
                for line in fi:
                    word_set.add(re.sub(r'\r|\n', '', line))

            # 利用词表对新词进行过滤
            self.word_infos_with_freq = [w for w in self.word_infos_with_freq if w.text not in word_set]
            self.word_with_freq = [(w.text, w.freq) for w in self.word_infos_with_freq]
            self.words = [w[0] for w in self.word_with_freq]
        except Exception as e:
            traceback.print_exc()

# ----------------------------------------------------------------------------------------------

# 代码示例2：优化后新词发现代码
# 其中discover_new_word函数为对外的接口(外部python代码直接调用discover_new_word函数)
# coding=utf-8

import re
import codecs
import math
from datetime import datetime


cdef class WordNeighbor(object):

    cdef public unicode text
    cdef public dict left_word
    cdef public dict right_word
    cdef public float left_entropy
    cdef public float right_entropy

    def __init__(self, text):
        self.text = text  # 文本片段
        self.left_word = {}  # 词的左邻字集合，字为key,字频为value
        self.right_word = {}  # 词的右邻字集合，字为key,字频为value
        self.left_entropy = 0.0  # 单字的左熵
        self.right_entropy = 0.0  # 单字的右熵

    def update_neighbor(self, left, right):
        """
        更新文本片段的左右邻字集合
        其中左/右邻字为空格(即' ')和不存在(即'')的情况合并统计计数
        """
        if left or left == '':
            if left == '':
                left = ' '
            self.left_word[left] = self.left_word.get(left, 0) + 1
        if right or right == '':
            if right == '':
                right = ' '
            self.right_word[right] = self.right_word.get(right, 0) + 1

    def compute_entropy(self, left_word, right_word):
        """
        计算文本片段的左右熵
        """
        self.left_entropy = self.entropy_of_dict(left_word)
        self.right_entropy = self.entropy_of_dict(right_word)

    def entropy_of_dict(self, neighbor_dict):
        """
        计算熵值
        """
        length = 0
        for v in neighbor_dict.values():
            length = length + v
        return sum([-v / length * math.log(float(v) / length) for v in neighbor_dict.values()])


cdef class WordInfo(object):

    cdef public unicode text
    cdef public float freq
    cdef public int count
    cdef public float left_entropy
    cdef public float right_entropy
    cdef public float aggregation
    cdef public float final_score
    cdef public float freq_score

    def __init__(self, text):
        self.text = text  # 文本片段
        self.freq = 0.0  # 词出现的频率
        self.count = 0  # 词出现的次数
        self.left_entropy = 0.0  # 词的左熵
        self.right_entropy = 0.0  # 词的右熵
        self.aggregation = 0.0  # 词的凝合程度/聚合程度
        self.final_score = 0.0  # 词的最终分数，即（左熵+右熵）*aggregation
        self.freq_score = 0.0  # 以freq_score为准进行排序,即freq*final_score

    def update_count(self):
        """
        更新文本片段出现的次数
        """
        self.count += 1

    def compute_freq(self, length):
        """
        计算文本片段的词频
        """
        self.freq = self.count / length
        return self.freq

    def compute_aggregation(self, freq_dict):
        """
        计算文本片段的聚合度
        """
        parts = self.generate_parts(self.text)
        if len(parts) > 0:
            self.aggregation = min(
                [self.freq / freq_dict[part[0]] / freq_dict[part[1]] for part in parts])

    def compute_final_score(self):
        """
        计算文本片段的分数
        score = (left + right) * aggregation
        """
        self.final_score = (self.left_entropy +
                            self.right_entropy) * self.aggregation

    def compute_freq_score(self):
        """
        计算文本片段分数和词频的乘积
        freq_score = freq * final_score
        """
        self.freq_score = self.freq * self.final_score

    def generate_parts(self, string):
        """
        将字符串切分为所有可能的两部分
        例如，输入 "abcd", 返回[("a", "bcd"), ("ab", "cd"), ("abc", "d")]
        如果输入字符串长度为1，返回空列表
        """
        cdef int length
        cdef list res
        length = len(string)
        res = []
        for i in range(1, length):
            res.append((string[0:i], string[i:]))
        return res


def is_word(word):
    """
    判断是否是合格的单词
    """
    if re.search(r'\s', word):  # 含有空格、回车、换行、制表符不算作单词
        return False
    elif re.match(r'^[a-zA-Z]+$', word):  # 纯英文的字符串不算做单词
        return False
    elif re.search(r'[a-z]|[A-Z]|[\u4E00-\u9FA5]', word):  # 单词但含有英文或汉字才记作单词
        return True
    else:
        return False

def get_all_indexes(line, max_word_len):
    """
    生成文本片段所有可能的索引集合
    :param line:读取的语料中每一行文本内容
    :param max_word_len:限制的最大词长
    """
    cdef list indexes
    cdef int length
    indexes = []
    length = len(line)
    for i in range(0, length):
        for j in range(i + 1, min(i + 1 + max_word_len, length + 1)):
            indexes.append((i, j))
    # 返回一个以(i,j)元组为元素的indexes列表
    return indexes

def filter_func(wordinfo_list, min_freq, min_entropy, min_aggregation):
    '''
    按照config文件中设定的左右熵和聚合度的阈值对候选词进行过滤
    '''
    cdef list word_infos
    word_filter = (lambda v: len(v.text) > 1 and v.aggregation > min_aggregation and
                   v.freq > min_freq and v.left_entropy > min_entropy and v.right_entropy > min_entropy)
    # word_infos是过滤后的包含所有符合标准候选词的WordInfo对象的列表
    word_infos = [w for w in list(filter(word_filter, wordinfo_list))]
    return word_infos


def discover_new_word(fi, int max_word_len=5, float min_freq=0.00005, float min_entropy=2.0, float min_aggregation=50):
    """
    主函数
    计算文本片段的各种属性信息
    """
    # 保留符号：中文，英文，数字，#&.+(为了发现新词C++、C#、R&B等)
    pattern = re.compile(
        '[\\s,<>/?:;\'\"[\\]{}()\\|~!$%^*\\-_=，。《》、？：；“”‘’｛｝【】（）…￥！—┄－]+')

    # 先按行计算候选词的出现次数，左邻字集合，右邻字集合
    cdef dict word_cands
    cdef dict word_neighbor
    cdef dict freq_dict
    cdef int length
    # word_cands是一个以候选词为key,候选词的WordInfo对象为value的字典结构
    word_cands = {}
    # word_neighbor是一个以候选词为key,候选词的WordNeighbor对象为value的字典结构
    word_neighbor = {}
    # freq_dict是一个以候选词为key,候选词的词频freq为value的字典结构
    freq_dict = {}
    # length是文本的长度
    length = 0
    with codecs.open(fi, mode='r', encoding='utf-8') as lines:
        for line in lines:
            # 将匹配的各种标点符号都替换为空格
            line = re.sub(pattern, ' ', line)
            length = length + len(line)
            indexes = get_all_indexes(line, max_word_len)
            for index in indexes:
                word = line[index[0]:index[1]]
                if word not in word_cands:
                    word_cands[word] = WordInfo(word)
                word_cands[word].update_count()
                # 长度为2的文本片段存入邻字字典
                if word not in word_neighbor and len(word) == 2:
                    word_neighbor[word] = WordNeighbor(word)
                if word in word_neighbor:
                    word_neighbor[word].update_neighbor(
                        line[index[0] - 1:index[0]], line[index[1]:index[1] + 1])

    # 总的计算候选词的词频,freq信息在freq_dict和WordInfo中都存放一份
    for word in word_cands:
        freq_dict[word] = word_cands[word].compute_freq(length)

    # 总的计算候选词的聚合度等(计算聚合度需要提前计算出候选词每个子部分的词频)
    for word in word_cands:
        # 对长度等于1或不符合正则标准的候选词，只需要它的词频信息，后期会过滤掉，因此不需要再计算聚合度等信息
        if len(word) == 1:
            continue
        if not is_word(word):
            continue
        word_cands[word].compute_aggregation(freq_dict)

    # 计算完聚合度之后过滤掉长度为1或不符合正则标准的候选词
    for word in list(word_cands):  # 字典结构不支持在循环过程中直接删除
        if len(word) == 1:
            del word_cands[word]
            continue
        if not is_word(word):
            del word_cands[word]

    # 计算候选词的左右熵信息
    for word in word_neighbor:
        left_word = word_neighbor[word].left_word
        right_word = word_neighbor[word].right_word
        word_neighbor[word].compute_entropy(left_word, right_word)
    for word in word_cands:
        word_cands[word].left_entropy = word_neighbor[word[0:2]].left_entropy
        word_cands[word].right_entropy = word_neighbor[word[-2:]].right_entropy

    # 计算候选词的综合分数
    for word in word_cands:
        word_cands[word].compute_final_score()
        word_cands[word].compute_freq_score()

    # 按照候选词的freq_score属性排序后生成一个包含所有候选词的WordInfo对象的列表
    cdef list wordinfo_list
    wordinfo_list = list(word_cands.values())
    wordinfo_list = sorted(
        wordinfo_list, key=lambda word_info: word_info.freq_score, reverse=True)

    # 按照config文件中设定的左右熵和聚合度的阈值对候选词进行过滤后返回一个列表
    word_infos = filter_func(wordinfo_list, min_freq,
                             min_entropy, min_aggregation)
    return word_infos
