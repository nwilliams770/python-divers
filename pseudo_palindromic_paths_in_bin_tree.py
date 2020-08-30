# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        result = 0
        paths = self.dfs(root, [], [])
        print("paths!", paths)
        for path in paths:
            if self.isPseudoPalindromic(path):
                result += 1

        return result

    def isPseudoPalindromic(self, p):
        frequency = {}
        for i in p:
            frequency[i] = frequency.get(i, 0) + 1

        odd_occurences = 0
        for v in frequency.values():
            if v % 2 != 0:
                odd_occurences += 1

            if odd_occurences > 1:
                return False
        return True

    def dfs(self, node, path, paths):
        if node is None:
            return

        if node.left is None and node.right is None:
            path.append(node.val)
            paths.append(path)
            return paths

        path.append(node.val)
        self.dfs(node.left, path.copy(), paths)
        self.dfs(node.right, path.copy(), paths)

        return paths
