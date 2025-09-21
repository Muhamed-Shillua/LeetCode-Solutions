# Problem: Two Sum

- **LeetCode Link:** [Two Sum](https://leetcode.com/problems/two-sum/)
- **Difficulty:** Easy
- **Language:** C++

## Problem Description
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

## Approach
- Use a hash map (unordered_map in C++) to store each number and its index as we iterate through the array.
- For each number `nums[i]`, calculate the complement `target - nums[i]`.
- If the complement exists in the hash map, return the pair of indices.
- Otherwise, insert the current number into the hash map and continue.
- This ensures we only traverse the list once.

## Time Complexity
- **O(n)**, where n is the length of `nums`, since we do a single pass with constant-time lookups.

## Space Complexity
- **O(n)** for storing up to n elements in the hash map.

## Example
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] == 9, we return [0, 1]
```

## Notes / Edge Cases
- Each input has exactly one valid solution.
- Cannot use the same element twice.
- The order of indices in the output does not matter.

---
*Author: Muhamed Shillua*
