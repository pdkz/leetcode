# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def insert(node, val):
            if not node:
                return
            
            if val < node.val:
                if node.left:
                    return insert(node.left, val)
                else:
                    node.left = TreeNode(val)
            elif val > node.val:
                if node.right:
                    return insert(node.right, val)
                else:
                    node.right = TreeNode(val)
            return
        
        if not root:
            root = TreeNode(val)    
        insert(root, val)
        
        return root
