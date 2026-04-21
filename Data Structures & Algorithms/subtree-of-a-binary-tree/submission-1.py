# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
      # Set up base cases
        # If we reached the end of the root tree, return False
        if root is None:
            return False
        # If not, check if val of root is the same as subRoot
        # If it is, call sameTree on the root and subtree
        if self.sameTree(root, subRoot):
            return True
        # Iterate tree 
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If we reached the end of the tree it means they are the same
        if p is None and q is None:
            return True
        # Comapre nodes, if they are differnt return False
        if p is None or q is None or p.val != q.val:
            return False
        # Set up recursive call,
        return self.sameTree(p.right, q.right) and self.sameTree(p.left, q.left)