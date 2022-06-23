from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        que = deque([(1, root)])
        prev_height, prev_node, ans = -1, None, []
        while que:
            h, node = que.popleft()

            if h != prev_height:
                node.next = None
            else:
                prev_node.next = node

            if node.left:
                que.append((h+1, node.left))
            if node.right:
                que.append((h+1, node.right))

            prev_node = node
            prev_height = h

        return root