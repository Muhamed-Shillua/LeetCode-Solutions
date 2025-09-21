# Problem: Add Two Numbers

- **LeetCode Link:** [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)
- **Difficulty:** Medium
- **Language:** C++

## Problem Description
You are given two non-empty linked lists representing two non-negative integers.  
The digits are stored in reverse order, and each of their nodes contains a single digit.  
Add the two numbers and return the sum as a linked list. 

## Approach
- Use a dummy head node to simplify linked list construction.
- Traverse both linked lists simultaneously, adding corresponding digits along with any carry from the previous step.
- If one list is shorter, treat missing digits as 0.
- Create a new node for each digit of the sum (`sum % 10`) and update the carry (`sum / 10`).
- Continue until both lists are exhausted and there is no carry left.
- Return the linked list starting from `dummy->next`.

## Time Complexity
- **O(max(m, n))**, where m and n are the lengths of the two linked lists.

## Space Complexity
- **O(max(m, n))** for the output linked list.

## Example
```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: Output: [7,0,8]
Explanation: 342 + 465 = 807
```

## Notes / Edge Cases
- If one list is longer than the other, continue processing the remaining digits.
- If there is a carry at the end, add a new node for it.
- The input numbers are given in reverse order.

---
*Author: Muhamed Shillua*
