# Question Difficulty: Easy
# Question URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Recursive Solution
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         return (1 + max(self.maxDepth(root.left), self.maxDepth(root.right)))
    
    

# Another Recursive Solution 
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# Iterative BFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        level = 1
        q = deque([root])
        while q:
            for i in range(len(q)):
                q.popleft()