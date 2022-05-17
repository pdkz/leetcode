# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        max_length = 0
        
        def dfs(node):
            nonlocal max_length
            if not node:
                return 0
            
            left = dfs(node.left) + 1
            right = dfs(node.right) + 1
            
            if node.left and node.left.val != node.val + 1:
                left = 1
            if node.right and node.right.val != node.val + 1:
                right = 1
            length = max(left, right)
            
            max_length = max(max_length, length)
            
            return length
        
        dfs(root)
        return max_length
