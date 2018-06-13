#要求输出所有在m和n范围内的水仙花数。100<=n,m<=1000
#“水仙花数”是指一个三位数，它的各位数字的立方和等于其本身，比如：153=1^3+5^3+3^3。

#找出范围内所有的水仙花数
def flower():
    for i in range(100,1000):
        str1=str(i)
        num=int(str1[0])**3+int(str1[1])**3+int(str1[2])**3
        if i==num:
            print(i)


def find_flower(m,n):
    list1=[153,370,371,407]
    list2=[]
    str1=''
    for i in list1:
        if m<=i<=n:
            list2.append(i)
    print(list2)
    if n<153 or m>407:
        print('no')



#m,n = map(int,input().split())
find_flower(100,500)







