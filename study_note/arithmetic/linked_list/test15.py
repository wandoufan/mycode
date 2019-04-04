#合并两个递增排序的链表

# leecode版

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        
        if p1 is None:
            return p2
        if p2 is None:
            return p1
        
        while p1 is not None and p2 is not None:
            if p1.val <= p2.val:
                while p1.next is not None and p1.next.val <= p2.val:
                    p1 = p1.next
                tmp = p1.next
                p1.next = p2
                p1 = tmp
            else:
                while p2.next is not None and p2.next.val < p1.val:
                    p2 = p2.next
                tmp = p2.next
                p2.next =p1
                p2 = tmp
        
        return l1 if l1.val <= l2.val else l2













class Listnode:
    def __init__(self,value=None,next=None):
        self.value=value
        self.next=next

n8=Listnode(8)        
n6=Listnode(6,n8)
n4=Listnode(4,n6)        
n2=Listnode(2,n4)

n9=Listnode(9)
n7=Listnode(7,n9)
n5=Listnode(5,n7)
n3=Listnode(3,n5)
n1=Listnode(1,n3)


#方法一：直接在两个链表上进行合并修改，合并过程使用四个指针
def combine(head1,head2):
    x1=head1.next
    x2=head2.next

    if head1.value<=head2.value:
        first=head1
    else:
        first=head2

    #结合两个链表直到其中一个到达尾部
    while True:

        if x1 is None or x2 is None:
            break

        if head1.value<=head2.value:
            head1.next=head2
            head1=x1
            x1=x1.next
        else:
            head2.next=head1
            head2=x2
            x2=x2.next
        #print(head1.value,head2.value)
    print(x1,x2)
    
    #处理尾部部分
    if x1 is None and x2 is not None:
        #print('?')
        if head1.value<head2.value:
            head1.next=head2
        else:
            while head1.value>=x2.value:
                head2=head2.next
                x2=x2.next
                if x2 is None:
                    break
            head2.next=head1
            head1.next=x2
    elif x2 is None and x1 is not None:
        #print('!')
        if head2.value<head1.value:
            head2.next=head1
        else:
            while head2.value>=x1.value:
                head1=head1.next
                x1=x1.next
                if x1 is None:
                    break
            head1.next=head2
            head2.next=x1
        
    else:
        pass
        #print('@')

    #输出链表
    while first is not None:
        print(first.value)
        first=first.next

#combine(n1,n2)

#方法二：重新建一个链表，依次添加两个链表的结点，合并过程使用三个指针
def combine_2(head1,head2):
    head3=Listnode()

    if head1.value<=head2.value:
        first=head1
    else:
        first=head2
    #结合两个链表直到其中一个到达尾部
    while head1 is not None and head2 is not None:
        if head1.value<=head2.value:
            head3.next=head1
            head3=head1
            head1=head1.next
        else:
            head3.next=head2
            head3=head2
            head2=head2.next
    #处理尾部部分
    if head1 is None:
        head3.next=head2
    else:
        head3.next=head1
    #输出链表
    while first is not None:
        print(first.value)
        first=first.next

combine_2(n1,n2)



