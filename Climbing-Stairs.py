# Question Difficulty: Easy
# Question URL: https://leetcode.com/problems/climbing-stairs/

# Solution 1
class Solution:
    def climbStairs(self, n: int) -> int:
        path = {1: 1, 2: 2, 3: 3}

        for x in range(4, n+1):
            path[x] = path[x-1] + path[x-2]
        return path[n]