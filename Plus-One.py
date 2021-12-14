# Question Difficulty: Easy
# Question URL: https://leetcode.com/problems/plus-one/

# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         My attempt
#         for number in range(len(digits)):
#             if digits[number -1] >= 9:
#                 return digits.append(1, 0)
#             end = digits[number - 1] + 1
#             return end


        

        
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         digits = digits[::-1]
#         one, i = 1, 0

#         while one == 1:
#             if i < len(digits):
#                 if digits[i] == 9:
#                     digits[i] = 0
#                 else:
#                     digits[i] += 1
#                     one = 0
#             else:
#                 digits.append(1)
#                 one = 0
#             i += 1
#         return digits[::-1]
        
        

# Another Solution: 
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Method 1: Type conversion
        return [int(x) for x in str(int("".join([str(i) for i in digits])) + 1)]
