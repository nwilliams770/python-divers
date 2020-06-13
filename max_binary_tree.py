# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        root_val, left_tree_nums, right_tree_nums = self._get_root_and_subtrees_vals(nums)
        root = TreeNode(val=root_val)
        root.left = self.constructMaximumBinaryTree(left_tree_nums)
        root.right = self.constructMaximumBinaryTree(right_tree_nums)

        return root

    def _get_root_and_subtrees_vals(self, nums):
        root = max(nums)
        root_idx = nums.index(root)
        left_tree_nums = nums[:root_idx]
        right_tree_nums = nums[root_idx + 1:]

        return root, left_tree_nums, right_tree_nums