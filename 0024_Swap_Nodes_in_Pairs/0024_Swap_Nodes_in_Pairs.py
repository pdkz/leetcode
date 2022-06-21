# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(next=head)
        prev, curr = dummy, head

        while curr and curr.next:
            post = curr.next
            if post:
                curr.next = curr.next.next
                post.next = curr
                prev.next = post
            else:
                curr.next = None
            prev = curr
            curr = curr.next
        return dummy.next