# Question url: https://leetcode.com/problems/two-sum/

# Question difficulty is easy

# Solution from another user on LeetCode:
# Brute force solution running O(n^2) 
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            return[i, j]
return []


# Faster solution:
# Solution source: https://youtu.be/2uWRxgN1Sbo
# complementMap = dict()
            
# for i in range(len(nums)):
#     num = nums[i]
#     complement = target - num
#     if num in complementMap:
#         return[complementMap[num], i]
#     else:
#         complementMap[complement] = i


# Another solution:
# for i in range(len(nums) - 1):
#     for j in range(i + 1, len(nums)):
#         if nums[i] + nums[j] == target:
#             return([i, j])


# Another solution 
# seen = {}

# for i, num in enumerate(nums):
#     if target - num in seen:
#         return([seen[target - num], i])
#     elif num not in seen:
#         seen[num] = i