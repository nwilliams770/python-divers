class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []

        for idx, num in enumerate(nums):
            if num == target:
                result.append(idx)

        return [-1, -1] if len(result) == 0 else [result[0], result[-1]]