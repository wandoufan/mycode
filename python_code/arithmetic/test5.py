# 二叉树的深度优先（先序，中序，后序），广度遍历算法


class Node:

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# root=Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))

n4 = Node('d')
n5 = Node('e')
n6 = Node('f')
n2 = Node('b', n4, n5)
n3 = Node('c', n6)
n1 = Node('a', n2, n3)

# 先序遍历 NLR
def pretree(root):
    if root == None:
        return
    print(root.value)
    pretree(root.left)
    pretree(root.right)

pretree(n1)
print('\n')


# 中序遍历 LNR
def midtree(root):
    if root == None:
        return
    midtree(root.left)
    print(root.value)
    midtree(root.right)

midtree(n1)
print('\n')

# 后序遍历 LRN
def afttree(root):
    if root == None:
        return
    afttree(root.left)
    afttree(root.right)
    print(root.value)

afttree(n1)
print('\n')



#广度优先（先兄弟节点，后子节点），队列实现
#等同于从上往下，从左往右打印结点

def breadth_first_search(root):
    queue=[]
    if root == None:
        return
    queue.append(root)#可以用列表来直接存储节点
    while len(queue)!=0:
        node=queue.pop(0)
        print(node.value)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


breadth_first_search(n1)


