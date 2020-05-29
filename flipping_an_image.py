from typing import List
import threading

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        row_size = len(A[0])

        for i in range(len(A)):
            # A[i] = self.invert_and_reverse(A[i], row_size)
            A[i] = self.flip2(A[i], row_size)

        return A

    def invert_and_reverse(self, arr: List[int], length: int) -> List[int]:
        result = []

        for i in reversed(range(length)):
            if arr[i] == 0:
                result.append(1)
            else:
                result.append(0)

        return result

    def flip2(self, arr: List[int], length: int) -> List[int]:
        inverted = [0 if (e == 1) else 1 for e in arr]
        self.reverse(inverted)
        return inverted

    def reverse(self, l) -> List[int]:
        for i in range(self.get_upper_bound(len(l))):
            temp = l[i]
            inverse_idx = self.get_inverse_idx(i, len(l))
            l[i] = l[inverse_idx]
            l[inverse_idx] = temp
        return l

    def get_upper_bound(self, n):
        return n // 2

    def get_inverse_idx(self, i, length):
        return length - i - 1

# Concurrency Solution
def flip_and_invert_image_with_threads(m: List[List[int]]) -> List[List[int]]:
    threads = []
    # for i, _ in enumerate(m):
    for i in range(len(m)):
        t_row = threading.Thread(target=_concurrent_reverse_invert_row, args=(m, i))
        t_row.start()
        threads.append(t_row)

    for thread in threads:
        thread.join()

    return m

def _concurrent_reverse_invert_row(m: List[List[int]], i: int):
        m[i] = [0 if (e == 1) else 1 for e in m[i]]
        m[i].reverse()



