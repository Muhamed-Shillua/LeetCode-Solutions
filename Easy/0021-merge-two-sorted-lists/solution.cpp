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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* Dummy = new ListNode(0);
        ListNode* Current = Dummy;

        while(list1 != nullptr && list2 != nullptr){
            if (list1->val <= list2->val){
                Current->next = list1;
                list1 = list1->next;
                Current = Current->next;
            }
            else{
                Current->next = list2;
                list2 = list2->next;
                Current = Current->next;
            }
        }
        if (list1 != nullptr) Current->next=list1;
        else Current->next=list2;

        return Dummy->next;
    }
};
