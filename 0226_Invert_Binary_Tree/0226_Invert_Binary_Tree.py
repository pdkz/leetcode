# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        queue = [root]
        
        while len(queue) > 0:
            node = queue.pop(0)
            
            left = node.left
            right = node.right
            
            tmp = left
            node.left = right
            node.right = tmp
            
            if left:
                queue.append(left)
            if right:
                queue.append(right)
        
        return root
