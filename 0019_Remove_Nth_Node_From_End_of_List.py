# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
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