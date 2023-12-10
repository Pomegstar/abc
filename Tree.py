#inorder Tree raversal
class TreeNode:
    def __init__(self, val):
        self.val = val 
        self.left, self.right = None, None
def inorder(self, root):
    global ans
    ans = []
    def traverse(root):
        if root:
            traverse(root.left)
            print(root.val) #ans.append(root.val)
            traverse(root.right)
    traverse(root)
    return ans