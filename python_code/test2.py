
# str1 = '血压'
# str2 = '高血压'
# str3 = '杨定'
# str4 = '杨定一'

top_list = ['杨定一', '文茜', '生命', '杨定', '人生', '念头', '萎缩', '监狱', '身份', \
'情绪', '出生', '理解', '身体', '接受', '带来', '比如', '找到', '希望', '快乐', '完美']


remove_list = []
for top_word in top_list:
    len_word = len(top_word)
    for word in top_list:
        if len(word) != len(top_word):
            if word[:len_word] == top_word or word[-len_word:] == top_word:
                remove_list.append(top_word)
print(remove_list)


