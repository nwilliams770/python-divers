from collections import deque

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        # One-liner
        # return sorted(num * num for num in A)

#       Maintain two pointers, one at front and one at back
        i, j = 0, len(A) - 1
#       Initialize solution of len(A)
        squares = [0] * len(A)

        while True:
#           We want to fill our solution from right to left, largest to smallest
#               So whatever abs val is higher, e.g. the largest square
#               We can calc the position in the array it should be at with our two pointers
#                   Then add and decrease our pointers as appropriate to continue iterating
            if abs(A[i]) > abs(A[j]):
                squares[j - i] = A[i] * A[i]
                i += 1
            else:
                squares[j - i] = A[j] * A[j]
                j -= 1

#           If our pointers have met, then break
            if i >= j:
                break

        return squares

    def sorted_squares_deque(self, A: List[int]) -> List[int]:
        result = deque()
        i, j = 0, len(A) - 1

        while i <= j:
            if abs(A[i]) > abs(A[j]):
                result.appendleft(A[i] * A[i])
                i += 1
            else:
                result.appendleft(A[j] * A[j])
                j -= 1

        return list(result)