# 判断单链表是否有环，如果有环就找到入口结点
# 注意，不是判断单链表是否是环，而是判断单链表中是否包含一个环

# 思路1：依次遍历链表的每一个结点，并存入一个hash表中，每遍历到一个新的结点，就与hash表中结点进行比对

# 思路2：用快慢两个指针指向head结点，慢指针一次向下移动一个结点，快指针一次移动两个结点，
# 如果有环则两个指针必会相遇(类似于跑道上两个人跑步)，否则快指针会先到尾结点
# 假设相遇结点为m结点，p1指向head结点，p2指向m结点，p1，p2一起向前移动，再次相遇的结点即为环的入口结点

class LinkNode:
    """
    定义链表中的一个结点
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def create_link(value_list):
    """
    初始化出链表，链表中结点存放在一个列表结构中，返回列表
    """
    node_list = []
    for i in value_list:
        node_list.append(LinkNode(i))
    for i in range(len(value_list) - 1):
        node_list[i].next = node_list[i + 1]
    return node_list


link_list = create_link([1, 2, 3, 4, 5, 6, 7, 8, 9])
link_list[-1].next = link_list[5] # 给链表设置一个环



def check_link(head):
    """
    传入链表的头结点，判断链表是否有环，如果有环则返回入口结点
    """
    p1 = head
    p2 = head
    while True:
        if p2 == None or p2.next == None:
            print('无环')
            break
        else:
            print(p1.value, p2.value)
            p1 = p1.next
            p2 = p2.next.next
            if p1 is p2:
                print('有环')
                while p1 is not head:
                    p1 = p1.next
                    head = head.next
                break
    return p1


print(check_link(link_list[0]).value)


