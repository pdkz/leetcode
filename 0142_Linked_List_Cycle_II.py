# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        slow = head
        fast = head
        while True:
            if fast is None or fast.next is None:
                return None

            fast = fast.next.next
            slow = slow.next
            
            if slow == fast:
                break
        
        fast = head
        while slow != fast:
            if slow is None or fast is None:
                return None
            slow = slow.next
            fast = fast.next
        return slow
