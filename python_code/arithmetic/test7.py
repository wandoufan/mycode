#冒泡排序
#每次排序都可确定出最大（最小）的数据的最终位置
list1=[7,3,6,8,2,1,9,0,5,4]
list2=[4,6,3,1,2,5]
list3=[-13,89,0,23,44,139,88,9,5,-3,63,29,45]

def bubble_sort(list1):
    count=len(list1)
    for i in range(count):
        for j in range(i+1,count):
            if list1[i]>list1[j]:
                list1[i],list1[j]=list1[j],list1[i]#交换两个值的写法
    print(list1)

#快排
#选取中间数据为标志位，每次排序可以确定出标志位的最终位置
def quick_sort(list1,low,high):
    if low>=high:
        return
    head=low
    tail=high
    middle=(low+high)//2
    flag=list1[middle]
    #print(flag)
    while low<high:
        while low<high and flag<list1[high]:
            high-=1
        while low<high and flag>list1[low]:
            low+=1
        list1[low],list1[high]=list1[high],list1[low]
        print(list1)
    quick_sort(list1,head,low-1)
    quick_sort(list1,low+1,tail)

#quick_sort(list3,0,12)

#直接选择排序：每一次从待排序的数据元素中选出最小（或最大）的一个元素，存放到序列的起始位置，直到全部排完。
def select_sort(list1):
    for i in range(len(list1)-1):
        min=i
        for j in range(i+1,len(list1)):
            if list1[j]<list1[min]:
                min=j
        
        list1[i],list1[min]=list1[min],list1[i]
        print(list1)


select_sort(list1)
#print(list1)

#插入排序:将一个数据插入到已经排好序的有序数据中，从而得到一个新的、个数加一的有序数据
#将序列分为左右两段，需要N-1趟排序

def insert_sort(list1):
    count=len(list1)
    for i in range(1,count):
        for j in range(i):
            if list1[j]>list1[i]:
                #print(list1[j],list1[i])
                list1.insert(j,list1[i])
                list1.pop(i+1)
        print(list1)

#insert_sort(list1)

