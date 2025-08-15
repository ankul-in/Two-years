#bst deletion in binary search tree
class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def getSucessor(curr):
    curr=curr.right
    while curr is not None and curr.left is not None:
        curr=curr.left
    return curr
def delNode(root,x):
    if root is None:
        return root
    if root.key>x:
        root.left=delNode(root.left,x)
    elif root.key<x:
        root.right=delNode(root.right,x)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        succ=getSucessor(root)
        root.key=succ.key
        root.right=delNode(root.right,succ.key)
    return root
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key,end=" ")
        inorder(root.right)
if __name__=="__main__":
    root=Node(10)
    root.left=Node(5)
    root.right=Node(15)
    root.right.left=Node(12)
    root.right.right=Node(18)
    x=15
    root=delNode(root,x)
    inorder(root)
    print()
