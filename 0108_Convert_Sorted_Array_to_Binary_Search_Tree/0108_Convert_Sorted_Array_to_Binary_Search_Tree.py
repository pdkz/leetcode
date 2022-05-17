# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:       
        nums_len = len(nums)
        if nums_len == 0:
            return None
        
        def recursion(nums, root):
            l = len(nums)
            if l < 2:
                return
            m = l // 2

            low = nums[0:m]
            high = nums[m+1:]

            low_len = len(low)
            high_len = len(high)
            if low_len > 0:
                node = TreeNode(low[low_len//2])
                root.left = node
                recursion(low, node)
            if high_len > 0:
                node = TreeNode(high[high_len//2])
                root.right = node
                recursion(high, node)
        
        m = nums[nums_len//2]
        root = TreeNode(m)
        
        recursion(nums, root)
        
        return root
