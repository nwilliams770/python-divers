def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
    target_array = [None] * len(nums)

    for i in range(len(nums)):
        if target_array[index[i]] is None:
            target_array[index[i]] = nums[i]
        else:
            target_array.insert(index[i], nums[i])

    result = [el for el in target_array if el is not None]

    return result

# Doesn't feel great doing the filter but seems to work best
# Time complexity is approximately 2n, but O(n)
# Memory usage (space complexity?) is 3n, but O(n)
#   target_array of size n
#   if index list is all one index, we'd have a target array of size 2n - 1; target array             starts at size n and grow up to size 2n - 1
#   generating a new array in filter func, up to size n