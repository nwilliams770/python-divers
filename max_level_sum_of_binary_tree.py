# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level_sums = {}
        self._sum_levels(root, 1, level_sums)
        levels = list(level_sums.keys())
        sums = list(level_sums.values())

        return levels[sums.index(max(sums))]


    def _sum_levels(self, root: TreeNode, level: int, level_sums: dict):
        if root is None:
            return

        level_sums[level] = level_sums.get(level, 0) + root.val

        self._sum_levels(root.left, level + 1, level_sums)
        self._sum_levels(root.right, level + 1, level_sums)


