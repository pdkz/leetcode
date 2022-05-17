# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.nodes = []
        
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.traversal(root)
        return self.nodes
    
    def traversal(self, node):
        if node == None:
            return
        
        self.traversal(node.left)

        if node.val != None:
            self.nodes.append(node.val)

        self.traversal(node.right)