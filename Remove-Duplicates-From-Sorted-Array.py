# Question Difficulty: Easy
# Question URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # index = 0
        # for i in range(len(nums)):
        #     if nums[i] != nums[i + 1]:
        #         nums[index + 1] = nums[i + 1]
        # return index
    
        if len(nums) == 0:
            return 0
        
        index = 0
        
        for i in range(len(nums)):
            if nums[index] != nums[i]:
                index += 1
                nums[index] = nums[i]
        return index + 1