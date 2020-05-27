class Solution:
    def sumZero(self, n: int) -> List[int]:
#       Solution #1, Space O(n) // Time O(n)
        result = []

        if n % 2 != 0:
            result.append(0)

        for i in range(1, self.getUpperBound(n)):
            result.append(i)
            result.append(i * -1)

        return result

    # Better to have this in a helper function because then we can unit test it!
    def getUpperBound(self, n):
        return n // 2 + 1


    # Solution #2, Looks cool but constantly stitching and appending arrays is not as performant
        if n == 0:
            return []
        elif n % 2 == 0:
            return [n] + [-n] + self.sumZero(n - 2)
        else:
            return [0] + self.sumZero(n - 1)