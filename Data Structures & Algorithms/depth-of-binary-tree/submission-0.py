# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case
        if not root:
            return 0
        # Save recursive calls for each side
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        # return bigger side and add one to keep count of level 
        return max(left, right) + 1