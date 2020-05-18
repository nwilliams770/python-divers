def decompressRLElist(self, nums: List[int]) -> List[int]:
    decompressed = []
    for i in range(0, len(nums), 2):
        freq, val = nums[i], nums[i + 1]
        decompressed += [val] * freq
    return decompressed

# Note how we can control step size in our range function
# Not sure what a nested brute-force solution would be
# This requires one pass, O(n) time complexity, I think O(n) memory too?