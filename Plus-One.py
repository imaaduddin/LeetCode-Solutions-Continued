# Question Difficulty: Easy
# Question URL: https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for number in range(len(digits)):
            if digits[number -1] >= 9:
                return digits.append(1, 0)
            end = digits[number - 1] + 1
            return end
