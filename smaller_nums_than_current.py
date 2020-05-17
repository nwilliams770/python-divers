    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)

        return map(lambda x: sorted_nums.index(x), nums)

# Brute force:
# - While iterating, given nums[i], iterate through all other elements,
# counting how many are less than
# - Two for loops, O(n ** 2)

# Lower time complexity:
# - In a sorted list (ascending), the index, i, of nums[i] corresponds to how many other elements
# are less than it (this does not hold true for duplicates)
# - Sort nums and store in new list (original input must be maintained for ordering of output);
# From original list, generate new one with index of sorted_nums list; index() grabs index of
# first occurence so this addresses duplicate problem
# - Longest operation is sorted() O(n log n); time complexity is O(n log n + n)

