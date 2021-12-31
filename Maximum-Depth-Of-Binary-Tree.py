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
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
        
#         level = 1
#         q = deque([root])
        
#         while q:
#             for i in range(len(q)):
#                 node = q.popleft()
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#             level += 1
#         return level


# Iterative DFS Solution:
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        
        stack = [[root, 1]]
        res = 1
        
        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res

                

        