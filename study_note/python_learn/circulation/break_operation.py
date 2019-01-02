# break语句用于结束当前整个循环然后跳转到下条语句，一般用在if和while语句中
# break和continue的区别：break结束整个循环，continue仅结束此次循环

# 寻找给定num的最大约数
num = 18
count = num / 2
while count > 0:
    if num % count == 0:
        print(count, 'is the largest factor of', num)
        break
    else:
        count -= 1
    print('not finish!')
print('finish!')