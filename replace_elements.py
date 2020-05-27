class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
#       Time O(len(arr)) // Space O(1)
#       Our max el might be last one, so grab it before replacing it with -1
        max = arr[-1]
        arr[-1] = -1

#        Starting from 2nd to last el
        for i in reversed(range(len(arr) - 1)):
            temp = arr[i]

#           If el is less than max, set to to max
            if temp < max:
                arr[i] = max
#           Else we've found a new max, since we are replacing each el with
#           rightmost max el, REPLACE it with old max, then set our new max
            else:
                arr[i] = max
                max = temp

        return arr