/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* Dummy = new ListNode(0);
        ListNode* Current = Dummy;
        int Carry = 0;
        while(l1 != nullptr || l2 != nullptr || Carry != 0){
            int x = (l1 != nullptr) ? l1->val : 0;
            int y = (l2 != nullptr) ? l2->val : 0;
            int Sum = x+y+Carry;
            int Digit = Sum %10;
            Carry = Sum/10;
            Current->next = new ListNode(Digit);
            Current = Current->next;

            if(l1 != nullptr) l1 = l1->next;
            if(l2 != nullptr) l2 = l2->next;
        }
        return Dummy->next;
    }
};