# coding:utf-8

# opencc(Open Chinese Convert)模块是用来实现中文简体和繁体相互转换的功能
# 参考链接：https://blog.csdn.net/tab_space/article/details/50823073
# 安装方法
# 安装：opencc-python-0.1.win32.exe
# 修改：Python36\Lib\site-packages\opencc\__init__.py文件
# 注释掉 from version import __version__  新增 __version__ = '0.1'

import opencc
import codecs

# 这里有四种内建的opencc翻译配置：
# t2s  繁体转简体（Traditional Chinese to Simplified Chinese） 
# s2t  简体转繁体（Simplified Chinese to Traditional Chinese） 
# mix2t  混合转繁体（Mixed to Traditional Chinese） 
# mix2s  混合转简体（Mixed to Simplified Chinese）

# 简体转繁体
cc = opencc.OpenCC('t2s')
print(cc.convert('我愛北京天安門'))
# 繁体转简体
cc = opencc.OpenCC('s2t')
print(cc.convert('我爱北京天安门'))


# 从繁体文本中逐行读出，并把简体写入新文本中
# old_file = 'D:/old.txt'# 繁体
# new_file = 'D:/new.txt'# 简体
# cc = opencc.OpenCC('t2s')
# with open(old_file, 'r', encoding='utf-8') as f1:
#     with open(new_file, 'w', encoding='utf-8') as f2:
#         for line in f1.readlines():
#             f2.write(cc.convert(line))
# f1.close()
# f2.close()


# 用linux命令行也可以实现繁简体转换
# opencc --help可以看到具体信息
# -i [file], --input=[file]   从 [file] 读取原始文本
# -o [file], --output=[file]  将转换后的文本写入 [file]
# -c [file], --config=[file]  从 [file] 中读取配置
# -v, --version               显示版本和生成信息
# -h, --help                  显示此帮助


# 代码示例：
# def write_txt(file_name, line):
#     with codecs.open(file_name, 'a', encoding='utf-8') as f:
#         f.write(line)

# if __name__ == '__main__':
#     # 实现繁体转简体，old_file为繁体文件，new_fie为简体文件
#     old_file = 'E:/nlp学习资料/分词测试数据/icwb2-data/testing/cityu_test.utf8'
#     new_file = 'E:/nlp学习资料/分词测试数据/icwb2-data/testing/cityu_test_simple.utf8'
#     cc = opencc.OpenCC('t2s')
#     with codecs.open(old_file, mode='r', encoding='utf-8') as f:
#         with codecs.open(new_file, mode='w', encoding='utf-8') as out:
#             lines = f.readlines()
#             count = 0
#             for line in lines:
#                 # print(cc.convert(line))
#                 count += 1
#                 if count % 1000 == 0:
#                     print(count)
#                 out.write(cc.convert(line))

