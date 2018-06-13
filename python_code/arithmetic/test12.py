#单链表添加头结点

class Listnode:
    def __init__(self,value=None,next=None):
        self.value=value
        self.next=next
n5=Listnode()
n4=Listnode('d')
n3=Listnode('c',n4)
n2=Listnode('b',n3)
n1=Listnode('a',n2)

def add_head(first,node):
    head=first
    new=node
    new.next=head
    head=new
    while True:
        print(head.value)
        head=head.next
        if head is None:
            break

#add_head(n1,Listnode('e'))

#插入任意位置结点(含头结点和尾结点)
def insert_node(first,index,node):
    if index==0:
        add_head(first,node)

    head=first
    new=node
    for i in range(index-1):
        head=head.next
    nex=head.next
    new.next=nex
    head.next=new
    #输出插入后的新链表
    while first is not None:
        print(first.value)
        first=first.next

#insert_node(n1,3,Listnode('e'))


#计算链表长度
def get_len(first):
    count=0
    head=first
    while head is not None:
        count+=1
        head=head.next
    return count

#print(get_len(n1))

#单链表删除头结点

def del_head(first):
    head=first.next
    first.next=None
    while head is not None:
        print(head.value)
        head=head.next

#单链表删除中间结点
#方法一：复杂度为O(n),需要从开头一直遍历到目标删除结点
#可以处理中间结点和尾结点
def del_node_1(first,node):
    if first==node:
        del_head(node)
    else:
            head=first
            while head.next is not node:
                head=head.next
                if head is None:
                    break
            #判断目标结点是否存在
            if head is None:
                print('node not exist')
            else:
                head.next=node.next
            #输出删除后的新链表
            while first is not None:
                print(first.value)
                first=first.next

#del_node_1(n1,n5)

#方法二：复杂度为O(1)，不需要遍历得到目标结点
#将目标的下一个结点内容覆盖目标，再删除下一个结点即可
#仅能处理中间结点，尾结点还需要从头遍历处理
def del_node_2(first,node):
    if first==node:
        del_head(node)
    else:
        if node.next is not None:#判断是否尾结点
            node.value=node.next.value
            node.next=node.next.next
        else:
            head=first
            while head.next is not node:
                head=head.next
            head.next=None

        while first is not None:
            print(first.value)
            first=first.next

#del_node_2(n1,n5)


#查找链表中的结点索引
def get_index(first,node):
    count=1
    while first is not None:
        if first == node:
            print(count)
            break
        else:
            count+=1
            first=first.next
    if first is None:
        print('node not exist')

#n5=Listnode('e')
#get_index(n1,n5) 

