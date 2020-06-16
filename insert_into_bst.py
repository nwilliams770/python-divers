# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            root = TreeNode(val=val)
        else:
            if root.val < val:
                if root.right is None:
                    root.right = TreeNode(val=val)
                else:
                    self.insertIntoBST(root.right, val)
            else:
                if root.left is None:
                    root.left = TreeNode(val=val)
                else:
                    self.insertIntoBST(root.left, val)
        return root