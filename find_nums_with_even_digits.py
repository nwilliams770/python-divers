import math

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_digit_count = 0
        for num in nums:
            if self.calc_num_digits(num) % 2 == 0:
                even_digit_count += 1
        return even_digit_count

    def calc_num_digits(self, num):
        return math.floor(math.log(num, 10)) + 1

# Brute force:
    # Iterate through list, for each item
        # cast to str, split, count each el, return count
    # if count % 2 == 0, add to even_digit_count
    # What is time complexity here? For each num in nums, we have to traverse its entire length
    # What is local variable space like? We have to create an array for each num in nums

# Mathy way:
    # Iterate through list, logarithmically getting digit count, adding to even_digit_count if its even
    # O(n) time complexity
    # O(1) local variable space