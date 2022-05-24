# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(nums, lo, hi):
            if lo > hi:
                return
            mid = (lo+hi) // 2
            root = TreeNode(nums[mid])
            root.left = dfs(nums, lo, mid-1)
            root.right = dfs(nums, mid+1, hi)
            return root

        return dfs(nums, 0, len(nums) - 1)