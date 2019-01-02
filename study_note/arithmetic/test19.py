#给定一个句子（只包含字母和空格）,将句子中的单词位置反转

#单词用空格分割,单词之间只有一个空格,前后没有空格
#比如：“hello xiao mi”-> “mi xiao hello”

def reverse_1(str):
    list1=str.split()
    list2=list1[::-1]
    str1=''
    for i in range(len(list2)):
        str1=str1+list2[i]
        str1=str1+' '
    str1=str1[:-1]#去掉多余空格
    
    print(str1)

a=input()

reverse_1(a)