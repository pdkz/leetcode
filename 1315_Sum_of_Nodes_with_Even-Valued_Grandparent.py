class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        total = 0
        def dfs(node, parent, gparent):
            nonlocal total
            if not node:
                return

            gparent = parent
            parent = node

            if gparent and not gparent.val % 2:
                if node.left:
                    total += node.left.val
                if node.right:
                    total += node.right.val
            dfs(node.left, parent, gparent)
            dfs(node.right, parent, gparent)
        dfs(root, None, None)
        return total