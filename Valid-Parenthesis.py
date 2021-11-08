# LeetCode Easy
# Problem URL: https://leetcode.com/problems/valid-parentheses/

# class Solution:
#     def isValid(self, s: str) -> bool:
#         # Inner string replace method

#         replace = True
#         while replace:
#             start_length = len(s)
#             for inner in ["{}", "()", "[]"]:
#                 s = s.replace(inner, "")
#             if start_length == len(s):
#                 replace = False
#         return s == ""
        

# Faster solution
# class Solution:
#     def isValid(self, s: str) -> bool:
#         # Close the last seen opening symbol w/ stack
#         close_map = {"(":")", "{":"}", "[":"]"}
#         opens = []

#         for symbol in s:
#             if symbol in close_map.keys():
#                 opens.append(symbol)
#             elif opens == [] or symbol != close_map[opens.pop()]:
#                 return False
#         return opens == []



# Another solution:
# O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in close_to_open:
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
        
        