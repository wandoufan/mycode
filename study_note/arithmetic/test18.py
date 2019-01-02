#将一组数字连接成最大数字

#例如：4个整数7,13,4,246连接成的最大整数为7424613
#思路：需要比较每个数字的第一个数字的大小，然后逐一往后比较
#思路：按数字比较的化，32<321,但是转化为字符串后'32'>'321'


#比较用于连接的两个整数的先后顺序，返回应该在前面的整数
#一般的54>521,543>542
#特别的54>543,54<546
def compare(num1,num2):
    str1=str(num1)
    str2=str(num2)
    len1=len(str1)
    len2=len(str2)
    
    #对于相同位数如543和542的整数可以直接比较得出结果
    if len1==len2:
        if str1>str2:
            return num1
        else:
            return num2
    else:
        m=max(len1,len2)
        n=min(len1,len2)
    #对于不同位数但如54和531的一般形式也可以逐位比较得出结果
        for i in range(n):
            if str1[i]>str2[i]:
                return num1
            elif str1[i]<str2[i]:
                return num2
            else:
                continue
    #特殊的，对于位数不同且如543和543510形式的需要比较510和543
    #用递归的方法继续比较
        if len1>len2:
            str3=str1[n:]
            if compare(int(str3),num2)==num2:
                return num2
            else:
                return num1
        else:
            str3=str2[n:]
            if compare(num1,int(str3))==num1:
                return num1
            else:
                return num2


#用于接收参数，并输出结果
def combine(n,*args):
    str1=''
    print(args)
    list1=list(args)
    while len(list1)>0:
        max_num=list1[0]
        for i in range(len(list1)):
            max_num=compare(max_num,list1[i])
        print(max_num)
        str1=str1+str(max_num)
        list1.remove(max_num)

    print(int(str1))



# combine(2,66,664)    
# combine(2,12,123)
# combine(4,7,13,4,246)

#combine(3,123,124,432,66,431,8,6,4321,4325)


if __name__=='__main__':
    n=input()
    list1=input().split(' ')
    combine(n,list1)