# Question Difficulty: Easy
# Question URL: https://leetcode.com/problems/same-tree/

# Convert the tree to a string
# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         if str(p) == str(q):
#             return True
#         else:
#             return False
        





class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
         if not p and not q:
                return True 
        if not p or not q or p.val != q.val:
            return False 
        
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))