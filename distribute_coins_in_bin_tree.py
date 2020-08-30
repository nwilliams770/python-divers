# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result= 0
    def distributeCoins(self, root: TreeNode) -> int:
        self.dfs(root)

        return self.result


    def dfs(self, node):
        if not node:
            return 0

        l, r = self.dfs(node.left), self.dfs(node.right)

        self.result += abs(l) + abs(r)

        return node.val + l + r - 1