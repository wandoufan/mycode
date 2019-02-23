# 二分查找/折半查找（有序表）
# 迭代法二分查找


def binary_search(list1, data):
    low = 0
    high = len(list1) - 1
    while low <= high:
        middle = (low + high) // 2
        if list1[middle] == data:
            return list1.index(data)
        elif list1[middle] > data:
            high = middle - 1
        else:
            low = middle + 1
    return None  # 查找对象不存在

# 递归法二分查找


def binary_search_2(list1, data, left, right):
    low = left
    high = right
    middle = (left + high) // 2
    if left > right:
        return None  # 查找对象不存在
    if list1[middle] == data:
        return list1.index(data)
    elif list1[middle] > data:
        return binary_search_2(list1, data, low, middle - 1)
    elif list1[middle] < data:
        return binary_search_2(list1, data, middle + 1, high)

list1 = [1, 3, 5, 7, 9]
print(binary_search(list1, 4))
print(binary_search_2(list1, 9, 0, 4))
