class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest_nums = self._get_two_largest(nums)
        print(largest_nums)
        return (largest_nums[0] - 1) * (largest_nums[1] - 1)

    def _get_two_largest(sefl, arr):
        largest = arr[0] if arr[0] > arr[1] else arr[1]
        second_largest = arr[1] if arr[1] < arr[0] else arr[0]

        for el in arr[2:]:
            if el >= largest:
                second_largest = largest
                largest = el
            elif largest > el > second_largest:
                second_largest = el
        return (largest, second_largest)