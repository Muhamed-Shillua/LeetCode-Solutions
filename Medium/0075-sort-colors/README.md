# Problem: Sort Colors

- **LeetCode Link:** [Sort Colors](https://leetcode.com/problems/sort-colors/)
- **Difficulty:** Medium
- **Language:** C++

## Problem Description
Given an array `nums` with `n` objects colored red, white, or blue (represented by integers `0`, `1`, and `2`), sort them **in-place** so that objects of the same color are adjacent, with the colors in the order red → white → blue.

You must solve this problem **without using the library's sort function**.

## Approach
### Selection Sort (current solution):
1. Iterate through the array.  
2. For each position `i`, find the smallest element in the unsorted portion.  
3. Swap it with `nums[i]`.  
4. Continue until the entire array is sorted.

This guarantees correctness but is **not optimal** for this problem.

### Optimal Approach (Dutch National Flag Algorithm – recommended):
- Use three pointers:  
  - `low` for 0s  
  - `mid` for 1s  
  - `high` for 2s  
- Traverse the array once and partition into 0s, 1s, and 2s.  
- This runs in **O(n)** time and **O(1)** space.
  
## Time Complexity
- **Current code (Selection Sort):** O(n²)  
- **Optimal solution:** O(n)
  
## Space Complexity
- **O(1)** – sorting is done in place.  

## Example
```
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Explanation: All 0s are placed first, then 1s, then 2s.
```

## Notes / Edge Cases
- Array length = 1 → already sorted.  
- All elements are the same (e.g., `[0,0,0]`).  
- Mixed distributions of 0s, 1s, and 2s.  
---
*Author: Muhamed Shillua*
