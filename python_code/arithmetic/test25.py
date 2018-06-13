#输入n值，使用递归函数，求杨辉三角形中各个位置上的值
#杨辉三角型:每行端点与结尾的数为1,第n行的数字有n项,每个数等于它上方两数之和

def yanghui(n):
    list1=[1]
    count=0
    while count<n:
        print(list1)
        list1=[1]+[list1[i]+list1[i+1] for i in range(len(list1)-1)]+[1]
        count+=1

#yanghui(6)


#用生成器实现（把print换成yield）
def yanghui_2(n):
    list1=[1]
    count=0
    while count<n:
        yield list1
        list1=[1]+[list1[i]+list1[i+1] for i in range(len(list1)-1)]+[1]
        count+=1

# for i in yanghui(6):
#      print(i)

#将循环部分写的更简单
def yanghui_3(n):
    list1=[1]
    count=0
    while count<n:
        print(list1)
        list2=[]
        for i  in range(len(list1)-1):
            list2.append(list1[i]+list1[i+1])
        #print(list2)
        list1=[1]+list2+[1]
        

        count+=1

#yanghui_3(8)

#把结构排列成三角形,调整输出格式

def yanghui_4(n):
    list1=[1]
    count=0
    while count<n:
        list2=[]
        list3=map(str,list1)#注意:join函数要求列表中的元素为字符串类型，不能是整数类型
        str1=' '*(n-count)+' '.join(list3)
        print(str1)
        for i in range(len(list1)-1):
            list2.append(list1[i]+list1[i+1])
        list1=[1]+list2+[1]
        count+=1

      
#yanghui_4(8)








