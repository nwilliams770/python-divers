# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum_to_date = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        if root.right:
            self.bstToGst(root.right)

        self.sum_to_date += root.val
        root.val = self.sum_to_date

        if root.left:
            self.bstToGst(root.left)

        return root
