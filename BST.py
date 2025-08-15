#binary search tree
class Node:
    def __init__(self,key):
        self.val=key
        self.left=None
        self.right=None
def insert(root,key):
    if root is None:
        return Node(key)
    if root.val == key:
        return root
    if root.val<key:
        root.right=insert(root.right,key)
    else:
        root.left=insert(root.left,key)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end= " ")
        inorder(root.right)

r=Node(15)
r=insert(r,10)
r=insert(r,18)
r=insert(r,4)
r=insert(r,11)
r=insert(r,16)
r=insert(r,20)
r=insert(r,13)

print(inorder(r))
