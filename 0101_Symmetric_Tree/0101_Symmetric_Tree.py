# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.lpath = []
        self.rpath = []
        
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        self.lpath.append(root.val)
        self.rpath.append(root.val)
        
        self.traverse_left(root.left)
        self.traverse_right(root.right)
        
        return self.lpath == self.rpath
        
    def traverse_left(self, node):
        if not node:
            self.lpath.append(None)
            return
        
        self.lpath.append(node.val)
        self.traverse_left(node.left)
        self.traverse_left(node.right)

    def traverse_right(self, node):
        if not node:
            self.rpath.append(None)
            return
            
        self.rpath.append(node.val)
        self.traverse_right(node.right)
        self.traverse_right(node.left)


