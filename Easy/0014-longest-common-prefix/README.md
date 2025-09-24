# Problem: Longest Common Prefix

- **LeetCode Link:** [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)
- **Difficulty:** Easy
- **Language:** C++

## Problem Description
Write a function to find the longest common prefix string amongst an array of strings.  
If there is no common prefix, return an empty string `""`.

## Approach
1. Assume the first string is the prefix (`pre = strs[0]`).  
2. For each string in the array:
   - While the string does not start with `pre`, reduce `pre` by removing its last character.  
   - If `pre` becomes empty → return `""`.  
3. After processing all strings, `pre` will hold the longest common prefix.

This works because we progressively shrink the prefix until it matches all strings.

## Time Complexity
- **O(n * m)**  
  - `n`: number of strings  
  - `m`: average length of the strings  
  Each mismatch reduces prefix length at most once per character.

## Space Complexity
- **O(1)** – only uses a few extra variables.

## Example
```
Input: ["flower","flow","flight"]
Output: "fl"
Explanation: The longest common prefix among all strings is "fl".
```

## Notes / Edge Cases
- If the list is empty → return `""`.
- If only one string → return it directly.
- No common prefix → return `""`.

---
*Author: Muhamed Shillua*
