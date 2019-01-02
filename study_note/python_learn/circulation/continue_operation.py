# 当遇到continue语句时，程序会终止当前循环，并忽略剩余的语句，然后回到循环的顶端；
# break和continue的区别：break结束整个循环，continue仅结束此次循环
# 在开始下一次循环之前，如果是条件循环if/while，先验证条件表达式；
# 如果是迭代循环for，先验证是否还有元素可以迭代；
# 验证成功，开始下一次循环；验证失败，结束循环；

#用户密码登陆时仅能试错三次，否则不允许在登陆
count = 3
while count > 0:
    user_password = input('enter password：\n')
    if user_password == str(123456):
        print('login success!')
        break  # break 结束整个循环,跳转到print
    else:
        count -= 1
        if count != 0:
            print('please try again,you have %d chance \n' % (count))
        else:
            print('system locked,can not try anymore')
        continue  # continue仅结束此次循环,跳转到while重新开始验证
print('finish!')
