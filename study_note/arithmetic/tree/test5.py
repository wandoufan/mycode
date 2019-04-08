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
def pretree(root, list1):
    if root == None:
        return
    # print(root.value)
    list1.append(root.value)
    pretree(root.left, list1)
    pretree(root.right, list1)

def test2():
    result = []
    pretree(n1, result)
    print(result)

test2()
print('\n')


# 中序遍历 LNR
def midtree(root):
    if root == None:
        return
    midtree(root.left)
    print(root.value)
    midtree(root.right)

midtree(n1)

def get_mid(x, list1):
    print(list1)
    if x is not None:
        if x.left is None and x.right is not None:
            list1.append('null')
        else:
            get_mid(x.left, list1)
    if x is None:
        return
    list1.append(x.val)
    if x.right is None and x.left is not None:
        list1.append('null')
    else:
        get_mid(x.right, list1)
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



# 层序遍历：广度优先（先兄弟节点，后子节点），队列实现
# 等同于从上往下，从左往右打印结点
# 按层序逐个输出结点

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


# 层序遍历：要求逐层输出每一层的结点
# 输入：[3,9,20,null,null,15,7]
# 输出：[[3],[9,20],[15,7]]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        queue = []
        if root is None:
            return result
        if root.left is None and root.right is None:
            result.append([root.val])
            return result
        # 使用双层列表按层存储所有结点
        queue.append([root])
        while len(queue[-1]) != 0:
            tmp = []
            for node in queue[-1]:
                if node.left is not None:
                    tmp.append(node.left)
                if node.right is not None:
                    tmp.append(node.right)
            queue.append(tmp)
        # 将每层的结点转换为结点的值
        for i in range(len(queue) - 1):
            level = queue[i]
            node_list = []
            for node in level:
                node_list.append(node.val)
            result.append(node_list)
        
        return result
