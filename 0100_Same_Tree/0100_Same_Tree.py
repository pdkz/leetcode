# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        lq = deque([p])
        rq = deque([q])

        while(len(lq) > 0 and len(rq) > 0):
            lnode = lq.popleft()
            rnode = rq.popleft()

            if lnode and rnode:
                if lnode.val != rnode.val:
                    return False
                lq.append(lnode.left)
                lq.append(lnode.right)
                rq.append(rnode.left)
                rq.append(rnode.right)
            elif (lnode and not rnode) or (not lnode and rnode):
                return False
        return True if len(lq) == 0 and len(rq) == 0 else False