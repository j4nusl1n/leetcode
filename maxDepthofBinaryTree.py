# https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.iterrate(root)
    
    def recur(self, node):
        if node is None:
            return 0

        left_depth = self.maxDepth(node.left)
        right_depth = self.maxDepth(node.right)

        max_depth = max(left_depth, right_depth)
        return 1 + max_depth
    
    def iterrate(self, node):
        if node is None:
            return 0
        
        next_level = [node]
        max_depth = 0
        while next_level:
            next_level = [
                child
                for n in next_level
                for child in (n.left, n.right)
                if child
            ]
            max_depth += 1
        
        return max_depth