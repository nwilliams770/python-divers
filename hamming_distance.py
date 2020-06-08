class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num1 = self._int_to_bin(x)
        num2 = self._int_to_bin(y)
        num1, num2 = self._equalize_len(num1, num2)

        hamming_distance = 0

        for i in range(0, len(num1)):
            if num1[i] != num2[i]:
                hamming_distance += 1

        return hamming_distance


    def _int_to_bin(self, num):
        return bin(num)[2:]

    def _equalize_len(self, a, b):
        long = a if len(a) >= len(b) else b
        short = b if len(b) <= len(a) else a

        while len(short) < len(long):
            short = "0" + short

        return long, short