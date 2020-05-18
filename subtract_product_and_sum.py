import math
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        num_digits = math.floor(math.log(n, 10)) + 1
        digits_product = 1
        digits_sum = 0

        for i in range(num_digits):
            digit = (n // (10 ** i)) % 10
            digits_product *= digit
            digits_sum += digit

        return digits_product - digits_sum

# Brute-force/obvious approach: Cast to a str, split it, iterate through and cast back to int;
# add/multiplying to get sum/product
# Time complexity is contingent upon length of n, casting back and forth adds too

# Math hack: Calc num digits, 10 to the what power equals n (+ 1 for ones-place);
# Iterate num_digits times, capturing each digit and add/multiply it
# O(n) but no casting!

