class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dups = []

        for i in range(len(nums)):
            if nums[abs(nums[i])-1] > 0:
                nums[abs(nums[i])-1] *= -1
            else:
                dups.append(abs(nums[i]))
        return dups