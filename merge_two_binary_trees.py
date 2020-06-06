from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def mergeTreesRecursive(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1

        t1.val += t2.val
        t1.left = self.mergeTreesRecursive(t1.left, t2.left)
        t1.right = self.mergeTreesRecursive(t1.right, t2.right)

        return t1

    def mergeTreesIterative(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        elif not t2:
            return t1

        stack = deque()
        stack.append([t1, t2])

        while stack:
            node1, node2 = stack.pop()

            if node2 == None:
                continue

            node1.val += node2.val

            if node1.left == None:
                node1.left = node2.left
            else:
                stack.append([node1.left, node2.left])

            if node1.right == None:
                node1.right = node2.right
            else:
                stack.append([node1.right, node2.right])

        return t1