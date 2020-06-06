class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        seen_nums = set()

        for num in A:
            if num in seen_nums:
                return num
            else:
                seen_nums.add(num)