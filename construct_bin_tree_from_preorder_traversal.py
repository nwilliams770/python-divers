#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        root = TreeNode(val = preorder.pop(0))

        # split list into left children and right children
        left_l, right_l = self._split_list(root.val, preorder)

        # recursively construct left and right
        root.left = self.bstFromPreorder(left_l)
        root.right = self.bstFromPreorder(right_l)

        return root

    def _split_list(self, midpoint:int, l: List):
#       Can optimize for this by bin-searching l each time for split point
        left = [x for x in l if x < midpoint]
        right = [x for x in l if x > midpoint]
        return left, right