# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Function to turn tree into list
        dummy = []
        tree_list = self.tree_to_list(root, dummy)

        return tree_list[k-1]

    def tree_to_list(self, root: Optional[TreeNode], nodes: List[int]) -> List[int]:
            if not root:
                return nodes
            self.tree_to_list(root.left, nodes)
            nodes.append(root.val)
            self.tree_to_list(root.right, nodes)

            return nodes
