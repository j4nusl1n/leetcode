# https://leetcode.com/problems/invert-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.iterative(root)

    def recursive(self, root):
        if root is None:
            return root
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root

    def iterative(self, root):
        cur = root
        stk = []
        traversed = set()
        traversed.add(id(None))
        while cur or stk:
            if id(cur.left) in traversed and id(cur.right) in traversed:
                cur.left, cur.right = cur.right, cur.left
                traversed.add(id(cur))
                if stk:
                    cur = stk.pop()
                else:
                    break
            else:
                if cur.left and id(cur.left) not in traversed:
                    stk.append(cur)
                    cur = cur.left
                elif cur.right and id(cur.right) not in traversed:
                    stk.append(cur)
                    cur = cur.right

        return root
