import math

class Solution:
    def maximum69Number (self, num: int) -> int:
#       Space O(len(num)) // time O(len(num))
        num_digits = math.floor(math.log(num, 10)) + 1
#       We want to prioritize the higest value digit then go down

#       For each digit, from highest to lowest
        for i in reversed(range(num_digits)):
#           Get digit
            digit = (num // (10 ** i)) % 10
#           If digit is a 6
            if digit < 9:
#               Remove that val, then add it as if it were a 9
                return (num - 6 * 10 ** i) + (9 * 10 ** i)
#       If digit is already max val, return it
        return num