# 调整数字顺序使奇数位于偶数前面

list1=[1,1,4,2,5,6,8,7,8,7,9,3]

def check(n):
    if n%2==0:
        return 'even'  # 偶数
    else:
        return 'odd'  # 奇数


def change(list):
    i=0
    j=len(list)-1
    # 两个指针分别指向首尾，然后依次比较挪动
    while i<j:
        if check(list[i])=='even' and check(list[j])=='odd':
            list[i],list[j]=list[j],list[i]
            i+=1
            j-=1
        elif check(list[i])=='odd' and check(list[j])=='odd':
            i+=1
        elif check(list[i])=='even' and check(list[j])=='even':
            j-=1
        else:
            i+=1
            j-=1
    print(list)

change(list1)