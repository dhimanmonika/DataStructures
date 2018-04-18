class Node():
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

def insert(root,node):
    if root.data>node.data:
        if root.left:
            insert(root.left,node)
        else:
            root.left=node
    elif root.data<node.data:
        if root.right:
            insert(root.right,node)
        else:
            root.right=node
    else :
        print("Duplicate cannot be inserted in the tree")
        return None

def inorder(root):
    if not root:
        return None
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def maxHeight(root):
    if root is None :
        return -1
    else:
        return max(maxHeight(root.left),maxHeight(root.right))+1





root=Node(20)

insert(root,Node(30))
insert(root,Node(10))
insert(root,Node(15))
insert(root,Node(25))
insert(root,Node(35))
print("inorder traversal of binary tree :")
inorder(root)

print("max height of binary tree :" ,maxHeight(root))



















