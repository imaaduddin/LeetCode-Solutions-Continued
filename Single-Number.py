# Question Difficulty: Easy
# Question Number: 136
# Question URL: https://leetcode.com/problems/single-number/

# My Attempt:
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for n in range(len(nums)):
            if nums[n].count() > 1:
                return False
            else:
                return nums