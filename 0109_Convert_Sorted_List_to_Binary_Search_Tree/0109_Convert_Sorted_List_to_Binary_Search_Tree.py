# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def dfs(nums, lo, hi):
            if lo > hi:
                return
            mid = (lo+hi) // 2
            root = TreeNode(nums[mid])
            root.left = dfs(nums, lo, mid-1)
            root.right = dfs(nums, mid+1, hi)
            return root

        sorted_list = []
        node = head
        while node:
            sorted_list.append(node.val)
            node = node.next

        return dfs(sorted_list, 0, len(sorted_list)-1)