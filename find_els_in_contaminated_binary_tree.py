# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.vals = []
        self.root = root

        self.recover_tree(self.root)

    def find(self, target: int) -> bool:
        return target in self.vals

    def recover_tree(self, root: TreeNode, root_val=0):
#       Base Case
        if root == None:
            return

        root.val = root_val
        self.vals.append(root_val)

        if root.left:
            root.left.val = 2 * root_val + 1
            self.recover_tree(root.left, root.left.val)

        if root.right:
            root.right.val = 2 * root_val + 2
            self.recover_tree(root.right, root.right.val)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)