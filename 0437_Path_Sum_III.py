# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sum = Counter()
        counter = 0
        
        def dfs(node, s, k):
            nonlocal counter

            if not node:
                return

            s += node.val
            if s == k:
                counter += 1

            counter += prefix_sum[s-k]
            
            prefix_sum[s] += 1

            dfs(node.left, s, k)
            dfs(node.right, s, k)

            prefix_sum[s] -= 1
        
        dfs(root, 0, targetSum)

        return counter