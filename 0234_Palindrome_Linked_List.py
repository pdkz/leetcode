# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nums = []
        node = head
        while(node != None):
            nums.append(node.val)            
            node = node.next
            
        l = len(nums)
        m = l // 2
        for i in range(m):
            if nums[i] != nums[l-i-1]:
                return False
        return True
