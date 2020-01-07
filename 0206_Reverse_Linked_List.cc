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
};
