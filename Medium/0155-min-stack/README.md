# Problem: Min Stack

- **LeetCode Link:** [Min Stack](https://leetcode.com/problems/min-stack/)
- **Difficulty:** Medium
- **Language:** C++

## Problem Description
Design a stack that supports the following operations **in constant time**:  

1. `push(val)` – Push element `val` onto the stack.  
2. `pop()` – Removes the element on top of the stack.  
3. `top()` – Get the top element.  
4. `getMin()` – Retrieve the minimum element in the stack.
   
## Approach
Use **two stacks**:
1. `st` – main stack to store all elements.  
2. `minst` – stack to store the minimum at each level.  

- **Push:**  
  - Push `val` to `st`.  
  - Push `min(val, minst.top())` to `minst` (or `val` if empty).  
- **Pop:**  
  - Pop from both `st` and `minst`.  
- **Top:**  
  - Return `st.top()`.  
- **GetMin:**  
  - Return `minst.top()`. 

## Time Complexity
- All operations (`push`, `pop`, `top`, `getMin`) → **O(1)**  

## Space Complexity
- **O(n)** – two stacks storing `n` elements each.

## Example
```
MinStack* obj = new MinStack();
obj->push(-2);
obj->push(0);
obj->push(-3);
obj->getMin(); // returns -3
obj->pop();
obj->top(); // returns 0
obj->getMin(); // returns -2

```

## Notes / Edge Cases
- Multiple duplicate minimums are handled correctly.  
- Stack can be empty; calling `top()` or `getMin()` on empty stack is undefined.  
- Push negative and positive numbers.  

---
*Author: Muhamed Shillua*
