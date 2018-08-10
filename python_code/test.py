line = '周杰伦 Jay Chou 1979年1月18日出生于台湾省新北市 中国台湾流行乐男歌手 音乐人 演员 导演 编剧 监制 商人'
line = '周杰伦的歌'

def get_all_indexes(line, max_word_len):
    """
    生成文本片段所有可能的索引集合
    :param line:读取的语料中每一行文本内容
    :param max_word_len:限制的最大词长
    """
    indexes = []
    length = len(line)
    for i in range(0, length):
        for j in range(i + 1, min(i + 1 + max_word_len, length + 1)):
            indexes.append((i, j))
    # 返回一个以(i,j)元组为元素的indexes列表
    return indexes

indexes = get_all_indexes(line, 4)

list1 = []
for index in indexes:
    word = line[index[0]:index[1]]
    list1.append(word)
    print('!!!',word)
print(list1)
print(len(list1))
    # print('左', line[index[0] - 1:index[0]])
    # if line[index[0] - 1:index[0]] == '':
    #     print('左边是空字符串')
    # else:
    #     print('左边不是空字符串')
    # print('右', line[index[1]:index[1] + 1])
    # if line[index[1]:index[1] + 1] == '':
    #     print('右边是空字符串')
    # else:
    #     print('右边不是空字符串')
