# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        result = self._search_tree(cloned, target)
        return result

    def _search_tree(self, root, target):
        if root == None:
            return None
        if root.val == target.val:
            return root
        else:
            a = self._search_tree(root.left, target)
            if a:
                return a
            b = self._search_tree(root.right, target)
            if b:
                return b