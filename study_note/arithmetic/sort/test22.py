# 求n个数中最小的K个数,按升序输出
# 思路：类似冒泡排序，但是只需要排出前n个数字即可

list1 = [1, 23, 57, -12, 88, 76, 34, 9, 24, 65, 54, 45, -5, -37]


def select(list1, k):
    count = len(list1)
    while k > 0:
        for i in range(count):
            for j in range(i + 1, count):
                if list1[i] > list1[j]:
                    list1[i], list1[j] = list1[j], list1[i]
            k -= 1
    print(list1[:k])


select(list1, 5)
