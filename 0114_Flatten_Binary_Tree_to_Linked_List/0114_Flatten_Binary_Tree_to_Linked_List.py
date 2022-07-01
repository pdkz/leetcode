from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        nodes = []
        def dfs(prev, node):
            nonlocal nodes
            if not node:
                return

            nodes.append(node)
            prev.left = None
            dfs(node, node.left)
            dfs(node, node.right)

        def flatten_tree(i, node):
            if i == len(nodes):
                return
            node.right = nodes[i]
            flatten_tree(i+1, node.right)

        dfs(root, root.left)
        dfs(root, root.right)
        flatten_tree(0, root)