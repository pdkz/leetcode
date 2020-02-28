# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        vals = collections.defaultdict(list)
        queue = [(1, root)]
        
        while len(queue) > 0:
            level, node = queue.pop(0)
            
            val = node.val
            left = node.left
            right = node.right
            
            vals[level].append(val)
            
            if left:
                queue.append([level+1, left])
            if right:
                queue.append([level+1, right])
        
        for k, v in vals.items():
            if k % 2 == 0:
                result.append(v[::-1])
            else:
                result.append(v)

        return resul
