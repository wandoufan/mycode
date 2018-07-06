# 脚本用来检测指定文本文件的内容中间是否有空行
# 如果有空行，将行号输出出来

file = 'd:/a.utf8'

with open(file, 'r', encoding='utf-8')as f:
    count = 0
    for each_line in f:
        count += 1
        # print(each_line)
        each_line = each_line.strip()
        if bool(each_line) == False:
        	print('!!!!', count)

# 下面两种方法无法判断是否是空行
# if len(each_line) == '0':
# if each_line == '':