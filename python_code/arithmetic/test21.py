#逆序的输出单链表上每个结点的值
#思路：将正序输出的单链表结果存在链表中，再将链表逆序输出
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


def output_reverse(head):
    list1=[]
    while head is not None:
        list1.append(head.value)
        head=head.next

    print(list1[::-1])

output_reverse(n1)



