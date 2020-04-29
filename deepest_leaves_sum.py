# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        # Solution 1
        max_depth = self.find_max_depth(root)
        return self.count_if_at_depth(root, target_depth = max_depth)

        # Solution 2
        tiered_tree = self.divide_by_tier(root)
        return sum(tiered_tree[max(tiered_tree.keys())])


# Solution 2 (more memory > less time):
# - recursively traverse the tree, storing every val at a given tier
# - get sum of values at highest tier (max depth)

    def divide_by_tier(self, root, current_depth=1, tier_tree={}):
        if root == None:
            return

        tier_tree.setdefault(current_depth, []).append(root.val)

        self.divide_by_tier(root.left, current_depth + 1, tier_tree)
        self.divide_by_tier(root.right, current_depth + 1, tier_tree)

        return tier_tree

# Solution 1 (more time > less memory):
# - recursively traverse get the max depth of the tree
# - recursively re-traverse the tree, only extracting values at target depth and summing them
    def count_if_at_depth(self, root, target_depth, current_depth=1):
        if root == None:
            return 0

        if current_depth == target_depth:
            return root.val
        else:
            leftSum = self.count_if_at_depth(root.left, target_depth, current_depth + 1)
            rightSum = self.count_if_at_depth(root.right, target_depth, current_depth + 1)
            return leftSum + rightSum


    def find_max_depth(self, root):
        if root == None:
            return 0

        leftDepth = self.find_max_depth(root.left)
        rightDepth = self.find_max_depth(root.right)

        return 1 + max(leftDepth, rightDepth)