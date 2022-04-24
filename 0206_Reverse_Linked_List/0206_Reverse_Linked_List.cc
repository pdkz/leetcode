/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *current = head;
        ListNode *next = nullptr;
        ListNode *prev = nullptr;
        while(current != nullptr) {
            next = current->next;

            current->next = prev;

            prev = current;
            current = next;
            //printf("%d ", prev->val);
        }

        head = prev;

        return head;
    }

    ListNode* reverse_recursive(ListNode *p) {
        ListNode *head = nullptr;
        if (p == nullptr || p->next == nullptr) {
            head = p;
            return head;
        }
        head = reverse(p->next);
        ListNode *temp = p->next;
        temp->next = p;
        p->next = nullptr;
        return head;
    }
};
