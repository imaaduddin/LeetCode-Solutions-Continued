# Question url: https://leetcode.com/problems/reverse-integer/

# Question difficulty is easy.

# Solution from a fellow LC member.
class Solution:
    def reverse(self, x: int) -> int:
        output = int(str(abs(x))[::-1])
        if output < 2**31:
            if x >= 0:
                return output
            else:
                return -output
        else:
            return 0


# Another solution from fellow LC member:
class Solution:
    def reverse(self, x):
        multiplier = 1
        ans = 0
        
        for i in str(x):
            if i.isalnum():
                ans += int(i) * multiplier
                multiplier *= 10
                
        if ans > pow(2, 31):
            return 0
        elif(x < 0):
            return ans * -1
        return ans


# Another solution:
class Solution:
    def reverse(self, x):
        sum = 0
        sign = 1
        if x < 0:
            sign = -1
            x = x * -1
        while x > 0:
            rem = x % 10
            sum = sum * 10 + rem
            x = x // 10
        if not -2147483648 < sum < 2147483647:
            return 0
        return sign * sum
    

# Solution from: https://youtu.be/HAgLH58IgJQ
import math
class Solution:
    def reverse(self, x):
        MIN = -2147483648
        MAX = 2147483648
        
        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if (res > MAX // 10 or (res == MAX // 10 and digit >= MAX % 10)):
                return 0
            if (res < MIN // 10 or (res == MIN // 10 and digit <= MIN % 10)):
                return 0
            res = (res * 10) + digit
        
        return res
    
# Another solution
class Solution:
    def reverse(self, x: int) -> int:
        output = int(str(abs(x))[::-1])
        if output < 2**31:
            if x >= 0:
                return output
            else:
                return -output
        else:
            return 0