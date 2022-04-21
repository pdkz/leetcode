# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.b = False
        
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        self.pathSum(root, sum, 0)
        return self.b
    
    def pathSum(self, node, s, t):
        if not node:
            return 0
        
        t += node.val
        
        self.pathSum(node.left, s, t)
        self.pathSum(node.right, s, t)
        
        if not node.left and not node.right:
            if s == t:
                self.b = True
        
        return node.val
