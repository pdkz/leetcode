# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd_1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        if not head.next:
            head = None
            return head

        p = head
        q = head
        
        for i in range(n - 1):
            # 2つめのポインタqを先頭からN番目のノードまで移動させる
            if not q.next:
                break
            q = q.next

        while p.next and q.next:
            # ポインタqが末尾に到達したとき,ポインタpは末尾からN番目のノードに到達
            prev = p
            p = p.next
            q = q.next
        
        if p == head:
            # pが先頭ノード
            head = p.next
        else:
            prev.next = p.next
        
        return head

    def removeNthFromEnd_2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        p = dummy
        q = dummy
        
        for i in range(1, n+2):
            p = p.next
            
        while p:
            p = p.next
            q = q.next
        
        q.next = q.next.next

        return dummy.next