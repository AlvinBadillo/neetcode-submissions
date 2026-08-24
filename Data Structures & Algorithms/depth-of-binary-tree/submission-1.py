# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        curr = root
        # so I think we need a var to store the result depth, then we want to make sure it gets updated acordinglly
        depth = 0 

        if curr is None:
            return 0
        
        # if we do have a node
        depth += max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        return depth
        