# Question Difficulty: Easy
# Question URL: https://leetcode.com/problems/sqrtx/
# import math
# My Solution:
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         square_root = math.sqrt(x)
#         rounded = math.floor(square_root)
#         return rounded
        




# Another Solution:
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         import math
#         return int(math.sqrt(x))
        

# Babylonian Method (More Interesting Approach):
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            x
        else:
            x_n = 0.5 * x
            change = 1
            while change > 0.01:
                next_n = 0.5 * (x_n + x/x_n)
                change = abs(x_n-next_n)
                x_n = next_n
            return(int(x_n))
            

