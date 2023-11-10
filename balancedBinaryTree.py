# https://leetcode.com/problems/balanced-binary-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) >= 0

    def height(self, node):
        if not node:
            return 0

        lh, rh = self.height(node.left), self.height(node.right)
        if lh == -1 or rh == -1:
            return -1
        elif abs(lh - rh) > 1:
            return -1
        else:
            return max(lh, rh) + 1
