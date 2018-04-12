class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.right=right
        self.left=left

def print_preorder(root):
    if root:
        print(root.data,end=" ")
        print_preorder(root.left)
        print_preorder(root.right)

root = Node(1,None,  Node(2, None,  Node(5 , Node(3,None,Node(4,None,None)),Node(6,None,None ) ) ) )
print_preorder(root)