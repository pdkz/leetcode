# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev_node = dummy
        for i in range(left-1):
            prev_node = prev_node.next

        curr_node = prev_node.next
        for i in range(right-left):
            next_node = curr_node.next
            curr_node.next = next_node.next
            next_node.next = prev_node.next
            prev_node.next = next_node
            #print(prev_node.val, curr_node.val, next_node.val)

        return dummy.next