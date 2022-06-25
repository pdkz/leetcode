class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        current = 0
        queue = [(1, root)]
        rsv = []
        while len(queue) > 0:
            height, node = queue.pop(0)
            if not node:
                break

            if height == current + 1:
                current = height
                rsv.append(node.val)

            if node.right:
                queue.append((current+1, node.right))
            if node.left:
                queue.append((current+1, node.left))

        return rsv

    def rightSideView_level_order_traversal(self, root: TreeNode) -> List[int]:
        res = []
        q = deque([root])

        while q:
            right_side = None
            q_len = len(q)

            for i in range(q_len):
                node = q.popleft()
                if node:
                    right_side = node
                    q.append(node.left)
                    q.append(node.right)
            if right_side:
                res.append(right_side.val)
        return res