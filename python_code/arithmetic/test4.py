#判断字符串或者数字是否是回文

#方法一
s1='abcdedcba'
num=12321
s2=str(num)
if s1 == ''.join(reversed(s1)):
    print('True')
else:
    print('False')

#方法二
if s1==s1[::-1]:
    print('True')
else:
    print('False')

#方法三  
flag = True
for i in range(int(len(s1)/2)):
    if s1[i]!=s1[len(s1)-i-1]:
        flag = False
        break
if flag:
    print('True')
else:
    print('False')

