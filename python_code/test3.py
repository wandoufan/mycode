# def indexOfSortedSuffix(doc, max_word_len):
#     """
#     Treat a suffix as an index where the suffix begins.
#     Then sort these indexes by the suffixes.
#     """
#     indexes = []
#     length = len(doc)
#     for i in range(0, length):
#         for j in range(i + 1, min(i + 1 + max_word_len, length + 1)):
#             indexes.append((i, j))
#     # 返回一个排序后的以(i,j)元组为元素的indexes列表
#     return sorted(indexes, key=lambda i_j: doc[i_j[0]:i_j[1]])


# string1 = 'hello abc bei jing china'
# string2 = 'helloabcbeijingchina'

# print(len(indexOfSortedSuffix(string1,3)))
# print(len(indexOfSortedSuffix(string2,3)))

# print(string1.split(' '))



str1 = ' '
print(bool(str1))



