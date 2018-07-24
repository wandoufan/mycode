# coding:utf-8

# re模块是python中用来操作正则表达式的模块

# 正则表达式(Regular Expression，在代码中常简写为regex、regexp或RE)
# 正则表达式用来检索、替换符合某个模式的文本

import re

# 实际用到的项目
# pattern = re.compile('[\\s,<>/?:;\'\])
# doc = re.sub(pattern, ' ', doc)

# pred_label = re.sub(r'__label__', '', pred_labels[0][0])


word = '奔驰S级'
# 筛选出中文英文混合的词
if re.search(r'[a-z][\u4E00-\u9FA5]|[A-Z][\u4E00-\u9FA5]|[\u4E00-\u9FA5][a-z]|[\u4E00-\u9FA5][A-Z]', word) is not None:
	print('yes')
else:
	print('no')

# '^word'表示以word开头，'word$'表示以word结尾，在Linux命令中也可以直接使用
# 正则表达式可以直接在linux命令中使用，例如：
# 'grep -i [a-z] test1.txt' 选取test1.txt中所有包含英文字母的行

# 如何判断字符串中仅包含英文字母??
# def test(word):
#     is_english = 'yes'
#     for character in word:
#         if not bool(re.search(r'[a-z]|[A-Z]', character)):
#             is_english = 'no'
#     if is_english == 'yes':
#         return False
