# Question URL: https://leetcode.com/problems/implement-strstr/
# Question difficulty: Easy

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        position = haystack.index(needle)
        return position

        if position == False:
            return -1
        
        if haystack and needle == "":
            return 0