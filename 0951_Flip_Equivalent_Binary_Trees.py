# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def rec(node1, node2):
            if node1 is node2:
                return True
            
            if node1 == None or node2 == None or node1.val != node2.val:
                return False
            
            return (rec(node1.left, node2.left) and rec(node1.right, node2.right)) or (rec(node1.left, node2.right) and rec(node1.right, node2.left))
        
        return rec(root1, root2)
