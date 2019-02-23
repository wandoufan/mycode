#输出链表的倒数第n个结点

class Listnode:
    def __init__(self,value=None,next=None):
        self.value=value
        self.next=next

n6=Listnode('f')        
n5=Listnode('e',n6)
n4=Listnode('d',n5)
n3=Listnode('c',n4)
n2=Listnode('b',n3)
n1=Listnode('a',n2)

#方法一：要对链表进行两次遍历，第一次获取链表长度，第二次找到目标结点
def get_len(first):
    count=0
    head=first
    while head is not None:
        count+=1
        head=head.next
    return count

def get_node_1(first,n):
    len=get_len(first)
    k=len-n
    for i in range(k):
        first=first.next
    print(first.value)

get_node_1(n1,2)


#方法二：仅对链表进行一次遍历，使用两个指针

def get_node_2(first,n):
    head=first
    tail=head
    #将第二个指针挪至第n个结点
    for i in range(n-1):
        tail=tail.next
    #当第二指针指向尾结点时，第一个指针即指向了倒数第n个结点
    while tail.next is not None:
        head=head.next
        tail=tail.next
    print(head.value)
    

get_node_2(n1,6)