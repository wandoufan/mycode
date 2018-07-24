import re

str1 = 'abcdfskd'

str2 = '低端人口'

str3 = 'abc低端人口'

str4 = '2011年'

str5 = '123'


def is_word(word):
    """判断是否是单词"""
    if re.search(r'\s', word):  # 含有空格、回车、换行、制表符不算作单词
        return False
    elif True:  # 纯英文的字符串不算做单词
        is_english = 'yes'
        for character in word:
            if not bool(re.search(r'[a-z]|[A-Z]', character)):
                is_english = 'no'
        if is_english == 'yes':
            return False
        elif re.search(r'[a-z]|[A-Z]|[\u4E00-\u9FA5]', word):  # 单词但含有英文，汉字才记作单词
            return True
        else:
            return False

for word in (str1, str2, str3, str4, str5):
    print(is_word(word))

# def test(word):
#     is_english = 'yes'
#     for character in word:
#         if not bool(re.search(r'[a-z]|[A-Z]', character)):
#             is_english = 'no'
#     if is_english == 'yes':
#         return False
