# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)
            if node.val == val:
                return node
            l = node.left
            r = node.right
            if l:
                queue.append(l)
            if r:
                queue.append(r)
        return None
