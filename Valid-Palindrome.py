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
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         new_str = ""
        
#         for c in s:
#             if c.isalnum():
#                 new_str += c.lower()
        return new_str == new_str[::-1]
    

# NeetCode Solution 2:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def alphaNum(self, c):
            return (ord("A") <= ord(c) <= ord("Z") or ord("a") <= ord(c) <= ord("z") or ord("0") <= ord(c) <= ord("9")) 
    