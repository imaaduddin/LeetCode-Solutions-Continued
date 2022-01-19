# Question Difficulty: Easy
# Question Number: 125
# Question URL: https://leetcode.com/problems/valid-palindrome/

# My Attempt
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         lower = s.lower()
#         no_space = lower.replace(" ", "")
#         remove_stuff = no_space.replace(",", "")
        
#         if remove_stuff == remove_stuff[::-1]:
#             return True
#         else:
#             return False


# NeetCode SOlution:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        