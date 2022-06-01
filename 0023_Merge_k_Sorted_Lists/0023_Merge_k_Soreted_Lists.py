# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def concatenate_nodes(lists):
            tail = None
            top = None
            for i, node in enumerate(lists):
                head = node
                if not node:
                    continue
                if not top:
                    top = node
                if tail:
                    tail.next = head
                while node.next:
                    node = node.next
                tail = node
            return top

        def find_middle_node(node):
            slow = fast = node
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def merge(lnode, rnode):
            dummy = ListNode()
            node = dummy
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

        if not lists:
            return None

        head = concatenate_nodes(lists)
        return merge_sort(head)