# 用python语言实现一个单向链表

# 定义节点类


class Node:
    # 初始化节点

    def __init__(self, data):
        self.data = data
        self.next = None

# 定义链表类


class Linklist:
    # 初始化链表

    def __init__(self):
        self.head = None
        self.length = 0

    # 获取链表长度
    def get_len(self):
        pointer = self.head
        length = 0
        while pointer:
            length += 1
            pointer = pointer.next
        return length

    # 列表末尾添加节点
    def append(self, node):
        data = None
        if isinstance(node, Node):
            data = node
        else:
            data = Node(node)

        if not self.head:
            self.head=data
        else:
            pointer=self.head
            while pointer.next:
                pointer=pointer.next
            pointer.next=data

    # 删除指定索引位置的节点
    def delete(self,index):
        




node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

list1=Linklist()
list1.append(node1)
list1.append(node2)
list1.append(node3)
print(list1.get_len())


