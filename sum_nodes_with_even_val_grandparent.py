from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        result = 0
        if root == None:
            return result

        queue = deque()
#       Add root to queue
#           node, parent, grandparent
        queue.append((root, None, None))

#       While queue is not empty
        while queue:
#           pop node from queue, along with parent/grandparent
            node, parent, grandparent = queue.popleft()

            if grandparent and grandparent.val % 2 == 0:
                result += node.val

#           Check for children, adding new lineage as well
            if node.left:
                queue.append((node.left, node, parent))

            if node.right:
                queue.append((node.right, node, parent))

        return result