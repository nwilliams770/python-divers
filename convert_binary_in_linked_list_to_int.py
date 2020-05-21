# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary_str = ""
        node = head

        while node:
            binary_str += str(node.val)
            node = node.next

        return int(binary_str, 2)