# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums = []
        def dfs(node, num):
            nonlocal nums
            if not node:
                return
            
            num += str(node.val)
            if not node.left and not node.right:
                nums.append(int(num))

            dfs(node.left, num)
            dfs(node.right, num)

        
        dfs(root, '')
                
        return sum(nums)