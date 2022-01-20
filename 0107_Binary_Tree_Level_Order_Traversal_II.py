# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        level = 1
        queue = deque([[level, root]])
        output = deque()

        while queue:
            level, node = queue.popleft()
            if len(output) == level:
                output[-level].append(node.val)
            else:
                output.appendleft([node.val])
            if node.left:
                queue.append([level+1, node.left])
            if node.right:
                queue.append([level+1, node.right])
        return output