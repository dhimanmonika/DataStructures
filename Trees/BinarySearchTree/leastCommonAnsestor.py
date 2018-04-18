class Node():
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

def insert(root,node):
    if root.data > node.data:
            if root.left:
                insert(root.left,node)
            else:
                root.left=node
    elif root.data < node.data:
            if root.right:
                insert(root.right,node)
            else:
                root.right=node
    else:
        print("Duplicate Cannot insert the node:",node.data)
        return None

def inorder(root):
    if not root:
        return None
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def lca(root,node1,node2):
    if root==None:
        return "Nothing is common"
    elif root.data > node1 and root.data > node2:
        lca(root.left,node1,node2)
    elif root.data < node1 and root.data < node2:
        lca(root.right,node1,node2)
    else:
        print("Common node is:",root.data)

root=Node(20)
insert(root,Node(10))
insert(root,Node(12))
insert(root,Node(24))
insert(root,Node(18))
insert(root,Node(45))
insert(root,Node(40))
insert(root,Node(35))
insert(root,Node(21))
inorder(root)

lca(root,24,18)