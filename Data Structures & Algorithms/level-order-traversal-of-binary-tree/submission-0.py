# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        lvl = 0
        return self.helper(root, result, lvl)
    def helper(self, root: Optional[TreeNode], result: List[List[int]], lvl):
        if root is None:
            return result
        if lvl == len(result):
            result.append([])
        result[lvl].append(root.val)
        self.helper(root.left, result, lvl + 1)
        self.helper(root.right, result, lvl + 1)
        return result