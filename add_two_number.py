# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        solution_head = None
        solution_current_node = None
        solution_prev_node = None
        carryover = 0

        while True:
            # If both are None, break, we're done
            if l1 is None and l2 is None and not carryover:
                break

            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            node_sum = l1_val + l2_val + carryover
            carryover = node_sum // 10
            node_sum = node_sum % 10
            solution_current_node = ListNode(val=node_sum)

            if solution_prev_node:
                solution_prev_node.next = solution_current_node
            else:
                solution_head = solution_current_node

            solution_prev_node = solution_current_node

            # Check if l1 and l2 are not None before iterating to next node
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return solution_head
