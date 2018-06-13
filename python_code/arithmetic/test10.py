#将单链表逆序

class Listnode:
    def __init__(self,value=None,next=None):
        self.value=value
        self.next=next
n5=Listnode('e')
n4=Listnode('d')
n3=Listnode('c',n4)
n2=Listnode('b',n3)
n1=Listnode('a',n2)

def reverse(first):
    if first is None or first.next is None:
        return first
    cur=first
    head=None
    nex=first.next

    while True:
        cur.next=head
        head=cur
        cur=nex
        if nex!=None:
            nex=nex.next
        else:
            break
    return head

#print(reverse(n1).value)

def reverse_2(head):#区别在于三个指针的位置
    x=head.next
    head.next=None
    while x is not None:
        y=x.next
        x.next=head
        head=x
        x=y

    while head is not None:
        print(head.value)
        head=head.next

#reverse_2(n5)

