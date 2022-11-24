class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = self.merge_sort(nums1, nums2)
        length = len(merged)

        return merged[length//2] if length % 2 != 0 else ((merged[length//2 - 1] + merged[length//2]) / 2)

    def merge_sort(self, a, b):
        result = []
        i = 0
        j = 0

        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1

        result = result + a[i:] + b[j:]

        return result