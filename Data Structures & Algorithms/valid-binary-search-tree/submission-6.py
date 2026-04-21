# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Perform in-order traversal of tree annd making it a list
        # At the end iterate the list and make sure its sorted
        tree_list = []
        tree_list = self.tree_to_list(root, tree_list)

        if len(tree_list) == 1:
            return True
        
        for i in range(len(tree_list)-1):
            if tree_list[i] >= tree_list[i+1]:
                return False
        return True
    def tree_to_list(self, root: Optional[TreeNode], tree_node: List[int]) -> List[int]:
        # Perform in order traversal
        if root is None:
            return tree_node
        self.tree_to_list(root.left, tree_node)
        tree_node.append(root.val)
        self.tree_to_list(root.right, tree_node)
        return tree_node
