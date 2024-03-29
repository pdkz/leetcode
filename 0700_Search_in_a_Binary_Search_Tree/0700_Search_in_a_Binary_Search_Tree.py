# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int)  -> Optional[TreeNode]:
        return self.bfs(root, val)

    def bfs(self, root: TreeNode, val: int) -> Optional[TreeNode]:
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

    def dfs(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def helper(node, val):
            if not node:
                return None
            if node.val == val:
                return node

            lnode = dfs(node.left, val)
            rnode = dfs(node.right, val)

            return lnode if lnode else rnode

        return helper(root, val)
