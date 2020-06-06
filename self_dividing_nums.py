import math
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []

        for i in range(left, right + 1):

#           if < 10, already self dividing and can add without computation
            if i < 10 or self._is_self_dividing_num(i):
                result.append(i)

        return result

    def _is_self_dividing_num(self, num):
        num_digits = self._get_num_digits(num)

        for i in range(num_digits):
            digit = (num // 10 ** i) % 10

            if digit == 0:
                return False
            elif num % digit != 0:
                return False

        return True

    def _get_num_digits(self, num):
        return math.floor(math.log(num, 10)) + 1