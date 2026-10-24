# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        seen = []
        def appendstuff(node):
            if not node:
                return
            appendstuff(node.left)
            seen.append(node.val)
            appendstuff(node.right)
        appendstuff(root) 
        print(seen)
        return seen[k-1]
        