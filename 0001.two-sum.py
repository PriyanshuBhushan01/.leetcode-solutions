"""
Leetcode #1 - two sum
Difficulty: Easy
Topic: Array, Hash map

Approach:
store each number and its index in a dictionary. For each number, check wheather target - number has already appeared.

Time complexity: o(n)
Space complexity: o(n)
"""
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     n = len(nums)
     hash_map={}
     for i in range(n):
        remaining=target-nums[i]
        if remaining in hash_map:
            return [hash_map[remaining],i]
        hash_map[nums[i]]=i
# @lc code=end

