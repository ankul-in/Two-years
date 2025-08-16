#tree traversal in bst
class Node:
    def __init__(self,v):
        self.left=None
        self.right=None
        self.data=v
def printInOrder(root):
    if root:
        printInOrder(root.left)
        print(root.data,end=" ")
        printInOrder(root.right)

if __name__=="__main__":
    root=Node(100)
    root.left=Node(20)
    root.right=Node(200)
    root.left.left=Node(10)
    root.left.right=Node(30)
    root.right.left=Node(150)
    root.right.right=Node(300)
    print("inorder Traversal-->",end=" ")
    printInOrder(root)