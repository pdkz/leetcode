# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ht = collections.defaultdict(int)
        
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.traverse(root)
        
        vals = sorted(list(self.ht.keys()))
        if len(vals) < 2:
            return -1
        
        return vals[1]
    
    def traverse(self, node):
        if not node:
            return
        
        self.ht[node.val] = 1
        
        self.traverse(node.left)
        self.traverse(node.right)
