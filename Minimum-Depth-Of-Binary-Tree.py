# Question DIfficulty: Easy (111)
# Question URL: https://leetcode.com/problems/minimum-depth-of-binary-tree/

# DFS
# class Solution:
#     def minDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
        
#         self.small = float("inf")

#         def dfs(node, num):
#             if not node:
#                 return
#             if not node.left and not node.right:
#                 self.small = min(self.small, num)
            
#             dfs(node.left, num + 1)
#             dfs(node.right, num + 1)
        
#         dfs(root, 1)

#         return self.small


# BFS
# class Solution:
#     def minDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
        
#         q = deque([(root, 1)])

#         while q:
#             cand, num = q.popleft()
#             if not cand.left and not cand.right:
#                 return num
#             if cand.left:
#                 q.append((cand.left, num + 1))
#             if cand.right:
#                 q.append((cand.right, num + 1))
#         return -1

# DFS
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1
        
        if not root.right and root.left:
            return 1 + self.minDepth(root.left)

        if not root.left and root.right:
            return 1 + self.minDepth(root.right)
        
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))