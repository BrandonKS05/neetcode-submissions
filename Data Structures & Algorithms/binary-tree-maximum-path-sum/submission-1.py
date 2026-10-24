# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.best = float('-inf')

        def dfs(node):
            if not node:
                return 0

            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            path_through = node.val + left_gain + right_gain
            self.best = max(self.best, path_through)

            # what we return upward: node can only extend ONE branch
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.best   