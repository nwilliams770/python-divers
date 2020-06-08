class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return True

        violations = 0

        for i in range(len(nums) - 2):
            if nums[i] > nums[i + 1]:
                violations += 1

                if violations > 1:
                    return False

                if i != 0 and nums[i + 1] < nums[i - 1] and nums[i] > nums[i + 2]:
                    return False

        return violations + int(nums[-1] < nums[-2]) < 2