class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        nums = list(range(lo, hi+1))
        powers = [None] * len(nums)

        for i, num in enumerate(nums):
            powers[i] = self._get_power(num)

        nums_pows = sorted(zip(powers, nums))


        return nums_pows[k - 1][1]



    def _get_power(self, x):
        power = 0
        while True:
            if x % 2 == 0:
                x /= 2
                power += 1
            else:
                x = 3 * x + 1
                power += 1

            if x == 1:
                break

        return power