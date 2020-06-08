import math

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0 or x >= math.pow(2, 31) - 1 or x <= math.pow(-2, 31):
            return 0

        sign = 1 if x > 0 else -1
        num = abs(x)
        num_digits = self._get_num_digits(num)
        num_reversed = 0

        for i in reversed(range(num_digits)):
            digit = (num // 10 ** i) % 10
            new_place = 10 ** (num_digits - (i + 1))

            num_reversed += digit * new_place

        return num_reversed * sign

    def _get_num_digits(self, num):
        return math.floor(math.log(num, 10)) + 1