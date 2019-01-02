#二叉排序树/二叉查找树/BST(左<根<右)
#对二叉排序树进行中序遍历可以得到一个递增的序列

class Node:
    def __init__(self,value=None,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

n13=Node(13)    
n12=Node(12,None,n13)
n11=Node(9.5)
n10=Node(8.5)
#n9=Node(7)
n8=Node(4)
n7=Node(10,n11,n12)
n6=Node(8,None,n10)
n5=Node(5,n8)
n4=Node(1)
n3=Node(9,n6,n7)
n2=Node(3,n4,n5)
n1=Node(6,n2,n3)

#二叉排序树的查找:查找指定的结点并返回路径
queue=[]#存储路径
def find(root,node):
    if root is None:
        print('node not exist')
        return 'not found'#未找到目标结点
    else:
        if root.value==node.value:
            print(node.value)
            queue.append(node.value)
            print('found')
            return 'found'#找到目标结点
        elif root.value<node.value:
            print(root.value)
            queue.append(root.value)
            root=root.right
            #注意：递归函数的return需要在每个引用函数的地方return
            return find(root,node)
        else:
            print(root.value)
            queue.append(root.value)
            root=root.left
            return find(root,node)        

#find(n1,n6)
#print(queue)
#print(find(n1,n9))

#二叉排序树的插入：插入一个新结点并返回路径
def insert(root,node):
    if root is None:
        root=node
        print(node.value)
    else:
        if root.value>node.value:
            print(root.value)
            root=root.left
            insert(root,node)
        elif root.value<node.value:
            print(root.value)
            root=root.right
            insert(root,node)
        else:
            print('node already exist')

#insert(n1,n9)

#广度优先遍历二叉排序树
def breadth_first(root):
    queue=[]
    queue.append(root)

    while len(queue)!=0:
        node=queue.pop(0)
        print(node.value)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

#breadth_first(n1)

    

#二叉排序树的删除：删除一个指定结点
#若目标x只有左子树或右子树或者没有子树，让x的子树成为x父节点的子树，代替x位置
#若目标x有左、右子树，用右子树上的最小结点y来代替x,之后删掉y

#注意：对于递归函数，将每次都要变化且需要传递的参数father写入函数参数中并初始设为None
def get_father(root,node,father=None):
    #获得一个结点的父结点(假设结点一定存在)

    if root.value==node.value:
        return  father
    elif root.value>node.value:
        father=root
        root=root.left
        return get_father(root,node,father)
    else:
        father=root
        root=root.right
        return get_father(root,node,father)
    
#print(get_father(n1,n8).value)

def delete(root,node):
    #判断目标结点是否存在
    if find(root,node) == 'not found':
        print('node not exist')
    else:
        if node.left is None:
            father=get_father(root,node)
            #判断目标结点是其父结点的左结点还是右结点
            if father.left==node:
                father.left=node.right
            else:
                father.right=node.right
        elif node.right is None:
            father=get_father(root,node)
            if father.left==node:
                father.left=node.left
            else:
                father.right=node.left
        else:
            #找到目标结点右子树上的最小结点right_min
            right_min=node.right
            while right_min.left is not None:
                right_min=right_min.left
            print('min:',right_min.value)
            father=get_father(root,right_min)
            #重要：判断right_min的父结点father与目标结点是否是同一结点
            if father is node:
                node.value=right_min.value
                #注意：right_min一定没有左结点，但可能有右结点，不能直接father.right=None
                father.right=right_min.right
            else:
                node.value=right_min.value
                #注意：right_min一定没有左结点，但可能有右结点，不能直接father.left=None
                father.left=right_min.right

    breadth_first(n1)

delete(n1,n7)

