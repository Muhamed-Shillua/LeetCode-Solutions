# Problem: Reverse Integer

- **LeetCode Link:** [Reverse Integer](https://leetcode.com/problems/reverse-integer/)
- **Difficulty:** Medium
- **Language:** C++

## Problem Description
Given a signed 32-bit integer `x`, return `x` with its digits reversed.  
If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2^31, 2^31 - 1]`, then return `0`.

## Approach
- Handle the sign of the number: if `x` is negative, remember the sign and work with its absolute value.
- Extract digits from the number using modulo (`x % 10`) and reduce `x` by dividing by 10.
- Before adding the new digit, check for overflow by comparing against `INT_MAX / 10`.
- If overflow would occur, return 0.
- Rebuild the reversed integer step by step.
- At the end, reapply the negative sign if necessary.

## Time Complexity
- **O(log n)**, where `n` is the value of `x`, since we process each digit once.

## Space Complexity
- **O(1)**, only a few variables are used.

## Example
```
Input: x = 123
Output: 321
```

## Notes / Edge Cases
- Return 0 if the reversed number overflows 32-bit signed integer range.
- Handle negative numbers correctly.
- Input `x = 0` should return 0.

---
*Author: Muhamed Shillua*
