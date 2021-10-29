
# Question url: https://leetcode.com/problems/palindrome-number/
# Difficulty is easy, question number 9 on LeetCode.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

# Solution not converting integer to string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reverse_num = 0
        digit = 0
        
        while(x // (10 ** digit) != 0):
            reverse_num = (reverse_num * 10) + (x // (10 ** digit) % 10)
            digit += 1
        return (x == reverse_num)