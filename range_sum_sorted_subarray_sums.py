class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = self._generate_sub_array_sums(nums)

        return sum(sums[left - 1:right])


    def _generate_sub_array_sums(self, nums: List[int]):
        sums = []

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums) + 1):
                sums.append(sum(nums[i:j]))

        sums.sort()
        return sums