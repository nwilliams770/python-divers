# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        good_nodes = []
        self._find_good_nodes(root, good_nodes, root.val)

        return len(good_nodes)


    def _find_good_nodes(self, root, good_nodes, highest_val_on_path):
        if root is None:
            return

        if root.val >= highest_val_on_path:
            good_nodes.append(root)
            self._find_good_nodes(root.left, good_nodes, root.val)
            self._find_good_nodes(root.right, good_nodes, root.val)
        else:
            self._find_good_nodes(root.left, good_nodes, highest_val_on_path)
            self._find_good_nodes(root.right, good_nodes, highest_val_on_path)

