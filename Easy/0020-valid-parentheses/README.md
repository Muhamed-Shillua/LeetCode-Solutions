# Problem: Valid Parentheses

- **LeetCode Link:** [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
- **Difficulty:** Easy
- **Language:** C++

## Problem Description
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine if the input string is valid.  
A string is valid if:  
1. Open brackets are closed by the same type of brackets.  
2. Open brackets are closed in the correct order.  

## Approach
1. Use a **stack** to keep track of opening brackets.  
2. Traverse each character in the string:
   - If it's an opening bracket → push it to the stack.  
   - If it's a closing bracket → check if the stack is not empty and its top matches the corresponding opening bracket.  
     - If not, return `false`.  
     - If yes, pop the top.  
3. At the end, if the stack is empty → return `true`, otherwise `false`.

This ensures proper matching and correct ordering of brackets.

## Time Complexity
- **O(n)** – each character is processed once.  

## Space Complexity
- **O(n)** – stack may hold all opening brackets in the worst case.  

## Example
```
Input: s = "()[]{}"
Output: true
Explanation: Each bracket is properly matched.
```

## Notes / Edge Cases
- Empty string → valid (returns `true`).  
- Single character → always invalid.  
- Must handle mixed nested cases like `"({[]})"`.  

---
*Author: Muhamed Shillua*
