# Problem: Delete Node in a Linked List

- **LeetCode Link:** [Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/)
- **Difficulty:** Medium
- **Language:** C++

## Problem Description
Write a function to **delete a node** (except the tail) in a singly linked list, given **only access to that node**.  

You are **not given access to the head of the list**.

## Approach
1. Copy the value from the **next node** into the current node.  
2. Update the current node's `next` pointer to skip the next node:  
   ```cpp
   node->val = node->next->val;
   node->next = node->next->next;
This effectively "deletes" the node without needing the head pointer.

## Time Complexity
O(1) – only a few pointer operations.

## Space Complexity
O(1) – no extra memory used.

## Example
```
Input: linked list 4 -> 5 -> 1 -> 9, node = 5
After calling deleteNode(node): linked list becomes 4 -> 1 -> 9

```

## Notes / Edge Cases
- Cannot delete the tail node.
- Only works if the node to delete is guaranteed not to be the last node.
- The solution modifies the list in place.
---
*Author: Muhamed Shillua*
