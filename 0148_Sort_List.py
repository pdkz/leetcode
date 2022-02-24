# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def find_middle_node(begin):
            fast = slow = begin
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            return slow

        def merge(lnode, rnode):
            dummy = node = ListNode()
            while lnode and rnode:
                if lnode.val < rnode.val:
                    node.next = lnode
                    lnode = lnode.next
                else:
                    node.next = rnode
                    rnode = rnode.next
                node = node.next
            node.next = lnode if lnode else rnode
            return dummy.next
            
        def merge_sort(lnode):
            if not lnode or not lnode.next:
                return lnode
            mid = find_middle_node(lnode)
            
            rnode = mid.next
            mid.next = None
            
            lnodes = merge_sort(lnode)
            rnodes = merge_sort(rnode)
            
            return merge(lnodes, rnodes)
        return merge_sort(head)