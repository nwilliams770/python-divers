# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        vals = []
        r1_els = self._get_els_from_bst(root1, vals)
        r2_els = self._get_els_from_bst(root2, vals)

        vals.sort()
        return vals

    def _get_els_from_bst(self, root, l):
        if root is None:
            return l
        else:
            l.append(root.val)
            self._get_els_from_bst(root.left, l)
            self._get_els_from_bst(root.right, l)

        return l
