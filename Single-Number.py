# Question Difficulty: Easy
# Question Number: 136
# Question URL: https://leetcode.com/problems/single-number/

# My Attempt:
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         new_num = str(nums)
#         for n in range(len(new_num)):
#             if new_num[n].count() > 1:
#                 return False
#             else:
#                 return new_num


# DataDaft Solution:
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         counts = {}
#         for n in nums:
#             if n not in counts:
#                 counts[n] = 1
#             else:
#                 del counts[n]
#         return list(counts.keys())[0]
    

# NeetCode Solution:
