# Question Difficulty: Easy
# Question URL: https://leetcode.com/problems/path-sum/
# Question Number: 112

# ALmost always in Tree problems recursion should be used

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        
        
        
        