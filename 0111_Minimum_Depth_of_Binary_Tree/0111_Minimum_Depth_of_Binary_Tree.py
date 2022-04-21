# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:        
        if root == None:
            return 0
        
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        
        if not l:
            return r + 1
        if not r:
            return l + 1
        
        return l+min(l,r)
