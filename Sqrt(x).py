# Question Difficulty: Easy
# Question URL: https://leetcode.com/problems/sqrtx/
import math
# My Solution:
class Solution:
    def mySqrt(self, x: int) -> int:
        square_root = math.sqrt(x)
        rounded = math.floor(square_root)
        return rounded
        
        

