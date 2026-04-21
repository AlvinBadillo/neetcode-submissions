# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Set up base cases
        # If they are the same check if they are null, if they are both null we reach the end of the tree so return true
        if not p and not q:
            return True
        # Check if the nodes are the same, if they arent, return false
        if p is None or q is None or p.val != q.val:
            return False
        # If they are not null, go to the next node
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)