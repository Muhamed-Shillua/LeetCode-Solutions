# Problem: Palindrome Number

- **LeetCode Link:** [Palindrome Number](https://leetcode.com/problems/palindrome-number/)
- **Difficulty:** Medium
- **Language:** C++

## Problem Description
Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.  
A palindrome number reads the same backward as forward.

## Approach
- If `x` is negative, it cannot be a palindrome.
- If `x` ends with `0` but is not `0` itself, it cannot be a palindrome.
- Reverse half of the number instead of the whole number to avoid overflow:
  - Keep extracting the last digit (`x % 10`) and building a reversed half `y`.
  - Stop when the reversed half is greater than or equal to the remaining `x`.
- At the end, the number is a palindrome if:
  - `x == y` (even number of digits), or
  - `x == y / 10` (odd number of digits, ignoring the middle digit).

## Time Complexity
- **O(log n)**, since we process roughly half of the digits.

## Space Complexity
- **O(1)**, using only a few variables.

## Example
```
Input: x = 121
Output: true
Explanation: Reversing the digits gives 121, which is the same as the original number
```

## Notes / Edge Cases
- Negative numbers are never palindromes.
- Numbers ending with zero (except 0 itself) cannot be palindromes.
- Efficient approach since only half the digits are reversed.

---
*Author: Muhamed Shillua*
