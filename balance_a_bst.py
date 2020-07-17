# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        vals = sorted(self._extract_tree_vals(root))
        return self._construct_balanced_bst(vals)

    def _construct_balanced_bst(self, vals: List[int]) -> TreeNode:
        if not vals:
            return

        mid_idx = len(vals) // 2
        root = TreeNode(vals[mid_idx])
        root.left = self._construct_balanced_bst(vals[:mid_idx])
        root.right = self._construct_balanced_bst(vals[mid_idx+1:])

        return root

    def _extract_tree_vals(self, root) -> List[int]:
        if root:
            return [root.val] + self._extract_tree_vals(root.left) + self._extract_tree_vals(root.right)
        else:
            return []