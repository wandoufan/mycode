# for 提供了python中最强大的迭代循环结构，可以遍历序列成员

# 1.通过序列项迭代,每次循环each_color变量都被设置为序列中特定某个元素，然后在下面代码块中对该元素做相应操作
color_list = ['red', 'blue', 'white', 'black', 'yellow']
for each_color in color_list:
    print(each_color)
print('\n')

# 2.通过序列的索引来迭代,但速度没有直接迭代序列快
for color_index in range(len(color_list)):
    print(color_list[color_index])
print('\n')

# 3.通过内建列举函数enumerate()来使用项和索引迭代
for i,each_color in enumerate(color_list):
    print('%d %s' %(i,each_color))