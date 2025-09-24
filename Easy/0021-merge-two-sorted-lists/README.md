# Problem: Merge Two Sorted Lists

- **LeetCode Link:** [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
- **Difficulty:** Easy
- **Language:** C++

## Problem Description
You are given the heads of two sorted linked lists `list1` and `list2`.  
Merge the two lists into a single sorted linked list and return the head of the merged list.  

The merged list should be made by splicing together the nodes of the first two lists.

## Approach
1. Create a **dummy node** to simplify edge cases.  
2. Use a pointer `Current` starting at the dummy node.  
3. While both lists are non-empty:
   - Compare `list1->val` and `list2->val`.  
   - Attach the smaller node to `Current->next`.  
   - Move the pointer (`list1` or `list2`) forward.  
   - Move `Current` forward.  
4. When one list becomes empty, attach the remainder of the other list.  
5. Return `Dummy->next` (skipping the dummy node).
This guarantees that the merged list remains sorted without creating new nodes.

## Time Complexity
- **O(n + m)** – where `n` and `m` are the lengths of the two lists.  

## Space Complexity
- **O(1)** – in-place merging, only using a few extra pointers.  

## Example
```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Explanation: Merge step by step keeps order.
```

## Notes / Edge Cases
- One or both lists empty.  
- Lists with duplicate values.  
- Lists of unequal length.
  
---
*Author: Muhamed Shillua*
