# Question Difficulty: Easy
# Question URL: https://leetcode.com/problems/length-of-last-word/

# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         i, length = len(s) - 1, 0

#         while s[i] == " ":
#             i -= 1
#         while i >= 0 and s[i] != " ":
#             length += 1
#             i -= 1
#         return length
        
        
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:   
#         Another Solution (String split version):
#         if s.split():
#             return len(s.split()[-1])
#         return 0     
        
        
        


# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
        
#         Another Solution (String split version):
#         if s.split():
#             return len(s.split()[-1])
#         return 0
    
#         Another Method: Manual string length count
#         count = 0
#         for letter in s[::-1]:
#             if letter == " ":
#                 if count >= 1:
#                     return count
#             else:
#                 count += 1

            
        

