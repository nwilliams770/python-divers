import math

class Solution:
    def countBits(self, num: int) -> List[int]:
        counted_1s = []
        for i in range(0, num + 1):
            counted_1s.append(self._count_binary_1s(i))

        return counted_1s

    def _count_binary_1s(self, num):
        return bin(num).count('1')

    def _count_binary_1s_manually2(self, num):
        count = 0
        while num:
            count += num & 1
            num >>= 1
        return count

    def _count_binary_1s_manually(self, num):
        if num <= 0:
            return 0
        elif num == 1:
            return 1
        else:
            counted_1s = 0
            while True:
                num = num - 2 ** math.floor(math.log(num, 2))
                counted_1s += 1

                if num <= 1:
                    counted_1s += 1 if num == 1 else 0
                    break

        return counted_1s