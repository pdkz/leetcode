# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.path = []
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.traversal(root)
        return self.path[k-1]
    
    def traversal(self, node):
        if node == None:
            return
        
        self.traversal(node.left)
        self.path.append(node.val)
        self.traversal(node.right)
