# Question Difficulty: Easy
# Question URL: https://leetcode.com/problems/symmetric-tree/

# Recursive Solution
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True 
        return self.is_Mirror(root, root)
    def is_Mirror(self, left, right):
        if left == None and right == None:
            return True
        elif left == None or right == None:
            return False
        else:
            return left.val == right.val and self.is_Mirror(left.left, right.right) and self.is_Mirror(left.right, right.left)