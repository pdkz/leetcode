# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.path = []
        
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        self.traverse(root)

        prev = None
        for i in self.path:
            if prev != None and prev >= i:
                return False
            prev = i
            
        return True
    
    def traverse(self, node):
        if not node:
            return
        
        self.traverse(node.left)
        self.path.append(node.val)
        self.traverse(node.right)
        
        
