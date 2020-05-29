class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        result_not_sorted_by_ascending = sorted(A, key=lambda x: x % 2)
        result = sorted(A, key=lambda x: [x % 2, x])
#       returns a list, which when sorted, will first sort by first el, then by second
#       [[0,2], [0,4],[0,6],  [0,8]]

#       Brute Force Approach
        result = []
        for num in A:
            if num % 2 == 0:
                result.insert(0, num)
            else:
                result.append(num)
        return result