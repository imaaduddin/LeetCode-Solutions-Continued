# Question Difficulty: Easy
# Question Number: 121
# Question URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# My Attempt:
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         new_list = []
        
#         for i in range(len(prices)):
#             value = prices[i + 1] - prices[i]
#             new_list.append(value)
#         return max(new_list)
            

# Correct Solution:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left is buying and right is selling
        l, r = 0, 1 
        maxP = 0
        
        while r < len(prices):
            # Profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP