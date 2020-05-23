import math

class Solution:
    def maximum69Number (self, num: int) -> int:
        num_digits = math.floor(math.log(num, 10))
#       We want to prioritize the higest value digit then go down

#       For each digit, from highest to lowest
        for i in reversed(range(num_digits)):
            digit = (num // (10 ** i)) % 10
            if digit < 9:
                return (num - 6 * 10 ** i) + (9 * 10 ** i)
