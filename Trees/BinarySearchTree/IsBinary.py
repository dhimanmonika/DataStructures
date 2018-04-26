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


def isBin(root):
    if root is None:
        return True
    if (root.left!=None and root.left.data>root.data):
        return False
    if(root.right!=None and root.right.data< root.data):
        return False
    if (not(isBin(root.left)) or not(isBin(root.right))):
        return False

    return True


def inorder(root):
    if not root:
        return None
    inorder(root.left)
    print(root.data)
    inorder(root.right)

root=Node(20)

insert(root,Node(30))
insert(root,Node(10))
insert(root,Node(15))
insert(root,Node(25))
insert(root,Node(35))


print("inorder traversal of binary tree :")
inorder(root)

if(isBin(root)):
    print("It is binary tree")
else:
    print("not a bonary tree")




""" one more solution :

def inOrder(root, stack=[]):
    if root.left:
        inOrder(root.left, stack)
    stack.append(root.data)
    if root.right:
        inOrder(root.right, stack)

        
def check_binary_search_tree_(root):
    stack = []
    inOrder(root, stack)
    length = len(stack)
    for i in range(length-1):
        if stack[i] >= stack[i+1]:
            return False
    return True"""