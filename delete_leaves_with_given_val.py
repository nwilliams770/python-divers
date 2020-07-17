# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        entire_tree_pruned = self._prune_tree(root, None, "", target)

        if entire_tree_pruned:
            return None
        else:
            return root

    def _prune_tree(self, root: TreeNode, parent: TreeNode, position: str, target:int) -> TreeNode:
        if root == None:
            return

        self._prune_tree(root.left, root, "L", target)
        self._prune_tree(root.right, root, "R", target)

        if root.left == None and root.right == None and root.val == target:
            if position == "L":
                parent.left = None
            elif position == "R":
                parent.right = None
            elif not parent:
                return True