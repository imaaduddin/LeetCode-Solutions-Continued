# Question Difficulty: Easy
# Question Number: 121
# Question URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        new_list = []
        
        for i in range(len(prices)):
            value = prices[i + 1] - prices[i]
            new_list.append(value)
        return max(new_list)
            
