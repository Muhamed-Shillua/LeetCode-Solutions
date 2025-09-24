# Problem: Roman to Integer

- **LeetCode Link:** [Roman to Integer](https://leetcode.com/problems/roman-to-integer/)
- **Difficulty:** Easy
- **Language:** C++

## Problem Description
Given a Roman numeral string `s`, convert it into an integer.  
Roman numerals are represented by seven symbols:
I -> 1, V -> 5, X -> 10, L -> 50, C -> 100, D -> 500, M -> 1000

Rules:
  - Normally, symbols are added (e.g., `VI = 5 + 1 = 6`).
  - If a smaller value precedes a larger one, it is subtracted (e.g., `IV = 5 - 1 = 4`).

## Approach
1. Use an **unordered_map** to store Roman numeral characters and their integer values.
2. Traverse the string from left to right:
   - If the current value is smaller than the next value → subtract it.  
   - Otherwise → add it.  
3. The final result is the converted integer.

## Time Complexity
- **O(n)** – where `n` is the length of the input string.
  
## Space Complexity
- **O(1)** – the map size is constant (7 Roman symbols).

## Example
```
Input: "MCMXCIV"
Output: 1994
Explanation: M (1000) + CM (900) + XC (90) + IV (4) = 1994
```

## Notes / Edge Cases
- Smallest input: `"I"` → `1`
- Handles subtractive notation correctly (`IV = 4`, `IX = 9`, etc.)
- No invalid Roman numeral inputs are given.

---
*Author: Muhamed Shillua*
