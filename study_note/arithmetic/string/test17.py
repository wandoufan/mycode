# 字符串的全排列：输入一个字符串，输出字符串中字符的所有排列
# 递归法：

str = list('abc')
count = 0


def sort_1(str, begin, end):
    global count  # 全局变量count用来保存个数
    if begin >= end:
        print(str)
        count += 1
    else:
        a = begin
        for i in range(begin, end):
            str[i], str[a] = str[a], str[i]
            sort(str, begin + 1, end)
            str[a], str[i] = str[i], str[a]

# sort(str,0,len(str))
# print(count)

# 求字符的所有组合?????????


def sort_2(list):
    list1 = []
    for i in range(0, len(list)):
        for j in range(i + 1, len(list) + 1):
            for k in range(j, len(list) + 1):
                str = list[i] + list[j:k]
                list1.append(str)

    return list1
list2 = sort_2('abcd')
list2 = list(set(list2))
