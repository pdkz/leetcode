# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.max = 0
        
    def maxDepth(self, root: TreeNode) -> int:
        self.traverse(root, 0)
        return self.max
    
    def traverse(self, node, level):
        if node == None:
            if level > self.max:
                self.max = level
            return
        
        self.traverse(node.left, level+1)
        self.traverse(node.right, level+1)
