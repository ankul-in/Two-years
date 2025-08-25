#https://www.geeksforgeeks.org/problems/root-to-leaf-paths/1?page=1&category=Recursion&sortBy=submissions
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def findPaths(root):
    def dfs(node,path,paths):
        if not node:
            return
        path.append(str(node.val))
        if not node.left and not node.right:
            path.append("-->>".join(path))
        else:
            dfs(node.left,path,paths)
            dfs(node.right,path,paths)
        path.pop()
    allPath=[]
    dfs(root,[],allPath)
    return allPath
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

print(findPaths(root))

#start learning man why are you running

